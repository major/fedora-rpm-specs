Name:       xrandr
Version:    1.5.3
Release:    %autorelease
Summary:    Commandline utility to change output properties

License:    HPND-sell-variant
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
%autochangelog
