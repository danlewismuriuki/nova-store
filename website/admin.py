from flask import Blueprint
from flask_login import login_required


admin = Blueprint('admin', __name__)

@admin.route('/add-shop-items', methods=['GET', 'POST'])
@login_required
def add_shop_items():
    if current_user.id == 1:
        form = ShopItemsForm()

        return rende_template('add-shop-items.html', form=form)
    return render_template('404.html')
