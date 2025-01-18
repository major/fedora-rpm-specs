Name:       appres
Version:    1.0.7
Release:    2%{?dist}
Summary:    X11 utility to print application resources

# SPDX confirmed
License:    MIT-open-group
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes: xorg-x11-resutils < 7.7-9

%description
The appres program prints the resources seen by an application (or
sub-hierarchy of an application) with the specified class and instance
names. It can be used to determine which resources a particular
program will load.

%prep
%autosetup
autoreconf -v --install

%build
%configure --disable-silent-rules --disable-xprint
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 27 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.7-1
- 1.0.7

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 05 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.6-7
- SPDX migration

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr  5 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.6-1
- 1.0.6

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.5-2
- Fix Obsoletes line to actually obsolete the -8 resutils

* Wed Mar 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.5-1
- Split appres out from xorg-x11-resutils into a separate package (#1934344)
