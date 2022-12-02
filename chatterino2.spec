# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global uuid com.chatterino.chatterino
%global chatterino_git_commit a0f9310062721e742ccd1cc869e4cc40ef626c0f
%global tarball_version %%(echo %{version} | tr '~' '-')

# Git submodules
#   * libcommuni
%global commit2         a7b32cd6fa0640721b6114b31d37d79ebf832411
%global shortcommit2    %(c=%{commit2}; echo ${c:0:7})

#   * settings
%global commit3         04792d853c7f83c9d7ab4df00279442a658d3be3
%global shortcommit3    %(c=%{commit3}; echo ${c:0:7})

#   * signals
%global commit4         25e4ec3b8d6ea94a5e65a26e7cfcbbce3b87c5d6
%global shortcommit4    %(c=%{commit4}; echo ${c:0:7})

#   * serialize
%global commit5         7d37cbfd5ac3bfbe046118e1cec3d32ba4696469
%global shortcommit5    %(c=%{commit5}; echo ${c:0:7})

#   * qtkeychain
%global commit8         de954627363b0b4bff9a2616f1a409b7e14d5df9
%global shortcommit8    %(c=%{commit8}; echo ${c:0:7})

#   * magic_enum
%global commit9         f4ebb4f185ce956bf50b93acbef1516030ecdb36
%global shortcommit9    %(c=%{commit9}; echo ${c:0:7})

#   * sanitizers-cmake
%global commit10         99e159ec9bc8dd362b08d18436bd40ff0648417b
%global shortcommit10    %(c=%{commit10}; echo ${c:0:7})


Name:           chatterino2
Version:        2.4.0
Release:        %autorelease
Summary:        Chat client for https://twitch.tv

# Boost Software License (v1.0) Boost Software License 1.0
# -----------------------------------------------------------------------
# resources/licenses/boost_boost.txt
#
# BSD 3-clause "New" or "Revised" License
# ---------------------------------------
# lib/libcommuni/
#
# Expat License
# -------------
# lib/serialize/
# lib/signals/
# resources/
#
# Mozilla Public License (v1.1) GNU General Public License (v2 or later) or GNU Lesser General Public License (v2.1 or later)
# ---------------------------------------------------------------------------------------------------------------------------
# lib/libcommuni/
#
# zlib/libpng license Aladdin Free Public License
# -----------------------------------------------
# lib/websocketpp/
#
License:        MIT and Boost and BSD and zlib and GPLv2+ and LGPLv2+ and MPLv1.1

URL:            https://github.com/Chatterino/chatterino2
Source0:        %{url}/archive/v%{tarball_version}/%{name}-%{tarball_version}.tar.gz
Source2:        https://github.com/hemirt/libcommuni/archive/%{commit2}/libcommuni-%{shortcommit2}.tar.gz
Source3:        https://github.com/pajlada/settings/archive/%{commit3}/settings-%{shortcommit3}.tar.gz
Source4:        https://github.com/pajlada/signals/archive/%{commit4}/signals-%{shortcommit4}.tar.gz
Source5:        https://github.com/pajlada/serialize/archive/%{commit5}/serialize-%{shortcommit5}.tar.gz
Source8:        https://github.com/Chatterino/qtkeychain/archive/%{commit8}/qtkeychain-%{shortcommit8}.tar.gz
Source9:        https://github.com/Neargye/magic_enum/archive/%{commit9}/magic_enum-%{shortcommit9}.tar.gz
Source10:       https://github.com/arsenm/sanitizers-cmake/archive/%{commit10}/sanitizers-cmake-%{shortcommit10}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make

BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.12
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(RapidJSON)
BuildRequires:  cmake(websocketpp)

BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(openssl)

Requires:       hicolor-icon-theme
Requires:       qt5-qtsvg

# Current submodules patched so not possible to build with system packages
#   * https://github.com/Chatterino/chatterino2/issues/1444
Provides:       bundled(libcommuni) = 3.6.0
Provides:       bundled(magic_enum) = 0.8.1~git%{shortcommit9}
Provides:       bundled(qtkeychain) = 0.9.1~git%{shortcommit8}
Provides:       bundled(sanitizers-cmake) = 0~git%{shortcommit10}
Provides:       bundled(serialize) = 0~git%{shortcommit5}
Provides:       bundled(settings) = 0~git%{shortcommit3}
Provides:       bundled(signals) = 0~git%{shortcommit4}

%description
Chatterino 2 is a chat client for Twitch.tv.


%prep
%setup -n %{name}-%{tarball_version} -q
%setup -n %{name}-%{tarball_version} -q -D -T -a2
%setup -n %{name}-%{tarball_version} -q -D -T -a3
%setup -n %{name}-%{tarball_version} -q -D -T -a4
%setup -n %{name}-%{tarball_version} -q -D -T -a5
%setup -n %{name}-%{tarball_version} -q -D -T -a8
%setup -n %{name}-%{tarball_version} -q -D -T -a9
%setup -n %{name}-%{tarball_version} -q -D -T -a10

mv libcommuni-%{commit2}/*  lib/libcommuni
mv settings-%{commit3}/*    lib/settings
mv signals-%{commit4}/*     lib/signals
mv serialize-%{commit5}/*   lib/serialize
mv qtkeychain-%{commit8}/*  lib/qtkeychain
mv magic_enum-%{commit9}/*  lib/magic_enum
mv sanitizers-cmake-%{commit10}/* cmake/sanitizers-cmake


%build
GIT_COMMIT=%{chatterino_git_commit}
%cmake \
    -DCHATTERINO_GIT_COMMIT=%{chatterino_git_commit} \
    -DUSE_PRECOMPILED_HEADERS=0FF \
    -DUSE_SYSTEM_QTKEYCHAIN=ON
%cmake_build


%install
%cmake_install
install -Dpm 0644 resources/%{uuid}.appdata.xml   \
    %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml
install -Dpm 0644 resources/icon.png              \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/chatterino.png


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE
%doc README.md BUILDING_ON_LINUX.md docs/
%{_bindir}/chatterino
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/*.xml


%changelog
%autochangelog
