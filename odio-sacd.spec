%global forgeurl https://github.com/tari01/odio-sacd

Name:           odio-sacd
Version:        23.1.31
Release:        %autorelease
Summary:        Command-line SACD decoder

License:        GPL-3.0-or-later
URL:            https://tari.in/www/software/odio-sacd/
Source:         %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

BuildRequires:  libodiosacd-devel

%description
Odio SACD is a command-line application which takes a Super Audio CD source and
extracts a 24-bit high resolution wave file. It handles both DST and DSD
streams.

The application reads the following input:
- SACD image files (*.iso)
- Sony DSF files (*.dsf)
- Philips DSDIFF files (*.dff)

Supported output sample rates:
- 88.2kHz
- 176.4kHz

%prep
%autosetup
chmod -x COPYING
sed -i Makefile \
  -e 's/CC =/CC ?=/' \
  -e 's/CFLAGS = -g -O$O/CFLAGS +=/'

%build
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
