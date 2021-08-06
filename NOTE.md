# NOTE

## Issue

`main.py` not work. check below log

```shell
Traceback (most recent call last):
  File "main.py", line 25, in <module>
    database_uri='sqlite:///database.sqlite3',
  File "/Users/dwkim/.local/share/virtualenvs/chatterbot-practice-mxc_9vZJ/lib/python3.7/site-packages/chatterbot/chatterbot.py", line 28, in __init__
    self.storage = utils.initialize_class(storage_adapter, **kwargs)
  File "/Users/dwkim/.local/share/virtualenvs/chatterbot-practice-mxc_9vZJ/lib/python3.7/site-packages/chatterbot/utils.py", line 33, in initialize_class
    return Class(*args, **kwargs)
  File "/Users/dwkim/.local/share/virtualenvs/chatterbot-practice-mxc_9vZJ/lib/python3.7/site-packages/chatterbot/storage/sql_storage.py", line 20, in __init__
    super().__init__(**kwargs)
  File "/Users/dwkim/.local/share/virtualenvs/chatterbot-practice-mxc_9vZJ/lib/python3.7/site-packages/chatterbot/storage/storage_adapter.py", line 21, in __init__
    'tagger_language', languages.ENG
  File "/Users/dwkim/.local/share/virtualenvs/chatterbot-practice-mxc_9vZJ/lib/python3.7/site-packages/chatterbot/tagging.py", line 13, in __init__
    self.nlp = spacy.load(self.language.ISO_639_1.lower())
  File "/Users/dwkim/.local/share/virtualenvs/chatterbot-practice-mxc_9vZJ/lib/python3.7/site-packages/spacy/__init__.py", line 52, in load
    name, vocab=vocab, disable=disable, exclude=exclude, config=config
  File "/Users/dwkim/.local/share/virtualenvs/chatterbot-practice-mxc_9vZJ/lib/python3.7/site-packages/spacy/util.py", line 330, in load_model
    raise IOError(Errors.E941.format(name=name, full=OLD_MODEL_SHORTCUTS[name]))
OSError: [E941] Can't find model 'en'. It looks like you're trying to load a model from a shortcut, which is obsolete as of spaCy v3.0. To load the model, use its full name instead:

nlp = spacy.load("en_core_web_sm")

For more details on the available models, see the models directory: https://spacy.io/models. If you want to create a blank model, use spacy.blank: nlp = spacy.blank("en")
```