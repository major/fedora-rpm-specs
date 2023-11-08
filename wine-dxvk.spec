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
Release:        %autorelease
Summary:        Vulkan-based D3D11 and D3D10 implementation for Linux / Wine

License:        zlib
URL:            https://github.com/doitsujin/dxvk
Source0:        %{url}/archive/v%{version}/dxvk-%{version}.tar.gz

# Apply fixes from git/1.10.x released after 1.10.3 till 2nd of Aug 2023
Patch01:        postrel_fixxes.patch

# GCC 13 buildfixes
# https://github.com/doitsujin/dxvk/pull/3308
Patch02:        3308.patch

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
%autosetup -n dxvk-%{version} -p1

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

%posttrans dxgi
if vulkaninfo |& grep "ERROR_INITIALIZATION_FAILED\|ERROR_SURFACE_LOST_KHR\|Vulkan support is incomplete" > /dev/null; then
    %{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedir}/dxgi.dll 'wine-dxgi%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-dxgi.dll 5
else
    %{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedir}/dxgi.dll 'wine-dxgi%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-dxgi.dll 5
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

%postun dxgi
%{_sbindir}/alternatives --remove 'wine-dxgi%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-dxgi.dll

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
%autochangelog
