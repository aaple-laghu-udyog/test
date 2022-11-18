def lambda_handler(event, context):
    message = 'Hello Product {} {}!'.format(event['first_name'], event['last_name'])
    return {
        'message' : message
    }