import json
from google.appengine.api import urlfetch

class IronMQ:
    def __init__(self, token, project_id, uri = 'https://mq-aws-us-east-1.iron.io', version = '1'):
        self.token = token
        self.project_id = project_id
        self.url = uri + '/' + version + '/projects/' + project_id + '/queues/'
        
    def post(self, queue_name, messages):
        form_data = { 'messages':[] }
        
        for msg in messages:
            form_data['messages'].append( {'body': msg } )
            
        form_data = json.dumps(form_data)

        result = urlfetch.fetch(
            url=self.url + queue_name + '/messages', payload=form_data, method=urlfetch.POST,
            headers={'Content-Type': 'application/json', 'Authorization': 'OAuth ' + self.token })
        msgs = { }
         
        if 200 != result.status_code:
            print "status_code: ", result.status_code
        else:
            msgs = json.loads(result.content)
        
        return msgs

    def get(self, queue_name):
        result = urlfetch.fetch(url=self.url + queue_name + '/messages', method=urlfetch.GET,
            headers={'Content-Type': 'application/json', 'Authorization': 'OAuth ' + self.token })
         
        if 200 != result.status_code:
            print "status_code: ", result.status_code
        else:
            msgs = json.loads(result.content)
            
        return msgs
    
    def delete(self, queue_name, message_id):
        result = urlfetch.fetch(url=self.url + queue_name + '/messages/' + message_id, method=urlfetch.DELETE,
            headers={'Content-Type': 'application/json', 'Authorization': 'OAuth ' + self.token})
             
        if 200 != result.status_code:
            print "status_code: ", result.status_code
        else:
            msgs = json.loads(result.content)
        
        return msgs
