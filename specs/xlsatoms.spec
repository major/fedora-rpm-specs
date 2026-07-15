Summary:    X11 atom list utility
Name:       xlsatoms
Version:    1.1.5
Release:    %autorelease
License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(xcb)

%description
xlsatoms prints the atom database from an X server.

%prep
%autosetup
%meson

%build
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_bindir}/xlsatoms
%{_mandir}/man1/xlsatoms.1*

%changelog
%autochangelog
