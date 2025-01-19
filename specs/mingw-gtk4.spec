%{?mingw_package_header}

%global bin_version 4.0.0
# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-gtk4
Version:        4.14.4
Release:        2%{?dist}
Summary:        MinGW Windows GTK+ library

License:        LGPLv2+
URL:            http://www.gtk.org
Source:         https://download.gnome.org/sources/gtk/%{release_version}/gtk-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build

BuildRequires:  mingw32-filesystem >= 107
BuildRequires:  mingw64-filesystem >= 107
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils

BuildRequires:  mingw32-cairo
BuildRequires:  mingw64-cairo
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw32-gettext
BuildRequires:  mingw64-gettext
BuildRequires:  mingw32-graphene
BuildRequires:  mingw64-graphene
BuildRequires:  mingw32-gstreamer1-plugins-bad-free
BuildRequires:  mingw64-gstreamer1-plugins-bad-free
BuildRequires:  mingw64-graphene
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  mingw32-libepoxy
BuildRequires:  mingw64-libepoxy
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw32-pango
BuildRequires:  mingw64-pango
BuildRequires:  mingw32-pixman
BuildRequires:  mingw64-pixman
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-zlib

# Native one for msgfmt
BuildRequires:  gettext
# Native one for glib-genmarshal
BuildRequires:  glib2-devel
# Native one for gtk-update-icon-cache
BuildRequires:  gtk-update-icon-cache


%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 4 library.


%package -n mingw32-gtk4
Summary:        MinGW Windows GTK+ library
Requires:       mingw32-adwaita-icon-theme
# split out in a subpackage
Requires:       mingw32-gtk4-update-icon-cache

%description -n mingw32-gtk4
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 4 library.


%package -n mingw32-gtk4-update-icon-cache
Summary: Icon theme caching utility

%description -n mingw32-gtk4-update-icon-cache
GTK+ can use the cache files created by gtk-update-icon-cache to avoid a lot of
system call and disk seek overhead when the application starts. Since the
format of the cache files allows them to be mmap()ed shared between multiple
applications, the overall memory consumption is reduced as well.

This package contains the MinGW Windows cross compiled gtk-update-icon-cache.


%package -n mingw64-gtk4
Summary:        MinGW Windows GTK+ library
Requires:       mingw64-adwaita-icon-theme
# split out in a subpackage
Requires:       mingw64-gtk4-update-icon-cache

%description -n mingw64-gtk4
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains the MinGW Windows cross compiled GTK+ 4 library.


%package -n mingw64-gtk4-update-icon-cache
Summary: Icon theme caching utility

%description -n mingw64-gtk4-update-icon-cache
GTK+ can use the cache files created by gtk-update-icon-cache to avoid a lot of
system call and disk seek overhead when the application starts. Since the
format of the cache files allows them to be mmap()ed shared between multiple
applications, the overall memory consumption is reduced as well.

This package contains the MinGW Windows cross compiled gtk-update-icon-cache.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n gtk-%{version}


%build
%mingw_meson -Dintrospection=disabled -Dvulkan=disabled
%mingw_ninja


%install
%mingw_ninja_install

