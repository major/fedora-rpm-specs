%global pkgname xbitmaps

Summary: X.Org X11 application bitmaps
Name: xorg-x11-%{pkgname}
Version: 1.1.4
Release: %autorelease
License: HPND AND ICU
URL: https://www.x.org
BuildArch: noarch

Source: https://www.x.org/pub/individual/data/xbitmaps-%{version}.tar.xz

BuildRequires: meson

%description
X.Org X11 application bitmaps

%prep
%autosetup -n xbitmaps-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_includedir}/X11
%{_datadir}/pkgconfig/xbitmaps.pc

%changelog
%autochangelog

