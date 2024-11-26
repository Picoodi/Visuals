//Getting the canvas from the html
const canvas = document.getElementById("SimulationFrame");
//creating ctx for being able to draw on the canvas
const ctx = canvas.getContext("2d");

//saving height and width same as the html canvas
const height = canvas.height;
const width = canvas.width;

//implementing the Newton G constant in js
const G = 0.1;



class Circle{
    constructor(color,x,y,radius,mass, velocityX, velocityY){
        this.color = color;
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.mass = mass;
        this.velocityX = velocityX;
        this.velocityY = velocityY;

    }

    DrawCircle() {
        ctx.beginPath();
        ctx.arc(this.x,this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.closePath();
    }

    movement(){
        this.x  += this.velocityX
        this.y  += this.velocityY

        if (this.x - this.radius <= 0  || this.x + this.radius >= height){
            this.velocityX *= -1
        }
        if (this.y - this.radius <= 0 || this.y + this.radius >= width){
            this.velocityY *= -1
        }

    }
}


function animate(){
    ctx.clearRect(0,0,width,height);
    Circ1.DrawCircle();
    Circ2.DrawCircle();
    Circ3.DrawCircle();

    Circ1.movement();
    Circ2.movement();
    Circ3.movement();
    requestAnimationFrame(animate)
}


let Circ1 = new Circle("red",100,100,10,1,2,1);
let Circ2 = new Circle("green",600,200,5,1,6,4);
let Circ3 = new Circle("grey",40,700,15,10,1.3,2.5);


animate();
