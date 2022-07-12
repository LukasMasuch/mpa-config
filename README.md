# Streamlit Multi-Page Configuration

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blackary-mpa-config-streamlit-app-0bp2ol.streamlitapp.com/)

<img width="600" src="https://user-images.githubusercontent.com/7164864/178483961-1f9abf49-eb44-455f-9362-37951daf055a.gif">

### Summary 

Streamlit recently [released multi-page apps](https://blog.streamlit.io/introducing-multipage-apps/) 🎉 where page filenames are the source of truth for page settings. 

In this repository, we show a prototype on how to use a [page_config.yaml](https://github.com/blackary/mpa-config/blob/main/page_config.yaml) to control the ordering, icons, and nesting of the pages in the sidebar of a multi-page Streamlit app.

Features include:

- **Decoupling page settings from filenames.** No need to use indices or emojis in filenames to handle page titles, icons or ordering! You can name your Python scripts however you want.
- **Controling the order of the pages.** Adding pages in the config in the order you want them to appear in the app.
- **Nesting related pages within a "section".** Using `sections` in page_config.yaml will add un-clickable placeholders that group pages together.
- **Adding a created date on each app.** Using the `created_date` field for each page config, the app automatically adds a 🆕 flag to the page title if it is under 30 days old!
- **Displaying some pages in wide-mode.** Using the `layout` field as `'wide'` or `'centered' (default).
- **Automatically adding the icon and title at the top of each page.** Bringing consistency to your pages!

⚠️ This project depends on an API that may change, and is not designed to be used this way,
so this will probably NOT work long-term.


### Get started

1. Install requirements `pip install -r requirements.txt` 
2. Run the Streamlit app `streamlit run streamlit_app.py`
3. Play with the page_config.yaml!


### Documentation

Supported parameters in page_config.yaml for `pages`:
- page_name
- icon
- script_path
- layout
- created_date

Supported parameters in page_config.yaml for `sections`:
- name
- icon
