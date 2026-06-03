Summary:    X Event utility
Name:       xev
Version:    1.2.7
Release:    %autorelease
License:    MIT
URL:        https://www.x.org

Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr) >= 1.2

Obsoletes: xorg-x11-utils < 7.5-39

%description
xev displays the X11 protocol events sent to a given window.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%doc README.md
%license COPYING
%{_bindir}/xev
%{_mandir}/man1/xev.1*

%changelog
%autochangelog
