# pages/1_Piracy_Patrol.py
import streamlit as st
from googlesearch import search
import pandas as pd
import re
from urllib.parse import urlparse

st.title("Piracy Patrol")
st.markdown("""
            The indie author's secret weapon against book piracy.
            Scan the web for pirate links, report them, and reclaim your books.
            
            This tool is free for self-service use, but if you would like to support its development, consider [buying me a coffee](https://www.buymeacoffee.com/jessiesreadingcorner).
            If you would like someone else to monitor your books for you, please [email me](mailto:jess@jesshaydenconsulting.com) and we can work out a solution for you. I do charge $20 for this service.
            """)
st.subheader("Scan. Report. Reclaim your books.")

book_title = st.text_input("Book Title")
author_name = st.text_input("Author Name")

# Load pirate domains from a CSV (could be expanded later)
try:
    domain_df = pd.read_csv("pirate_domains.csv")
    pirate_domains = domain_df["domain"].tolist()
except:
    pirate_domains = ["zlibrary", "pdfdrive", "epub", "ebookhunter", "pdfcoffee", "libgen", "book4you", "oceanofpdf", "pdfroom", "freebookpdf", "pirate"]

def is_suspicious(url):
    return any(domain in url for domain in pirate_domains)

if st.button("Scan for Piracy"):
    if not book_title or not author_name:
        st.warning("Please enter both a book title and author name.")
    else:
        query = f"{book_title} {author_name} free download OR read online OR PDF OR EPUB"
        st.info(f"Searching Google for piracy-related links...\n\nQuery: {query}")

        try:
            results = list(search(query, num_results=20))
            suspicious_links = [url for url in results if is_suspicious(url)]

            st.markdown("---")
            st.markdown(f"### Found {len(suspicious_links)} Suspicious Link(s)")

            # Display the suspicious links as buttons
            if suspicious_links:
                for i, link in enumerate(suspicious_links, 1):
                    st.markdown(f"**{i}.** [{link}]({link})")

                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"[🔗 Report This Page](https://www.google.com/webmasters/tools/dmca-notice)", unsafe_allow_html=True)
                    with col2:
                        st.markdown(f"[🔍 Lookup Domain Info (via WHOIS)](https://lookup.icann.org/en)", unsafe_allow_html=True)

                st.markdown("---")
            else:
                st.success("No suspicious links found in the top 20 results. Looking good!")
        except Exception as e:
            st.error(f"An error occurred while searching: {e}")

# Hall of Infamy
st.markdown("---")
st.markdown("## 😈 Hall of Infamy")
st.caption("The worst offenders in the book piracy world. Report them. Mock them. Avoid them.")

infamy_data = pd.DataFrame([
    {"Site": "zlibrary.to", "Status": "Active (mirror)", "Confidence": "High", "Notes": "Seized by FBI, still multiplying."},
    {"Site": "pdfdrive.com", "Status": "Active", "Confidence": "High", "Notes": "Dodgy search engine excuse."},
    {"Site": "ebookhunter.ch", "Status": "Unstable", "Confidence": "Medium", "Notes": "Rebrands often."},
    {"Site": "freebookpdf.com", "Status": "Dead-ish", "Confidence": "Low", "Notes": "Redirects or limps along."}
])

st.dataframe(infamy_data, use_container_width=True)