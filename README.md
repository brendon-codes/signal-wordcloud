# SIGNAL WORDCLOUD GENERATOR

## PYTHON SETUP

```shell
python3 -m venv ./.venv
./.venv/bin/pip3 install -U pip
./.venv/bin/pip3 install setuptools wheel
./.venv/bin/pip3 install .
```

## SQLITE SETUP

Install [DB Browser For SQlite](https://sqlitebrowser.org/).
To install on Fedora:

```shell
sudo dnf install sqlitebrowser
```


## DATA EXTRACTION

Open SQLite DB:

1. Open `DB Browser For SQLite`.
2. `Open Database Readonly`
3. Select Signal SQLite DB path:
    - Linux / Flatpak: `~/.var/app/org.signal.Signal/config/Signal/sql/db.sqlite`
4. Encryption Settings: `SQLCipher 4 defaults`
5. Password:
    1. Find the Signal config key file:
        - Linux / Flatpak: `~/.var/app/org.signal.Signal/config/Signal/config.json`
    2. The raw key is in the `key` property.
    3. The final password is the raw key prefixed with `0x`.
    4. Select `Raw Key`
    5. Enter the final password
    6. Click `Ok`

Extract Messages:

1. See the SQL script in `signal-wordcloud/sql/extract.sql`.
   You will need to edit it to match your Signal group name.
2. Run the SQL script:
    1. Go to the `Execute SQL` tab
    2. Click the `Execute All/Selected SQL` button
3. Click the `Save results view` button
    1. Uncheck `Column names in first line`
    2. Click `Save`
    3. Save file to `signal-wordcloud/data/messages.csv`


## GENERATE WORDCLOUD IMAGE

Generate preview image:

```shell
./.venv/bin/python3 ./bin/messages_to_wordcloud.py < ./data/messages.csv
```

To save the image, you should see an icon for `Save the figure`.
You can save the wordcloud at the location and format that you want.
