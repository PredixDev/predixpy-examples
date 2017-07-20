
# PredixPy Examples

This repository contains some short functional demonstrations of common
patterns of working with PredixPy for a range of applications.

# Installation

- [ ] Install PredixPy Python SDK for Predix Services.

```
pip install predix
```

# Setup

- [ ] Configure your environment

## Configuration / Admin Mode

When working with `predix.admin.` modules you are in configuration or
administrator mode.  This allows you to create services and store their
important configuration details in the manifest.yml file.

- [ ] Make sure you have done a `cf login` to a Predix API Endpoint

## Service Consumer Mode

PredixPy looks to the environment for specific variables that contain service
details such as URIs, Client IDs, Secrets, etc.  If you use configuration /
admin mode these details can be stored in your `manifest.yml` for easy env
access both locally and in the cloud.

Since most Predix Services rely on UAA, you'll need the following minimum
environment variables:

- **PREDIX_SECURITY_UAA_URI**
- **PREDIX_APP_CLIENT_ID**
- **PREDIX_APP_CLIENT_SECRET**

