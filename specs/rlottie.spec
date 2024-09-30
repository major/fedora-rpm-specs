Name: rlottie
Version: 0.2
Release: 12%{?dist}

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
%meson \
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
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild
