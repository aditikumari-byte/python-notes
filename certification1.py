def add_setting(settings_dict,setting_tuple):
    key,value = setting_tuple
    key = str(key).lower()
    value = str(value).lower()
    
    if key in settings_dict:
        return f"Setting {key} already exists! Cannot add a new setting with this name."
    else:
        settings_dict[key]=value
        return f"Setting '{key}' added with value '{value}' successfully!"
my_setting = {'theme':'dark'}
new_data = ('fontsize',14)      
print(add_setting(my_setting,new_data))                
print("current dictionary:", my_setting)