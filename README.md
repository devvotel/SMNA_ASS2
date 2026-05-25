## GUIDE
1) Make sure there is a folder named "data" in the same folder than `fetch_posts.py` and `fetch_threads.py` are in.
2) - IF you have the **uv package manager** installed:
    simply run `uv synv` in the terminal in the project folder - it will automatically create a virtual environment (.venv)
    and install all packages needed to run all files in the project into it.
   - IF you do NOT have uv: create a virtual environment manually (.venv), run `.venv/Scripts/activate` in the terminal, then install
   all packages that are listed in the `pyproject.toml` file.
3) Run `fetch_posts.py` - it will gather ~14000 Bluesky posts using the API and save them into the **data** folder: `data/posts.csv`.
4) Run `fetch_threads.py` - it will gather reply threads from the 20 most replied-to posts and save them in the **data** folder too: `data/edges.csv`.
5) Now you can open `bluesky_analysis.ipynb` and run all the cells in the notebook.
6) Open `network_analysis.ipynb` and do the same.



Progress:
**Initial posts collected across 7 search keywords:**
- `twitter` - 2057 posts
- `elon` - 2009 posts
- `twitter refugee` - 2007 posts
- `bluesky vs twitter` - 2009 posts
- `twitter is dead` - 2016
- `quit twitter` - 2008
- `miss twitter` - 2059

**TOTAL:**: 14165 posts

Potential issue:
- there might be a decent chunk of an *overlap* between posts from searches with different keywords (particularly `twitter` and other keywords containing the word 'twitter')

UPD: actually solid data.
- only 120 duplicates
- 6623 posts are replies to other posts we can look at


UPD2:
- gathered entire reply threads (including nested threads) from top 10 posts with most replies + top 10 posts with most replies fetched by keyword `twitter vs bluesky`
- 2825 posts from the threads were gathered separately into `data/edges.csv`

UPD3: 
- Network analysis section is done
- Sentiment analysis done

UPD4: 
- Topic modelling done