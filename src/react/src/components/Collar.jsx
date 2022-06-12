import React from 'react';

import img from './img/for_card/first.jpg';

const Collar = () => {
  return (
    <div className="product">
        <img src={img} alt="" className="product__photo"/>
        <div className="product-info">
            <div className="product__name">Ошейник</div>
            <div className="product__price">12 333 ₽</div>

            <div className="section-2">
                <div className="colors">
                    <p className="color__title">Цвет</p>
                    <button className="color blue">Синий</button>
                    <button className="color black">Чёрный</button>
                    <button className="color orange">Оранжевый</button>
                </div>
                <button className="add-to-cart"><p className="cart-text">Корзина</p></button>
            </div>
        </div>
    </div>   
    );
}

export default Collar;