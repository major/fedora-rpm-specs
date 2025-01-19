Summary: A library for using real 3D models within a Clutter scene
Name: libmash
Version: 0.2.0
Release: 40%{?dist}
URL: http://clutter-project.github.com/mash/
Source0: https://github.com/downloads/clutter-project/mash/mash-%{version}.tar.xz

# Already sent upstream for review,
# see http://lists.clutter-project.org/pipermail/clutter-devel-list/2011-March/000196.html
Patch0:		0001-Use-the-system-version-of-rply-if-available.patch

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
BuildRequires: libtool
BuildRequires: glib2-devel >= 2.16
BuildRequires: clutter-devel
BuildRequires: gtk-doc
BuildRequires: rply-devel
BuildRequires: gobject-introspection-devel
BuildRequires: make

# Do not BR: mx-devel, as the lighting example isn't actually installed

%description
Mash is a small library for using real 3D models within a Clutter
scene. Models can be exported from Blender or other 3D modeling
software as PLY files and then used as actors. It also supports a
lighting model with animatable lights.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains libraries and header files needed for
development of programs using %{name}.

%prep
%setup -q -n mash-%{version}
#%patch0 -p1 -b .use-system-rply

%build
autoconf

export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

%ldconfig_scriptlets

%files
%doc README COPYING.LIB NEWS AUTHORS
%{_libdir}/libmash-0.2.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib

%files devel
%dir %{_includedir}/mash-0.2
%{_includedir}/mash-0.2/*
%{_libdir}/libmash-0.2.so
%{_libdir}/pkgconfig/mash-0.2.pc
%dir %{_datadir}/gtk-doc/html/mash
%{_datadir}/gtk-doc/html/mash/*
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/gir-1.0

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.0-39
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.2.0-17
- Rebuilt for gobject-introspection 1.41.4

* Thu Jun 26 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.2.0-16
- Add explicit BR: gobject-introspection-devel (#1106038)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 20 2014 Kalev Lember <kalevlember@gmail.com> - 0.2.0-14
- Rebuilt for cogl soname bump

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> - 0.2.0-13
- Rebuild for libevdev soname bump

* Wed Feb 05 2014 Kalev Lember <kalevlember@gmail.com> - 0.2.0-12
- Rebuilt for cogl soname bump

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 0.2.0-11
- Rebuilt for cogl 1.15.4 soname bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 09 2013 Richard Hughes <rhughes@redhat.com> - 0.2.0-9
- Compile with -fno-strict-aliasing
- Resolves: https://bugzilla.redhat.com/show_bug.cgi?id=905497

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 0.2.0-8
- Rebuilt for cogl soname bump

* Fri Jan 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.0-7
- Rebuild for new cogl

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 19 2012 Matthias Clasen <mclasen@redhat.com> - 0.2.0-5
- Rebuild for new cogl

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Matthias Clasen <mclasen@redhat.com> - 0.2.0-3
- Rebuild against new clutter

* Mon Sep 26 2011 Richard Hughes <rhughes@redhat.com> - 0.2.0-2
- Rebuild for new cogl.

* Thu Sep 15 2011 Richard Hughes <rhughes@redhat.com> - 0.2.0-1
- New upstream release.

* Thu Mar 26 2011 Richard Hughes <rhughes@redhat.com> - 0.1.0-2
- Updated after review concerns.
- Do not use 'mash' in the package summary
- Add the README file to the package docs
- Own datadir/gir-1.0 and libdir/girepository-1.0
- Added note about the non-BR of mx-devel
- Added BR of rply-devel, and patched configure to use it pending a new
  upstream release.

* Sat Mar 26 2011 Richard Hughes <rhughes@redhat.com> - 0.1.0-1
- Initial version for review.
