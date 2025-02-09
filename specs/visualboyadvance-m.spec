%undefine _hardened_build

%global shortname vbam

Name:           visualboyadvance-m
Version:        2.1.11
Release:        %autorelease
Summary:        High compatibility Gameboy Advance Emulator combining VBA builds

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
Url:            https://github.com/visualboyadvance-m/visualboyadvance-m
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cairo-devel
BuildRequires:  cmake
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  nasm
BuildRequires:  openal-soft-devel
BuildRequires:  SDL2-devel
BuildRequires:  SFML-devel
BuildRequires:  wxGTK-devel
BuildRequires:  zlib-devel
BuildRequires:  zip

BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  libappstream-glib

Requires:  hicolor-icon-theme

# 32bit package serves very little purpose, s390x has build issues:
ExcludeArch: %{ix86} s390x

#Using info from here: http://vba-m.com/about.html and debian files
%description
VisualBoyAdvance-M is a Nintendo Game Boy Emulator with high compatibility with
commercial games. It emulates the Nintendo Game Boy Advance hand held console,
in addition to the original Game Boy hand held systems and its Super and Color
variants. VBA-M is a continued development of the now inactive VisualBoy
Advance project, with many improvements from various developments of VBA.

%package        sdl
Summary:        SDL version (no GUI) for VBA-M, a high compatibility Gameboy Advance Emulator

%description    sdl
This package provides the no-GUI, SDL only version of VisualBoyAdvance-M.
VisualBoyAdvance-M is a Nintendo Game Boy Emulator with high compatibility with
commercial games. It emulates the Nintendo Game Boy Advance hand held console,
in addition to the original Game Boy hand held systems and its Super and Color
variants. VBA-M is a continued development of the now inactive VisualBoy
Advance project, with many improvements from various developments of VBA.

%prep
%autosetup -p1 -n %{name}-%{version}
sed -i 's/ -mtune=generic//g' CMakeLists.txt
#Some odd permission issues:
chmod -x src/wx/rpi.h

%build
%cmake \
    -DCMAKE_SKIP_RPATH=ON \
    -DVERSION="%{version}" \
    -DVERSION_RELEASE=TRUE \
    -DENABLE_SDL=ON \
    -DENABLE_WX=ON \
    -DENABLE_FFMPEG=OFF \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
    -DENABLE_LINK=ON
%cmake_build

%install
%cmake_install
%find_lang wx%{shortname}

%check
desktop-file-validate \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/metainfo/%{name}.metainfo.xml

%files -f wx%{shortname}.lang
%license doc/gpl.txt doc/License.txt
%doc doc/ips.htm
%{_mandir}/man6/%{name}.*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/%{shortname}
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%files sdl
%doc doc/ReadMe.SDL.txt
%license doc/gpl.txt doc/License.txt
%config(noreplace) %{_sysconfdir}/%{shortname}.cfg
%{_mandir}/man6/%{shortname}.*
%{_bindir}/%{shortname}

%changelog
%autochangelog
