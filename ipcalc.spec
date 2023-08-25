Name: ipcalc
Version: 1.0.3
Release: %autorelease
Summary: IP network address calculator
License: GPL-2.0-or-later
URL: https://gitlab.com/ipcalc/ipcalc
Source0: https://gitlab.com/ipcalc/ipcalc/-/archive/%{version}/ipcalc-%{version}.tar.gz

BuildRequires: gcc, libmaxminddb-devel, meson, rubygem-ronn-ng
Recommends:    libmaxminddb, geolite2-city, geolite2-country

# Explicitly conflict with older initscript packages that ship ipcalc
Conflicts: initscripts < 9.63
# Obsolete ipcalculator
Obsoletes:  ipcalculator < 0.41-20


%description
ipcalc provides a simple way to calculate IP information for a host
or network. Depending on the options specified, it may be used to provide
IP network information in human readable format, in a format suitable for
parsing in scripts, generate random private addresses, resolve an IP address,
or check the validity of an address.

%prep
%autosetup

%build
%meson -Duse_maxminddb=enabled -Duse_runtime_linking=enabled
%meson_build

%install
%meson_install

%check
%meson_test

%files

%{_bindir}/ipcalc
%license COPYING
%doc README.md
%{_mandir}/man1/ipcalc.1*

%changelog
%autochangelog
