# pii_redaction_standard

An attempt to develop standards for PII redaction.

## Overview

Many different people and organizations, from journalists to scientists to medical professionals, need to share sensitive data that may contain PII (personally identifying information). Usually this data is redacted, but there is little in the way of a standard set of tools for doing so, nor is there a standard set of tests for verifying the reliability of those tools or any new ones that come out. This repository aims to lay some groundwork for this, by providing the following:

1. A definition of PII, broadly construed, that can be used to determine...
2. A set of examples for those different kinds of PII, which are used to test...
3. A library for finding the presence of that PII in text documents.

This repository does **_not_** aim to be complete or comprehensive, covering all the possible kinds of PII, nor all the kinds of documents which may contain PII. Rather, it tries to provide a good first attempt that can be used as a reference point for further expansion.

## Necessity for Openness and Peer Review

We believe that having work like this be done out in the open, and subject to the review of our peers, is important to prevent redaction from being alchemy. We may have useful redaction techniques, but we're not infallible, and the safety of the people who's PII may be leaked by incomplete example data, buggy code, or erroneous assumptions is a top priority. It's also in the interests of other researchers and organizations to have easy to use and modify tools available to them. Lastly, by making reliable tools widely available, the task of journalists, scientists, etc. becomes easier and thus more of it can be done.

## Contents

The repository consists of the following items:

- Below, a set of definitions of PII that we are interested in
- Example data, found in `example_data/`
- A baseline library in `library/`, written in Python, which defines functions that will locate PII in text
- Tests in `tests/` that confirm the functionality of the library
- Code from related projects in `related/`, which can be used as a starting point, or as a reference of what other work has been done

The `example_data` files are formatted such that each line is an example, white space, or a comment. Comment lines begin with `//` and non-comment.

## Considerations

PII location is inherently going to be a fuzzy problem. Text can have typos or data transmission errors or all sorts of other issues that can mangle PII in a way that makes it hard to detect programmatically despite being perfectly interpretable to a human reader. Text extracted from document formats other than raw text also have the problem that document formats can do weird things with how they structure text, breaking text up into disjoint parts or inserting other information that mangles PII from the programmatic perspective but not the human perspective.

PII in documents such as images or video, while potentially textual, may be even harder to detect, because OCR is unreliable, and the conversion to text often mangles PII greatly. Additionally, the process of locating the PII spatially in the image or video makes automatic redaction much harder than textual redaction. Audio and other methods of conveying PII add further complications to both detection and redaction.

Ultimately, any PII location technique will need to be approximate, and needs to err on the side of caution. A journalist can always ask to unredact a part of redacted text if they ever suspect that it's not in fact PII but rather an error. The reverse is not possible: we cannot un-release someone's home address or phone number. We therefore should aim to build PII location tools that have no false negatives, but possibly some false positives.

## Definitions

The kinds of PII that this repository is aimed at modeling currently are:

- US and CA phone numbers
- email addresses
- US social security numbers (SSNs)
- US and CA addresses

We aim to flesh this out to identify:

- International phone numbers
- National identification numbers more broadly
- National and sub-national identity card numbers (eg. state IDs, drivers license numbers)
- Passport numbers
- Bank account numbers
- Credit and debit card numbers
- License plate numbers

Eventually it may also make sense to try to identify further things such as videos and photographs that include faces, houses, cards, etc., as well as speech, as those can also be used to some degree to identify people, especially in the age of crowdsourcing via social media.
