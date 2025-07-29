%global commit 7fa23e746ce7dbb793fc6af9482304157479e5c4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate  20250130

Name:           mankalaengine
Version:        1.1.%{commitdate}.%{shortcommit}
Release:        1%{?dist}
Summary:        A Mancala game engine with AI support

License:        GPL-3.0-or-later 
URL:            https://invent.kde.org/joaotgouveia/mankalaengine
Source0:        https://invent.kde.org/joaotgouveia/mankalaengine/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# Integrated Pallanguli rules and tui
Patch0: 0000-Draft-MR-integrated-pallaguli-rules-and-tui.patch
# Removed cppcheck from CMakeLists.txt
Patch1: 0001-Removed-cppcheck-from-CMakeLists.txt.patch 
# Installing TUI Binaries: https://invent.kde.org/joaotgouveia/mankalaengine/-/commit/6a401a492986c85f45b79e50585fd2697795121d
Patch2: 0002-Installing-Tui-binaries.patch 
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  extra-cmake-modules
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  kf6-rpm-macros
Requires:       qt6-qtbase
Requires:       mesa-libGL

%description
MankalaEngine is an engine used for 
creating computerized opponents for Mancala variants.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains 
libraries and header files for
developing  applications and plugins that use %{name}.

%package tui-games
Summary: TUI Binaries for Mancala Game Variants

%description tui-games
The %{name}-binaries package contains TUI binaries for different 
Mancala Variants supported by MankalaEngine.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
%cmake -DBUILD_EXAMPLES=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%{_libdir}/libMankalaEngine.so.1
%{_libdir}/libMankalaEngine.so.1.1
%license LICENSES/GPL-3.0-or-later.txt
%doc README.md

%files devel
%{_libdir}/cmake/mankalaengine/
%{_libdir}/libMankalaEngine.so
%{_includedir}/mankalaengine/

%files tui-games
%{_bindir}/bohnespieltui
%{_bindir}/pallangulitui

%changelog
%autochangelog

