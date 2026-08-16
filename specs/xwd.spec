Name:       xwd
Version:    1.0.10
Release:    %autorelease
Summary:    Dump an X window to file

%global forgeurl https://gitlab.freedesktop.org/xorg/app/xwd
%global tag %{name}-%{version}
%forgemeta

License:    MIT-open-group AND HPND-sell-variant
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz.sig
Source2:    gpgkey-3AB285232C46AE43D8E192F4DAB0F78EA6E7E2D2.gpg

BuildRequires:  gcc
BuildRequires:  gpgverify
BuildRequires:  meson
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xproto) >= 7.0.25

%description
Xwd is an X Window System window dumping utility. Xwd allows X users to
store window images in a specially formatted dump file. This file can then
be read by various other X utilities for redisplay, printing, editing,
formatting, archiving, image processing, etc.

%prep
%gpgverify -k 2 -s 1 -d 0
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
