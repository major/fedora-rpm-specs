%global samba_version 4.13
%global talloc_version 2.0.5
%global nickname VULCAN

# the python subpackage doesn't work, due to hard disable in patches for build requirements
%global build_python_package 0
%global built_mapitest 0

%if 0%{?rhel}
%global build_server_package 0
%else
# currently disabled also for rawhide (f18), due to samba4 changes
%global build_server_package 0
%endif

%if %{build_python_package}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%endif

### Abstract ###

# Licensing Note: The code is GPLv3+ and the IDL files are public domain.

Name: openchange
Version: 2.3
Release: 54%{?dist}
Summary: Provides access to Microsoft Exchange servers using native protocols
License: GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain
URL: http://www.openchange.org/
Source0: https://github.com/openchange/openchange/archive/openchange-%{version}-%{nickname}.tar.gz
Source1: doxygen_to_devhelp.xsl

### Build Dependencies ###

BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: doxygen
BuildRequires: file-devel
BuildRequires: flex
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libical-devel
BuildRequires: libldb-devel
BuildRequires: libtalloc-devel >= %{talloc_version}
BuildRequires: libtdb-devel
BuildRequires: pkgconfig
BuildRequires: libxslt
BuildRequires: popt-devel
%if %{build_python_package}
BuildRequires: python3-devel
%endif
BuildRequires: samba-common >= %{samba_version}
BuildRequires: samba-devel >= %{samba_version}
BuildRequires: samba-libs >= %{samba_version}
BuildRequires: samba-pidl >= %{samba_version}
BuildRequires: zlib-devel

%if %{build_server_package}
BuildRequires: libmemcached-devel
BuildRequires: sqlite-devel
%endif

# Certain versions of libtevent have incorrect
# internal ABI versions
Conflicts: libtevent < 0.9.13

### Patches ###

# OpenChange's libmapi conflicts with Zarafa's libmapi.
# Zarafa is older than OpenChange, so it wins.
Patch0: libmapi-0.8.2-libmapi-conflict.patch

# RH bug #552984
Patch1: openchange-0.9-generate-xml-doc.patch

# Do not build server and python parts
Patch2: openchange-1.0-OC_RULE_ADD-fix.patch

# RH-bug #1028698
Patch4: openchange-1.0-symbol-clash.patch

Patch5: openchange-2.2-samba-4.2.0-rc2.patch
Patch6: openchange-2.3-disable-server-tools-build.patch
Patch7: openchange-2.3-samba-4.4.patch
Patch8: openchange-2.3-fix-connection-args.patch
Patch9: openchange-2.3-no-yyunput.patch
Patch10: openchange-2.3-libical-3.0.patch
Patch11: openchange-2.3-disable-mysql.patch
Patch12: openchange-2.3-switch-to-python3.patch
%if !%{build_python_package}
Patch13: openchange-2.3-disable-python3.patch
%endif
Patch14: openchange-2.3-covscan.patch
Patch15: openchange-2.3-samba-4.10-macros.patch
Patch16: openchange-2.3-samba-4.11.patch
Patch17: openchange-2.3-samba-4.12.patch
Patch18: openchange-2.3-samba-4.13.patch
Patch19: openchange-2.3-autoconf-2.71.patch
%if !%{build_server_package}
Patch20: openchange-2.3-disable-server-reqs.patch
%endif
Patch21: openchange-2.3-samba-4.15.patch
Patch22: openchange-configure-c99.patch
Patch23: openchange-2.3-samba-4.20.patch

%description
OpenChange provides libraries to access Microsoft Exchange servers
using native protocols.

%package devel
Summary: Developer tools for OpenChange libraries
Requires: openchange = %{version}-%{release}
%if %{build_server_package}
Requires: openchange-server = %{version}-%{release}
%endif

%description devel
This package provides the development tools and headers for
OpenChange, providing libraries to access Microsoft Exchange servers
using native protocols.

%package devel-docs
Summary: Developer documentation for OpenChange libraries
Requires: devhelp
Requires: openchange = %{version}-%{release}
BuildArch: noarch

%description devel-docs
This package contains developer documentation for Openchange.

%package client
Summary: User tools for OpenChange libraries
Requires: openchange = %{version}-%{release}

%description client
This package provides the user tools for OpenChange, providing access to
Microsoft Exchange servers using native protocols.

%if %{build_python_package}
%package python
Summary: Python bindings for OpenChange libraries
Requires: openchange = %{version}-%{release}

