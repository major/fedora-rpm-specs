Name: rlottie
Version: 0.2
Release: %autorelease

# Main source: MIT
# rapidjson (base) - MIT
# rapidjson (msinttypes) - BSD-3-Clause
# freetype rasterizer - FTL
# vector (vinterpolator) - MPL-1.1
License: MIT AND FTL AND BSD-3-Clause AND MPL-1.1
Summary: Platform independent standalone library that plays Lottie Animation

URL: https://github.com/Samsung/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: %{name}-gcc11.patch

BuildRequires: gtest-devel
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: cmake
BuildRequires: gcc

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
%{summary}.

%prep
%autosetup -p1
sed -e "s/, 'optimization=s'//" -i meson.build

%build
# Upstream default C++ standard is c++14; gtest 1.17 requires C++17
%meson \
    -Dcpp_std=c++17 \
    -Dwerror=false \
    -Dtest=true \
    -Dthread=true \
    -Dexample=false \
    -Dcache=false \
    -Dlog=false \
    -Dcmake=true \
    -Dmodule=false
%meson_build

%install
%meson_install

%check
%meson_test

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
