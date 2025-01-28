%global _appid net.sourceforge.kmidimon

Name:           kmidimon
Version:        1.4.1
Release:        %autorelease
License:        GPL-2.0-or-later
Summary:        Drumstick MIDI monitor
URL:            https://kmidimon.sourceforge.net
Source:         https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  cmake >= 3.16
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pandoc

BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(drumstick-alsa) >= 2.10

%description
Drumstick MIDI Monitor monitors events coming from MIDI external ports or
applications via the ALSA sequencer, and from SMF (Standard MIDI files) or
WRK (Cakewalk/Sonar) files. It is especially useful if you want to debug MIDI
software or your MIDI setup. It features a nice graphical user interface,
customizable event filters and sequencer parameters, support for MIDI and ALSA
messages, and saving the recorded event list to a SMF or text file.

%prep
%autosetup


%build
%cmake
%cmake_build


%install
%cmake_install

%find_lang %{name} --with-man --with-qt


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{_appid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{_appid}.metainfo.xml


%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{_appid}.desktop
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*.ins
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{_appid}.metainfo.xml


%changelog
%autochangelog
