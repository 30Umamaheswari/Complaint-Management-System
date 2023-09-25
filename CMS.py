from email.mime.text import MIMEText

import streamlit as st
import smtplib


def submit_msg(c, a):
    mail = c

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    s.login("Sender_Mail_id", "Password")

    subject = "Complaint Submission Confirmation"
    recipient_name = a

    # message to be sent
    message = MIMEText(f"""
        Dear {recipient_name},

        We are writing to inform you that your complaint has been successfully submitted. Your complaint token was generated successfully.
        I inform you that your issue will be resolved within 48 hours.

        If you have any further questions or require assistance, please do not hesitate to contact our customer support team.

        Thank you,
        Sincerely,
        Uma Maheswari.
        """)

    message['Subject'] = subject

    # sending the mail
    s.sendmail("Sender_mail_id", mail, message.as_string())
    if s:
        msg = 'Your Complaint has been successfully submitted. Please check your email for further details.'

    # Terminating the session
    s.quit()

    return msg


def email(mail_id):
    flag = False
    if '@' not in mail_id and '.' not in mail_id:
        flag = False
    s1 = mail_id.index('@')
    s2 = mail_id.index('.')
    if mail_id.count('@') == 1 and mail_id.count('.') == 1:
        flag = True
    if (s2 - s1) > 4 and s1 > 2 and mail_id.endswith('.com'):
        flag = True
    else:
        flag = False
    return flag


def inputs():
    col1, col2 = st.columns([0.2,0.7])

    x = col2.text_input('User Name')
    y = col2.text_input('Email Id')

    if y:
        if email(y):
            col2.markdown(f'<div style="color: darksalmon; font-weight: bold; font-size: 20px;">Mail_id is verified</div>',
                        unsafe_allow_html=True)
        else:
            col2.markdown(
                f'<div style="color: darksalmon; font-weight: bold; font-size: 20px;">Please, enter the valid '
                f'mail_id</div>',
                unsafe_allow_html=True)
    z = col2.text_input("Enter your complaint here, it should be minimum 120 characters")

    if z:
        if len(z) <= 120:
            col2.markdown(
                f'<div style="color: darksalmon; font-weight: bold; font-size: 20px;">Please, enter minimum \'120\' characters</div>',
                unsafe_allow_html=True)

    return x, y, z


if __name__ == '__main__':
    st.set_page_config(page_title='Complaint Management System',
                       layout='centered')
    page_bg_image = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://images.pexels.com/photos/7457656/pexels-photo-7457656.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
    
    base="light";
    primaryColor="#bf8068";
    backgroundColor="#a0522d";
    secondaryBackgroundColor="#AD7359";

    width: 100vw;
    height: 100vh;
    margin: 0;
    padding: 0;
    }
    </style>
    """

    st.markdown(page_bg_image, unsafe_allow_html=True)

    app_title = """
    color: royalblue;
    text-align: center;
    font-family: Serif;
    font-size: 50px;
    """
    st.markdown(f'<h1 style="{app_title}">Complaint Box</h1>', unsafe_allow_html=True)

    a, b, c = inputs()

    c1, c2 = st.columns([0.2,0.7])

    c2.markdown(f'<div style="display: flex; align-items: center;"><div style="color: brown; font-weight: bold; font-size: 20px;">Name:</div><div style="margin-left: 10px;">{a}</div></div>', unsafe_allow_html=True)
    c2.markdown(f'<div style="display: flex; align-items: center;"><div style="color: brown; font-weight: bold; font-size: 20px;">Mail Id:</div><div style="margin-left: 10px;">{b}</div></div>', unsafe_allow_html=True)
    c2.markdown(f'<div style="display: flex; align-items: center;"><div style="color: brown; font-weight: bold; font-size: 20px; margin-bottom: 70px">Complaint:</div><div style="margin-left: 10px; margin-top: 10px">{c}</div></div>', unsafe_allow_html=True)

    # c2.markdown(
    #     """
    #     <style>
    #     .centered-button {
    #         display: flex;
    #         justify-content: center;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True,
    # )

    if c2.button('Submit', key="centered-submit-button"):
        d = submit_msg(b, a)

        c2.markdown(f'<div style="color: indianred; font-weight: bold; font-size: 20px;">{d}</div>', unsafe_allow_html=True)


