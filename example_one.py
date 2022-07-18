from pathlib import Path

import streamlit as st

other_code, pages_code = Path("streamlit_app.py").read_text().split("## Pages")

common_elements = other_code.split("## Common elements")[1]


f"""
### This is the first page (`example_one.py`), loaded by default (because it's the first st.page in streamlit_app.py)

Note that the pages list in the sidebar is generated by the following code in streamlit_app.py:

```python
{pages_code}
```

And the common elements are generated by the following code:

```python
{common_elements}
```

The rest of the code in these pages is from the individual python files
or the function code.
"""
