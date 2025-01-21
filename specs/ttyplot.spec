Name: ttyplot
Summary: Real-time plotting utility for the terminal
License: Apache-2.0

Version: 1.7.0
Release: 2%{?dist}

URL: https://github.com/tenox7/ttyplot/
Source0: %{URL}archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig(ncursesw)


%description
%{name} is a realtime plotting utility for text mode consoles and terminals
with data input from stdin / pipe.


%prep
%autosetup


%build
%make_build


%install
%make_install PREFIX=%{_prefix} MANPREFIX=%{_mandir}


%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 30 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.7.0-1
- Initial packaging
