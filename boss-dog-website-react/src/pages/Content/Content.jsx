import React from 'react';

import cart from './img/for_card/cart.png';
import first from './img/for_card/first.jpg';

import './Content.css';

const Content = () => {
    return(
        <div className="container">
            <div className="market">
                <div className="card collar">
                    <a href="collar/index.html" className="card_image_link"><img className="card_image" src={first} alt="Ошейник"/></a>
                    <div className="product_name"><a href="#" className="product_name">Ошейник</a> </div>
                    <div className="product_price">
                        <p className="price">12 333 ₽</p>
                        <div className="add_cart">
                            <a href="#" className="add_cart_image_link"><img src={cart} alt="" className="cart_add_img"/></a>
                        </div>
                    </div>
                </div>

                <div className="card collar">
                    <a href="#" className="card_image_link"><img className="card_image" src={first} alt="Ошейник"/></a>
                    <div className="product_name"><a href="#" className="product_name">Ошейник</a> </div>
                    <div className="product_price">
                        <p className="price">12 333 ₽</p>
                        <div className="add_cart">
                            <a href="#" className="add_cart_image_link"><img src={cart} alt="" className="cart_add_img"/></a>
                        </div>
                    </div>
                </div>

                <div className="card collar">
                    <a href="#" className="card_image_link"><img className="card_image" src={first} alt="Ошейник"/></a>
                    <div className="product_name"><a href="#" className="product_name">Ошейник</a></div>
                    <div className="product_price">
                        <p className="price">12 333 ₽</p>
                        <div className="add_cart">
                            <a href="#" className="add_cart_image_link"><img src={cart} alt="" className="cart_add_img"/></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Content;

