Summary:    X client list utility
Name:       xlsclients
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
BuildRequires:  pkgconfig(xcb) >= 1.6

%description
xlsclients lists the names of the clients currently connected to an X server.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%files
%license COPYING
%{_bindir}/xlsclients
%{_mandir}/man1/xlsclients.1*

%changelog
%autochangelog
