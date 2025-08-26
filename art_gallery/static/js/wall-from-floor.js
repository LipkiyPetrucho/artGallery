const wallFromFloorComponent = {
  schema:{placed:{default:false}},
  init(){
    this.raycaster=new THREE.Raycaster()
    this.camera = document.querySelector('#camera')
    this.threeCam=this.camera.getObject3D('camera')
    this.ground = document.querySelector('#ground')
    const scene=this.el.sceneEl

    const placeWall = ()=>{
      this.data.placed=true
      // создаём невидимую «стену»
      const wall=document.createElement('a-box')
      wall.setAttribute('material','color:white;transparent:true;opacity:0')
      wall.object3D.scale.set(100,100,0.25)
      wall.object3D.rotation.y=this.el.object3D.rotation.y
      wall.setAttribute('position',{
        x:this.el.object3D.position.x,
        y:this.el.object3D.position.y+25,
        z:this.el.object3D.position.z})
      wall.id='wall'
      scene.appendChild(wall)

      // создаём картину
      const frame = document.createElement('a-plane')
      frame.id = 'frame'
      frame.setAttribute('width', '3')
      frame.setAttribute('height', '4')
      frame.setAttribute('place-on-wall', '')
      // сразу задаём текстуру, не трогая mesh вручную
      if (window.PAINTING_IMG) {
        frame.setAttribute('material', {src: window.PAINTING_IMG, side: 'double'});
      }
      scene.appendChild(frame)


      // подставляем текстуру, если передана
      if (window.PAINTING_IMG){
        const texLoader=new THREE.TextureLoader()
        texLoader.load(window.PAINTING_IMG,(tex)=>{
          frame.getObject3D('mesh').material.map=tex
          frame.getObject3D('mesh').material.needsUpdate=true
        })
      }
      scene.removeEventListener('click',placeWall)
      this.el.parentNode.removeChild(this.el) // убрать прицел
    }
    scene.addEventListener('click',placeWall)
  },
  tick(){
    if(this.data.placed)return
    const pos=new THREE.Vector3()
    const ndc=new THREE.Vector2(0,-0.5)
    this.threeCam=this.threeCam||this.camera.getObject3D('camera')
    this.raycaster.setFromCamera(ndc,this.threeCam)
    const hit=this.raycaster.intersectObject(this.ground.object3D,true)[0]
    if(hit)pos.copy(hit.point)
    this.el.object3D.position.lerp(pos,0.4)
    this.el.object3D.rotation.y=this.camera.object3D.rotation.y
  }
}

const placeOnWallComponent={
  schema:{placed:{default:false}},
init () {
    this.raycaster = new THREE.Raycaster();
    this.camera = document.querySelector('#camera');
    // wall пока ещё нет – не выходим!
    const scene = this.el.sceneEl;
    scene.addEventListener('click', () => { this.data.placed = true; });
},
  tick(){
    if(this.data.placed)return
    // пробуем достать стену каждый кадр, пока её нет
    this.wall = this.wall || document.querySelector('#wall');
    if (!this.wall) return;            // ещё не создана — просто ждём

  const ndc = new THREE.Vector2(0, 0);
  this.raycaster.setFromCamera(ndc, this.camera.getObject3D('camera'));
  const hit = this.raycaster.intersectObject(this.wall.object3D, true)[0];
  if (hit) {
    this.el.object3D.position.lerp(hit.point, 0.4);
    this.el.object3D.rotation.y = this.wall.object3D.rotation.y;
  }
}
}

export {placeOnWallComponent, wallFromFloorComponent}
