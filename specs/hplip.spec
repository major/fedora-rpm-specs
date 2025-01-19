# we don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
}

Summary: HP Linux Imaging and Printing Project
Name: hplip
Version: 3.24.4
Release: 2%{?dist}
# most files (base/*, *, ui*/...) - GPL2+
# prnt/hpijs/ jpeg related files - IJG
# prnt/* - BSD-3-Clause-HP - it is modified a little, asked here https://gitlab.com/fedora/legal/fedora-license-data/-/issues/267
# base/exif.py - BSD-2-Clause - reported as https://gitlab.com/fedora/legal/fedora-license-data/-/issues/268
# base/ldif.py - python-ldap - reported https://gitlab.com/fedora/legal/fedora-license-data/-/issues/269
# io/*, scan/* - MIT
# protocol/discovery/* - LGPL-2.1-or-later
# protocol/* - GPL2only
# scan/sane/sane.h - Public Domain
License: GPL-2.0-or-later AND MIT AND BSD-3-Clause-HP AND IJG AND GPL-2.0-only AND LGPL-2.1-or-later AND BSD-2-Clause AND LicenseRef-Fedora-Public-Domain AND python-ldap

Url: https://developers.hp.com/hp-linux-imaging-and-printing
# Original source tarball
# Source0: http://downloads.sourceforge.net/sourceforge/hplip/hplip-%%{version}.tar.gz
#
# Repacked source tarball without redundant files - always repack
# the original tarball once a new version arrives by:
#
# ./hplip-repack.sh <version>
#

Source0: hplip-%{version}-repack.tar.gz
Source1: hpcups-update-ppds.sh
Source2: copy-deviceids.py
Source3: %{name}.appdata.xml
Source4: hp-laserjet_cp_1025nw.ppd.gz
Source5: hp-laserjet_professional_p_1102w.ppd.gz
Source6: hplip-repack.sh
Source7: hp-plugin.in

Patch1: hplip-pstotiff-is-rubbish.patch
Patch2: hplip-strstr-const.patch
Patch3: hplip-ui-optional.patch
Patch4: hplip-no-asm.patch
Patch5: hplip-deviceIDs-drv.patch
Patch6: hplip-udev-rules.patch
Patch7: hplip-retry-open.patch
Patch8: hplip-snmp-quirks.patch
Patch9: hplip-hpijs-marker-supply.patch
Patch10: hplip-clear-old-state-reasons.patch
Patch11: hplip-hpcups-sigpipe.patch
Patch12: hplip-logdir.patch
Patch13: hplip-bad-low-ink-warning.patch
Patch14: hplip-deviceIDs-ppd.patch
Patch15: hplip-ppd-ImageableArea.patch
Patch16: hplip-scan-tmp.patch
Patch17: hplip-log-stderr.patch
Patch18: hplip-avahi-parsing.patch
Patch19: hplip-dj990c-margin.patch
Patch20: hplip-strncpy.patch
Patch21: hplip-no-write-bytecode.patch
Patch22: hplip-silence-ioerror.patch
Patch23: hplip-sourceoption.patch
Patch24: hplip-noernie.patch
Patch25: hplip-appdata.patch
Patch26: hplip-check-cups.patch
Patch27: hplip-typo.patch
# python3 - recent HP release removed encoding/decoding to utf-8 in fax/pmlfax.py -
# that results in text string going into translate function in base/utils.py, which
# expects binary string because of parameters. Remove this patch if base/utils.py
# code gets fixed.
Patch28: hplip-use-binary-str.patch
# m278-m281 doesn't work correctly again
Patch29: hplip-error-print.patch
Patch30: hplip-hpfax-importerror-print.patch
Patch31: hplip-wifisetup.patch
# pgp.mit.edu keyserver got bad connection, so we need to have pool of keyservers
# to choose (Bz#1641100, launchpad#1799212)
Patch32: hplip-keyserver.patch
# QMessagebox call was copy-pasted from Qt4 version, but Qt5 has different arguments,
# This patch solves most of them
Patch33: 0026-Call-QMessageBox-constructors-of-PyQT5-with-the-corr.patch
# HP upstream introduced new binary blob, which is not open-source, so it violates
# FPG by two ways - shipping binary blob and non open source code - so it needs to be removed.
# Patch is taken from Debian.
Patch34: 0025-Remove-all-ImageProcessor-functionality-which-is-clo.patch
# In hplip-3.18.10 some parts of UI code was commented out, which leaved hp-toolbox
# unusable (crashed on the start). The patch removes usages of variables, which were
# commented out.
# The patch is taken from Debian.
Patch35: 0027-Fixed-incomplete-removal-of-hp-toolbox-features-whic.patch
# hp-setup crashed when user wanted to define a path to PPD file. It was due
# byte + string variables incompatibility and it is fixed by decoding the 
# bytes-like variable
# part of https://bugzilla.redhat.com/show_bug.cgi?id=1666076
# reported upstream https://bugs.launchpad.net/hplip/+bug/1814272
Patch36: hplip-add-ppd-crash.patch
# external scripts, which are downloaded and run by hp-plugin, try to create links
# in non-existing dirs. These scripts ignore errors, so plugin is installed fine
# but then internal hp-plugin can check for plugin state, where links are checked too.
# It results in corrupted plugin state, which breaks printer installation by GUI hp-setup.
# Temporary workaround is to ignore these bad links and real fix should come from HP,
# because their external scripts try to create links in non-existing dirs.
# Bugzilla: https://bugzilla.redhat.com/show_bug.cgi?id=1671513
# Reported upstream: https://bugs.launchpad.net/hplip/+bug/1814574
Patch37: hplip-missing-links.patch
# change in 3.18.9 in scanext.c caused broken scanning for HP LaserJet 3052. Since I cannot figure
# it out what author wanted by the change (it sets option number 9 to true, but different handles
# have different options, so I'm not sure what author wanted to set).
# Remove the change for now, it works for user and me.
Patch38: hplip-hplj-3052.patch
# hpmud parses mdns txt record badly
# upstream tickets: https://bugs.launchpad.net/hplip/+bug/1797501
#                   https://bugs.launchpad.net/hplip/+bug/1817214
#                   https://bugs.launchpad.net/hplip/+bug/1821932
# with no response from upstream
# Patch taken from Debian https://lists.debian.org/debian-printing/2018/11/msg00049.html
Patch39: hplip-hpmud-string-parse.patch
# Part of https://bugzilla.redhat.com/show_bug.cgi?id=1694663
# It was found out that specific device needs plugin for scanning
# Reported upstream as https://bugs.launchpad.net/hplip/+bug/1822762
Patch40: hplip-m278-m281-needs-plugin.patch
# hpcups crashes when a printer needs a plugin and does not have one installed
# it crashes in destructor, because pointer is not initialized
# bugzilla https://bugzilla.redhat.com/show_bug.cgi?id=1695716
# reported upstream 
Patch41: hplip-hpcups-crash.patch
# Fixing the issues found by coverity scan
# reported upstream https://bugs.launchpad.net/hplip/+bug/1808145
Patch42: hplip-covscan.patch
# Segfault during logging to syslog because argument are switched
# bugzilla https://bugzilla.redhat.com/show_bug.cgi?id=1727162
# upstream https://bugs.launchpad.net/hplip/+bug/1837846
Patch43: hplip-logging-segfault.patch
# Traceback in hp-systray when there are no resource
# wanted to report upstream, but launchpad ends with timeout error
# bugzilla https://bugzilla.redhat.com/show_bug.cgi?id=1738321
Patch44: hplip-systray-blockerror.patch
# several printers were removed in 3.19.1, but actually someone still uses them
# reported upstream https://bugs.launchpad.net/hplip/+bug/1843592
# bugzillas 1742949, 1740132, 1739855
Patch45: hplip-missing-drivers.patch
# laserjet 2200 and other devices have different device id than HP expects...
# https://bugzilla.redhat.com/show_bug.cgi?id=1772698
# reported upstream https://bugs.launchpad.net/hplip/+bug/1853002
Patch46: hplip-model-mismatch.patch
# sixext has problems with python3 strings (bz#1573430)
# reported https://bugs.launchpad.net/bugs/1480152
Patch47: hplip-unicodeerror.patch
# error with new gcc, already reported in upstream as
# https://bugs.launchpad.net/hplip/+bug/1836735
Patch48: hplip-fix-Wreturn-type-warning.patch
# upstream check for python clears OS build system
# CFLAGS
# https://bugs.launchpad.net/hplip/+bug/1879445
Patch49: hplip-configure-python.patch
# taken from hplip upstream report - toolbox uses deprecated method
# setMargin(), which generates an exception, resulting in a infinite loop
# of request on cupsd
# https://bugs.launchpad.net/hplip/+bug/1880275
Patch50: hplip-dialog-infinite-loop.patch
# searching algorithm did not expect '-' in model name and thought it is a new PDL
# it resulted in incorrect PPD match, so e.g. hpijs driver was used instead of hpcups
# bug: https://bugzilla.redhat.com/show_bug.cgi?id=1590014
# reported upstream: https://bugs.launchpad.net/hplip/+bug/1881587
Patch51: hplip-find-driver.patch
# hp-clean didn't work for Photosmart C1410 because it was comparing
# string length with buffer size for string object, which is different,
# causing cleaning to fail - the fix is to make the object bytes-like,
# then buffer size is the same as the length.
# Thanks to Stefan Assmann we were able to fix level 1 cleaning
# for the device, but there can be similar issues with other devices
# bug https://bugzilla.redhat.com/show_bug.cgi?id=1833308
# reported upstream https://bugs.launchpad.net/hplip/+bug/1882193
Patch52: hplip-clean-ldl.patch
# 3.20.6 turned off requirement for most devices which needed it
# - it will cause malfunction of printing and scanning for them
# https://bugs.launchpad.net/hplip/+bug/1883898
Patch53: hplip-revert-plugins.patch
# if an user tries to install scanner via hp-setup (printer/fax utility)
# it fails further down - break out earlier with a message
# reported upstream as https://bugs.launchpad.net/hplip/+bug/1916114
Patch54: hplip-hpsetup-noscanjets.patch
# 1963114 - patch for hplip firmware load timeout fix
# reported upstream https://bugs.launchpad.net/hplip/+bug/1922404
Patch55: hplip-hpfirmware-timeout.patch
# 1985251 - Incorrect permission for gpg directory
# reported upstream https://bugs.launchpad.net/hplip/+bug/1938442
Patch56: hplip-gpgdir-perms.patch
# 1987141 - hp-plugin installs malformed udev files
# reported upstream https://bugs.launchpad.net/hplip/+bug/1847477
Patch57: hplip-plugin-udevissues.patch
# 2080235 - Misleading errors about missing shared libraries when scanning
# downstream patch to prevent errors:
# - when loading libhpmud.so - unversioned .so files belong into devel packages,
#   but dlopen() in hplip was set to load the unversioned .so - so to remove rpmlint
#   error (when libhpmud.so is in non-devel package) and prevent runtime dependency on -devel
#   package (if libhpmud.so had been moved to -devel) the dlopen on unversioned .so file was
#   removed
# - /lib64/libm.so is not symlink but ld script, which cannot be used in dlopen()
Patch58: hplip-no-libhpmud-libm-warnings.patch
Patch60: hplip-plugin-script.patch
# C99 compatibility fixes by fweimer - use explicit int
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
Patch61: hplip-pserror-c99.patch
# C99 compatibility patch by fweimer - several undefined functions in hpaio
# backend are declared in orblite.h
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
Patch62: hplip-scan-hpaio-include.patch
# C99 compatibility patch by fweimer - undefined _DBG() and dynamic linking funcs in orblite.c
# - _DBG() looks like typo and new header is added for funcs
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
Patch63: hplip-scan-orblite-c99.patch
# C99 compatibility patch by fweimer:
# PyString_AsStringAndSize is removed in Python3, remove its compilation for now
# in case there is a request for compiling it again, there is a possible solution
# for the function py3 alternative https://opendev.org/openstack/pyeclib/commit/19c8313986
# - disabling removes hp-unload and /usr/share/hplip/pcard as well
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
Patch64: hplip-pcardext-disable.patch
# undefined strcasestr() in sclpml.c - build with _GNU_SOURCE
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
Patch65: hplip-sclpml-strcasestr.patch
# 2192131 - parseQueues() doesn't get device uri from 'lpstat -v', because parsing pattern changed
# https://bugs.launchpad.net/hplip/+bug/2027972
Patch67: hplip-fix-parsing-lpstat.patch
# switch to curl by downstream patch from wget to workaround openstack dropping IPv6
# which causes great delays...
# Remove this once internal openstack handles IPv6 better - test by pinging IPv6 in OpenStack,
# it should not hang.
Patch68: hplip-plugin-curl.patch
# fix SyntaxWarning from python3.12
# https://bugs.launchpad.net/hplip/+bug/2029480
Patch69: hplip-use-raw-strings.patch
# FTBFS GCC 14
# https://bugs.launchpad.net/hplip/+bug/2048780
Patch70: hplip-hpaio-gcc14.patch
# format is no longer method in locale module
# https://bugs.launchpad.net/hplip/+bug/2045507
Patch71: hplip-locale-format.patch

%if 0%{?fedora} || 0%{?rhel} <= 8
# mention hplip-gui if you want to have GUI
Patch1000: hplip-fedora-gui.patch
%endif


# uses automatic creation of configure
BuildRequires: autoconf
# uses automatic creation of Makefile
BuildRequires: automake
# Make sure we get postscriptdriver tags - need cups and python3-cups.
BuildRequires: cups
# uses functions from CUPS in filters, backends and libraries defining them
BuildRequires: cups-devel
%if 0%{?rhel} <= 8 || 0%{?fedora}
# needed for desktop file validation in spec file
BuildRequires: desktop-file-utils
%endif
# gcc and gcc-c++ are no longer in buildroot by default
# gcc is needed for compilation of HPAIO scanning backend, HP implementation of
# IPP and MDNS protocols, hpps driver, hp backend, hpip (image processing
# library), multipoint transport driver hpmud
BuildRequires: gcc
# gcc-c++ is needed for hpijs, hpcups drivers
BuildRequires: gcc-c++
# support for JPEG file formats in hp-scan
BuildRequires: libjpeg-devel
# uses libtool for autorconf
BuildRequires: libtool
# implements support for USB devices
BuildRequires: libusb1-devel
# uses make
BuildRequires: make
# SLP device discovery is based on SNMP
BuildRequires: net-snmp-devel
# wasn't able to find out why, but SO libraries in hplip-libs require them...
BuildRequires: openssl-devel
# supports mDNS device discovery via Avahi
BuildRequires: pkgconfig(avahi-client)
BuildRequires: pkgconfig(avahi-core)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: python3-cups
# implements C Python extensions like hpmudext, cupsext, scanext
BuildRequires: python3-devel
# distutils are removed in Python3.12, use setuptools
BuildRequires: python3-setuptools
# SANE backend hpaio uses function from SANE API
BuildRequires: sane-backends-devel
# macros: %%{_tmpfilesdir}, %%{_udevrulesdir}
BuildRequires: systemd

