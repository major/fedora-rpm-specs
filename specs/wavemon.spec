Name:           wavemon
Version:        0.9.7
Release:        %autorelease
Summary:        Ncurses-based monitoring application for wireless network devices

# ISC: nl80211.h
License:        GPL-3.0-or-later AND ISC
URL:            https://github.com/uoaerg/wavemon
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  autoconf
BuildRequires:  automake

%description
wavemon is a wireless device monitoring application that allows you to
watch all important information like device configuration, encryption,
and power management parameters and network information at once.
Adaptive level bar-graphs for link quality, signal/noise strength and
signal-to-noise ratio.  The customizable "level alarm" feature that
notices the user of changes in signal level strength audibly and/or
visually. wavemon is able to list of access points in range and shows
full-screen level histogram displaying signal/noise levels and SNR.

%prep
%autosetup
sed -e '/^CFLAGS=/d' -i configure.ac
sed -r 's|\?=|=|g' -i Makefile.in
autoreconf -fiv

%build
%configure
%make_build

%install
%make_install
# Delete wrong placed doc files (LICENSE and README.md)
rm -rf %{buildroot}%{_datadir}/%{name}/*

%files
%doc README.md
%license LICENSE
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}

%changelog
%autochangelog
