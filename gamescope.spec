%global libliftoff_minver 0.4.1

Name:           gamescope
Version:        3.12.5
Release:        %autorelease
Summary:        Micro-compositor for video games on Wayland

License:        BSD
URL:            https://github.com/Plagman/gamescope
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Create stb.pc to satisfy dependency('stb')
Source1:        stb.pc

BuildRequires:  meson >= 0.54.0
BuildRequires:  ninja-build
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  google-benchmark-devel
BuildRequires:  libXmu-devel
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  (pkgconfig(wlroots) >= 0.16.0 with pkgconfig(wlroots) < 0.17)
BuildRequires:  (pkgconfig(libliftoff) >= 0.4.1 with pkgconfig(libliftoff) < 0.5)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  stb_image-devel
BuildRequires:  stb_image_write-devel
BuildRequires:  vkroots-devel
BuildRequires:  /usr/bin/glslangValidator

# libliftoff hasn't bumped soname, but API/ABI has changed for 0.2.0 release
Requires:       libliftoff%{?_isa} >= %{libliftoff_minver}
Requires:       xorg-x11-server-Xwayland
Recommends:     mesa-dri-drivers
Recommends:     mesa-vulkan-drivers

%description
%{name} is the micro-compositor optimized for running video games on Wayland.

%prep
%autosetup -p1
# Install stub pkgconfig file
mkdir -p pkgconfig
cp %{SOURCE1} pkgconfig/stb.pc

%build
export PKG_CONFIG_PATH=pkgconfig
%meson -Dpipewire=enabled -Denable_openvr_support=false -Dforce_fallback_for=[]
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/gamescope
%{_libdir}/libVkLayer_FROG_gamescope_wsi.so
%{_datadir}/vulkan/implicit_layer.d/VkLayer_FROG_gamescope_wsi.*.json


%changelog
%autochangelog
