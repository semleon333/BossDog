import React from 'react';
import { Routes, Route } from 'react-router-dom';

import {
  Header,
  Footer,
  Content,
  Login,
  ERROR_404,
  Register,
  PasswordRecovery,
  PasswordChange,
  Collar,
} from './components';

function App() {
  return (
    <div className="wrap">
      <link rel="preconnect" href="https://fonts.googleapis.com" />
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
      <link
        href="https://fonts.googleapis.com/css2?family=Hurricane&display=swap"
        rel="stylesheet"
      />
      <link rel="preconnect" href="https://fonts.googleapis.com" />
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
      <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap"
      />
      <Header />

      <Routes>
        <Route path="/" element={<Content />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/password-recovery" element={<PasswordRecovery />} />
        <Route path="/passwordChange" element={<PasswordChange />} />
        <Route path="collar" element={<Collar />} />
        <Route path="*" element={<ERROR_404 />} />
      </Routes>

      <Footer />
    </div>
  );
}

export default App;
