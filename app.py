from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')  # Добавьте этот маршрут
def blog():
    return render_template('blog.html')

@app.route('/contacts')  # Убедитесь, что у вас есть этот маршрут
def contacts():
    return "Страница контактов"

if __name__ == '__main__':
    app.run(debug=True)