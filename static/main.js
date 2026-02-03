let btn1 = document.getElementById("category-0");
let btn2 = document.getElementById("category-1");
let laptop = document.querySelectorAll(".lp");
let pc = document.querySelectorAll(".pc");



btn2.addEventListener("click", function(){
    laptop.forEach(lp => {
        lp.style.display = "block"; 
    });
    pc.forEach(pc => {
        pc.style.display = "none"; 
    });
})

btn1.addEventListener("click", function(){
    laptop.forEach(lp => {
        lp.style.display = "none"; 
    });
    pc.forEach(pc => {
        pc.style.display = "block"; 
    });
})
