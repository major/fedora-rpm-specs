%global debug_package %{nil}
%{?mingw_package_header}

%global libdisplay_commit 275e6459c7ab1ddd4b125f28d0440716e4888078
%global libdisplay_shortcommit %(c=%{libdisplay_commit}; echo ${c:0:7})

%global winepedir x86_64-windows
%global target_x86_type 64
%global mingw_sysroot %mingw64_sysroot
%global mingw_build_win64 1
%global mingw_build_win32 0

Name:           wine-dxvk
Version:        2.7.1
Release:        %autorelease
Summary:        Vulkan-based implementation of D3D8, 9, 10 and 11 for Linux / Wine

License:        zlib AND MIT
URL:            https://github.com/doitsujin/dxvk
Source0:        %{url}/archive/v%{version}/dxvk-%{version}.tar.gz
Source1:        https://gitlab.freedesktop.org/frog/libdisplay-info/-/archive/%{libdisplay_commit}/libdisplay-info-%{libdisplay_shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glslang
BuildRequires:  meson
BuildRequires:  wine-devel

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-headers
BuildRequires:  mingw64-cpp
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-winpthreads-static
BuildRequires:  mingw64-vulkan-headers
BuildRequires:  mingw64-spirv-headers

Requires(pre):  vulkan-tools

Requires:       wine-core%{?_isa}
Requires:       wine-dxvk-dxgi%{?_isa} = %{version}-%{release}
Requires:       vulkan-loader%{?_isa}

Obsoletes:      wine-dxvk.i686 <= 2.6.2-1

# Recommend also d3d8, d3d9, and d3d10
Recommends:     wine-dxvk-d3d8%{?_isa}  = %{version}-%{release}
Recommends:     wine-dxvk-d3d9%{?_isa}  = %{version}-%{release}
Recommends:     wine-dxvk-d3d10%{?_isa} = %{version}-%{release}

Requires(posttrans):   %{_sbindir}/alternatives wine-core%{?_isa}
Requires(preun):       %{_sbindir}/alternatives

ExclusiveArch:  x86_64

Provides:       bundled(libdisplay-info) = 0.3.0~dev^git%{libdisplay_shortcommit}

%description
%{summary}

%package dxgi
Summary:        DXVK DXGI implementation

Obsoletes:      wine-dxvk-dxgi.i686 <= 2.6.2-1

%description dxgi
%{summary}

This package doesn't enable the use of this DXGI implementation,
it should be installed and overridden per prefix.

%package d3d10
Summary:        DXVK D3D10 implementation

Requires:       wine-dxvk%{?_isa} = %{version}-%{release}

Obsoletes:      wine-dxvk-d3d10.i686 <= 2.6.2-1

%description d3d10
%{summary}

%package d3d9
Summary:        DXVK D3D9 implementation

Requires:       wine-dxvk%{?_isa} = %{version}-%{release}

Obsoletes:      wine-dxvk-d3d9.i686 <= 2.6.2-1

%description d3d9
%{summary}

%package d3d8
Summary:        DXVK D3D8 implementation

Requires:       wine-dxvk%{?_isa} = %{version}-%{release}

Obsoletes:      wine-dxvk-d3d8.i686 <= 2.6.2-1

%description d3d8
%{summary}

%prep
%autosetup -n dxvk-%{version} -p1 -a1
rm -rf subprojects/libdisplay-info && mv libdisplay-info-%{libdisplay_commit} subprojects/libdisplay-info

%build
%mingw_meson --buildtype=plain --wrap-mode=nodownload --auto-features=enabled --cross-file ../build-win%{target_x86_type}.txt --buildtype release
%mingw_ninja

%install
%mingw_ninja_install
winebuild --builtin %buildroot%mingw_sysroot/mingw/bin/dxgi.dll
winebuild --builtin %buildroot%mingw_sysroot/mingw/bin/d3d8.dll
winebuild --builtin %buildroot%mingw_sysroot/mingw/bin/d3d9.dll
winebuild --builtin %buildroot%mingw_sysroot/mingw/bin/d3d10core.dll
winebuild --builtin %buildroot%mingw_sysroot/mingw/bin/d3d11.dll

