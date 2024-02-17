Name:           mmsd-tng
Version:        2.5.0
Release:        %autorelease
Summary:        Multimedia Messaging Service

License:        GPL-2.0-or-later
URL:            https://gitlab.com/kop316/mmsd
Source0:        https://gitlab.com/kop316/mmsd/-/archive/%{version}/mmsd-%{version}.tar.gz

Source1:        mmsd-tng.service

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(mobile-broadband-provider-info)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  cmake(libphonenumber)
BuildRequires:  protobuf-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros

Requires:       pkgconfig(mobile-broadband-provider-info)
Requires:       systemd

%description
mmsd-tng is a lower level daemon that transmits and recieves MMSes. It works with
both the Modem Manager stack.

%prep
%autosetup -p1 -n mmsd-%{version}

%build
%meson -Dbuild-mmsctl=true
%meson_build

%check
%meson_test

%install
%meson_install

mkdir -p %{buildroot}%{_userunitdir}
install -pDm644 %{SOURCE1} %{buildroot}%{_userunitdir}

%preun
%systemd_user_preun mmsd-tng.service

%post
%systemd_user_post mmsd-tng.service

%files
%license COPYING
%doc README
%{_bindir}/mmsdtng
%{_bindir}/mmsctl
%{_userunitdir}/mmsd-tng.service

%changelog
%autochangelog
