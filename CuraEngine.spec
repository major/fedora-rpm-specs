Name:           CuraEngine
Epoch:          1
Version:        5.4.0
Release:        %autorelease
Summary:        Engine for processing 3D models into G-code instructions for 3D printers
License:        AGPL-3.0-or-later
URL:            https://github.com/Ultimaker/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Cmake bits taken from 4.13.1, before upstream went nuts with conan
Source2:        FindGMock.cmake
Source3:        FindPolyclipping.cmake
Source4:        FindStb.cmake
Source5:        CMakeLists.txt
Source6:        CPackConfig.cmake

# This is some kind of "public" layer of a private logging thing :/
# It's header-only and not usable as a system library,
# so I (churchyard) decided to bundle it for now. Shame on me.
# It's AGPL-3.0-or-later.
%global scripta_version c378c837eeb505146ab67abe0904bfed2099128f
Source7:        https://github.com/Ultimaker/Scripta_public/archive/%{scripta_version}/Scripta_public-%{scripta_version}.tar.gz
Provides:       bundled(scripta) = %{scripta_version}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libarcus-devel >= 5.2.2
BuildRequires:  polyclipping-devel >= 6.1.2
BuildRequires:  protobuf-devel
BuildRequires:  rapidjson-devel
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  boost-devel
BuildRequires:  range-v3-devel
BuildRequires:  fmt-devel
BuildRequires:  spdlog-devel

# Header-only package; -static version is for tracking per guidelines
# Enforce the the minimum EVR to contain fixes for all of:
# CVE-2021-28021
# CVE-2021-42715
# CVE-2021-42716
# CVE-2022-28041
# CVE-2023-43898
# CVE-2023-45661
# CVE-2023-45662
# CVE-2023-45663
# CVE-2023-45664
# CVE-2023-45666
# CVE-2023-45667
BuildRequires:  stb_image-static >= 2.28^20231011gitbeebb24-12

Patch0:         %{name}-static-libstdcpp.patch
# Patch for fmtlib 10, from https://github.com/Ultimaker/CuraEngine/commit/5a4ca90594f965b6a5e6af626a5c508185277162
Patch1:         CuraEngine-5.4.0-fmt10.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
%{name} is a C++ console application for 3D printing G-code generation. It
has been made as a better and faster alternative to the old Skeinforge engine.

This is just a console application for G-code generation. For a full graphical
application look at cura with is the graphical frontend for %{name}.

%prep
%setup -q

mkdir cmake
cp -a %{SOURCE2} %{SOURCE3} %{SOURCE4} cmake
rm -rf CMakeLists.txt
cp -a %{SOURCE5} %{SOURCE6} .

tar xf %{SOURCE7}
mv Scripta_public-%{scripta_version}/include/scripta/ include/

%patch -P0 -p1
%patch -P1 -p1

# bundled libraries
rm -rf libs

# The -DCURA_ENGINE_VERSION does not work, so we sed-change the default value
# sed -i 's/"DEV"/"%{version}"/' src/settings/Settings.h

%build
%cmake \
  -DSET_RPATH:BOOL=OFF \
  -DBUILD_SHARED_LIBS:BOOL=OFF \
  -DCURA_ENGINE_VERSION:STRING=%{version} \
  -DUSE_SYSTEM_LIBS:BOOL=ON \
  -DCMAKE_CXX_FLAGS_RELEASE_INIT:STRING="%{optflags} -fPIC" \
  -DStb_INCLUDE_DIRS:PATH=%{_includedir}
%cmake_build


%install
%cmake_install


%check
# Smoke test
%{buildroot}%{_bindir}/%{name} help

%files
%doc LICENSE README.md
%{_bindir}/%{name}

%changelog
%autochangelog
