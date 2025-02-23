document.getElementById("reservation-form").addEventListener("submit", function(event) {
    event.preventDefault(); 

    document.getElementById("reservation-form").style.display = "none";
    document.getElementById("confirmation-message").classList.remove("hidden");
});
