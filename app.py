import streamlit as st

from quote.lib import get_quote

quote = get_quote()  # assuming the function returns an author and a quote

f"{quote}"