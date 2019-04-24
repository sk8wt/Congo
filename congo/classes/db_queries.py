import MySQLdb
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import random
from classes import *

def get_connection():
	return MySQLdb.connect(host='54.157.229.227',user= 'root',password='databaes',port=3306, database = 'congo')

def list_merch(request):
	db = get_connection() #MYSQLdb.connect(host='54.157.229.227', user='root', password='databaes', port=3306, database='congo')
	cur = db.cursor()
	sql = "select * from merchandise"
	cur.execute(sql)
	merch = []
	for row in cur.fetchall():
		merch.append(Merch(row[1], row[2], row[3], row[4], row[5]))
	db.close()
	return merch
	# Load the html for merch
	# return render(request, template, {"merch": merch})

'''
	{% for landloard in data%}
	{{landloard.office_addr}}
	{%endfor%}
'''


def create_merch(request, name, price, desc, rating, url):
	db = get_connection() #MYSQLdb.connect(host='54.157.229.227', user='root', password='databaes', port=3306, database='congo')
	cur = db.cursor()
	rand_id = random.randint(1000,60000)
	sql = "insert into merchandise values("+rand_id+", "+name+", "+price+", "+desc+ ", "+rating + ", "+ url + ")"
	cur.execute(sql)
	db.commit()
	db.close()
	return redirect('home')

def edit_merch(request, m_id, name, price, desc, rating, url):
	db = get_connection()
	cur = db.cursor()
	sql = "update merchandise set m_name="+name+", m_price="+price+", m_desc="+desc+ ",m_rating= "+rating + ", merchandise_image="+ url + " where merchandise_id=" + m_id
	cur.execute(sql)
	db.commit()
	db.close()
	return redirect('home')

def delete_merch(request, merch_id):
	db = get_connection()
	cur = db.cursor()
	sql = "delete from merchandise where merchandise_id=" + merch_id
	cur.execute(sql)
	db.commit()
	db.close()
	return redirect('home')