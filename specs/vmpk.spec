Name:           vmpk
Version:        0.9.1
Release:        %autorelease
Summary:        Virtual MIDI Piano Keyboard
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://vmpk.sourceforge.io/
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel >= 6.2
BuildRequires:  qt6-qtsvg-devel >= 6.2
BuildRequires:  qt6-qttools-devel >= 6.2
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  drumstick-devel >= 2.9
BuildRequires:  libxcb-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake >= 3.9
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:  desktop-file-utils

Requires:       fluid-soundfont-gm

%description
VMPK is a MIDI event generator/receiver. It doesn't produce any sound by
itself, but can be used to drive a MIDI synthesizer (either hardware or
software, internal or external). You can use the computer's keyboard to play
MIDI notes, and also the mouse. You can use the Virtual MIDI Piano Keyboard to
display the played MIDI notes from another instrument or MIDI file player.


%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/net.sourceforge.VMPK.desktop

%files
%doc NEWS README.md ChangeLog AUTHORS TODO COPYING
%{_bindir}/%{name}
%{_datadir}/applications/net.sourceforge.VMPK.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/net.sourceforge.VMPK.metainfo.xml
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
