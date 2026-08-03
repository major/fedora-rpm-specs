# VCS   https://gitlab.xfce.org/apps/parole

%global fullname org.xfce.Parole
%global xfceversion  4.20
%global minorversion 4.20

Name:           parole
Version:        4.20.0
Release:        %autorelease
Summary:        Media player for the Xfce desktop
License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/apps/parole/start
Source0:        https://archive.xfce.org/src/apps/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

BuildRequires:  dbus-devel >= 0.60
BuildRequires:  dbus-glib-devel >= 0.70
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel >= 2.38.0
BuildRequires:  gstreamer1-plugins-base-devel >= 1.0.0
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel >= 3.22.0
BuildRequires:  libappstream-glib
BuildRequires:  libnotify-devel >= 0.7.8
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxfce4util-devel >= %{xfceversion}
BuildRequires:  meson
BuildRequires:  taglib-devel >= 1.4
BuildRequires:  xfconf-devel >= %{xfceversion}
Requires:       gstreamer1-plugins-good

%description
Parole is a modern simple media player based on the GStreamer framework and 
written to fit well in the Xfce desktop. Parole features playback of local 
media files, DVD/CD and live streams. Parole is extensible via plugins.

The project still in its early developments stage, but already contains the 
following features:
* Audio playback
* Video playback with optional subtitle
* Playback of live sources


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains header files for developing plugins for 
%{name}.


%prep
%autosetup

%build
%meson -Dgtk-doc=true
%meson_build

%install
%meson_install

# Rename non-standard hye locale to hy
if [ -d %{buildroot}%{_datadir}/locale/hye ]; then
    mv %{buildroot}%{_datadir}/locale/hye %{buildroot}%{_datadir}/locale/hy
fi

%find_lang %{name}

desktop-file-install                                    \
  --delete-original                                     \
  --remove-mime-type=video/x-totem-stream               \
  --dir=%{buildroot}%{_datadir}/applications            \
  %{buildroot}/%{_datadir}/applications/%{fullname}.desktop

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

%check
%meson_test

%files -f %{name}.lang
%license COPYING
%doc AUTHORS TODO THANKS README.md
%{_bindir}/%{name}
%dir %{_libdir}/%{name}-0/
%{_libdir}/%{name}-0/*.so
%{_datadir}/applications/%{fullname}.desktop
%{_datadir}/icons/hicolor/*/apps/*parole*
%{_datadir}/%{name}/
%{_datadir}/metainfo/%{name}.appdata.xml

%files devel
%doc %{_datadir}/gtk-doc/
%{_includedir}/%{name}/


%changelog
%autochangelog
