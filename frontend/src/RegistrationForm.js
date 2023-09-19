import React, { useState } from 'react';

const RegistrationForm = () => {
  const [correo, setCorreo] = useState('');
  const [telefono, setTelefono] = useState('');
  const [mensaje, setMensaje] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log('Formulario enviado');

    
    try {
      const response = await fetch('http://localhost:5000/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ correo, telefono }),
      });

      if (response.ok) {
        setMensaje('Datos guardados exitosamente en la base de datos');
      } else {
        setMensaje('Error. El correo o teléfono ya se han registrado anteriormente');
      }
    } catch (error) {
      console.error('Error de red:', error);
      setMensaje('Error de red al enviar datos');
    }
  };

  return (
    <div className="container h-100 center-contents">
      <div className="row justify-content-center align-items-center">
        <div className="col-md-2">
          <form onSubmit={handleSubmit} className="text-center">
            <div className="form-group">
              <label htmlFor="correo" className="font-weight-bold h5">Correo Electrónico:</label>
              <input
                type="email"
                id="correo"
                value={correo}
                onChange={(e) => setCorreo(e.target.value)}
                className="form-control form-control-sm durazno-background"
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="telefono" className="font-weight-bold h5">Teléfono:</label>
              <input
                type="tel"
                id="telefono"
                value={telefono}
                onChange={(e) => {
                  const inputValue = e.target.value.replace(/\D/g, '');
                  setTelefono(inputValue);
                }}
                className="form-control form-control-sm durazno-background"
                required
              />
            </div>
            <div className="form-group mt-3">
              <button type="submit" className="btn btn-danger">Subscribir</button>
            </div>
          </form>
          <p className="text-center mt-3">{mensaje}</p>
        </div>
      </div>
    </div>
  );
};

export default RegistrationForm;
