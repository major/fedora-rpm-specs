%global commitdate 20240317
%global commit 0a487d79c0d91f3fd299d8fde3f08d120d40187d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global wlr_protocols_commit 4264185db3b7e961e7f157e1cc4fd0ab75137568

%global xlib_minver 1.6.7
%global glib2_minver 2.68.0
%global gtk3_minver 3.24.0
%global gdk_pixbuf_minver 2.40.0
%global wnck_minver 3.14
%global wl_minver 1.15

%global api_majorver 0

Name:           libxfce4windowing
Version:        4.19.3%{?commitdate:^git%{commitdate}.%{shortcommit}}
Release:        1%{?dist}
Summary:        Windowing concept abstraction library for X11 and Wayland

License:        LGPL-2.1-or-later
URL:            https://gitlab.xfce.org/xfce/libxfce4windowing
Source0:        %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.bz2
# Used exclusively at build-time
Source1:        https://gitlab.freedesktop.org/wlroots/wlr-protocols/-/archive/%{wlr_protocols_commit}/wlr-protocols-%{wlr_protocols_commit}.tar.bz2

BuildRequires:  bzip2
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  tar
BuildRequires:  xfce4-dev-tools >= 4.18.1
# Generic deps
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_minver}
BuildRequires:  pkgconfig(gobject-2.0) >= %{glib2_minver}
BuildRequires:  pkgconfig(gio-unix-2.0) >= %{glib2_minver}
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= %{gdk_pixbuf_minver}
BuildRequires:  pkgconfig(gdk-3.0) >= %{gtk3_minver}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_minver}
BuildRequires:  pkgconfig(gtk-doc) >= 1.30
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.66.0
# Wayland deps
BuildRequires:  pkgconfig(gdk-wayland-3.0) >= %{gtk3_minver}
BuildRequires:  pkgconfig(wayland-scanner) >= %{wl_minver}
BuildRequires:  pkgconfig(wayland-client) >= %{wl_minver}
# X11 deps
BuildRequires:  pkgconfig(x11) >= %{xlib_minver}
BuildRequires:  pkgconfig(gdk-x11-3.0) >= %{gtk3_minver}
BuildRequires:  pkgconfig(libwnck-3.0) >= %{wnck_minver}

%description
Libxfce4windowing is an abstraction library that attempts to present
windowing concepts (screens, toplevel windows, workspaces, etc.) in a
windowing-system-independent manner.

Currently, X11 is fully supported, via libwnck.  Wayland is partially
supported, through various Wayland protocol extensions.  However, the
full range of operations available on X11 is not available on Wayland,
due to missing features in these protocol extensions.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -S git_am -n %{name}-%{commit}
# Extract wlr-protocols to replace missing submodule
mkdir -p protocols/wlr-protocols
tar -C protocols/wlr-protocols -xf %{SOURCE1} --strip-components=1


%build
%{?commitdate:NOCONFIGURE=1 xdt-autogen}
%configure --disable-static %{?commitdate:--enable-maintainer-mode}
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc NEWS
%{_libdir}/%{name}*.so.%{api_majorver}{,.*}
%{_libdir}/girepository-1.0/Libxfce4windowing*-%{api_majorver}.0.typelib

%files devel
# Co-own the directory for now
%dir %{_includedir}/xfce4
%{_includedir}/xfce4/%{name}*/
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}*.pc
%{_datadir}/gir-1.0/Libxfce4windowing*-%{api_majorver}.0.gir


%changelog
* Sun Mar 24 2024 Joshua Strobl <joshua@buddiesofbudgie.org> - 4.19.3^git20240317.0a487d7-1
- Update to 4.19.3

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.19.2^git20231104.1fbbf17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.19.2^git20231104.1fbbf17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 02 2023 Neal Gompa <ngompa@fedoraproject.org> - 4.19.2^git20231104.1fbbf17-1
- Initial package
