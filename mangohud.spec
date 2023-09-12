%global appname MangoHud

%global imgui_ver 1.81
%global imgui_wrap_ver 1
%global vulkan_headers_ver 1.2.158
%global vulkan_headers_wrap_ver 1

# Failed on s390x arch
# [  ERROR   ] --- 0x4000 != 0x40
# [   LINE   ] --- ../tests/test_amdgpu.cpp:35: error: Failure!
# [  FAILED  ] amdgpu_tests: 1 test(s), listed below:
# [  FAILED  ] test_amdgpu_get_instant_metrics
%ifnarch s390x
%bcond_without tests
%endif

Name:           mangohud
Version:        0.6.9.1
Release:        %autorelease
Summary:        Vulkan overlay layer for monitoring FPS, temperatures, CPU/GPU load and more

License:        MIT
URL:            https://github.com/flightlessmango/MangoHud
Source0:        %{url}/archive/v0.6.9-1/%{name}-%{version}.tar.gz
# imgui
Source1:        https://github.com/ocornut/imgui/archive/v%{imgui_ver}/imgui-%{imgui_ver}.tar.gz
Source2:        https://wrapdb.mesonbuild.com/v%{imgui_wrap_ver}//projects/imgui/%{imgui_ver}/%{imgui_wrap_ver}/get_zip#/imgui-%{imgui_ver}-%{imgui_wrap_ver}-wrap.zip
# Vulkan-Headers
Source3:        https://github.com/KhronosGroup/Vulkan-Headers/archive/v%{vulkan_headers_ver}/Vulkan-Headers-%{vulkan_headers_ver}.tar.gz
Source4:        https://wrapdb.mesonbuild.com/v%{vulkan_headers_wrap_ver}/projects/vulkan-headers/%{vulkan_headers_ver}/%{vulkan_headers_wrap_ver}/get_zip#/vulkan-headers-%{vulkan_headers_ver}-%{vulkan_headers_wrap_ver}-wrap.zip

# MangoHud switched to bundled vulkan-headers since 0.6.9 version. This rebased
# upstream patch which reverts this change.
# https://github.com/flightlessmango/MangoHud/commit/bc282cf300ed5b6831177cf3e6753bc20f48e942
# Patch0:         mangohud-0.6.9-use-system-vulkan-headers.patch

# GCC 13 fix
# params: add cstdint header
# https://github.com/flightlessmango/MangoHud/commit/3f8f036ee8773ae1af23dd0848b6ab487b5ac7de
Patch1:         https://github.com/flightlessmango/MangoHud/commit/3f8f036ee8773ae1af23dd0848b6ab487b5ac7de.patch#/params:-add-cstdint-header.patch

# https://github.com/flightlessmango/MangoHud/commit/5754ca13ee2cdf19a76b4fc79dd914a58d6371f5
# vulkan manifest: set cpu_family in layer name 
Patch2:         https://github.com/flightlessmango/MangoHud/commit/5754ca13ee2cdf19a76b4fc79dd914a58d6371f5.patch#/vulkan-manifest:-set-cpu_family-in-layer-name.patch

BuildRequires:  appstream
BuildRequires:  dbus-devel
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  glew-devel
BuildRequires:  glfw-devel
BuildRequires:  glslang-devel
BuildRequires:  libappstream-glib
BuildRequires:  mesa-libGL-devel
BuildRequires:  meson >= 0.60
BuildRequires:  python3-mako
BuildRequires:  spdlog-devel

BuildRequires:  pkgconfig(nlohmann_json)
# Tip and memo if upstream decide to unbundle vulkan-headers
# BuildRequires:  pkgconfig(vulkan) < 1.3.241
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)

%if %{with tests}
BuildRequires:  libcmocka-devel
%endif

Requires:       hicolor-icon-theme
Requires:       vulkan-loader%{?_isa}

Recommends:     (mangohud(x86-32) if glibc(x86-32))

Suggests:       goverlay

Provides:       bundled(imgui) = %{imgui_ver}
Provides:       bundled(vulkan-headers) = %{vulkan_headers_ver}

%global _description %{expand:
A modification of the Mesa Vulkan overlay. Including GUI improvements,
temperature reporting, and logging capabilities.

To install GUI front-end:

  # dnf install goverlay}

%description %{_description}


%prep
%autosetup -n %{appname}-0.6.9-1 -p1
%setup -qn %{appname}-0.6.9-1 -D -T -a1
%setup -qn %{appname}-0.6.9-1 -D -T -a2
%setup -qn %{appname}-0.6.9-1 -D -T -a3
%setup -qn %{appname}-0.6.9-1 -D -T -a4

# imgui
mv imgui-%{imgui_ver} subprojects/
# Vulkan-Headers
mv Vulkan-Headers-%{vulkan_headers_ver} subprojects/

%if %{with tests}
# Use system cmocka instead of subproject
# https://gitlab.archlinux.org/archlinux/packaging/packages/mangohud/-/blob/0.6.9.1-10/PKGBUILD?ref_type=tags#L32
sed -i "s/  cmocka = subproject('cmocka')//g" meson.build
sed -i "s/cmocka_dep = cmocka.get_variable('cmocka_dep')/cmocka_dep = dependency('cmocka')/g" meson.build
%endif


%build
%meson \
    -Dinclude_doc=true \
    -Duse_system_spdlog=enabled \
    -Dwith_wayland=enabled \
    -Dwith_xnvctrl=disabled \
    %if %{with tests}
    -Dtests=enabled \
    %else
    -Dtests=disabled \
    %endif
    %{nil}
%meson_build


%install
%meson_install


%check
# https://github.com/flightlessmango/MangoHud/issues/812
# ? tag-invalid           : stock icon is not valid [io.github.flightlessmango.mangohud]
%dnl appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
%if %{with tests}
%meson_test
%endif


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}*
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/vulkan/implicit_layer.d/*Mango*.json
%{_docdir}/%{name}/%{appname}.conf.example
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/*.metainfo.xml


%changelog
%autochangelog
