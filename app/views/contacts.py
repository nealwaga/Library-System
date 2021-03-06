# internal imports
from app.forms import member_form
from app import app, db

# external imports 
import requests

from flask import render_template, redirect, url_for, flash, request
from app.models import Book, Member


# Renders member page
@app.route('/contacts', methods=['GET', 'POST'])
def contacts_page():
    # read members from db
    member = Member.query.order_by('id').all() 
    form_member = member_form() 
    #checks book and member eligibility for borrowing
    books_to_borrow = Book.query.filter(Book.borrow_stock > 0).all()
    members_can_borrows = Member.query.filter(Member.to_pay < 500).all()
    books_to_return =  Book.query.filter(Book.borrower).all()
    # if no validation error in creating a member
    if form_member.validate_on_submit():
        # creates a member in db
        member_to_create = Member(name = member_form().name.data,
                                  phone_number = member_form().phone_number.data,
                                  member_name = member_form().member_name.data)
        db.session.add(member_to_create)
        db.session.commit()

        flash('Successfully create a member', category="success")
        return redirect(request.referrer)
    
    # if validation error occured
    if form_member.errors != {}: # If there are not errors from the validations
        for err_msg in form_member.errors.values():
            flash(f'There was an error with creating a Member: {err_msg}', category = 'danger')
    return render_template('contacts/contacts.html', member_form = form_member,
                            members = member, length = len(member), 
                            books_to_borrow = books_to_borrow, 
                            members_can_borrow = members_can_borrows, 
                            books_to_return = books_to_return)


# deletes a member
@app.route('/delete-contact/<member_id>', methods=['POST'])
def delete_contact(member_id):
    try:
        # reads requested member from db
        member = Member.query.filter_by(id=member_id).first()
        db.session.delete(member)
        db.session.commit()
        flash("Deleted Successfully", category="success")

    except:
        flash("Error in deletion", category="danger")

    return redirect(url_for('contacts_page'))



# updates a member
@app.route('/update-contact/<member_id>', methods=['GET','POST'])
def update_contact(member_id):
    # reads requested member from db
    member = Member.query.filter_by(id=member_id).first()
    newName = request.form.get("name")
    newNumber = request.form.get("phone_number")
    newMember = request.form.get("member_name")

    try:
        if(member.name is not newName):
            member.name = newName
        if(member.phone_number is not newNumber):
            member.phone_number = newNumber
        if(member.member_name is not newMember):
            member.member_name = newMember
        db.session.commit()
        flash("Updated successfully!", category="success")

    except:
        flash("Failed to update", category="danger")

    return redirect(url_for('contacts_page'))
