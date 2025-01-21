Name:       x11perf
Version:    1.6.1
Release:    11%{?dist}
Summary:    X11 server performance test program

License:    SMLNJ AND HPND
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

# We keep our scripts in $datadir, not $libdir, because ... history?
Patch01:    x11perf-1.6.0-x11perf-datadir-cleanups.patch

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps < 7.7-31

%description
The x11perf program runs one or more performance tests and reports how fast
an X server can execute the tests.

%prep
%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/x11perf
%{_bindir}/x11perfcomp
%{_mandir}/man1/x11perf.1*
%{_mandir}/man1/x11perfcomp.1*
%{_mandir}/man1/Xmark.1*
%{_datadir}/X11/x11perfcomp

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 28 2023 Peter Hutterer <peter.hutterer@redhat.com> - 1.6.1-8
- SPDX migration

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.6.1-2
- Fix Obsoletes line to actually obsolete the -30 xorg-x11-apps (#1947245)

* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.6.1-1
- Split x11perf out from xorg-x11-apps into a separate package (#1933936)
