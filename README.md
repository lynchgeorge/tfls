# TfL API Experiment

A collaborative play around with the TfL API for a few hours, partly using AI.

The aim was to create a map showing all TfL lines (coloured accordingly) and the live locations of every train.

We started using the Python API wrapper but quickly realised this was out of date and, in particular, only seemed to be giving integer latitude and longitudes for stations which meant most stations were at the same location. So we switched to using the raw API instead by calling the `tfl_get` function in `tfls/custom_api.py`.

We modelled each line, station and train in objects.

We used `notebooks/lines.ipynb` to test and experiment.

Then created several UIs (mainly with AI):

- `tfls/backend`: Heavily vibe-coded UI (badly named) that plots the stations. May or may not hard-code the locations.
- `ai_generated_server.py`: An AI generated flask server that shows all stations and creates the HTML file `templates/index.html`
- `static_ui.py`: A very bad, very simple UI that repeatedly gets all live trains, creates a static HTML file in `/tmp` that plots all their current locations on OpenStreetMap coloured according to their line's colour, and opens that HTML file in the browser.

## Future Aspirations

- Having an actual backend and frontend so the frontend gets updates from the backend which queries the API (or just have a frontend that directly hits the TfL API but at least let it update seamlessly)
- Clearly split into things that only run at startup or every now and then vs often to update:
    - Startup: Getting and drawing the lines and their stations
    - Often: Getting and drawing updated locations for all trains
- Draw the lines themselves in the correct colour by joining up consecutive stations - but this requires knowing which stations are consecutive which may require the `Routes` part of the API which we haven't touched yet.
- Displaying "approaching" a station as different to being at the station already - but this requires knowing which direction the train is going and therefore also using the `Routes` part of the API.
- Animating the trains moving between the stations based on their expected arrival times (in the train objects)
- Allow the user to click on trains/stations/lines in the UI and view info about them

## TfL API Credentials

To query the TfL API, you need credentials to be given access. To set this up:

1. Register for an account and create credentials at `api.tfl.gov.uk` if you haven't already.
2. Copy the file `.env.example` to the file `.env` and replace the strings after the equals signs with your credentials from the website, without quotes.

Then `tfls/custom_api.py` will automatically read your credentials and use them when querying the TfL API.
