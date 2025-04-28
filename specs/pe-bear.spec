# Capitalized application name...
%global appname PE-bear

# Git revision of bearparser...
%global commit1 e2bfabf5d8c4b9c47596853be50260f8841b21ed
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

# Git revision of capstone...
%global commit2 80ede42453ce5717c1808cad512a4410fcb9df5a
%global shortcommit2 %(c=%{commit2}; echo ${c:0:7})

# Git revision of sig_finder...
%global commit3 1ac3b1a55c00a8f685d5bf2a722045e5bc49d1b6
%global shortcommit3 %(c=%{commit3}; echo ${c:0:7})

Name: pe-bear
Version: 0.7.1
Release: %autorelease

# main - GPL-2.0-or-later
# bearparser - BSD-2-Clause
# capstone - BSD-3-Clause
# sig_finder - BSD-2-Clause
License: GPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause
Summary: Portable Executable analyzing tool with a friendly GUI
URL: https://github.com/hasherezade/%{name}

Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: https://github.com/hasherezade/bearparser/archive/%{commit1}/bearparser-%{shortcommit1}.tar.gz
Source2: https://github.com/capstone-engine/capstone/archive/%{commit2}/capstone-%{shortcommit2}.tar.gz
Source3: https://github.com/hasherezade/sig_finder/archive/%{commit3}/sig_finder-%{shortcommit3}.tar.gz

Provides: bundled(bearparser) = 0.5~git%{shortcommit1}
Provides: bundled(capstone) = 5.0~git%{shortcommit2}
Provides: bundled(sig_finder) = 0~git%{shortcommit3}

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: ninja-build

%description
PE-bear is a multiplatform analyzing tool for PE (Portable Executable)
files. Its objective is to deliver fast and flexible "first view" for
malware analysts, stable and capable to handle malformed PE files.

%prep
%autosetup -p1

# Unpacking submodules...
tar -xf %{SOURCE1} -C bearparser --strip=1
tar -xf %{SOURCE2} -C capstone --strip=1
tar -xf %{SOURCE3} -C sig_finder --strip=1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DRELATIVE_LIBS:BOOL=OFF \
    -DSHOW_CONSOLE:BOOL=OFF \
    -DUSE_QT4:BOOL=OFF \
    -DUSE_QT5:BOOL=OFF
%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_metainfodir}/*.metainfo.xml

%changelog
%autochangelog
