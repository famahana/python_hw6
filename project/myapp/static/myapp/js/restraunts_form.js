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
        form.reset();
        window.location.reload();
})
    .catch((error) => console.error("Error:", error));
});
function deleteRestraunt(id) {
  fetch(`restraunts/delete/${id}`, {
    method: "POST"
  })
  .then(res => res.json())
  .then(() => {
    location.reload();
  });
}
function updateRestraunt(id) {
  const data = {
    name: prompt("Name"),
    specialization: prompt("Specialization"),
    adress: prompt("Adress"),
    web_url: prompt("Web URL"),
    phone_number: prompt("Phone")
  };

  fetch(`/restraunts/update/${id}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(() => location.reload());
}
function searchRestraunts() {
  const query = document.getElementById("searchInput").value;

  fetch(`/restraunts/search/?q=${query}`)
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("list");
      list.innerHTML = "";

      data.forEach(r => {
        list.innerHTML += `
          <div class="card">
            <h3>${r.name}</h3>
            <p><b>Спеціалізація:</b> ${r.specialization}</p>
            <p><b>Адреса:</b> ${r.adress}</p>
            <p><b>Телефон:</b> ${r.phone_number}</p>

            ${r.web_url ? `<a href="${r.web_url}" target="_blank">Вебсайт</a>` : ""}
          </div>
        `;
      });
    });
}