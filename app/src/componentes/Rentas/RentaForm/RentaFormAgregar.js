import React, { useState } from "react";

import "./RentaForm.css";

const RentaForm = (props) => {
    const [IdClienteIngresado, setIdClienteIngresado] = useState("");
    const [IdPeliculaIngresado, setIdPeliculaIngresado] = useState("");
    const [fecha, setFechaIngresado] = useState("");
    const [diasIngresados, setDiasIngresado] = useState("");
    
  const cambioIdClienteHandler = (event) => {
    setIdClienteIngresado(event.target.value);
  };

  const cambioIdPeliculaHandler = (event) => {
    setIdPeliculaIngresado(event.target.value);
  };

  const cambioFechaHandler = (event) => {
    setFechaIngresado(event.target.value);
  };

  const cambioDiasHandler = (event) => {
	setDiasIngresado(event.target.value);
  };
    
  const submitHandler = (event) => {
    event.preventDefault();

    const renta = {
	idCliente: IdClienteIngresado,
	idPelicula: IdPeliculaIngresado,
	fecha: fecha,
	dias: diasIngresados,
	estatus: "Sin entegrar",
    };

    props.onGuardarRenta(renta);
    setIdClienteIngresado("");
    setIdPeliculaIngresado("");
    setFechaIngresado("");
    setDiasIngresado("");
  };

  return (
    <form onSubmit={submitHandler}>
      <div className="nueva-renta__controls">
        <div className="nueva-renta__control">
          <label>Id Cliente: </label>
          <input
            type="number"
            value={IdClienteIngresado}
            min="1"
            onChange={cambioIdClienteHandler}
            required
          />
        </div>
        <div className="nueva-renta__control">
          <label>Id Pelicula: </label>
          <input
            type="number"
            value={IdPeliculaIngresado}
            min="1"
            onChange={cambioIdPeliculaHandler}
            required
          />
        </div>
	  <div className="nueva-renta__control">
          <label>fecha: </label>
          <input
            type="date"
            value={fecha}
            onChange={cambioFechaHandler}
          />
        </div>
        <div className="nueva-renta__control">
          <label>Dais de renta: </label>
          <input
            type="number"
            value={diasIngresados}
            defaultValue={5}
            min="1"
            onChange={cambioDiasHandler}
            required
          />
        </div>
        <div className="nueva-renta__actions">
          <button type="submit">Agregar renta</button>
        </div>
      </div>
    </form>
  );
};

export default RentaForm;
