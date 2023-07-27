%global apiver 1.0

Name:           gst-devtools
Version:        1.22.5
Release:        1%{?dist}
Summary:        Development and debugging tools for GStreamer

License:        LGPL-2.0-or-later
URL:            https://gstreamer.freedesktop.org/src/gst-devtools
# git clone --depth 1 --branch %%{version} https://gitlab.freedesktop.org/gstreamer/gstreamer.git
# cd gstreamer/subprojects ; tar -czf gst-devtools.tar.gz gst-devtools
Source0:        %{name}.tar.gz

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

%prep
%autosetup -n %{name}

%build
%meson -D doc=disabled
%meson_build

%install
%meson_install

for lib in `find %{buildroot} -type f -name '*.py'`; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

sed -i "s/env\ //g" %{buildroot}%{_bindir}/gst-validate-launcher

%ldconfig_scriptlets

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

%changelog
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