mkdir -p %{buildroot}%{_libdir}/wine/%{winepedir}/
install -p -m 644 %buildroot%mingw_sysroot/mingw/bin/dxgi.dll %{buildroot}%{_libdir}/wine/%{winepedir}/dxvk-dxgi.dll
install -p -m 644 %buildroot%mingw_sysroot/mingw/bin/d3d8.dll %{buildroot}%{_libdir}/wine/%{winepedir}/dxvk-d3d8.dll
install -p -m 644 %buildroot%mingw_sysroot/mingw/bin/d3d9.dll %{buildroot}%{_libdir}/wine/%{winepedir}/dxvk-d3d9.dll
install -p -m 644 %buildroot%mingw_sysroot/mingw/bin/d3d10core.dll %{buildroot}%{_libdir}/wine/%{winepedir}/dxvk-d3d10core.dll
install -p -m 644 %buildroot%mingw_sysroot/mingw/bin/d3d11.dll %{buildroot}%{_libdir}/wine/%{winepedir}/dxvk-d3d11.dll

# Clean-up
rm -rf %buildroot%mingw_sysroot/mingw

%posttrans
if vulkaninfo |& grep "ERROR_INITIALIZATION_FAILED\|ERROR_SURFACE_LOST_KHR\|Vulkan support is incomplete" > /dev/null; then
    %{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedir}/d3d11.dll 'wine-d3d11%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d11.dll 5
else
    %{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedir}/d3d11.dll 'wine-d3d11%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d11.dll 20
fi

%posttrans dxgi
if vulkaninfo |& grep "ERROR_INITIALIZATION_FAILED\|ERROR_SURFACE_LOST_KHR\|Vulkan support is incomplete" > /dev/null; then
    %{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedir}/dxgi.dll 'wine-dxgi%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-dxgi.dll 5
else
    %{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedir}/dxgi.dll 'wine-dxgi%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-dxgi.dll 20
fi

%posttrans d3d10
if vulkaninfo |& grep "ERROR_INITIALIZATION_FAILED\|ERROR_SURFACE_LOST_KHR\|Vulkan support is incomplete" > /dev/null; then
    %{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedir}/d3d10core.dll 'wine-d3d10core%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d10core.dll 5
else
    %{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedir}/d3d10core.dll 'wine-d3d10core%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d10core.dll 20
fi

%posttrans d3d9
if vulkaninfo |& grep "ERROR_INITIALIZATION_FAILED\|ERROR_SURFACE_LOST_KHR\|Vulkan support is incomplete" > /dev/null; then
    %{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedir}/d3d9.dll 'wine-d3d9%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d9.dll 5
else
    %{_sbindir}/alternatives --install %{_libdir}/wine/%{winepedir}/d3d9.dll 'wine-d3d9%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d9.dll 20
fi

%postun
%{_sbindir}/alternatives --remove 'wine-d3d11%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d11.dll

%postun d3d10
%{_sbindir}/alternatives --remove 'wine-d3d10core%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d10core.dll

%postun d3d9
%{_sbindir}/alternatives --remove 'wine-d3d9%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-d3d9.dll

%postun dxgi
%{_sbindir}/alternatives --remove 'wine-dxgi%{?_isa}' %{_libdir}/wine/%{winepedir}/dxvk-dxgi.dll

%files
%license LICENSE
%doc README.md
%{_libdir}/wine/%{winepedir}/dxvk-d3d11.dll

%files d3d10
%license LICENSE
%{_libdir}/wine/%{winepedir}/dxvk-d3d10core.dll

%files d3d9
%license LICENSE
%{_libdir}/wine/%{winepedir}/dxvk-d3d9.dll

%files d3d8
%license LICENSE
%{_libdir}/wine/%{winepedir}/dxvk-d3d8.dll

%files dxgi
%license LICENSE
%{_libdir}/wine/%{winepedir}/dxvk-dxgi.dll

%changelog
%autochangelog
