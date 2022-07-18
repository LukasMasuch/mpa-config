import streamlit_patches as st

url = "https://www.notion.so/streamlit/Johannes-MPA-v2-idea-1869aafe213b45fabb090db9cae845c1"

## Common elements

st.sidebar.write("Common sidebar element")

"# Common header!"

"### [Give feedback here](url)"

## Pages


def function_example():
    st.write(
        """
        ## Example
        This is a function!
        """
    )

import time

time.sleep(1)

show = st.checkbox("Show page two")

st.page("example_one.py", name="Home!", icon="🍔")

st.page("example_four.py", icon="🦊")

st.page("example_three.py", name="Custom name!", icon="🔥")


time.sleep(1)


if show:
    st.page("example_two.py", icon="⭐")

st.page(function_example, icon="🌊")
