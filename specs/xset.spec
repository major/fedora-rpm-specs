Name:       xset
Version:    1.2.6
Release:    %autorelease
Summary:    User preference utility for X
License:    MIT-open-group
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xproto) >= 7.0.17

%description
This program is used to set various user preference options of the X server,
including bell volume, DPMS features, font paths and some settings related
to the pointer.

%prep
%autosetup

%build
%meson -Dxf86misc=disabled -Dfontcache=disabled
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
