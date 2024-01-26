Name:           dxvk-native
Version:        1.9.2a
Release:        5%{?dist}
Summary:        Vulkan-based D3D11 and D3D9 implementation for Linux

# Main sources are zlib
## Licenses of customized vendored headers
### Vulkan headers are ASL 2.0
### Wine/ReactOS DX headers are LGPLv2+
### SPIR-V headers are Khronos License (MIT)
### MinGW Windows headers are Public Domain
### Unused OpenVR headers are BSD
License:        zlib and ASL 2.0 and LGPLv2+ and MIT and Public Domain and BSD
URL:            https://github.com/Joshua-Ashton/dxvk-native
Source0:        %{url}/archive/native-%{version}/%{name}-%{version}.tar.gz
# Will hopefully be upstreamed in a different form...
Source1:        dxvk-native.pc.in

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.46
BuildRequires:  glslang
BuildRequires:  SDL2-devel
BuildRequires:  vulkan-loader-devel

Requires:       vulkan-loader%{?_isa}
Requires:       SDL2%{?_isa}

# This is a mangled customized version
Provides:       bundled(vulkan-headers)
# This name is made up, but it is what it is
## Note, this is a slim, customized for this library
Provides:       bundled(wine-d3dheaders)
# This is a mangled customized version
Provides:       bundled(spirv-headers)
# This is a slim, customized version
Provides:       bundled(mingw-headers)

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
%autosetup -n %{name}-native-%{version} -p1


%build
%meson -Denable_tests=true -Dbuild_id=true
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
%{_libdir}/libdxvk_d3d11.so
%{_libdir}/libdxvk_dxgi.so


%files devel
%{_bindir}/%{name}-*
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}/


%changelog
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
