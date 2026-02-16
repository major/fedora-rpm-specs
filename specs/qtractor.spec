Name:           qtractor
Version:        1.5.11
Release:        %autorelease
Summary:        Audio/MIDI multi-track sequencer
License:        GPL-2.0-or-later
URL:            https://www.qtractor.org
Source0:        https://download.sourceforge.net/qtractor/qtractor-%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=2385565
Patch0:         0001-cmake-jack-libs.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6LinguistTools)

BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(aubio)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(lilv-0)

# disable for Qt6
#BuildRequires:  pkgconfig(suil-0)

# https://github.com/rncbc/qtractor/issues/431
#BuildRequires:  pkgconfig(gtk+-2.0)
#BuildRequires:  pkgconfig(gtkmm-2.4)

BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig(dssi)

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme

%description
Qtractor is an Audio/MIDI multi-track sequencer application written in C++ with
the Qt framework. Target platform is Linux, where the Jack Audio Connection Kit
(JACK) for audio, and the Advanced Linux Sound Architecture (ALSA) for MIDI, are
the main infrastructures to evolve as a fairly-featured Linux desktop audio
workstation GUI, specially dedicated to the personal home-studio.

%prep
%autosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCONFIG_XUNIQUE=ON \
    -DCONFIG_STACKTRACE=ON \
    -DCONFIG_WAYLAND=ON \
    -DCONFIG_QT6=ON \
    -DCONFIG_LIBJACK=ON \
    -DCONFIG_LIBASOUND=ON \
    -DCONFIG_LV2_UI_GTK2=OFF \
    -DCONFIG_LV2_UI_GTKMM2=OFF
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%files -f %{name}.lang
%doc ChangeLog README
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/org.rncbc.qtractor.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/org.rncbc.qtractor.xml
%{_datadir}/man/man1/%{name}*
%{_datadir}/man/*/man1/%{name}*
%{_datadir}/metainfo/org.rncbc.qtractor.metainfo.xml
%dir %{_datadir}/qtractor
%{_datadir}/qtractor/audio/
%{_datadir}/qtractor/instruments/
%{_datadir}/qtractor/palette/

%changelog
%autochangelog
