# Notes:
# The lcmaps-*-devel packages are meant for developing client
# programs. The preferred model of development is to dlopen() the
# interface library at run-time, which means that a) the libraries are
# not required for development at all and b) client programs become
# independent of the run-time version of LCMAPS.  This is why the
# devel packages only contain header files and the .so symlinks are in
# the run-time package.
#
# The LCMAPS interfaces are:
# -basic, which are very simple and do not require openssl,
# -openssl, which include 'basic' and require openssl for x509 structures,
# -globus, which include 'openssl' and require Globus Toolkit functions.
#
# The lcmaps-devel package is the most inclusive, so it's a safe choice
# to install in case of any development work.

Summary: Grid (X.509) and VOMS credentials to local account mapping service
Name: lcmaps
Version: 1.6.6
Release: 17%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://wiki.nikhef.nl/grid/LCMAPS
Source0: https://software.nikhef.nl/security/lcmaps/lcmaps-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: globus-common-devel
BuildRequires: globus-gssapi-gsi-devel
BuildRequires: globus-gss-assist-devel
BuildRequires: globus-gsi-credential-devel
BuildRequires: globus-gsi-proxy-core-devel
BuildRequires: voms-devel
BuildRequires: flex, bison
BuildRequires: make

%description
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

It is a highly configurable pluggable interface, and many plugins are
available to tailor almost every need. Since this is middleware, it
does not interact with the user directly; to use it in a program please
see the lcmaps-devel package.


%package without-gsi
Summary: Grid mapping service without GSI

%description without-gsi
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

It is a highly configurable pluggable interface, and many plugins are
available to tailor almost every need. Since this is middleware, it
does not interact with the user directly; to use it in a program please
see the lcmaps-devel package.

This version is built without support for the GSI protocol.


%package devel
Summary: LCMAPS plug-in API header files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-common-devel%{?_isa} = %{version}-%{release}
Requires: globus-gssapi-gsi-devel%{?_isa}
Requires: openssl-devel%{?_isa}
Provides: %{name}-globus-interface = %{version}-%{release}
Obsoletes: %{name}-globus-interface < 1.6.1-4
Provides: %{name}-openssl-interface = %{version}-%{release}
Obsoletes: %{name}-openssl-interface < 1.6.1-4
Provides: %{name}-interface = %{version}-%{release}
Obsoletes: %{name}-interface < 1.4.31-1
# the pkgconfig requirement is only necessary for EPEL5 and below;
# it's automatic for Fedora and EPEL6.
%if %{?rhel}%{!?rhel:6} <= 5
Requires: pkgconfig
%endif

%description devel
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

It is a highly configurable pluggable interface, and many plugins are
available to tailor almost every need. Since this is middleware, it
does not interact with the user directly; to use it in a program please
see the lcmaps-devel package.

This package contains the files necessary to compile and link
against the LCMAPS library.


%package common-devel
Summary: LCMAPS plug-in API header files
Provides: %{name}-basic-interface = %{version}-%{release}
Obsoletes: %{name}-basic-interface < 1.6.1-4
# the pkgconfig requirement is only necessary for EPEL5 and below;
# it's automatic for Fedora and EPEL6.
%if %{?rhel}%{!?rhel:6} <= 5
Requires: pkgconfig
%endif

%description common-devel
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

This package contains the header files and interface definitions
for client applications.


%package without-gsi-devel
Summary: LCMAPS development libraries
Requires: %{name}-without-gsi%{?_isa} = %{version}-%{release}
Requires: %{name}-common-devel%{?_isa} = %{version}-%{release}
# the pkgconfig requirement is only necessary for EPEL5 and below;
# it's automatic for Fedora and EPEL6.
%if %{?rhel}%{!?rhel:6} <= 5
Requires: pkgconfig
%endif

%description without-gsi-devel
The Local Centre MAPping Service (LCMAPS) is a security middleware
component that processes the users Grid credentials (typically X.509
proxy certificates and VOMS attributes) and maps the user to a local
account based on the site local policy.

