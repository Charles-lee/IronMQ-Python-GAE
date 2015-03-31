# IronMQ-Python-GAE
Simple IronMQ python client for Google App Engine.
It solves the issue related requests v2.3.0 which is a library not working when you use iron_mq_python(https://github.com/iron-io/iron_mq_python) on Google App Engine.

## How to use
    from ironmq import IronMQ
      
    ironmq = IronMQ(
       token = 'your_OAuth_token',
       project_id = 'your_project_id'
    )
    
    print 'POST'
    ironmq.post(queue_name='my_queue', messages=['Hello world'])
    
    print 'GET'
    msgs = ironmq.get(queue_name='my_queue')
    msg = msgs['messages'][0]
    
    print msg['body']
    
    print 'DELETE'
    ironmq.delete(queue_name='my_queue', message_id=msg['id'])
    
    print 'END'