# uses avahi-browse for discovering IPP-over-USB printers
Recommends: avahi-tools
# 1733449 - Scanner on an HP AIO printer is not detected unless libsane-hpaio is installed
Recommends: libsane-hpaio%{?_isa} = %{version}-%{release}
# downloaded plugin requires python3-gobject to work even via CLI...
# but make it weak dependency, so users which don't need the plugin and have servers
# can remove the python3-gobject which is used by desktop apps
Recommends: python3-gobject

Requires: cups
# switch to curl by downstream patch from wget to workaround openstack dropping IPv6
# which causes great delays...
Requires: curl
# for bash script acting as hp-plugin (Source7)
Requires: gawk
# set require directly to /usr/bin/gpg, because gnupg2 and gnupg ships it,
# but gnupg will be deprecated in the future
Requires: %{_bindir}/gpg
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: python3-dbus
%if 0%{?rhel} <= 8 || 0%{?fedora}
Requires: python3-pillow
%endif
# /usr/lib/udev/rules.d
Requires: systemd
# 1788643 - Fedora minimal does not ship tar by default
Requires: tar
# require usbutils, hp-diagnose_queues needs lsusb
Requires: usbutils

# require coreutils, because timeout binary is needed in post scriptlet,
# because hpcups-update-ppds script can freeze in certain situation and
# stop the update
Requires(post): coreutils

%description
The Hewlett-Packard Linux Imaging and Printing Project provides
drivers for HP printers and multi-function peripherals.

%package common
Summary: Files needed by the HPLIP printer and scanner drivers

%description common
Files needed by the HPLIP printer and scanner drivers.

%package libs
Summary: HPLIP libraries
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Requires: python3

%description libs
Libraries needed by HPLIP.

%if 0%{?rhel} <= 8 || 0%{?fedora}
%package gui
Summary: HPLIP graphical tools
BuildRequires: libappstream-glib

# for avahi-browse - looks for devices on local network
Recommends: avahi-tools
Recommends: libsane-hpaio%{?_isa} = %{version}-%{release}
# for hp-check
Recommends: pkgconf

Requires: %{name}%{?_isa} = %{version}-%{release}
# hpssd.py
Requires: python3-gobject
Requires: python3-reportlab
Requires: python3-qt5

%description gui
HPLIP graphical tools.
%endif

%package -n libsane-hpaio
Summary: SANE driver for scanners in HP's multi-function devices

Requires: sane-backends
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description -n libsane-hpaio
SANE driver for scanners in HP's multi-function devices (from HPOJ).

%prep
%setup -q

# The pstotiff filter is rubbish so replace it (launchpad #528394).
%patch -P 1 -p1 -b .pstotiff-is-rubbish

# Fix compilation.
%patch -P 2 -p1 -b .strstr-const

# Make utils.checkPyQtImport() look for the gui sub-package (bug #243273).
%patch -P 3 -p1 -b .ui-optional

# Make sure to avoid handwritten asm.
%patch -P 4 -p1 -b .no-asm

# Corrected several IEEE 1284 Device IDs using foomatic data.
# Color LaserJet 2500 series (bug #659040)
# LaserJet 4100 Series/2100 Series (bug #659039)
%patch -P 5 -p1 -b .deviceIDs-drv
chmod +x %{SOURCE2}
mv prnt/drv/hpijs.drv.in{,.deviceIDs-drv-hpijs}
%{SOURCE2} prnt/drv/hpcups.drv.in \
           prnt/drv/hpijs.drv.in.deviceIDs-drv-hpijs \
           > prnt/drv/hpijs.drv.in

# Move udev rules from /etc/ to /usr/lib/ (bug #748208).
%patch -P 6 -p1 -b .udev-rules

# Retry when connecting to device fails (bug #532112).
%patch -P 7 -p1 -b .retry-open

# Mark SNMP quirks in PPD for HP OfficeJet Pro 8500 (bug #581825).
%patch -P 8 -p1 -b .snmp-quirks

# Fixed bogus low ink warnings from hpijs driver (bug #643643).
%patch -P 9 -p1 -b .hpijs-marker-supply

# Clear old printer-state-reasons we used to manage (bug #510926).
%patch -P 10 -p1 -b .clear-old-state-reasons

# Avoid busy loop in hpcups when backend has exited (bug #525944).
%patch -P 11 -p1 -b .hpcups-sigpipe

# CUPS filters should use TMPDIR when available (bug #865603).
%patch -P 12 -p1 -b .logdir

# Fixed Device ID parsing code in hpijs's dj9xxvip.c (bug #510926).
%patch -P 13 -p1 -b .bad-low-ink-warning

