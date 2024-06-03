from flask import request, redirect, url_for, render_template, flash, session
from holiday_maintenance import app
from holiday_maintenance import db
from holiday_maintenance.models.mst_holiday import Holiday
from datetime import date

@app.route("/maintenance_date", methods=["POST"])
def maintenance_date():
    #祝日の日付型への変換
    dt = date(int(request.form["holiday"][0:4]), int(request.form["holiday"][5:7]), int(request.form["holiday"][8:10]))
    if request.form["button"] == "insert_update":    
        #DBデータの取得
        holiday = Holiday.query.filter_by(holi_date=dt).first()

        #新規登録(DBから取得できなかった場合)        
        if holiday is None:      
            holiday_insup = Holiday(holi_date = dt, holi_text = request.form["holiday_text"])  
            db.session.add(holiday_insup)            
            db.session.commit()
            msg_out = request.form["holiday"] + "（" + request.form["holiday_text"] + "）が登録されました"
        #更新(DBから取得できた場合)
        else:         
            holiday_insup = Holiday(holi_date = holiday.holi_date, holi_text = request.form["holiday_text"])  
            db.session.merge(holiday_insup)
            db.session.commit()   
            msg_out = request.form["holiday"] + "は「" + request.form["holiday_text"] + "」に更新されました"                     

        return render_template("result.html", msg_out = msg_out)

    elif request.form["button"] == "delete":
        holiday = Holiday.query.filter_by(holi_date=dt).first()
        #存在した場合のみ削除
        if holiday is None: 
            flash(request.form["holiday"] + "は、祝日マスタに登録されていません")
            return redirect(url_for("input")) 
        else:
            Holiday.query.filter_by(holi_date = dt).delete()
            db.session.commit()
            msg_out = str(holiday.holi_date) + "（" + holiday.holi_text + "）は、削除されました"              
            return render_template("result.html", msg_out = msg_out)                            



