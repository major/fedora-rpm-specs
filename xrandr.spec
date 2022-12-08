Name:       xrandr
Version:    1.5.2
Release:    1%{?dist}
Summary:    Commandline utility to change output properties

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-server-utils < 7.7-40

%description
xrandr is a commandline utility to set the size, orientation and/or
reflection of the outputs for an X screen. It can also set the screen size
and turn outputs on and off..

%prep
%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

# "needs more nickle bindings" since 2009...
rm -f $RPM_BUILD_ROOT%{_bindir}/xkeystone

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Dec 06 2022 Peter Hutterer <peter.hutterer@redhat.com> - 1.5.2-1
- xrandr 1.5.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 08 2021 Peter Hutterer <peter.hutterer@redhat.com> - 1.5.1-2
- Fix Obsoletes line to actually obsolete the -39 server-utils (#1932754)

* Wed Mar 03 2021 Peter Hutterer <peter.hutterer@redhat.com> 1.5.1-1
- Split xrandr out from xorg-x11-server-utils into a separate package
  (#1934391)

