import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('/').then(response => {
      setMessage('Bem-vindo ao {{ project_name }}!');
    });
  }, []);

  return (
    <div className="App">
      <h1>{message}</h1>
      <p>Projeto gerado com Kobra 🐍</p>
    </div>
  );
}

export default App;