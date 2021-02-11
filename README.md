# Group Project for USU CS3450

## Setup Instructions
This project contains the `parking_api` django backend API
Running/setup instructions found in it's subfolder /parking_api/README.md

This project contains the `parking_client` react frontend client
Running/setup instructions found in it's subfolder /parking-client/README.md

## Projects

There are three project boards currently, which are not intended to be used simultaneously. They are of three distinct styles, and eventually two of them will be retired.

## Wiki

There is a GitHub Wiki initialized, but it is currently empty. Perhaps eventually it will be used for documentation and other customer-facing information.

## Requirements

 - Transactions, collecting money, University takes commission
 - Actors: parkers, lot owners, lot attendants, University, supervisor
 - All lots have attendants
 - Prices set by lot owners
 - Prices set by lot owner
 - Phone friendly, no app required
 - Different sizes of parking spots (mobile homes, large sites for tailgating, etc.)
 - QR codes required for authentication on the spot

## Organization

The workspace is organized as follows:

 - Documentation is contained in the ```docs/``` folder
 - Source code is contained in the ```src/``` folder, and each project (client side, server side, test suites etc.) are in their own folders.

## Version Control

All version control numbers are of the following format:

v0.1.2b

The last digit, 2b, signifies that this version contains the second small feature update (2) and the second iteration (b) of the first major version update (1) of the first major version (0) of the app.

## Testing

Test suites, when they're available, will be run from their own directories under ```src/```.
