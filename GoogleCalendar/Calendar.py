from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import re

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'
reviewDayIntervals = [3,7,14,21,28,60,90]

def getAdditionalReviewDates():
    '''Gets the dates for the recurring date field, these will be all 
       the days I want to review memory information. Presently it is
       today +3 days, +7, 14, 21, 28, 60, 90. 
    
    Returns:
        [str] -- A list of dates
    '''
    dates = ''

    # Tomorrow is the first event occurrence, so everything is referenced from that
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)

    for day in reviewDayIntervals:
        dates += ( tomorrow + datetime.timedelta(days=day)).strftime('%Y%m%d')+','

    return dates.rstrip(',')

def createEvent(title, time):
    
    # Add one day and the specified time for the first event
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    firstDate = datetime.datetime.combine(tomorrow, time).astimezone()
    endDate = firstDate.replace(hour=firstDate.hour+1)

    event = {
        'summary': title,
        'description': 'Review content',
        'start': {
            'dateTime': firstDate.isoformat(),
            'timeZone': 'America/Los_Angeles'
        },
        'end': {
            'dateTime': endDate.isoformat(),
            'timeZone': 'America/Los_Angeles'
        },
        'transparency': 'transparent',
        'visibility': 'private',
        'colorId': '10',
        'reminders': {
            'useDefault': False,
            'overrides': [{
                'method': 'popup',
                'minutes': 0
            }]
        },
        'recurrence': [
            'RDATE;VALUE=DATE:' + getAdditionalReviewDates(),
            'RRULE:FREQ=MONTHLY;INTERVAL=6'
        ]
    }

    return event


    #     }
#   ]

### Could be handy ###
#   'source': {
#     'url': string,
#     'title': string
#   },
#   'attachments': [
#     {
#       'fileUrl': string,
#       'title': string,
#       'mimeType': string,
#       'iconLink': string,
#       'fileId': string
#     }

def main():
    '''Adds memorizations that I want to review on my Google Calendar 
    in specified intervals
    '''
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('./../data/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Should get some user input here
    title = input('Event Name: ')

    while not title:
        title = input('Event name is required, enter it here: ')

    timeInput = input('Event Time: ')
    
    timeData = re.match('(\d{1,2})\s*:\s*(\d{1,2})\s*(am|pm)?', timeInput)
    hour = 10
    minute = 0

    if timeData :
        hour = int(timeData.group(1))
        minute = int(timeData.group(2))

        if timeData.group(3) and timeData.group(3) == 'pm' and hour != 12:
            hour += 12


    event = createEvent(title, datetime.time(hour, minute))

    response = service.events().insert(calendarId='primary', body=event).execute()

    print(response)



if __name__ == '__main__':
    main()