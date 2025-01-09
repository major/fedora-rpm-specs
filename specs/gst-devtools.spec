%global apiver 1.0

Name:           gst-devtools
Version:        1.24.11
Release:        1%{?dist}
Summary:        Development and debugging tools for GStreamer

License:        LGPL-2.0-or-later
URL:            https://gstreamer.freedesktop.org/src/gst-devtools
Source:         https://gstreamer.freedesktop.org/src/gst-devtools/gst-devtools-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  gobject-introspection-devel
BuildRequires:  json-glib-devel
BuildRequires:  gtk-doc
BuildRequires:  python3-devel
BuildRequires:  cairo-devel

%description
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       gstreamer1-devel%{?_isa}

%description devel
%{summary}.

%package -n gst-debug-viewer
Summary:        GStreamer Debug Viewer
Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       python3-gobject
BuildArch:      noarch

%description -n gst-debug-viewer
A simple graphical utility to view and analyze GStreamer debug files.

%prep
%autosetup -p3

%build
%meson -D doc=disabled -D debug_viewer=enabled
%meson_build

%install
%meson_install

%files
%doc validate/README
%license validate/COPYING
%{_bindir}/gst-validate-*
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/GstValidate-%{apiver}.typelib
%{_libdir}/gstreamer-1.0/libgstvalidatetracer.so
%{_libdir}/libgstvalidate-%{apiver}.so.*
%{_datadir}/gstreamer-1.0/validate/
%{_libdir}/gstreamer-1.0/validate/*.so
%{_libdir}/gst-validate-launcher/
%{_libdir}/libgstvalidate-default-overrides-1.0.so.0*

%files devel
%{_includedir}/gstreamer-1.0/gst/validate/
%{_libdir}/libgstvalidate-%{apiver}.so
%{_libdir}/pkgconfig/gstreamer-validate-%{apiver}.pc
%dir %{_datadir}/gir-1.0/
%{_datadir}/gir-1.0/GstValidate-%{apiver}.gir
%{_libdir}/libgstvalidate-default-overrides-1.0.so

%files -n gst-debug-viewer
%{_bindir}/gst-debug-viewer
%{python3_sitelib}/GstDebugViewer/
%{_datadir}/applications/org.freedesktop.GstDebugViewer.desktop
%{_datadir}/gst-debug-viewer/
%{_datadir}/icons/hicolor/*/apps/gst-debug-viewer.*
%{_metainfodir}/org.freedesktop.GstDebugViewer.appdata.xml

%changelog
* Tue Jan 07 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.24.11-1
- 1.24.11

* Wed Dec 04 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.10-1
- 1.24.10

* Thu Oct 31 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.9-1
- 1.24.9

* Thu Sep 19 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.8-1
- 1.24.8

* Wed Aug 21 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.7-1
- 1.24.7

* Mon Jul 29 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.6-1
- 1.24.6

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 21 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.5-1
- 1.24.5

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.24.4-2
- Rebuilt for Python 3.13

* Wed May 29 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.4-1
- 1.24.4

* Tue Apr 30 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.3-1
- 1.24.3

* Thu Apr 18 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.24.0-1
- 1.24.0

* Thu Jan 25 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.22.9-1
- 1.22.9

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.22.8-1
- 1.22.8

* Tue Nov 21 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 1.22.7-2
- Use upstream source tarball
- Add gst-debug-viewer

* Mon Nov 13 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.22.7-1
- 1.22.7

* Wed Sep 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.22.6-1
- 1.22.6

* Tue Jul 25 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.22.5-1
- 1.22.5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.19.2-4
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 15 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.19.2-1
- 1.19.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.12.3-4
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.12.3-2
- Review fixes.

* Mon Oct 02 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.12.3-1
- Initial package.
