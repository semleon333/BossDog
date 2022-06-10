import React from 'react';

import telegram from '../scss/assests/telegram.png';
import instagram from '../scss/assests/instagram.png';
import vk from '../scss/assests/vk.png';

const Footer = () => {
    return(
        <footer className="footer">
        <div className="footer__content">
            <div className="footer__right">
                <div className="footer__right-phone">
                    <a href="tel:8999999999" className="phone-number">+7 999 999 999</a>
                </div>
                <div className="footer__right-street">г. Москва, Новорязанская ул., 18, стр. 11</div>
            </div>
            {/* <div className="footer__center">
                <a href="#" className="logo_link">DogShop</a>
            </div> */}
            <div className="footer__left">
                <ul className="social-medias">
                    <li className="social-medias_icons">
                        <a href="/#" className="social-medias_icons-link">
                            <img src={telegram} alt="Наш Telegram"/>
                        </a>
                    </li>
                    <li className="social-medias_icons">
                        <a href="/#" className="social-medias_icons-link">
                            <img src={instagram} alt="Наш Instagram"/>
                        </a>
                    </li>
                    <li className="social-medias_icons">
                        <a href="/#" className="social-medias_icons-link">
                            <img src={vk} alt="Наш VKontakte"/>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </footer>
    );
}

export default Footer;