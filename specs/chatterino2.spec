# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

#note to future contributors:
# Do NOT use forge macros
#they crash bodhi

#pin to commit for patch fixes
%global         forgeurl0 https://github.com/Chatterino/chatterino2
%global         version0  2.5.4
%global         date      20251110
%global         commit0   f3559280786dbabc8cebe1951a525580d11cb2a5



# Git submodules
#   * libcommuni
%global forgeurl2   https://github.com/hemirt/libcommuni
%global commit2         bb5417c451d764f57f2f1b3e1c9a81496b5521bd
%global shortcommit2    %(c=%{commit2}; echo ${c:0:7})

#   * settings
%global forgeurl3   https://github.com/pajlada/settings
%global commit3         d847148cbf0becb75e48b90c2c25b78922f4e181
%global shortcommit3    %(c=%{commit3}; echo ${c:0:7})

#   * signals
%global forgeurl4   https://github.com/pajlada/signals
%global commit4         4b127541d30d9ae86df1553cb567cc2fc55fac46
%global shortcommit4    %(c=%{commit4}; echo ${c:0:7})

#   * serialize
%global forgeurl5   https://github.com/pajlada/serialize
%global commit5         f4a7dbfa64e7515506bdb75f6037cb74cd37f67c
%global shortcommit5    %(c=%{commit5}; echo ${c:0:7})

#   * magic_enum
%global forgeurl9   https://github.com/Neargye/magic_enum
%global commit9         e55b9b54d5cf61f8e117cafb17846d7d742dd3b4
%global shortcommit9    %(c=%{commit9}; echo ${c:0:7})


#   * certify
%global forgeurl11  https://github.com/djarek/certify
%global commit11       a448a3915ddac716ce76e4b8cbf0e7f4153ed1e2
%global shortcommit11   %(c=%{commit11}; echo ${c:0:7})

#   * expected-lite
%global forgeurl12  https://github.com/martinmoene/expected-lite
%global commit12        6656728c5874fefa976ff7c67999798df7fc961d
%global shortcommit12   %(c=%{commit12}; echo ${c:0:7})


Name:           chatterino2
Version:        %forgeversion
Release:        %autorelease
Summary:        Chat client for https://twitch.tv



#  - Main is MIT
# - chatterino2: MIT AND BSD-3-Clause
#  - cmake/CodeCoverage.cmake: BSD-3-Clause (CMake helper only, does not propagate to binary, SourceLicense only)
#  - lib/lrucache: BSD-3-Clause
#  - src/providers/twitch/ChatterinoWebSocketppLogger.hpp: BSD-3-Clause
#  - semver/include/semver/semver.hpp: MIT
#  - resources/*: MIT
# libcommuni: BSD-3-Clause
#  - Main is BSD-3-Clause
# settings: MIT
#  - Main is MIT
#  - cmake/conan_provider.cmake: MIT (CMake helper only, does not propagate to binary, SourceLicense only)
# signals: MIT
#  - Main is MIT
#  - cmake/conan_provider.cmake: MIT (CMake helper only, does not propagate to binary, SourceLicense only)
# serialize: MIT
#  - Main is MIT
# magic_enum: MIT
#  - Main is MIT
#  - cmake/GenPkgConfig: UNLICENSE (CMake helper only, does not propagate to binary, SourceLicense only)
# certify: BSL-1.0
#  - Main is BSL-1.0
# expected-lite: BSL-1.0
#  - Main is BSL-1.0
# lrucache
# - Main is BSD-3-Clause

License:        MIT AND BSD-3-Clause AND BSL-1.0
SourceLicense:  MIT AND BSD-3-Clause AND BSL-1.0 AND Unlicense

%global _description %{expand:
Chatterino 2 is a chat client for Twitch.tv. The Chatterino 2 wiki can be
found https://wiki.chatterino.com/.}
URL:            %{forgeurl}
Source0:        %{forgeurl0}/archive/%{commit0}.tar.gz
Source2:        %{forgeurl2}/archive/%{commit2}.tar.gz
Source3:        %{forgeurl3}/archive/%{commit3}.tar.gz
Source4:        %{forgeurl4}/archive/%{commit4}.tar.gz
Source5:        %{forgeurl5}/archive/%{commit5}.tar.gz
Source9:        %{forgeurl9}/archive/%{commit9}.tar.gz
Source11:       %{forgeurl11}/archive/%{commit11}.tar.gz
Source12:       %{forgeurl12}/archive/%{commit12}.tar.gz

# Patch0:https://patch-diff.githubusercontent.com/raw/Chatterino/chatterino2/pull/6495.diff
# fixes lua system lib lookup

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build

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
BuildRequires:  cmake(Qt6CorePrivate)
# BuildRequires: cmake(sol2)

BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(websocketpp)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libnotify)
BuildRequires: miniaudio-devel


%description
%_description

%package -n chatterino

Summary:        Chat client for https://twitch.tv


# because directory ownership
Requires:       hicolor-icon-theme

Provides:     chatterino2%{?_isa} = %{version}-%{release}

# Current submodules patched so not possible to build with system packages
#   * https://github.com/Chatterino/chatterino2/issues/1444
Provides:       bundled(expected-lite) = 0.9.0~git%{commit12}
Provides:       bundled(libcommuni) = 3.7.0~git%{commit2}
Provides:       bundled(magic_enum) = 0.9.5~git%{commit9}
Provides:       bundled(serialize) = 0.1.0~git%{commit5}
Provides:       bundled(settings) = 0.3.0~git%{commit3}
Provides:       bundled(signals) = 0.1.0~git%{commit4}
Provides:       bundled(certify) = 0.1~git%{commit4}

%description -n chatterino
%_description


%prep
%autosetup -a 0 -n chatterino2-%{commit0}

cd lib/libcommuni
tar -xf %{SOURCE2} --strip-components=1
cd ../settings
tar -xf %{SOURCE3} --strip-components=1
cd ../signals
tar -xf %{SOURCE4}  --strip-components=1
cd ../serialize
tar -xf %{SOURCE5} --strip-components=1
cd ../magic_enum
tar -xf %{SOURCE9} --strip-components=1
cd ../certify
tar -xf %{SOURCE11} --strip-components=1
cd ../expected-lite
tar -xf %{SOURCE12} --strip-components=1


%build
export GIT_COMMIT=%{commit0}
export GIT_HASH=%(c=%{commit0}; echo ${c:0:7})
export GIT_RELEASE=%{version0}
#NOTE: we need to fix `-DCHATTERINO_PLUGINS=OFF` in te future
%cmake -G Ninja \
                -DUSE_SYSTEM_QTKEYCHAIN=ON \
                -DUSE_SYSTEM_MINIAUDIO=ON \
                -DCHATTERINO_PLUGINS=OFF

%cmake_build


%install
%cmake_install
install -Dpm 0644 resources/com.chatterino.chatterino.appdata.xml   \
    %{buildroot}%{_metainfodir}/com.chatterino.chatterino.appdata.xml
install -Dpm 0644 resources/icon.png              \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/chatterino.png


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/com.chatterino.chatterino.desktop


%files -n chatterino
%license LICENSE resources/licenses/*
%doc README.md
%{_bindir}/chatterino
%{_datadir}/applications/com.chatterino.chatterino.desktop
%{_datadir}/icons/hicolor/256x256/apps/*chatterino.png
%{_metainfodir}/com.chatterino.chatterino.appdata.xml


%changelog
%autochangelog

