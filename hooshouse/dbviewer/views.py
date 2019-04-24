from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .apt_building import apt_building, landlord, unit, lease, tenant, available_apt
from .forms import *
import MySQLdb



# Create your views here.
def test(request):
    db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
    cur = db.cursor()
    cur.execute("select * from apt_building")
    data = []
    for row in cur.fetchall():
        data.append(apt_building(row[0], row[1], row[2], row[3]))
    db.close()
    template = "viewAptBuilding.html"
    return render(request, template, {"data":data})

def create_apt(request):
    template = 'create_apt.html'
    if request.method == "GET":
        form = apt_form()
    else:
        form = apt_form(request.POST)
        if form.is_valid():
            db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
            cur = db.cursor()
            cur.execute("insert into apt_building(address, num_units, building_name, year_of_construction) values('{0}',{1},'{2}',{3})".format(form.cleaned_data['address'], str(form.cleaned_data['units']), form.cleaned_data['name'], form.cleaned_data['year']))
            db.commit()
            db.close()
            return HttpResponseRedirect("/apt_building")
    return render(request, template, {"form":form})

def delete_apt(request, apt_name):
    db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
    cur = db.cursor()
    sql = "delete from apt_building where address = '" + apt_name +"'"
    print(sql)
    cur.execute(sql)
    db.commit()
    db.close()
    return redirect('apt_building')

def view_landlords(request):
    db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
    cur = db.cursor()
    cur.execute("select * from landlord")
    data = []
    for row in cur.fetchall():
        data.append(landlord(row[0], row[1], row[2], row[3], ""))
    db.close()
    template = "view_landlords.html"
    return render(request, template, {"data":data})

def delete_landlord(request, comp_name):
    db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
    cur = db.cursor()
    sql = "delete from landlord where company_name = '" + comp_name +"'"
    cur.execute(sql)
    db.commit()
    db.close()
    return redirect('view_landlords')

