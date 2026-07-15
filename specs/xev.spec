Summary:    X Event utility
Name:       xev
Version:    1.2.7
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
BuildRequires:  pkgconfig(xproto) >= 7.0.22
BuildRequires:  pkgconfig(xrandr) >= 1.2

%description
xev displays the X11 protocol events sent to a given window.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
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
%{_bindir}/xev
%{_mandir}/man1/xev.1*

%changelog
%autochangelog
