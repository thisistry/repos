import jira.client
from jira.client import JIRA


jira_options={'server': 'https://jira.com'}
jira=JIRA(options=jira_options,basic_auth=('admin','password'))

 

issues_in_project = jira.search_issues('JQL',startAt=0, maxResults=2000, validate_query=True, fields=None, expand=None, json_result=None)

print (issues_in_project)
WARNING:root:Got recoverable error from GET http://alifsemi.atlassian.net/rest/api/2/serverInfo, will retry [1/3] in 19.5001791337s. Err: 401 Unauthorized
AENp4e2PGrxvWqQSnb995262
