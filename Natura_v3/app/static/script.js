 /* When the user clicks on the button,
 toggle between hiding and showing the dropdown content */
 function myFunction() {
     document.getElementById("myDropdown").classList.toggle("show");
 }

 // Close the dropdown if the user clicks outside of it
 window.onclick = function(e) {
     if (!e.target.matches('.dropbtn')) {
         var myDropdown = document.getElementById("myDropdown");
         if (myDropdown.classList.contains('show')) {
             myDropdown.classList.remove('show');
         }
     }
 }





const stars=document.querySelector(".ratings").children;
let ratingValue;
let index;

    for(let i=0; i<stars.length; i++){
        stars[i].addEventListener("mouseover", function(){
            for(let j=0; j<stars.length; j++){
                stars[j].classList.remove("fa-star");
                stars[j].classList.add("fa-star-o");
            }
            for(let j=0; j<=i; j++){
                stars[j].classList.remove("fa-star-o");
                stars[j].classList.add("fa-star");
            }
        })
        stars[i].addEventListener("click", function(){
            ratingValue = i+1;
            window.location.search = '?rating=' + ratingValue;
            index=i;
            })
        stars[i].addEventListener("mouseout", function(){
            for(let j=0; j<stars.length; j++){
                stars[j].classList.remove("fa-star");
                stars[j].classList.add("fa-star-o");
            }
            for(let j=0; j<=index; j++){
                stars[j].classList.remove("fa-star-o");
                stars[j].classList.add("fa-star");
            }
        })
    }