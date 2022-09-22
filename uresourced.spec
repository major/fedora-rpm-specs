Name:           uresourced
Version:        0.5.3
Release:        %autorelease
Summary:        Dynamically allocate resources to the active user

License:        LGPLv2+
URL:            https://gitlab.freedesktop.org/benzea/uresourced
Source0:        https://gitlab.freedesktop.org/benzea/uresourced/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  git
BuildRequires:  pipewire-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(gio-2.0)

%description
This daemon dynamically assigns a resource allocation to the active
graphical user. If the user has an active graphical session managed
using systemd (e.g. GNOME), then the memory allocation will be used
to protect the sessions core processes (session.slice).

%prep
%autosetup -S git -n %{name}-v%{version}

%build
%meson -Dappmanagement=true
%meson_build

%install
%meson_install

%post
%systemd_post uresourced.service
%systemd_user_post uresourced.service

%preun
%systemd_preun uresourced.service
%systemd_user_preun uresourced.service

%postun
%systemd_postun uresourced.service
%systemd_user_postun uresourced.service

%files
%license COPYING
%doc README
%doc NEWS.md
%config(noreplace) %{_sysconfdir}/uresourced.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.UResourced.conf
%{_libexecdir}/uresourced
%{_libexecdir}/cgroupify
%{_unitdir}/*
%{_userunitdir}/*

%changelog
%autochangelog
