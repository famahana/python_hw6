const form = document.getElementById("restrauntForm");
form.addEventListener("submit", (e) => {
  e.preventDefault();
    const data = Object.fromEntries(new FormData(form).entries());
    fetch("/restraunts", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then((response) => response.json())
    .then((data) => {
        alert(data.name);
        form.reset();
        window.location.reload();
})
    .catch((error) => console.error("Error:", error));
});