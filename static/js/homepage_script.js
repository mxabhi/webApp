// Smooth scrolling
$(document).ready(function(){
	$("a").on('click', function(event) {
		if (this.hash !== "") {
			event.preventDefault();
			var hash = this.hash;
			$('html, body').animate({
				scrollTop: $(hash).offset().top
			}, 800, function(){
				window.location.hash = hash;
			});
		}
	});
	$('.navbar-toggle').click(function() {
		$(this).toggleClass('active');
		$('.navbar-collapse').toggleClass('active');
	});
});

// Form validation
function validateForm() {
	var name = document.forms["enrollmentForm"]["name"].value;
	var email = document.forms["enrollmentForm"]["email"].value;
	var phone = document.forms["enrollmentForm"]["phone"].value;
	var message = document.forms["enrollmentForm"]["message"].value;

	if (name == "") {
		alert("Please enter your name");
		return false;
	}
	if (email == "") {
		alert("Please enter your email address");
		return false;
	}
	if (phone == "") {
		alert("Please enter your phone number");
		return false;
	}
	if (message == "") {
		alert("Please enter your message");
		return false;
	}
}

// Random quote generator
var quotes = [
	"Believe you can and you're halfway there. -Theodore Roosevelt",
	"Education is the most powerful weapon which you can use to change the world. -Nelson Mandela",
	"The only way to do great work is to love what you do. -Steve Jobs",
	"The best way to predict the future is to create it. -Abraham Lincoln",
	"Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. -Steve Jobs",
	"The purpose of our lives is to be happy. -Dalai Lama"
];

function getRandomQuote() {
	var quoteIndex = Math.floor(Math.random() * quotes.length);
	var quote = quotes[quoteIndex];
	document.getElementById("quote").innerHTML = quote;
}

