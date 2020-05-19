function remove_my_image() {
    var remove = document.getElementsByClassName('remove-image');
    for (let i = 0; i < remove.length; i++) {
        remove[i].addEventListener("click", function () {
            remove_image = confirm('Är du säker på att du vill ta bort bilden?')
            if(remove_image) {
                imageID = (document.getElementsByClassName('images')[0].id);
                window.location.href = '?imageid=' + imageID + "&remove=True";
            }
        })
    }
    console.log(remove);
};

function savedPlace(){
    const saved = document.getElementById('saved').value;
    if(saved==='True'){
        const heart = document.getElementById('heart');
        heart.classList.remove('far');
        heart.classList.add('fas')

    }else{
        savePlace();
    }
}

function savePlace(){
    const heart = document.getElementById('heart');
    heart.addEventListener("mouseover", function () {
        heart.classList.remove('far')
        heart.classList.add('fas')
    });

    heart.addEventListener("click", function () {
        window.location.href = '?saved=True';
    });

    heart.addEventListener("mouseout", function () {
        heart.classList.remove('fas')
        heart.classList.add('far')
    });


}