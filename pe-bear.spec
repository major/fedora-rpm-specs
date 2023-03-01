# Capitalized application name...
%global appname PE-bear

# Git revision of bearparser...
%global commit1 0e07f217650bf1fb1883b602398377e376c8ace2
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

# Git revision of capstone...
%global commit2 afb5575140dbf8405a8f6c3ec00ba1f954f668d0
%global shortcommit2 %(c=%{commit2}; echo ${c:0:7})

Name: pe-bear
Version: 0.6.5
Release: 1%{?dist}

# main - GPL-2.0-or-later
# bearparser - BSD-2-Clause
# capstone - BSD-3-Clause
License: GPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause
Summary: Portable Executable analyzing tool with a friendly GUI
URL: https://github.com/hasherezade/%{name}

Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: https://github.com/hasherezade/bearparser/archive/%{commit1}/bearparser-%{shortcommit1}.tar.gz
Source2: https://github.com/capstone-engine/capstone/archive/%{commit2}/capstone-%{shortcommit2}.tar.gz

# https://github.com/hasherezade/pe-bear/pull/21
Patch100: %{name}-linux-integration.patch

Provides: bundled(bearparser) = 0.3~git%{shortcommit1}
Provides: bundled(capstone) = 4.0.2~git%{shortcommit2}

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)

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

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DRELATIVE_LIBS:BOOL=OFF \
    -DSHOW_CONSOLE:BOOL=OFF \
    -DUSE_QT4:BOOL=OFF
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
* Sun Feb 26 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.5-1
- Initial SPEC release.
