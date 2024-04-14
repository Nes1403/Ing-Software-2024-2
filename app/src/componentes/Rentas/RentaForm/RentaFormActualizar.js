import React, { useState } from "react";

import "./RentaForm.css";

const RentaFormActualizar = (props) => {
    const [idRentaIngresado, setIdRentaIngresado] = useState("");
    const [idClienteIngresado, setIdClienteIngresado] = useState("");
    const [idPeliculaIngresado, setIdPeliculaIngresado] = useState("");
    const [fehcaIngresada, setFechaIngresada] = useState("");
    const [diasIngresados, setDiasIngresados] = useState("");
    const [estatusIngresado, setEstatusIngresado] = useState("");
    const [idActualizarIngresado, setIdActualizarIngresado] = useState("")
  
  const cambioIdRentaHandler = (event) => {
    setIdRentaIngresado(event.target.value);
  };

  const cambioIdClienteHandler = (event) => {
    setIdClienteIngresado(event.target.value);
  };

  const cambioIdPeliculaHandler = (event) => {
    setIdPeliculaIngresado(event.target.value);
  };

  const cambioFechaHandler = (event) => {
    setFechaIngresada(event.target.value);
  };

  const cambioDiasHandler = (event) => {
    setDiasIngresados(event.target.value);
  };

  const cambioEstatusHandler = (event) => {
	setEstatusIngresado(event.target.value)
  };

    
  const buscarId = (event) => {
    event.preventDefault();
    setIdActualizarIngresado(idRentaIngresado);
    setIdRentaIngresado(event.target.value);
    const indice = props.rentas.findIndex(r => r.idRenta === parseInt(idRentaIngresado));
    if (indice === -1){
      alert("Id no encontrado")
      setIdRentaIngresado("");
      setIdClienteIngresado("");
      setIdPeliculaIngresado("");
      setFechaIngresada("");
      setDiasIngresados("");
      setEstatusIngresado("");
      return;
    }
    const renta = props.rentas[indice];
    setIdRentaIngresado(renta.idRenta);
    setIdClienteIngresado(renta.idCliente);
    setIdPeliculaIngresado(renta.idPelicula);
    setFechaIngresada(renta.fecha);
    setDiasIngresados(renta.dias);
  };

  const submitHandler = (event) => {
    event.preventDefault();
    const indice = props.rentas.findIndex(r => r.idRenta === parseInt(idActualizarIngresado));
    const renta = {
      idRenta: parseInt(idActualizarIngresado),
      idCliente: idClienteIngresado,
      idPelicula: idPeliculaIngresado,
      fecha: fehcaIngresada,
      dias: diasIngresados,
      estatus: estatusIngresado,
    };
    props.onActualizarRenta(renta);
    setIdRentaIngresado("");
    setIdClienteIngresado("");
    setIdPeliculaIngresado("");
    setFechaIngresada("");
    setDiasIngresados("");
    setEstatusIngresado("");
    setIdActualizarIngresado("");
  };

  return (
    <form onSubmit={submitHandler}>
    <label>
      ID:
    </label>
    <input type="number" value={idRentaIngresado} min="1" onChange={cambioIdRentaHandler}/>
    <button className="button" onClick={buscarId}> Buscar Renta</button>
    <br/>

    <a>Id del renta por actualizar: {idActualizarIngresado}</a>

    <div className="nueva-renta__controls">
    <div className="nueva-renta__control">
          <label>Id Cliente: </label>
          <input
            type="number"
            value={idClienteIngresado}
            min="1"
            onChange={cambioIdClienteHandler}
            required
          />
          <a class="red-text"></a>
        </div>
        <div className="nueva-renta__control">
          <label>Id Pelicula: </label>
          <input
            type="number"
            value={idPeliculaIngresado}
            min="1"
            onChange={cambioIdPeliculaHandler}
            required
          />
          <a class="red-text"></a>
        </div>
        <div className="nueva-renta__control">
          <label>Fecha: </label>
          <input
            type="date"
            value={fehcaIngresada}
            onChange={cambioFechaHandler}
            required
          />
          <a class="red-text"></a>
        </div>
	      <div className="nueva-renta__control">
          <label>Dias de renta: </label>
          <input
            type="number"
            value={diasIngresados}
            min="1"
            onChange={cambioDiasHandler}
            required
          />
          <a class="red-text"></a>
        </div>
        <div className="nueva-renta__control">
          <label>Estatus: </label>
          <select
          value={estatusIngresado}
          onChange={cambioEstatusHandler}
          required
          >
          <option value="" disabled selected>Seleccione una opción</option>
          <option value="Entregado">Entregado</option>
          <option value="Sin entregar">Sin Entregar</option>
          </select>
          <a class="red-text"></a>
        </div>
        <div className="nueva-renta__actions">
        <button type="submit">Actualizar renta</button>
        </div>
    </div>
    </form>
  );
};

export default RentaFormActualizar;