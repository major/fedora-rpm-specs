Name:           xkill
Version:        1.0.7
Release:        %autorelease
Summary:        Utility to force-close an X client's connection

License:        MIT-open-group
URL:            https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:      xorg-x11-server-utils < 7.7-40

%description
xkill is a utility for forcing the X server to close connections to
clients. This program is very dangerous, but is useful for aborting
programs that have displayed undesired windows on a user's screen.

%prep
%autosetup

%build
autoreconf -v --install
%configure --disable-silent-rules
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
