# -*- rpm-spec -*-

%define with_introspection 0

%if 0%{?fedora} >= 18
%define with_introspection 1
%endif
%if 0%{?rhel} >= 7
%define with_introspection 1
%endif
%define with_vala %{with_introspection}

Name: libvirt-designer
Version: 0.0.2
Release: 18%{?dist}%{?extra_release}
Summary: Libvirt configuration designer
License: LGPLv2+
URL: http://libvirt.org/
Source0: http://libvirt.org/sources/designer/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires: libvirt-gconfig-devel >= 0.1.7
BuildRequires: libvirt-gobject-devel >= 0.1.3
%if %{with_introspection}
BuildRequires: gobject-introspection-devel
%endif
BuildRequires: libosinfo-devel >= 0.2.7
%if %{with_vala}
BuildRequires: vala
BuildRequires: libosinfo-vala >= 0.2.7
%endif
BuildRequires: /usr/bin/pod2man

%package libs
Summary: Libvirt configuration designer libraries

%package devel
Summary: Libvirt configuration designer development headers
Requires: %{name}-libs = %{version}-%{release}
Requires: libvirt-gconfig-devel >= 0.1.7

%package devel-doc
Summary: Libvirt configuration designer development documentation
Requires: %{name}-devel = %{version}-%{release}

%if %{with_vala}
%package vala
Summary: Libvirt designer vala language bindings
Requires: %{name}-libs = %{version}-%{release}
Requires: libosinfo-vala >= 0.2.7
%endif

%description
This package provides the libvirt configuration designer command
line tools.

%description libs
This package provides the libvirt configuration designer run-time
libraries.

%description devel
This package provides the libvirt configuration designer development
headers

%description devel-doc
This package provides the libvirt configuration designer development
documentation like API and exported symbols description.

%if %{with_vala}
%description vala
This package provides the libvirt configuration designer vala
language binding
%endif

%prep
%setup -q

%build

%if %{with_introspection}
%define introspection_arg --enable-introspection
%else
%define introspection_arg --disable-introspection
%endif

%configure %{introspection_arg}
%__make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%__make install  DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/libvirt-designer-1.0.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libvirt-designer-1.0.la

%ldconfig_scriptlets libs

%files
%{_bindir}/virt-designer
%{_mandir}/man1/virt-designer.1*

%files libs
%doc README COPYING AUTHORS ChangeLog NEWS
%{_libdir}/libvirt-designer-1.0.so.*
%if %{with_introspection}
%{_libdir}/girepository-1.0/LibvirtDesigner-1.0.typelib
%endif

%if %{with_vala}
%files vala
%{_datadir}/vala/vapi/libvirt-designer-1.0.deps
%{_datadir}/vala/vapi/libvirt-designer-1.0.vapi
%endif

%files devel
%{_libdir}/libvirt-designer-1.0.so
%{_libdir}/pkgconfig/libvirt-designer-1.0.pc
%dir %{_includedir}/libvirt-designer-1.0
%dir %{_includedir}/libvirt-designer-1.0/libvirt-designer
%{_includedir}/libvirt-designer-1.0/libvirt-designer/libvirt-designer.h
%{_includedir}/libvirt-designer-1.0/libvirt-designer/libvirt-designer-*.h
%if %{with_introspection}
%{_datadir}/gir-1.0/LibvirtDesigner-1.0.gir
%endif

%files devel-doc
%{_datadir}/gtk-doc/html/libvirt-designer

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 30 2019 Adam Williamson <awilliam@redhat.com> - 0.0.2-12
- Rebuild with libosinfo 1.7.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 0.0.2-10
- Update BRs for vala packaging changes

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Danie P. Berrange <berrange@rdhat.com> - 0.0.2-1
- Update to 0.0.2 release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.0.1-9
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 18 2013 Michal Privoznik <mprivozn@redhat.com> 0.0.1-6
- add recent patches to reflect libosinfo changes in set of deprecated functions

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 19 2012 Michal Privoznik <mprivozn@redhat.com> 0.0.1-4
- rebuild to prevent trashcan

* Fri Oct 12 2012 Michal Privoznik <mprivozn@redhat.com> 0.0.1-3
- introduce -devel-doc package
- drop F15 and RHEL referrence at the head

* Fri Oct 12 2012 Michal Privoznik <mprivozn@redhat.com> 0.0.1-2
- changed commiter name of the -1 release

* Tue Oct 09 2012 Michal Privoznik <mprivozn@redhat.com> 0.0.1-1
- Initial packaging of libvirt-designer
