from market import app,db,login_manager
from flask import  render_template,redirect,url_for,flash,get_flashed_messages
from market.models import Item,User
from market.form import RegForm,LoginForm
from flask_login import login_user , logout_user,login_required,current_user

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/market')
@login_required
def market_page():
    items = Item.query.all()
    return  render_template('market.html',item=items)
@app.route('/register', methods = ['GET','POST'] )
def reg_page():
    form = RegForm()
    if form.validate_on_submit():
        cu = User(username=form.username.data, password_hashed=form.password.data,cpass=form.cpass.data,email=form.email.data)
        db.session.add(cu)
        db.session.commit()
        login_user(cu)
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for errmsg in form.errors.values():
            print(f"error with {errmsg}")
            flash(f"error with {errmsg}")
    return render_template('register.html',form=form)
@app.route('/login',methods=["GET","POST"])
def login_page():
    if current_user.is_authenticated:
         return render_template("myhome.html",name=current_user.username)
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password(attempted_password=form.password.data) :
            login_user(attempted_user)
            flash(f"sucess you r logged in as  {attempted_user.username}")
            return render_template("myhome.html",name=attempted_user)
            return redirect(url_for('market_page'))
    return render_template('login.html', form = form)

@app.route('/logout')
@login_required
def logout_page():
    x = current_user.username
    logout_user()
    return render_template("home.html",name=x)

@app.errorhandler(404)
def page_not_found(e):
   return render_template("404.html"),404
print("hi")
