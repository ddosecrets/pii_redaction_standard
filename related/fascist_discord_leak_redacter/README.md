# Redacter

This program tries to redact Discord messages which contain phone numbers, SSNs,
email addresses, and postal addresses (US/CA mostly). It works by iterating
over the lines of a Discord dump one by one, and so relies on messages always
being on their own line in their entirety. This seems to be the case with
Discord dumps, however.

# How to Use

To run the redacter from the command line, run the following bash command:

```
python3 redacter.py $INPUT $OUTPUT
```

The Bash variables `$INPUT` and `$OUTPUT` should be the file paths to the input
and output files, respectively.

# Dependencies

This is a Python 3 program. The following Python 3 packages are required to run
this program: `pyap`, `re`, `cursor`, `time`, `subprocess`, `sys`, and `os`.
Some of these will likely need to be installed. We recommend using pip3.