It is a highly configurable pluggable interface, and many plugins are
available to tailor almost every need. Since this is middleware, it
does not interact with the user directly; to use it in a program please
see the lcmaps-devel package.

This package contains the development libraries to build
without the GSI protocol.


%prep
%setup -q

%build

# First configure and build the without-gsi version
mkdir build-without-gsi && cd build-without-gsi && ln -s ../configure
%configure --disable-gsi-mode --disable-static

# The following lines were suggested by
# https://fedoraproject.org/wiki/Packaging/Guidelines to prevent any
# RPATHs creeping in, and by
# https://fedoraproject.org/wiki/Common_Rpmlint_issues#unused-direct-shlib-dependency
# to prevent unnecessary linking
%define fixlibtool() sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool\
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool\
sed -i -e 's! -shared ! -Wl,--as-needed\\0!g' libtool

%fixlibtool
make %{?_smp_mflags}
cd ..

# configure and build the full version
mkdir build && cd build && ln -s ../configure
%{configure} --disable-static
%fixlibtool
make %{?_smp_mflags}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

# install the without-gsi version
cd build-without-gsi
make DESTDIR=$RPM_BUILD_ROOT install
cd ..

# install the full version
cd build
make DESTDIR=$RPM_BUILD_ROOT install
cd ..

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# create empty lcmaps.db directory
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/lcmaps
# create empty plugin directory
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/lcmaps

# clean up installed files
rm -rf ${RPM_BUILD_ROOT}%{_docdir}

%ldconfig_scriptlets

%ldconfig_scriptlets without-gsi

%files
# The libraries are meant to be dlopened by client applications,
# so the .so symlinks are here and not in devel.
%{_libdir}/liblcmaps.so
%{_libdir}/liblcmaps.so.0
%{_libdir}/liblcmaps.so.0.0.0
%{_libdir}/liblcmaps_gss_assist_gridmap.so
%{_libdir}/liblcmaps_gss_assist_gridmap.so.0
%{_libdir}/liblcmaps_gss_assist_gridmap.so.0.0.0
%{_libdir}/liblcmaps_return_account_from_pem.so
%{_libdir}/liblcmaps_return_account_from_pem.so.0
%{_libdir}/liblcmaps_return_account_from_pem.so.0.0.0
%{_libdir}/liblcmaps_return_poolindex.so
%{_libdir}/liblcmaps_return_poolindex.so.0
%{_libdir}/liblcmaps_return_poolindex.so.0.0.0
%{_libdir}/liblcmaps_verify_account_from_pem.so
%{_libdir}/liblcmaps_verify_account_from_pem.so.0
%{_libdir}/liblcmaps_verify_account_from_pem.so.0.0.0
%{_mandir}/man3/lcmaps.3*
%dir %{_libdir}/lcmaps
%dir %{_sysconfdir}/lcmaps
%doc BUGS AUTHORS LICENSE README README.NO_LDAP NEWS
%doc build/etc/lcmaps.db build/etc/groupmapfile build/etc/vomapfile

%files without-gsi
# These libraries are dlopened, so the .so symlinks cannot be in devel
%{_libdir}/liblcmaps_without_gsi.so
%{_libdir}/liblcmaps_without_gsi.so.0
%{_libdir}/liblcmaps_without_gsi.so.0.0.0
%{_libdir}/liblcmaps_return_poolindex_without_gsi.so
%{_libdir}/liblcmaps_return_poolindex_without_gsi.so.0
%{_libdir}/liblcmaps_return_poolindex_without_gsi.so.0.0.0
%{_libdir}/liblcmaps_gss_assist_gridmap_without_gsi.so
%{_libdir}/liblcmaps_gss_assist_gridmap_without_gsi.so.0
%{_libdir}/liblcmaps_gss_assist_gridmap_without_gsi.so.0.0.0
%{_mandir}/man3/lcmaps.3*
%dir %{_libdir}/lcmaps
%dir %{_sysconfdir}/lcmaps
%doc BUGS AUTHORS LICENSE README README.NO_LDAP NEWS
%doc build-without-gsi/etc/lcmaps.db
%doc build-without-gsi/etc/groupmapfile
%doc build-without-gsi/etc/vomapfile

