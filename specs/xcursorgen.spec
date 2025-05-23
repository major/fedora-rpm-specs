Name:       xcursorgen
Version:    1.0.9
Release:    %autorelease
Summary:    Prepare X11 cursor sets for use with libXcursor

License:    HPND-sell-variant
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  automake libtool
BuildRequires:  gcc make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

Obsoletes:  xorg-x11-apps < 7.7-31

%description
xcursorgen prepares X11 cursor sets for use with libXcursor.

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
