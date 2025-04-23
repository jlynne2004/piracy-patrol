# Home.py
import streamlit as st

st.set_page_config(
    page_title="Plot Twists & Pivot Tables",
    page_icon="📚",
    layout="centered"
)

st.title("Plot Twists & Pivot Tables")
st.subheader("Analytics with heat. Tools with bite.")

st.markdown("""
Welcome to **Plot Twists & Pivot Tables**, your cozy-caffeinated tech hub for indie authors.

Navigate to the tool you need from the sidebar:
- **Backlist Extractor**: Quickly compile your book catalog *(Coming Soon!)*
- **Piracy Patrol**: Scan for pirate links and generate reports [Live!](https://piracy-patrol.streamlit.app/Piracy_Patrol)
- **Release Day Countdown**: Track ARCs, promo tasks, and deadlines *(Coming Soon!)*
- **Series Bible Helper**: Keep character and world details straight *(Coming Soon!)*

More tools coming soon. Got any ideas or feature requests? [Email me](mailto:jessiesreadingcorner@gmail.com) or [Fill out this form](https://forms.gle/pdgBZHfAtGNQDQuFA)
""")