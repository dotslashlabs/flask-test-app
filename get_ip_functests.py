import json
import urllib2

response = urllib2.urlopen('http://localhost:5000/get_my_ip').read()
ip = json.loads(response)
assert ip['ip'] == '127.0.0.1'

print '==== End of Functional Tests. All Passed. ===='
