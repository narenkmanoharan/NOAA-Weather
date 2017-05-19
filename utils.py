parameters = ['maxt', 'temp', 'mint', 'pop12', 'sky', 'wspd', 'appt', 'qpf', 'snow', 'wx', 'wgust', 'icons', 'rh']


# Generates the parameter string to append to the url request
def parameter_string_xml():
    parameters_string = []
    for val in parameters:
        parameters_string.append("%s=%s" % (val, val))
    parameter = '&'.join(parameters_string)
    return parameter
