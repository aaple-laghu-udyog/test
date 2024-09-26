def lambda_handler(event, context):
    message = 'Hello Product Owner {} {}!'.format(event['first_name'], event['last_name'])
    return {
        'message' : message
    }