import React, { useState } from 'react';
import './App.css'; 


import CRUDClientes from './componentes/Clientes/CRUDClientes';

function App() {
  const [clientes, setClientes] = useState([]);
  const [peliculas, setPeliculas] = useState([]);


  return (
    <div className="App">
	<CRUDClientes clientes={clientes} setClientes = {setClientes}/>
    </div>
  );
}

export default App;
