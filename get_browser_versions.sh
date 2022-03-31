#!/bin/bash

print_chrome_version ()
{
    chrome_loc="/opt/google"
    ${chrome_loc}/$1/google-chrome --version | awk '{print $3}'
}

print_firefox_version ()
{
    firefox_loc="/opt/mozilla"
    ${firefox_loc}/$1/firefox --full-version | awk '{print $3 " " $4}'
}

#
# Architecture
#
arch=$(uname -i)

#
# Stable versions
#
chrome_stable=$(print_chrome_version "chrome")
firefox_stable=$(print_firefox_version "firefox")
firefox_esr=$(print_firefox_version "firefox-esr")
firefox_esr_aws=$(print_firefox_version "firefox-esr-amazonws") # Preinstalled on Amazon Linux 2

#
# Beta versions
#
chrome_beta=$(print_chrome_version "chrome-beta")
firefox_beta=$(print_firefox_version "firefox-beta")

#
# Unstable versions
#
chrome_unstable=$(print_chrome_version "chrome-unstable")
firefox_nightly=$(print_firefox_version "firefox-nightly")

###

echo -e "
BROWSERS STABLE:
    CHROME [${chrome_stable} (${arch})]
    FIREFOX [${firefox_stable} (${arch})]
    FIREFOX [${firefox_esr} (${arch})]
    FIREFOX [${firefox_esr_aws} amazonws (${arch})]
"
