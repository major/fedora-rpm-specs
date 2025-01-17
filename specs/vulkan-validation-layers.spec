Name:           vulkan-validation-layers
Version:        1.4.304.0
Release:        %autorelease
Summary:        Vulkan validation layers

License:        Apache-2.0
URL:            https://github.com/KhronosGroup/Vulkan-ValidationLayers
Source0:        %url/archive/vulkan-sdk-%{version}.tar.gz#/Vulkan-ValidationLayers-sdk-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  glslang-devel
BuildRequires:  ninja-build
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  spirv-tools-devel
BuildRequires:  spirv-headers-devel
BuildRequires:  vulkan-headers
BuildRequires:  vulkan-loader-devel
BuildRequires:  vulkan-utility-libraries-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xcb)

%description
Vulkan validation layers

%prep
%autosetup -p1 -n Vulkan-ValidationLayers-vulkan-sdk-%{version}


%build
# Decrease debuginfo verbosity to reduce memory consumption even more
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%global optflags %(echo %{optflags} | sed 's/-O2 /-O1 /')

%cmake3 -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_WERROR=OFF \
        -DGLSLANG_INSTALL_DIR=%{_prefix} \
        -DBUILD_LAYER_SUPPORT_FILES:BOOL=ON \
        -DUSE_ROBIN_HOOD_HASHING:BOOL=OFF \
        -DSPIRV_HEADERS_INSTALL_DIR=%{_prefix} \
        -DVULKAN_HEADERS_INSTALL_DIR=%{_prefix} \
        -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets


%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md
%{_datadir}/vulkan/explicit_layer.d/*.json
%{_libdir}/libVkLayer_*.so

%changelog
%autochangelog
