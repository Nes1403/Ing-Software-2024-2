import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom';
import './App.css'; 
import CRUDClientes from './componentes/Clientes/CRUDClientes';
import CRUDPeliculas from './componentes/Peliculas/CRUDPeliculas';
import CRURentas from './componentes/Rentas/CRURentas';


function Inicio() {
  return (
    <div>
      <h1>Menu principal</h1>
      <Link to="/clientes">
        <button>Ver Clientes</button>
      </Link>

      <Link to="/peliculas">
        <button>Ver Peliculas</button>
      </Link>

      <Link to="/rentas">
        <button>Ver Rentas</button>
      </Link>
    </div>
  );
}

function App() {
  const [clientes, setClientes] = useState([]);
  const [peliculas, setPeliculas] = useState([]);
  const [rentas, setRentas] = useState([]);


  return (
    <Router>
      <Routes>
        <Route path="/" element={<Inicio />} />
        <Route path="/clientes" element={<CRUDClientes setClientes={setClientes} clientes={clientes} />} />
        <Route path="/peliculas" element={<CRUDPeliculas setPeliculas={setPeliculas} peliculas={peliculas} />} />
        <Route path="/rentas" element={<CRURentas setRentas={setRentas} rentas={rentas} clientes={clientes} peliculas={peliculas} />} />
      </Routes>
    </Router>
  );
}

export default App;
