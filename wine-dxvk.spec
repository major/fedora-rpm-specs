%global debug_package %{nil}
%{?mingw_package_header}

%ifarch x86_64
%global winepedir x86_64-windows
%global target_x86_type 64
%global mingw_sysroot %mingw64_sysroot
%global mingw_build_win64 1
%global mingw_build_win32 0
%else
%global winepedir i386-windows
%global target_x86_type 32
%global mingw_sysroot %mingw32_sysroot
%global mingw_build_win64 0
%global mingw_build_win32 1
%endif

Name:           wine-dxvk
Version:        1.10.3
Release:        1%{?dist}
Summary:        Vulkan-based D3D11 and D3D10 implementation for Linux / Wine

License:        zlib
URL:            https://github.com/doitsujin/dxvk
Source0:        %{url}/archive/v%{version}/dxvk-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glslang
BuildRequires:  meson
BuildRequires:  wine-devel

%ifarch x86_64
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-headers
BuildRequires:  mingw64-cpp
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-winpthreads-static
%else
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-headers
BuildRequires:  mingw32-cpp
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-winpthreads-static
%endif

Requires(pre):  vulkan-tools

Requires:       wine-core%{?_isa} >= 6.8
Recommends:     wine-dxvk-dxgi%{?_isa} = %{version}-%{release}
Requires:       vulkan-loader%{?_isa}

# We want x86_64 users to always have also 32 bit lib, it's the same what wine does
%ifarch x86_64
Requires:       wine-dxvk(x86-32) = %{version}-%{release}
%endif

# Recommend also the d3d9 (former D9VK)
Recommends:     wine-dxvk-d3d9%{?_isa} = %{version}-%{release}

Requires(posttrans):   %{_sbindir}/alternatives wine-core%{?_isa} >= 6.8
Requires(preun):       %{_sbindir}/alternatives

ExclusiveArch:  %{ix86} x86_64

%description
%{summary}

%package dxgi
Summary:        DXVK DXGI implementation
%ifarch x86_64
Requires:       wine-dxvk-dxgi(x86-32) = %{version}-%{release}
%endif

%description dxgi
%{summary}

This package doesn't enable the use of this DXGI implementation,
it should be installed and overridden per prefix.

%package d3d9
Summary:        DXVK D3D9 implementation

Requires:       wine-dxvk%{?_isa} = %{version}-%{release}

# We want x86_64 users to always have also 32 bit lib, it's the same what wine does
%ifarch x86_64
Requires:       wine-dxvk-d3d9(x86-32) = %{version}-%{release}
%endif

%description d3d9
%{summary}

%prep
%setup -q -n dxvk-%{version}

%build
%mingw_meson --buildtype=plain --wrap-mode=nodownload --auto-features=enabled --cross-file ../build-win%{target_x86_type}.txt --buildtype release
%mingw_ninja

%install
%mingw_ninja_install
winebuild --builtin %buildroot%mingw_sysroot/mingw/bin/dxgi.dll
winebuild --builtin %buildroot%mingw_sysroot/mingw/bin/d3d9.dll
winebuild --builtin %buildroot%mingw_sysroot/mingw/bin/d3d10.dll
winebuild --builtin %buildroot%mingw_sysroot/mingw/bin/d3d10core.dll
winebuild --builtin %buildroot%mingw_sysroot/mingw/bin/d3d10_1.dll
winebuild --builtin %buildroot%mingw_sysroot/mingw/bin/d3d11.dll

mkdir -p %{buildroot}%{_libdir}/wine/%{winepedir}/
install -p -m 644 %buildroot%mingw_sysroot/mingw/bin/dxgi.dll %{buildroot}%{_libdir}/wine/%{winepedir}/dxvk-dxgi.dll
install -p -m 644 %buildroot%mingw_sysroot/mingw/bin/d3d9.dll %{buildroot}%{_libdir}/wine/%{winepedir}/dxvk-d3d9.dll
install -p -m 644 %buildroot%mingw_sysroot/mingw/bin/d3d10.dll %{buildroot}%{_libdir}/wine/%{winepedir}/dxvk-d3d10.dll
install -p -m 644 %buildroot%mingw_sysroot/mingw/bin/d3d10core.dll %{buildroot}%{_libdir}/wine/%{winepedir}/dxvk-d3d10core.dll
install -p -m 644 %buildroot%mingw_sysroot/mingw/bin/d3d10_1.dll %{buildroot}%{_libdir}/wine/%{winepedir}/dxvk-d3d10_1.dll
install -p -m 644 %buildroot%mingw_sysroot/mingw/bin/d3d11.dll %{buildroot}%{_libdir}/wine/%{winepedir}/dxvk-d3d11.dll

# Clean-up
rm -rf %buildroot%mingw_sysroot/mingw

