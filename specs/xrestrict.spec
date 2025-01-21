%global commit          35a944a6e739d5b3462ee79ffc0c527b6e5753d1
%global snapshotdate    20160730
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Summary: A utility to modify the "Coordinate Transformation Matrix" of an XInput2 device
Name: xrestrict
Version: 0.8.0
Release: 10.%{snapshotdate}git%{shortcommit}%{?dist}
URL: https://github.com/Ademan/xrestrict
Source0: %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
License: MIT
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig(inputproto)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xrandr)

%description
A utility to modify the "Coordinate Transformation Matrix" of an XInput2 device.

The typical application is restricting graphical tablet drawing area to a single
monitor in multi-monitor set-ups.

%prep
%setup -q -n %{name}-%{commit}
autoreconf -fiv

%build
%configure
%make_build

%install
%make_install

%check
src/rectest

%files
%doc README.md
%license COPYING
%exclude %{_bindir}/rectest
%{_bindir}/xrestrict

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-10.20160730git35a944a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-9.20160730git35a944a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-8.20160730git35a944a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7.20160730git35a944a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6.20160730git35a944a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5.20160730git35a944a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4.20160730git35a944a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3.20160730git35a944a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 13 2021 Dominik Mierzejewski <rpm@greysector.net> 0.8.0-2.20160730git35a944a
- package latest snapshot directly

* Fri Mar 19 2021 Dominik Mierzejewski <rpm@greysector.net> 0.8.0-1.20160730git35a944a
- initial build
