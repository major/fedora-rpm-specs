%global apiver  0

Name:           gtk-layer-shell
Version:        0.9.1
Release:        %autorelease
Summary:        Library to create components for Wayland using the Layer Shell

License:        LGPL-3.0-or-later and MIT
URL:            https://github.com/wmww/gtk-layer-shell
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.45.1
BuildRequires:  vala

# https://github.com/wmww/gtk-layer-shell/blob/master/compatibility.md
BuildRequires:  pkgconfig(gtk+-wayland-3.0) >= 3.22.0

BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(wayland-client) >= 1.10.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.16
BuildRequires:  pkgconfig(wayland-scanner) >= 1.10.0
BuildRequires:  pkgconfig(wayland-server) >= 1.10.0


%description
A library to write GTK applications that use Layer Shell. Layer Shell is a
Wayland protocol for desktop shell components, such as panels, notifications
and wallpapers. You can use it to anchor your windows to a corner or edge of
the output, or stretch them across the entire output. This library only makes
sense on Wayland compositors that support Layer Shell, and will not work on
X11. It supports all Layer Shell features including popups and popovers
(GTK popups Just Work™). Please open issues for any bugs you come across.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.


%prep
%autosetup


%build
%meson           \
    -Dtests=true \
    %{nil}
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license LICENSE_LGPL.txt LICENSE_MIT.txt
%doc README.md CHANGELOG.md
%{_libdir}/girepository-1.0/GtkLayerShell-%{apiver}.?.typelib
%{_libdir}/lib%{name}.so.%{apiver}*

%files devel
%{_datadir}/gir-1.0/GtkLayerShell-%{apiver}.?.gir
%{_datadir}/vala/vapi/%{name}-%{apiver}*
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc


%changelog
%autochangelog
