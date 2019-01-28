"""
Created on Tue Jan 15 14:20:02 2019

@author: jdhruwa
"""
import os
from flask import Flask, flash, request,url_for,redirect,jsonify,render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
import ModelLDA

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(["png","jpg",'docx','pdf'])

app = Flask(__name__)
cors=CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#Check for allowed extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
#Upload file       
@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.to_dict()
        # check if the post request has the file part
        if len(request.files)==0:
            flash('No file part')
            return redirect(request.url)
        
        # if user does not select file, browser also
        # submit an empty part without filename
        
        print(files)
        for f in files:
            f=files[f]
            #print(f)
            if f.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if f and allowed_file(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        jd=url_for('uploaded_file',filename=secure_filename(files['file1'].filename))
        cv=url_for('uploaded_file',filename=secure_filename(files['file2'].filename))   
        match=ModelLDA.LDA(jd[1:],cv[1:])
        #print(match)
        return render_template('result.html',match=round(match,2))

    if request.method=='GET':
        return render_template('home.html')



from flask import send_from_directory
#view uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    
if __name__=="__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True)