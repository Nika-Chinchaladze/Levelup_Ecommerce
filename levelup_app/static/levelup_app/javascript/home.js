function filterProducts() {
    var userInput = document.getElementById("searchProduct");
    var myFilter = userInput.value.toUpperCase();
    var productList = document.getElementById("myList");
    var eachProduct = productList.getElementsByClassName("actualProduct")
    var eachHeading = productList.getElementsByClassName("product-heading");

    for (var i = 0; i < eachHeading.length; i++) {
        myh2 = eachHeading[i];
        textValue = myh2.textContent || myh2.innerHTML;
        if (textValue.toUpperCase().indexOf(myFilter) > -1) {
            eachProduct[i].style.display = "";
        }
        else {
            eachProduct[i].style.display = "none";
        }
    }
}


function filterProductAverage() {
    var userInput = document.getElementById("search-product");
    var myFilter = userInput.value.toUpperCase();
    var productList = document.getElementById("my-list");
    var eachProduct = productList.getElementsByClassName("actual-product")
    var eachHeading = productList.getElementsByClassName("my-product-heading");

    for (var i = 0; i < eachHeading.length; i++) {
        myh2 = eachHeading[i];
        textValue = myh2.textContent || myh2.innerHTML;
        if (textValue.toUpperCase().indexOf(myFilter) > -1) {
            eachProduct[i].style.display = "";
        }
        else {
            eachProduct[i].style.display = "none";
        }
    }
}