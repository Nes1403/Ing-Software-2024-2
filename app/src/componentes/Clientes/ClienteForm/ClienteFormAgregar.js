import React, { useState } from "react";

import "./ClienteForm.css";

const ClienteForm = (props) => {
    const [nombreIngresado, setNombreIngresado] = useState("");
    const [ap_patIngresado, setAp_patIngresado] = useState("");
    const [ap_matIngresado, setAp_matIngresado] = useState("");
    const [passwordIngresado, setPasswordIngresado] = useState("");
    const [emailIngresado, setEmailIngresado] = useState("");
    const [superUserIngresado, setSuperUser] = useState(false);
    
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
	setPasswordIngresado(event.target.value);
  };

  const cambioEmailHandler = (event) => {
	setEmailIngresado(event.target.value);
  };

  const cambioSuperUserHandler = (event) => {
    setSuperUser(event.target.checked);
  };
    
  const submitHandler = (event) => {
    event.preventDefault();

    const cliente = {
	nombre: nombreIngresado,
	ap_pat: ap_patIngresado,
	ap_mat: ap_matIngresado,
	password: passwordIngresado,
	email: emailIngresado,
  superUser: superUserIngresado,
    };

    props.onGuardarCliente(cliente);
    setNombreIngresado("");
    setAp_patIngresado("");
    setAp_matIngresado("");
    setPasswordIngresado("");
    setEmailIngresado("");
    setSuperUser(false);
  };

  return (
    <form onSubmit={submitHandler}>
      <div className="nuevo-cliente__controls">
        <div className="nuevo-cliente__control">
          <label>Nombre: </label>
          <input
            type="text"
            value={nombreIngresado}
            onChange={cambioNombreHandler}
            required
          />
        </div>
        <div className="nuevo-cliente__control">
          <label>Apellido Paterno: </label>
          <input
            type="text"
            value={ap_patIngresado}
            onChange={cambioAp_patHandler}
            required
          />
        </div>
	  <div className="nuevo-cliente__control">
          <label>Apellido Materno: </label>
          <input
            type="text"
            value={ap_matIngresado}
            onChange={cambioAp_matHandler}
          />
        </div>
        <div className="nuevo-cliente__control">
          <label>Password: </label>
          <input
            type="password"
            value={passwordIngresado}
            onChange={cambioPasswordHandler}
            required
          />
        </div>
	  <div className="nuevo-cliente__control">
          <label>Email: </label>
          <input
            type="email"
            value={emailIngresado}
            onChange={cambioEmailHandler}
          />
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
          <button type="submit">Agregar cliente</button>
        </div>
      </div>
    </form>
  );
};

export default ClienteForm;
