import React from "react";
import { BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom';
import "./CRURentas.css";
import RentaForm from "./RentaForm/RentaFormAgregar";
import RentaFormActualizar from "./RentaForm/RentaFormActualizar";

const CRURentas = ({setRentas, rentas, clientes, peliculas}) => {
  const guardaRentaHandler = (rentaIngresada) => {
    if(rentas.length === 0){
      rentaIngresada.idRenta = 1;
    }else{
      rentaIngresada.idRenta = rentas[rentas.length - 1].idRenta + 1
    }
    const nuevasrentas = [...rentas, rentaIngresada];
    setRentas(nuevasrentas);
  };
  
  const actualizarRenta = (rentaIngresada) => {
    const nuevasrentas = [...rentas];
    const indice = nuevasrentas.findIndex(c => c.idRenta === rentaIngresada.idRenta);
    nuevasrentas[indice] = rentaIngresada;
    setRentas(nuevasrentas);
  };

  const eliminarRenta = (index) => {

    const nuevasrentas = [...rentas];

    nuevasrentas.splice(index, 1);

	setRentas(nuevasrentas);
  };

  return (
    <div>
      <h2>Rentas</h2>
      <table>
        <thead>
          <tr>
            <th>Id</th>
            <th>Id Cliente</th>
            <th>Id Pelicula</th>
            <th>Fecha</th>
            <th>Dias de renta</th>
            <th>Estatus</th>
	      <th></th>
          </tr>
        </thead>
        <tbody>
          {rentas.map((renta, index) => (
            <tr key={index}>
              <td>{renta.idRenta}</td>
              <td>{renta.idCliente}</td>
              <td>{renta.idPelicula}</td>
              <td>{renta.fecha}</td>
		          <td>{renta.dias}</td>
              <td>{renta.estatus}</td>
			        <td>
		            <button onClick={() => eliminarRenta(index)}>Eliminar</button>
		          </td>
            </tr>
          ))}
        </tbody>
      </table>
      <h3>Agregar Renta</h3>
      <RentaForm onGuardarRenta={guardaRentaHandler} />
      <h3>Actualizar Renta</h3>
      <RentaFormActualizar rentas = {rentas} onActualizarRenta = {actualizarRenta}> </RentaFormActualizar>
      <div>
      <Link to="/">
        <button>Menu principal</button>
      </Link>
    </div>
    </div>
  );
};

export default CRURentas;
