%undefine __cmake_in_source_build
%global _appid net.sourceforge.kmetronome

Name:           kmetronome
Version:        1.3.0
Release:        %autorelease
License:        GPLv2+
Summary:        A MIDI metronome using the Drumstick library
URL:            http://kmetronome.sourceforge.net
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.9
BuildRequires:  gettext
BuildRequires:  qt6-qtbase-devel >= 6.2
BuildRequires:  qt6-qtsvg-devel >= 6.2
BuildRequires:  qt6-qttools-devel >= 6.2
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  drumstick-devel >= 2.0.0
BuildRequires:  alsa-lib-devel >= 1.0
BuildRequires:  desktop-file-utils
BuildRequires:  %{_bindir}/pandoc

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
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{_appid}.desktop

%files
%doc readme.md ChangeLog AUTHORS TODO COPYING NEWS
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{_appid}.desktop
%{_datadir}/dbus-1/*/*
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1.*
%{_datadir}/metainfo/%{_appid}.appdata.xml

%changelog
%autochangelog
