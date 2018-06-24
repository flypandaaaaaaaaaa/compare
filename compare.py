from flask import Flask,render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField,FileField,TextAreaField
from flask_wtf.file import FileAllowed,FileRequired
from werkzeug import secure_filename
import difflib,os
from wtforms.validators import DataRequired

class FileForm(FlaskForm):
    File1=FileField('文件1',validators=[FileRequired(' '),FileAllowed(['txt'],'text only')])
    File2=FileField('文件2',validators=[FileRequired(' '),FileAllowed(['txt'],'text only')])
    submit = SubmitField('开始对比')
class TextForm(FlaskForm):
    Text1=TextAreaField('文本1',validators=[DataRequired()])
    Text2=TextAreaField('文本2',validators=[DataRequired()])
    submit = SubmitField('开始对比')
class ChangeForm(FlaskForm):
    submit=SubmitField('切换一下')

app=Flask(__name__)
bootstrap=Bootstrap(app)
app.config['SECRET_KEY']='DADSSADSA'
uppath='/tmp/'
@app.route("/cmpfile",methods=['GET','POST'])
def findex():
    fform=FileForm()
    tform = TextForm()
    CForm=ChangeForm()
    set_fform='True'
    if fform.validate_on_submit():
        filename1=secure_filename(fform.File1.data.filename)
        fform.File1.data.save(uppath+filename1)
        filename2=secure_filename(fform.File2.data.filename)
        fform.File2.data.save(uppath+filename2)
        with open(uppath+filename1,'r') as f1,open(uppath+filename2,'r') as f2:
            cmp=difflib.HtmlDiff()
            cmp_result=cmp.make_file(f1,f2)
        os.remove(uppath+filename1)
        os.remove(uppath+filename2)
        return cmp_result.encode('utf-8')
    return render_template('index.html',fform=fform,tform=tform,set_fform=set_fform)

@app.route("/cmptext",methods=['GET','POST'])
def tindex():
    fform = FileForm()
    tform=TextForm()
    CForm=ChangeForm()
    set_fform='False'
    if tform.validate_on_submit():
        text1=tform.Text1.data.splitlines()
        text2=tform.Text2.data.splitlines()
        cmp=difflib.HtmlDiff()
        cmp_result=cmp.make_file(text1,text2)
        return cmp_result.encode('utf-8')
    return render_template('index.html',fform=fform,tform=tform,set_fform=set_fform)


app.run(host='0.0.0.0',port=10112)
