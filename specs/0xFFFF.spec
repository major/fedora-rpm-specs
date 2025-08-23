Name:           0xFFFF
Version:        0.10
Release:        %autorelease
Summary:        The Open Free Fiasco Firmware Flasher
# License available here https://github.com/pali/0xFFFF/blob/master/COPYING
License:        GPL-3.0-only
URL:            https://talk.maemo.org/showthread.php?t=87996
Source0:        https://github.com/pali/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  make

%description
The 'Open Free Fiasco Firmware Flasher' aka 0xFFFF utility implements
a free (GPL3) userspace handler for the NOLO bootloader and related
utilities for the Nokia Internet Tablets like flashing setting device
options, packing/unpacking FIASCO firmware format and more.

%prep
%autosetup

%build
%make_build -C src BUILD_DATE="$(date '+%b %e %Y' -d @${SOURCE_DATE_EPOCH:?})"

%install
%make_install PREFIX=/usr

%files
%doc README INSTALL
%license COPYING
%{_bindir}/*
%{_mandir}/man1/0xFFFF.1*

%changelog
%autochangelog
