%define debug_package %{nil}
Name:           lutris
Version:        0.5.14
Release:        %autorelease
Summary:        Install and play any video game easily

License:        GPLv3
URL:            http://%{name}.net
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3-gobject, python3-wheel, python3-setuptools, python3-gobject
Requires:       python3-dbus, python3-evdev, python3-gobject, python3-PyYAML, cabextract
Requires:       gtk3, psmisc, xorg-x11-server-Xephyr, xrandr
Requires:       hicolor-icon-theme
Requires:       gnome-desktop3
Requires:       python3-distro

%ifarch x86_64
Requires:       mesa-dri-drivers(x86-32)
Requires:       mesa-vulkan-drivers(x86-32)
Requires:       vulkan-loader(x86-32)
Requires:       mesa-libGL(x86-32)
Recommends:     pipewire(x86-32)
Recommends:     libFAudio(x86-32)
Recommends:     wine-pulseaudio(x86-32)
Recommends:     wine-core(x86-32)
%endif

Requires:       mesa-vulkan-drivers
Requires:       mesa-dri-drivers
Requires:       vulkan-loader
Requires:       mesa-libGL
Requires:       python3-requests
Requires:       python3-pillow
Requires:       glx-utils
Requires:       gvfs
Requires:       webkit2gtk4.1
Requires:       python3-lxml
Recommends: 	p7zip, curl
Recommends:	fluid-soundfont-gs
Recommends:     wine-core
Recommends:	p7zip-plugins
Recommends:	gamemode
Recommends:     libFAudio
Recommends:     gamescope
BuildRequires:  fdupes
BuildRequires:  libappstream-glib
BuildRequires:  meson, gettext

%description
Lutris is a gaming platform for GNU/Linux. Its goal is to make
gaming on Linux as easy as possible by taking care of installing
and setting up the game for the user. The only thing you have to
do is play the game. It aims to support every game that is playable
on Linux.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%py3_build
%meson
%meson_build

%install
%py3_install
%meson_install
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/net.%{name}.Lutris.metainfo.xml
%fdupes %{buildroot}%{python3_sitelib}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications share/applications/net.%{name}.Lutris.desktop

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/net.%{name}.Lutris.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/man/man1/%{name}.1.gz
%{python3_sitelib}/%{name}-*.egg-info
%{python3_sitelib}/%{name}/
%{_datadir}/metainfo/
%{_datadir}/locale/

%changelog
%autochangelog
