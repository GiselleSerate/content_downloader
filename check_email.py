from guerrillamail import GuerrillaMailSession

session = GuerrillaMailSession(email_address='phoenix@guerrillamailblock.com')
print(session.get_session_state()['email_address'])
email_list = session.get_email_list()
for email_summary in email_list:
    email = session.get_email(email_summary.guid)
    print(email.body)

# hqt7en+3x1o341y10qc@sharklasers.com