%posttrans
if vulkaninfo |& grep "ERROR_INITIALIZATION_FAILED\|ERROR_SURFACE_LOST_KHR\|Vulkan support is incomplete" > /dev/null; then
    %{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedir}/d3d10.dll 'wine-d3d10%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d10.dll 5 \
    --slave %{_libdir}/wine/%{winepedir}/d3d10_1.dll 'wine-d3d10_1%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d10_1.dll \
    --slave %{_libdir}/wine/%{winepedir}/d3d10core.dll 'wine-d3d10core%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d10core.dll
    %{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedir}/d3d11.dll 'wine-d3d11%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d11.dll 5
else
    %{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedir}/d3d10.dll 'wine-d3d10%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d10.dll 20 \
    --slave %{_libdir}/wine/%{winepedir}/d3d10_1.dll 'wine-d3d10_1%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d10_1.dll \
    --slave %{_libdir}/wine/%{winepedir}/d3d10core.dll 'wine-d3d10core%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d10core.dll
    %{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedir}/d3d11.dll 'wine-d3d11%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d11.dll 20
fi

%posttrans d3d9
if vulkaninfo |& grep "ERROR_INITIALIZATION_FAILED\|ERROR_SURFACE_LOST_KHR\|Vulkan support is incomplete" > /dev/null; then
    %{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedir}/d3d9.dll 'wine-d3d9%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d9.dll 5
else
    %{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedir}/d3d9.dll 'wine-d3d9%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d9.dll 5
fi

%postun
%{_sbindir}/alternatives --remove 'wine-d3d10%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d10.dll
%{_sbindir}/alternatives --remove 'wine-d3d11%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d11.dll

%postun d3d9
%{_sbindir}/alternatives --remove 'wine-d3d9%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d9.dll

%files
%license LICENSE
%doc README.md
%{_libdir}/wine/%{winepedir}/dxvk-d3d10.dll
%{_libdir}/wine/%{winepedir}/dxvk-d3d10_1.dll
%{_libdir}/wine/%{winepedir}/dxvk-d3d10core.dll
%{_libdir}/wine/%{winepedir}/dxvk-d3d11.dll

%files d3d9
%license LICENSE
%{_libdir}/wine/%{winepedir}/dxvk-d3d9.dll

%files dxgi
%license LICENSE
%{_libdir}/wine/%{winepedir}/dxvk-dxgi.dll


%changelog
* Wed Aug 03 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.10.3-1
- Release 1.10.3 (closes RHBZ#2114663)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.10.2-1
- Release 1.10.2

* Sat Apr 02 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.10.1-1
- Release 1.10.1

* Sun Mar 06 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.10-1
- Release 1.10
- Clean up spec file, use mingw build macros

* Mon Jan 31 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.9.4-1
- Release 1.9.4

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.9.3-1
- Release 1.9.3

* Mon Sep 20 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.9.2-1
- Release 1.9.2

* Thu Jul 29 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.9.1-1
- Release 1.9.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.9-1
- Release 1.9

* Fri May 14 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.8.1-2
- Adapt to wine directory structure changes from wine-6.8

* Tue Mar 02 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.8.1-1
- Release 1.8.1

* Mon Feb 22 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.8-1
- Release 1.8

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.7.3-2
- We now have mingw-8.0 in Fedora 34, don't revert IDXGIFactory6 and IDXGIFactory7 in F34

* Sun Jan 17 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.7.3-1
- Release 1.7.3
- Try to blacklist lavapipe driver (hacky solution for now by catching ERROR_SURFACE_LOST_KHR from vulkaninfo)
- Revert IDXGIFactory6 and IDXGIFactory7 changes until we get mingw >= 8.0

* Sun Nov 29 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.7.2-3
- Backout dxvk-d3d9 from the default installation until the issues with vulkan childwindow support are solved

* Sat Nov 14 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.7.2-2
- Blacklist Intel Haswell and Ivy Bridge from default dxvk installation

* Thu Oct 08 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.7.2-1
- Release 1.7.2

* Fri Aug 14 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.7.1-1
- Release 1.7.1

* Sun Aug 09 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.7-3
- Install dxvk as primary alternative only on systems with Vulkan support

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 17 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.7-1
- Release 1.7
- Remove winelib build and fix mingw build dll names (Matias Zuniga)

* Mon Apr 20 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.6.1-1
- Release 1.6.1

* Tue Mar 24 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.6-1
- Release 1.6

* Sat Mar 07 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.5.5-1
- Release 1.5.5

* Sun Feb 09 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.5.4-1
- Release 1.5.4

* Fri Jan 31 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.5.3-1
- Release 1.5.3

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.5.1-1
- Release 1.5.1
- Support D3D9 (wine-dxvk-d3d9 subpackage)

* Sat Dec 07 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.4.6-1
- Release 1.4.6

* Thu Nov 21 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.4.5-1
- Release 1.4.5

* Tue Oct 29 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.4.4-1
- Release 1.4.4

* Sat Oct 19 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.4.3-1
- Release 1.4.3

* Sat Sep 28 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.4.1-1
- Release 1.4.1

* Mon Sep 23 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.4-1
- Release 1.4

* Sun Aug 11 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.3.2-1
- Release 1.3.2
- Use alternatives for .dll files and dxgi.dll.so

* Thu Jul 25 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.3.1-1
- Initial packaging

