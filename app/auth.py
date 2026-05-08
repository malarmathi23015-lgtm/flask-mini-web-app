from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    abort
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.forms import (
    LoginForm,
    RegisterForm,
    NoteForm
)

from app.models.user import User
from app.models.note import Note

from app.extensions import db


auth = Blueprint('auth', __name__)


# HOME PAGE
@auth.route('/')
def home():

    return render_template(
        'home.html'
    )


# REGISTER
@auth.route('/register', methods=['GET', 'POST'])
def register():

    # IF ALREADY LOGGED IN
    if current_user.is_authenticated:

        return redirect(
            url_for('auth.dashboard')
        )

    form = RegisterForm()

    if form.validate_on_submit():

        # CHECK EXISTING USER
        existing_user = User.query.filter_by(
            email=form.email.data
        ).first()

        if existing_user:

            flash(
                'Email already exists',
                'danger'
            )

            return redirect(
                url_for('auth.register')
            )

        # CREATE NEW USER
        user = User(

            email=form.email.data,

            password=generate_password_hash(
                form.password.data
            )
        )

        db.session.add(user)

        db.session.commit()

        flash(
            'Registration successful',
            'success'
        )

        return redirect(
            url_for('auth.login')
        )

    return render_template(
        'register.html',
        form=form
    )


# LOGIN
@auth.route('/login', methods=['GET', 'POST'])
def login():

    # IF ALREADY LOGGED IN
    if current_user.is_authenticated:

        return redirect(
            url_for('auth.dashboard')
        )

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and check_password_hash(
            user.password,
            form.password.data
        ):

            login_user(user)

            flash(
                'Login successful',
                'success'
            )

            return redirect(
                url_for('auth.dashboard')
            )

        flash(
            'Invalid email or password',
            'danger'
        )

    return render_template(
        'login.html',
        form=form
    )


# DASHBOARD
@auth.route('/dashboard')
@login_required
def dashboard():

    notes = Note.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        'dashboard.html',
        notes=notes
    )


# CREATE NOTE
@auth.route('/create_note', methods=['GET', 'POST'])
@login_required
def create_note():

    form = NoteForm()

    if form.validate_on_submit():

        note = Note(

            title=form.title.data,

            content=form.content.data,

            user_id=current_user.id
        )

        db.session.add(note)

        db.session.commit()

        flash(
            'Note created successfully',
            'success'
        )

        return redirect(
            url_for('auth.dashboard')
        )

    return render_template(
        'create_note.html',
        form=form
    )


# VIEW NOTE
@auth.route('/note/<int:note_id>')
@login_required
def view_note(note_id):

    note = Note.query.get_or_404(note_id)

    # SECURITY CHECK
    if note.author != current_user:

        abort(403)

    return render_template(
        'view_note.html',
        note=note
    )


# EDIT NOTE
@auth.route('/edit_note/<int:note_id>',
            methods=['GET', 'POST'])

@login_required
def edit_note(note_id):

    note = Note.query.get_or_404(note_id)

    # SECURITY CHECK
    if note.author != current_user:

        abort(403)

    form = NoteForm()

    if form.validate_on_submit():

        note.title = form.title.data

        note.content = form.content.data

        db.session.commit()

        flash(
            'Note updated successfully',
            'success'
        )

        return redirect(
            url_for('auth.dashboard')
        )

    form.title.data = note.title

    form.content.data = note.content

    return render_template(
        'edit_note.html',
        form=form
    )


# DELETE NOTE
@auth.route('/delete_note/<int:note_id>')
@login_required
def delete_note(note_id):

    note = Note.query.get_or_404(note_id)

    # SECURITY CHECK
    if note.author != current_user:

        abort(403)

    db.session.delete(note)

    db.session.commit()

    flash(
        'Note deleted successfully',
        'warning'
    )

    return redirect(
        url_for('auth.dashboard')
    )


# PROFILE
@auth.route('/profile')
@login_required
def profile():

    total_notes = Note.query.filter_by(
        user_id=current_user.id
    ).count()

    return render_template(
        'profile.html',
        total_notes=total_notes
    )


# LOGOUT
@auth.route('/logout')
@login_required
def logout():

    logout_user()

    flash(
        'Logged out successfully',
        'success'
    )

    return redirect(
        url_for('auth.login')
    )