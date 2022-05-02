# fooBar
Test SDE challenge.

# Part 1
`location` - google_trends_scraper

# Part 2
`location` - api

# Part 3
`location` - google_trends_scraper.Dockerfile; api.Dockerfile;

# Part 3 CI/CD
Question: explain how you would set up a CI/CD pipeline that uses Github actions ?

1. within created .github/workflows I've created multiple scenarios with .yaml files,
where those files will serve action-wise instructions for github (for instance release.yaml which may stand for service release process).
   - I suppose the functionalities of deploying `CLOUD PROVIDER` have to be included into 
   services codebase, hence, to deploy one of these services to `CLOUD`, you have to populate steps in .yaml file.

   - One of quick examples: `fabric` is popular "deployment" framework, which logic can sit in project codebase and be invoked on the server side.

For example for release.yaml:
```bash
name: Spiny-release

on:
  release:
    types: [created]

jobs:
    package:
        name: Build package
        runs-on: ubuntu-18.04

        steps:
            - name: Checkout code
              uses: actions/checkout@v2
            - name: Setup Python
              uses: actions/setup-python@v2
              with:
                python-version: '3.7'
            - name: Install deployment dependencies
            ...
```

For example for push_and_pull_request.yaml:
```bash
name: Spiny-push-and-pull-request

on: [push, pull_request]

jobs:
    package:
        name: Build package
        runs-on: ubuntu-18.04

        steps:
            - name: Checkout code
              uses: actions/checkout@v2
            - name: Setup Python
              uses: actions/setup-python@v2
              with:
                python-version: '3.7'
            - name: Install deployment dependencies
            ...
```