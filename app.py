import json
import streamlit as st
from streamlit.web.server.websocket_headers import _get_websocket_headers

def get_user_info():
    headers = _get_websocket_headers()
    user_info_json = headers.get("Rstudio-Connect-Credentials")
    if user_info_json is None:
        return None
    return json.loads(user_info_json)

def get_username():
    user_info = get_user_info()
    if user_info is None:
        return None
    return user_info.get("user")


st.write("_get_websocket_headers(): " + str(_get_websocket_headers()))
st.write("_get_websocket_headers().get(Rstudio-Connect-Credentials): user info before json loads" + str(_get_websocket_headers().get("Rstudio-Connect-Credentials")))
st.write("get_user_info(): after json loads:" + str(get_user_info()))
st.write("Username: get(user)" + str(get_username()))
         