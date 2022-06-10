import React from "react";

const Login = () => {
  return (
    <div className="Login">
      <div className="title">
        <h1 className="title__heading">Вход в кабинет покупателя</h1>
      </div>
      <div className="login">
        <div className="login__text text">
          Телефон или Email<span className="asterisk">*</span>
        </div>
        <input className="passwd__input" type="login__text" />
      </div>
      <div className="passwd">
        <div className="passwd__text text">
          Пароль<span className="asterisk">*</span>
        </div>
        <input className="passwd__input" type="password" />
      </div>
      <div className="buttons">
        <a className="voiti" href="/#">
          Войти
        </a>
        <a className="passwd_restore" href="/#">
          Восстановить пароль
        </a>
        <a className="register" href="/register">
          Зарегистрироваться
        </a>
      </div>
    </div>
  );
};

export default Login;
