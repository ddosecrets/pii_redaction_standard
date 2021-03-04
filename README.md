# pii_redaction_standard

An attempt to develop standards for PII redaction.

## Overview

Many different people and organizations, from journalists to scientists to medical professionals, need to share sensitive data that may contain PII (personally identifying information). Usually this data is redacted, but there is little in the way of a standard set of tools for doing so, nor is there a standard set of tests for verifying the reliability of those tools or any new ones that come out. This repository aims to lay some groundwork for this, by providing the following:

1. A definition of PII, broadly construed, that can be used to determine...
2. A set of examples for those different kinds of PII, which are used to test...
3. A library for finding the presence of that PII in text documents.

This repository does ***not*** aim to be complete or comprehensive, covering all the possible kinds of PII, nor all the kinds of documents which may contain PII. Rather, it tries to provide a good first attempt that can be used as a reference point for further expansion.

## Contents

The repository consists of the following items:

- Below, a set of definitions of PII that we are interested in
- Example data, found in `example_data/`
- A baseline library in `library/`, written in Python, which defines functions that will locate PII in text
- Tests in `tests/` that confirm the functionality of the library

## Considerations

PII location is inherently going to be a fuzzy problem. Text can have typos or data transmission errors or all sorts of other issues that can mangle PII in a way that makes it hard to detect programmatically despite being perfectly interpretable to a human reader. Text extracted from document formats other than raw text also have the problem that document formats can do weird things with how they structure text, breaking text up into disjoint parts or inserting other information that mangles PII from the programmatic perspective but not the human perspective.

PII in documents such as images or video, while potentially textual, may be even harder to detect, because OCR is unreliable, and the conversion to text often mangles PII greatly. Additionally, the process of locating the PII spatially in the image or video makes automatic redaction much harder than textual redaction. Audio and other methods of conveying PII add further complications to both detection and redaction.

Ultimately, any PII location technique will need to be approximate, and needs to err on the side of caution. A journalist can always ask to unredact a part of redacted text if they ever suspect that it's not in fact PII but rather an error. The reverse is not possible: we cannot un-release someone's home address or phone number. We therefore should aim to build PII location tools that have no false negatives, but possibly some false positives.
