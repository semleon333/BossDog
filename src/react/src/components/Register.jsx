import React from 'react';

const Register = () => {
  return (
    <div className="Register">
        <div class="title">
            <h1 class="title__heading">Регистрация</h1>
        </div>
        <div class="layout_margin">
            <div class="text">
                Контактное лицо (ФИО)<span class="asterisk">*</span>
            </div>
            <input class="input" type="text" />
        </div>
        <div class="layout_margin">
            <div class="text">
                Контактный телефон<span class="asterisk">*</span>
            </div>
            <input class="input" type="tel" />
        </div>
        <div class="layout_margin">
            <div class="text">
                Email<span class="asterisk">*</span>
            </div>
            <input class="input" type="email" />
        </div>
        <div class="layout_margin">
            <div class="text">
                Пароль<span class="asterisk">*</span>
            </div>
            <input class="input" type="password" />
        </div>
        <div class="layout_margin">
            <div class="text">
                Повторите пароль<span class="asterisk">*</span>
            </div>
            <input class="input" type="password" />
        </div>
        
        <div class="buttons">
            <a class="bold__button" href="/#">Зарегистрироваться</a>
            <a class="dotted_button" href="/login">У меня уже есть аккаунт</a>
        </div>
    </div>
  );
}

export default Register;