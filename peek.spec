%global uuid    com.uploadedlobster.%{name}

Name:           peek
Version:        1.5.1
Release:        %autorelease
Summary:        Animated GIF screen recorder with an easy to use interface
# The entire source code is GPLv3+ except:
# * MIT:        print-description.py
License:        GPLv3+ and MIT
URL:            https://github.com/phw/peek
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# GNOME Flashback imitates Shell but does not support Screencast
Patch0:         peek-1.5.1-gnome-flashback.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gzip
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python
BuildRequires:  txt2man
BuildRequires:  vala

BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(keybinder-3.0)

Requires:       dbus-common
Requires:       gstreamer1-plugins-good >= 1.2
Requires:       hicolor-icon-theme

# Since F36 ffmpeg-free available in official repos
%if 0%{?fedora} >= 36
Recommends:  ffmpeg-free
%endif
# Available in RPM Fusion
# * https://rpmfusion.org/Configuration
#Recommends:     ffmpeg >= 3
#Recommends:     gstreamer1-plugins-ugly

# TODO: Rust package
#Recommends:     gifski

%description
Peek makes it easy to create short screencasts of a screen area. It was built
for the specific use case of recording screen areas, e.g. for easily showing UI
features of your own apps or for showing a bug in bug reports. With Peek, you
simply place the Peek window over the area you want to record and press
"Record". Peek is optimized for generating animated GIFs, but you can also
directly record to WebM or MP4 if you prefer.

Peek is not a general purpose screencast app with extended features but rather
focuses on the single task of creating small, silent screencasts of an area of
the screen for creating GIF animations or silent WebM or MP4 videos.

Peek runs on X11 or inside a GNOME Shell Wayland session using XWayland. Support
for more Wayland desktops might be added in the future.

Peek requires FFmpeg or running GNOME Shell session. FFmpeg avaliable in RPM
Fusion repo. Enabling the RPM Fusion repositories:

* RPM Fusion
  - https://rpmfusion.org/Configuration
  - https://rpmfusion.org/Howto/Multimedia


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}
# Don't show desktop entry for non-GNOME environment. Works only with:
# * gnome-shell and GNOME session
# * ffpmpeg (RPM Fusion)
# * gstreamer1-plugins-ugly (RPM Fusion)
# - https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/SOUYWF72MZSEH27PBJB6FI5YBR4SXPVT/
# - https://github.com/phw/peek/issues/539
#
# Disable temporary in favour of proper upstream fix
%dnl sed -i  '/Desktop Entry/a OnlyShowIn=GNOME' \
%dnl         %{buildroot}%{_datadir}/applications/%{uuid}.desktop


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/man/man1/*.1*
%{_metainfodir}/*.xml


%changelog
%autochangelog
