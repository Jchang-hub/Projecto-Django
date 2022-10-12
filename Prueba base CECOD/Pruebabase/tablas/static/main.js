let paisp = document.getElementById("pais");
let nacionalidadp = document.getElementById("nacionalidad")

const autoNacionalidad = async (idpais) => {
    try {
        const response = await fetch("./json");
        const data = await response.json();
        let respuesta = ``

        data.forEach((pais) => {
            if (idpais == pais.id) {
                respuesta = `${pais.nacionalidad}`;
            }
        });
        console.log(respuesta);
        if (respuesta != ``){
        nacionalidadp.value = respuesta;
        }

    } catch (error) {
        console.log(error);
    }
};




paisp.addEventListener("change", (event) => {
        
    autoNacionalidad(event.target.value);
                
});





  





