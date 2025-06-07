%global         pkgname        OpenXR-SDK-Source
%global         libmajor 1

Name:           openxr
Version:        1.1.48
Release:        %autorelease
Summary:        Cross-platform VR/AR runtime and API
License:        Apache-2.0
URL:            https://github.com/KhronosGroup/%{pkgname}
Source:         %{url}/archive/refs/tags/release-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glslang)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-dri2)
BuildRequires:  pkgconfig(xrandr) 
BuildRequires:  python3dist(jinja2)

%description
OpenXR provides a vendor-neutral API for XR hardware, enabling portable
mixed reality and virtual reality applications.

%package libs
Summary:        OpenXR runtime loader library
%{?generate_subpackages:Requires: %{name}-devel = %{version}-%{release}}

%description libs
Shared library implementing the OpenXR loader for XR hardware interaction.

%package devel
Summary:        Headers and development files of the OpenXR library
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Headers and development files for building applications using OpenXR XR API.

%prep
%autosetup -n %{pkgname}-release-%{version}
%generate_buildrequires

%build
%cmake \
    -DBUILD_ALL_EXTENSIONS=ON \
    -DBUILD_LOADER=ON \
    -DBUILD_STATIC_LIBS=OFF \
    -DBUILD_TESTS=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_CXX_STANDARD=17 \
    -DDYNAMIC_LOADER=ON \
    -DFILESYSTEM_USE_STD=ON \
    -DGLSLANG_VALIDATOR=%{_bindir}/glslangValidator
%cmake_build


%install
%cmake_install

%check
%ctest

%files
%license LICENSE
# Include license in doc otherwise build complains
%doc CHANGELOG.SDK.md LICENSE README.md
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*.1*

%files libs
%{_libdir}/lib%{name}_loader.so.%{libmajor}{,.*}

%files devel
%doc README.md
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
