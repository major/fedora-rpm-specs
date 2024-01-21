Name:          clapper
Version:       0.5.2
Release:       4%{?dist}
Summary:       GStreamer-based GNOME media player built using GJS and GTK4

License:       GPLv3+ and LGPLv2+
URL:           https://github.com/Rafostar/clapper
Source0:       https://github.com/Rafostar/clapper/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-base-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gstreamer-tag-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(gstreamer-gl-1.0)
BuildRequires: pkgconfig(gstreamer-gl-prototypes-1.0)
BuildRequires: pkgconfig(gstreamer-gl-x11-1.0)
BuildRequires: pkgconfig(gstreamer-gl-wayland-1.0)
BuildRequires: pkgconfig(gstreamer-gl-egl-1.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: gobject-introspection-devel
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gtk4-x11)
BuildRequires: pkgconfig(gtk4-wayland)
BuildRequires: gjs
BuildRequires: libappstream-glib
BuildRequires: glib2-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires:      gjs
Requires:      libadwaita%{_isa}
Requires:      hicolor-icon-theme

%description
A GNOME media player built using GJS with GTK4 toolkit. The media player uses
GStreamer as a media backend and renders everything via OpenGL.

%package devel
Summary:  Header files and libraries for Clapper development
Requires: %{name}%{_isa} = %{version}-%{release}

%description devel
The clapper-devel package contains header files and libraries needed to develop
programs that use Clapper.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang com.github.rafostar.Clapper

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f com.github.rafostar.Clapper.lang
%license COPYING
%doc README.md
%{_bindir}/clapper
%{_bindir}/com.github.rafostar.Clapper*
%{_datadir}/applications/com.github.rafostar.Clapper.desktop
%{_datadir}/com.github.rafostar.Clapper/
%{_datadir}/dbus-1/services/com.github.rafostar.Clapper.service
%{_datadir}/glib-2.0/schemas/com.github.rafostar.Clapper.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/mime/packages/com.github.rafostar.Clapper.xml
%{_libdir}/clapper-1.0/gst/plugin/importers/libgstclapperglimporter.so
%{_libdir}/clapper-1.0/gst/plugin/importers/libgstclappergluploader.so
%{_libdir}/clapper-1.0/gst/plugin/importers/libgstclapperrawimporter.so
%dir %{_libdir}/com.github.rafostar.Clapper/
%{_libdir}/com.github.rafostar.Clapper/girepository-1.0/
%{_libdir}/com.github.rafostar.Clapper/libgstclapper-1.0.so.*
%{_libdir}/gstreamer-1.0/libgstclapper.so
%{_libdir}/libgstclapperglbaseimporter.so
%{_libdir}/libgstclapperglbaseimporter.so.*
%{_metainfodir}/com.github.rafostar.Clapper.metainfo.xml

%files devel
%dir %{_datadir}/gir-1.0/
%{_datadir}/gir-1.0/GstClapper-1.0.gir
%{_libdir}/com.github.rafostar.Clapper/libgstclapper-1.0.so

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jul 31 2022 Jonathan Schleifer <js@nil.im> - 0.5.2-1
- Update to 0.5.2

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 29 2022 Jonathan Schleifer <js@nil.im> - 0.4.1-1
- Update to 0.4.1

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 19 2021 Jonathan Schleifer <js@nil.im> - 0.4.0-3
- Apply 2 patches from upstream to fix more libadwaita 0.6.alpha.4 issues

* Fri Nov 19 2021 Jonathan Schleifer <js@nil.im> - 0.4.0-2
- Apply patch from upstream to fix dark mode with libadwaita 0.6.alpha.4

* Sun Nov 14 2021 Jonathan Schleifer <js@nil.im> - 0.4.0-1
- Initial release
- Spec file improved as per review
