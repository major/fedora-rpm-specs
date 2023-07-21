Summary:       X11 utility to view and edit application resources
Name:          editres
Version:       1.0.8
Release:       2%{?dist}
License:       MIT
URL:           https://www.x.org
Source0:       https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Patch01:       editres-1.0.6-format-security.patch
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xaw7)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(xorg-macros) >= 1.8
BuildRequires: pkgconfig(xt)
Obsoletes:     xorg-x11-resutils < 7.7-9
%description
editres is a tool that allows users and application developers to view
the full widget hierarchy of any Xt Toolkit application that speaks the
Editres protocol  In addition, editres will help the user construct
resource specifications, allow the user to apply the resource to
the application and view the results dynamically.

%prep
%autosetup

%build
%configure --disable-silent-rules --disable-xprint
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/X11/app-defaults/Editres
%{_datadir}/X11/app-defaults/Editres-color

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 04 2023 Terje Rosten <terje.rosten@ntnu.no> - 1.0.8-1
- 1.0.8
- No need for autoreconf any longer

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.7-2
- Fix Obsoletes line to actually obsolete the -8 resutils

* Wed Mar 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.7-1
- Split editres out from xorg-x11-resutils into a separate package (#1934345)
