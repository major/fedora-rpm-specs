# Git submodules
#   * wf-utils
%global commit1 889fdafa7b09fc6ce70313fd3f067cfc8c21a2ac
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

#   * wf-touch
%global commit2 8974eb0f6a65464b63dd03b842795cb441fb6403
%global shortcommit2 %(c=%{commit2}; echo ${c:0:7})

Name:           wayfire
Version:        0.7.4
Release:        %autorelease
Summary:        3D wayland compositor

License:        MIT
URL:            https://github.com/WayfireWM/wayfire
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/WayfireWM/wf-utils/archive/%{commit1}/wf-utils-%{shortcommit1}.tar.gz
Source2:        https://github.com/WayfireWM/wf-touch/archive/%{commit2}/wf-touch-%{shortcommit2}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  inotify-tools-devel
BuildRequires:  libevdev-devel
BuildRequires:  meson >= 0.53.0

BuildRequires:  cmake(doctest)
BuildRequires:  cmake(glm)

BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput) >= 1.7.0
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.12
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wf-config) >= 0.7.0
BuildRequires:  pkgconfig(wlroots) >= 0.15.0
BuildRequires:  pkgconfig(xkbcommon)

Recommends:     wayfire-config-manager
Recommends:     wf-shell

Provides:       bundled(wf-touch) = 0.0~git%{commit2}
Provides:       bundled(wf-utils) = 0.0~git%{commit1}

%description
Wayfire is a wayland compositor based on wlroots. It aims to create a
customizable, extendable and lightweight environment without sacrificing its
appearance.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.


%prep
%autosetup -p1
%autosetup -D -T -a1
%autosetup -D -T -a2
mv wf-utils-%{commit1}/* subprojects/wf-utils/
mv wf-touch-%{commit2}/* subprojects/wf-touch/


%build
%meson                            \
    -Duse_system_wfconfig=enabled \
    -Duse_system_wlroots=enabled  \
    %{nil}
%meson_build


%install
%meson_install
install -Dpm0644 %{name}.desktop %{buildroot}%{_datadir}/wayland-sessions/%{name}.desktop
rm -f %{buildroot}%{_libdir}/libwftouch.a


%files
%license LICENSE
%doc README.md %{name}.ini
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/wayland-sessions/*.desktop
%{_libdir}/%{name}/
%{_libdir}/libwf-utils.so.0*

%files devel
%{_libdir}/libwf-utils.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}/


%changelog
%autochangelog
