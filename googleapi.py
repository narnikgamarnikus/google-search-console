import argparse
import sys
from googleapiclient import sample_tools
from pprint import pprint

def execute_request(service, property_uri, request):
    """Executes a searchAnalytics.query request.

    Args:
      service: The webmasters service to use when executing the query.
      property_uri: The site or app URI to request data for.
      request: The request to be executed.

    Returns:
      An array of response rows.
    """
    return service.searchanalytics().query(
        siteUrl=property_uri, body=request).execute()



# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('property_uri', type=str,
                       help=('Site or app URI to query data for (including '
                             'trailing slash).'))
argparser.add_argument('start_date', type=str,
                       help=('Start date of the requested date range in '
                             'YYYY-MM-DD format.'))
argparser.add_argument('end_date', type=str,
                       help=('End date of the requested date range in '
                             'YYYY-MM-DD format.'))


service, flags = sample_tools.init(
    sys.argv, 'webmasters', 'v3', __doc__, 'client_secrets.json', parents=[argparser],
    scope='https://www.googleapis.com/auth/webmasters.readonly')

# First run a query to learn which dates we have data for. You should always
# check which days in a date range have data before running your main query.
# This query shows data for the entire range, grouped and sorted by day,
# descending; any days without data will be missing from the results.
request = {
    'startDate': flags.start_date,
    'endDate': flags.end_date,
    'dimensions': ['date']
}
response = execute_request(service, flags.property_uri, request)
pprint(response)
