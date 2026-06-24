async function actualizar() {

    try {

        const res = await fetch("http://127.0.0.1:8000/conteo");
        const data = await res.json();

        document.getElementById("objetos").innerText =
            data.objetos_detectados;

        document.getElementById("personas").innerText =
            data.personas_detectadas;

    } catch (error) {

        console.log("Error:", error);

    }
}

setInterval(actualizar, 500);