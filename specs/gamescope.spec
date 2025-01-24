%if 0%{?fedora} >= 41
%global libliftoff_minver 0.5.0
%else
%global libliftoff_minver 0.4.1
%endif
%global reshade_commit 696b14cd6006ae9ca174e6164450619ace043283
%global reshade_shortcommit %(c=%{reshade_commit}; echo ${c:0:7})

Name:           gamescope
Version:        3.16.1
Release:        %autorelease
Summary:        Micro-compositor for video games on Wayland
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/ValveSoftware/gamescope
# luajit is not available on ppc64le:
# https://bugzilla.redhat.com/show_bug.cgi?id=2339416
ExcludeArch:    ppc64le

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Create stb.pc to satisfy dependency('stb')
Source1:        stb.pc
Source2:        https://github.com/Joshua-Ashton/reshade/archive/%{reshade_commit}/reshade-%{reshade_shortcommit}.tar.gz

# https://github.com/misyltoad/reshade/pull/1:
Patch:          0001-cstdint.patch
# Allow to use system wlroots
# We use/package rest from the forks, I've tried to verify that wlroots match relevant commits
# We'll hold on rebases of gamescope if tags diverge in the future
Patch:          Allow-to-use-system-wlroots.patch
Patch:          Switch-wlroots-to-the-new-pc-filename.patch
Patch:          Add-pixman-dependency.patch
# https://github.com/ValveSoftware/gamescope/pull/1548:
Patch:          https://github.com/ValveSoftware/gamescope/commit/fa0832f616a1060a3311f9b41368590169ba4872.patch

BuildRequires:  meson >= 0.54.0
BuildRequires:  ninja-build
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  glm-devel
BuildRequires:  google-benchmark-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXcursor-devel
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
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(wlroots-0.18)
BuildRequires:  (pkgconfig(libliftoff) >= %{libliftoff_minver} with pkgconfig(libliftoff) < 0.6)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libeis-1.0)
BuildRequires:  pkgconfig(libdecor-0)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(openvr) >= 2.7
BuildRequires:  spirv-headers-devel
# Enforce the the minimum EVR to contain fixes for all of:
# CVE-2021-28021 CVE-2021-42715 CVE-2021-42716 CVE-2022-28041 CVE-2023-43898
# CVE-2023-45661 CVE-2023-45662 CVE-2023-45663 CVE-2023-45664 CVE-2023-45666
# CVE-2023-45667
BuildRequires:  stb_image-devel >= 2.28^20231011gitbeebb24-12
# Header-only library: -static is for tracking per guidelines
BuildRequires:  stb_image-static
BuildRequires:  stb_image_resize-devel
BuildRequires:  stb_image_resize-static
BuildRequires:  stb_image_write-devel
BuildRequires:  stb_image_write-static
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
%autosetup -p1 -a2 -N
# Install stub pkgconfig file
mkdir -p pkgconfig
cp %{SOURCE1} pkgconfig/stb.pc

# Replace spirv-headers include with the system directory
sed -i 's^../thirdparty/SPIRV-Headers/include/spirv/^/usr/include/spirv/^' src/meson.build

# Push in reshade from sources instead of submodule
rm -rf src/reshade && mv reshade-%{reshade_commit} src/reshade

%autopatch -p1

%build
export PKG_CONFIG_PATH=pkgconfig
%meson -Dpipewire=enabled -Denable_openvr_support=true -Dforce_fallback_for=[]
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/gamescope
%{_bindir}/gamescopectl
%{_bindir}/gamescopereaper
%{_bindir}/gamescopestream
%{_datadir}/gamescope
%{_libdir}/libVkLayer_FROG_gamescope_wsi_*.so
%{_datadir}/vulkan/implicit_layer.d/VkLayer_FROG_gamescope_wsi.*.json


%changelog
%autochangelog
