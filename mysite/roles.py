from rolepermissions.roles import AbstractUserRole

class Administrator(AbstractUserRole):
	available_permissions = {
		'add_new_post':True,
		'edit_old_post':True,
		}

class Viewer(AbstractUserRole):
	available_permission = {
		'add_new_post':True,
	}
	