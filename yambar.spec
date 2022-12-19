%define bcond_feature() %{lua:do
    local name = rpm.expand("%{1}")
    local value = rpm.expand("%{?with_" .. name:gsub('-', '_') .. "}")
    print(value ~= '' and "enabled" or "disabled")
end}

%bcond_without  backend_wayland
%bcond_without  backend_x11

Name:           yambar
Version:        1.9.0
Release:        1%{?dist}
Summary:        Modular status panel for X11 and Wayland

# The main source is MIT
# The bundled wayland protocol files:
#   external/river-status-unstable-v1.xml: ISC
#   external/wlr-foreign-toplevel-management-unstable-v1.xml: HPND-sell-variant
#   external/wlr-layer-shell-unstable-v1.xml: HPND-sell-variant
# Those files are processed to C-compilable files by the
# `wayland-scanner` binary during build and don't alter
# the main license of the binaries linking with them by
# the underlying licenses.
License:        MIT
URL:            https://codeberg.org/dnkl/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  meson >= 0.59

BuildRequires:  pkgconfig(fcft) >= 3.0.0
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(tllist) >= 1.0.1
BuildRequires:  pkgconfig(yaml-0.1)
# require *-static for header-only library
BuildRequires:  tllist-static
%if %{with backend_wayland}
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
%endif
%if %{with backend_x11}
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-render)
# XKB plugin
BuildRequires:  pkgconfig(xcb-xkb)
%endif
# modules
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)

%description
yambar is a lightweight and configurable status panel (bar, for short)
for X11 and Wayland, that goes to great lengths to be both CPU and
battery efficient - polling is only done when absolutely necessary.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains header files for developing
applications and plugins for %{name}.


%prep
%autosetup -n %{name}
chmod -x examples/scripts/*


%build
%meson \
    -Dbackend-wayland=%{bcond_feature backend-wayland} \
    -Dbackend-x11=%{bcond_feature backend-x11} \
    -Dplugin-xkb=%{bcond_feature backend-x11}
%meson_build


%install
%meson_install
# Will be installed to correct location with rpm macros
rm %{buildroot}%{_docdir}/%{name}/LICENSE


%check
%meson_test
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%doc README.md examples/*
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}*.5*

%files devel
%{_includedir}/%{name}

%changelog
* Sat Dec 17 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0 (#2154516)
- Add bcond for backends
- Convert License tag to SPDX

* Fri Aug 26 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.8.0-1
- Initial import (#2051066)
