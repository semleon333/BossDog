import React from 'react'

const  PasswordRecovery = () => {
  return (
    <div className="PasswordRecovery">
        <div className="title">
            <h1 className="title__heading">Вход в кабинет покупателя</h1>
        </div>
        <div className="layout_margin">
            <div className="text">
                Email<span className="asterisk">*</span>
            </div>
            <input className="input" type="text" />
        </div>
        <a className="bold__button" href="/#">
          Восстановить пароль
        </a>
        <a className="dotted_button" href="password-recovery">
          Я вспомнил(а) пароль
        </a>
    </div>
  )
}

export default PasswordRecovery