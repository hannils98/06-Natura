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