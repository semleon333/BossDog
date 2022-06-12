import React from 'react'

const PasswordChange = () => {
  return (
    <div className="PasswordRecovery">
        <div className="title">
            <h1 className="title__heading">Изменение пароля</h1>
        </div>
        <div className="layout_margin">
            <div className="text">
                Пароль<span className="asterisk">*</span>
            </div>
            <input className="input" type="password" />
        </div>
        <div className="layout_margin">
            <div className="text">
                Повторите пароль<span className="asterisk">*</span>
            </div>
            <input className="input" type="password" />
        </div>
        <a className="bold__button" href="/#">
            Установить пароль
        </a>
        <a className="dotted_button" href="password-recovery">
            Я вспомнил(а) пароль
        </a>
</div>
    )
}

export default PasswordChange