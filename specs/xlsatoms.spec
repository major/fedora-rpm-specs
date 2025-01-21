Summary:    X11 atom list utility
Name:       xlsatoms
Version:    1.1.4
Release:    6%{?dist}
License:    MIT
URL:        http://www.x.org

Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  libtool

BuildRequires:  pkgconfig(x11)

Obsoletes: xorg-x11-utils < 7.5-39

%description
xlsatoms prints the atom database from an X server.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xlsatoms
%{_mandir}/man1/xlsatoms.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.4-1
- xlsatoms 1.1.4

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.3-1
- xlsatoms 1.1.3

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 16 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.1.2-2
- Add Obsoletes for xorg-x11-utils
- Use make_build and other rpm macros

* Tue Jan 19 2021 Adam Jackson <ajax@redhat.com> - 1.1.2-1
- Initial split packaging (#1918034)
