Name: rlottie
Epoch: 1
Version: 0.2

%global forgeurl https://github.com/Samsung/%{name}
%global commit ea06d2f29ba01b8d06c00a838d107f5e484ae59b

%global forgeurl1 https://github.com/kuba--/zip
%global tag1 v0.3.2

%forgemeta -a

Release: %autorelease

# Main source: MIT
# kuba--/zip - Unlicense
# miniz - MIT AND Unlicense
# freetype rasterizer - FTL
# vinterpolator.cpp (modified from mozilla/gecko-dev/dom/smil/SMILKeySpline.cpp) - MPL-1.1
# pixman arm neon routines - MIT
License: MIT AND FTL AND BSD-3-Clause AND MPL-1.1 AND (MIT AND Unlicense)
Summary: Platform independent standalone library that plays Lottie Animation

URL: %{forgeurl}
Source0: %{forgesource}
Source1: %{forgesource1}
# https://github.com/Samsung/rlottie/pull/553.patch
# Use GNUInstallDirs
Patch0: 0001-cmake-fix.patch
Patch1: 0002-update-zip.patch
# gtest 1.17 requires C++17; upstream hardcodes -std=c++14
Patch2: 0003-bump-cxx-standard.patch
# System stb_image >= 2.30 fails to compile with STBI_ONLY_PNG (upstream bug)
Patch3: 0004-stb-image-no-pnm.patch

BuildRequires: gcc
BuildRequires: gcc-c++

BuildRequires: cmake
BuildRequires: cmake(GTest)
BuildRequires: stb_image-static
BuildRequires: rapidjson-static

Provides: bundled(minizip) = 3.0.2
Provides: bundled(kuba-zip) = %{tag1}

%description
rlottie is a platform independent standalone c++ library for rendering
vector based animations and art in realtime.

Lottie loads and renders animations and vectors exported in the bodymovin
JSON format. Bodymovin JSON can be created and exported from After Effects
with bodymovin, Sketch with Lottie Sketch Export, and from Haiku.

For the first time, designers can create and ship beautiful animations
without an engineer painstakingly recreating it by hand. Since the animation
is backed by JSON they are extremely small in size but can be large in
complexity!

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains headers and development files for %{name}.

%prep
%forgeautosetup -p1

# Unbundle / upgrade deps
rm -rfv src/vector/stb/stb_image.h src/lottie/zip/*.{h,cpp} src/lottie/rapidjson
tar -xf %{SOURCE1} -C src/lottie/zip --strip-components=2 --wildcards "*/src/*"

%build
%cmake -DBUILD_TESTING:BOOL=ON -DLOTTIE_MODULE:BOOL=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc AUTHORS README.md
%license COPYING licenses/*
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/

%changelog
%autochangelog
