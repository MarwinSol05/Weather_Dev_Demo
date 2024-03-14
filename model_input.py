def get_region_country():

    reg_cty = { 
        'Europe' : ['UK', 'France', 'Germany', 'Italy', 'Netherlands', 'Spain'],
        'Asia' : ['China', 'India', 'Hong Kong', 'Japan'],
        'Africa': ['South Africa'],
        'Australasia': ['Australia', 'New Zealand'],
        'Middle East': ['Kuwait'],
        'North America': ['USA- CONUS', 'USA- CAISO', 'Canada', 'Jamaica'],
        'South America' : ['Argentina', 'Brazil', 'Chile', 'Colombia']
    }
    
    reg_cty_tree = []
    
    for key, val in reg_cty.items():
        reg_cty_tree.append(
            {
                "value" : key,
                "title" : key,
                "children" : [{"value" : elt, "title" : elt} for elt in val]
            }
        )

    start_cols = ['UK']

    return reg_cty_tree, start_cols