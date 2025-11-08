Name:           switcheroo-control
Version:        3.0
Release:        %autorelease
Summary:        D-Bus service to check the availability of dual-GPU

License:        GPL-3.0-only
URL:            https://gitlab.freedesktop.org/hadess/switcheroo-control/
# URL from https://gitlab.freedesktop.org/hadess/switcheroo-control/-/releases
Source0:        https://gitlab.freedesktop.org/hadess/switcheroo-control/-/releases/3.0/downloads/switcheroo-control-3.0.tar.xz

BuildRequires:  gcc
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  systemd
BuildRequires:  libdrm-devel
BuildRequires:  kernel-headers
BuildRequires:  python3-dbusmock
BuildRequires:  umockdev

%{?systemd_requires}

%description
D-Bus service to check the availability of dual-GPU.

%package docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description docs

This package contains the documentation for %{name}.

%prep
%autosetup


%build
%meson -Dgtk_doc=true
%meson_build


%install
%meson_install

%post
if [ $1 -eq 2 ] && [ -x /usr/bin/systemctl ] ; then
    /usr/bin/systemctl daemon-reload
fi
%systemd_post switcheroo-control.service
%udev_hwdb_update
%udev_rules_update

%preun
%systemd_preun switcheroo-control.service

%postun
%systemd_postun_with_restart switcheroo-control.service
%udev_hwdb_update
%udev_rules_update

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/switcherooctl
%{_datadir}/dbus-1/system.d/net.hadess.SwitcherooControl.conf
%{_unitdir}/switcheroo-control.service
%{_libexecdir}/switcheroo-control
%{_libexecdir}/switcheroo-control-check-discrete-amdgpu
%{_libexecdir}/switcheroo-control-check-discrete-nouveau
%{_libexecdir}/switcheroo-control-check-discrete-xe
%{_udevhwdbdir}/30-pci-intel-gpu.hwdb
%{_udevrulesdir}/30-discrete-gpu.rules
%{_mandir}/man1/switcherooctl.1*

%files docs
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/%{name}/

%changelog
%autochangelog
