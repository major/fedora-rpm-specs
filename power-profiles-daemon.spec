%global forgeurl    https://gitlab.freedesktop.org/upower/%{name}

Version:        0.13
%forgemeta

Name:           power-profiles-daemon
Release:        %autorelease
Summary:        Makes power profiles handling available over D-Bus

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  systemd-rpm-macros

# Test dependencies
BuildRequires:  umockdev
BuildRequires:  python3dist(python-dbusmock)
BuildRequires:  python3dist(pygobject)

%description
%{summary}.

%package docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description docs
This package contains the documentation for %{name}.

%prep
%forgeautosetup

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install
mkdir -p %{buildroot}/%{_localstatedir}/lib/power-profiles-daemon

%check
%meson_test

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%triggerpostun -- power-profiles-daemon < 0.10.1-2
if [ $1 -gt 1 ] && [ -x /usr/bin/systemctl ] ; then
    # Apply power-profiles-daemon.service preset on upgrades to F35 and F36 as
    # the preset was changed to enabled in F35.
    /usr/bin/systemctl --no-reload preset power-profiles-daemon.service || :
fi

%files
%license COPYING
%doc README.md
%{_bindir}/powerprofilesctl
%{_libexecdir}/%{name}
%{_unitdir}/%{name}.service
%{_datadir}/dbus-1/system.d/net.hadess.PowerProfiles.conf
%{_datadir}/dbus-1/system-services/net.hadess.PowerProfiles.service
%{_datadir}/polkit-1/actions/net.hadess.PowerProfiles.policy
%{_localstatedir}/lib/power-profiles-daemon

%files docs
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/%{name}/

%changelog
%autochangelog