%files devel
%{_includedir}/lcmaps/lcmaps_return_poolindex.h
%{_includedir}/lcmaps/_lcmaps_return_poolindex.h
%{_includedir}/lcmaps/lcmaps.h
%{_includedir}/lcmaps/lcmaps_globus.h
%{_includedir}/lcmaps/lcmaps_openssl.h
%{_datadir}/pkgconfig/lcmaps-openssl-interface.pc
%{_datadir}/pkgconfig/lcmaps-globus-interface.pc
%{_datadir}/pkgconfig/lcmaps-interface.pc
%{_libdir}/pkgconfig/lcmaps-gss-assist-gridmap.pc
%{_libdir}/pkgconfig/lcmaps-return-account-from-pem.pc
%{_libdir}/pkgconfig/lcmaps-return-poolindex.pc
%{_libdir}/pkgconfig/lcmaps-verify-account-from-pem.pc
%{_libdir}/pkgconfig/lcmaps.pc
%doc LICENSE

%files common-devel
%dir %{_includedir}/lcmaps
%{_includedir}/lcmaps/lcmaps_version.h
%{_includedir}/lcmaps/lcmaps_account.h
%{_includedir}/lcmaps/lcmaps_arguments.h
%{_includedir}/lcmaps/lcmaps_basic.h
%{_includedir}/lcmaps/lcmaps_cred_data.h
%{_includedir}/lcmaps/lcmaps_db_read.h
%{_includedir}/lcmaps/lcmaps_defines.h
%{_includedir}/lcmaps/_lcmaps_gss_assist_gridmap.h
%{_includedir}/lcmaps/lcmaps_gss_assist_gridmap.h
%{_includedir}/lcmaps/_lcmaps.h
%{_includedir}/lcmaps/lcmaps_if.h
%{_includedir}/lcmaps/lcmaps_log.h
%{_includedir}/lcmaps/lcmaps_modules.h
%{_includedir}/lcmaps/_lcmaps_return_account_from_pem.h
%{_includedir}/lcmaps/lcmaps_return_account_from_pem.h
%{_includedir}/lcmaps/lcmaps_types.h
%{_includedir}/lcmaps/lcmaps_utils.h
%{_includedir}/lcmaps/_lcmaps_verify_account_from_pem.h
%{_includedir}/lcmaps/lcmaps_verify_account_from_pem.h
%{_includedir}/lcmaps/lcmaps_vo_data.h
%{_includedir}/lcmaps/lcmaps_return_poolindex_without_gsi.h
%{_includedir}/lcmaps/lcmaps_plugin_typedefs.h
%{_includedir}/lcmaps/lcmaps_plugin_prototypes.h
%{_datadir}/pkgconfig/lcmaps-basic-interface.pc
%doc LICENSE

%files without-gsi-devel
%{_libdir}/pkgconfig/lcmaps-return-poolindex-without-gsi.pc
%{_libdir}/pkgconfig/lcmaps-gss-assist-gridmap-without-gsi.pc
%{_libdir}/pkgconfig/lcmaps-without-gsi.pc
%doc LICENSE


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul  24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.6-16
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 20 2024 Mischa Sallé <msalle@nikhef.nl> - 1.6.6-14
- Use https for source URL and URL

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.6.6-7
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb  5 2019 Dennis van Dok <dennisvd@nikhef.nl> 1.6.6-1
- Update to version 1.6.6

* Mon Feb  4 2019 Mischa Sallé <msalle@nikhef.nl> 1.6.5-11
- Update globus dependencies

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep 17 2014 Dennis van Dok <dennisvd@nikhef.nl> 1.6.5-2
- Compounded the changelog entries of intermediate versions

