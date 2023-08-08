%global appname CorsixTH
%global uuid    com.corsixth.%{appname}
%global tarball_version %%(echo %{version} | tr '~' '-')

Name:           corsix-th
Version:        0.67
Release:        %autorelease
Summary:        Open source clone of Theme Hospital

# For a breakdown of the licensing, see LICENSE.txt
# The entire source code is MIT except:
# BSD:          CMake scripts
# GPLv3+:       SpriteEncoder
License:        MIT and BSD and GPLv3+
URL:            https://github.com/CorsixTH/CorsixTH
Source0:        %{url}/archive/v%{tarball_version}/%{name}-%{tarball_version}.tar.gz

BuildRequires:  cmake >= 3.10
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  lua-devel >= 5.4.2
BuildRequires:  ninja-build

BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(sdl2)

%if 0%{?fedora} <= 33
BuildRequires:  auto-destdir
%endif

Requires:       %{name}-data
Requires:       hicolor-icon-theme
Requires:       lua-filesystem
Requires:       lua-lpeg

# For music support
Recommends:     fluid-soundfont-lite-patches

# For extracting GOG version
Recommends:     innoextract

%global _description %{expand:
CorsixTH aims to reimplement the game engine of Theme Hospital, and be able to
load the original game data files. This means that you will need a purchased
copy of Theme Hospital, or a copy of the demo, in order to use CorsixTH. After
most of the original engine has been reimplemented in open source code, the
project will serve as a base from which extensions and improvements to the
original game can be made.

  * To play CorsixTH, you will need either the Demo:

    https://th.corsix.org/Demo.zip

  * or the full game of Theme Hospital, available for example at:

    https://www.gog.com/game/theme_hospital}

%description %{_description}


%package        data
Summary:        Data files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    data %{_description}

Package contains data files for %{name}.


%prep
%autosetup -n %{appname}-%{tarball_version} -p1


%build
%cmake \
    -G Ninja \
    -DWITH_MOVIES=0 \
    %{nil}
%cmake_build


%install
%cmake_install
# Remove and catch license file by RPM macros
rm %{buildroot}%{_datadir}/%{name}/LICENSE.txt


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%doc README.md README.txt
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_mandir}/man6/%{name}.6*
%{_metainfodir}/*.xml

%files data
%license LICENSE.txt
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/scalable/apps/*.svg


%changelog
%autochangelog
