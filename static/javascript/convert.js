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

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
