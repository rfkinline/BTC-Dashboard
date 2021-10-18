# Versions

## Version 2.0.0

### Major Update
- Implemented Threading for major performance increases
- Added settings button and menu
- Set custom refresh time
- Connect to your own Node's Mempool.Space instance
- Removed socket connection to Google's server to test internet connection
- Reworked "No Internet Connection Available!" error detection
- Added version to splashscreen
- Added `CHANGELOG.md`
- Added `Licence`

## Version 1.5.6

### Minor Adjustment
- Changed source of difficulty adjustment to mempool.space api

## Version 1.5.5

### Bug Fix
- `ATH date` detection fix

## Version 1.5.4

### ATH fixes, screen dimensions, error handling
- Improved ATH handling
- Added detected screen dimensions on splash screen.
- Fixed some error display issues.
- Changed error colors to be more distinct.

## Version 1.5.3

### Minor Adjustment
- Simplified screensaver off output

## Version 1.5.2

### Bug Fix
- Fixed block time missing when 2 blocks found quickly

## Version 1.5.1

## Minor Improvements and Bug Fixes
- Added time since last block for better context with recommended fee rates.
- Change timer for green block height from 1 minute to 2 minutes.
- Changed the Price trend indicator to be  larger and more obvious.
- Fixed bug where new block found but timestamp did not update for the new block

## Version 1.5.0

### New Features and Bug Fixes
- Bitcoin Price flashes green or red depending on immediate movement
- Added trend indicator arrow to price: If BTC price goes up or down 2% in 1 hour then an arrow appears next to it in respective direction.
- All indicators show their previous values when an error occurs.
- Indicators turn red when an error occurs respective to the API that has the error. All indicators turn red when internet connection is lost
- ATH change updates with price
- Eliminated variable errors when no internet connection 
- Code cleanup

## Version 1.4.0

### Visual Improvements
- ATH turns bold and green if new ATH on the same day
- ATH Date turns green for the same
- ATH Change turns green when within -5% of ATH and turns red when -50% or below
- Added a splash screen while initializing the main screen.
- Rows now scale for larger screens
- Removed gray background and border on the Bitcoin logo and increased it's size

## Version 1.3.1

### Bug Fixes
- Reverted only once
- Checks and sets some variables that caused errors when internet connection is down
- Division by 0 error solved for mempool fees
- Moved only once code higher

## Version 1.3.0

### Minor Update
- Added mempool.space API for better fee estimates and mempool data.
- Reorganized and renamed data for better flow
- Added lightning nodes #

## Version 1.2.0

### Minor improvements
Changed `BTC` to `Bitcoin`
Added resolution detection

## Version 1.1.0

### Improved error handling
- Improved internect connectivity check
- Display multiple errors on screen

## Version 1.0.0

### Widescreen release
