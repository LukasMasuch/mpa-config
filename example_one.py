from tkinter import W
from typing import List

import streamlit as st

from page_config import Page, configure_pages, standard_page_widgets

# Add this on top of any page to make mpa-config work!
# standard_page_widgets()

st.title("This is the first page, loaded by default!")

st.write("Example One")

st.stop()


pages: List[Page] = [
    {
        "name": "Home",
        "path": "streamlit_app.py",
        "icon": "🏠",
    },
    {
        "name": "Example One",
        "icon": "⭐",
    },
    {
        "name": "Example Two",
        "icon": "🦇",
    },
]

configure_pages(pages)
