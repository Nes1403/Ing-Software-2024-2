import React, { useState } from "react";

import "./PeliculaForm.css";

const PeliculaForm = (props) => {
    const [nombreIngresado, setNombreIngresado] = useState("");
    const [generoIngresado, setGeneroIngresado] = useState("");
    const [duracionIngresada, setDuracionIngresada] = useState("");
    const [inventarioIngresado, setInventarioIngresado] = useState("");
    
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
	setInventarioIngresado(event.target.value);
  };
    
  const submitHandler = (event) => {
    event.preventDefault();

    const pelicula = {
	nombre: nombreIngresado,
	genero: generoIngresado,
	duracion: duracionIngresada,
	inventario: inventarioIngresado,
    };

    props.onGuardarPelicula(pelicula);
    setNombreIngresado("");
    setGeneroIngresado("");
    setDuracionIngresada("");
    setInventarioIngresado("");
  };

  return (
    <form onSubmit={submitHandler}>
      <div className="nueva-pelicula__controls">
        <div className="nueva-pelicula__control">
          <label>Nombre: </label>
          <input
            type="text"
            value={nombreIngresado}
            onChange={cambioNombreHandler}
            required
          />
        </div>
        <div className="nueva-pelicula__control">
          <label>Genero: </label>
          <input
            type="text"
            value={generoIngresado}
            onChange={cambioGeneroHandler}
          />
        </div>
	  <div className="nueva-pelicula__control">
          <label>Duracion (min): </label>
          <input
            type="number"
            min="1"
            value={duracionIngresada}
            onChange={cambioDuracionHandler}
          />
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
        </div>
        <div className="nueva-pelicula__actions">
          <button type="submit">Agregar pelicula</button>
        </div>
      </div>
    </form>
  );
};

export default PeliculaForm;
