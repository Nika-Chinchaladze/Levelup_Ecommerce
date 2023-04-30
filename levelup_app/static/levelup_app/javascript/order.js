document.getElementById("checkout-button").disabled = true;


// event-listener to input
document.getElementById("id_quantity").addEventListener("click", function(){
    var current_balance = parseFloat(document.getElementById("current-balance").textContent);
    var total_quantity = parseInt(document.getElementById("total-quantity").textContent);
    var order_quantity = parseInt(document.getElementById("id_quantity").value);
    var product_price = parseFloat(document.getElementById("product_price").textContent);
    var total_price = 0;

    // check if order quantity is valid:
    if (order_quantity > 0) {
        total_price = order_quantity * product_price;
        if (order_quantity > total_quantity) {
            document.getElementById("checkout-button").disabled = true;
            document.getElementById("alert-div").style.display = "block";
            document.getElementById("error-message").textContent = "There is not anough Quantity of desired product!";
        }
        else {
            if (current_balance < total_price) {
                document.getElementById("checkout-button").disabled = true;
                document.getElementById("alert-div").style.display = "block";
                document.getElementById("error-message").textContent = "You don't have anough money on balance!";
            }
            else {
                document.getElementById("checkout-button").disabled = false;
                document.getElementById("alert-div").style.display = "none";
            }
        }
    }
    else {
        document.getElementById("checkout-button").disabled = true;
        document.getElementById("alert-div").style.display = "block";
        document.getElementById("error-message").textContent = "Wrong quantity - change it!";
    }

    document.getElementById("total_price").textContent = total_price.toFixed(2);
    document.getElementById("hidden_total_price").value = total_price.toFixed(2);
})
