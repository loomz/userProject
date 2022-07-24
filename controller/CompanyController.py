from bottle import get, post, put, delete, request
import json

from model.Company import Company


@get("/company/<id>")
def getCompany(id):
    print("getCompany id=%s" % id)


@post("/company")
def createCompany():
    print("create Company")


@put("/company/<id>")
def updateCompany(id):
    print("update Company %s" % id)


@delete("/company/<id>")
def deleteCompany(id):
    print("delete Company id=%s" % id)

