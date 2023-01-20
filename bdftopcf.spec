Name:       bdftopcf
Version:    1.1
Release:    6%{?dist}
Summary:    Font compiler for the X server and font server

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  gcc make libtool
BuildRequires:  pkgconfig(x11) pkgconfig(fontsproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Conflicts:  xorg-x11-font-utils < 7.5-51

%description
bdftopcf is a font compiler for the X server and font server.  Fonts
in Portable Compiled Format can be read by any architecture, although
the file is structured to allow one particular architecture to read
them directly without reformatting.  This allows fast reading on the
appropriate machine, but the files are still portable (but read more
slowly) on other machines.

%prep
%autosetup

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/bdftopcf
%{_mandir}/man1/bdftopcf.1*

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.1-2
- Fix the Conflicts line to properly conflict with the -50 font-utils,
  without a {?dist} <= doesn't work as expected.

* Thu Feb 25 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.1-1
- Split bdftopcf out from xorg-x11-font-utils into its own
  package (#1932736)
