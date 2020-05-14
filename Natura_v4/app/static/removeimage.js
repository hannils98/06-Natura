function remove_my_image() {
    var remove = document.getElementsByClassName('remove-image');
    for (let i = 0; i < remove.length; i++) {
        remove[i].addEventListener("click", function () {
            alert('Är du säker på att du vill ta bort bilden?')
        })
    }
    console.log(remove);
};