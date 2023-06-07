# qa-pdf - Chat with PDF

You can ask PDF that you specified.  The default PDF file is: [scala_text](https://scala-text.github.io/scala_text_pdf/scala_text.pdf).

## Instalattion

```console
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

1. Prepare OpenAI API Key.  You should store it in api_key.txt:

```console
echo <your api key> > api_key.txt
```

2. Create index from the PDF:

```console
python create_index.py
```

3. Chat with your PDF:

``` console
python chat.py
```
