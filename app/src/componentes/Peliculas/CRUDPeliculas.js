import React from "react";
import { BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom';
import "./CRUDPeliculas.css";
import PeliculaForm from "./PeliculaForm/PeliculaFormAgregar";
import PeliculaFormActualizar from "./PeliculaForm/PeliculaFormActualizar";

const CRUDPeliculas = ({setPeliculas, peliculas}) => {


  const guardaPeliculaHandler = (peliculaIngresada) => {
    if(peliculas.find(p => p.email === peliculaIngresada.nombre)){
      alert("Esta pelicula ya esta registrada");
      return;
    }
    if(peliculas.length === 0){
      peliculaIngresada.idPelicula = 1;
    }else{
      peliculaIngresada.idPelicula = peliculas[peliculas.length - 1].idPelicula + 1
    }
    const nuevasPeliculas = [...peliculas, peliculaIngresada];
    setPeliculas(nuevasPeliculas);
  };
  const actualizarPelicula = (peliculaIngresada) => {
   if(peliculas.find(p => p.nombre === peliculaIngresada.nombre && p.idPelicula !== peliculaIngresada.idPelicula)){
      alert("Esta pelicula ya esta registrada");
      return;
  }
    const nuevasPeliculas = [...peliculas];
    const indice = nuevasPeliculas.findIndex(p => p.idPelicula === peliculaIngresada.idPelicula);
    nuevasPeliculas[indice] = peliculaIngresada;
    setPeliculas(nuevasPeliculas);
  };

  const eliminarPelicula = (index) => {

    const nuevasPeliculas = [...peliculas];

    nuevasPeliculas.splice(index, 1);

	setPeliculas(nuevasPeliculas);
  };



  return (
    <div>
      <h2>Peliculas</h2>
      <table>
        <thead>
          <tr>
            <th>Id</th>
            <th>Nombre</th>
            <th>Genero</th>
            <th>Duracion</th>
            <th>Inventario</th>
	      <th></th>
          </tr>
        </thead>
        <tbody>
          {peliculas.map((pelicula, index) => (
            <tr key={index}>
              <td>{pelicula.idPelicula}</td>
              <td>{pelicula.nombre}</td>
              <td>{pelicula.genero}</td>
              <td>{pelicula.duracion}</td>
		      <td>{pelicula.inventario}</td>
                  <td>
		            <button onClick={() => eliminarPelicula(index)}>Eliminar</button>
		          </td>
            </tr>
          ))}
        </tbody>
      </table>
      <h3>Agregar Pelicula</h3>
      <PeliculaForm onGuardarPelicula={guardaPeliculaHandler} />
      <h3>Actualizar Pelicual</h3>
      <PeliculaFormActualizar peliculas = {peliculas} onActualizarPelicula = {actualizarPelicula}> </PeliculaFormActualizar>
      <div>
      <Link to="/">
        <button>Menu principal</button>
      </Link>
    </div>
    </div>
  );
};

export default CRUDPeliculas;
