import re   #importing regex module to help check for valid formats
from datetime import datetime       #needed for the date validator
class DataValidator:

    '''These are some of the possible email formats gotten from the web:
    john.doe@example.com
    jane.smith@company.co.uk
    john+newsletter@example.com
    user+tag@domain.org
    user123@example.com
    987654@domain.net
    first-last@company-name.com
    user_name@domain.org
    info@sub.example.com
    support@mail.department.co.uk
    contact@university.education
    admin@corporation.solutions
    user@state.gov
    officer@army.mil
    admin@company123.com
    user@mail4you.net
    a@domain.com
    x@mail.net'''
    def validate_email(self, email):        #defining the validate_email to accept only email
       regex_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'        # catering for all possible cases of email listed above
       valid=re.fullmatch(regex_pattern, email) #This checks if the entire date string exactly matches the given regex pattern. 
       if valid:
          return f"{email} is valid"
       else:
          return f"{email} is not valid"
          
    
    '''For phone number validator, I will consider three formats
    i. with country code and plus sign at the beginning e.g +14155552671 (USA), +447911123456 (UK), +2348023456789 (Nigeria)
    ii. with country code and no plus sigh at the begining e.g 14155552671, 447911123456, 2348023456789
    iii. without country code, just local dial format e.g 4155552671 (USA), 07911123456 (UK), 08023456789 (Nigeria)
    iv. with dash after the country code e.g +1-4155552671 (USA), +44-7911123456 (UK), +234-8023456789 (Nigeria)'''
    def validate_phone(self, phone):    #defining the validate_phone to accept only one feature: phone
       regex_pattern = r'^(\+?[0-9]{1,3}-?)?[0-9]{7,15}$'   #optional +, optional up to 3 digits with/without '-', compulsory 7 to 15 digits at the end
       valid=re.fullmatch(regex_pattern, phone)
       if valid:
          return f"{phone} is valid"
       else:
          return f"{phone} is not valid"


    '''For date validator, I will consider the following date formats and define regex pattern for each of them
       YYYY-MM-DD (2025-03-12)
       YYYY/MM/DD (2025/03/12)
        DD-MM-YYYY (12-03-2025)
        DD/MM/YYYY (12/03/2025)
       DD-MMM-YYYY (12-Mar-2025)
       DD-Month-YYYY (12-March-2025)
      MMM DD, YYYY (Mar 12, 2025)
      Month DD, YYYY (March 12, 2025)'''
    
    def validate_date(self, date):
       regex_pattern = [(r'^\d{4}-\d{1,2}-\d{2}$', "%Y-%m-%d"),
                        (r'^\d{4}/\d{1,2}/\d{2}$', "%Y/%m/%d"),
                        (r'^\d{2}-\d{2}-\d{4}$', "%d-%m-%Y"),
                        (r'^\d{2}/\d{2}/\d{4}$', "%d/%m/%Y"),
                        (r'^\d{2}-[A-Za-z]{3}-\d{4}$', "%d-%b-%Y"),
                        (r'^\d{2}-[A-Za-z]-\d{4}$', "%d-%b-%Y"),
                        (r'^[A-Za-z]{3}\s\d{2},\s\d{4}$', "%b %d, %Y"),
                        (r'^[A-Za-z]\s\d{2},\s\d{4}$', "%b %d %Y")]
       for pattern, format in regex_pattern:
        if re.fullmatch(pattern, date):     #This checks if the entire date string exactly matches the given regex pattern. 
              try:
                datetime.strptime(date, format)     #This parses a string into a datetime object based on the provided format.
                return f"{date} is valid" # when date is valid
              except ValueError:
                return f"{date} is not valid"  # If invalid date is entered e.g, 31st Feb
       
       return f"{date} does not match defined pattern"  # If no regex matches

    
    '''Here's a breakdown of the common components of a URL: 
    1. Scheme (Protocol):
    This specifies how the browser should handle the request (e.g., http://, https://, ftp://, file://, mailto://, 
    ws://, wss://, mailto://, tel://, sms://, magnet://). 

    2. Optional username:password@:
    The "Optional username:password@" format is used for authentication in URLs. It allows you to specify credentials 
    directly in the URL before accessing a resource, typically used in FTP, HTTP, and other network protocols.
    For example-https://admin:secret@secure.example.com:8080/dashboard

    3. Hostname:
    This is the domain name, such as www.example.com.
    It can also include a subdomain (e.g., blog.example.com). 

    4. Optional path:
    This indicates the location of the resource on the server (e.g., /index.html, /about/). 

    5. Optional Query Parameters:
    These are optional parameters that are sent to the server (e.g., ?name=John&age=30).
    They are separated by & and consist of a key-value pair. 
    5. Fragment:
    This is an optional part of the URL that allows you to link to a specific section of a page (e.g., #section1). 
    ---Source: Google
    
    I will consider all these components to structure the regex pattern'''
    def validate_url(self, url):
       regex_pattern = r'^(https?|ftp|file|mailto|ws|wss|mailto|tel|sms|magnet):\/\/([\w.-]+(?::\w+)?@)?([a-zA-Z0-9.-]+|\[[0-9a-fA-F:]+\])(?::\d{1,5})?(?:[/?#][^\s]*)?$'
       valid=re.fullmatch(regex_pattern, url)
       if valid:
          return f"{url} is valid"
       else:
          return f"{url} is not valid"
       