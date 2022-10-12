%global uuid org.gabmus.%{name}

Name:           hydrapaper
Version:        3.3.1
Release:        %autorelease
Epoch:          1
Summary:        Set two different backgrounds for each monitor on GNOME

License:        GPLv3+
URL:            https://gitlab.com/gabmus/HydraPaper
Source0:        %{url}/-/archive/%{version}/HydraPaper-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.58.0
BuildRequires:  pandoc
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.3.1
BuildRequires:  pkgconfig(libadwaita-1) >= 1.0.0

Requires:       dbus-common
Requires:       glib2
Requires:       gtk4 >= 4.3.1
Requires:       hicolor-icon-theme
Requires:       libadwaita >= 1.0.0
Requires:       python3-dbus
Requires:       python3-pillow

%description
GTK utility to set two different backgrounds for each monitor on GNOME (which
lacks this feature).

Wallpaper manager with multimonitor support.

HydraPaper officially supports the following desktop environments:

  - GNOME 3
  - MATE
  - Cinnamon
  - Budgie

Experimental support for the sway window manager/Wayland compositor is also
present.


%prep
%autosetup -n HydraPaper-%{version} -p1


%build
%meson \
%if 0%{?flatpak}
  -Denabledaemon=false
%endif

%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%if !0%{?flatpak}
%post
%systemd_user_post %{uuid}d.service

%preun
%systemd_user_preun %{uuid}d.service

%postun
%systemd_user_postun_with_restart %{uuid}d.service
%endif


%files -f %{name}.lang
%license COPYING LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%if !0%{?flatpak}
%{_libexecdir}/%{name}d
%endif
%{_mandir}/man1/*.1*
%{_metainfodir}/*.xml
%if !0%{?flatpak}
%{_userunitdir}/*.service
%endif
%{python3_sitelib}/%{name}/


%changelog
%autochangelog
