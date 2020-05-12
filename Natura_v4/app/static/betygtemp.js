function view_my_ratings() {
    
    var ratings_list = []
    for (let i = 0; i < ratings_list.length; i++) {
        ratings_item = document.querySelector(".my_rating").innerHTML;
        ratings_list.push(ratings_item)
    }
    console.log(ratings_list)
}

view_my_ratings();
