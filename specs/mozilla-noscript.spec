# internal macros ???
%global _firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}

# common macros, yet to be defined. see:
# https://fedoraproject.org/wiki/User:Kalev/MozillaExtensionsDraft
%global _moz_extensions %{_datadir}/mozilla/extensions
%global _firefox_extdir %{_moz_extensions}/%{_firefox_app_id}

# needed for this package
%global extension_id \{73a6fe31-595d-460b-a920-fcc0f8843232\}

%global nscl_commit e7716f66443ce4605781dd52cb580e9b6fdaa068

Name:           mozilla-noscript
Version:        12.1.1
Release:        %autorelease
Summary:        JavaScript white list extension for Mozilla Firefox

License:        GPL-3.0-or-later AND MIT AND MPL-2.0 AND CC-BY-SA-3.0
URL:            http://noscript.net/
Source0:        https://github.com/hackademix/noscript/archive/%{version}/noscript-%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=1364409
Source1:        %{name}.metainfo.xml
Source2:        https://github.com/hackademix/nscl/archive/%{nscl_commit}/nscl-%{nscl_commit}.tar.gz
# work offline
# use zip instead of web-ext
Patch0:         %{name}-fedora.patch

BuildRequires:  libappstream-glib
BuildRequires:  nodejs
BuildRequires:  publicsuffix-list
BuildRequires:  zip
Requires:       mozilla-filesystem
# https://github.com/mdmoreau/flextabs MIT
Provides:       bundled(js-flextabs) = 0.2.0
# https://mths.be/he MIT
Provides:       bundled(js-he) = 1.2.0
# https://mths.be/punycode MIT
Provides:       bundled(js-punycode) = 1.4.1
# https://github.com/hackademix/nscl GPLv3+
Provides:       bundled(js-nscl) = 0.0.1
# https://github.com/mozilla/webextension-polyfill MPL
Provides:       bundled(webextension-polyfill) = 0.8.0
Provides:       firefox-noscript = %{version}-%{release}
BuildArch:      noarch

%description
The NoScript extension provides extra protection for Firefox.
It allows JavaScript, Java, Flash and other plug-ins to be executed only by
trusted web sites of your choice (e.g. your online bank) and additionally
provides Anti-XSS protection.

%prep
%setup -q -n noscript-%{version}
tar -xz -C src/nscl --strip-components=1 -f %{S:2}
%patch 0 -p1 -b .f
cp -p src/nscl/COPYING nscl.COPYING
cp -p src/nscl/LICENSE.md nscl.LICENSE.md

%build
export NSCL_TLD_DAT=/usr/share/publicsuffix/public_suffix_list.dat
sh -x ./build.sh

%install
# install into _firefox_extdir
install -Dp -m 644 xpi/noscript-%{version}.xpi %{buildroot}%{_firefox_extdir}/%{extension_id}.xpi

# install MetaInfo file for firefox, etc
install -Dpm644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml

%files
%license LICENSE nscl.COPYING nscl.LICENSE.md src/nscl/lib/{browser-polyfill,punycode}.js.license
%{_firefox_extdir}/%{extension_id}.xpi
# GNOME Software Center metadata
%{_datadir}/metainfo/%{name}.metainfo.xml

%changelog
%autochangelog
