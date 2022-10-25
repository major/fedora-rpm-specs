# Force out of source build
%undefine __cmake_in_source_build

# lib%%{name}core.so* is a private lib with no headers, so we should
# not provide that.
%global __provides_exclude ^lib%{name}.*\\.so$
%global __requires_exclude ^lib%{name}.*\\.so$

%global commit          aceda48bf37b77e042769ee5b2337b38a6d40538
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20200701

Name:       soundkonverter
Version:    3.0.1
Release:    %autorelease
Summary:    Audio file converter, CD ripper and Replay Gain tool

License:    GPL-2.0-or-later
URL:        http://kde-apps.org/content/show.php?content=29024
Source0:    https://github.com/dfaust/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5Cddb)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(phonon4qt5)
BuildRequires:  pkgconfig(taglib) >= 1.4
BuildRequires:  cdparanoia-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme
Requires:       cdparanoia
Requires:       flac
Requires:       fluidsynth
Requires:       speex
Requires:       timidity++
Requires:       vorbis-tools
Requires:       wavpack
Recommends:     faac
Recommends:     faad2
Recommends:     ffmpeg
Recommends:     lame
Recommends:     mac
Recommends:     mp3gain
Recommends:     mppenc
Recommends:     sox
Recommends:     twolame
Recommends:     vorbisgain
Recommends:     opus-tools

%description
SoundKonverter is a front-end to various audio converters.

The key features are:
  * Audio conversion
  * Replay Gain calculation
  * CD ripping

%prep
%autosetup -p1 -n %{name}-%{commit}
# sed 's|<fileref.h|<taglib/fileref.h>|' src/metadata/MetaReplayGain.h

%build
%cmake_kf5 src "-DKF5_BUILD=ON"
%cmake_build

%install
%cmake_install
%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%{_kf5_bindir}/%{name}
%{_kf5_libdir}/lib%{name}core.so
%{_kf5_libdir}/qt5/plugins/%{name}_*
%{_kf5_datadir}/%{name}
%dir %{_kf5_datadir}/solid
%dir %{_kf5_datadir}/solid/actions
%dir %{_kf5_datadir}/kxmlgui5/%{name}
%{_kf5_datadir}/kservices5/%{name}_*
%{_kf5_datadir}/kservicetypes5/%{name}_*
%{_kf5_datadir}/kxmlgui5/%{name}/%{name}ui.rc
%{_kf5_datadir}/solid/actions/%{name}-*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}-replaygain.png
%{_kf5_metainfodir}/%{name}.appdata.xml

%changelog
%autochangelog
