Name:           0xFFFF
Version:        0.10
Release:        %autorelease
Summary:        The Open Free Fiasco Firmware Flasher
# Modernized spec file to meet Fedora Rawhide, Fedora 45, and EPEL 10 guidelines
# License available here https://github.com/pali/0xFFFF/blob/master/COPYING
License:        GPL-3.0-only
# Modernized URL to the project's GitHub repository
URL:            https://github.com/pali/0xFFFF
Source:         https://github.com/pali/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
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
# Use SOURCE_DATE_EPOCH for reproducible builds
%make_build -C src BUILD_DATE="$(date '+%b %e %Y' -d @${SOURCE_DATE_EPOCH:?})"

%install
# Use %%{_prefix} macro instead of hardcoded /usr
%make_install PREFIX=%{_prefix}

%check
# Basic check to ensure the binary was built correctly
./src/%{name} -h

%files
%license COPYING
%doc README
# Specific file paths instead of glob to avoid rpmlint warnings
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
