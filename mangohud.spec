%global appname MangoHud

%global imgui_ver       1.81
%global imgui_wrap_ver  1

Name:           mangohud
Version:        0.6.8
Release:        %autorelease
Summary:        Vulkan overlay layer for monitoring FPS, temperatures, CPU/GPU load and more

License:        MIT
URL:            https://github.com/flightlessmango/MangoHud
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/ocornut/imgui/archive/v%{imgui_ver}/imgui-%{imgui_ver}.tar.gz
Source2:        https://wrapdb.mesonbuild.com/v1/projects/imgui/%{imgui_ver}/%{imgui_wrap_ver}/get_zip#/imgui-%{imgui_ver}-%{imgui_wrap_ver}-wrap.zip

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

BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)

Requires:       hicolor-icon-theme
Requires:       vulkan-loader%{?_isa}

Recommends:     (mangohud(x86-32) if glibc(x86-32))

Suggests:       goverlay

Provides:       bundled(imgui) = %{imgui_ver}

%global _description %{expand:
A modification of the Mesa Vulkan overlay. Including GUI improvements,
temperature reporting, and logging capabilities.

To install GUI front-end:

  # dnf install goverlay}

%description %{_description}


%prep
%autosetup -n %{appname}-%{version} -p1
%autosetup -n %{appname}-%{version} -DTa1
%autosetup -n %{appname}-%{version} -DTa2

mkdir subprojects/imgui
mv imgui-%{imgui_ver}/* subprojects/imgui/


%build
%meson \
    -Dinclude_doc=true \
    -Duse_system_spdlog=enabled \
    -Duse_system_vulkan=enabled \
    -Dwith_xnvctrl=disabled \
    %{nil}
%meson_build


%install
%meson_install


%check
# https://github.com/flightlessmango/MangoHud/issues/812
%dnl appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml


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
