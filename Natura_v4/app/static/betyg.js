function user_ratings() {
    const stars = document.querySelector(".user_rating").children;
    let ratingValue;
    let index;

    for (let i = 0; i < stars.length; i++) {
        stars[i].style.cursor="pointer";
        stars[i].addEventListener("mouseover", function () {
            for (let j = 0; j < stars.length; j++) {
                stars[j].classList.remove("fa-star");
                stars[j].classList.add("fa-star-o");
            }
            for (let j = 0; j <= i; j++) {
                stars[j].classList.remove("fa-star-o");
                stars[j].classList.add("fa-star");
            }
        })
        stars[i].addEventListener("click", function () {
            ratingValue = i + 1;
            window.location.search = '?rating=' + ratingValue;
            index = i;
        })
        stars[i].addEventListener("mouseout", function () {
            for (let j = 0; j < stars.length; j++) {
                stars[j].classList.remove("fa-star");
                stars[j].classList.add("fa-star-o");
            }
            for (let j = 0; j <= index; j++) {
                stars[j].classList.remove("fa-star-o");
                stars[j].classList.add("fa-star");
            }
        })
    }
}

function show_average_rating() {
    var average_rating = Number(Math.round(document.getElementById('ave_rating').value));
    const stars = document.querySelector(".average_ratings").children;
    for (let i = 0; i < stars.length; i++) {
        for (let j = 0; j < average_rating; j++) {
            stars[j].classList.remove("fa-star-o");
            stars[j].classList.add("fa-star");
        }

    }

}

function show_user_rating() {
    var saved_user_rating = Number(document.getElementById('user_rating').value);
    const stars = document.querySelector(".user_rating").children;
    if (saved_user_rating >= 0 && saved_user_rating <= 5) {
        for (let i = 0; i < stars.length; i++) {
            stars[i].style.cursor='not-allowed';
            for (let j = 0; j < saved_user_rating; j++) {
                stars[j].classList.remove("fa-star-o");
                stars[j].classList.add("fa-star");
            }
        }
    } else {
        user_ratings();
    }
}

function view_my_ratings() {
    
    var ratings_list = document.getElementById('my_ratings').getElementsByClassName('my_rating');
    const numberOfRatings = ratings_list.length;
    

    for (let i = 0; i < numberOfRatings; i++) {
        var rating = document.getElementById('rating' + (i+1)).innerHTML;
        document.getElementById('rating' + (i+1)).innerHTML = "";
        for (let j = 1; j < 6; j++) {
            var star = document.createElement('span');
            star.classList.add('fa');
            if (rating < j) {
                star.classList.add('fa-star-o');
            }else {
                star.classList.add('fa-star');
            }
            
            document.getElementById('rating' + (i+1)).appendChild(star);
            
        }
    } 
        
}

function change_my_rating() {
    var icon = document.getElementById('my_ratings').getElementsByClassName('change_rating');
    const numberOfPlaces = icon.length;
    for (let i = 0; i < numberOfPlaces; i++) {
        
        icon[i].addEventListener("click", function cl() {
            changeRating (i, icon);
            icon[i].removeEventListener("click", cl, true);
        }, true);

    }   
}

function changeRating(i, icon) {

    var clicked = false;

    var stars = document.getElementById('rating' + (i+1)).getElementsByClassName('fa');

    var saveIcon = icon[i].parentNode.getElementsByClassName('change_rating');

    for (let j = 0; j < stars.length; j++) {
        
        stars[j].classList.remove("fa-star");
        stars[j].classList.add("fa-star-o");

        stars[j].style.cursor="pointer";
        stars[j].addEventListener("mouseover", function mo() {
            if(!clicked)
                setNewRating(j, stars);
        });
        stars[j].addEventListener("click", function cl() {
            clickRating(j, stars, saveIcon);
            clicked = true;
            stars[j].removeEventListener('click', cl, true);
        }, true);

    }
}

function setNewRating(newRating, stars) {
    for (let j = 0; j < stars.length; j++) {
            
        stars[j].classList.remove("fa-star");
        stars[j].classList.add("fa-star-o");
    }
    for (let i = newRating; i > -1; i--) {
        stars[i].classList.remove("fa-star-o");
        stars[i].classList.add("fa-star");

    }
}

function clickRating(newRating, saveIcon) {

    saveIcon[0].classList.remove("fas");
    saveIcon[0].classList.remove("fa-pencil-alt");
    saveIcon[0].classList.add("far");
    saveIcon[0].classList.add("fa-save");

    saveIcon[0].addEventListener("click", function save() {
        var ratingValue = newRating + 1;
        window.location.href = '?rating=' + ratingValue + "&placeid=" + saveIcon[0].parentNode.getElementsByClassName("name")[0].id;
    
    });

    

}

