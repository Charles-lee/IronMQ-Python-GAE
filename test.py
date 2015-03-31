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
