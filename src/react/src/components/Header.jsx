import React from 'react';

import menu_icon from './img/free-icon-menu-6059003.png';
import user_icon from './img/user.png';
import shopping_cart from './img/shopping-cart.png';


const Header = () => {
    return(
        <header className="header">
            <div className="header__content">
                <div className="header__right">
                    <img className="menu_icon" src={menu_icon}/>
                </div>

                <div className="header__center">
                    <a href="/" className="logo_link">DogShop</a>
                </div>

                <div className="header__left">
                    <a href="/login" className="account">
                        <img className="account_img" src={user_icon} alt="account"/>
                    </a>
                    <a href="/cart" className="cart">
                        <img className="cart_img" src={shopping_cart} alt="CART"/>
                    </a>
                </div>
            </div>
        </header>
    );
}

export default Header; 
