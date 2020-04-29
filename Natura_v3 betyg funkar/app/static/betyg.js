function user_ratings() {
    const stars=document.querySelector(".user_rating").children;
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
}

function show_average_rating() {
    var average_rating = Number(Math.round(document.getElementById('ave_rating').value));
    const stars=document.querySelector(".average_ratings").children;
        for(let i=0; i<stars.length; i++){
            for(let j=0; j<average_rating; j++){
                stars[j].classList.remove("fa-star-o");
                stars[j].classList.add("fa-star");
            }
        
        }

}

function show_user_rating() {
    var saved_user_rating = Number(document.getElementById('user_rating').value);
    const stars=document.querySelector(".user_rating").children;
    console.log(saved_user_rating);
    if(saved_user_rating >= 0 && saved_user_rating <= 5){
        console.log('hej')
        for(let i=0; i<stars.length; i++){
            for(let j=0; j<saved_user_rating; j++){
                stars[j].classList.remove("fa-star-o");
                stars[j].classList.add("fa-star");
                console.log(stars)
            }
        }
    }else{
        user_ratings();
    }
    

}

show_average_rating();
show_user_rating();