from Controller.authors_controller import authors
from Controller.books_controller import books
from Controller.commons import Carousel
from Controller.log_in_controller import logins
from Controller.sign_up_controller import signups
from Controller.search_controller import *
from Model.MongoDB.Models.books import Book
from flask_bootstrap import Bootstrap
from data import *
from Model.MongoDB.Models.authors_db import *
from Model.MongoDB.Models.books_db import *



app = Flask(__name__)
app.debug = True


app.register_blueprint(books)
app.register_blueprint(authors)
app.register_blueprint(logins)
app.register_blueprint(signups)

app.config['SECRET_KEY'] = 'passw0rd'

Bootstrap(app)



@app.route('/', methods=['GET', 'POST'])
def index():
    names = get_names(AUTHORS)
    form = NameForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        if name.lower() in names:
            form.name.data = ""
            id = get_id(AUTHORS, name)
            return redirect(url_for('author', id=id))
        else:
            message = "No results"
    return render_template('index.html', form=form, message=message, names=names, carousel=Carousel(Book.all(), items_per_row=3))


@app.route('/search/<id>')
def author(id):
    id, name, photo = get_author(AUTHORS, id)
    if name == "Unknown":
        return render_template('404.html'), 404
    else:
        return render_template('search.html', id=id, name=name, photo=photo)


if __name__ == '__main__':
    app.run()