%description python
This module contains a wrapper that allows the use of OpenChange via Python.
%endif

%if %{build_server_package}
%package server
Summary: Server-side modules for OpenChange
Requires: openchange = %{version}-%{release}
Requires: sqlite

%description server
This package provides the server elements for OpenChange.
%endif

%prep
%setup -q -n openchange-%{name}-%{version}-%{nickname}
%patch -P0 -p1 -b .libmapi-conflict
%patch -P1 -p1 -b .generate-xml-doc
%patch -P2 -p1 -b .OC_RULE_ADD-fix
%patch -P4 -p1 -b .symbol-clash
%patch -P5 -p1 -b .samba-4.2.0-rc2
%patch -P6 -p1 -b .disable-server-tools-build
%patch -P7 -p1 -b .samba-4.4
%patch -P8 -p1 -b .fix-connection-args
%patch -P9 -p1 -b .no-yyunput
%patch -P10 -p1 -b .libical-3.0
%patch -P11 -p1 -b .disable-mysql
%patch -P12 -p1 -b .switch-to-python3
%if !%{build_python_package}
%patch -P13 -p1 -b .disable-python3
%endif
%patch -P14 -p1 -b .covscan
%patch -P15 -p1 -b .samba-4.10-macros
%patch -P16 -p1 -b .samba-4.11
%patch -P17 -p1 -b .samba-4.12
%patch -P18 -p1 -b .samba-4.13
%patch -P19 -p1 -b .autoconf-2.71
%if !%{build_server_package}
%patch -P20 -p1 -b .disable-server-reqs
%endif
%patch -P21 -p1 -b .samba-4.15
%patch -P22 -p1
%patch -P23 -p1 -b .samba-4.20

%build
export CFLAGS="-DSOURCE4_LIBRPC_INTERNALS=1 $CFLAGS"
# Backup manually-written Makefile
mv Makefile Makefile.bak
# Provide fake Makefile.am for autoconf 2.71
touch Makefile.am
autoupdate
autoreconf -fi
%configure \
%if %{build_python_package}
	--enable-pymapi \
%endif
	--with-modulesdir=%{_libdir}/samba/modules

# Restore manually-written Makefile
mv Makefile.bak Makefile

# Parallel builds prohibited by makefile
make
if test -d apidocs ; then
	rm -r apidocs
fi
make doxygen

xsltproc -o openchange-libmapi.devhelp --stringparam "booktitle" "MAPI client library (libmapi)" --stringparam "bookpart" "libmapi" %{SOURCE1} apidocs/xml/libmapi/index.xml
xsltproc -o openchange-libmapiadmin.devhelp --stringparam "booktitle" "MAPI administration libraries (libmapiadmin)" --stringparam "bookpart" "libmapiadmin" %{SOURCE1} apidocs/xml/libmapiadmin/index.xml
xsltproc -o openchange-libocpf.devhelp --stringparam "booktitle" "OpenChange Property Files (libocpf)" --stringparam "bookpart" "libocpf" %{SOURCE1} apidocs/xml/libocpf/index.xml
%if %{built_mapitest}
xsltproc -o openchange-mapitest.devhelp --stringparam "booktitle" "MA regression test framework (mapitest)" --stringparam "bookpart" "mapitest" %{SOURCE1} apidocs/xml/mapitest/index.xml
%endif
xsltproc -o openchange-mapiproxy.devhelp --stringparam "booktitle" "MAPIProxy project (mapiproxy)" --stringparam "bookpart" "mapiproxy" %{SOURCE1} apidocs/xml/mapiproxy/index.xml
xsltproc -o openchange-libmapi++.devhelp --stringparam "booktitle" "C++ bindings for libmapi (libmapi++)" --stringparam "bookpart" "libmapi++" %{SOURCE1} apidocs/xml/libmapi++/index.xml

%install
rm -rf $RPM_BUILD_ROOT

%make_install

# This makes the right links, as rpmlint requires that the
# ldconfig-created links be recorded in the RPM.
/sbin/ldconfig -N -n $RPM_BUILD_ROOT/%{_libdir}

mkdir $RPM_BUILD_ROOT%{_mandir}
cp -r doc/man/man1 $RPM_BUILD_ROOT%{_mandir}

# Skip man3 for now, it doesn't work anyway
# cp -r apidocs/man/man3 $RPM_BUILD_ROOT%{_mandir}
rm -r apidocs/man/man3

