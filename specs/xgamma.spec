Name:       xgamma
Version:    1.0.7
Release:    5%{?dist}
Summary:    X utility to query and alter the gamma correction of a monitor
# COPYING:      X11 AND HPND-sell-variant
# man/xgamma.man:   X11 without the permision grant, probably a copy-and-paste
#                   mistake
#                   <https://gitlab.freedesktop.org/xorg/app/xgamma/-/issues/2>
# xgamma.c:     X11
## Not in any binary package
# configure.ac: HPND-sell-variant
# INSTALL:      FSFAP
# Makefile.am:  HPND-sell-variant
## Unbundled
# aclocal.m4:   FSFULLRWD AND FSFULLR AND
#               GPL-2.0-or-later WITH Autoconf-exception-generic AND
#               GPL-3.0-or-later WITH Autoconf-exception-macro AND X11
# compile:      GPL-2.0-ro-later WITH Autoconf-exception-generic
# config.guess: GPL-3.0-or-later WITH Autoconf-exception-generic
# config.sub:   GPL-3.0-or-later WITH Autoconf-exception-generic
# configure:    FSFUL
# depcomp:      GPL-2.0-or-later WITH Autoconf-exception-generic
# install-sh:   X11 AND LicenseRef-Fedora-Public-Domain
# Makefile.in:  FSFULLRWD AND HPND-sell-variant
# man/Makefile.in:  FSFULLRWD
# missing:      GPL-2.0-or-later WITH Autoconf-exception-generic
License:    X11 AND HPND-sell-variant
URL:        https://www.x.org/
Source0:    %{url}releases/individual/app/%{name}-%{version}.tar.xz
Source1:    %{url}releases/individual/app/%{name}-%{version}.tar.xz.sig
# Key exported from Petr Pisar's keyring
Source2:    gpgkey-4A193C06D35E7C670FA4EF0BA2FB9E081F2D130E.gpg
BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
# xorg-x11-server-utils-7.7-39.fc35 splitted into many packages
Obsoletes:      xorg-x11-server-utils < 7.7-40

%description
xgamma allows X users to query and alter the gamma correction of a
monitor via the X video mode extension (XFree86-VidModeExtension).

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup
rm aclocal.m4 compile config.guess config.sub configure depcomp install-sh \
     Makefile.in man/Makefile.in missing

%build
autoreconf -v --force --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Petr Pisar <ppisar@redhat.com> - 1.0.7-1
- 1.0.7 bump

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.6-2
- Fix Obsoletes line to actually obsolete the -39 server-utils (#1932754)

* Wed Mar 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.6-1
- Split xgamma out from xorg-x11-server-utils into a separate package
  (#1934385)

