const form2 = document.getElementById("contactsForm");
form2.addEventListener("submit", (e) => {
  e.preventDefault();
  const data = Object.fromEntries(new FormData(form2).entries());
  console.log(data);
  fetch("/contacts", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      form2.reset();
      window.location.reload()
    })
    .catch((error) => console.error("Error:", error));
});