# cookie-collector
A simple flask api to collect antibot cookies like Incapsula from browser in less than 4 seconds.


## Usage
In the request data, input a url that returns a session cookie, the browser will get that url and return the cookie generated by the site.

## Credits 
Based on https://github.com/kaliiiiiiiiii/Selenium-Driverless web driver that uses your own chrome to spawn browsers.

## Packages Required
- selenium_driverless (``pip install selenium-driverless``)
- waitress (``pip install waitress``)
- flask (``pip install flask``)