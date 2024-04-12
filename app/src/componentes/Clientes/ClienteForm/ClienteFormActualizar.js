import React, { useState } from "react";

import "./ClienteForm.css";

const ClienteFormActualizar = (props) => {
    const [idClienteIngresado, setIdClienteIngresado] = useState("");
    const [nombreIngresado, setNombreIngresado] = useState("");
    const [ap_patIngresado, setAp_patIngresado] = useState("");
    const [ap_matIngresado, setAp_matIngresado] = useState("");
    const [passwordIngresado, setPasswordIngresado] = useState("");
    const [emailIngresado, setEmailIngresado] = useState("");
    const [superUserIngresado, setSuperUser] = useState(false);
    const [idActualizarIngresado, setIdActualizarIngresado] = useState("")
  

  const cambioIdClienteHandler = (event) => {
    setIdClienteIngresado(event.target.value);
  };

  const cambioNombreHandler = (event) => {
    setNombreIngresado(event.target.value);
  };

  const cambioAp_patHandler = (event) => {
    setAp_patIngresado(event.target.value);
  };

  const cambioAp_matHandler = (event) => {
    setAp_matIngresado(event.target.value);
  };

  const cambioPasswordHandler = (event) => {
	setPasswordIngresado(event.target.value)
  };

  const cambioEmailHandler = (event) => {
	setEmailIngresado(event.target.value)
  };

  const cambioSuperUserHandler = (event) => {
    setSuperUser(event.target.checked)
  };

    
  const buscarId = (event) => {
    event.preventDefault();
    setIdActualizarIngresado(idClienteIngresado);
    setIdClienteIngresado(event.target.value);
    const indice = props.clientes.findIndex(c => c.idCliente === parseInt(idClienteIngresado));
    if (indice === -1){
      alert("Id no encontrado")
      setIdClienteIngresado("");
      setNombreIngresado("");
      setAp_patIngresado("");
      setAp_matIngresado("");
      setPasswordIngresado("");
      setEmailIngresado("");
      setSuperUser(false);
      setIdActualizarIngresado("");
      return;
    }
    const cliente = props.clientes[indice];
    setIdClienteIngresado(cliente.idCliente);
    setNombreIngresado(cliente.nombre);
    setAp_patIngresado(cliente.ap_pat);
    setAp_matIngresado(cliente.ap_mat);
    setPasswordIngresado(cliente.password);
    setEmailIngresado(cliente.email);
    setSuperUser(cliente.superUser);
  };

  const submitHandler = (event) => {
    event.preventDefault();
    const indice = props.clientes.findIndex(c => c.idCliente === parseInt(idActualizarIngresado));
    const cliente = {
      idCliente: parseInt(idActualizarIngresado),
      nombre: nombreIngresado,
      ap_pat: ap_patIngresado,
      ap_mat: ap_matIngresado,
      password: passwordIngresado,
      email: emailIngresado,
      superUser: superUserIngresado,
    };
    props.onActualizarCliente(cliente);
    setIdClienteIngresado("");
    setNombreIngresado("");
    setAp_patIngresado("");
    setAp_matIngresado("");
    setPasswordIngresado("");
    setEmailIngresado("");
    setSuperUser(false);
    setIdActualizarIngresado("");
  };

  return (
    <form onSubmit={submitHandler}>
    <label>
      ID:
    </label>
    <input type="number" value={idClienteIngresado} min="1" onChange={cambioIdClienteHandler}/>
    <button className="button" onClick={buscarId}> Buscar Cliente</button>
    <br/>

    <a>Id del cliente por actualizar: {idActualizarIngresado}</a>

    <div className="nuevo-cliente__controls">
        <div className="nuevo-cliente__control">
          <label>Nombre: </label>
          <input
            type="text"
            value={nombreIngresado}
            onChange={cambioNombreHandler}
            required
          />
          <a class="red-text"></a>
        </div>
        <div className="nuevo-cliente__control">
          <label>Apellido Paterno: </label>
          <input
            type="text"
            value={ap_patIngresado}
            onChange={cambioAp_patHandler}
            required
          />
          <a class="red-text"></a>
        </div>
	      <div className="nuevo-cliente__control">
          <label>Apellido Materno: </label>
          <input
            type="text"
            value={ap_matIngresado}
            onChange={cambioAp_matHandler}
          />
          <a class="red-text"></a>
        </div>
        <div className="nuevo-cliente__control">
          <label>Password: </label>
          <input
            type="password"
            value={passwordIngresado}
            onChange={cambioPasswordHandler}
            required
          />
          <a class="red-text"></a>
        </div>
	      <div className="nuevo-cliente__control">
          <label>Email: </label>
          <input
            type="email"
            value={emailIngresado}
            onChange={cambioEmailHandler}
          />
          <a class="red-text"></a>
	      </div>
	      <div className="nuevo-cliente__control">
          <label>Super user: </label>
          <input
            type="checkbox"
            checked={superUserIngresado}
            onChange={cambioSuperUserHandler}
          />
          <a class="red-text"></a>
        </div>
        <div className="nuevo-cliente__actions">
          <button type="submit">Actualizar cliente</button>
        </div>
    </div>
    </form>
  );
};

export default ClienteFormActualizar;