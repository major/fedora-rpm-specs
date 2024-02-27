%global forgeurl https://github.com/ZerBea/%{name}
%global tag %{version}

Name:           hcxtools
Version:        6.3.4
%forgemeta
Release:        %autorelease
Summary:        Portable solution for conversion WiFi dump files to hashcat formats

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-5920CE1C567948AFD2C0A9B7375516A45DB88630.gpg

BuildRequires:  gcc >= 11
BuildRequires:  gnupg2
BuildRequires:  make

# Use hard-coded package name instead of pkg-config for now due fedora-review
# issue
# https://bugzilla.redhat.com/show_bug.cgi?id=2118906#c8
BuildRequires:  libcurl-devel
BuildRequires:  libpcap-devel
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
# BuildRequires:  pkgconfig(libcurl)
# BuildRequires:  pkgconfig(libpcap)
# BuildRequires:  pkgconfig(openssl)
# BuildRequires:  pkgconfig(zlib)

%description
Small set of tools convert packets from captures (h = hash, c = capture,
convert and calculate candidates, x = different hashtypes) for the use with
latest hashcat or John the Ripper. The tools are 100% compatible to hashcat
and John the Ripper and recommended by hashcat. This branch is pretty closely
synced to hashcat git and John the Ripper git.

Support of hashcat hash-modes: 4800, 5500, 2200x, 16100, 250x (deprecated),
1680x (deprecated)

Support of John the Ripper hash-modes: WPAPSK-PMK, PBKDF2-HMAC-SHA1, chap,
netntlm, tacacs-plus

Support of gzip (.gz) single file compression.

Main purpose is to detect weak points within own WiFi networks by analyzing
the hashes. Therefore convert the dump file to WPA-PBKDF2-PMKID+EAPOL hash
file and check if wlan-key or plainmasterkey was transmitted unencrypted. Or
upload the "uncleaned" dump file (pcapng, pcap, cap) here
https://wpa-sec.stanev.org/?submit to find out if your ap or the client is
vulnerable by using common wordlists or a weak password generation algorithm.


%prep
%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%forgeautosetup -p1

# rpmlint
# E: env-script-interpreter 
sed -e 's|/usr/bin/env python3|/usr/bin/python3|' -i usefulscripts/hcxgrep.py

# Obsolete and - no longer under maintenance - will be removed, when OpenSSL
# switching to version 3.0.0
# https://github.com/ZerBea/hcxtools#detailed-description
sed -e /hcxmactool/d \
    -e /hcxpmkidtool/d \
    -e /hcxessidtool/d \
    -e /hcxhashcattool/d \
    -i Makefile


%build
%set_build_flags
%make_build


%install
%make_install

# Install man page
install -Dpm 0644 man/%{name}.1 -t %{buildroot}%{_mandir}/man1/


%files
%license license.txt
%doc README.md changelog
# Useful scripts
# https://github.com/ZerBea/hcxtools#useful-scripts
# piwritecard: Example script to restore SD-Card
# piwreadcard: Example script to backup SD-Card
# hcxgrep.py:  Extract records from m22000 hashline/hccapx/pmkid file based on
# regexp
%doc usefulscripts/
%{_bindir}/hcxeiutool
%{_bindir}/hcxhash2cap
%{_bindir}/hcxhashtool
%{_bindir}/hcxpcapngtool
%{_bindir}/hcxpmktool
%{_bindir}/hcxpsktool
%{_bindir}/hcxwltool
%{_bindir}/whoismac
%{_bindir}/wlancap2wpasec
%{_mandir}/man1/*.1*


%changelog
%autochangelog
