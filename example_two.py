from typing import List

import streamlit as st

from page_config import Page, configure_pages, standard_page_widgets

st.write("Example two!")


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
    {
        "name": "Example Three",
        "icon": "🦊",
    },
]

configure_pages(pages)
