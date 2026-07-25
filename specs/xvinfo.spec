Summary:    X video extension query utility
Name:       xvinfo
Version:    1.1.6
Release:    %autorelease
License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
Source1:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz.sig
Source2:    gpgkey-3AB285232C46AE43D8E192F4DAB0F78EA6E7E2D2.gpg
BuildRequires:  gcc
BuildRequires:  gpgverify
BuildRequires:  meson
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xv)

%description
xvinfo displays information about the XVideo extension on an X server.

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
%doc README.md
%license COPYING
%{_bindir}/xvinfo
%{_mandir}/man1/xvinfo.1*

%changelog
%autochangelog
