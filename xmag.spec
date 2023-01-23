Name:       xmag
Version:    1.0.7
Release:    4%{?dist}
Summary:    Display a magnified snapshot of an X11 screen
# CutPaste.c:   MIT-open-group
# CutPaste.h:   X11
# man/xmag.man: MIT-open-group
# RootWin.c:    MIT-open-group
# RootWin.h:    MIT-open-group
# RootWinP.h:   MIT-open-group
# Scale.c:      MIT-open-group
# Scale.h:      MIT-open-group
# ScaleP.h:     MIT-open-group
# xmag.c:       MIT-open-group
## Not in any binary package
# aclocal.m4:   FSFULLR AND GPL-2.0-or-later WITH Autoconf-exception-2.0 AND
#               MIT AND GPL-3.0-or-later WITH Autoconf-exception-3.0 and MIT-open-group
# compile:      GPL-2.0-or-later WITH Autoconf-exception-2.0
# config.guess: GPL-3.0-or-later WITH Autoconf-exception-3.0
# config.sub:   GPL-3.0-or-later WITH Autoconf-exception-3.0
# configure:    FSFUL
# configure.ac: MIT-CMU
# COPYING:      MIT-open-group AND MIT
# depcomp:      GPL-2.0-or-later WITH Autoconf-exception-2.0
# INSTALL:      FSFAP
# install-sh:   MIT
# Makefile.am:  MIT-CMU
# Makefile.in:  FSFULLR
# man/Makefile.in:  FSFULLR
# missing:      GPL-2.0-or-later WITH Autoconf-exception-2.0
License:    MIT-open-group AND X11
URL:        https://gitlab.freedesktop.org/xorg/app/xmag
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz.sig
# Retrieved from http://keyserver.ubuntu.com:11371 key server.
Source2:    gpgkey-4A193C06D35E7C670FA4EF0BA2FB9E081F2D130E.gpg
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(x11)
Obsoletes:      xorg-x11-apps < 7.7-31

%description
xmag displays a magnified snapshot of a portion of an X11 screen.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
autoreconf --force --install
%configure --enable-selective-werror --disable-silent-rules --disable-strict-compilation
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README.md Scale.txt
%{_bindir}/xmag
%{_mandir}/man1/xmag.1*
%{_datadir}/X11/app-defaults/Xmag

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jul 25 2022 Petr Pisar <ppisar@redhat.com> - 1.0.7-3
- Migrate a License tag to SPDX

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Petr Pisar <ppisar@redhat.com> - 1.0.7-1
- 1.0.7 bump

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.6-2
- Fix Obsoletes line to actually obsolete the -30 xorg-x11-apps (#1947245)

* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.6-1
- Split xmag out from xorg-x11-apps into a separate package (#1933947)
