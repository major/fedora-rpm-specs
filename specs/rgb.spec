Name:       rgb
Version:    1.1.1
Release:    %autorelease
Summary:    X color name database

License:    MIT-open-group
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto)

Obsoletes:  xorg-x11-server-utils < 7.7-40

%description
The rgb package provides the X color name database which maps color names
to RGB values. It also includes a utility to display the database.

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
%doc AUTHORS ChangeLog README.md
%{_bindir}/showrgb
%{_datadir}/X11/rgb.txt
%{_mandir}/man1/showrgb.1*

%changelog
%autochangelog
