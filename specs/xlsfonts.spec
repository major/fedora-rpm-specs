Summary:    X font list utility
Name:       xlsfonts
Version:    1.0.9
Release:    %autorelease
License:    MIT
URL:        https://www.x.org
Source:     https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xproto)

%description
xlsfonts lists the fonts available on an X server.

%prep
%autosetup -p1

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
%{_bindir}/xlsfonts
%{_mandir}/man1/xlsfonts.1*

%changelog
%autochangelog
