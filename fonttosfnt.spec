Name:       fonttosfnt
Version:    1.2.3
Release:    1%{?dist}
Summary:    Tool to wrap bdf or pcf bitmap fonts in an sfnt wrapper

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  gcc make libtool
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Conflicts:  xorg-x11-font-utils < 7.5-51

%description
fonttosfnt wraps a set of bdf or pcf bitmap fonts in a sfnt (TrueType or
OpenType) wrapper.

%prep
%autosetup

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/fonttosfnt
%{_mandir}/man1/fonttosfnt.1*

%changelog
* Fri Oct 13 2023 Peter Hutterer <peter.hutterer@redhat.com> - 1.2.3-1
- fonttosfnt 1.2.3

* Mon Aug 21 2023 Parag Nemade <pnemade AT fedoraproject DOT org> - 1.2.2-7
- Mark this as SPDX license expression converted

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.2.2-1
- fonttosfnt 1.2.2

* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.2.1-2
- Fix the Conflicts line to properly conflict with the -50 font-utils,
  without a {?dist} <= doesn't work as expected.

* Thu Feb 25 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.2.1-1
- Split fonttosfnt out from xorg-x11-font-utils into its own
  package (#1932737)
