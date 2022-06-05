from data import db_session
from data.deliverymen import Deliverymen

deliverymen = {'Антон': 754288169, 'Aртём': 456, 'Глеб': 789}
admin = 190401858511
delyverymen_id = {'Антон': '@slutmee', 'Aртём': '@soberaf', 'Глеб': '@Senkuxd'}
text_chat = '''Наш канал t.me/GhostVapeKgn
Переходите в закреп, там удобное меню

Доставка осуществляется в нижеперечисленные районы города:

Стадион-Рынок-Звёздный-Каравай-Ксм: 
@slutmee

Ксм-Швейная фирма-Рынок-Звёздный:
@soberaf

Центральный рынок-гостиница Москва:
@Senkuxd

Оплата производится только при получении товара!

Возможна доставка и дальше по предварительному уведомлению об этом нашим курьерам.'''

def add_deliverymen(deliverymen):
    db_sess = db_session.create_session()
    spis = db_sess.query(Deliverymen.user_id).all()
    for name, user_id in deliverymen.items():
        if (user_id,) not in spis:
            deliveryman = Deliverymen(name=name, user_id=user_id)
            db_sess.add(deliveryman)
            db_sess.commit()

