import jira.client
from jira.client import JIRA


jira_options={'server': 'https://jira.com'}
jira=JIRA(options=jira_options,basic_auth=('admin','password'))

 

issues_in_project = jira.search_issues('JQL',startAt=0, maxResults=2000, validate_query=True, fields=None, expand=None, json_result=None)

print (issues_in_project)
