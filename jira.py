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

# Server Authentication
username = "XXXXXX"
password = "XXXXXX"

jira = JIRA(options, basic_auth=(str(username), str(password)))

# Get instance of the ticket
issue = jira.issue('PROJ-1')

# Upload the file
with open('/some/path/attachment.txt', 'rb') as f:
    jira.add_attachment(issue=issue, attachment=f)
