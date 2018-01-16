from flask import Flask, render_template, request, session
from wtforms import Form, StringField, validators

import MainProcess

app = Flask(__name__)


class RegisterUser(Form):
    firstname = StringField('Firstname', [validators.Length(min=1, max=150), validators.DataRequired()])
    lastname = StringField('Lastname', [validators.Length(min=1, max=150), validators.DataRequired()])
    age = StringField('Age', [validators.Length(min=1, max=150), validators.DataRequired()])

@app.route('/home', methods=['GET', 'POST'])
def home():
    session['userid'] = 'John'
    form = RegisterUser(request.form)
    if request.method == 'POST' and form.validate():
        MainProcess.registerNewUser(form.firstname.data, form.lastname.data, form.age.data)
        print("User Successfully Register")

    return render_template('home.html', form=form)

@app.route('/views')
def views():
    return render_template('views.html')

@app.route('/loans')
def graph():
    totalPaid = 0
    totalUnpaid = 0
    totalOverdue = 0
    totalPaid = MainProcess.processTransaction(session['userid'], 'Dec', 'paid')
    totalUnpaid = MainProcess.processTransaction('John', 'Dec', 'unpaid')
    totalOverdue = MainProcess.processTransaction('John', 'Dec', 'overdue')

    return render_template('loans.html', totalPaidAmount = totalPaid, totalUnpaidAmount = totalUnpaid,totalOverdueAmount = totalOverdue)

@app.route('/details')
def details():
    userslist = []
    userslist = MainProcess.processUser()
    return render_template('Details.html', users=userslist, count=len(userslist))

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()