import {placeOnWallComponent, wallFromFloorComponent} from './wall-from-floor.js'
AFRAME.registerComponent('place-on-wall',  placeOnWallComponent)
AFRAME.registerComponent('wall-from-floor', wallFromFloorComponent)

// вытаскиваем url картинки из query (?img=…)
const params = new URLSearchParams(window.location.search)
window.PAINTING_IMG = params.get('img')      // сделаем глобальной
