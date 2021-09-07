const card = document.querySelectorAll(".card__inner");
const btn = document.querySelectorAll(".botton");
const btn2 = document.querySelectorAll(".botton2");


card.forEach(function(card) {
  



btn.forEach(function(btn) {
  btn.addEventListener("click", function (e) {
    card.classList.toggle('is-flipped');
    console.log("os filped")
  
   
  })
  })

  btn2.forEach(function(btn2) {
    btn2.addEventListener("click", function (e) {
      card.classList.remove('is-flipped');
      console.log("los filped")
    
     
    })
    })
    
  });




// btn.addEventListener("click", function (e) {
//   card.classList.toggle('is-flipped');
//   console.log("os filped")

 
// })

// btn2.addEventListener("click", function (e) {
//   card.classList.remove('is-flipped');
//   console.log("os filped");
// })

