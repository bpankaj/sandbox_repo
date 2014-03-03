from bottle import get, post, request,route, run, template,put,delete
patient_dict = {}
display_list=[]

@route('/')
@route('/patient')
def patient():
	""" Function that show whats operation to perform! """
	return '<b>Patient is working create, update, delete</b>!'

@post('/patient')
def patient_create():
	""" Function that create patient information! """
	patient_id = request.POST['id']
	patient_name = request.POST['name']
	patient_gender = request.POST['gender']
	patient_age = request.POST['age']
	patient_address = request.POST['address']
	patient_phone = request.POST['phone']
	display_list = [patient_name,patient_gender,patient_age,patient_address,patient_phone]
	patient_dict.update({patient_id:display_list})
	return patient_dict

@get('/patient/<id>')
def patient_read(id):
	""" Function that return all the information of patient! """
	return patient_dict[id]

@put('/patient/<id>')
def patient_update(id):
	""" Function that update existing records of patient! """
	patient_name = request.POST['name']
	patient_gender = request.POST['gender']
	patient_age = request.POST['age']
	patient_address = request.POST['address']
	patient_phone = request.POST['phone']
	update_patient=[patient_name,patient_gender,patient_age,patient_address,patient_phone]
	patient_dict[id]=update_patient
	return patient_dict

@delete('/patient/<id>')
def patient_delete(id):
	""" Function that delete patient information! """
	del(patient_dict[id])
	return patient_dict

run(host='localhost', port=8080)