* Wed Sep 17 2014  Mischa Salle <msalle@nikhef.nl> 1.6.5-1
- Do not install very old doc/INSTALL_WITH_WORKSPACE_SERVICE
- Install NEWS file
- Fix macro expansion for pkgconfig to include only rhel not fedora
- Add new interface files, Remove the unused patch
- Create empty plugin directory
- Do not remove lcmaps_plugin_example related files, as they are not installed

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 25 2013 Dennis van Dok <dennisvd@nikhef.nl> 1.6.1-7
- Patch the example DB file so it doesn't contain an
  architecture-specific path. Fixes bug #1034019.

* Tue Nov 12 2013 Dennis van Dok <dennisvd@nikhef.nl> 1.6.1-6
- Make requirements arch-specific for devel package

* Mon Nov 11 2013 Dennis van Dok <dennisvd@nikhef.nl> 1.6.1-5
- put BuildRoot and clean section back in for EPEL5
- Add requirement on pkgconfig for EPEL5
- Include Provides/Obsoletes to rename interface packages

* Wed Oct 30 2013 Dennis van Dok <dennisvd@nikhef.nl> 1.6.1-3
- Reduced the number of development packages

* Wed Oct 23 2013 Dennis van Dok <dennisvd@nikhef.nl> 1.6.1-2
- Renamed the -interface packages to -devel
- Dropped buildroot and defattr

* Wed Feb 27 2013 Mischa Salle <msalle@nikhef.nl> 1.6.1-1
- install BUGS as doc
- updated version

* Tue Feb 26 2013 Mischa Salle <msalle@nikhef.nl> 1.6.0-1
- updated version

* Tue Oct 23 2012 Mischa Salle <msalle@nikhef.nl> 1.5.7-1
- Do not install INSTALL in doc.
- Update URL.
- updated version

* Fri Jul  6 2012 Mischa Salle <msalle@nikhef.nl> 1.5.6-1
- updated version

* Mon Apr 23 2012 Mischa Salle <msalle@nikhef.nl> 1.5.5-1
- build both with and without gsi packages in one spec file
- updated version

* Mon Mar 26 2012 Mischa Salle <msalle@nikhef.nl> 1.5.4-1
- updated version

* Fri Mar 16 2012 Mischa Salle <msalle@nikhef.nl> 1.5.3-1
- updated version

* Mon Jan 30 2012 Mischa Salle <msalle@nikhef.nl> 1.5.2-3
- add manpage in main package
- updated version

* Wed Dec 14 2011 Mischa Salle <msalle@nikhef.nl> 1.5.0-1

* Tue Sep 20 2011 Mischa Salle <msalle@nikhef.nl> 1.4.33-1
- updated version
- added obsoletes for lcmaps-interface

* Fri Sep 16 2011 Mischa Salle <msalle@nikhef.nl> 1.4.32-1
- updated version

* Tue Sep 13 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.31-5
- Repaired the unintended post macro in the changelog

* Wed Aug 10 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.31-4
- Split interface according to dependencies on globus and openssl

* Wed Jul 20 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.30-2
- Moved the .so files to the runtime package as these are dlopened

* Wed Jul 13 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.30-1
- updated version

* Mon Jul  4 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.4.29-2
- Make interface package noarch
- Remove Vendor tag

* Mon Jul  4 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.29-1
- Updated version

* Wed Mar 23 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.28-2
- removed explicit requires

* Wed Mar  9 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.28-1
- Made examples out of config files

* Tue Mar  8 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.27-2
- Disable rpath in configure

* Mon Mar  7 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.27-1
- Fixed globus dependencies
- added ldconfig to post and postun section

* Fri Mar  4 2011 Dennis van Dok <dennisvd@nikhef.nl> 1.4.26-3
- disabled static libraries
- added proper base package requirement for devel
- fixed license string

* Mon Feb 21 2011 Dennis van Dok <dennisvd@nikhef.nl>
- Initial build.
