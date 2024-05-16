from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import Transfer, User
from . import db
import json
import os

banks_file = 'Website/banks_nr.json'

views = Blueprint('views', __name__)

@views.route('/formularz', methods=['GET', 'POST'])
@login_required
def formularz():
    if request.method == 'POST':
        bankNr = request.form.get('bankNumber')
        name = request.form.get('name')
        surname = request.form.get('surname')

        if len(bankNr) != 26:
            flash("Account number must have 26 numbers", category='error')
        else:
            with open(banks_file) as bf:
                bank_dict = json.load(bf)

                print(bankNr[2:6])

                if bankNr[2:6] in bank_dict:

                    print("INSIDE")

                    new_transfer = Transfer(number=bankNr, name=name, surname=surname, user_id=current_user.id)
                    db.session.add(new_transfer)
                    db.session.commit()

                    return redirect(url_for('views.formularzAcc', id=new_transfer.id))

    return render_template('formularz.html', user=current_user)

# user=current_user, bank_nr=bankNr, name_t=name, surname_t=surname
@views.route('/formularz_acc/<id>', methods=['GET', 'POST'])
@login_required
def formularzAcc(id):
    if request.method == 'POST':
        return redirect(url_for('views.formularz'))

    if request.method == 'GET':
        # t = db.session.query(Transfer.id).order_by(Transfer.date.desc()).where(current_user.id==Transfer.user_id)
        transfers = Transfer.query.get(id)

        if transfers:
            if transfers.user_id == current_user.id:
                return render_template('formularz_acc.html', user=current_user, bankNr=transfers.number, name=transfers.name, surname=transfers.surname)

    return render_template('formularz_acc.html', user=current_user)

 # bankNr=transfers.number, name=transfers.name, surname=transfers.surname

@views.route('/dane')
@login_required
def dane():
    name = User.query.get(current_user.id).first_name
    mail = User.query.get(current_user.id).email
    print(name)
    print(mail)
    return render_template('dane.html', name=name, mail=mail, user=current_user)