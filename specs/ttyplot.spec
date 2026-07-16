Name: ttyplot
Summary: Real-time plotting utility for the terminal
License: Apache-2.0

Version: 1.7.6
Release: 1%{?dist}

URL: https://github.com/tenox7/ttyplot/
Source0: %{URL}archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make

BuildRequires: aalib-devel
BuildRequires: pkgconfig(ncursesw)


%description
%{name} is a realtime plotting utility for text mode consoles and terminals
with data input from stdin / pipe.


%prep
%autosetup


%build
%make_build AA=1


%install
%make_install PREFIX=%{_prefix} MANPREFIX=%{_mandir}


%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Jul 14 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.7.6-1
- Update to v1.7.6 (with aalib support)

* Mon Jun 22 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.7.5-1
- Update to v1.7.5

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Aug 18 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.7.4-1
- Update to v1.7.4

* Sun Aug 03 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.7.3-1
- Update to v1.7.3

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 16 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.7.2-1
- Update to v1.7.2

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 30 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.7.0-1
- Initial packaging
