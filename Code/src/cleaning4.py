import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import re
import numpy

import re
def limpieza2(x):
    x=re.findall('[0-9.]+',str(x))
    if len(x)>0:
        return x[0]
    else:
        return 0

def room(x):
    if 'bed and breakfast'in x:
        return 'bed and breakfast'
    elif 'rental unit'in x:
        return 'house'
    elif 'hostel' in x:
        return 'hostel'
    elif 'condominium' in x:
        return 'condominium'
    elif 'townhouse' in x:
        return 'house'
    elif 'hotel' in x:
        return 'hotel'
    elif 'villa' in x:
        return 'house'
    elif 'chalet' in x:
        return 'house'
    elif 'apartment' in x:
        return 'apartment'
    elif 'house' in x:
        return 'house'
    elif 'home' in x:
        return 'house'
    elif 'houseboat' in x:
        return 'house'
    elif 'loft' in x:
        return 'apartment'
    elif 'guest' in x:
        return 'house'
    elif 'farm' in x:
        return 'house'
    elif 'boat' in x:
        return 'boat'
    elif 'bungalow' in x:
        return 'house'
    elif 'lodge' in x:
        return 'house'
    elif 'resort' in x:
        return 'resort'
    elif 'castle' in x:
        return 'castle'
    elif 'casa' in x:
        return 'house'
    elif 'tipi' in x:
        return 'bungalow'
    else:
        return '-'

def sales(x):
    if x>=600:
        return 600
    else:
        return x

def rev(x):
    if x>=400:
        return 400
    else:
        return x








