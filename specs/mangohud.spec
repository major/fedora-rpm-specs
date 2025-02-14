%global appname MangoHud
%global forgeurl https://github.com/flightlessmango/MangoHud

%global imgui_ver 1.89.9
%global imgui_wrap_ver 2
%global vulkan_headers_ver 1.2.158
%global vulkan_headers_wrap_ver 1
%global implot_ver 0.16
%global implot_wrap_ver 2

%global tarball_version %%(echo %{version} | tr '~' '-')

# TODO: try to fix amdgpu tests
%bcond_with tests

Name:           mangohud
Version:        0.8.0
%forgemeta
Release:        %autorelease
Summary:        Vulkan and OpenGL overlay for monitoring FPS, temperatures, CPU/GPU load

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}
# imgui
Source1:        https://github.com/ocornut/imgui/archive/v%{imgui_ver}/imgui-%{imgui_ver}.tar.gz
Source2: https://wrapdb.mesonbuild.com/v%{imgui_wrap_ver}/imgui_%{imgui_ver}-1/get_patch#/imgui-%{imgui_ver}-%{imgui_wrap_ver}-wrap.zip
# Vulkan-Headers
Source3:        https://github.com/KhronosGroup/Vulkan-Headers/archive/v%{vulkan_headers_ver}/Vulkan-Headers-%{vulkan_headers_ver}.tar.gz
Source4:        https://wrapdb.mesonbuild.com/v%{vulkan_headers_wrap_ver}/projects/vulkan-headers/%{vulkan_headers_ver}/%{vulkan_headers_wrap_ver}/get_zip#/vulkan-headers-%{vulkan_headers_ver}-%{vulkan_headers_wrap_ver}-wrap.zip
# implot
Source5:        https://github.com/epezent/implot/archive/v%{implot_ver}/implot-%{implot_ver}.tar.gz
Source6:        https://wrapdb.mesonbuild.com/v%{implot_wrap_ver}/implot_%{implot_ver}-1/get_patch#/implot-%{implot_ver}-%{implot_wrap_ver}-wrap.zip
Source20:       README.Fedora.md

# MangoHud switched to bundled vulkan-headers since 0.6.9 version. This rebased
# upstream patch which reverts this change.
# https://github.com/flightlessmango/MangoHud/commit/bc282cf300ed5b6831177cf3e6753bc20f48e942
# Patch0:         mangohud-0.6.9-use-system-vulkan-headers.patch
BuildRequires:  vulkan-headers

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
BuildRequires:  pkgconfig(xkbcommon)

%if %{with tests}
BuildRequires:  libcmocka-devel
%endif

Requires:       hicolor-icon-theme
Requires:       vulkan-loader%{?_isa}

Recommends:     (mangohud(x86-32) if glibc(x86-32))

Suggests:       %{name}-mangoplot
Suggests:       goverlay

Provides:       bundled(imgui) = %{imgui_ver}
Provides:       bundled(vulkan-headers) = %{vulkan_headers_ver}

%global _description %{expand:
A Vulkan and OpenGL overlay for monitoring FPS, temperatures, CPU/GPU load and
more.}

%description %{_description}


%package        mangoplot
Summary:        Local visualization "mangoplot" for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Requires:       python3-matplotlib
Requires:       python3-numpy

%description    mangoplot
Local visualization "mangoplot" for %{name}.


%prep
%forgeautosetup -p1
%setup -qn %{appname}-%{tarball_version} -D -T -a1
%setup -qn %{appname}-%{tarball_version} -D -T -a2
%setup -qn %{appname}-%{tarball_version} -D -T -a3
%setup -qn %{appname}-%{tarball_version} -D -T -a4
%setup -qn %{appname}-%{tarball_version} -D -T -a5
%setup -qn %{appname}-%{tarball_version} -D -T -a6

# imgui
mv imgui-%{imgui_ver} subprojects/
# Vulkan-Headers
mv Vulkan-Headers-%{vulkan_headers_ver} subprojects/
# implot
mv implot-%{implot_ver} subprojects/

%if %{with tests}
# Use system cmocka instead of subproject
# https://gitlab.archlinux.org/archlinux/packaging/packages/mangohud/-/blob/0.6.9.1-10/PKGBUILD?ref_type=tags#L32
sed -i "s/  cmocka = subproject('cmocka')//g" meson.build
sed -i "s/cmocka_dep = cmocka.get_variable('cmocka_dep')/cmocka_dep = dependency('cmocka')/g" meson.build
%endif

# https://github.com/flightlessmango/MangoHud/commit/dc1761e98a435aaee6a919e21f43b85cc38500ac
sed -i "s/, '-static-libstdc++'//" \
    src/meson.build


%build
%meson \
    -Dmangoapp=true \
    -Dmangohudctl=true \
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

# ERROR: ambiguous python shebang
sed -i "s@#!/usr/bin/env python@#!/usr/bin/python3@" \
    %{buildroot}%{_bindir}/mangoplot

# Install Fedora docs
install -D -p -m 0644 %{SOURCE20} %{buildroot}%{_docdir}/%{name}/README.Fedora.md


%check
# https://github.com/flightlessmango/MangoHud/issues/812
# ? tag-invalid           : stock icon is not valid [io.github.flightlessmango.mangohud]
%dnl appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
%if %{with tests}
%meson_test
%endif


%files
%license LICENSE
%doc README.md presets.conf.example README.Fedora.md
%{_bindir}/mangoapp
%{_bindir}/mangohud
%{_bindir}/mangohudctl
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/vulkan/implicit_layer.d/*Mango*.json
%{_docdir}/%{name}/%{appname}.conf.example
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/mangoapp.1*
%{_metainfodir}/*.metainfo.xml

%files mangoplot
%{_bindir}/mangoplot


%changelog
%autochangelog
