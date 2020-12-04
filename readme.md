# text_cleaner_cli


## :mag_right: Description

Simple tool for cleaning up textual data in post-processing (removing spaces, punctuation, lowercase numbers etc.)

## :computer: Basic usage

- Install dependencies via `requirements.txt` in a virtual environment

- Case 1 : To process a single character sequence
```bash
python main.py [-s | --sequence] this a Sequence of CHARacters to cLean ^^ [CLEAN OPTIONS=False|True]
```
- Case 2 : To process a unique file
```bash
python main.py [-pt | --path_text_file] /path_to_file.txt [CLEAN OPTIONS=False|True]
```
- Case 2 : To batch file process
```bash
python main.py [ -pb | --path_batch_text] /path_to_directory [CLEAN OPTIONS=False|True]
```
