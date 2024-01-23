Name:       mmsd-tng
Version:    2.2.0
Release:    4%{?dist}
Summary:    Multimedia Messaging Service

License:    GPLv2
URL:        https://gitlab.com/kop316/mmsd/
Source0:    https://gitlab.com/kop316/mmsd/-/archive/%{version}/mmsd-%{version}.tar.gz

Source1:    mmsd-tng.service

Requires:           pkgconfig(mobile-broadband-provider-info)
Requires:           systemd
BuildRequires:      pkgconfig(mobile-broadband-provider-info)
BuildRequires:      gcc
BuildRequires:      gcc-c++
BuildRequires:      meson
BuildRequires:      protobuf-devel
BuildRequires:      dbus-c++-devel
BuildRequires:      libphonenumber-devel
BuildRequires:      c-ares-devel
BuildRequires:      pkgconfig(mm-glib)
BuildRequires:      pkgconfig(gobject-2.0)
BuildRequires:      pkgconfig(glib-2.0)
BuildRequires:      pkgconfig(libsoup-3.0)
BuildRequires:      systemd-devel
BuildRequires:      systemd-rpm-macros

%description
mmsd is a lower level daemon that transmits and recieves MMSes. It works with
both the ofono stack and the Modem Manager stack.

Please note that mmsd alone will not get MMS working! It is designed to work 
with a higher level chat application to facilitate fetching and 
sending MMS. It interfaces with other applications via the dbus.

%prep
%autosetup -p1 -n mmsd-%{version}

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

mkdir -p %{buildroot}%{_userunitdir}
cp %{SOURCE1} %{buildroot}%{_userunitdir}

%preun
%systemd_user_preun mmsd-tng.service

%post
%systemd_user_post mmsd-tng.service


%files
%{_bindir}/mmsdtng
%{_userunitdir}/mmsd-tng.service
%doc README
%license COPYING

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

%autochangelog
