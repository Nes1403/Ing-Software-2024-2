import React, { useState } from "react";
import "./PeliculaForm.css";

const PeliculaFormActualizar = (props) => {
    const [idPeliculaIngresada, setIdPeliculaIngresada] = useState("");
    const [nombreIngresado, setNombreIngresado] = useState("");
    const [generoIngresado, setGeneroIngresado] = useState("");
    const [duracionIngresada, setDuracionIngresada] = useState("");
    const [inventarioIngresado, setInventarioIngresado] = useState("");
    const [idActualizarIngresado, setIdActualizarIngresado] = useState("");
  

  const cambioIdPeliculaHandler = (event) => {
    setIdPeliculaIngresada(event.target.value);
  };

  const cambioNombreHandler = (event) => {
    setNombreIngresado(event.target.value);
  };

  const cambioGeneroHandler = (event) => {
    setGeneroIngresado(event.target.value);
  };

  const cambioDuracionHandler = (event) => {
    setDuracionIngresada(event.target.value);
  };

  const cambioInventarioHandler = (event) => {
	setInventarioIngresado(event.target.value)
  };
    
  const buscarId = (event) => {
    event.preventDefault();
    setIdActualizarIngresado(idPeliculaIngresada);
    setIdPeliculaIngresada(event.target.value);
    const indice = props.peliculas.findIndex(c => c.idPelicula === parseInt(idPeliculaIngresada));
    if (indice === -1){
      alert("Id no encontrado")
      setIdPeliculaIngresada("");
      setNombreIngresado("");
      setGeneroIngresado("");
      setDuracionIngresada("");
      setInventarioIngresado("");
      setIdActualizarIngresado("");
      return;
    }
    const pelicula = props.peliculas[indice];
    setIdPeliculaIngresada(pelicula.idPelicula);
    setNombreIngresado(pelicula.nombre);
    setGeneroIngresado(pelicula.genero);
    setDuracionIngresada(pelicula.duracion);
    setInventarioIngresado(pelicula.inventario);
  };

  const submitHandler = (event) => {
    event.preventDefault();
    const indice = props.peliculas.findIndex(c => c.idPelicula === parseInt(idActualizarIngresado));
    const pelicula = {
      idPelicula: parseInt(idActualizarIngresado),
      nombre: nombreIngresado,
      genero: generoIngresado,
      duracion: duracionIngresada,
      inventario: inventarioIngresado,
    };
    props.onActualizarPelicula(pelicula);
    setIdPeliculaIngresada("");
    setNombreIngresado("");
    setGeneroIngresado("");
    setDuracionIngresada("");
    setInventarioIngresado("");
    setIdActualizarIngresado("");
  };

  return (
    <form onSubmit={submitHandler}>
    <label>
      ID:
    </label>
    <input type="number" value={idPeliculaIngresada} min="1" onChange={cambioIdPeliculaHandler}/>
    <button className="button" onClick={buscarId}> Buscar Pelicula</button>
    <br/>

    <a>Id de la pelicula por actualizar: {idActualizarIngresado}</a>

    <div className="nueva-pelicula__controls">
        <div className="nueva-pelicula__control">
          <label>Nombre: </label>
          <input
            type="text"
            value={nombreIngresado}
            onChange={cambioNombreHandler}
            required
          />
          <a class="red-text"></a>
        </div>
        <div className="nueva-pelicula__control">
          <label>Genero: </label>
          <input
            type="text"
            value={generoIngresado}
            onChange={cambioGeneroHandler}
          />
          <a class="red-text"></a>
        </div>
	      <div className="nueva-pelicula__control">
          <label>Duracion (min): </label>
          <input
            type="number"
            min="1"
            value={duracionIngresada}
            onChange={cambioDuracionHandler}
          />
          <a class="red-text"></a>
        </div>
        <div className="nueva-pelicula__control">
          <label>Inventario: </label>
          <input
            type="number"
            min="1"
            value={inventarioIngresado}
            onChange={cambioInventarioHandler}
            required
          />
          <a class="red-text"></a>
        </div>
        <div className="nueva-pelicula__actions">
          <button type="submit">Actualizar pelicula</button>
        </div>
    </div>
    </form>
  );
};

export default PeliculaFormActualizar;