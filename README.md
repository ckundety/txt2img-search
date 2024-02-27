# Text2Image Search

This project implements the task given [here](https://gist.github.com/generall/45004be240d9130d52d62ca57d0e6175).

## Features

- Enter a textual search query to retrieve images from an image store that match the query.
- Customize the number of results displayed and set a minimum score threshold.
- View the actual images corresponding to the search results.

## Limitations

- The app uses only the advertisement images provided in the task.
- Search query can be a maximum of 200 characters long.
- Results are subject to the limitations of [**Salesforce BLIP**](https://github.com/salesforce/BLIP) model.
- This is not an image generation app.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/ckundety/txt2img-search.git
    cd txt2img-search
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the Qdrant docker container:

   ```bash
   docker compose up qdrant
   ```

4. Set up the data:

   - Open `01_generate_embedding.ipynb` and run all the cells.
   
5. Start the webapp docker container:

    ```bash
    docker compose up t2iapp
    ```

6. Start using the app:

   - Open http://localhost:8501 in a browser