# Remove desktop files and corresponding icons as they aren't useful for win32
rm -f %{buildroot}%{mingw32_datadir}/applications/*.desktop
rm -f %{buildroot}%{mingw64_datadir}/applications/*.desktop
rm -rf %{buildroot}%{mingw32_datadir}/icons/
rm -rf %{buildroot}%{mingw64_datadir}/icons/
rm -rf %{buildroot}%{mingw32_datadir}/metainfo/
rm -rf %{buildroot}%{mingw64_datadir}/metainfo/

%mingw_find_lang %{name} --all-name


%files -n mingw32-gtk4 -f mingw32-%{name}.lang
%license COPYING
%{mingw32_bindir}/gtk4-demo-application.exe
%{mingw32_bindir}/gtk4-demo.exe
%{mingw32_bindir}/gtk4-icon-browser.exe
%{mingw32_bindir}/gtk4-widget-factory.exe
%{mingw32_bindir}/gtk4-builder-tool.exe
%{mingw32_bindir}/gtk4-encode-symbolic-svg.exe
%{mingw32_bindir}/gtk4-query-settings.exe
%{mingw32_bindir}/gtk4-node-editor.exe
%{mingw32_bindir}/gtk4-path-tool.exe
%{mingw32_bindir}/gtk4-print-editor.exe
%{mingw32_bindir}/gtk4-rendernode-tool.exe
%{mingw32_bindir}/libgtk-4-1.dll
%{mingw32_includedir}/gtk-4.0/
%dir %{mingw32_libdir}/gtk-4.0
%dir %{mingw32_libdir}/gtk-4.0/%{bin_version}
%dir %{mingw32_libdir}/gtk-4.0/%{bin_version}/media
%{mingw32_libdir}/gtk-4.0/%{bin_version}/media/libmedia-gstreamer.dll
%{mingw32_libdir}/gtk-4.0/%{bin_version}/media/libmedia-gstreamer.dll.a
%{mingw32_libdir}/libgtk-4.dll.a
%{mingw32_libdir}/pkgconfig/gtk4.pc
%{mingw32_libdir}/pkgconfig/gtk4-win32.pc
%{mingw32_datadir}/gettext/
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.Demo4.gschema.xml
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.gtk4.Settings.ColorChooser.gschema.xml
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.gtk4.Settings.Debug.gschema.xml
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.gtk4.Settings.EmojiChooser.gschema.xml
%{mingw32_datadir}/glib-2.0/schemas/org.gtk.gtk4.Settings.FileChooser.gschema.xml
%{mingw32_datadir}/gtk-4.0/

%files -n mingw32-gtk4-update-icon-cache
%license COPYING
%{mingw32_bindir}/gtk4-update-icon-cache.exe

%files -n mingw64-gtk4 -f mingw64-%{name}.lang
%license COPYING
%{mingw64_bindir}/gtk4-demo-application.exe
%{mingw64_bindir}/gtk4-demo.exe
%{mingw64_bindir}/gtk4-icon-browser.exe
%{mingw64_bindir}/gtk4-widget-factory.exe
%{mingw64_bindir}/gtk4-builder-tool.exe
%{mingw64_bindir}/gtk4-encode-symbolic-svg.exe
%{mingw64_bindir}/gtk4-query-settings.exe
%{mingw64_bindir}/gtk4-node-editor.exe
%{mingw64_bindir}/gtk4-path-tool.exe
%{mingw64_bindir}/gtk4-print-editor.exe
%{mingw64_bindir}/gtk4-rendernode-tool.exe
%{mingw64_bindir}/libgtk-4-1.dll
%{mingw64_includedir}/gtk-4.0/
%dir %{mingw64_libdir}/gtk-4.0
%dir %{mingw64_libdir}/gtk-4.0/%{bin_version}
%dir %{mingw64_libdir}/gtk-4.0/%{bin_version}/media
%{mingw64_libdir}/gtk-4.0/%{bin_version}/media/libmedia-gstreamer.dll
%{mingw64_libdir}/gtk-4.0/%{bin_version}/media/libmedia-gstreamer.dll.a
%{mingw64_libdir}/libgtk-4.dll.a
%{mingw64_libdir}/pkgconfig/gtk4.pc
%{mingw64_libdir}/pkgconfig/gtk4-win32.pc
%{mingw64_datadir}/gettext/
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.Demo4.gschema.xml
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.gtk4.Settings.ColorChooser.gschema.xml
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.gtk4.Settings.Debug.gschema.xml
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.gtk4.Settings.EmojiChooser.gschema.xml
%{mingw64_datadir}/glib-2.0/schemas/org.gtk.gtk4.Settings.FileChooser.gschema.xml
%{mingw64_datadir}/gtk-4.0/

%files -n mingw64-gtk4-update-icon-cache
%license COPYING
%{mingw64_bindir}/gtk4-update-icon-cache.exe


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Marc-André Lureau <marcandre.lureau@redhat.com> - 4.14.4-1
- new version

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 27 2023 Marc-André Lureau <marcandre.lureau@redhat.com> - 4.11.4-1
- new version

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 25 2022 Marc-André Lureau <marcandre.lureau@redhat.com> - 4.8.2-1
- Bump to 4.8.2 release

* Thu Aug 18 2022 Marc-André Lureau <marcandre.lureau@redhat.com> - 4.7.2-1
- initial packaging
