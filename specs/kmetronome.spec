%global _appid net.sourceforge.kmetronome

Name:           kmetronome
Version:        1.4.1
Release:        %autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Summary:        A MIDI metronome using the Drumstick library
URL:            https://kmetronome.sourceforge.net
Source:         https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  cmake >= 3.16
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  pandoc

BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(drumstick-alsa) >= 2.10
# transitive dependency of drumstick-alsa
BuildRequires:  alsa-lib-devel >= 1.0

%description
KMetronome is a MIDI metronome with Qt interface, based on the Drumstick
library. The intended audience is musicians and music students. Like
solid, real metronomes it is a tool to keep the rhythm while playing musical
instruments. It uses MIDI for sound generation instead of digital audio,
allowing low CPU usage, and very accurate timing thanks to the ALSA sequencer.

%prep
%setup -q

%build
%{cmake}
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{_appid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{_appid}.metainfo.xml

%files
%doc readme.md ChangeLog AUTHORS TODO COPYING NEWS
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{_appid}.desktop
%{_datadir}/dbus-1/*/%{_appid}.*
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{_appid}.metainfo.xml

%changelog
%autochangelog
