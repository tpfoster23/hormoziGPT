import streamlit as st
import re


bot_msg_container_html_template = '''
<div style='background-color: #FFFFFF; padding: 10px; border-radius: 5px; margin-bottom: 10px; display: flex'>
    <div style="width: 20%; display: flex; justify-content: center">
        <img src="https://yt3.googleusercontent.com/ixwBtVrollE0Z5nA5YPHrnkKQoK09Evbe4gWCvJlleB2rFERDz3m2Jynhc3sGBE-EnzbH6ov=s176-c-k-c0x00ffffff-no-rj" style="max-height: 50px; max-width: 50px; border-radius: 50%;">
    </div>
    <div style="width: 80%;color:black;">
        $MSG
    </div>
</div>
'''

user_msg_container_html_template = '''
<div style='background-color: #FFFFFF; padding: 10px; border-radius: 5px; margin-bottom: 10px; display: flex'>
    <div style="width: 78%;color:black;">
        $MSG
    </div>
    <div style="width: 20%; margin-left: auto; display: flex; justify-content: center;">
        <img src="https://lh3.google.com/u/0/drive-viewer/AITFw-xnBHfpeMfbepvqQBdTxtYVlh063oxyhbl6CSuPRxeCgjqstf1TRsY2xQdKv8IYhjuZiafLOSTMg5xNXCqhMpybsyrFxg=w590-h1206" style="max-width: 50px; max-height: 50px; float: right; border-radius: 50%;">
    </div>    
</div>
'''

def render_article_preview(docs, tickers):
    message = f"<h5>Here are relevant articles for {tickers} that may answer your question. &nbsp; &nbsp;</h5>"
    message += "<div>"
    for d in docs:
        elipse = " ".join(d[2].split(" ")[:140])        
        message += f"<br><a href='{d[1]}'>{d[0]}</a></br>"
        message += f"<p>{elipse} ...</p>"
        message += "<br>"
    message += "</div>"
    return message

def render_earnings_summary(ticker, summary):
    transcript_title = summary["transcript_title"]
    message = f"<h5>Here is summary for {ticker} {transcript_title} </h5>"
    message += "<div>"
    body =  re.sub(r'^-', r'*  ', summary["summary"])
    body =  re.sub(r'\$', r'\\$', body)
    message += f"<p>{body}</p>"
    message += "</div>"
    return message

def render_stock_question(answer, articles):
    message = "<div>"
    message += f"{answer} &nbsp; <br>"
    message += "Sources: "
    for a in articles:
        message += f"<a href='{a[1]}'>{a[0]}</a><br>"
    message += "</div>"
    return message

def render_chat(**kwargs):
    """
    Handles is_user 
    """
    if kwargs["is_user"]:
        st.write(
            user_msg_container_html_template.replace("$MSG", kwargs["message"]),
            unsafe_allow_html=True)
    else:
        st.write(
            bot_msg_container_html_template.replace("$MSG", kwargs["message"]),
            unsafe_allow_html=True)

    if "figs" in kwargs:
        for f in kwargs["figs"]:
            st.plotly_chart(f, use_container_width=True)

