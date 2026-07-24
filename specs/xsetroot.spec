Name:       xsetroot
Version:    1.1.4
Release:    %autorelease
Summary:    Root window parameter setting utility for X
License:    MIT-open-group
URL:        https://www.x.org
Source:     https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  meson >= 1.1.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xbitmaps)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xproto) >= 7.0.25

%description
The xsetroot program allows you to tailor the appearance of the background
window of an X server.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
