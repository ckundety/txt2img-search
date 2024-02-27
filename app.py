import logging

import PIL.Image

import streamlit as st

import constants as c
from text2imagesearch import Text2ImageSearch


logger = logging.getLogger(__name__)


t2is = Text2ImageSearch(qdrant_url=c.QDRANT_URL, qdrant_collection=c.QDRANT_COLLECTION)


st.title('Text To Image Search')
st.subheader('Enter a search query to find relevant images')

st.sidebar.subheader('Search parameters')
limit = st.sidebar.number_input('Results limit', min_value=1, max_value=5, value=1)
threshold = st.sidebar.slider('Score threshold', min_value=0.0, max_value=1.0, value=0.5, step=0.1)
query = st.sidebar.text_input("Query", "", max_chars=200)
with st.container():
    submit = st.sidebar.button("Search", use_container_width=True)

if submit:
    if query:
        with st.spinner('Searching...'):
            results = t2is(query, limit=limit, threshold=threshold)

            if len(results) > 0:
                for result in results:
                    img = PIL.Image.open(result.payload['location'])
                    score = result.score * 100
                    if img:
                        caption = result.payload['caption'] + f' (score: {score:2f}%)'
                        st.image(img, caption=caption, use_column_width=True)
            else:
                st.write('No images found for search criteria...')
            st.success('Done!')
    else:
        st.warning("Please enter a search query.")


# query input and search button at the bottom
# st.text_input("Enter your query here", key="query_bottom")
# st.button("Search", key="search_bottom")


# Footer
st.write("Built with Streamlit")

