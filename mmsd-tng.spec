Name:       mmsd-tng
Version:    1.9
Release:    3%{?dist}
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
BuildRequires:      pkgconfig(libsoup-2.4)
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
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 18 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.9-1
- Update to 1.9

* Thu Feb 03 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.8-1
- Update to 1.8

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 09 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.7-1
- Initial packaging
