
Name:           scamp
Version:        2.13.1
Release:        %autorelease
Summary:        compute astrometric and photometric solutions from sextractor catalogs

License:        GPL-3.0-only
URL:            http://www.astromatic.net/software/scamp
Source0:        https://github.com/astromatic/scamp/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: wrong-pointer-i386.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  cdsclient
BuildRequires:  curl-devel
BuildRequires:  fftw-devel
BuildRequires:  libtool
BuildRequires:  openblas-devel
BuildRequires:  pkgconfig
BuildRequires:  plplot-devel

Requires:       cdsclient

%description
SCAMP is a program that computes astrometric and photometric solutions from
SExtractor catalogs

%prep
%autosetup  -p1


%build
sh autogen.sh
%configure --enable-openblas \
  --enable-plplot
%make_build


%install
%make_install


%files
%license COPYRIGHT LICENSE
%doc AUTHORS ChangeLog HISTORY README.md THANKS
%{_bindir}/scamp
%{_datadir}/scamp/
%{_mandir}/*/scamp.*.gz


%changelog
%autochangelog
