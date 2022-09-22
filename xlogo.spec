Name:       xlogo
Version:    1.0.5
Release:    4%{?dist}
Summary:    Display the X11 logo

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps < 7.7-31

%description
xlogo displays a magnified snapshot of a portion of an X11 screen.

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
%{_bindir}/xlogo
%{_mandir}/man1/xlogo.1*
%{_datadir}/X11/app-defaults/XLogo
%{_datadir}/X11/app-defaults/XLogo-color

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 06 2021 David Cantrell <dcantrell@redhat.com> - 1.0.5-1
- Upgrade to xlogo-1.0.5 (#1957538)

* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.0.4-2
- Fix Obsoletes line to actually obsolete the -30 xorg-x11-apps (#1947245)

* Tue Mar 02 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.0.4-1
- Split xlogo out from xorg-x11-apps into a separate package (#1933949)
