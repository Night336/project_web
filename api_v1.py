from datetime import datetime, timedelta
from functools import wraps
from typing import Optional

import jwt
from flask import Blueprint, request, jsonify, current_app

from accessor import Accessor

api_v1_bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api_v1_bp.accessor: Optional[Accessor] = None


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Отсутствует токен авторизации'}), 401

        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])

            current_user_id = payload['sub']
            print(payload)
        except:
            return jsonify({'message': 'Неверный токен авторизации'}), 401

        return func(current_user_id=current_user_id, *args, **kwargs)

    return decorated


@api_v1_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = api_v1_bp.accessor.get_user_by_email(email)
    if user:
        return jsonify({'error': 'Email already exists'}), 400

    api_v1_bp.accessor.create_user(email=email, password=password)

    return jsonify({'message': 'User created successfully'}), 201


@api_v1_bp.route('/login', methods=['POST'])
def api_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = api_v1_bp.accessor.get_user_by_email(email)
    if not user or not user.password == password:
        return jsonify({'error': 'Invalid username or password'}), 401

    token = jwt.encode({
        'sub': user.id,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }, current_app.config['SECRET_KEY'])

    return jsonify({'token': token})


@api_v1_bp.route('/products', methods=['POST'])
@token_required
def get_products(current_user_id):
    products = api_v1_bp.accessor.get_all_product()
    products = [p.to_dict() for p in products]

    return jsonify({'products': products})


@api_v1_bp.route('/cart', methods=['GET'])
@token_required
def get_cart(current_user_id):
    orders = api_v1_bp.accessor.get_all_orders_by_user_id(current_user_id)
    orders = [i.to_dict() for i in orders]
    return jsonify({"orders": orders})


@api_v1_bp.route('/cart/add', methods=['POST'])
@token_required
def add_to_cart(current_user_id):
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    if product_id is None or quantity is None:
        return jsonify({'message': 'Неправильный запрос'}), 400

    # Вместо добавления просто выводим информацию о добавленном продукте
    api_v1_bp.accessor.create_orders(quantity=quantity, user_id=current_user_id, product_id=product_id)
    return jsonify({'message': 'Продукт успешно добавлен в корзину'})


@api_v1_bp.route('/cart/del', methods=['POST'])
@token_required
def del_from_cart(current_user_id):
    data = request.get_json()
    order_id = data.get('order_id')
    if order_id is None:
        return jsonify({'message': 'Неправильный запрос'}), 400

    # Вместо добавления просто выводим информацию о добавленном продукте
    api_v1_bp.accessor.delete_orders(order_id)
    return jsonify({'message': 'Продукт успешно удален из корзины'})
