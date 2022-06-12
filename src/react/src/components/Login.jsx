import React from "react";

const Login = () => {
  return (
    <div className="Login">
      <div className="title">
        <h1 className="title__heading">Вход в кабинет покупателя</h1>
      </div>
      <div className="layout_margin">
        <div className="text">
          Телефон или Email<span className="asterisk">*</span>
        </div>
        <input className="input" type="text" />
      </div>
      <div className="layout_margin">
        <div className="text">
          Пароль<span className="asterisk">*</span>
        </div>
        <input className="input" type="password" />
      </div>
      <div className="buttons">
        <a className="bold__button" href="/#">
          Войти
        </a>
        <a className="dotted_button" href="password-recovery">
          Восстановить пароль
        </a>
        <a className="dotted_button" href="/register">
          Зарегистрироваться
        </a>
      </div>
    </div>
  );
};

export default Login;
