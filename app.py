from flask import Flask,render_template,request,redirect,url_for
from pymongo import MongoClient

app=Flask(__name__)

@app.route("/read",methods=["post","get"])
def Insert():
    if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")
        mobile=request.form.get("mobile")
        dic={"id":id,"name":name,"mobile":mobile}
        
        client=MongoClient("mongodb://localhost:27017")
        database=client.siva
        collection=database.ranjani
        collection.insert_one(dic)
        print("success")
        client.close()

    return render_template("insert.html")

@app.route("/")
def read():
    client=MongoClient("mongodb://localhost:27017")
    database=client.siva
    collection=database.ranjani
    x=collection.find()
    l=[]
    for i in x:
        l.append(i)
    client.close()

    return render_template("index.html",data=l)

@app.route("/update/<id>",methods=["post","get"])
def Update(id):
    if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")
        mobile=request.form.get("mobile")
        client=MongoClient("mongodb://localhost:27017")
        database=client.siva
        collection=database.ranjani
        collection.update_one({"id":id},{"$set":{"name":name,"mobile":mobile}})
        client.close()
        return redirect(url_for("read"))

    client=MongoClient("mongodb://127.0.0.1:27017")
    database=client.siva
    collection=database.ranjani
    x=collection.find_one({"id":id})
    dic={"id":x.get("id"),"name":x.get("name"),"mobile":x.get("mobile")}
    client.close()

    return render_template("update.html",data=dic)

@app.route("/delete/<id>")
def Delete(id):
    client=MongoClient("mongodb://127.0.0.1:27017")
    database=client.siva
    table=database.ranjani
    table.delete_one({"id":id})
    client.close()
    return redirect(url_for("read"))

if __name__=="__main__":
    app.run(debug=True)