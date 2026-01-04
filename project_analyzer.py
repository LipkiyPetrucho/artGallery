import os
import json
import argparse
from typing import Dict, List, Optional


def get_file_info(file_path: str, include_content: bool = True) -> Optional[Dict]:
    """Получает информацию о файле и его содержимое (если требуется)."""
    try:
        file_info = {
            "path": file_path,
            "type": "file",
            "size": os.path.getsize(file_path),
            "extension": os.path.splitext(file_path)[1].lower(),
        }

        if include_content:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_info["content"] = f.read()
            except UnicodeDecodeError:
                # Пропускаем бинарные файлы
                return None
            except Exception as e:
                file_info["content"] = f"<ERROR READING FILE: {str(e)}>"

        return file_info
    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}")
        return None


def scan_project(directory: str, include_content: bool = True,
                 exclude_dirs: List[str] = None, exclude_exts: List[str] = None) -> Dict:
    """Рекурсивно сканирует проект и возвращает его структуру."""
    if exclude_dirs is None:
        exclude_dirs = ['.git', '__pycache__', 'node_modules', 'venv', '.idea', '.vscode']
    if exclude_exts is None:
        exclude_exts = ['.pyc', '.pyo', '.pyd', '.so', '.dll', '.exe', '.jpg', '.png']

    project_structure = {
        "name": os.path.basename(directory),
        "path": directory,
        "type": "directory",
        "children": []
    }

    try:
        items = os.listdir(directory)
    except Exception as e:
        print(f"Error reading directory {directory}: {str(e)}")
        return project_structure

    for item in items:
        item_path = os.path.join(directory, item)

        if os.path.isdir(item_path):
            if item in exclude_dirs:
                continue
            dir_info = scan_project(item_path, include_content, exclude_dirs, exclude_exts)
            project_structure["children"].append(dir_info)
        else:
            if any(item.endswith(ext) for ext in exclude_exts):
                continue
            file_info = get_file_info(item_path, include_content)
            if file_info:
                project_structure["children"].append(file_info)

    return project_structure


def save_project_structure(structure: Dict, output_file: str) -> None:
    """Сохраняет структуру проекта в JSON-файл."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(structure, f, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(description='Анализатор структуры проекта')
    parser.add_argument('project_path', type=str, help='Путь к проекту')
    parser.add_argument('output_file', type=str, help='Файл для сохранения результатов')
    parser.add_argument('--no-content', action='store_true', help='Не включать содержимое файлов')
    args = parser.parse_args()

    print(f"Сканирование проекта: {args.project_path}")
    structure = scan_project(args.project_path, not args.no_content)
    save_project_structure(structure, args.output_file)
    print(f"Результаты сохранены в: {args.output_file}")


if __name__ == "__main__":
    main()