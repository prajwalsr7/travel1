function convertCurrency() {
    var amount = document.getElementById("amount").value;
    var fromCurrency = document.getElementById("from_currency").value;
    var toCurrency = document.getElementById("to_currency").value;

    $.ajax({
        url: "http://currency.eba-qchvcgzv.us-east-1.elasticbeanstalk.com/convert",
        type: "GET",
        data: { amount: amount, from_currency: fromCurrency, to_currency: toCurrency },
        success: function(response) {
            document.getElementById("result").innerHTML = amount + " " + fromCurrency + " = " + response.converted_amount.toFixed(2) + " " + toCurrency;
        },
        error: function(_xhr, _status, error) {
            console.error(error);
            document.getElementById("result").innerHTML = "An error occurred. Please try again later.";
        }
    });
}
