%global appid   net.sourceforge.dmidiplayer

Name:           dmidiplayer
Version:        1.7.5
Release:        %autorelease
Summary:        Drumstick MIDI Player
# code is GPLv3+, examples (content) are mostly CC-BY-SA, except for one GPLv2+
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND CC-BY-SA-3.0
URL:            https://dmidiplayer.sourceforge.io/
Source:         https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  cmake >= 3.14
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pandoc

BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(drumstick-file) >= 2.10
BuildRequires:  cmake(drumstick-rt) >= 2.10
BuildRequires:  cmake(drumstick-widgets) >= 2.10
BuildRequires:  cmake(uchardet) >= 0.0.8

Requires:       hicolor-icon-theme

%description
This application is a multiplatform MIDI file player. It reads .MID (Standard
MIDI Files), .KAR (Karaoke), .RMI (RIFF MIDI), and .WRK (Cakewalk) file formats,
and outputs MIDI events to hardware MIDI ports and also software synths.

%prep
%autosetup -p1
cp examples/README.md LICENSE.examples


%build
%cmake
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml


%files
%license LICENSE LICENSE.examples
%doc ChangeLog README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{appid}.metainfo.xml


%changelog
%autochangelog
