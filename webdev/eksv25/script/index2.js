const N = 3;
const ul = document.createElement("ul");

function lagMeny() {
    for (let i = 1; i <= N; i++) {
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.textContent = "Prosjekt " + i;
        a.href = "prosjekt" + i + "/index" + i + ".html";
        li.appendChild(a);
        ul.appendChild(li);
        }
    }
const menyDiv = document.getElementById("meny");
menyDiv.appendChild(ul);

lagMeny();