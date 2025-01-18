# -*- rpm-spec -*-

Summary: Tethered shooting & control of digital cameras
Name: entangle
Version: 3.0
Release: 9%{?dist}
License: GPL-3.0-or-later
Source: https://entangle-photo.org/download/sources/%{name}-%{version}.tar.xz
Patch: 0001-meson-fix-build-for-meson-0.60.0.patch
URL: https://entangle-photo.org/

BuildRequires: glib2-devel >= 2.36.0
BuildRequires: gtk3-devel >= 3.22.0
BuildRequires: libgphoto2-devel >= 2.4.11
BuildRequires: libgudev1-devel >= 145
BuildRequires: lcms2-devel >= 2.0
BuildRequires: gobject-introspection-devel >= 1.54.0
BuildRequires: libpeas1-devel >= 1.2.0
BuildRequires: libgexiv2-devel >= 0.2.2
BuildRequires: intltool
BuildRequires: libX11-devel
BuildRequires: libXext-devel >= 1.3.0
BuildRequires: LibRaw-devel >= 0.9.0
BuildRequires: itstool
BuildRequires: gtk-doc
BuildRequires: gstreamer1-devel >= 1.0.0
BuildRequires: gstreamer1-plugins-base-devel >= 1.0.0
BuildRequires: meson >= 0.41.0

BuildRequires: adwaita-icon-theme
Requires: adwaita-icon-theme
Requires: libpeas1-loader-python3%{?_isa}

%description
Entangle is an application which uses GTK and libgphoto2 to provide a
graphical interface for tethered photography with digital cameras.

It includes control over camera shooting and configuration settings
and 'hands off' shooting directly from the controlling computer.

%prep
%autosetup -p1

%build
%meson -Denable-gtk-doc=true
%meson_build

%install
%meson_install
%find_lang %{name}

rm -f %{buildroot}%{_libdir}/libentangle_backend.so
rm -f %{buildroot}%{_libdir}/libentangle_frontend.so

%files -f %{name}.lang
%doc README.rst COPYING AUTHORS NEWS ChangeLog
%{_bindir}/entangle
%{_mandir}/man1/entangle.1*

%{_libdir}/libentangle_backend.so.0
%{_libdir}/libentangle_backend.so.0.0.0
%{_libdir}/libentangle_frontend.so.0
%{_libdir}/libentangle_frontend.so.0.0.0

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins

%{_datadir}/icons/hicolor/*/apps/org.entangle_photo.Manager.png
%{_datadir}/icons/hicolor/*/apps/entangle-*.png
%{_datadir}/icons/hicolor/scalable/apps/org.entangle_photo.Manager.svg

%dir %{_datadir}/help/C/entangle/
%{_datadir}/help/C/entangle/*.page
%{_datadir}/help/C/entangle/*.xml
%dir %{_datadir}/help/C/entangle/figures
%{_datadir}/help/C/entangle/figures/*.png

%dir %{_libdir}/%{name}/plugins/photobox
%dir %{_datadir}/%{name}/plugins/photobox
%dir %{_datadir}/%{name}/plugins/photobox/schemas
%{_libdir}/%{name}/plugins/photobox/photobox.plugin
%{_libdir}/%{name}/plugins/photobox/photobox.py*
%{_datadir}/%{name}/plugins/photobox/schemas/gschemas.compiled
%{_datadir}/%{name}/plugins/photobox/schemas/org.entangle-photo.plugins.photobox.gschema.xml

%dir %{_libdir}/%{name}/plugins/shooter
%dir %{_datadir}/%{name}/plugins/shooter
%dir %{_datadir}/%{name}/plugins/shooter/schemas
%{_libdir}/%{name}/plugins/shooter/shooter.plugin
%{_libdir}/%{name}/plugins/shooter/shooter.py*
%{_datadir}/%{name}/plugins/shooter/schemas/gschemas.compiled
%{_datadir}/%{name}/plugins/shooter/schemas/org.entangle-photo.plugins.shooter.gschema.xml

%dir %{_libdir}/%{name}/plugins/eclipse
%dir %{_datadir}/%{name}/plugins/eclipse
%dir %{_datadir}/%{name}/plugins/eclipse/schemas
%{_libdir}/%{name}/plugins/eclipse/eclipse.plugin
%{_libdir}/%{name}/plugins/eclipse/eclipse.py*
%{_datadir}/%{name}/plugins/eclipse/schemas/gschemas.compiled
%{_datadir}/%{name}/plugins/eclipse/schemas/org.entangle-photo.plugins.eclipse.gschema.xml

%{_datadir}/%{name}/sRGB.icc
%{_datadir}/gtk-doc/html/%{name}
%{_datadir}/applications/org.entangle_photo.Manager.desktop
%{_datadir}/metainfo/org.entangle_photo.Manager.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.entangle-photo.manager.gschema.xml
%{_datadir}/gir-1.0/Entangle-0.1.gir
%{_libdir}/girepository-1.0/Entangle-0.1.typelib

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Daniel P. Berrange <berrange@redhat.com> - 3.0-7
- Switch to libpeas1 dep

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.0-2
- LibRaw rebuild

* Tue Aug  2 2022 Daniel P. Berrange <berrange@redhat.com> - 3.0-1
- Update to 3.0 release

* Tue Aug  2 2022 Daniel P. Berrange <berrange@redhat.com> - 2.0-12
- Fix meson incompatibility (rhbz#2113204)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.0-5
- Rebuild for new LibRaw

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 13 2019 Daniel P. Berrange <berrange@redhat.com> - 2.0-1
- Update to 2.0 release

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.0-7
- Rebuild with fixed binutils

* Fri Jul 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0-6
- Rebuild for new binutils

* Thu Jul 26 2018 Adam Williamson <awilliam@redhat.com> - 1.0-5
- Rebuild for new libraw

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0-2
- Remove obsolete scriptlets

* Tue Oct 10 2017 Daniel P. Berrange <berrange@redhat.com> - 1.0-1
- Update to 1.0 release

* Fri Aug 25 2017 Daniel P. Berrange <berrange@redhat.com> - 0.7.2-1
- Update to 0.7.2 release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
