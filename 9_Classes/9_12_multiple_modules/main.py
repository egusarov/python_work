# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly.


from admin import Admin

admin = Admin('cillian', 'murphy', 47, 'married')
admin.actions.show_privileges()