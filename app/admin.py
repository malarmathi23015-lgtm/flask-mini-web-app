from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import User, ActivityLog

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/dashboard")
@login_required
def admin_dashboard():
    if current_user.role != "admin":
        return "Access Denied"

    users = User.query.all()
    logs = ActivityLog.query.all()
    return render_template("admin_dashboard.html", users=users, logs=logs)