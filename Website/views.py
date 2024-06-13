from flask import Blueprint, render_template, request, redirect, flash, url_for, jsonify, session
from flask_login import login_user, login_required, logout_user, current_user
from .models import Transfer, User
from . import db
import json
import os
import uuid

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

@views.route('/acc', methods=['GET', 'POST'])
@login_required
def acc():
    if request.method == 'GET':
        if current_user.superuser:
            transfers = Transfer.query.all()
            return render_template('acc.html', user=current_user, transfer=transfers)
        else:
            return redirect(url_for('views.formularz'))


@views.route('/accept-transfer', methods=['POST'])
def accept_transfer():
    transfer = json.loads(request.data)
    transferId = transfer['transferId']
    transfer = Transfer.query.get(transferId)
    if transfer:
        transfer.accepted = True
        db.session.commit()

    return jsonify({})