Summary:	Model to synchronize multiple instances over DBus
Name:		dee
Version:	1.2.7
Release:	57%{?dist}
# GPLv3-licensed tests and examples are in the tarball, but not installed
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:	LGPL-3.0-only
URL:		https://launchpad.net/dee
Source0:	http://launchpad.net/dee/1.0/%{version}/+download/%{name}-%{version}.tar.gz
Patch0:		dee-1.2.7-gcc6-fixes.patch
Patch1:		dee-1.2.7-deprecated-g_type_class_add_private.patch
# https://salsa.debian.org/debian/dee/-/blob/master/debian/patches/vapi-skip-properties.patch
Patch2:		vapi-skip-properties.patch
# Skip duplicates flagged by vala 0.5X
Patch3:		dee-1.2.7-fix-duplicates-vala-0.5X.patch
# Fix issue where g_string_free was not storing the return value
Patch4:		dee-1.2.7-fix-g_string_free-usage.patch
BuildRequires:	vala
BuildRequires:	gtk-doc
BuildRequires:	dbus-glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	libicu-devel >= 4.6
BuildRequires:	python3-devel
BuildRequires:	autoconf, automake, libtool
BuildRequires: make
# For %%{python3_sitearch}/gi/overrides directory
Requires:	python3-gobject-base

%description
Libdee is a library that uses DBus to provide objects allowing you to
create Model-View-Controller type programs across DBus. It also
consists of utility objects which extend DBus allowing for peer-to-peer
discoverability of known objects without needing a central registrar.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch -P0 -p1 -b .gcc6
%patch -P1 -p1 -b .dep
%patch -P2 -p1
%patch -P3 -p1 -b .dupes
%patch -P4 -p1 -b .freefix
autoupdate
autoreconf -ifv .

%build
export CFLAGS="%{optflags} -Wno-error=maybe-uninitialized"
export PYTHON="/usr/bin/python3"
%configure --disable-static
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -regex ".*\.la$" | xargs rm -f --

%ldconfig_scriptlets

%files
%license COPYING
%{_bindir}/dee-tool
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/libdee*.so.*
%{python3_sitearch}/gi/overrides/*

%files devel
%license COPYING
%{_includedir}/dee-1.0
%{_libdir}/libdee*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/dee-1.0
%{_datadir}/vala/vapi/*.vapi
%{_datadir}/vala/vapi/*.deps

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 1.2.7-56
- Rebuild for ICU 76

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.7-55
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.7-53
- Rebuilt for Python 3.13

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 1.2.7-52
- Rebuild for ICU 74

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 1.2.7-48
- Rebuilt for ICU 73.2

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.2.7-47
- Rebuilt for Python 3.12

* Fri Apr 28 2023 Tom Callaway <spot@fedoraproject.org> - 1.2.7-46
- fix FTBFS caused by g_string_free() calls not storing return value

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 1.2.7-44
- Rebuild for ICU 72

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.2.7-43
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.7-41
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Tom Callaway <spot@fedoraproject.org> - 1.2.7-39
- Skip duplicates flagged by vala 0.5X

* Thu Sep 16 2021 Tom Callaway <spot@fedoraproject.org> - 1.2.7-38
- invoke autoupdate
- rebuild against new vala

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.7-36
- Rebuilt for Python 3.10

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 1.2.7-35
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 1.2.7-34
- Rebuild for ICU 69

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.7-31
- Rebuilt for Python 3.9

* Mon May 18 2020 Kalev Lember <klember@redhat.com> - 1.2.7-30
- Fix the build with latest vala (#1817654)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 1.2.7-28
- Rebuild for ICU 65

* Thu Sep  5 2019 Tom Callaway <spot@fedoraproject.org> - 1.2.7-27
- replace use of deprecated g_type_class_add_private

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.7-26
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 1.2.7-24
- Update BRs for vala packaging changes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 1.2.7-22
- Rebuild for ICU 63

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 1.2.7-20
- Rebuild for ICU 62

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.7-19
- Rebuilt for Python 3.7

* Tue May 15 2018 Pete Walter <pwalter@fedoraproject.org> - 1.2.7-18
- Rebuild for ICU 61.1

* Tue May  1 2018 Tom Callaway <spot@fedoraproject.org> - 1.2.7-17
- use python3 in rawhide (fix ftbfs)

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 1.2.7-16
- Rebuild for ICU 61.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 1.2.7-14
- Rebuild for ICU 60.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 1.2.7-9
- rebuild for ICU 57.1

* Fri Feb 12 2016 Tom Callaway <spot@fedoraproject.org> - 1.2.7-8
- fix gcc6 issues

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 1.2.7-6
- rebuild for ICU 56.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 1.2.7-4
- rebuild for ICU 54.1

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 1.2.7-3
- rebuild for ICU 53.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug  7 2014 Tom Callaway <spot@fedoraproject.org> - 1.2.7-1
- update to 1.2.7

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.14-5
- Rebuilt for gobject-introspection 1.41.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 14 2014 David Tardon <dtardon@redhat.com> - 1.0.14-3
- rebuild for new ICU

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Tom Callaway <spot@fedoraproject.org> - 1.0.14-1
- update to 1.0.14

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 18 2012 Tom Callaway <spot@fedoraproject.org> - 1.0.0-1
- new release 1.0.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct  7 2011 Adam Williamson <awilliam@redhat.com> - 0.5.22-1
- new release 0.5.22

* Wed May 11 2011 Adam Williamson <awilliam@redhat.com> - 0.5.18-1
- new release 0.5.18

* Mon Mar 07 2011 Adam Williamson <awilliam@redhat.com> - 0.5.12-1
- new release 0.5.12

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Adam Williamson <awilliam@redhat.com> - 0.5.4-1
- new release

* Fri Dec 03 2010 Adam Williamson <awilliam@redhat.com> - 0.4.2-1
- initial package
