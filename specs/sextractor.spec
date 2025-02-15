Name: sextractor
Version: 2.28.2
Release: %autorelease
Summary: Extract catalogs of sources from astronomical images

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: http://astromatic.iap.fr/software/%{name}
Source0: https://github.com/astromatic/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: sextractor-format-sec.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: automake autoconf libtool
BuildRequires: fftw-devel >= 3.1
BuildRequires: openblas-devel
BuildRequires: cfitsio-devel

%description
SExtractor is a program that builds a catalogue of objects from an 
astronomical image. Although it is particularly oriented towards 
reduction of large scale galaxy-survey data, it performs rather 
well on moderately crowded star fields.

%prep
%setup -q
%patch -P0 -p1
sh ./autogen.sh

%build
%configure --enable-openblas
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 644 -p config/*.conv %{buildroot}%{_datadir}/%{name}
install -m 644 -p config/default.nnw %{buildroot}%{_datadir}/%{name}

%files
%doc AUTHORS BUGS COPYRIGHT HISTORY README.md THANKS config/default.sex config/default.param config/README
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/manx/*
%{_datadir}/%{name}/

%changelog
%autochangelog
