Name:       sessreg
Version:    1.1.4
Release:    %autorelease
Summary:    Utility to manage utmp/wtmp entries for X sessions
License:    MIT AND MIT-open-group 
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-server-utils < 7.7-40

%description
Sessreg is a simple program for managing utmp/wtmp entries for X sessions.
It was originally written for use with xdm, but may also be used with
other display managers such as gdm or kdm.

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
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
