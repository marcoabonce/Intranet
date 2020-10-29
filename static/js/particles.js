const canvas = document.getElementById("canvas1");
const ctx = canvas.getContext('2d');
//ctx.mozImageSmoothingEnabled = this._imageSmoothingEnabled; 
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let particles;

//obtenermos la posicion del mouse c:

let mouse = {
    x:null,
    y:null,
    radious:(canvas.height/80)*(canvas.width/80)
}

window.addEventListener('mousemove',
    function(event){
        mouse.x = event.x;
        mouse.y = event.y;
    }
);

//clase particula

class Particle {
    constructor (x,y,direccionX,direccionY,size,color){
        this.x = x;
        this.y = y;
        this.direccionX = direccionX;
        this.direccionY = direccionY;
        this.size = size;
        this.color = color;
    }

    //metodo para dibujar las particulas <3

    draw(){
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI*2, false);
        ctx.fillStyle = '#2c4b5e';
        ctx.fill();
    }

    //Animacion

    update(){
        //verificar si la particula esta en el area
        if (this.x > canvas.width || this.x < 0)
            this.direccionX = -this.direccionX;
         
        if (this.y > canvas.height || this.y < 0)
            this.direccionY = -this.direccionY;
        
        //revisar colision o acercamiento del mouse
        let dx = mouse.x - this.x;
        let dy = mouse.y - this.y;
        let distance = Math.sqrt(dx*dx + dy*dy);
        if (distance < mouse.radious + this.size){
            if(mouse.x < this.x && this.x < canvas.width - this.size * 10)
                this.x += 3;
            
            if (mouse.x > this.x && this.x > this.size * 10)
                this.x -= 3;

            if(mouse.y < this.y && this.y < canvas.height - this.size * 10)
                this.y += 3;

            if (mouse.y > this.y && this.y > this.size * 10)
                this.y -= 3;
        }

        //mover particula

        this.x += this.direccionX/2;
        this.y += this.direccionY/2;

        //dibujamos la particula
        this.draw();
    }
}

//iniciamos el array de particulas

function init(){
    particles = [];
    let numberOfParticles = (canvas.height * canvas.width) / 21000;
    for (let index = 0; index < numberOfParticles; index++) {
        let size = (Math.random() * 1.7) + 1;
        let x = (Math.random() * ((innerWidth - size * 2 ) - (size * 2 )) + size * 2);
        let y = (Math.random() * ((innerHeight - size * 2 ) - (size * 2 )) + size * 2);
        let direccionX = (Math.random() * 5) - 2.5;
        let direccionY = (Math.random() * 5) - 2.5;
        let color = '#2c4b5e';

        particles.push(new Particle(x, y, direccionX, direccionY, size, color));
    }
}
//conectar las particulas
function conectar(){
    for (let a = 0; a < particles.length; a++) {
        for (let b = 0; b < particles.length; b++) {
            let distance = ((particles[a].x-particles[b].x)*(particles[a].x-particles[b].x))+
            (particles[a].y-particles[b].y)*(particles[a].y-particles[b].y);
            if(distance < (canvas.width/7) * (canvas.height/7)){
                let opacityValue = 1 - (distance/16000);
                ctx.strokeStyle='rgba(41, 80, 106,'+opacityValue+')';
                ctx.lineWith = 1;
                ctx.beginPath();
                ctx.moveTo(particles[a].x, particles[a].y);
                ctx.lineTo(particles[b].x, particles[b].y);
                ctx.stroke();
            }
        }
    }
}

//funcion de animacion

function animate(){
    requestAnimationFrame(animate);
    ctx.clearRect(0,0,innerWidth, innerHeight);

    for (let index = 0; index < particles.length; index++) {
        particles[index].update();
    }
    conectar();
}

//resize event

window.addEventListener('resize',
    function(){
        canvas.width = innerWidth;
        canvas.height = innerHeight;
        mouse.radious = ((canvas.height/80) * (canvas.height/80));
        init()
    }
)

//mouse out event
window.addEventListener('mouseout',
    function(){
        mouse.x = undefined;
        mouse.y = undefined;
    }
)

init();
animate();