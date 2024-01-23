# Capitalized application name...
%global appname PE-bear

# Git revision of bearparser...
%global commit1 e2c08098410c85e5546b77a2785444bbc9e0e21b
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

# Git revision of capstone...
%global commit2 61cdc56159986e6d77be571b04c570cf2c378d13
%global shortcommit2 %(c=%{commit2}; echo ${c:0:7})

Name: pe-bear
Version: 0.6.5.2
Release: 3%{?dist}

# main - GPL-2.0-or-later
# bearparser - BSD-2-Clause
# capstone - BSD-3-Clause
License: GPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause
Summary: Portable Executable analyzing tool with a friendly GUI
URL: https://github.com/hasherezade/%{name}

Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: https://github.com/hasherezade/bearparser/archive/%{commit1}/bearparser-%{shortcommit1}.tar.gz
Source2: https://github.com/capstone-engine/capstone/archive/%{commit2}/capstone-%{shortcommit2}.tar.gz

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
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 09 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.5.2-1
- Updated to version 0.6.5.2.

* Sun Feb 26 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.5-1
- Initial SPEC release.
