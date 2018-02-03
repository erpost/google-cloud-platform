for binding in orgInfo['bindings']:
    role = binding['role']
    for member in binding['members']:
        print('Organization,' + org + ',' + member + ',' + role)
