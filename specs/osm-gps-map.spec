Name:           osm-gps-map
Version:        1.2.0
Release:        1%{?dist}
Summary:        Gtk+ widget for displaying OpenStreetMap tiles

License:        GPL-2.0-or-later
URL:            https://github.com/nzjrs/%{name}/
Source0:        https://github.com/nzjrs/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gnome-common
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  libsoup-devel


%description
A Gtk+ widget that when given GPS co-ordinates, draws a GPS track, and
points of interest on a moving map display. Downloads map data from a
number of websites, including openstreetmap.org.

%package devel
Summary:        Development files for the osm-gps-map Gtk+ widget
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The development files for the osm-gps-map Gtk+ widget

%package gobject
Summary:        GObject introspection bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gobject-introspection

%description gobject
GObject introspection bindings for %{name}.


%prep
%autosetup


%build
%configure --disable-static
%make_build


%install
%make_install


%files
%doc AUTHORS README NEWS ChangeLog
%license COPYING
%exclude %{_libdir}/*.la
%exclude %{_datadir}/gtk-doc/html/libosmgpsmap/
%if 0%{?rhel} <= 7
%exclude %{_datadir}/doc/%{name}/
%endif

%{_libdir}/libosmgpsmap-1.0.so.1{,.*}

%files gobject
%{_libdir}/girepository-1.0/OsmGpsMap-1.0.typelib

%files devel
%{_includedir}/osmgpsmap-1.0
%{_libdir}/libosmgpsmap-1.0.so
%{_libdir}/pkgconfig/osmgpsmap-1.0.pc
%{_datarootdir}/gir-1.0/OsmGpsMap-1.0.gir


%changelog
* Mon Jan 13 2025 David Auer <dreua@posteo.de> - 1.2.0-1
- new version

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 27 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 1.1.0-18
- Modernize spec

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.0-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Jiri Kastner <jkastner@@fedoraproject.org> - 1.1.0-2
- added excluded files for epel7

* Wed May 30 2018 Jiri Kastner <jkastner@@fedoraproject.org> - 1.1.0-1
- update to latest release (RHBZ#1562521)
- cleaned build and install

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-15
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.1-7
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 26 2013 Jiri Kastner <jkastner ( at ) redhat ( dot ) com> - 1.0.1-5
- obsoletes for python-osmgpsmap

* Fri Aug 23 2013 Jiri Kastner <jkastner ( at ) redhat ( dot ) com> - 1.0.1-4
- removed --disable-introspection from %%configure
- removed osm-gps-map-gobject dependency on pygobject3

* Thu Aug 22 2013 Richard Shaw <hobbes1069@gmail.com> - 1.0.1-3
- Separate gobject python binding into its own package.
- Update requirements for gobject package so the python  module can be imported.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.0.1-1
- Update to 1.0.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.7.3-4
- Rebuild for new libpng

* Tue May 10 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.7.3-3
- Drop unecessary BR cairo-gobject-devel

* Fri May  6 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.7.3-2
- Fix issues noted in review:
- - grammatical issues
- - drop reference to python bindings
- - use GPLv2 license
- - add/remove doc files
- - use verbose build
- - disable gobject introspection

* Tue May  3 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.7.3-1
- First version for Fedora