# Add Device ID for
# HP LaserJet Color M451dn (bug #1159380)
for ppd_file in $(grep '^diff' %{PATCH14} | cut -d " " -f 4);
do
  gunzip ${ppd_file#*/}.gz
done
%patch -P 14 -p1 -b .deviceIDs-ppd
for ppd_file in $(grep '^diff' %{PATCH14} | cut -d " " -f 4);
do
  gzip -n ${ppd_file#*/}
done

# Fix ImageableArea for Laserjet 8150/9000 (bug #596298).
for ppd_file in $(grep '^diff' %{PATCH15} | cut -d " " -f 4);
do
  gunzip ${ppd_file#*/}.gz
done
%patch -P 15 -p1 -b .ImageableArea
for ppd_file in $(grep '^diff' %{PATCH15} | cut -d " " -f 4);
do
  gzip -n ${ppd_file#*/}
done

# Scan to /var/tmp instead of /tmp (bug #1076954).
%patch -P 16 -p1 -b .scan-tmp

# Treat logging before importing of logger module (bug #984699).
%patch -P 17 -p1 -b .log-stderr

# Fix parsing of avahi-daemon output (bug #1096939).
%patch -P 18 -p1 -b .parsing

# Fixed left/right margins for HP DeskJet 990C (LP #1405212).
%patch -P 19 -p1 -b .dj990c-margin

# Fixed uses of strncpy throughout.
%patch -P 20 -p1 -b .strncpy

# Don't try to write bytecode cache for hpfax backend (bug #1192761)
# or hp-config_usb_printer (bug #1266903)
# or hpps filter (bug #1241548).
%patch -P 21 -p1 -b .no-write-bytecode

# Ignore IOError when logging output (bug #712537).
%patch -P 22 -p1 -b .silence-ioerror

# [abrt] hplip: hp-scan:663:<module>:NameError: name 'source_option' is not defined (bug #1341304)
%patch -P 23 -p1 -b .sourceoption

# hplip license problem (bug #1364711)
%patch -P 24 -p1 -b .no-ernie

# hplip appdata
%patch -P 25 -p1 -b .appdata

# hp-check shows 'CUPS incompatible or not running' even if CUPS is running (bug #1456467)
%patch -P 26 -p1 -b .check-cups

# hp-firmware:NameError: name 'INTERACTIVE_MODE4' is not defined (bug #1533869)
%patch -P 27 -p1 -b .typo

%patch -P 28 -p1 -b .use-binary-str

# TypeError: 'Error' object does not support indexing (bug #1564770)
# upstream bug: https://bugs.launchpad.net/ubuntu/+source/hplip/+bug/1718129
# in python2 it was possible to acces Exception message by index [0].
# in python3 this is no longer possible and it causes TypeError.
%patch -P 29 -p1 -b .error-print-fix

# TypeError: not all arguments converted during string formatting (bug #1566938)
# upstream bug: https://bugs.launchpad.net/ubuntu/+source/hplip/+bug/616450
# bug caused by more arguments than argument specifiers in formatted string
%patch -P 30 -p1 -b .hpfax-import-error-print

# 'WifiSetupDialog' object has no attribute 'wifiobj' (bug #1626877)
# upstream bug: https://bugs.launchpad.net/hplip/+bug/1752060
# bug caused by typo in wifisetupdialog wifiObj property call
%patch -P 31 -p1 -b .wifisetup-bad-call-fix

# have pool of keyservers to choose
%patch -P 32 -p1 -b .keyserver

# TypeError: argument 5 has unexpected type 'StandardButtons' (bug #1594602)
# upstream bug: https://bugs.launchpad.net/ubuntu/+source/hplip/+bug/1745383
# bug caused by typo in QMessageBox constructor call
# this patch fixes more of those typos - some fixed by tkorbar, some taken from ubuntu fix
%patch -P 33 -p1 -b .qmsgbox-typos-fix

# removal of non open source code, taken from ubuntu
%patch -P 34 -p1 -b .libimageprocessor-removal

%{_bindir}/rm prnt/hpcups/libImageProcessor-x86*

%patch -P 35 -p1 -b .toolbox-crash
# part of https://bugzilla.redhat.com/show_bug.cgi?id=1666076
%patch -P 36 -p1 -b .add-ppd-crash
# 1671513 - after 'successful' plugin installation it is not installed
%patch -P 37 -p1 -b .missing-links
# 1684434 - Scanning broken for HP LaserJet 3052
%patch -P 38 -p1 -b .hp-laserjet-3052-broken-scanning
# 1694663 - Cannot scan with M281fdw LaserJet - failed: Error during device I/O (part 1)
%patch -P 39 -p1 -b .hpmud-string-parse
# 1694663 - Cannot scan with M281fdw LaserJet - failed: Error during device I/O (part 2)
%patch -P 40 -p1 -b .m278-m281-needs-plugin
# 1695716 - hpcups crashes in Compressor destructor
%patch -P 41 -p1 -b .hpcups-crash
# fixing issues found by coverity scan
%patch -P 42 -p1 -b .covscan
# segfault during logging (1727162)
%patch -P 43 -p1 -b .logging-segfault
# 1738321 - [abrt] hp-systray:BlockingIOError: [Errno 11] Resource temporarily unavailable
%patch -P 44 -p1 -b .systray-blockerror
# 1742949, 1740132, 1739855 - missing drivers
%patch -P 45 -p1 -b .missing-drivers
# 1772698 - Can't setup printer (HP LJ 2200): no attributes found in model.dat
%patch -P 46 -p1 -b .model-mismatch
# 1573430 - sixext.py:to_string_utf8:UnicodeDecodeError: 'utf-8' codec can't decode bytes
%patch -P 47 -p1 -b .unicodeerror
%patch -P 48 -p1 -b .Wreturn-fix
%patch -P 49 -p1 -b .configure-python
%patch -P 50 -p1 -b .dialog-infinite-loop
# 1590014 - hplip PPD search doesn't expect '-' in device name
%patch -P 51 -p1 -b .find-driver
# 1833308 - hp-clean cannot clean HP PSC1410 - Device I/O error
%patch -P 52 -p1 -b .clean-ldl
%patch -P 53 -p1 -b .revert-plugins
# if an user tries to install scanner via hp-setup (printer/fax utility)
# it fails further down - break out earlier with a message
%patch -P 54 -p1 -b .hpsetup-noscanjets
# 1963114 - patch for hplip firmware load timeout fix
%patch -P 55 -p1 -b .hpfirmware-timeout
# 1985251 - Incorrect permission for gpg directory
%patch -P 56 -p1 -b .gpgdir-perms
# 1987141 - hp-plugin installs malformed udev files
%patch -P 57 -p1 -b .hpplugin-udevperms
# 2080235 - Misleading errors about missing shared libraries when scanning
%patch -P 58 -p1 -b .no-libm-libhpmud-warn
%patch -P 60 -p1 -b .plugin-patch
# C99 compatibility fixes by fweimer - use explicit int
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
%patch -P 61 -p1 -b .pserror-int
# C99 compatibility patch by fweimer - several undefined functions in hpaio
# backend are declared in orblite.h
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
%patch -P 62 -p1 -b .hpaio-orblite-defs
# C99 compatibility patch by fweimer - undefined _DBG() and dynamic linking funcs in orblite.c
# - _DBG() looks like typo and new header is added for funcs
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
%patch -P 63 -p1 -b .orblite-undefs
# C99 compatibility patch by fweimer - python2 PyString_AsStringAndSize in python3 code
# gives undefined reference - removed for now with dependent hp-unload
%patch -P 64 -p1 -b .pcardext-disable
# C99 compatibility patch by fweimer - undefined strcasestr() in sclpml.c - build with _GNU_SOURCE
%patch -P 65 -p1 -b .sclpml-strcasestr
# 2192131 - parseQueues() doesn't get device uri from 'lpstat -v', because parsing pattern changed
# https://bugs.launchpad.net/hplip/+bug/2027972
%patch -P 67 -p1 -b .lpstat-parse
# switch to curl by downstream patch from wget to workaround openstack dropping IPv6
# which causes great delays...
%patch -P 68 -p1 -b .curl-switch
# fix warnings
# upstream https://bugs.launchpad.net/hplip/+bug/2029480
%patch -P 69 -p1 -b .raw-strings
# FTBFS GCC 14
# https://bugs.launchpad.net/hplip/+bug/2048780
%patch -P 70 -p1 -b .hpaio-gcc14
# format is no longer method in locale module
# https://bugs.launchpad.net/hplip/+bug/2045507
%patch -P 71 -p1 -b .locale-format

# Fedora specific patches now, don't put a generic patches under it
%if 0%{?fedora} || 0%{?rhel} <= 8
# mention hplip-gui should be installed if you want GUI
%patch -P 1000 -p1 -b .fedora-gui
%endif


sed -i.duplex-constraints \
    -e 's,\(UIConstraints.* \*Duplex\),//\1,' \
    prnt/drv/hpcups.drv.in

# Change shebang /usr/bin/env python -> /usr/bin/python3 (bug #618351).
find -name '*.py' -print0 | xargs -0 \
    sed -i.env-python -e 's,^#!/usr/bin/env python,#!%{__python3},'
sed -i.env-python -e 's,^#!/usr/bin/env python,#!%{__python3},' \
    prnt/filters/hpps \
    fax/filters/pstotiff

cp -p %{SOURCE4} %{SOURCE5} ppd/hpcups

# 2129849 - move hp-plugin script into srcdir
cp -p %{SOURCE7} .


%build
# Work-around Makefile.am imperfections.
sed -i 's|^AM_INIT_AUTOMAKE|AM_INIT_AUTOMAKE([foreign])|g' configure.in
# Upstream uses old libtool, which causes problems (due to libhpmud requiring
# libhpdiscovery) when we try to remove rpath from it.
# Regenerating all autotools files works-around these rpath issues.
autoreconf --verbose --force --install

%configure \
        --enable-fax-build \
        --enable-foomatic-drv-install \
        --enable-gui-build \
        --enable-hpcups-install \
        --enable-hpijs-install \
        --enable-pp-build \
        --enable-qt5 \
        --enable-scan-build \
        --disable-foomatic-rip-hplip-install \
        --disable-imageProcessor-build \
        --disable-policykit \
        --disable-qt4 \
        --with-mimedir=%{_datadir}/cups/mime PYTHON=%{__python3}

%make_build


%install
mkdir -p %{buildroot}%{_bindir}
%make_install PYTHON=%{__python3}

# Create /run/hplip & /var/lib/hp
mkdir -p %{buildroot}/run/hplip
mkdir -p %{buildroot}%{_sharedstatedir}/hp

# install /usr/lib/tmpfiles.d/hplip.conf (bug #1015831)
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/hplip.conf <<EOF
# See tmpfiles.d(5) for details

d /run/hplip 0775 root lp -
EOF


# Remove unpackaged files
rm -rf  %{buildroot}%{_sysconfdir}/sane.d \
        %{buildroot}%{_docdir} \
        %{buildroot}%{_datadir}/hal/fdi \
        %{buildroot}%{_datadir}/hplip/pkservice.py \
        %{buildroot}%{_bindir}/hp-pkservice

rm -rf  %{buildroot}%{_datadir}/hplip/locatedriver* \
        %{buildroot}%{_datadir}/hplip/dat2drv*

rm -f   %{buildroot}%{_bindir}/hp-logcapture \
        %{buildroot}%{_bindir}/hp-doctor \
        %{buildroot}%{_bindir}/hp-pqdiag \
        %{buildroot}%{_datadir}/hplip/logcapture.py \
        %{buildroot}%{_datadir}/hplip/doctor.py \
        %{buildroot}%{_datadir}/hplip/pqdiag.py

rm -f   %{buildroot}%{_bindir}/foomatic-rip \
        %{buildroot}%{_libdir}/cups/filter/foomatic-rip \
        %{buildroot}%{_libdir}/*.la \
        %{buildroot}%{python3_sitearch}/*.la \
        %{buildroot}%{_libdir}/libhpip.so \
        %{buildroot}%{_libdir}/libhpmud.so \
        %{buildroot}%{_libdir}/libhpipp.so \
        %{buildroot}%{_libdir}/libhpdiscovery.so \
        %{buildroot}%{_libdir}/sane/*.la \
        %{buildroot}%{_datadir}/cups/model/foomatic-ppds \
        %{buildroot}%{_datadir}/applications/hplip.desktop \
        %{buildroot}%{_datadir}/ppd/HP/*.ppd

rm -f %{buildroot}%{_datadir}/hplip/hpaio.desc

rm -rf %{buildroot}%{_datadir}/hplip/install.* \
       %{buildroot}%{_datadir}/hplip/uninstall.* \
       %{buildroot}%{_bindir}/hp-uninstall \
       %{buildroot}%{_datadir}/hplip/upgrade.* \
       %{buildroot}%{_bindir}/hp-upgrade \
       %{buildroot}%{_datadir}/hplip/hplip-install

rm -f %{buildroot}%{_datadir}/hplip/hpijs.drv.in.template

rm -f %{buildroot}%{_datadir}/cups/mime/pstotiff.types \
      %{buildroot}%{_datadir}/hplip/fax/pstotiff*

rm -f %{buildroot}%{_datadir}/hplip/hplip-install

rm -f %{buildroot}%{_unitdir}/hplip-printer@.service

rm -f %{buildroot}%{_datadir}/ipp-usb/quirks/HPLIP.conf

rm -rf %{buildroot}%{_bindir}/hp-unload \
       %{buildroot}%{_datadir}/%{name}/pcard

# The systray applet doesn't work properly (displays icon as a
# window), so don't ship the launcher yet.
rm -f %{buildroot}%{_sysconfdir}/xdg/autostart/hplip-systray.desktop

%if 0%{?rhel} > 8
rm -rf %{buildroot}%{_bindir}/hp-check \
       %{buildroot}%{_bindir}/hp-devicesettings \
       %{buildroot}%{_bindir}/hp-diagnose_plugin \
       %{buildroot}%{_bindir}/hp-faxsetup \
       %{buildroot}%{_bindir}/hp-linefeedcal \
       %{buildroot}%{_bindir}/hp-makecopies \
       %{buildroot}%{_bindir}/hp-print \
       %{buildroot}%{_bindir}/hp-printsettings \
       %{buildroot}%{_bindir}/hp-systray \
       %{buildroot}%{_bindir}/hp-scan \
       %{buildroot}%{_bindir}/hp-toolbox \
       %{buildroot}%{_bindir}/hp-uiscan \
       %{buildroot}%{_bindir}/hp-wificonfig \
       %{buildroot}%{_datadir}/applications/*.desktop \
       %{buildroot}%{_datadir}/metainfo/hplip.appdata.xml \
       %{buildroot}%{_datadir}/icons/hicolor/*/apps/* \
       %{buildroot}%{_datadir}/hplip/base/imageprocessing.py* \
       %{buildroot}%{_datadir}/hplip/check.py* \
       %{buildroot}%{_datadir}/hplip/devicesettings.py* \
       %{buildroot}%{_datadir}/hplip/diagnose_plugin.py* \
       %{buildroot}%{_datadir}/hplip/faxsetup.py* \
       %{buildroot}%{_datadir}/hplip/linefeedcal.py* \
       %{buildroot}%{_datadir}/hplip/makecopies.py* \
       %{buildroot}%{_datadir}/hplip/print.py* \
       %{buildroot}%{_datadir}/hplip/printsettings.py* \
       %{buildroot}%{_datadir}/hplip/systray.py* \
       %{buildroot}%{_datadir}/hplip/scan.py* \
       %{buildroot}%{_datadir}/hplip/toolbox.py* \
       %{buildroot}%{_datadir}/hplip/uiscan.py* \
       %{buildroot}%{_datadir}/hplip/wificonfig.py* \
       %{buildroot}%{_datadir}/hplip/data/images \
       %{buildroot}%{_datadir}/hplip/scan \
       %{buildroot}%{_datadir}/hplip/ui5 \
       %{buildroot}%{_docdir}/hplip/hpscan.html \
       doc/hpscan.html
%endif

install -p -m755 hp-plugin %{buildroot}%{_bindir}/hp-plugin-download

%if 0%{?rhel} <= 8 || 0%{?fedora}
mkdir -p %{buildroot}%{_datadir}/metainfo
cp %{SOURCE3} %{buildroot}%{_datadir}/metainfo/

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,64x64}/apps
install -p -m644 %{buildroot}%{_datadir}/hplip/data/images/16x16/hp_logo.png \
   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/hp_logo.png
install -p -m644 %{buildroot}%{_datadir}/hplip/data/images/32x32/hp_logo.png \
   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/hp_logo.png
install -p -m644 %{buildroot}%{_datadir}/hplip/data/images/64x64/hp_logo.png \
   %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/hp_logo.png

mkdir -p %{buildroot}%{_datadir}/applications
sed -i -e '/^Categories=/d' hplip.desktop
# Encoding key is deprecated
sed -i -e '/^Encoding=/d' hplip.desktop
desktop-file-validate hplip.desktop

desktop-file-install                               \
        --dir %{buildroot}/%{_datadir}/applications              \
        --add-category System \
        --add-category Settings \
        --add-category HardwareSettings                        \
        hplip.desktop

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

# install hp-uiscan desktop file
sed -i 's/\/usr\/share\/icons\/Humanity\/devices\/48\/printer\.svg/hp_logo/' hp-uiscan.desktop

desktop-file-validate hp-uiscan.desktop

desktop-file-install \
          --dir %{buildroot}/%{_datadir}/applications \
          --add-category Graphics \
          --add-category Scanning \
          --add-category Application \
          hp-uiscan.desktop
%endif

# Regenerate hpcups PPDs on upgrade if necessary (bug #579355).
install -p -m755 %{SOURCE1} %{buildroot}%{_bindir}/hpcups-update-ppds

%{__mkdir_p} %{buildroot}%{_sysconfdir}/sane.d/dll.d
echo hpaio > %{buildroot}%{_sysconfdir}/sane.d/dll.d/hpaio

# Images in docdir should not be executable (bug #440552).
find doc/images -type f -exec chmod 644 {} \;

# Create an empty plugins directory to make sure it gets the right
# SELinux file context (bug #564551).
%{__mkdir_p} %{buildroot}%{_datadir}/hplip/prnt/plugins

%post
# timeout is to prevent possible freeze during update
%{_bindir}/timeout 10m -k 15m %{_bindir}/hpcups-update-ppds &>/dev/null ||:

%ldconfig_scriptlets libs


%files
%doc COPYING doc/*
# ex-hpijs
%{_bindir}/hpijs
# ex-hpijs
%{_bindir}/hpcups-update-ppds
%{_bindir}/hp-align
%{_bindir}/hp-clean
%{_bindir}/hp-colorcal
%{_bindir}/hp-config_usb_printer
%{_bindir}/hp-diagnose_queues
%{_bindir}/hp-fab
%{_bindir}/hp-firmware
%{_bindir}/hp-info
%{_bindir}/hp-levels
%{_bindir}/hp-makeuri
%{_bindir}/hp-plugin
%{_bindir}/hp-plugin-download
%{_bindir}/hp-probe
%{_bindir}/hp-query
%if 0%{?rhel} <= 8 || 0%{?fedora}
%{_bindir}/hp-scan
%endif
%{_bindir}/hp-sendfax
%{_bindir}/hp-setup
%{_bindir}/hp-testpage
%{_bindir}/hp-timedate
%{_cups_serverbin}/backend/hp
%{_cups_serverbin}/backend/hpfax
# ex-hpijs
%{_cups_serverbin}/filter/hpcdmfax
%{_cups_serverbin}/filter/hpcups
%{_cups_serverbin}/filter/hpcupsfax
%{_cups_serverbin}/filter/hpps
%{_cups_serverbin}/filter/pstotiff
# ex-hpijs
%{_datadir}/cups/drv/*
%{_datadir}/cups/mime/pstotiff.convs
# Files
%{_datadir}/hplip/align.py*
%{_datadir}/hplip/check-plugin.py*
%{_datadir}/hplip/clean.py*
%{_datadir}/hplip/colorcal.py*
%{_datadir}/hplip/config_usb_printer.py*
%{_datadir}/hplip/diagnose_queues.py*
%{_datadir}/hplip/fab.py*
%{_datadir}/hplip/fax
%{_datadir}/hplip/firmware.py*
%{_datadir}/hplip/hpdio.py*
%{_datadir}/hplip/hplip_clean.sh
%{_datadir}/hplip/hpssd*
%{_datadir}/hplip/info.py*
%{_datadir}/hplip/__init__.py*
%{_datadir}/hplip/levels.py*
%{_datadir}/hplip/makeuri.py*
%{_datadir}/hplip/plugin.py*
%{_datadir}/hplip/probe.py*
%{_datadir}/hplip/query.py*
%if 0%{?rhel} <= 8 || 0%{?fedora}
%{_datadir}/hplip/scan.py*
%endif
%{_datadir}/hplip/sendfax.py*
%{_datadir}/hplip/setup.py*
%{_datadir}/hplip/testpage.py*
%{_datadir}/hplip/timedate.py*
%{_datadir}/hplip/unload.py*
# Directories
%{_datadir}/hplip/base
%{_datadir}/hplip/copier
%{_datadir}/hplip/data/ldl
%{_datadir}/hplip/data/localization
%{_datadir}/hplip/data/pcl
%{_datadir}/hplip/data/ps
%{_datadir}/hplip/installer
%{_datadir}/hplip/prnt
%if 0%{?rhel} <= 8 || 0%{?fedora}
%{_datadir}/hplip/scan
%endif
%{_datadir}/ppd
%{_sharedstatedir}/hp
%dir %attr(0775,root,lp) /run/hplip
%{_tmpfilesdir}/hplip.conf
%{_udevrulesdir}/56-hpmud.rules

%files common
%license COPYING
%dir %{_sysconfdir}/hp
%config(noreplace) %{_sysconfdir}/hp/hplip.conf
%dir %{_datadir}/hplip
%dir %{_datadir}/hplip/data
%{_datadir}/hplip/data/models

%files libs
%{_libdir}/libhpip.so.0
%{_libdir}/libhpip.so.0.0.1
%{_libdir}/libhpipp.so.0
%{_libdir}/libhpipp.so.0.0.1
%{_libdir}/libhpdiscovery.so.0
%{_libdir}/libhpdiscovery.so.0.0.1
%{_libdir}/libhpmud.so.0
%{_libdir}/libhpmud.so.0.0.6
# Python extension
%{python3_sitearch}/*

%if 0%{?rhel} <= 8 || 0%{?fedora}
%files gui
%{_bindir}/hp-check
%{_bindir}/hp-devicesettings
%{_bindir}/hp-diagnose_plugin
%{_bindir}/hp-faxsetup
%{_bindir}/hp-linefeedcal
%{_bindir}/hp-makecopies
%{_bindir}/hp-print
%{_bindir}/hp-printsettings
%{_bindir}/hp-systray
%{_bindir}/hp-toolbox
%{_bindir}/hp-uiscan
%{_bindir}/hp-wificonfig
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/hplip.appdata.xml
# Files
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/hplip/check.py*
%{_datadir}/hplip/devicesettings.py*
%{_datadir}/hplip/diagnose_plugin.py*
%{_datadir}/hplip/faxsetup.py*
%{_datadir}/hplip/linefeedcal.py*
%{_datadir}/hplip/makecopies.py*
%{_datadir}/hplip/print.py*
%{_datadir}/hplip/printsettings.py*
%{_datadir}/hplip/systray.py*
%{_datadir}/hplip/toolbox.py*
%{_datadir}/hplip/uiscan.py*
%{_datadir}/hplip/wificonfig.py*
# Directories
%{_datadir}/hplip/data/images
%{_datadir}/hplip/ui5
%endif

%files -n libsane-hpaio
%{_libdir}/sane/libsane-*.so
%{_libdir}/sane/libsane-*.so.1
%{_libdir}/sane/libsane-*.so.1.0.0
%config(noreplace) %{_sysconfdir}/sane.d/dll.d/hpaio

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jul 23 2024 Zdenek Dohnal <zdohnal@redhat.com> - 3.24.4-1
- 2292623 - hplip-3.24.4 is available

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.23.12-7
- Rebuilt for Python 3.13

* Thu Mar 21 2024 Zdenek Dohnal <zdohnal@redhat.com> - 3.23.12-6
- hp-plugin-download - curl removed --create-dir parameter

* Mon Mar 18 2024 Zdenek Dohnal <zdohnal@redhat.com> - 3.23.12-5
- 2270031 - hp-firmware: module 'locale' not longer provides method 'format', causing traceback

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Zdenek Dohnal <zdohnal@redhat.com> - 3.23.12-2
- add fallback url to hp-plugin-download

* Mon Jan 08 2024 Zdenek Dohnal <zdohnal@redhat.com> - 3.23.12-1
- 2252302 - hplip-3.23.12 is available

* Tue Oct 03 2023 Zdenek Dohnal <zdohnal@redhat.com> - 3.23.8-1
- 2239465 - hplip-3.23.8 is available

* Tue Oct 03 2023 Zdenek Dohnal <zdohnal@redhat.com> - 3.23.5-10
- BSD-3-Clause-HP and python-ldap are added into SPDX list

* Thu Aug 24 2023 Zdenek Dohnal <zdohnal@redhat.com> - 3.23.5-9
- hp-check: use pkgconf when checking for cups version

* Thu Aug 03 2023 Zdenek Dohnal <zdohnal@redhat.com> - 3.23.5-8
- fallback to using external plugin for Hbpl1 printers

* Fri Jul 28 2023 Zdenek Dohnal <zdohnal@redhat.com> - 3.23.5-7
- SPDX migration

* Thu Jul 27 2023 Zdenek Dohnal <zdohnal@redhat.com> - 3.23.5-6
- remove redundant files

* Fri Jul 21 2023 Zdenek Dohnal <zdohnal@redhat.com> - 3.23.5-6
- fix syntax warnings

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Adam Williamson <awilliam@redhat.com> - 3.23.5-4
- Require curl, not curl-minimal, due to conflicts

* Mon Jul 17 2023 Zdenek Dohnal <zdohnal@redhat.com> - 3.23.5-3
- 2192131 - parseQueues() doesn't get device uri from 'lpstat -v', because parsing pattern changed
- switch to curl when downloading plugin
- 2221311 - [python3.12] hplip tools/binaries crash due depending on removed configparser.readfp()

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.23.5-2
- Rebuilt for Python 3.12

* Tue Jun 06 2023 Zdenek Dohnal <zdohnal@redhat.com> - 3.23.5-1
- 2184067 - hplip-3.23.5 is available

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Zdenek Dohnal <zdohnal@redhat.com> - 3.22.10-3
- 2148210 - hplip: pcardext Python extension broken
- stop shipping hp-unload, since it depends on pcardext

* Thu Nov 24 2022 Florian Weimer <fweimer@redhat.com> - 3.22.10-2
- C99 compatibility fixes
- Stop building the pcardext Python extension because it unusable (#2148210)

* Wed Nov 23 2022 Zdenek Dohnal <zdohnal@redhat.com> - 3.22.10-1
- 2139309 - hplip-3.22.10 is available

* Wed Oct 19 2022 Zdenek Dohnal <zdohnal@redhat.com> - 3.22.6-5
- distutils will be removed in Python3.12, use setuptools now

* Thu Oct 13 2022 Zdenek Dohnal <zdohnal@redhat.com> - 3.22.6-4
- bump the NVR

* Thu Oct 13 2022 Zdenek Dohnal <zdohnal@redhat.com> - 3.22.6-3
- 2129849 - hp-plugin unable to load plugin.conf - add a new backup download script

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Zdenek Dohnal <zdohnal@redhat.com> - 3.22.6-1
- 2101790 - hplip-3.22.6 is available

* Mon Jul 18 2022 Zdenek Dohnal <zdohnal@redhat.com> - 3.22.4-3
- recommend libsane-hpaio - duplicated scanners are better than no scanner

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.22.4-2
- Rebuilt for Python 3.11

* Tue May 17 2022 Zdenek Dohnal <zdohnal@redhat.com> - 3.22.4-1
- 2080235 - Misleading errors about missing shared libraries when scanning

* Wed May 11 2022 Zdenek Dohnal <zdohnal@redhat.com> - 3.22.4-1
- 2079740 - hplip-3.22.4 is available

* Mon Mar 28 2022 Zdenek Dohnal <zdohnal@redhat.com> - 3.22.2-2
- make libsane-hpaio only suggested to prevent possible duplicated scanner devices

* Thu Mar 10 2022 Zdenek Dohnal <zdohnal@redhat.com> - 3.22.2-1
- 2059085 - hplip-3.22.2 is available

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.21.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Zdenek Dohnal <zdohnal@redhat.com> - 3.21.12-1
- 2015910 - [GUI] hp-setup crashes when loading smart_install module

* Fri Jan 14 2022 Zdenek Dohnal <zdohnal@redhat.com> - 3.21.12-1
- 1959242 - hplip-3.21.12 is available

* Fri Dec 03 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.21.2-15
- 2028697 - hp-setup trackbacks when hplip-gui RPM is not installed

* Tue Nov 23 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.21.2-14
- 2025853 - hplip: double "and" in license

* Tue Oct 26 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.21.2-13
- 2015428 - python3.10 has Callable in collections.abc
- GUI hp-setup uses avahi-browse
- adjust osname for CoreOS/Linux
- 2015428 - python3.10 doesn't do an implicit conversion for integer arguments

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.21.2-12
- Rebuilt with OpenSSL 3.0.0

* Fri Sep 03 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.21.2-11
- 1995647 - Hplip package shows as proprietary in Gnome Software

* Fri Jul 30 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.21.2-10
- 1985251 - Incorrect permission for gpg directory
- 1987141 - hp-plugin installs malformed udev files
- fixed warning: redhatenterpriselinux distro is not found in AUTH_TYPES

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.21.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 02 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.21.2-8
- 1976465 - [hplip] PY_SSIZE_T_CLEAN macro must be defined for '#' formats
- require usbutils - needed by hp-diagnose_queues

* Mon Jun 28 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.21.2-7
- sleep after utils.run() (related #1963114)

* Fri Jun 11 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.21.2-6
- 1963114 - patch for hplip firmware load timeout fix

* Wed Jun 09 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.21.2-5
- track hplip-repack.sh as source, to have it in srpm

* Wed Jun 09 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.21.2-4
- remove redundant files

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.21.2-3
- Rebuilt for Python 3.10

* Thu Apr 22 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.21.2-2
- 1951922 - hp-systray doesn't support a valid --qt5 option

* Fri Feb 19 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.21.2-1
- 1929977 - hplip-3.21.2 is available

* Fri Feb 19 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.11-6
- get out of hp-setup if the device is a standalone scanner

* Thu Feb 18 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.11-6
- remove the old search algorithm

* Fri Feb 05 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.11-5
- 1925259 - %pre scriptlet enables and starts cups.service, which is unnecessary
- 1919556 - hp-fab crashed: QFileDialog.getOpenFileName is not used correctly

* Tue Feb 02 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.11-4
- 1912147 - Enable matching for '<model>_series' drivers in PPD search algorithm
- rework optional gui messages

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.11-2
- apply eln changes

* Wed Dec 02 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.11-1
- 1903029 - hplip-3.20.11 is available

* Thu Nov 19 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.9-4
- 1899410 - non-sudoers cannot authenticate because of bad username in prompt

* Thu Nov 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.9-3
- make is no longer in buildroot by default

* Thu Oct 22 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.9-2
- timeb is removed from glibc

* Tue Oct 13 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.9-2
- downloading gpg key for plugin can take some time and wayland can
  kill the connection, work it around to prefer more stable keyservers

* Mon Oct 12 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.9-2
- fix the patch for adding uncompressed ppd via CLI
- fix the patch for GUI too

* Fri Oct 02 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.9-1
- 3.20.9

* Wed Sep 30 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.6-13
- fix bashisms in hplip-configure-python.patch
- thanks for Daniel Pielmeier from Gentoo for review

* Fri Sep 11 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.6-12
- move ifdef for removing hplip-gui a little in install phase

* Thu Aug 27 2020 Josef Ridky <jridky@redhat.com> - 3.20.6-11
- Rebuilt for new net-snmp release

* Tue Aug 25 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.6-10
- fix eln build - remove unpackaged files

* Tue Aug 25 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.6-9
- 1772698 - dont use uninitialized value as an index

* Mon Aug 24 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.6-8
- typo in hplip-model-mismatch.patch causes regression for 1772698

* Wed Aug 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.6-7
- don't build gui for newer RHELs

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.6-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.6-5
- 1861055 - hplip: remove threading.Thread.isAlive method calls - use threading.Thread.is_alive()

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tom Stellard <tstellar@redhat.com> - 3.20.6-3
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue Jun 23 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.6-2
- appdata.xml needs to be in %%{_datadir}/metainfo

* Wed Jun 17 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.6-1
- 3.20.6

* Tue Jun 16 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.5-6
- remove the check for scripts which are only in hplip-gui

* Tue Jun 16 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.5-5
- fix the optional GUI

* Fri Jun 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.5-4
- 1833308 - hp-clean cannot clean HP PSC1410 - Device I/O error

* Mon Jun 01 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.5-4
- 1794147 - HP-setup crashes with Python3 ui5 module not found error
- 1590014 - hplip PPD search doesn't expect '-' in device name

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.20.5-3
- Rebuilt for Python 3.9

* Mon May 25 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.5-2
- fix infinite loop in password dialog in hp-toolbox

* Thu May 14 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.5-1
- 3.20.5

* Wed Apr 15 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.3-5
- model mismatch during scanning due 'HP_' string

* Tue Apr 07 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.3-4
- add keyserver.ubuntu.com too (1821469)

* Tue Apr 07 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.3-3
- 1821469 - use list of keyservers when trying to download gpg keys

* Wed Mar 25 2020 Tom Stellard <tstellar@redhat.com> - 3.20.3-2
- Fix some -Wreturn-type warnings
- clang treates these as errors, so this fixes the build with clang.

* Tue Mar 10 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.3-1
- 3.20.3

* Wed Mar 04 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.20.2-1
- 3.20.2

* Mon Feb 17 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.12-4
- 1573430 - sixext.py:to_string_utf8:UnicodeDecodeError: 'utf-8' codec can't decode bytes
- fix pillow version check

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.12-2
- 1788643 - hp-plugin needs explicit requirement for tar

* Thu Dec 12 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.12-1
- 3.19.12

* Thu Nov 28 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.11-1
- 3.19.11

* Thu Nov 28 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.10-3
- 1777457 - hplip-3.19.10-2 breaks support for devices with '_series' in device id

* Mon Nov 18 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.10-2
- 1773345 - Problems with HP M281fdw LaserJet

* Fri Nov 15 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.10-2
- 1772698 - missing HP LaserJet 2200 driver

* Fri Nov 01 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.10-1
- 3.19.10

* Tue Oct 01 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.8-2
- hp-check traceback due change in python-pillow

* Tue Oct 01 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.8-1
- 3.19.8

* Tue Sep 10 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.6-9
- 1739855, 1740132, 1742949 - missing drivers

* Mon Sep 09 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.6-8
- 1750111 - [abrt] hplip: syntax(): unindent does not match any outer indentation level

* Fri Sep 06 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.6-7
- 1745317 - hp-plugin is broken on Rawhide

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.19.6-6
- Rebuilt for Python 3.8

* Thu Aug 08 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.6-5
- 1738321 - [abrt] hp-systray:BlockingIOError: [Errno 11] Resource temporarily unavailable

* Thu Aug 01 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.6-4
- sks-keyservers.net seems more reliable

* Mon Jul 29 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.6-3
- 1733449 - Scanner on an HP AIO printer is not detected unless libsane-hpaio is installed

* Thu Jul 25 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.6-2
- 1727162 - [abrt] hplip: strlen(): hp killed by SIGSEGV

* Fri Jul 12 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.19.6-1
- 3.19.6

* Fri Jul 12 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.12-16
- fixing issues found by coverity scan

* Thu Jul 11 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.12-15
- ignore symlinks when installing plugins, because they are ubuntu-specific
  and are not used, but its checking breaks plugin installation

* Tue Jul 09 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.12-14
- remove old obsoletes and provides for hpijs, libsane-hpoj and hplip-compat-libs

* Wed Jun 26 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.12-13
- fix #1722222 without downstream patch, just call desktop-install-file with
  other parameters

* Thu Jun 20 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.12-12
- 1722222 - Broken hp-uiscan.desktop (upstream bug)

* Thu May 16 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.12-11
- 1706233 - hplip FTBFS with python38

* Mon Apr 15 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.12-10
- fix several desktop issues reported in bodhi

* Thu Apr 04 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.12-9
- 1695716 - hpcups crashes in Compressor destructor

* Mon Apr 01 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.12-8
- 1694663 - Cannot scan with M281fdw LaserJet - failed: Error during device I/O

* Mon Apr 01 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.12-7
- 1694569 - hp-uiscan does not have interactive mode

* Mon Mar 25 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.12-6
- 1684434 - Scanning broken for HP LaserJet 3052

* Mon Mar 04 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.12-5
- 1684792 - devel-file-in-non-devel-package /usr/lib64/libhpmud.so

* Tue Feb 05 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.12-4
- 1671513 - after 'successful' plugin installation it is not installed

* Fri Feb 01 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.12-3
- m277-m281 printer support got some fixes, so try to do not use our downstream patch
- hpcups-update-ppds can freeze sometimes, add timeout for to be sure
- fixed hp-setup crash when user wants to define path to PPD file

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.12-1
- 3.18.12

* Mon Dec 03 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.6-12
- Built with new net-snmp

* Tue Nov 13 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.6-11
- 1641100 - Retrieval of signing keys for plugin verification should use a server pool

* Mon Nov 12 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.6-10
- 1645815 - hp-check --runtime crashes involving FileNotFoundError

* Mon Oct 01 2018 Tomas Korbar <tkorbar@redhat.com> - 3.18.6-9
- 1594602 - Fix typos in QMessageBox constructor calls

* Mon Oct 01 2018 Tomas Korbar <tkorbar@redhat.com> - 3.18.6-8 
- 1626877 - Fix AttributeError when connecting to printer via wifi

* Tue Sep 25 2018 Tomas Korbar <tkorbar@redhat.com> - 3.18.6-7
- 1566938 - Fix TypeError when printing ImportError message in hpfax

* Tue Sep 18 2018 Tomas Korbar <tkorbar@redhat.com> - 3.18.6-6
- 1564770 - Fix TypeError when printing error object message

* Tue Jul 24 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.6-5
- correcting license

* Sat Jul 21 2018 Kevin Fenzi <kevin@scrye.com> - 3.18.6-4
- Rebuild for new net-snmp

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.18.6-2
- Rebuilt for Python 3.7

* Mon Jun 11 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.6-1
- 3.18.6, have cups running because hp tools

* Fri May 25 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.5-2
- hp-setup fails on fax setup - use binary strings 
- m278-m281 doesn;t work correctly again

* Thu May 24 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.5-1
- 3.18.5

* Thu May 24 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.4-3
- revert 1544912

* Fri May 11 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.4-2
- 1577078 - add other trap for missing gui

* Thu Apr 26 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.4-1
- 3.18.4

* Tue Apr 24 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.3-3
- 1544912 - hp colorlaserjet m278-m281 doesn't install correctly

* Wed Apr 18 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.3-2
- set dependency directly to /usr/bin/gpg

* Mon Mar 12 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.18.3-1
- 3.18.3 

* Wed Feb 28 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.11-10
- name libraries explicitly

* Mon Feb 19 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.11-9
- gcc and gcc-c++ are no longer in buildroot by default

* Tue Feb 13 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.11-8
- 1544788 - HP ColorLaserjet MFP M278-M281 - missing family class 

* Tue Feb 13 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.11-7
- Rebuild for mass rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 12 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.11-5
- 1533869 - hp-firmware:NameError: name 'INTERACTIVE_MODE4' is not defined

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.17.11-4
- Remove obsolete scriptlets

* Mon Jan 08 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.11-3
- fixing 1528851 for option -xraw

* Tue Jan 02 2018 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.11-2
- 1528851 - Unable to scan and save jpg with color with hp-scan

* Thu Dec 07 2017 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.11-1
- 3.17.11

* Mon Nov 06 2017 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.10-3
- 1509394 - Add support for HP ColorLaserjet MFP M278-M281

* Thu Oct 26 2017 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.10-2
- changing url

* Fri Oct 20 2017 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.10-1
- rebase to 3.17.10

* Wed Oct 04 2017 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.9-2
- 1498487 - Add missing Exec line in desktop file

* Wed Sep 20 2017 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.9-1
- rebase to 3.17.9

* Fri Aug 04 2017 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.6-1
- rebase to 3.17.6
- adding hplip-rebase.sh script for testing if plugin is available - removing its testing from spec

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.17.4-5
- Rebuild due to bug in RPM (RHBZ #1468476)

* Mon May 29 2017 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.4-4
- 1456467 - hp-check shows 'CUPS incompatible or not running' even if CUPS is running 

* Tue May 09 2017 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.4-3
- added appdata.xml, several tools moved into gui subpackage because they don't have CLI variant and use only GUI, hp-pqdiag was removed because it is deprecated and not functional

* Wed Apr 26 2017 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.4-2
- 1440502 - hp 8610 Filter failed when trying to print on fedora 26 - redo hplip-noernie.patch

* Mon Apr 24 2017 Zdenek Dohnal <zdohnal@redhat.com> - 3.17.4-1
- rebase to 3.17.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.11-6
- reverting previous commit

* Wed Jan 11 2017 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.11-5
- added Requires: python3-qt5

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.16.11-4
- Rebuild for Python 3.6

* Tue Nov 29 2016 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.11-3
- fixing requires for hpplugincheck

* Mon Nov 28 2016 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.11-2
- adding spec switch hpplugincheck - for testing if new hp plugin is available

* Fri Nov 25 2016 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.11-1
- rebase to 3.16.11

* Mon Oct 31 2016 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.10-1
- rebase to 3.16.10, removed include-ppdh patch

* Mon Oct 24 2016 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.9-2
- changing url to http://hplipopensource.com/

* Thu Sep 22 2016 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.9-1
- rebase to 3.16.9 

* Thu Sep 01 2016 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.8-2
- bad whitespaces (bug #1372343)

* Tue Aug 30 2016 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.8-1
- rebase to 3.16.8

* Fri Aug 12 2016 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.7-4
- adding jpopelka's patch into hplip-ui-optional.patch (launchpad #1612132)

* Wed Aug 10 2016 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.7-3
- editing previous commit

* Wed Aug 10 2016 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.7-2
- 1361968 - adding error message when hp-setup fails because of missing hplip-gui

* Mon Aug 08 2016 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.7-2
- hplip license problem - removing proprietary ErnieFilters.{cpp,h} + ernieplatform.h, disabling PCL3GUI2 driver (because of using proprietary ErnieFilters)

* Thu Jul 21 2016 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.7-1
- 1358761 - Rebase 3.16.7

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.5-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 11 2016 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.5-3
- including cups/ppd.h into HPCupsFilter.h and hpcupsfax.h

* Wed Jun 22 2016 Zdenek Dohnal <zdohnal@redhat.com> - 3.16.5-2
- bug 1341304 - name 'source_option' is not defined

* Thu May 19 2016 Jiri Popelka <jpopelka@redhat.com> - 3.16.5-1
- 3.16.5 (gui moves from Qt4 to Qt5)

* Fri Mar 18 2016 zdohnal <zdohnal@redhat.com> - 3.16.3-1
- 3.16.3

* Tue Feb 09 2016 Jiri Popelka <jpopelka@redhat.com> - 3.16.2-1
- 3.16.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Jiri Popelka <jpopelka@redhat.com> - 3.15.11-6
- updated patch for bug #1249414

* Fri Jan 22 2016 Jiri Popelka <jpopelka@redhat.com> - 3.15.11-5
- hp-plugin hangs on 'su' (bug #1249414).

* Mon Jan 04 2016 Jiri Popelka <jpopelka@redhat.com> - 3.15.11-4
- Don't try to write bytecode cache for hpps filter (bug #1241548).

* Thu Dec 10 2015 Jiri Popelka <jpopelka@redhat.com> - 3.15.11-3
- move 56-hpmud.rules into main package completely (bug #1033952)

* Wed Nov 18 2015 Jiri Popelka <jpopelka@redhat.com> - 3.15.11-2
- run autoreconf instead of patching libtool script to work-around rpath issues

* Mon Nov 16 2015 Jiri Popelka <jpopelka@redhat.com> - 3.15.11-1
- 3.15.11

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.15.9-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 05 2015 Jiri Popelka <jpopelka@redhat.com> - 3.15.9-4
- Rebuilt for Python3.5 rebuild

* Fri Oct 23 2015 Tim Waugh <twaugh@redhta.com> - 3.15.9-3
- Don't try to write bytecode cache for hp-config_usb_printer (bug #1266903).

* Fri Sep 25 2015 Jiri Popelka <jpopelka@redhat.com> - 3.15.9-2
- Don't specify python version in hplip-printer@.service (bug #1266423)

* Tue Sep 15 2015 Jiri Popelka <jpopelka@redhat.com> - 3.15.9-1
- 3.15.9

* Tue Aug 18 2015 Jiri Popelka <jpopelka@redhat.com> - 3.15.7-5
- remove compat-libs subpackage (bug #1196237)
- make copy-deviceid.py Python 3 compatible

* Tue Aug 11 2015 Jiri Popelka <jpopelka@redhat.com> - 3.15.7-4
- Upstream fix for 'Stopped "Filter Failed"' (Launchpad #1476920)

* Thu Jul 30 2015 Jiri Popelka <jpopelka@redhat.com> - 3.15.7-3
- fix hpijs Obsoletes & Provides
- remove Group tag

* Wed Jul 29 2015 Jiri Popelka <jpopelka@redhat.com> - 3.15.7-2
- merge hpijs into main package (#1033952#14)
- ship hp-config_usb_printer in main package along with
  udev rule and unit file (#1033952#11)

* Wed Jul 15 2015 Jiri Popelka <jpopelka@redhat.com> - 3.15.7-1
- 3.15.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.15.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jiri Popelka <jpopelka@redhat.com> - 3.15.6-1
- 3.15.6

* Thu Apr 16 2015 Jiri Popelka <jpopelka@redhat.com> - 3.15.4-1
- 3.15.4

* Mon Mar 23 2015 Jiri Popelka <jpopelka@redhat.com> - 3.15.2-9
- Build and ship also Python 2 modules for hp-plugin (bug #1196237).

* Fri Mar 20 2015 Tim Waugh <twaugh@redhat.com> - 3.15.2-7
- filters: don't use 'env' when starting Python (bug #1202451).

* Mon Mar 16 2015 Tim Waugh <twaugh@redhat.com> - 3.15.2-6
- Ignore IOError when logging output (bug #712537).

* Fri Mar 13 2015 Tim Waugh <twaugh@redhat.com> - 3.15.2-5
- Requires python3-PyQt4, not PyQt4.

* Thu Mar 12 2015 Jiri Popelka <jpopelka@redhat.com> - 3.15.2-4
- Make reportlab.patch Python3 compatible (bug #1201088).

* Tue Mar  3 2015 Tim Waugh <twaugh@redhat.com> - 3.15.2-3
- Move PPDs requiring hpps to the main package along with the filter
  itself (bug #1194186).
- Don't try to write bytecode cache for hpfax backend (bug #1192761).

* Thu Feb 12 2015 Tim Waugh <twaugh@redhat.com> - 3.15.2-2
- Don't ship hp-logcapture or hp-doctor (bug #1192090). They are not
  useful in Fedora.

* Wed Feb 04 2015 Jiri Popelka <jpopelka@redhat.com> - 3.15.2-1
- 3.15.2

* Wed Jan 21 2015 Tim Waugh <twaugh@redhat.com> - 3.14.10-8
- No need to remove hpcac as it is no longer provided upstream.

* Wed Jan 21 2015 Tim Waugh <twaugh@redhat.com> - 3.14.10-7
- Fixed uses of strncpy throughout.

* Wed Jan 14 2015 Tim Waugh <twaugh@redhat.com> - 3.14.10-6
- Requires python3-cups to get postscriptdriver() tags.

* Tue Dec 23 2014 Tim Waugh <twaugh@redhat.com> - 3.14.10-5
- Fixed left/right margins for HP DeskJet 990C (LP #1405212).

* Tue Nov  4 2014 Tim Waugh <twaugh@redhat.com> - 3.14.10-4
- IEEE 1284 Device ID for HP LaserJet Professional M1132 MFP
  (bug #1158743 comment #5).
- IEEE 1284 Device ID for HP LaserJet Color M451dn (bug #1159380).

* Fri Oct 31 2014 Tim Waugh <twaugh@redhat.com> - 3.14.10-3
- Fixed build against libjpeg-turbo 1.3.90.

* Fri Oct 31 2014 Tim Waugh <twaugh@redhat.com> - 3.14.10-2
- Fixed incorrect name in function call in makeURI when a parallel
  port device is used (bug #1159161).

* Tue Oct 07 2014 Jiri Popelka <jpopelka@redhat.com> - 3.14.10-1
- 3.14.10

* Tue Aug 26 2014 Tim Waugh <twaugh@redhat.com> - 3.14.6-7
- Reverted previous change as it didn't help (bug #1076954).

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Tim Waugh <twaugh@redhat.com> - 3.14.6-5
- Main package requires gnupg (bug #1118724).
- Fixed version comparisons for x.y.z-style versions such as
  reportlab (bug #1121433).

* Wed Jul  9 2014 Tim Waugh <twaugh@redhat.com> - 3.14.6-4
- Bumped release.

* Wed Jul  9 2014 Tim Waugh <twaugh@redhat.com> - 3.14.6-3
- Another fix for commafy() (bug #984167/bug #1076954 comment #21).

* Tue Jun 17 2014 Jiri Popelka <jpopelka@redhat.com> - 3.14.6-2
- Fix parsing of avahi-daemon output (bug #1096939).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 05 2014 Jiri Popelka <jpopelka@redhat.com> - 3.14.6-1
- 3.14.6

* Thu May 22 2014 Jiri Popelka <jpopelka@redhat.com> - 3.14.4-5
- Treat logging before importing of logger module (bug #984699).

* Tue Apr 29 2014 Tim Waugh <twaugh@redhat.com> - 3.14.4-4
- Fixed scan-tmp patch (bug #1076954).

* Tue Apr 22 2014 Tim Waugh <twaugh@redhat.com> - 3.14.4-3
- Fix for last fix (bug #984167).

* Wed Apr 16 2014 Tim Waugh <twaugh@redhat.com> - 3.14.4-2
- Fixed codec issue (bug #984167).

* Wed Apr 09 2014 Jiri Popelka <jpopelka@redhat.com> - 3.14.4-1
- 3.14.4

* Fri Apr  4 2014 Tim Waugh <twaugh@redhat.com> - 3.14.3-3
- Scan to /var/tmp instead of /tmp (bug #1076954).

* Mon Mar 10 2014 Jiri Popelka <jpopelka@redhat.com> - 3.14.3-2
- BuildRequires: pkgconfig(dbus-1) instead of dbus-devel

* Fri Mar 07 2014 Jiri Popelka <jpopelka@redhat.com> - 3.14.3-1
- 3.14.3
- --enable-udev-acl-rules configure flag has been removed upstream

* Thu Jan 09 2014 Jiri Popelka <jpopelka@redhat.com> - 3.14.1-1
- 3.14.1

* Wed Nov 27 2013 Jiri Popelka <jpopelka@redhat.com> - 3.13.11-4
- do not %%ghost /run/hplip (bug #1034928)

* Mon Nov 25 2013 Tim Waugh <twaugh@redhat.com> - 3.13.11-3
- Moved hp-doctor to gui sub-package as it requires check module
  (bug #1015441).

* Thu Nov 21 2013 Jiri Popelka <jpopelka@redhat.com> - 3.13.11-2
- create /usr/lib/tmpfiles.d/hplip.conf (bug #1015831).

* Wed Nov 06 2013 Jiri Popelka <jpopelka@redhat.com> - 3.13.11-1
- 3.13.11

* Tue Oct 15 2013 Jaromír Končický <jkoncick@redhat.com> - 3.13.10-1
- 3.13.10: 8 patches applied upstream, big changes in tmp and log dirs, removed hp-mkuri
- Fixed Incorrect IEEE 1284 MFG value for LaserJet Professional P1102 (bug #1018826).

* Wed Sep 18 2013 Tim Waugh <twaugh@redhat.com> - 3.13.9-2
- Applied patch to avoid unix-process authorization subject when using
  polkit as it is racy (bug #1009541, CVE-2013-4325).

* Tue Sep 10 2013 Jiri Popelka <jpopelka@redhat.com> - 3.13.9-1
- 3.13.9: hplipjs filter removed, several patches applied upstream

* Wed Aug 14 2013 Tim Waugh <twaugh@redhat.com> - 3.13.8-2
- Moved hpps filter to hpijs sub-package (bug #996852).
- Fixed typo in systemtray.py (bug #991638).

* Tue Aug 13 2013 Jiri Popelka <jpopelka@redhat.com> - 3.13.8-1
- 3.13.8

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Jiri Popelka <jpopelka@redhat.com> - 3.13.7-1
- 3.13.7
- Device IDs for CM4540 (bug #968177) and cp4005 (bug #980976).


* Mon Jun 24 2013 Jiri Popelka <jpopelka@redhat.com> - 3.13.6-2
- add one more arch-specific dependency.

* Mon Jun 24 2013 Jiri Popelka <jpopelka@redhat.com> - 3.13.6-1
- 3.13.6
- hplip-ipp-accessors.patch merged upstream
- /etc/cron.daily/hplip_cron -> /usr/share/hplip/hplip_clean.sh

* Wed May 29 2013 Tim Waugh <twaugh@redhat.com> - 3.13.5-2
- Avoid several bugs in createTempFile (bug #925032).

* Tue May 14 2013 Jiri Popelka <jpopelka@redhat.com> - 3.13.5-1
- 3.13.5
- change udev rule to not add printer queue, just check plugin.

* Fri May 10 2013 Jiri Popelka <jpopelka@redhat.com> - 3.13.4-3
- Device ID for HP LaserJet 2200 (bug #873123#c8).

* Thu Apr 11 2013 Tim Waugh <twaugh@redhat.com> - 3.13.4-2
- Fixed changelog dates.
- Device ID for HP LaserJet P1005 (bug #950776).
- mark cron job file as config(noreplace)

* Tue Apr 09 2013 Jiri Popelka <jpopelka@redhat.com> - 3.13.4-1
- 3.13.4

* Fri Mar 15 2013 Jiri Popelka <jpopelka@redhat.com> - 3.13.3-3
- Remove unused Requires.

* Thu Mar 14 2013 Tim Waugh <twaugh@redhat.com> - 3.13.3-2
- Moved hpfax pipe to /var/run/hplip (bug #917756).

* Fri Mar 08 2013 Jiri Popelka <jpopelka@redhat.com> - 3.13.3-1
- 3.13.3

* Thu Feb 14 2013 Jiri Popelka <jpopelka@redhat.com> - 3.13.2-1
- 3.13.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Jiri Popelka <jpopelka@redhat.com> - 3.12.11-7
- No need to run update-desktop-database (and require desktop-file-utils)
  because there are no MimeKey lines in the desktop files.

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 3.12.11-6
- rebuild due to "jpeg8-ABI" feature drop

* Fri Jan 18 2013 Jiri Popelka <jpopelka@redhat.com> 3.12.11-5
- Use arch-specific dependencies.
- Don't provide private python extension libs.

* Wed Jan 16 2013 Jiri Popelka <jpopelka@redhat.com> 3.12.11-4
- hpijs no longer requires net-snmp (bug #376641, bug #895643).

* Tue Jan 15 2013 Jiri Popelka <jpopelka@redhat.com> 3.12.11-3
- Use the form of import of PIL that is pillow compatible (bug #895266).

* Fri Dec 07 2012 Jiri Popelka <jpopelka@redhat.com> 3.12.11-2
- desktop file: remove deprecated Encoding key and Application category

* Tue Nov 27 2012 Jiri Popelka <jpopelka@redhat.com> 3.12.11-1
- 3.12.11
-- release-parport.patch merged upstream

* Thu Nov 22 2012 Tim Waugh <twaugh@redhat.com> 3.12.10-5.a
- Make 'hp-check' check for hpaio set-up correctly (bug #683007).

* Wed Oct 17 2012 Tim Waugh <twaugh@redhat.com> 3.12.10-4.a
- Some more CUPS filters using the wrong temporary directory
  (bug #865603).

* Tue Oct 16 2012 Tim Waugh <twaugh@redhat.com> 3.12.10-3.a
- CUPS filters should use TMPDIR when available (bug #865603).

* Thu Oct 11 2012 Jiri Popelka <jpopelka@redhat.com> 3.12.10-2.a
- 3.12.10a

* Thu Oct 04 2012 Jiri Popelka <jpopelka@redhat.com> 3.12.10-1
- 3.12.10

* Tue Oct 02 2012 Jiri Popelka <jpopelka@redhat.com> 3.12.9-6
- Ship %%{_localstatedir}/log/hp/tmp directory (bug #859658)

* Thu Sep 27 2012 Jiri Popelka <jpopelka@redhat.com> 3.12.9-5
- remove useless Conflicts:, Obsoletes: and Provides: fields
- remove %%pre section (stopping&disabling of hplip service on upgrade)
- make hplip_cron work with non-english locale

* Mon Sep 24 2012 Jiri Popelka <jpopelka@redhat.com> 3.12.9-4
- amend hplip-notification-exception.patch (bug #859543).

* Thu Sep 20 2012 Jiri Popelka <jpopelka@redhat.com> 3.12.9-3
- Support IEEE 1284.4 protocol over USB (bug #858861).

* Fri Sep 07 2012 Jiri Popelka <jpopelka@redhat.com> 3.12.9-2
- build against CUPS-1.6

* Fri Sep 07 2012 Jiri Popelka <jpopelka@redhat.com> 3.12.9-1
- 3.12.9
-- no longer needed: fax-ppd.patch

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Jiri Popelka <jpopelka@redhat.com> 3.12.6-1
- 3.12.6

* Tue Jun 05 2012 Jiri Popelka <jpopelka@redhat.com> 3.12.4-3
- Require systemd instead of udev.

* Mon Apr 30 2012 Tim Waugh <twaugh@redhat.com> 3.12.4-2
- The hpijs sub-package no longer requires cupsddk-drivers (which no
  longer exists as a real package), but cups >= 1.4.

* Thu Apr 12 2012 Jiri Popelka <jpopelka@redhat.com> 3.12.4-1
- 3.12.4

* Wed Mar 21 2012 Tim Waugh <twaugh@redhat.com> 3.12.2-4
- Release parport if unsupported model connected (bug #699052).

* Wed Feb 29 2012 Tim Waugh <twaugh@redhat.com> 3.12.2-3
- Added another IEEE 1284 Device ID for Color LaserJet CP2025dn to
  cope with its DNS-SD response, which has no usb_* keys (bug #651509).

* Wed Feb 22 2012 Tim Waugh <twaugh@redhat.com> 3.12.2-2
- Added IEEE 1284 Device ID for LaserJet Professional P1102w (bug #795958).

* Tue Feb 07 2012 Jiri Popelka <jpopelka@redhat.com> 3.12.2-1
- 3.12.2

* Wed Jan 18 2012 Jiri Popelka <jpopelka@redhat.com> 3.11.12-3
- Added IEEE 1284 Device ID for LaserJet P2035.

* Wed Jan 11 2012 Tim Waugh <twaugh@redhat.com> 3.11.12-2
- When copying Device IDs from hpcups to hpijs, use ModelName as the
  key instead of ShortNickName (bug #651509 comment #7).

* Mon Dec 19 2011 Jiri Popelka <jpopelka@redhat.com> 3.11.12-1
- 3.11.12

* Mon Nov 21 2011 Tim Waugh <twaugh@redhat.com> 3.11.10-11
- Added IEEE 1284 Device ID for Designjet T770 (bug #747957).

* Wed Nov 16 2011 Tim Waugh <twaugh@redhat.com> 3.11.10-10
- Corrected IEEE 1284 Device ID for LaserJet M1120 MFP (bug #754139).

* Wed Nov 16 2011 Jiri Popelka <jpopelka@redhat.com> 3.11.10-9
- revert prnt/hpcups/HPCupsFilter.cpp 3.11.5->3.11.7 change (bug #738089).

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.10-8
- Rebuilt for glibc bug#747377

* Tue Oct 25 2011 Tim Waugh <twaugh@redhat.com> 3.11.10-7
- Catch DBusException in hp-systray (bug #746024).

* Mon Oct 24 2011 Jiri Popelka <jpopelka@redhat.com> 3.11.10-6
- Move udev rules to /lib/udev/rules.d (bug #748208).

* Thu Oct 20 2011 Tim Waugh <twaugh@redhat.com> 3.11.10-5
- Pay attention to the SANE localOnly flag in hpaio (bug #743593).

* Mon Oct 17 2011 Tim Waugh <twaugh@redhat.com> 3.11.10-4
- Corrected IEEE 1284 Device ID for LaserJet M1319f MFP (bug #746614)

* Wed Oct 12 2011 Tim Waugh <twaugh@redhat.com> 3.11.10-3
- Corrected IEEE 1284 Device ID for LaserJet M1522nf MFP (bug #745498).

* Fri Oct  7 2011 Tim Waugh <twaugh@redhat.com> 3.11.10-2
- Corrected IEEE 1284 Device IDs:
  - LaserJet M1536dnf MFP (bug #743915)
  - PSC 1600 series (bug #743821)

* Tue Oct 04 2011 Jiri Popelka <jpopelka@redhat.com> 3.11.10-1
- 3.11.10
- Use _cups_serverbin macro from cups-devel for where to put driver executables.
- No need to define BuildRoot and clean it in clean and install section anymore.
- Corrected IEEE 1284 Device IDs:
  Officejet 6300 series (bug #689378)
  LaserJet Professional M1212nf MFP (bug #742490)

* Fri Sep 23 2011 Tim Waugh <twaugh@redhat.com> 3.11.7-5
- Fixed broken patch for pstotiff.

* Tue Sep 06 2011 Jiri Popelka <jpopelka@redhat.com> 3.11.7-4
- Fixed xsane crash when doing a multi-image scan (bug #725878)

* Fri Sep  2 2011 Tim Waugh <twaugh@redhat.com> 3.11.7-3
- Fixed hpcups crash when required plugin missing (bug #733461).

* Thu Aug 18 2011 Tim Waugh <twaugh@redhat.com> 3.11.7-2
- Create debugging files securely (CVE-2011-2722, bug #725830).

* Mon Jul 25 2011 Jiri Popelka <jpopelka@redhat.com> 3.11.7-1
- 3.11.7

* Mon Jul 11 2011 Jiri Popelka <jpopelka@redhat.com> 3.11.5-5
- rebuilt against new net-snmp-5.7

* Tue Jun 28 2011 Tim Waugh <twaugh@redhat.com> 3.11.5-4
- Added Device ID for HP LaserJet Professional P1606dn (bug #708472).
- Update IEEE 1284 Device IDs in hpijs.drv from hpcups.drv.

* Fri Jun 10 2011 Tim Waugh <twaugh@redhat.com> 3.11.5-3
- Fix building against CUPS 1.5.
- Re-create installed hpcups PPDs unconditionally (bug #712241).

* Thu May 19 2011 Jiri Popelka <jpopelka@redhat.com> 3.11.5-2
- Main package requires wget to avoid
  misleading errors about network connectivity (bug #705843).

* Thu May 12 2011 Jiri Popelka <jpopelka@redhat.com> 3.11.5-1
- 3.11.5

* Fri Apr  1 2011 Tim Waugh <twaugh@redhat.com> 3.11.3a-2
- Some rpmlint fixes for obsoletes/provides tags.

* Thu Mar 31 2011 Tim Waugh <twaugh@redhat.com> 3.11.3a-1
- 3.11.3a.

* Fri Mar 18 2011 Jiri Popelka <jpopelka@redhat.com> 3.11.3-1
- 3.11.3 (new hpps filter)

* Tue Mar  1 2011 Jiri Popelka <jpopelka@redhat.com> 3.11.1-5
- Avoid KeyError in ui4/wifisetupdialog.py (bug #680939).
- Corrected IEEE 1284 Device IDs:
  LaserJet 1300 (bug #670548)
  LaserJet 3390 (bug #678565)
  LaserJet P1505 (bug #680951)

* Tue Feb 22 2011 Tim Waugh <twaugh@redhat.com> - 3.11.1-4
- Ship hpijs.drv to give another driver option in case of problems
  with hpcups.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb  4 2011 Tim Waugh <twaugh@redhat.com> - 3.11.1-2
- Fixed typo causing ";marker-supply-low-warning" state reason to be
  reported by hpijs (bug #675151).

* Mon Jan 24 2011 Jiri Popelka <jpopelka@redhat.com> 3.11.1-1
- 3.11.1

* Mon Jan 17 2011 Tim Waugh <twaugh@redhat.com> - 3.10.9-14
- Applied patch to fix CVE-2010-4267, remote stack overflow
  vulnerability (bug #670252).

* Wed Jan 12 2011 Tim Waugh <twaugh@redhat.com> - 3.10.9-13
- Removed unused hpcac filter to avoid unnecessary perl dependency.

* Wed Jan 12 2011 Tim Waugh <twaugh@redhat.com> - 3.10.9-12
- Removed duplicate pstotiff files.

* Wed Jan 12 2011 Tim Waugh <twaugh@redhat.com> - 3.10.9-11
- Fixed "CUPS Web Interface" button (bug #633899).
- Set mimedir explicitly via configure.

* Wed Jan 05 2011 Jiri Popelka <jpopelka@redhat.com> 3.10.9-10
- Catch GError exception when notification showing failed (bug #665577).

* Wed Dec 15 2010 Tim Waugh <twaugh@redhat.com> - 3.10.9-9
- Enable D-Bus threading (and require pygobject2) (bug #600932).
- Fixed incorrect signal name in setup dialog (bug #653626).
- Another missing newline in filter output (Ubuntu #418053).
- Prevent hpaio segfaulting on invalid URIs (bug #649092).
- Catch D-Bus exceptions in fax dialog (bug #645316).

* Fri Dec 03 2010 Jiri Popelka <jpopelka@redhat.com> 3.10.9-8
- Corrected IEEE 1284 Device IDs:
  HP Color LaserJet CP2025dn (bug #651509).
  HP Color LaserJet CM3530 MFP (bug #659381).

* Fri Dec 03 2010 Jiri Popelka <jpopelka@redhat.com> 3.10.9-7
- The pycups requirement is now python-cups.
- Corrected IEEE 1284 Device IDs:
  HP LaserJet 4050/4100/2100 Series/2420/4200/4300/4350/5100/8000
              M3027 MFP/M3035 MFP/P3005/P3010/P4014/P4515 (bug #659039).
  HP Color LaserJet 2500/2550 series/3700/4550/4600/4650/4700/5550
                    CP1515n/CP3525/CP4520/CM2320nf MFP (bug #659040).
  HP Color LaserJet CM4730 MFP (bug #658831).

* Fri Nov 12 2010 Tim Waugh <twaugh@redhat.com> - 3.10.9-6
- Call cupsSetUser in cupsext's addPrinter method before connecting so
  that we can get an authentication callback (bug #538352).
- Prevent hp-fab traceback when run as root.

* Thu Nov 11 2010 Jiri Popelka <jpopelka@redhat.com> 3.10.9-5
- Don't emit SIGNALs in ui4.setupdialog.SetupDialog the PyQt3 way (bug #623834).

* Sun Oct 24 2010 Jiri Popelka <jpopelka@redhat.com> 3.10.9-4
- Avoid UnicodeDecodeError in printsettingstoolbox.py (bug #645739).

* Mon Oct 18 2010 Tim Waugh <twaugh@redhat.com> - 3.10.9-3
- Fixed traceback on error condition in device.py (bug #628125).
- Fixed bogus low ink warnings from hpijs driver (bug #643643).

* Thu Oct 14 2010 Jiri Popelka <jpopelka@redhat.com> - 3.10.9-2
- Fixed utils.addgroup() to return array instead of string (bug #642771).

* Mon Oct 04 2010 Jiri Popelka <jpopelka@redhat.com> - 3.10.9-1
- 3.10.9.

* Thu Sep 30 2010 Tim Waugh <twaugh@redhat.com> - 3.10.6-7
- More fixes from package review:
  - Avoided another macro in comment.
  - Use python_sitearch macro throughout.

* Wed Sep 29 2010 jkeating - 3.10.6-6
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Jiri Popelka <jpopelka@redhat.com> - 3.10.6-5
- Increased timeouts for curl, wget, ping for high latency networks (bug #635388).

* Sat Sep 18 2010 Dan Horák <dan[at]danny.cz> - 3.10.6-4
- drop the ExcludeArch for s390(x)

* Wed Sep 15 2010 Tim Waugh <twaugh@redhat.com>
- Fixes from package review:
  - Main package and hpijs sub-package require cups for directories.
  - The common sub-package requires udev for directories.
  - The libs sub-package requires python for directories.
  - Avoided macro in comment.
  - The lib sub-package now runs ldconfig for post/postun.
  - Use python_sitearch macro.

* Mon Sep 13 2010 Jiri Popelka <jpopelka@redhat.com>
- Added IEEE 1284 Device ID for HP LaserJet 4000 (bug #633227).

* Fri Aug 20 2010 Tim Waugh <twaugh@redhat.com> - 3.10.6-3
- Added another SNMP quirk for an OfficeJet Pro 8500 variant.

* Thu Aug 12 2010 Tim Waugh <twaugh@redhat.com> - 3.10.6-2
- Use correct fax PPD name for Qt3 UI.

* Tue Jul 27 2010 Jiri Popelka <jpopelka@redhat.com> - 3.10.6-1
- 3.10.6.
- Changed shebang /usr/bin/env python -> /usr/bin/python (bug #618351).
- Corrected IEEE 1284 Device IDs:
  - HP Color LaserJet CP1518ni (bug #613689).
  - HP Color LaserJet 2600n (bug #613712).

* Mon Jul 26 2010 Tim Waugh <twaugh@redhat.com>
- Removed selinux-policy version conflict as it is no longer
  necessary.

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 3.10.5-8
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 24 2010 Jiri Popelka <jpopelka@redhat.com> - 3.10.5-7
- Added COPYING to common sub-package.

* Thu Jun 24 2010 Jiri Popelka <jpopelka@redhat.com> - 3.10.5-6
- Main package requires explicit version of hplip-libs.

* Thu Jun 17 2010 Tim Waugh <twaugh@redhat.com> - 3.10.5-5
- Fixed marker-supply attributes in hpijs (bug #605269).

* Wed Jun  9 2010 Tim Waugh <twaugh@redhat.com> - 3.10.5-4
- Mark SNMP quirks in PPD for HP OfficeJet Pro 8500 (bug #581825).

* Mon Jun 07 2010 Jiri Popelka <jpopelka@redhat.com> - 3.10.5-3
- hplip-gui requires libsane-hpaio

* Thu Jun 03 2010 Jiri Popelka <jpopelka@redhat.com> - 3.10.5-2
- Fix ImageableArea for Laserjet 8150/9000 (#596298)

* Mon May 17 2010 Jiri Popelka <jpopelka@redhat.com> - 3.10.5-1
- 3.10.5.   No longer need tray-icon-crash.patch
- Increase the timeout for system tray availability checking (bug #569969).

* Wed May 12 2010 Jiri Popelka <jpopelka@redhat.com> - 3.10.2-16
- Prevent segfault in cupsext when opening PPD file (bug #572775).

* Wed May 12 2010 Jiri Popelka <jpopelka@redhat.com> - 3.10.2-15
- Added/corrected more IEEE 1284 Device IDs:
  - HP LaserJet 4250 (bug #585499).
  - HP Color LaserJet 2605dn (bug #583953).
  - HP LaserJet P1007 (bug #585272).

* Wed May 12 2010 Jiri Popelka <jpopelka@redhat.com> - 3.10.2-14
- Wait for max 30s to see if a system tray becomes available (bug #569969).

* Wed Apr 28 2010 Tim Waugh <twaugh@redhat.com> - 3.10.2-13
- Clear old printer-state-reasons we used to manage (bug #510926).

* Tue Apr 27 2010 Jiri Popelka <jpopelka@redhat.com> - 3.10.2-12
- Added missing newline to string argument in dbglog() call (bug #585275).

* Fri Apr 16 2010 Tim Waugh <twaugh@redhat.com> - 3.10.2-11
- Added/corrected more IEEE 1284 Device IDs:
  - HP Color LaserJet CM1312nfi (bug #581005).
  - HP Color LaserJet 3800 (bug #581935).
  - HP Color LaserJet 2840 (bug #582215).
  - HP PSC 2400 (bug #583103).

* Fri Apr 16 2010 Jiri Popelka <jpopelka@redhat.com> - 3.10.2-10
- Fixed black/blank lines in ljcolor hpcups output (bug #579461).
  Work-around is to send entire blank raster lines instead of skipping them.

* Fri Apr  9 2010 Jiri Popelka <jpopelka@redhat.com> - 3.10.2-9.1
- Added/Corrected several IEEE 1284 Device IDs
  (bugs #577262, #577282, #577282, #577288, #577292, #577302,
  ,#577306, #577308, #577898, #579920, #580231)

* Wed Apr  7 2010 Tim Waugh <twaugh@redhat.com> - 3.10.2-8
- Regenerate hpcups PPDs on upgrade if necessary (bug #579355).

* Fri Mar 26 2010 Jiri Popelka <jpopelka@redhat.com> - 3.10.2-6
- Add Device ID for HP LaserJet 2300 (#576928)

* Tue Mar 23 2010 Tim Waugh <twaugh@redhat.com> - 3.10.2-5
- Explicitly destroy tray icon on exit (bug #543286).

* Thu Mar  4 2010 Tim Waugh <twaugh@redhat.com> - 3.10.2-4
- Main package doesn't require hal.
- Sub-package common requires udev.

* Wed Mar  3 2010 Tim Waugh <twaugh@redhat.com> - 3.10.2-3
- Set defattr in gui sub-package file manifest.
- Avoid mixed use of spaces and tabs.

* Mon Mar  1 2010 Tim Waugh <twaugh@redhat.com> - 3.10.2-2
- Removed SYSFS use in udev rules and actually made them work
  (bug #560754).
- Use a temporary file in pstotiff to allow gs random access.

* Fri Feb 26 2010 Tim Waugh <twaugh@redhat.com> - 3.10.2-1
- 3.10.2.  No longer need preferences-crash patch.
- The pstotiff filter is rubbish so replace it (launchpad #528394).
- Stopped hpcups pointlessly trying to read spool files
  directly (bug #552572).

* Sat Feb 20 2010 Tim Waugh <twaugh@redhat.com> - 3.9.12-8
- Corrected several IEEE 1284 Device IDs using foomatic data
  (launchpad bug #523259).

* Tue Feb 16 2010 Tim Waugh <twaugh@redhat.com> - 3.9.12-7
- Ship %%{_datadir}/hplip/prnt/plugins directory (bug #564551).

* Fri Feb  5 2010 Tim Waugh <twaugh@redhat.com> - 3.9.12-6
- Build requires cups for postscriptdriver tags for .drv file.

* Thu Feb  4 2010 Tim Waugh <twaugh@redhat.com> - 3.9.12-5
- Rebuild for postscriptdriver tags.

* Wed Jan 20 2010 Tim Waugh <twaugh@redhat.com> - 3.9.12-4
- Fixed crash when using Preferences dialog (bug #555979).

* Tue Jan 12 2010 Tim Waugh <twaugh@redhat.com> - 3.9.12-3
- Do ship pkit module even though the PolicyKit mechanism is not
  shipped (bug #554817).

* Tue Jan  5 2010 Tim Waugh <twaugh@redhat.com> - 3.9.12-2
- Retry when connecting to device fails (bug #532112).
- Don't ship PolicyKit mechanism (bug #551773).

* Tue Dec 22 2009 Tim Waugh <twaugh@redhat.com> - 3.9.12-1
- 3.9.12.  No longer need hpcups-plugin patch.

* Thu Dec 10 2009 Tim Waugh <twaugh@redhat.com> - 3.9.10-5
- Reverted fix for bug #533462 until bug #541604 is solved.

* Thu Nov 26 2009 Tim Waugh <twaugh@redhat.com> 3.9.10-4
- Fixed Device ID parsing code in hpijs's dj9xxvip.c (bug #510926).

* Thu Nov 26 2009 Tim Waugh <twaugh@redhat.com> 3.9.10-3
- Removed duplex constraints on page sizes with imageable areas larger
  than possible when duplexing (bug #541572).
- Fixed duplex reverse sides being horizontally flipped (bug #541604).

* Wed Nov 18 2009 Tim Waugh <twaugh@redhat.com> 3.9.10-2
- Fixed duplex handling in hpcups.drv (bug #533462).

* Wed Nov  4 2009 Tim Waugh <twaugh@redhat.com> 3.9.10-1
- 3.9.10.  No longer need clear-previous-state-reasons,
  hpcups-reorder, non-scripts, parenths, plugin-error,
  requirespageregion or state-reasons-newline patches.

* Mon Nov  2 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-21
- Added 'requires proprietary plugin' to appropriate model names
  (bug #513283).

* Fri Oct 30 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-20
- Reverted retry patch until it can be tested some more.

* Thu Oct 29 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-19
- Retry when connecting to device fails (bug #528483).
- Avoid busy loop in hpcups when backend has exited (bug #525944).

* Wed Oct 28 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-18
- Set a printer-state-reason when there's a missing required plugin
  (bug #531330).

* Tue Sep 29 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-17
- Give up trying to print a job to a reconnected device (bug #515481).

* Wed Sep 23 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-16
- Enable parallel port support when configuring (bug #524979).

* Wed Sep 16 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-15
- Fixed hp-setup traceback when discovery page is skipped (bug #523685).

* Fri Aug 28 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-14
- Include missing base files.

* Fri Aug 28 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-13
- Use dll.d file instead of post scriptlet for hpaio (bug #519988).
- Fixed RequiresPageRegion patch (bug #518756).

* Thu Aug 27 2009 Tomas Mraz <tmraz@redhat.com> - 3.9.8-12
- rebuilt with new openssl

* Wed Aug 26 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-11
- Set RequiresPageRegion in hpcups PPDs (bug #518756).

* Tue Aug 25 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-10
- Removed never-used definition of BREAKPOINT in scan/sane/common.h
  in hope of fixing the build.

* Tue Aug 25 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-9
- New common sub-package for udev rules and config file (bug #516459).
- Don't install base/*.py with executable bit set.

* Mon Aug 24 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-8
- Fixed typos in page sizes (bug #515469).
- Build no longer requires libudev-devel.
- Fixed state reasons handling problems (bug #501338).

* Wed Aug 19 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-6
- Make sure to avoid handwritten asm.
- Don't use obsolete configure options.

* Wed Aug 19 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-5
- Use upstream udev rules instead of hal policy (bug #518172).
- Removed unnecessary dependency on PyQt as we only use PyQt4 now.

* Wed Aug 12 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-4
- Upstream patch to fix paper size order and LJColor device class
  color space.

* Wed Aug 12 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-3
- The python-reportlab dependency was in the wrong sub-package.

* Thu Aug  6 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-2
- Removed access_control.grant_group line from HAL fdi file.

* Wed Aug  5 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-1
- 3.9.8.

* Tue Aug  4 2009 Tim Waugh <twaugh@redhat.com> 3.9.6b-5
- Fix hpcups fax PPDs (bug #515356)

* Tue Jul 28 2009 Tim Waugh <twaugh@redhat.com> 3.9.6b-4
- Fixed ui-optional patch for qt4 code path (bug #500473).
- Fixed HWResolution for 'Normal' output from the hpcups driver
  (laundpad bug #405400).

* Mon Jul 27 2009 Tim Waugh <twaugh@redhat.com> 3.9.6b-2
- 3.9.6b.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Tim Waugh <twaugh@redhat.com> 3.9.2-8
- Use existing libusb-using routines to try fetching Device ID.

* Thu Jul 23 2009 Tim Waugh <twaugh@redhat.com> 3.9.2-7
- Error checking in the libudev device-id fallback code.

* Tue Jul 21 2009 Tim Waugh <twaugh@redhat.com> 3.9.2-6
- Fixed device-id reporting.

* Wed Jun 24 2009 Tim Waugh <twaugh@redhat.com> 3.9.2-5
- Set disc media for disc page sizes (bug #495672).

* Mon Mar  9 2009 Tim Waugh <twaugh@redhat.com> 3.9.2-4
- Ship libhpmud.so (bug #489059).
- Fixed no-root-config patch (bug #489055).

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Tim Waugh <twaugh@redhat.com> 3.9.2-2
- 3.9.2.  No longer need systray or quit patches.

* Tue Jan 27 2009 Tim Waugh <twaugh@redhat.com> 2.8.12-7
- Only ship compressed PPD files.

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> 2.8.12-6
- rebuild with new openssl

* Tue Jan 13 2009 Tim Waugh <twaugh@redhat.com> 2.8.12-5
- Fixed Quit menu item in device manager (bug #479751).

* Tue Jan 13 2009 Tim Waugh <twaugh@redhat.com> 2.8.12-4
- Prevent crash when DEVICE_URI/PRINTER environment variables are not
  set (bug #479808 comment 6).

* Tue Jan 13 2009 Tim Waugh <twaugh@redhat.com> 2.8.12-3
- Make --qt4 the default for the systray applet, so that it appears
  in the right place, again (bug #479751).
- Removed hal preprobe rules as they were causing breakage
  (bug #479648).

* Mon Jan 12 2009 Tim Waugh <twaugh@redhat.com> 2.8.12-2
- Don't write to system-wide configuration file (bug #479178).

* Tue Dec 23 2008 Tim Waugh <twaugh@redhat.com> 2.8.12-1
- 2.8.12.

* Thu Dec 11 2008 Tim Waugh <twaugh@redhat.com> 2.8.10-2
- Rediff libsane patch.

* Thu Dec 11 2008 Tim Waugh <twaugh@redhat.com> 2.8.10-1
- 2.8.10.  No longer need gzip-n or quiet patches.

* Thu Dec 11 2008 Tim Waugh <twaugh@redhat.com> 2.8.7-5
- Prevent backend crash when D-Bus not running (bug #474362).

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.8.7-4
- Rebuild for Python 2.6

* Tue Oct 21 2008 Tim Waugh <twaugh@redhat.com> 2.8.7-3
- Ship PPDs in the correct location (bug #343841).

* Fri Sep 26 2008 Tim Waugh <twaugh@redhat.com> 2.8.7-2
- Moved Python extension into libs sub-package (bug #461236).

* Mon Aug  4 2008 Tim Waugh <twaugh@redhat.com> 2.8.7-1
- 2.8.7.
- Avoid hard-coded rpaths.
- New libs sub-package (bug #444016).

* Thu Jul 31 2008 Tim Waugh <twaugh@redhat.com>
- Move libhpip.so* to the main package to avoid libsane-hpaio
  depending on hpijs (bug #457440).

* Thu Jul 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.8.6b-2
- fix license tag

* Mon Jul 28 2008 Tim Waugh <twaugh@redhat.com> 2.8.6b-1
- 2.8.6b.

* Mon Jun 23 2008 Tim Waugh <twaugh@redhat.com> 2.8.6-1
- 2.8.6.  No longer need libm patch.

* Fri Jun  6 2008 Tim Waugh <twaugh@redhat.com> 2.8.5-2
- Make --qt4 the default for the systray applet, so that it appears
  in the right place.  Requires PyQt4.

* Tue Jun  3 2008 Tim Waugh <twaugh@redhat.com> 2.8.5-1
- 2.8.5.
- Configure with --enable-dbus.  Build requires dbus-devel.
- Fix chmod 644 line.
- Ship hp-systray in the gui sub-package, but don't ship the desktop
  launcher yet as the systray applet is quite broken.
- Don't run autoconf.

* Tue May 13 2008 Tim Waugh <twaugh@redhat.com> 2.8.2-3
- Move installer directory to main package (bug #446171).

* Fri Apr  4 2008 Tim Waugh <twaugh@redhat.com> 2.8.2-2
- Update hplip.fdi for Fedora 9: info.bus -> info.subsystem.
- Images in docdir should not be executable (bug #440552).

* Tue Mar  4 2008 Tim Waugh <twaugh@redhat.com> 2.8.2-1
- 2.8.2.  No longer need alloc, unload-traceback or media-empty patches.
- Ship cupsddk driver.  The hpijs sub-package now requires cupsddk-drivers.

* Tue Mar  4 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-6
- Fixed marker-supply-low strings.

* Wed Feb 13 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-5
- Rebuild for GCC 4.3.

* Fri Jan 25 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-4
- The hpijs compression module doesn't allocate enough memory (bug #428536).

* Wed Jan 23 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-3
- Really grant the ACL for the lp group (bug #424331).

* Fri Jan 18 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-2
- Ship installer directory (bug #428246).
- Avoid multilib conflict (bug #341531).
- The hpijs sub-package requires net-snmp (bug #376641).

* Fri Jan 18 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-1
- 2.7.12.  No longer need ljdot4 patch.

* Fri Jan  4 2008 Tim Waugh <twaugh@redhat.com> 2.7.10-2
- Don't ship udev rules; instead, grant an ACL for group lp (bug #424331).

* Fri Dec 07 2007 Release Engineering <rel-eng at fedoraproject dot org> - 2.7.10-2
- Rebuild for deps

* Mon Oct 22 2007 Tim Waugh <twaugh@redhat.com> 2.7.10-1
- 2.7.10.

* Fri Oct 12 2007 Tim Waugh <twaugh@redhat.com> 2.7.9-3
- Applied patch to fix remnants of CVE-2007-5208 (bug #329111).

* Tue Oct  9 2007 Tim Waugh <twaugh@redhat.com> 2.7.9-2
- Use raw instead of 1284.4 communication for LJ4000 series (bug #249191).
- Build requires openssl-devel.

* Wed Oct  3 2007 Tim Waugh <twaugh@redhat.com> 2.7.9-1
- 2.7.9.
- Adjusted udev rules to be less permissive.  We use ConsoleKit to add
  ACLs to the device nodes, so world-writable device nodes can be avoided.

* Tue Sep 25 2007 Tim Waugh <twaugh@redhat.com> 2.7.7-5
- Prevent hpfax trying to load configuration files as user lp.

* Thu Sep  6 2007 Tim Waugh <twaugh@redhat.com> 2.7.7-4
- Reverted udev rules change.
- Ship a HAL FDI file to get correct access control on the USB device
  nodes (bug #251470).
- Make libsane-hpaio requires the main hplip package, needed for
  libhpip.so (bug #280281).

* Thu Aug 30 2007 Tim Waugh <twaugh@redhat.com> 2.7.7-3
- Updated udev rules to allow scanning by console user.

* Wed Aug 29 2007 Tim Waugh <twaugh@redhat.com> 2.7.7-2
- Better buildroot tag.
- More specific license tag.

* Fri Aug  3 2007 Tim Waugh <twaugh@redhat.com> 2.7.7-1
- 2.7.7.

* Mon Jul 23 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-10
- Move libhpmud to hpijs package (bug #248978).

* Fri Jul 20 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-9
- Remove hplip service on upgrade.
- Updated selinux-policy conflict for bug #249014.
- Fixed the udev rules file (bug #248740, bug #249025).

* Tue Jul 17 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-8
- Fixed hp-toolbox desktop file (bug #248560).

* Mon Jul 16 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-7
- Low ink is a warning condition, not an error.

* Wed Jul 11 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-6
- Add hp-check back, but in the gui sub-package.
- Show the HP Toolbox menu entry again.

* Mon Jul  9 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-5
- Read system config when run as root (bug #242974).

* Mon Jul  9 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-4
- Moved reportlab requirement to gui sub-package (bug #189030).
- Patchlevel 1.

* Sat Jul  7 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-3
- Fixed pre scriptlet (bug #247349, bug #247322).

* Fri Jul  6 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-2
- Main package requires python-reportlab for hp-sendfax (bug #189030).
- Explicitly enable scanning.
- Main package requires python-imaging for hp-scan (bug #247210).

* Mon Jul  2 2007 Tim Waugh <twaugh@redhat.com>
- Updated selinux-policy conflict for bug #246257.

* Fri Jun 29 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-1
- 2.7.6.

* Thu Jun 28 2007 Tim Waugh <twaugh@redhat.com> 1.7.4a-3
- Another go at avoiding AVC messages on boot (bug #244205).

* Thu Jun 14 2007 Tim Waugh <twaugh@redhat.com> 1.7.4a-2
- Don't try to write a /root/.hplip.conf file when running as a CUPS
  backend (bug #244205).

* Wed Jun 13 2007 Tim Waugh <twaugh@redhat.com> 1.7.4a-1
- Don't put the version in the desktop file; let desktop-file-install do it.
- 1.7.4a.  No longer need marker-supply or faxing-with-low-supplies
  patches.  Cheetah and cherrypy directories no longer shipped in source
  tarball.

* Mon Jun 11 2007 Tim Waugh <twaugh@redhat.com>
- Don't ship hp-check (bug #243273).
- Moved hp-setup back to the base package, and put code in
  utils.checkPyQtImport() to check for the gui sub-package as well as
  PyQt (bug #243273).

* Fri Jun  8 2007 Tim Waugh <twaugh@redhat.com>
- Moved hp-setup to the ui package (bug #243273).
- Prevent SELinux audit message from the CUPS backends (bug #241776)

* Thu May 10 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-10
- Prevent a traceback when unloading a photo card (bug #238617).

* Fri May  4 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-9
- When faxing, low ink/paper is not a problem (bug #238664).

* Tue Apr 17 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-8
- Update desktop database on %%postun as well (bug #236163).

* Mon Apr 16 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-7
- Some parts can run without GUI support after all (bug #236161).
- Added /sbin/service and /sbin/chkconfig requirements for the scriptlets
  (bug #236445).
- Fixed %%post scriptlet's condrestart logic (bug #236445).

* Fri Apr 13 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-6
- Fixed dangling symlinks (bug #236156).
- Move all fax bits to the gui package (bug #236161).
- Don't ship fax PPD and backend twice (bug #236092).
- Run update-desktop-database in the gui package's %%post scriptlet
  (bug #236163).
- Moved desktop-file-utils requirement to gui package (bug #236163).
- Bumped selinux-policy conflict version (bug #236092).

* Thu Apr  5 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-5
- Better media-empty-error state handling: always set the state.

* Wed Apr  4 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-4
- Clear the media-empty-error printer state.

* Wed Apr  4 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-3
- Fixed typo in marker-supply-low patch.

* Wed Apr  4 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-2
- Split out a gui sub-package (bug #193661).
- Build requires sane-backends-devel (bug #234813).

* Tue Apr  3 2007 Tim Waugh <twaugh@redhat.com>
- Change 'Hidden' to 'NoDisplay' in the desktop file, and use the System
  category instead of Utility (bug #170762).
- Link libsane-hpaio against libsane (bug #234813).

* Fri Mar 30 2007 Tim Waugh <twaugh@redhat.com>
- Use marker-supply-low IPP message.

* Thu Mar  1 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-1
- 1.7.2.

* Wed Feb 14 2007 Tim Waugh <twaugh@redhat.com> 1.7.1-1
- 1.7.1.

* Wed Jan 10 2007 Tim Waugh <twaugh@redhat.com> 1.6.12-1
- 1.6.12.  No longer need broken-conf, loop, out-of-paper or
  sane-debug patches.

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 1.6.10-7
- rebuild against python 2.5

* Wed Dec  6 2006 Tim Waugh <twaugh@redhat.com>
- Minor state fixes for out-of-paper patch.

* Thu Nov 23 2006 Tim Waugh <twaugh@redhat.com> 1.6.10-6
- Report out-of-paper and offline conditions in CUPS backend (bug #216477).

* Wed Nov  1 2006 Tim Waugh <twaugh@redhat.com> 1.6.10-5
- Fixed debugging patch.

* Wed Nov  1 2006 Tim Waugh <twaugh@redhat.com> 1.6.10-4
- Allow debugging of the SANE backend.

* Mon Oct 30 2006 Tim Waugh <twaugh@redhat.com> 1.6.10-3
- IPv6 support (bug #198377).  Local-only sockets are IPv4, and ought
  to be changed to unix domain sockets in future.

* Fri Oct 27 2006 Tim Waugh <twaugh@redhat.com> 1.6.10-2
- 1.6.10.  No longer need compile patch.
- Fixed default config file (bug #211072).
- Moved libhpip to hpijs sub-package (bug #212531).

* Fri Sep 29 2006 Tim Waugh <twaugh@redhat.com> 1.6.7-4
- Don't wake up every half a second (bug #204725).

* Mon Sep 25 2006 Tim Waugh <twaugh@redhat.com>
- Fixed package URL.

* Mon Aug 21 2006 Tim Waugh <twaugh@redhat.com> 1.6.7-3
- Don't look up username in PWDB in the fax backend (removed redundant code).

* Mon Aug  7 2006 Tim Waugh <twaugh@redhat.com> 1.6.7-2
- 1.6.7.
- Conflict with selinux-policy < 2.3.4 to make sure new port numbers are
  known about (bug #201357).

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - (none):1.6.6a-3.1
- rebuild

* Tue Jul  4 2006 Tim Waugh <twaugh@redhat.com> 1.6.6a-3
- libhpip should link against libm (bug #197599).

* Wed Jun 28 2006 Tim Waugh <twaugh@redhat.com> 1.6.6a-2
- 1.6.6a.

* Mon Jun 26 2006 Tim Waugh <twaugh@redhat.com>
- Patchlevel 1.
- Fixed libsane-hpaio %%post scriptlet (bug #196663).

* Fri Jun 16 2006 Tim Waugh <twaugh@redhat.com> 1.6.6-2
- 1.6.6.

* Mon Jun 12 2006 Tim Waugh <twaugh@redhat.com> 0.9.11-6
- Build requires autoconf (bug #194682).

* Fri May 26 2006 Tim Waugh <twaugh@redhat.com> 0.9.11-5
- Include doc files (bug #192790).

* Mon May 15 2006 Tim Waugh <twaugh@redhat.com> 0.9.11-4
- Patchlevel 2.

* Wed May 10 2006 Tim Waugh <twaugh@redhat.com> 0.9.11-3
- Move hpijs to 0.9.11 too.

* Wed May 10 2006 Tim Waugh <twaugh@redhat.com> 0.9.11-2
- 0.9.11.
- Keep hpijs at 0.9.8 for now.

* Fri Apr 21 2006 Tim Waugh <twaugh@redhat.com> 0.9.10-6
- Patchlevel 2.

* Wed Apr 19 2006 Tim Waugh <twaugh@redhat.com>
- Don't package COPYING twice (bug #189162).

* Tue Apr 18 2006 Tim Waugh <twaugh@redhat.com> 0.9.10-5
- Patchlevel 1.
- Fixed another case-sensitive match.
- Require hpijs sub-package (bug #189140).
- Don't package unneeded files (bug #189162).
- Put fax PPD in the right place (bug #186213).

* Tue Apr  4 2006 Tim Waugh <twaugh@redhat.com> 0.9.10-4
- Use case-insensitive matching.  0.9.8 gave all-uppercase in some
  situations.
- Last known working hpijs comes from 0.9.8, so use that.

* Tue Mar 28 2006 Tim Waugh <twaugh@redhat.com> 0.9.10-3
- Always use /usr/lib/cups/backend.

* Tue Mar 28 2006 Tim Waugh <twaugh@redhat.com> 0.9.10-2
- 0.9.10.
- Ship PPDs.

* Fri Mar 24 2006 Tim Waugh <twaugh@redhat.com> 0.9.9-7
- Include hpfax.
- Build requires libusb-devel.

* Thu Mar 23 2006 Tim Waugh <twaugh@redhat.com> 0.9.9-6
- CUPS backend directory is always in /usr/lib.

* Mon Mar 13 2006 Tim Waugh <twaugh@redhat.com> 0.9.9-4
- Quieten hpssd on startup.

* Sat Mar 11 2006 Tim Waugh <twaugh@redhat.com> 0.9.9-3
- Patchlevel 1.

* Thu Mar  9 2006 Tim Waugh <twaugh@redhat.com> 0.9.9-2
- 0.9.9.  No longer need quiet or 0.9.8-4 patches.

* Wed Mar 01 2006 Karsten Hopp <karsten@redhat.de> 0.9.8-6
- Buildrequires: desktop-file-utils

* Mon Feb 27 2006 Tim Waugh <twaugh@redhat.com> 0.9.8-5
- Patchlevel 4.

* Tue Feb 14 2006 Tim Waugh <twaugh@redhat.com> 0.9.8-4
- Added Obsoletes: hpoj tags back in (bug #181476).

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - (none):0.9.8-3.1
- bump again for double-long bug on ppc(64)

* Tue Feb  7 2006 Tim Waugh <twaugh@redhat.com> 0.9.8-3
- Patchlevel 3.

* Fri Feb  3 2006 Tim Waugh <twaugh@redhat.com> 0.9.8-2
- Patchlevel 2.

* Thu Feb  2 2006 Tim Waugh <twaugh@redhat.com> 0.9.8-1
- 0.9.8.
- No longer need initscript patch.
- Don't package hpfax yet.

* Wed Jan 18 2006 Tim Waugh <twaugh@redhat.com> 0.9.7-8
- Don't package PPD files.

* Thu Jan  5 2006 Tim Waugh <twaugh@redhat.com> 0.9.7-7
- Fix initscript (bug #176966).

* Mon Jan  2 2006 Tim Waugh <twaugh@redhat.com> 0.9.7-6
- Rebuild.

* Fri Dec 23 2005 Tim Waugh <twaugh@redhat.com> 0.9.7-5
- Rebuild.

* Wed Dec 21 2005 Tim Waugh <twaugh@redhat.com> 0.9.7-4
- Build requires python-devel, libjpeg-devel (bug #176317).

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Dec  7 2005 Tim Waugh <twaugh@redhat.com> 0.9.7-3
- Use upstream patch 0.9.7-2.
- No longer need lpgetstatus or compile patches.

* Fri Nov 25 2005 Tim Waugh <twaugh@redhat.com> 0.9.7-2
- Prevent LPGETSTATUS overrunning format buffer.

* Thu Nov 24 2005 Tim Waugh <twaugh@redhat.com> 0.9.7-1
- 0.9.7.

* Fri Nov 18 2005 Tim Waugh <twaugh@redhat.com> 0.9.6-7
- Fix compilation.

* Wed Nov  9 2005 Tomas Mraz <tmraz@redhat.com> 0.9.6-6
- rebuilt against new openssl

* Mon Nov  7 2005 Tim Waugh <twaugh@redhat.com> 0.9.6-5
- Rebuilt.

* Wed Oct 26 2005 Tim Waugh <twaugh@redhat.com> 0.9.6-4
- Ship initscript in %%{_sysconfdir}/rc.d/init.d.

* Fri Oct 14 2005 Tim Waugh <twaugh@redhat.com>
- Install the desktop file with Hidden=True (bug #170762).

* Fri Oct 14 2005 Tim Waugh <twaugh@redhat.com> 0.9.6-3
- Don't install desktop file (bug #170762).
- Quieten the hpssd daemon at startup (bug #170762).

* Wed Oct 12 2005 Tim Waugh <twaugh@redhat.com> 0.9.6-2
- 0.9.6.

* Tue Sep 20 2005 Tim Waugh <twaugh@redhat.com> 0.9.5-3
- Apply upstream patch to fix scanning in LaserJets and parallel InkJets.

* Mon Sep 19 2005 Tim Waugh <twaugh@redhat.com> 0.9.5-2
- 0.9.5.
- No longer need condrestart patch.
- Fix compile errors.

* Tue Jul 26 2005 Tim Waugh <twaugh@redhat.com> 0.9.4-3
- Fix condrestart in the initscript.

* Mon Jul 25 2005 Tim Waugh <twaugh@redhat.com> 0.9.4-2
- Use 'condrestart' not 'restart' in %%post scriptlet.

* Fri Jul 22 2005 Tim Waugh <twaugh@redhat.com> 0.9.4-1
- forward-decl patch not needed.
- 0.9.4.

* Fri Jul  1 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-8
- Removed Obsoletes: hpoj tags (bug #162222).

* Thu Jun 30 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-7
- Rebuild to get Python modules precompiled.

* Wed Jun 22 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-6
- For libsane-hpaio ExcludeArch: s390 s390x, because it requires
  sane-backends.

* Wed Jun 15 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-5
- Use static IP ports (for SELinux policy).

* Tue Jun 14 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-4
- Conflicts: hpijs from before this package provided it.
- Conflicts: system-config-printer < 0.6.132 (i.e. before HPLIP support
  was added)

* Thu Jun  9 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-3
- Added Obsoletes: for xojpanel and hpoj-devel (but we don't actually package
  devel files yet).

* Thu Jun  9 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-2
- Add 'hpaio' to SANE config file, not 'hpoj' (bug #159954).

* Thu Jun  9 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-1
- Use /usr/share/applications for putting desktop files in (bug #159932).
- Requires PyQt (bug #159932).

* Tue Jun  7 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-0.1
- Initial package, based on Mandriva spec file.
