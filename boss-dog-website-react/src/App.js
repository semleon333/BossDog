import React from 'react';

import Header from './pages/Header/Header.jsx';
import Content from './pages/Content/Content.jsx';


function App() {
  return (
    <div className="wrap">
      <link rel="preconnect" href="https://fonts.googleapis.com"/>
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
      <link href="https://fonts.googleapis.com/css2?family=Hurricane&display=swap" rel="stylesheet"/>
      <link rel="preconnect" href="https://fonts.googleapis.com"/>
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
      <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet"/> 
      <Header />
      <Content />
    </div>
  );
}

export default App;
