Name:           dxvk-native
Version:        2.3
Release:        1%{?dist}
Summary:        Vulkan-based D3D11 and D3D9 implementation for Linux

License:        Zlib
URL:            https://github.com/doitsujin/dxvk
Source0:        %{url}/archive/v%{version}/dxvk-%{version}.tar.gz
# Will hopefully be upstreamed in a different form...
Source1:        dxvk-native.pc.in

# From: https://github.com/doitsujin/dxvk/pull/3824
Patch01:        0001-meson-Only-use-the-libdisplay-info-subproject-as-a-f.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.46
BuildRequires:  glslang
BuildRequires:  SDL2-devel
BuildRequires:  vulkan-loader-devel
BuildRequires:  spirv-headers-devel
BuildRequires:  mingw64-headers
BuildRequires:  pkgconfig(libdisplay-info)

Requires:       vulkan-loader%{?_isa}
Requires:       SDL2%{?_isa}

# Requires x86-specific headers for now...
ExclusiveArch:  %{ix86} x86_64

%description
DXVK Native is a port of DXVK to Linux which allows it
to be used natively without Wine.

This is primarily useful for game and application ports
to either avoid having to write another rendering backend,
or to help with port bringup during development.

%package devel
Summary:        Development files used to build applications using %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       SDL2-devel%{?_isa}
Requires:       vulkan-loader-devel%{?_isa}

%description devel
This package provides the development libraries and other
files for building applications that use %{name}.

%prep
%autosetup -n dxvk-%{version} -p1

# Replace local vulkan/directx headers includes with the system directories
sed -i 's^./include/vulkan/include^/usr/include^' meson.build
sed -i 's^./include/spirv/include^/usr/include^' meson.build

# Copy the MinGW DirectX headers to include/native/directx/
cp %{mingw64_includedir}/d3d10_1.h include/native/directx
cp %{mingw64_includedir}/d3d10_1shader.h include/native/directx
cp %{mingw64_includedir}/d3d10effect.h include/native/directx
cp %{mingw64_includedir}/d3d10.h include/native/directx
cp %{mingw64_includedir}/d3d10misc.h include/native/directx
cp %{mingw64_includedir}/d3d10sdklayers.h include/native/directx
cp %{mingw64_includedir}/d3d10shader.h include/native/directx
cp %{mingw64_includedir}/d3d11_1.h include/native/directx
cp %{mingw64_includedir}/d3d11_2.h include/native/directx
cp %{mingw64_includedir}/d3d11_3.h include/native/directx
cp %{mingw64_includedir}/d3d11_4.h include/native/directx
cp %{mingw64_includedir}/d3d11.h include/native/directx
cp %{mingw64_includedir}/d3d11on12.h include/native/directx
cp %{mingw64_includedir}/d3d11sdklayers.h include/native/directx
cp %{mingw64_includedir}/d3d11shader.h include/native/directx
cp %{mingw64_includedir}/d3d12.h include/native/directx
cp %{mingw64_includedir}/d3d12sdklayers.h include/native/directx
cp %{mingw64_includedir}/d3d12shader.h include/native/directx
cp %{mingw64_includedir}/d3d8caps.h include/native/directx
cp %{mingw64_includedir}/d3d8.h include/native/directx
cp %{mingw64_includedir}/d3d8types.h include/native/directx
cp %{mingw64_includedir}/d3d9caps.h include/native/directx
cp %{mingw64_includedir}/d3d9.h include/native/directx
cp %{mingw64_includedir}/d3d9types.h include/native/directx
cp %{mingw64_includedir}/d3dcaps.h include/native/directx
cp %{mingw64_includedir}/d3dcommon.h include/native/directx
cp %{mingw64_includedir}/d3dcompiler.h include/native/directx
cp %{mingw64_includedir}/d3d.h include/native/directx
cp %{mingw64_includedir}/d3dhal.h include/native/directx
cp %{mingw64_includedir}/d3drmdef.h include/native/directx
cp %{mingw64_includedir}/d3drm.h include/native/directx
cp %{mingw64_includedir}/d3drmobj.h include/native/directx
cp %{mingw64_includedir}/d3dtypes.h include/native/directx
cp %{mingw64_includedir}/d3dvec.inl include/native/directx
cp %{mingw64_includedir}/d3dx9anim.h include/native/directx
cp %{mingw64_includedir}/d3dx9core.h include/native/directx
cp %{mingw64_includedir}/d3dx9effect.h include/native/directx
cp %{mingw64_includedir}/d3dx9.h include/native/directx
cp %{mingw64_includedir}/d3dx9math.h include/native/directx
cp %{mingw64_includedir}/d3dx9math.inl include/native/directx
cp %{mingw64_includedir}/d3dx9mesh.h include/native/directx
cp %{mingw64_includedir}/d3dx9shader.h include/native/directx
cp %{mingw64_includedir}/d3dx9shape.h include/native/directx
cp %{mingw64_includedir}/d3dx9tex.h include/native/directx
cp %{mingw64_includedir}/d3dx9xof.h include/native/directx
cp %{mingw64_includedir}/dxdiag.h include/native/directx
cp %{mingw64_includedir}/dxerr8.h include/native/directx
cp %{mingw64_includedir}/dxerr9.h include/native/directx
cp %{mingw64_includedir}/dxfile.h include/native/directx
cp %{mingw64_includedir}/dxgi1_2.h include/native/directx
cp %{mingw64_includedir}/dxgi1_3.h include/native/directx
cp %{mingw64_includedir}/dxgi1_4.h include/native/directx
cp %{mingw64_includedir}/dxgi1_5.h include/native/directx
cp %{mingw64_includedir}/dxgi1_6.h include/native/directx
cp %{mingw64_includedir}/dxgicommon.h include/native/directx
cp %{mingw64_includedir}/dxgidebug.h include/native/directx
cp %{mingw64_includedir}/dxgiformat.h include/native/directx
cp %{mingw64_includedir}/dxgi.h include/native/directx
cp %{mingw64_includedir}/dxgitype.h include/native/directx
cp %{mingw64_includedir}/dxtmpl.h include/native/directx
cp %{mingw64_includedir}/dxva2api.h include/native/directx
cp %{mingw64_includedir}/dxva.h include/native/directx
cp %{mingw64_includedir}/dxvahd.h include/native/directx
cp %{mingw64_includedir}/_mingw_unicode.h include/native/directx

