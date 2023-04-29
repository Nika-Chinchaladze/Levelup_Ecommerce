document.getElementById("id_quantity").addEventListener("click", function(){
    var order_quantity = parseInt(document.getElementById("id_quantity").value);
    var product_price = parseFloat(document.getElementById("product_price").textContent);
    var total_price = 0;
    console.log(order_quantity);
    if (order_quantity > 0) {
        total_price = order_quantity * product_price;
    }
    document.getElementById("total_price").textContent = total_price.toFixed(2);
    document.getElementById("hidden_total_price").value = total_price.toFixed(2);
})
