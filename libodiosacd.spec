%global forgeurl https://github.com/tari01/libodiosacd

Name:           libodiosacd
Version:        23.8.1
Release:        %autorelease
Summary:        SACD decoder shared library

License:        GPL-3.0-or-later
URL:            https://tari.in/www/software/libodiosacd/
Source:         %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description
The Odio SACD shared library is a decoding engine which takes a Super Audio CD
source and extracts a 24-bit high resolution wave file. It handles both DST and
DSD streams.

The library reads the following input:
- SACD image files (*.iso)
- Sony DSF files (*.dsf)
- Philips DSDIFF files (*.dff)

Supported output sample rates:
- 88.2kHz
- 176.4kHz

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup
chmod -x COPYING
sed -i Makefile \
  -e 's/CC =/CC ?=/' \
  -e 's/CFLAGS = -g -O$O/CFLAGS +=/' \
  -e 's/LIBDIR = lib/LIBDIR = %{_lib}/'

%build
%set_build_flags
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.1*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so

%changelog
%autochangelog