#%if ! %{build_python_package}
#rm -r $RPM_BUILD_ROOT%{python3_sitearch}/openchange
#%endif

%if ! %{build_server_package}
# XXX OC_RULE_ADD patch disables build of this, no need to delete it.
#rm $RPM_BUILD_ROOT%{_libdir}/libmapiserver.so.*
#rm -r $RPM_BUILD_ROOT%{_libdir}/samba/modules/*
#rm $RPM_BUILD_ROOT%{_libdir}/samba/dcerpc_server/dcesrv_mapiproxy.so
rm $RPM_BUILD_ROOT%{_libdir}/nagios/check_exchange
rm -r $RPM_BUILD_ROOT%{_datadir}/setup/*
%endif

#%if !%{build_python_package} && !%{build_server_package}
#rm $RPM_BUILD_ROOT%{_bindir}/check_fasttransfer
#%endif

mkdir -p $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapi
cp openchange-libmapi.devhelp $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapi
cp -r apidocs/html/libmapi/* $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapi

mkdir -p $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapiadmin
cp openchange-libmapiadmin.devhelp $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapiadmin
cp -r apidocs/html/libmapiadmin/* $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapiadmin

mkdir -p $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libocpf
cp openchange-libocpf.devhelp $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libocpf
cp -r apidocs/html/libocpf/* $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libocpf

%if %{built_mapitest}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-mapitest
cp openchange-mapitest.devhelp $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-mapitest
cp -r apidocs/html/mapitest/* $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-mapitest
%endif

mkdir -p $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-mapiproxy
cp openchange-mapiproxy.devhelp $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-mapiproxy
cp -r apidocs/html/mapiproxy/* $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-mapiproxy

mkdir -p $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapi++
cp openchange-libmapi++.devhelp $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapi++
cp -r apidocs/html/libmapi++/* $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapi++

%ldconfig_scriptlets

%if %{build_server_package}
%ldconfig_scriptlets server
%endif

%files
%doc COPYING IDL_LICENSE.txt VERSION
%{_libdir}/libmapi-openchange.so.0
%{_libdir}/libmapi-openchange.so.2.3
%{_libdir}/libmapiadmin.so.0
%{_libdir}/libmapiadmin.so.2.3
%{_libdir}/libmapipp.so.0
%{_libdir}/libmapipp.so.2.3
%if %{build_server_package}
%{_libdir}/libmapiproxy.so.0
%{_libdir}/libmapiproxy.so.2.3
%{_libdir}/libmapistore.so.0
%{_libdir}/libmapistore.so.2.3
%endif
%{_libdir}/libocpf.so.0
%{_libdir}/libocpf.so.2.3

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files devel-docs
#%%{_mandir}/man3/*
%doc %{_datadir}/devhelp/books/*
%doc apidocs/html/libmapi
%doc apidocs/html/libocpf
%doc apidocs/html/overview
%doc apidocs/html/index.html

%files client
%{_bindir}/*
%{_mandir}/man1/*
%if %{built_mapitest}
%{_datadir}/mapitest/*
%endif

%if %{build_python_package}
%files python
%{python3_sitearch}/openchange
%endif

%if %{build_server_package}
%files server
%{_libdir}/libmapiserver.so.*
%{_libdir}/samba/dcerpc_server/dcesrv_mapiproxy.so
%{_libdir}/samba/modules/*
%if !0%{?rhel}
%{_libdir}/nagios/check_exchange
%endif
%{_datadir}/setup/*
%endif

%changelog
* Mon Feb 10 2025 Milan Crha <mcrha@redhat.com> - 2.3-54
- Rebuilt against new Samba 4.22.0 rc1

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 22 2024 Milan Crha <mcrha@redhat.com> - 2.3-52
- Rebuilt against new Samba 4.21

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Guenther Deschner <gdeschner@redhat.com> - 2.3-50
- Fix build with new Samba 4.20.0rc1

* Tue Jan 30 2024 Milan Crha <mcrha@redhat.com> - 2.3-49
- Rebuilt against new Samba 4.20rc1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 08 2023 Guenther Deschner <gdeschner@redhat.com> - 2.3-46
- Rebuilt against new Samba 4.19.0rc2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 27 2023 Florian Weimer <fweimer@redhat.com> - 2.3-44
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 09 2022 Adam Williamson <awilliam@redhat.com> - 2.3-42
- Rebuild against new libndr

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Milan Crha <mcrha@redhat.com> - 2.3-38
- Add patch to build against samba 4.15

* Thu Jun 17 2021 Milan Crha <mcrha@redhat.com> - 2.3-37
- Avoid build time dependencies related to server, when it's not built

* Fri Mar 26 2021 Milan Crha <mcrha@redhat.com> - 2.3-36
- Add patch to build with autoconf 2.71

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Milan Crha <mcrha@redhat.com> - 2.3-34
- Add patch to build against samba 4.13

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 2.3-32
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Milan Crha <mcrha@redhat.com> - 2.3-30
- Add patch to build against samba 4.12

* Fri Aug 30 2019 Milan Crha <mcrha@redhat.com> - 2.3-29
- Rebuild for newer libldb
- Add patch to build against samba 4.11

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 14 2019 Milan Crha <mcrha@redhat.com> - 2.3-27
- Add patch to build against samba 4.10 semi-public macro changes

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Milan Crha <mcrha@redhat.com> - 2.3-25
- Address some of the Coverity Scan and clang issues

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Milan Crha <mcrha@redhat.com> - 2.3-23
- Switch to python3 (partly) and disable python3 build dependency by default

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.3-22
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Mar 07 2018 Milan Crha <mcrha@redhat.com> - 2.3-21
- Do not copy content of libmapi++/ into includedir (RH bug #1548719)

* Mon Feb 19 2018 Milan Crha <mcrha@redhat.com> - 2.3-20
- Remove unneeded build dependency on mariadb-connector-c-devel

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Milan Crha <mcrha@redhat.com> - 2.3-18
- Rebuild for newer libical

* Fri Sep 22 2017 Milan Crha <mcrha@redhat.com> - 2.3-17
- Use mariadb-connector-c-devel instead of community-mysql-devel (RH bug #1494307)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 2.3-13
- rebuild for ICU 57.1

* Thu Apr 07 2016 Milan Crha <mcrha@redhat.com> - 2.3-12
- Add patch to fix connection string for samba
- Add patch to be able to build with flex 2.6.0

* Tue Feb 09 2016 Milan Crha <mcrha@redhat.com> - 2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
- Add patch to build against new samba

* Mon Jan 18 2016 Milan Crha <mcrha@redhat.com> - 2.3-10
- Rebuild against newer libical

* Thu Dec 03 2015 Milan Crha <mcrha@redhat.com> - 2.3-9
- Do not depend on libsamba-debug private library

* Mon Oct 26 2015 Milan Crha <mcrha@redhat.com> - 2.3-8
- Rebuild against newer samba

* Mon Sep 14 2015 Milan Crha <mcrha@redhat.com> - 2.3-7
- Rebuild against newer samba

* Mon Sep 07 2015 Milan Crha <mcrha@redhat.com> - 2.3-6
- Rebuild against newer samba

* Tue Sep 01 2015 Milan Crha <mcrha@redhat.com> - 2.3-5
- Rebuild against newer samba

* Mon Jul 20 2015 Milan Crha <mcrha@redhat.com> - 2.3-4
- Rebuild against newer samba

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Milan Crha <mcrha@redhat.com> - 2.3-2
- Rebuild against newer samba

* Mon May 18 2015 Milan Crha <mcrha@redhat.com> - 2.3-1
- Update to 2.3

* Thu Apr 23 2015 Milan Crha <mcrha@redhat.com> - 2.2-6
- Rebuild against newer samba

* Tue Apr 07 2015 Milan Crha <mcrha@redhat.com> - 2.2-5
- Rebuild against newer samba with a patch for samba 4.2.0 update

* Tue Jan 27 2015 Dan Horák <dan[at]danny.cz> - 2.2-4
- Rebuild again for newer samba to workaround samba-4.2.0-0.1.rc3.fc22 < samba-4.2.0-0.2.rc2.fc22 situation in secondary koji

* Tue Jan 06 2015 Milan Crha <mcrha@redhat.com> - 2.2-3
- Rebuild against newer samba

* Mon Nov 24 2014 Milan Crha <mcrha@redhat.com> - 2.2-2
- Add a patch to be able to build against samba 4.2.0-rc2

* Thu Aug 21 2014 Matthew Barnes <mbarnes@redhat.com> - 2.2-1
- Update to OpenChange 2.2

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Milan Crha <mcrha@redhat.com> - 2.1-1
- Update to OpenChange 2.1

* Thu Nov 21 2013 Milan Crha <mcrha@redhat.com> - 2.0-6
- Rebuild for new libical (RH bug #1023020)

* Mon Nov 11 2013 Milan Crha <mcrha@redhat.com> - 2.0-5
- Add patch for RH bug #1028698 (Symbol collision with NSS)

* Thu Sep 19 2013 Milan Crha <mcrha@redhat.com> - 2.0-4
- Add patch to fix multilib issue in libmapi/version.h
- Move devel-docs subpackage to noarch

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 24 2013 Rex Dieter <rdieter@fedoraproject.org> 2.0-2
- rebuild (libical)

* Thu Feb 14 2013 Milan Crha <mcrha@redhat.com> - 2.0-1
- Update to OpenChange 2.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 26 2012 Milan Crha <mcrha@redhat.com> - 1.0-12
- Add patch for Gnome bug #682449 (WriteStream fails)

* Mon Aug 06 2012 Milan Crha <mcrha@redhat.com> - 1.0-11
- Add patch for Red Hat bug #845618 (incorrect symbol resolution)

* Thu Jul 26 2012 Milan Crha <mcrha@redhat.com> - 1.0-10
- Remove check_fasttransfer from openchange-client, if not building server package

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Milan Crha <mcrha@redhat.com> - 1.0-8
- Add patch for OpenChange bug #397 (crash under MAPIUninitialize)
- Disable build of python and mapiproxy

* Fri Jun 01 2012 Milan Crha <mcrha@redhat.com> - 1.0-7
- Add patch to use system's popt.h
- Add patch to compile only certain parts of the package
- Disable openchange-server for rawhide too (due to samba4 changes)

* Thu May 17 2012 Matthew Barnes <mbarnes@redhat.com> -1.0-6
- Do not build openchange-server in RHEL.
  (And make disabling the subpackage actually work.)

* Wed May 02 2012 Milan Crha <mcrha@redhat.com> - 1.0-5
- Do not include nagios/check_exchange in RHEL

* Tue Apr 24 2012 Milan Crha <mcrha@redhat.com> - 1.0-4
- Bump samba4 dependency

* Thu Apr 19 2012 Matthew Barnes <mbarnes@redhat.com> - 1.0-3
- Add BR: libical-devel (RH bug #803640).

* Wed Apr 18 2012 Milan Crha <mcrha@redhat.com> - 1.0-2
- Bump samba4 dependency

* Tue Apr 03 2012 Milan Crha <mcrha@redhat.com> - 1.0-1
- Update to 1.0
- Enable packages for server part and python bindings
- Skip man3 pages, which are generated incomplete (use devhelp instead)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 30 2011 Milan Crha <mcrha@redhat.com> - 0.11-3
- Fix package version number

* Mon Aug 29 2011 Stephen Gallagher <sgallagh@redhat.com> - 0.11-2.1
- Rebuild against fixed libtevent version

* Mon Aug 29 2011 Milan Crha <mcrha@redhat.com> - 0.11-2
- Sync version and changes with Fedora 16 package

* Thu Aug 11 2011 Milan Crha <mcrha@redhat.com> - 0.11-1
- Update to OpenChange 0.11 Transporter upstream release
- Remove unnecessary build modification patches.
- Add patch to not use mapi_ctx->session as a TALLOC_CTX (OpenChange issue #366)
- Add patch to read/write PidNameKeywords (OpenChange issue #367)

* Wed Apr 6 2011 Matthew Barnes <mbarnes@redhat.com> - 0.10.9-4
- OpenChange relies on a private Samba 4 library (libsamba-util-common).
  Add extra linker flags to libmapi.pc to compensate.

* Wed Apr 6 2011 Matthew Barnes <mbarnes@redhat.com> - 0.10.9-3
- Move libmapiproxy.so, libmapistore.so and mapistore backend libraries
  to the main package so the client subpackage is installable.

* Fri Mar 25 2011 Simo Sorce <ssorce@redhat.com> - 0.10.9-2
- New snapshot that avoid bison issues.
- Also add patch that fix build (previously erroneously preapplied in the
  snapshot tarball)
- Fix timestamps in tarball
- Fix specfile's install and files section to cope with newer version changes

* Fri Mar 25 2011 Simo Sorce <ssorce@redhat.com> - 0.10.9-1
- Upgrade to a 0.11 development snapshot.
- Required by the new samba4 packages.

* Mon Feb 21 2011 Milan Crha <mcrha@redhat.com> - 0.9-14
- Rebuild against newer libldb

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011 Milan Crha <mcrha@redhat.com> - 0.9-12
- Add patch for message sending, found by Gianluca Cecchi (RH bug #674034)

* Thu Dec 16 2010 Matthew Barnes <mbarnes@redhat.com> - 0.9-11
- Re-fix man-pages file conflict (RH bug #654729).

* Thu Dec 02 2010 Milan Crha <mcrha@redhat.com> - 0.9-10
- Add patch for talloc abort in FindGoodServer, found by Jeff Raber (RH bug #602661)

* Wed Sep 29 2010 jkeating - 0.9-9
- Rebuilt for gcc bug 634757

* Mon Sep 13 2010 Matthew Barnes <mbarnes@redhat.com> - 0.9-8
- Backport unicode and properties support (RH bug #605364).

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 24 2010 Matthew Barnes <mbarnes@redhat.com> - 0.9-6
- Disable python and server subpackages until they're needed.

* Wed Jun 23 2010 Matthew Barnes <mbarnes@redhat.com> - 0.9-5
- More spec file cleanups.

* Fri Jun 18 2010 Matthew Barnes <mbarnes@redhat.com> - 0.9-4
- Spec file cleanups.

* Mon May 24 2010 Matthew Barnes <mbarnes@redhat.com> - 0.9-3
- Avoid a file conflict with man-pages package.

* Sat Jan 09 2010 Matthew Barnes <mbarnes@redhat.com> - 0.9-2
- Add a devel-docs subpackage (RH bug #552984).

* Sat Dec 26 2009 Matthew Barnes <mbarnes@redhat.com> - 0.9-1
- Update to 0.9 (COCHRANE)
- Bump samba4 requirement to alpha10.

* Wed Sep 23 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8.2-5
- Rebuild.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8.2-3
- Rename libmapi so as not to conflict with Zarafa (RH bug #505783).

* Thu May 07 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8.2-2
- Do not own the pkgconfig directory (RH bug #499655).

* Tue Mar 31 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8.2-1
- Update to 0.8.2
- Add a server subpackage.
- Add BuildRequires: sqlite-devel (for server)

* Sun Mar 08 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8-6
- Fix build breakage.
- Explicitly require libldb-devel.
- Bump samba4 requirement to alpha7.

* Wed Feb 25 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8-5
- Rebuild with correct tarball.

* Wed Feb 25 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8-4
- Formal package review cleanups.

* Wed Feb 25 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8-3
- Add documentation files.

* Thu Feb 19 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8-2
- Add some missing build requirements.

* Tue Jan 20 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8-1
- Update to 0.8 (ROMULUS)

* Sat Jan 17 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8-0.7.svn949
- Add missing BuildRequires: zlib-devel

* Sat Dec 27 2008 Matthew Barnes <mbarnes@redhat.com> - 0.8-0.6.svn949
- Update to SVN revision 949.

* Mon Dec 15 2008 Matthew Barnes <mbarnes@redhat.com> - 0.8-0.5.svn909
- Package review feedback (RH bug #453395).

* Fri Dec 12 2008 Matthew Barnes <mbarnes@redhat.com> - 0.8-0.4.svn909
- Update to SVN revision 909.
- Bump the samba4 requirement.

* Fri Aug 29 2008 Andrew Bartlett <abartlet@samba.org> - 0:0.8-0.3.svn960.fc9
- Bump version
- Don't make the Samba4 version distro-dependent

* Sat Jul 26 2008 Brad Hards <bradh@frogmouth.net> - 0:0.8-0.2.svnr674.fc10
- Bump version
- Install documentation / man pages correctly
- Remove epoch (per https://bugzilla.redhat.com/show_bug.cgi?id=453395)
- Remove %%post and %%postun (per https://bugzilla.redhat.com/show_bug.cgi?id=453395)
- Remove talloc dependency (per https://bugzilla.redhat.com/show_bug.cgi?id=453395)
- Take out libmapiproxy, because we aren't up to server side yet.

* Sat Jul 12 2008 Andrew Bartlett <abartlet@samba.org> - 0:0.7-0.2.svnr627.fc9
- Add popt-devel BR

* Mon Jun 30 2008 Andrew Bartlett <abartlet@samba.org> - 0:0.7-0.1.svnr627.fc9
- Initial package of OpenChange for Fedora
