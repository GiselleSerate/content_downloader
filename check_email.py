from guerrillamail import GuerrillaMailSession
from bs4 import BeautifulSoup


session = GuerrillaMailSession(email_address='phoenix@guerrillamailblock.com')
print(session.get_session_state()['email_address'])
email_list = session.get_email_list()
for email_summary in email_list:
    email = session.get_email(email_summary.guid)
    mailsoup = BeautifulSoup(email.body, 'html5lib')
    try:
        header = mailsoup.find('h1')
        otpElement = header.find_next_sibling('p').find_next_sibling('p')
        otpCode = otpElement.string.strip()
        print(otpCode)
    except Exception as e:
        print(e)
        print('Didn\'t get OTP code') # TODO handle errors better. 

# hqt7en+3x1o341y10qc@sharklasers.com