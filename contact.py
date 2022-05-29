import streamlit as st

def app():
    st.header(":mailbox: Please send me your feedabek!")
    
    contact_form = """
    <form action="https://formsubmit.co/mmoralls0@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required><br><br>
        <input type="email" name="email" placeholder="Your email" required><br><br>
        <textarea name="message" placeholder="Your message here"></textarea><br>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    local_css("style/style.css")