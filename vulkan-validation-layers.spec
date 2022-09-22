Name:           vulkan-validation-layers
Version:        1.3.224.0
Release:        1%{?dist}
Summary:        Vulkan validation layers

License:        ASL 2.0
URL:            https://github.com/KhronosGroup/Vulkan-ValidationLayers
Source0:        %url/archive/sdk-%{version}.tar.gz#/Vulkan-ValidationLayers-sdk-%{version}.tar.gz
Patch0:         fix_shared.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  glslang-devel
BuildRequires:  ninja-build
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  spirv-tools-devel
BuildRequires:  spirv-headers-devel
BuildRequires:  vulkan-loader-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xcb)

%description
Vulkan validation layers

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       vulkan-headers

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n Vulkan-ValidationLayers-sdk-%{version}


%build
# Decrease debuginfo verbosity to reduce memory consumption even more
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%global optflags %(echo %{optflags} | sed 's/-O2 /-O1 /')

%cmake3 -DCMAKE_BUILD_TYPE=Release \
        -DGLSLANG_INSTALL_DIR=%{_prefix} \
        -DBUILD_LAYER_SUPPORT_FILES:BOOL=ON \
        -DUSE_ROBIN_HOOD_HASHING:BOOL=OFF \
        -DSPIRV_HEADERS_INCLUDE_DIR=%{_includedir} \
        -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/vulkan/
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets


%files
%license LICENSE.txt
%doc README.md CONTRIBUTING.md LAYER_CONFIGURATION.md
%{_datadir}/vulkan/explicit_layer.d/*.json
%{_libdir}/libVkLayer_*.so

%files devel
%{_includedir}/vulkan/

%changelog
* Wed Aug 24 2022 Dave Airlie <airlied@redhat.com> - 1.3.224.0-1
- Update to latest 1.3.224.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.216.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Dave Airlie <airlied@redhat.com> - 1.3.216.0-1
- Update to latest 1.3.216.0

* Wed Apr 27 2022 Dave Airlie <airlied@redhat.com> - 1.3.211.0-1
- Update to latest 1.3.211.0

* Wed Feb 16 2022 Dave Airlie <airlied@redhat.com> - 1.3.204.0-1
- Update to latest 1.3.204.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.198.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 10 2021 Dave Airlie <airlied@redhat.com> - 1.2.198.0-3
- build against new spirv-tools

* Thu Dec 09 2021 Dave Airlie <airlied@redhat.com> - 1.2.198.0-2
- fix ABI issue with spirv-tools

* Tue Nov 23 2021 Dave Airlie <airlied@redhat.com> - 1.2.198.0-1
- Update to latest 1.2.198.0

* Wed Sep 08 2021 Dave Airlie <airlied@redhat.com> - 1.2.189.0-1
- Update to latest 1.2.189.0

* Sat Aug 07 2021 Dave Airlie <airlied@redhat.com> - 1.2.182.0-3
- fix validation layers missing export

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.182.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Dave Airlie <airlied@redhat.com> - 1.2.182.0-1
- Update to latest 1.2.182.0 release

* Tue May 18 2021 Dave Airlie <airlied@redhat.com> - 1.2.176.1-1
- Update to latest 1.2.176.1 release

* Fri Jan 29 2021 Dave Airlie <airlied@redhat.com> - 1.2.162.0-1
- Update to latest 1.2.162.0 release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.154.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Adam Jackson <ajax@redhat.com> - 1.2.154.0-2
- Add LAYER_CONFIGURATION.md to the docs

* Wed Nov 04 2020 Dave Airlie <airlied@redhat.com> - 1.2.154.0-1
- Update to 1.2.154.0

* Wed Aug 05 2020 Dave Airlie <airlied@redhat.com> - 1.2.148.0-1
- Update to 1.2.148.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.135.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.135.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Dave Airlie <airlied@redhat.com> - 1.2.135.0-1
- Update validation layers to 1.2.135.0

* Wed Jan 29 2020 Dave Airlie <airlied@redhat.com> - 1.2.131.1-1
- Update validation layers to 1.2.131.1

* Wed Nov 13 2019 Dave Airlie <airlied@redhat.com> - 1.1.126.0-1
- Update validation layers to 1.1.126.0

* Wed Jul 31 2019 Dave Airlie <airlied@redhat.com> - 1.1.114.0-1
- Update validation layers to 1.1.114.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.108.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Dave Airlie <airlied@redhat.com> - 1.1.108.0-1
- Update valdiation layers to 1.1.108.0

* Wed Mar 06 2019 Dave Airlie <airlied@redhat.com> - 1.1.101.0-1
- Update valdiation layers to 1.1.101.0

* Wed Feb 13 2019 Dave Airlie <airlied@redhat.com> - 1.1.97.0-1
- Update validation layers to 1.1.97.0

* Wed Feb 13 2019 Dave Airlie <airlied@redhat.com> - 1.1.92.0-1
- Update validation layers to 1.1.92.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.82.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.82.0-1
- Update to 1.1.82.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.77.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.77.0-3
- Workaround i686 build issue

* Tue Jun 26 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.77.0-2
- Exclude i686 due to 'virtual memory exhausted' FTBFS

* Sat Jun 23 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.77.0-1
- Initial package
