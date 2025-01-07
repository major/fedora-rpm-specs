# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

# Switch to Clang due LTO regression in GCC
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=114501
%global toolchain clang

%global forgeurl https://github.com/Chatterino/%{name}
%global uuid com.chatterino.chatterino
%global chatterino_git_commit 3aead09339ffff0fbfd9f8a7a5ea9eb551ad8fb8
%global chatterino_git_shortcommit %(c=%{chatterino_git_commit}; echo ${c:0:7})
%global tarball_version %%(echo %{version} | tr '~' '-')

# Git submodules
#   * libcommuni
%global commit2         030710ad53dda1541601ccabbad36a12a9e90c78
%global shortcommit2    %(c=%{commit2}; echo ${c:0:7})

#   * settings
%global commit3         9e9c2f65f4ae195a96329a90fd6ae24c24fb8f2f
%global shortcommit3    %(c=%{commit3}; echo ${c:0:7})

#   * signals
%global commit4         d06770649a7e83db780865d09c313a876bf0f4eb
%global shortcommit4    %(c=%{commit4}; echo ${c:0:7})

#   * serialize
%global commit5         17946d65a41a72b447da37df6e314cded9650c32
%global shortcommit5    %(c=%{commit5}; echo ${c:0:7})

#   * magic_enum
%global commit9         e55b9b54d5cf61f8e117cafb17846d7d742dd3b4
%global shortcommit9    %(c=%{commit9}; echo ${c:0:7})

#   * sanitizers-cmake
%global commit10        0573e2ea8651b9bb3083f193c41eb086497cc80a
%global shortcommit10   %(c=%{commit10}; echo ${c:0:7})

#   * miniaudio
%global commit11        4a5b74bef029b3592c54b6048650ee5f972c1a48
%global shortcommit11   %(c=%{commit11}; echo ${c:0:7})

#   * expected-lite
%global commit12        5b5caad7cd57d5ba3ca796bf1521b131d73ca405
%global shortcommit12   %(c=%{commit12}; echo ${c:0:7})

Name:           chatterino2
Version:        2.5.2
%forgemeta
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
License:        MIT and BSL-1.0 and BSD-3-Clause and zlib and GPL-2.0-or-later and LGPL-2.1-or-later and MPL-1.1

URL:            %{forgeurl}
Source0:        %{forgesource}
Source2:        https://github.com/hemirt/libcommuni/archive/%{commit2}/libcommuni-%{shortcommit2}.tar.gz
Source3:        https://github.com/pajlada/settings/archive/%{commit3}/settings-%{shortcommit3}.tar.gz
Source4:        https://github.com/pajlada/signals/archive/%{commit4}/signals-%{shortcommit4}.tar.gz
Source5:        https://github.com/pajlada/serialize/archive/%{commit5}/serialize-%{shortcommit5}.tar.gz
Source9:        https://github.com/Neargye/magic_enum/archive/%{commit9}/magic_enum-%{shortcommit9}.tar.gz
Source10:       https://github.com/arsenm/sanitizers-cmake/archive/%{commit10}/sanitizers-cmake-%{shortcommit10}.tar.gz
Source11:       https://github.com/mackron/miniaudio/archive/%{commit11}/miniaudio-%{shortcommit11}.tar.gz
Source12:       https://github.com/martinmoene/expected-lite/archive/%{commit12}/expected-lite-%{shortcommit12}.tar.gz


BuildRequires:  boost-devel
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  make

BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(RapidJSON)

BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(websocketpp)
BuildRequires:  pkgconfig(xkbcommon)

Requires:       hicolor-icon-theme
Requires:       qt6-qtsvg
Requires:       qt6-qtimageformats

# Current submodules patched so not possible to build with system packages
#   * https://github.com/Chatterino/chatterino2/issues/1444
Provides:       bundled(expected-lite) = 0.8.0~git%{shortcommit12}
Provides:       bundled(libcommuni) = 3.7.0~git%{shortcommit2}
Provides:       bundled(magic_enum) = 0.9.3~git%{shortcommit9}
Provides:       bundled(miniaudio) = 0.11.18~git%{shortcommit11}
Provides:       bundled(sanitizers-cmake) = 0~git%{shortcommit10}
Provides:       bundled(serialize) = 0~git%{shortcommit5}
Provides:       bundled(settings) = 0~git%{shortcommit3}
Provides:       bundled(signals) = 0.1.0~git%{shortcommit4}

%description
Chatterino 2 is a chat client for Twitch.tv. The Chatterino 2 wiki can be
found https://wiki.chatterino.com/.


%prep
%forgesetup
%setup -n %{name}-%{tarball_version} -q -D -T -a2
%setup -n %{name}-%{tarball_version} -q -D -T -a3
%setup -n %{name}-%{tarball_version} -q -D -T -a4
%setup -n %{name}-%{tarball_version} -q -D -T -a5
%setup -n %{name}-%{tarball_version} -q -D -T -a9
%setup -n %{name}-%{tarball_version} -q -D -T -a10
%setup -n %{name}-%{tarball_version} -q -D -T -a11
%setup -n %{name}-%{tarball_version} -q -D -T -a12

mv libcommuni-%{commit2}/*  lib/libcommuni
mv settings-%{commit3}/*    lib/settings
mv signals-%{commit4}/*     lib/signals
mv serialize-%{commit5}/*   lib/serialize
mv magic_enum-%{commit9}/*  lib/magic_enum
mv miniaudio-%{commit11}/*  lib/miniaudio
mv expected-lite-%{commit12}/* lib/expected-lite
mv sanitizers-cmake-%{commit10}/* cmake/sanitizers-cmake


%build
export GIT_COMMIT=%{chatterino_git_commit}
export GIT_HASH=%{chatterino_git_shortcommit}
export GIT_RELEASE=%{version}
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_WITH_QT6=ON \
    -DUSE_PRECOMPILED_HEADERS=0FF \
    -DUSE_SYSTEM_QTKEYCHAIN=ON \
    -DBUILD_WITH_QTKEYCHAIN=ON \
    %{nil}
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
