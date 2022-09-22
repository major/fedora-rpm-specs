Name:       xclock
Version:    1.1.1
Release:    2%{?dist}
Summary:    The classic X Window System clock utility

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps < 7.7-31

%description
xclock is the classic X Window System clock utility. It displays
the time in analog or digital form, continuously updated at a
frequency which may be specified by the user.

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
%{_bindir}/xclock
%{_mandir}/man1/xclock.1*
%{_datadir}/X11/app-defaults/XClock
%{_datadir}/X11/app-defaults/XClock-color

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 08 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.1.1-1
- New upstream release 1.1.1 (rhbz#2071460)

* Tue Apr 05 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 1.1.0-1
- New upstream release 1.1.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.9-2
- Fix Obsoletes line to actually obsolete the -30 xorg-x11-apps (#1947245)

* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.9-1
- Split xclock out from xorg-x11-apps into a separate package (#1933940)
