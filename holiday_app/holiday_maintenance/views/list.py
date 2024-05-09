from flask import request, redirect, url_for, render_template, flash, session
from holiday_maintenance import app
from holiday_maintenance import db
from holiday_maintenance.models.mst_holiday import Holiday

@app.route("/list", methods=["POST"])
def list():
    holidaylist = Holiday.query.all()
    return render_template('list.html',holidaylist = holidaylist)
