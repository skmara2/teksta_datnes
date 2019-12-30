from flask import Flask, render_template, request
import requests
import json
import numpy as np
app = Flask(__name__)

#@app.route('/') #pamtdokuments
#def home():
  #return "Sveika, pasaule!"


global i
i=-2;
global k
k=-3;

@app.route('/')
def home():
  garums()
  return render_template("template.html")
  

@app.route('/pogas')
def pogas():
  return render_template("pogas.html")



@app.route('/garums')
def garums():
  fn='teksts.txt'
  masivs(fn)
  garums=(len(mas1))
  return str(garums);
    

def first(i):
    return i + 1

@app.route('/ajax')
def ajax():
  fn='teksts.txt'
  masivs(fn)
  global i
  i = first(i)
  if i < (len(mas1)-1):
    r = i + 1
    i == r
    result = (mas1[r]);
    return result;
  else:
    return "x";

#@app.route('/a') #pamtdokuments
def masivs(fn):
  f = open(fn, 'r')
  content = f.read()
  f.close()
  #print=(Convert(content))
  global mas1
  mas1 = (Convert(content))
  print (mas1)
  return content
  
@app.route('/atb')
def atb():
  fn='teksts1.txt'
  masivs(fn)
  if k<i:
    k==i
    resulta = (mas1[i+1]);
    return resulta;  
  
  

def Convert(string): 
    li = list(string.split(",")) 
    return li
    



#if __name__== "__main__":
  #main()


app.run(host='0.0.0.0', port=8020)
