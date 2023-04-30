var spent_moneys = document.getElementsByClassName("money_spent");
var total_spending = 0;

for (var i = 0; i < spent_moneys.length; i++) {
    total_spending += parseFloat(spent_moneys[i].textContent);
}

document.getElementById("total-spent").textContent = total_spending;