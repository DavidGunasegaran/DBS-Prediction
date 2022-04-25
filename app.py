#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template,request
app = Flask(__name__)
import joblib


# In[2]:


@app.route("/",methods=["GET","POST"])
def index():
     if request.method == "POST":
        rate = float(request.form.get("rate"))# rate is from frontend name 'rate'
        print(rate)
        model = joblib.load('DBS_Prediction')
        pred = model.predict([[rate]])

        return(render_template("index.html",result=pred)) # when clicked enter, result = what you see
     else:
        return(render_template("index.html",result="waiting")) # when first entered to site, in index.html {{result}} = waiting


# In[ ]:


if __name__ == "__main__":
    app.run()