%build
%meson -Dbuild_id=true
%meson_build


%install
%meson_install

# Install headers
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -a include/native %{buildroot}%{_includedir}/%{name}

# Install pkgconfig files
mkdir -p %{buildroot}%{_libdir}/pkgconfig

# Install dxvk-native-d3d9 pc file
sed -e "s:@prefix@:%{_prefix}:g" \
    -e "s:@libdir@:%{_libdir}:g" \
    -e "s:@includedir@:%{_includedir}/%{name}:g" \
    -e "s:@PACKAGE_VERSION@:%{version}:g" \
    -e "s:@D3DVER@:9:g" \
    %{SOURCE1} > %{buildroot}%{_libdir}/pkgconfig/%{name}-d3d9.pc

# Install dxvk-native-d3d10 pc file
sed -e "s:@prefix@:%{_prefix}:g" \
    -e "s:@libdir@:%{_libdir}:g" \
    -e "s:@includedir@:%{_includedir}/%{name}:g" \
    -e "s:@PACKAGE_VERSION@:%{version}:g" \
    -e "s:@D3DVER@:10core:g" \
    %{SOURCE1} > %{buildroot}%{_libdir}/pkgconfig/%{name}-d3d10.pc

# Install dxvk-native-d3d11 pc file
sed -e "s:@prefix@:%{_prefix}:g" \
    -e "s:@libdir@:%{_libdir}:g" \
    -e "s:@includedir@:%{_includedir}/%{name}:g" \
    -e "s:@PACKAGE_VERSION@:%{version}:g" \
    -e "s:@D3DVER@:11:g" \
    %{SOURCE1} > %{buildroot}%{_libdir}/pkgconfig/%{name}-d3d11.pc

%files
%license LICENSE
%doc README.md
# The libraries are ABI stable and match Windows conventions
%{_libdir}/libdxvk_d3d9.so
%{_libdir}/libdxvk_d3d10core.so
%{_libdir}/libdxvk_d3d11.so
%{_libdir}/libdxvk_dxgi.so


%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}/


%changelog
* Fri Jan 26 2024 Ethan Lee <flibitijibibo@gmail.com> - 2.3-1
- Update to 2.3

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 17 2022 Neal Gompa <ngompa@fedoraproject.org> - 1.9.2a-1
- Update to 1.9.2a

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 13 2021 Neal Gompa <ngompa@fedoraproject.org> - 1.9.1a-1
- Initial package for Fedora (#2010139)

* Tue Oct 12 2021 Neal Gompa <ngompa@fedoraproject.org> - 1.9.1a-0.2
- Update license tag to include header licenses
- Add pkgconfig files

* Tue Aug 31 2021 Neal Gompa <ngompa@fedoraproject.org> - 1.9.1a-0.1
- Initial package
