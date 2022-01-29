# x.509 diagrams

x.509 certs chain of trust diagrams generator

## Usage

```shell
pip3 install --user -r requirements.txt
```

```shell
python3 main.py -r -s /path/to/certs
```

## Man

```shell
usage: main.py [-h] --source-directory SRC [--recursive] [--debug] [--output-format {dot,diagram}] [--output-file OUTPUT]

Generage diagrams from x.509 certificates

optional arguments:
  -h, --help            show this help message and exit
  --source-directory SRC, -s SRC
                        The source directory containing x.509 certificates
  --recursive, -r       Recurse in source directory
  --debug               Debug logs
  --output-format {dot,diagram}, -f {dot,diagram}
                        The output format
  --output-file OUTPUT, -o OUTPUT
                        The output file path
```