#!/bin/bash

paxctl -cm /opt/google/chrome/chrome
paxctl -cm /opt/google/chrome/nacl_helper
paxctl -cm /opt/google/chrome/chrome-sandbox
paxctl -cm /opt/jre1.7.0_45-x64/bin/java
paxctl -cm /usr/lib*/firefox/firefox
paxctl -cm /usr/lib*/firefox/plugin-container
paxctl -cm /usr/bin/skype
paxctl -cm /usr/lib/ld-2.18.so
paxctl -cm /usr/lib*/opera/opera
paxctl -cm /usr/lib*/opera/pluginwrapper/operapluginwrapper-native
paxctl -cm /usr/lib*/thunderbird/thunderbird
paxctl -cm /usr/lib*/thunderbird/plugin-container
setfattr -n user.pax.flags -v "me" /usr/bin/midori 
cp /usr/bin/python2.7 /usr/bin/python2.7.tmp
paxctl -cm /usr/bin/python2.7.tmp
mv -f /usr/bin/python2.7.tmp /usr/bin/python2.7
