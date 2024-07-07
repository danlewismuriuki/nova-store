from flask import Blueprint, render_template
from .models import Product, Cart
from flash_login import login_required

views = Blueprint('views', __name__)

@views.route('/')
def home():

    items = Product.query.filter_by(flash_sale=True)

    return render_template('home.html', items=items)

@views.route('/add-to-cart/<int:item_id>')
@login_required
def add_to_cart(item_id):
    item_to_add = product.query.get(item_id)
    item_exists = Cart.query.filter_by(product_links=item_id, customer_links=current_user.id).first()
    if item_exists:
        try:
            item_exists.quantity = item_exists.quantity + 1
            db.session.commit()
            flash(f' Quantity of { item_exists.product.product_name } has been updated')
        except Exception as e:
            print('Quantity not Updated', e)
            flash(f'Quantity of { item_exisrs.product.product_name } not updated')
            return redirect(request.referrer)

    new_cart_item = Cart()
    new_cart_item.quantity = 1
    new_cart_item.product.product_link = item_to_add.id
    new_cart_item.customer_link = current_user.id

    try:
        db.session.add(new_cart_item)
        db.session.commit()
        flash(f'{new_cart_item.product.product_name} added to cart')
    except Exception as e:
        print('Item not added to cart', e)
        flash(f'{new_cart_item.product.product_name} has not been added to cart')
        return redirect(request.referrer)
