import React, { useState } from 'react';
import './CRURentas.css'; // Importa los estilos CSS para este componente

function CRURentas() {
  const [rentas, setRentas] = useState([]);

  // Funciones para CRU de rentas

  return (
    <div className="rentas-container">
      <h2>CRU Rentas</h2>
      {/* Aquí va la interfaz para CRU de rentas */}
    </div>
  );
}

export default CRURentas;
