const form = document.getElementById("registerForm");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const data = Object.fromEntries(new FormData(form).entries());   
  data.subscribe = document.getElementById("subscribe").checked;
  fetch("/registration", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
    })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("result").innerHTML = `
            <h2>Дані користувача</h2>
            <p><b>Ім'я:</b> ${data.first_name}</p>
            <p><b>Прізвище:</b> ${data.last_name}</p>
            <p><b>Вік:</b> ${data.age}</p>
            <p><b>Email:</b> ${data.email}</p>
            <p><b>Стать:</b> ${data.gender}</p>
            <p><b>Адреса:</b> ${data.address}</p>
            <p><b>Підписка:</b> ${data.subscribe ? "Так" : "Ні"}</p>
        `;
    })
    .catch((error) => console.error("Error:", error));
});
