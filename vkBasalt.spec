# 'reshade' commit
%global commit ee98003229465f9872e983a43a83b8cddc054fce
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: vkBasalt
Version: 0.3.2.10
Release: %autorelease
Summary: Vulkan post processing layer

# The entire source code is zlib except:
# * ASL 2.0: include/vulkan/
License: zlib and ASL 2.0
URL: https://github.com/DadSchoorse/vkBasalt
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++ >= 9
BuildRequires: glibc-devel
BuildRequires: glslang
BuildRequires: meson
BuildRequires: spirv-headers-devel
BuildRequires: spirv-tools
BuildRequires: vulkan-headers
BuildRequires: vulkan-tools
BuildRequires: vulkan-validation-layers-devel

BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(x11)

Suggests: goverlay

Provides: bundled(reshade) = 0~git%{shortcommit}

%description
vkBasalt is a Vulkan post processing layer to enhance the visual graphics of
games.

Currently, the build in effects are:

  - Contrast Adaptive Sharpening
  - Denoised Luma Sharpening
  - Fast Approximate Anti-Aliasing
  - Enhanced Subpixel Morphological Anti-Aliasing
  - 3D color LookUp Table

It is also possible to use Reshade Fx shaders.


%prep
%autosetup -p1


%build
%meson \
    -Dappend_libdir_vkbasalt=true
%meson_build


%install
%meson_install

# Configuration file
install -Dpm 0644 config/%{name}.conf -t %{buildroot}%{_sysconfdir}/


%files
%license LICENSE
%doc README.md
%{_datadir}/vulkan/implicit_layer.d/%{name}.json
%{_libdir}/vkbasalt/
%config(noreplace) %{_sysconfdir}/%{name}.conf


%changelog
%autochangelog
