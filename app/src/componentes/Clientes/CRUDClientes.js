import React from "react";
import ClienteForm from "./ClienteForm/ClienteFormAgregar";
import ClienteFormActualizar from "./ClienteForm/ClienteFormActualizar";

const CRUDClientes = (props) => {


  const guardaClienteHandler = (clienteIngresado) => {
    if(props.clientes.find(c => c.email === clienteIngresado.email) && clienteIngresado.email !== ""){
      alert("El correo ya esta registrado");
      return;
    }
    if(props.clientes.length === 0){
      clienteIngresado.idCliente = 1;
    }else{
      clienteIngresado.idCliente = props.clientes[props.clientes.length - 1].idCliente + 1
    }
    const nuevosClientes = [...props.clientes, clienteIngresado];
    props.setClientes(nuevosClientes);
  };
  const actualizarCliente = (clienteIngresado) => {
   if(props.clientes.find(c => c.email === clienteIngresado.email && c.idCliente !== clienteIngresado.idCliente) && clienteIngresado.email !== ""){
      alert("El correo ya esta registrado");
      return;
  }
    const nuevosClientes = [...props.clientes];
    const indice = nuevosClientes.findIndex(c => c.idCliente === clienteIngresado.idCliente);
    nuevosClientes[indice] = clienteIngresado;
    props.setClientes(nuevosClientes);
  };

  const eliminarCliente = (index) => {

    const nuevosClientes = [...props.clientes];

    nuevosClientes.splice(index, 1);

	props.setClientes(nuevosClientes);
  };



  return (
    <div>
      <h2>Clientes</h2>
      <table>
        <thead>
          <tr>
            <th>Id</th>
            <th>Nombre</th>
            <th>Apellido Paterno</th>
            <th>Apellido Materno</th>
            <th>Email</th>
            <th>password</th>
            <th>Super </th>
	      <th></th>
          </tr>
        </thead>
        <tbody>
          {props.clientes.map((cliente, index) => (
            <tr key={index}>
              <td>{cliente.idCliente}</td>
              <td>{cliente.nombre}</td>
              <td>{cliente.ap_pat}</td>
              <td>{cliente.ap_mat}</td>
		          <td>{cliente.email}</td>
              <td>{cliente.password}</td>
              <td>{cliente.superUser ? "Sí" : "No"}</td>
			        <td>
		            <button onClick={() => eliminarCliente(index)}>Eliminar</button>
		          </td>
            </tr>
          ))}
        </tbody>
      </table>
      <h3>Agregar Cliente</h3>
      <ClienteForm onGuardarCliente={guardaClienteHandler} />
      <h3>Actualizar Cliente</h3>
      <ClienteFormActualizar clientes = {props.clientes} onActualizarCliente = {actualizarCliente}> </ClienteFormActualizar>
    </div>
  );
};

export default CRUDClientes;
