import jira.client
from jira.client import JIRA


jira_options={'server': 'https://jira.com'}
jira=JIRA(options=jira_options,basic_auth=('admin','password'))

 

issues_in_project = jira.search_issues('JQL',startAt=0, maxResults=2000, validate_query=True, fields=None, expand=None, json_result=None)

print (issues_in_project)
WARNING:root:Got recoverable error from GET http://alifsemi.atlassian.net/rest/api/2/serverInfo, will retry [1/3] in 19.5001791337s. Err: 401 Unauthorized
AENp4e2PGrxvWqQSnb995262


options = {'server': 'YOUR SERVER NAME'}
jira = JIRA(options, basic_auth=('YOUR EMAIL', 'YOUR PASSWORD'))
size = 100
initial = 0
while True:
    start= initial*size
    issues = jira.search_issues('project=<NAME OR ID>',  start,size)
    if len(issues) == 0:
        break
    initial += 1
    for issue in issues:
        print 'ticket-no=',issue
        print 'IssueType=',issue.fields.issuetype.name
        print 'Status=',issue.fields.status.name
        print 'Summary=',issue.fields.summary

        
        
        from jira import JIRA    
        
        
        http://10.10.4.200:9090/#/VE/VC9QSUeTtaB9eMcfbZFVnFlifr9dSJgXlsdaAQ==$MTAwMDA3NTphc2hpc2gubmFuZGFuQGFsaWZzZW1pLmNvbQ==

# Server Authentication
username = "XXXXXX"
password = "XXXXXX"

jira = JIRA(options, basic_auth=(str(username), str(password)))

# Get instance of the ticket
issue = jira.issue('PROJ-1')

# Upload the file
with open('/some/path/attachment.txt', 'rb') as f:
    jira.add_attachment(issue=issue, attachment=f)
  
  
  
  
2010420e82e2101220202064a8ed300fc0c0000000380200080403a023e2d402f2bc02f2851800
57fffffff072

*for p in $(rpm -qa); do rpm –setperms $p; done**

$ curl -s --request GET --netrc $REST_URL/changes/I64f1c892c13a9bad903955678f104c34f36d1079 | sed 1d | jq --raw-output "._number"
$ 32151
