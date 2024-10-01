import pandas as pd
import hashlib 
import re

## replace and fillna
def replace_fillna(df, column_name, replace_dict=None, fill_value=None):
    if replace_dict:
        df[column_name] = df[column_name].replace(replace_dict)
    if fill_value is not None:
        df[column_name] = df[column_name].fillna(fill_value)
    return df

# format clean telephone

def format_phone(phone):
    if pd.isna(phone):
        return phone
    else:
        phone_str = str(phone)
        phone_str = phone_str.split(".")[0]
        return f"+{phone_str[:2]} {phone_str[2:5]} {phone_str[5:7]} {phone_str[7:9]} {phone_str[9:]}"

# Obtainin phone code number

def country_code(value, skip_value="Sin completar"):
    if value == skip_value:
        return value
    else:
        return str(value).split(" ")[0]
    
def apply_country_code(df, column_name, new_column_name, skip_value="Sin completar"):
    df[new_column_name] = df[column_name].apply(lambda x: country_code(x, skip_value))
    return df[new_column_name]

# Obtainin country through phone code

def country(code, skip_value="Sin completar"):
    country_by_code = {
"+34": "España",
"+52": "México",
"+56": "Chile",
"+54": "Argentina",
"+57": "Colombia",
"+59": "Bolivia",
"+50": "Guatemala",
"+51": "Perú",
"+39": "Italia",
"+41": "Suiza",
"+58": "Venezuela",
"+17": "Estados Unidos",
"+19": "Canadá",
"+61": "Australia",
"+12": "Estados Unidos",
"+18": "Estados Unidos",
"+33": "Francia",
"+44": "Reino Unido",
"+49": "Alemania",
"+96": "Bahréin",
"+15": "Estados Unidos",
"+55": "Brasil",
"+13": "Estados Unidos",
"+16": "Estados Unidos",
"+97": "Emiratos Árabes Unidos",
"+32": "Bélgica",
"+35": "Gibraltar",
"+14": "Estados Unidos",
"+38": "Yugoslavia",
"+86": "China",
"+37": "Lituania",
"+84": "Vietnam",
"+36": "Hungría",
"+46": "Suecia",
"+31": "Países Bajos",
"+48": "Polonia",
"+47": "Noruega",
"+64": "Nueva Zelanda"
}
    
    if code == skip_value:
        return "Desconocido"
    else:
        return country_by_code.get(code)

## Anonimizer functions

def anonymize_name(name):
    return hashlib.md5(name.encode()).hexdigest()[:8]

def anonymize_email(email):
    username, domain = email.split('@')
    return f"{hashlib.md5(username.encode()).hexdigest()[:8]}@{domain}"

def anonymize_phone(phone):
    if phone == "Sin completar":
        return phone
  
    match = re.match(r'(\+\d+)\s*(.*)', phone)
    if match:
        country_code, rest_of_number = match.groups()
      
        rest_of_number = rest_of_number.replace(" ", "")
        return f"{country_code} {hashlib.md5(rest_of_number.encode()).hexdigest()[:8]}"
    else:
      
        return hashlib.md5(phone.encode()).hexdigest()[:8]