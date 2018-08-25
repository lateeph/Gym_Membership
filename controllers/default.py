
def home():
    return dict()

def register():
	return dict()

def store():
	submitted_firstname = request.vars.firstname
	submitted_lastname = request.vars.lastname
	submitted_phonenumber = request.vars.phonenumber
	submitted_gender = request.vars.gender
	submitted_email = request.vars.email
	submitted_password = request.vars.password

	results = db.users.insert(
		db_firstname=submitted_firstname,
		db_lastname=submitted_lastname,
		db_phonenumber=submitted_phonenumber,
		db_gender=submitted_gender,
		db_email=submitted_email,
		db_password=submitted_password
	)

	if results:
		return "User Saved Successfully"
	else:
		return "An Error Occured"

def seeUsers():
	users =db().select(db.users.ALL)
	return dict(users=users)


def login():
	return dict()

def charges():
	return dict()

def schedule():
	return locals()
