function removeMyImage() {
    var remove = document.getElementsByClassName('remove-image');
    for (let i = 0; i < remove.length; i++) {
        remove[i].addEventListener("click", function () {
<<<<<<< HEAD
            remove_image = confirm('Är du säker på att du vill ta bort bilden?');
            if(remove_image) {
=======
            remove_image = confirm('Är du säker på att du vill ta bort bilden?')
            if (remove_image) {
>>>>>>> 8f1ece1bdb50ed396b11cdb77c955f58fc3f763e
                imageID = (document.getElementsByClassName('images')[0].id);
                window.location.href = '?imageid=' + imageID + "&remove=True";
            }
        })
    }
};

function savedPlace() {
    const saved = document.getElementById('saved').value;
    if (saved === 'True') {
        const heart = document.getElementById('heart');
        heart.classList.remove('far');
<<<<<<< HEAD
        heart.classList.add('fas');

    }else{
=======
        heart.classList.add('fas')
    } else {
>>>>>>> 8f1ece1bdb50ed396b11cdb77c955f58fc3f763e
        savePlace();
    }
}

function savePlace() {
    const heart = document.getElementById('heart');
    heart.addEventListener("mouseover", function () {
        heart.classList.remove('far');
        heart.classList.add('fas');
    });
    heart.addEventListener("click", function () {
        window.location.href = '?saved=True';
    });
    heart.addEventListener("mouseout", function () {
        heart.classList.remove('fas');
        heart.classList.add('far');
    });
}


function removeSavedPlace() {
    heart = document.getElementsByClassName('heart_btn');
    for (let i = 0; i < heart.length; i++) {
        heart[i].addEventListener("mouseover", function () {
            heart[i].classList.remove('fas');
            heart[i].classList.add('far');
        });
        heart[i].addEventListener("click", function () {
            window.location.href = '?placeid=' + heart[i].id + '&saved=False';
        });
        heart[i].addEventListener("mouseout", function () {
            heart[i].classList.remove('far');
            heart[i].classList.add('fas');
        });
    }
}