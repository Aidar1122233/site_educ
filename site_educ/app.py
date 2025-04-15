from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import init_db, get_courses, add_to_cart, get_cart
from certificates import generate_certificate

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Инициализация БД
init_db()

@app.route('/')
def index():
    courses = get_courses()
    return render_template('index.html', courses=courses)

@app.route('/add_to_cart/<int:course_id>')
def add_to_cart(course_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(course_id)
    flash('Курс добавлен в корзину!')
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart_items = get_cart(session.get('cart', []))
    total = sum(item[3] for item in cart_items)
    return render_template('cart.html', cart=cart_items, total=total)

@app.route('/checkout', methods=['POST'])
def checkout():
    email = request.form.get('email')
    for course_id in session.get('cart', []):
        generate_certificate(email, course_id)
    session['cart'] = []
    flash('Заказ оформлен! Удостоверение отправлено на почту.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)