def view_units(request):
    db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
    cur = db.cursor()
    cur.execute("select * from unit")
    data = []
    for row in cur.fetchall():
        data.append(unit(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
    db.close()
    template = "view_units.html"
    return render(request, template, {"data":data})

def delete_unit(request, unit_add, apt_num):
        db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
        cur = db.cursor()
        sql = "delete from unit where address = '" + unit_add +"' and apt_number = " + str(apt_num)
        cur.execute(sql)
        db.commit()
        db.close()
        return redirect('view_units')

def update_unit(request, unit_add, apt_num):
    template = 'update_unit.html'
    db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
    cur = db.cursor()
    cur.execute("select * from unit where address = '" + unit_add +"' and apt_number = " + str(apt_num))
    data = []
    for row in cur.fetchall():
        data.append(unit(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
    this_unit = data[0]
    db.close()
    if request.method == "GET":
        form = unit_form({"occupied":this_unit.occupied.replace(' ', ''), "furnished":this_unit.furnished, "sq_footage":this_unit.sq_footage, "num_bathrooms":this_unit.num_bathrooms, "num_bedrooms":this_unit.num_bedrooms, "internet":this_unit.internet, "laundry":this_unit.laundry, "kitchen":this_unit.kitchen})
    else:
        form = unit_form(request.POST)
        if form.is_valid():
            db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
            cur = db.cursor()
            sql = "UPDATE unit SET occupied = '"+form.cleaned_data["occupied"]+"', furnished = '" + form.cleaned_data["furnished"]+"', sq_footage = "+ str(form.cleaned_data["sq_footage"])+", num_bathrooms = "+ str(form.cleaned_data["num_bathrooms"])+ ", num_bedrooms = "+ str(form.cleaned_data["num_bedrooms"])+ ", internet = '"+form.cleaned_data["internet"] + "', laundry = '" + form.cleaned_data["laundry"] + "', kitchen = '" + form.cleaned_data["kitchen"] + "' WHERE address = '" + unit_add + "' and apt_number = " + apt_num
            cur.execute(sql)
            db.commit()
            db.close()
        return redirect('view_units')
    return render(request, template, {"form":form, "unit" : this_unit})

def lease_unit(request, unit_add, apt_num):
    if request.method == "GET":
        form = lease_form({"apt_address":unit_add, "apt_number":apt_num})
        template = "new_lease.html"
        return render(request, template, {"form":form})
    else:
        form = lease_form(request.POST)
        if form.is_valid():
            db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
            cur = db.cursor()
            sql = "UPDATE unit SET occupied = 'yes' WHERE address = '" + unit_add + "' and apt_number = " + apt_num
            cur.execute(sql)
            db.commit()
            sql = "INSERT INTO lease(computing_id, apt_address, apt_number, rent_amount, term) values('{0}','{1}','{2}','{3}','{4}')".format(form.cleaned_data['computing_id'], form.cleaned_data['apt_address'], form.cleaned_data['apt_number'], form.cleaned_data['rent_amount'], form.cleaned_data['term'])
            try:
                cur.execute(sql)
                db.commit()
                db.close()
            except Exception as e:
                print(e)

        return redirect('view_leases')

def view_leases(request):
    db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
    cur = db.cursor()
    cur.execute("select * from lease")
    data = []
    for row in cur.fetchall():
        data.append(lease(row[0], row[1], row[2], row[3], row[4]))
    db.close()
    template = "view_lease.html"
    return render(request, template, {"data":data})

def delete_lease(request, cid):
    db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
    cur = db.cursor()
    sql = "delete from lease where computing_id = '" + cid + "'"
    cur.execute(sql)
    db.commit()
    db.close()
    return redirect('view_leases')

def create_tenant(request):
    template = 'create_tenant.html'
    if request.method == "GET":
        form = tenant_form()
    else:
        form = tenant_form(request.POST)
        if form.is_valid():
            db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
            cur = db.cursor()
            cur.execute("insert into tenant(computing_id, name, perm_address, current_address, phone_number, email_address) values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(form.cleaned_data["computing_id"], form.cleaned_data["name"], form.cleaned_data["perm_address"], form.cleaned_data["current_address"], form.cleaned_data["phone_number"], form.cleaned_data["email"]))
            db.commit()
            db.close()
            return HttpResponseRedirect("/tenant/")
    return render(request, template, {"form":form})

def tenants(request):
    db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
    cur = db.cursor()
    cur.execute("SELECT * FROM tenant")
    data = []
    for row in cur.fetchall():
        data.append(tenant(row[0], row[1], row[2], row[3], row[4], row[5]))
    db.close()
    template = "tenant.html"
    return render(request, template, {"data":data})

def delete_tenants(request, cid):
    db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
    cur = db.cursor()
    sql = "DELETE FROM tenant where computing_id = '" + cid + "'"
    cur.execute(sql)
    db.commit()
    db.close()
    return redirect('tenant')

def get_num_available(request):
    db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
    cur = db.cursor()
    cur.execute("select building_name, address, count(apt_number) from apt_building natural join (select * from unit where occupied = 'no ') as t group by building_name")
    data = []
    for row in cur.fetchall():
        data.append(available_apt(row[0], row[1], row[2]))
    db.close()
    template = "view_available_apt.html"
    return render(request, template, {"data":data})
def update_tenants(request, cid):
    template = 'update_tenant.html'
    db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
    cur = db.cursor()
    cur.execute("SELECT * FROM tenant where computing_id = '" + cid +"'")
    data = []
    for row in cur.fetchall():
        data.append(tenant(row[0], row[1], row[2], row[3], row[4], row[5]))
    this_tenant = data[0]
    db.close()
    if request.method == "GET":
        form = tenant_form({"computing_id":this_tenant.computing_id.replace(' ', ''),"name":this_tenant.name,"perm_address":this_tenant.perm_address,"current_address":this_tenant.cur_address,"email":this_tenant.email_address})
    else:
        form = tenant_form(request.POST)
        if form.is_valid():
            db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
            cur = db.cursor()
            sql = "UPDATE tenant SET perm_address = '"+form.cleaned_data["perm_address"]+"', current_address='"+ form.cleaned_data["current_address"]+"', email_address = '"+ str(form.cleaned_data["email"])+"' WHERE computing_id = '"+str(cid)+"'"
            print(sql)
            cur.execute(sql)
            db.commit()
            db.close()
        return redirect('tenant')
    return render(request, template, {"form":form, "tenant" : this_tenant})
def update_maintains(request, apt_addr):
    template = 'update_maintains.html'
    db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
    cur = db.cursor()
    cur.execute("select * from landlord natural join maintains where apt_address = '" + apt_addr + "'")
    data = []
    for row in cur.fetchall():
        data.append(landlord(row[0], row[1], row[2], row[3], row[4]))
    this_maintains = data[0]
    db.close()
    if request.method == "GET":
        form = maintains_form({"phone_number":this_maintains.phone_number, "email_address":this_maintains.email_address})
    else:
        form = maintains_form(request.POST)
        if form.is_valid():
            db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
            cur = db.cursor()
            sql = "UPDATE landlord natural join maintains SET phone_number = '"+ str(form.cleaned_data["phone_number"])+"', email_address = '"+ str(form.cleaned_data["email_address"])+"' WHERE apt_address = '"+apt_addr+"'"            
            cur.execute(sql)
            db.commit()
            db.close()
        return redirect('view_maintains')
    return render(request, template, {"form":form, "maintains" : this_maintains})
def delete_maintains(request, apt_addr):
    db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
    cur = db.cursor()
    sql = "delete from maintains where apt_address = '" + apt_addr +"'"
    cur.execute(sql)
    db.commit()
    db.close()
    return redirect('view_maintains')
def view_maintains(request):
    db = MySQLdb.connect(host='mysql.cs.virginia.edu',user= 'elh5wc',password='pSuR6c3g',port=3306, database = 'elh5wc_HoosHouse')
    cur = db.cursor()
    cur.execute("Select * from landlord natural join maintains")
    data = []
    for row in cur.fetchall():
        data.append(landlord(row[0], row[1], row[2], row[3], row[4]))
    db.close()
    template = "view_maintains.html"
    return render(request, template, {"data":data})
