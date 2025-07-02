import streamlit as st
from user import admin , coustomer
from notifier import emailnotifier,pushnotifier,SMSnotifier

admin1=admin("pruthvirajgawande2@gmail.com","Pruthviraj Gawande",9423109104)
cust=coustomer("shantyacool@gmail.com","Shantanu Gawande",7020696650)

notifiers={"Email":emailnotifier(),
    "SMS":SMSnotifier(),
    "Push":pushnotifier()}
    
st.title(" 📣Smart Notifications System")
user_type=st.sidebar.selectbox("Select Your Usertype",["Admin","customer"])
if user_type=="Admin":
    user=admin1
else:
    user=cust

notifier_type=st.selectbox("Chosse Notification",["Email","SMS","Push"])
message=st.text_area("Enter a message")

if st.button("Send Notification"):
    st.balloons()
    notifier = notifiers[notifier_type]
    notifier.send(message, user)
    st.success("✅ Notification sent!")


if user_type==admin:
    with st.expander("User Info"):
        st.write("**Name:**", user.n)
        st.write("**Email:**", user.get_email())
        st.write("**Phone:**", user.get_phone())
else:
    with st.expander("User Info"):
        st.write("**User Type:**", user_type)
        st.write("**Name:**", user.n)
        st.write("**Email:**", user.get_email())
        st.write("**Phone:**", user.get_phone())

