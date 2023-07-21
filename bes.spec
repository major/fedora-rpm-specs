%global bescachedir %{_localstatedir}/cache/%{name}
%global bespkidir %{_sysconfdir}/pki/%{name}
%global beslogdir %{_localstatedir}/log/%{name}
%global besuser %{name}
%global besgroup %{name}

%global commit 20781c060611626c4fbf9788510fd8a5794a2dcc

Name:           bes
Version:        3.20.13
Release:        10%{?dist}
Summary:        Back-end server software framework for OPeNDAP

License:        LGPLv2+
URL:            https://github.com/OPENDAP/bes
Source0:        http://www.opendap.org/pub/source/bes-%{version}.tar.gz
Source1:        bes.service
# Fix link
Patch1:         bes-link.patch
# Use int32 type
Patch2:         bes-int32.patch
# Fix configure test compromised by LTO
Patch3:		bes-config.patch
Patch4: bes-c99.patch

BuildRequires:  gcc-c++
BuildRequires:  make
# For autoreconf
BuildRequires:  libtool
BuildRequires:  libdap-devel >= 3.20.10
BuildRequires:  bzip2-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libuuid-devel
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
# needed by ppt
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  doxygen graphviz
BuildRequires:  systemd
# For modules
BuildRequires:  cfitsio-devel
# swath2grid with gdal currently fails to build
BuildRequires:  gdal-devel
BuildRequires:  hdf-static
BuildRequires:  hdf5-devel
BuildRequires:  libicu-devel
BuildRequires:  netcdf-devel
# For tests
BuildRequires:  cppunit-devel
# To remove rpath due to https://github.com/OPENDAP/bes/issues/565
BuildRequires:  chrpath

Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# Don't provide modules
%global __provides_exclude_from ^%{_libdir}/bes/.*\\.so$
%global __requires_exclude ^libdap_module\\.so.*$

# Obsolete the separate handlers
Obsoletes:      dap-freeform_handler < 3.8.8-3
Provides:       dap-freeform_handler = 3.8.8-3
Obsoletes:      dap-hdf4_handler < 3.11.5-3
Provides:       dap-hdf4_handler = 3.11.5-3
Obsoletes:      dap-netcdf_handler < 3.10.4-3
Provides:       dap-netcdf_handler = 3.10.4-3
Obsoletes:      dap-server < 4.1.6-3
Provides:       dap-server = 4.1.6-3

%description
BES is a high-performance back-end server software framework for 
OPeNDAP that allows data providers more flexibility in providing end 
users views of their data. The current OPeNDAP data objects (DAS, DDS, 
and DataDDS) are still supported, but now data providers can add new data 
views, provide new functionality, and new features to their end users 
through the BES modular design. Providers can add new data handlers, new 
data objects/views, the ability to define views with constraints and 
aggregation, the ability to add reporting mechanisms, initialization 
hooks, and more.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libdap-devel%{?_isa} >= 3.13.0
# for the /usr/share/aclocal directory ownership
Requires:       automake
Requires:       bzip2-devel%{?_isa}
Requires:       libtirpc-devel%{?_isa}
Requires:       openssl-devel%{?_isa}
Requires:       zlib-devel%{?_isa}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package doc
Summary: Documentation of the OPeNDAP BES

%description doc
Documentation of OPeNDAP BES.


%prep
%setup -q -n bes-%{version}
%patch1 -p1 -b .link
%patch2 -p1 -b .int32
%patch3 -p1 -b .config
%patch4 -p1

# Fixes rpaths
autoreconf --install
chmod a-x dispatch/BESStreamResponseHandler*

%build
# We need to enable static builds so it can link against libdap_module.a
%configure --disable-dependency-tracking \
  --with-cfits-inc=%{_includedir} --with-cfits-libdir=%{_libdir} \
  CPPFLAGS="-I%{_includedir}/cfitsio -I%{_includedir}/tirpc" LDFLAGS=-L%{_libdir}/libdap LIBS=-ltirpc
# This fails currently: --without-dap-modules
%make_build

make docs
rm -rf __distribution_docs
cp -pr docs __distribution_docs
chmod a-x __distribution_docs/BES_*.doc
mv html __distribution_docs/api-html
# .map and .md5 files are of dubious use
find \( -name \*.map -o -name \*.md5 \) -delete

sed -i.dist -e 's:=/tmp:=%{bescachedir}:' \
  -e 's:=.*/bes.log:=%{beslogdir}/bes.log:' \
  -e 's:=/full/path/to/serverside/certificate/file.pem:=%{bespkidir}/cacerts/file.pem:' \
  -e 's:=/full/path/to/serverside/key/file.pem:=%{bespkidir}/public/file.pem:' \
  -e 's:=/full/path/to/clientside/certificate/file.pem:=%{bespkidir}/cacerts/file.pem:' \
  -e 's:=/full/path/to/clientside/key/file.pem:=%{bespkidir}/public/file.pem:' \
  -e 's:=user_name:=%{besuser}:' \
  -e 's:=group_name:=%{besgroup}:' \
  dispatch/bes/bes.conf

%install
%make_install
find $RPM_BUILD_ROOT \( -name '*.la' -o -name '*.a' \) -exec rm -f {} ';'
mkdir -p $RPM_BUILD_ROOT%{bescachedir}
mkdir -p $RPM_BUILD_ROOT%{bespkidir}/{cacerts,public}
mkdir -p $RPM_BUILD_ROOT%{beslogdir}
mv $RPM_BUILD_ROOT%{_bindir}/bes-config-pkgconfig $RPM_BUILD_ROOT%{_bindir}/bes-config
# Use systemd instead
rm -r ${RPM_BUILD_ROOT}/etc/rc.d
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
cp -p %SOURCE1 $RPM_BUILD_ROOT%{_unitdir}/bes.service
mkdir -p $RPM_BUILD_ROOT%{_tmpfilesdir}
mv $RPM_BUILD_ROOT%{_bindir}/bes-tmpfiles-conf $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
chrpath -d $RPM_BUILD_ROOT%{_bindir}/build_dmrpp


%check
make check || cat modules/*_handler/bes-testsuite/*.log || cat */tests/*.log || cat */unit-tests/test-suite.log


%pre
getent group %{besgroup} >/dev/null || groupadd -r %{besgroup}
getent passwd %{besuser} >/dev/null || \
useradd -r -g %{besuser} -d %{beslogdir} -s /sbin/nologin \
    -c "BES daemon" %{besuser}
exit 0

%post
/sbin/ldconfig
%systemd_post bes.service

%preun
%systemd_preun bes.service

%postun
/sbin/ldconfig
%systemd_postun_with_restart bes.service 


%files
%license COPYING
%doc ChangeLog NEWS README.md
%dir %{_sysconfdir}/bes/
%config(noreplace) %{_sysconfdir}/bes/bes.conf
%config(noreplace) %{_sysconfdir}/bes/site.conf.proto
%config(noreplace) %{_sysconfdir}/bes/modules/
%config(noreplace) %{_sysconfdir}/logrotate.d/
%{_unitdir}/bes.service
%{_tmpfilesdir}/bes.conf
%dir %{_datadir}/bes
%{_datadir}/bes/*.html
%{_datadir}/bes/*.txt
%{_datadir}/bes/*.xml
%{_datadir}/hyrax/
%{_bindir}/bescmdln
%{_bindir}/besctl
%{_bindir}/besdaemon
%{_bindir}/beslistener
%{_bindir}/besstandalone
%{_bindir}/build_dmrpp
%{_bindir}/check_dmrpp
%{_bindir}/get_dmrpp
%{_bindir}/hyraxctl
%{_bindir}/ingest_filesystem
%{_bindir}/ingest_s3bucket
%{_bindir}/localBesGetDap
%{_bindir}/merge_dmrpp
%{_bindir}/populateMDS
%{_bindir}/reduce_mdf
%{_libdir}/*.so.*
%{_libdir}/bes/
%{bescachedir}
%{bespkidir}/
%attr (-,%{besuser},%{besgroup}) %{beslogdir}
%attr (-,%{besuser},%{besgroup}) %{_datadir}/mds/

%files devel
%doc __distribution_docs/BES_*.doc
%{_bindir}/besCreateModule
%{_bindir}/bes-config
%{_includedir}/bes/
%{_libdir}/*.so
%{_libdir}/pkgconfig/bes_*.pc
%{_datadir}/bes/templates/
%{_datadir}/aclocal/bes.m4

%files doc
%license COPYING
%doc __distribution_docs/api-html/

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 3.20.13-9
- Rebuilt for ICU 73.2

* Thu May 11 2023 Sandro Mani <manisandro@gmail.com> - 3.20.13-8
- Rebuild (gdal)

* Thu Feb 23 2023 Florian Weimer <fweimer@redhat.com> - 3.20.13-7
- Port to C99

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Maxwell G <gotmax@e.email> - 3.20.13-5
- Rebuild for cfitsio 4.2

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 3.20.13-4
- Rebuild for ICU 72

* Thu Dec 29 2022 Maxwell G <gotmax@e.email> - 3.20.13-3
- Rebuild for cfitsio 4.2

* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 3.20.13-2
- Rebuild (gdal)

* Sun Oct 02 2022 Orion Poplawski <orion@nwra.com> - 3.20.13-1
- Update to 3.20.13

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 3.20.10-6
- Rebuilt for ICU 71.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 01 2022 Orion Poplawski <orion@nwra.com> - 3.20.10-4
- Add patch to include needed time.h header

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 3.20.10-3
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Orion Poplawski <orion@nwra.com> - 3.20.10-1
- Update to 3.20.10

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 3.20.8-4
- Rebuild (gdal)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.20.8-3
- Rebuilt with OpenSSL 3.0.0

* Tue Aug 17 2021 Orion Poplawski <orion@nwra.com> - 3.20.8-2
- Exclude private libdap_module from requires (bz#1993861)

* Mon Aug 09 2021 Orion Poplawski <orion@nwra.com> - 3.20.8-1
- Update to 3.20.8

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Sandro Mani <manisandro@gmail.com> - 3.20.6-14
- Rebuild (gdal)

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 3.20.6-13
- Rebuild for ICU 69

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 3.20.6-12
- Rebuild (gdal)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.20.6-11
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Feb 03 2021 Orion Poplawski <orion@nwra.com> - 3.20.6-10
- Rebuild for cfitsio 3.490

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov  6 21:35:42 CET 2020 Sandro Mani <manisandro@gmail.com> - 3.20.6-8
- Rebuild (proj, gdal)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Jeff Law <law@redhat.com> - 3.20.6-6
- Fix configure test compromised by LTO

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 3.20.6-5
- Rebuild for hdf5 1.10.6

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 3.20.6-4
- Rebuild (gdal)

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 3.20.6-3
- Rebuild for ICU 67

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 3.20.6-2
- Rebuild (gdal)

* Sat Feb 08 2020 Orion Poplawski <orion@nwra.com> - 3.20.6-1
- Update to 3.20.6

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 3.20.5-2
- Rebuild for ICU 65

* Sat Oct 26 2019 Orion Poplawski <orion@nwra.com> - 3.20.5-1
- Add patch to fix getopt() calls

* Mon Jul 29 2019 Orion Poplawski <orion@nwra.com> - 3.20.5-1
- Update to 3.20.5

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Orion Poplawski <orion@nwra.com> - 3.20.1-1
- Update to 3.20.1

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.19.1-6
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 3.19.1-4
- Rebuild for ICU 63

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 3.19.1-2
- Rebuild for ICU 62

* Fri Jun 22 2018 Orion Poplawski <orion@cora.nwra.com> - 3.19.1-1
- Update to 3.19.1
- Add patch for icu 61.1.  Fixes FTBFS (bug #1582724)

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 3.17.4-9
- rebuilt for cfitsio 3.450

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 3.17.4-8
- Rebuild for ICU 61.1

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 3.17.4-7
- rebuilt for cfitsio 3.420 (so version bump)

* Wed Feb 14 2018 Orion Poplawski <orion@nwra.com> - 3.17.4-6
- Use libtirpc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 3.17.4-5
- Rebuild for ICU 60.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Orion Poplawski <orion@cora.nwra.com> - 3.17.4-1
- Update to 3.17.4

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.17.3-2
- Rebuild for readline 7.x

* Tue Dec 6 2016 Orion Poplawski <orion@cora.nwra.com> - 3.17.3-1
- Update to 3.17.3

* Fri Aug 12 2016 Orion Poplawski <orion@cora.nwra.com> - 3.17.1-1
- Update to 3.17.1
- Drop gcc6 patch applied upstream

* Mon Apr 18 2016 Orion Poplawski <orion@cora.nwra.com> - 3.17.0-3
- Rebuild for libdap 3.17.2
- Use %%license

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 3.17.0-2
- rebuild for ICU 57.1

* Sat Feb 13 2016 Orion Poplawski <orion@cora.nwra.com> - 3.17.0-1
- Update to 3.17.0
- Add patch for gcc 6 support

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> - 3.16.0-2
- Rebuild for hdf5 1.8.16

* Thu Jan 14 2016 Orion Poplawski <orion@cora.nwra.com> - 3.16.0-1
- Update to 3.16.0

* Sat Dec 12 2015 Orion Poplawski <orion@cora.nwra.com> - 3.14.0-8
- BR hdf-static (bug #1284296)

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 3.14.0-7
- rebuild for ICU 56.1

* Sat Sep 19 2015 Orion Poplawski <orion@cora.nwra.com> - 3.14.0-6
- Bump dap-server obsolete/provide (bug #1213600)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Orion Poplawski <orion@cora.nwra.com> - 3.14.0-4
- Rebuild for hdf5 1.8.15

* Mon Apr 20 2015 Orion Poplawski <orion@cora.nwra.com> - 3.14.0-3
- Build and obsolete/provide modules (bug #1213600)
- Disable modules failing tests
- Add patch to fix gdal detection, unused for now due to build failure
- Fix linking of xml_command
- Run autoreconf to fix rpaths

* Sun Apr 19 2015 Orion Poplawski <orion@cora.nwra.com> - 3.14.0-2
- Filter modules from provides
- Add patch to not build netcdf dependent modules
- Run tests

* Thu Apr 16 2015 Orion Poplawski <orion@cora.nwra.com> - 3.14.0-1
- Update to 3.14.0
- Add patch to fix getopt() usage
- Add systemd unit file

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 10 2014 Orion Poplawski <orion@cora.nwra.com> - 3.13.1-1
- Update to 3.13.1
- Drop includes patch applied upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 6 2013 Orion Poplawski <orion@cora.nwra.com> - 3.11.0-1
- Update to 3.11.0
- Add patches to add missing includes, fix some linking
- spec cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-2
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Orion Poplawski <orion@cora.nwra.com> - 3.9.2-1
- Update to 3.9.2
- Add patch to support gcc 4.7

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 8 2011 Orion Poplawski <orion@cora.nwra.com> - 3.9.0-1
- Update to 3.9.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 15 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.4-3
- Drop BR libuuid-devel

* Thu Jul 15 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.4-2
- Rebuild for libdap soname bump

* Tue Jul 13 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.4-1
- Update to 3.8.4
- Drop includes patch fixed upstream
- Rebase openssl patch
- Add COPYING to main package and -doc subpackage

* Sat Aug 22 2009 Tomas Mraz <tmraz@redhat.com> - 3.7.2-3
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Orion Poplawski <orion@cora.nwra.com> - 3.7.2-1
- update to 3.7.2, enable tcp_wrapper support
- Drop gcc43 patch fixed upstream

* Wed Mar 04 2009 Caolán McNamara <caolanm@redhat.com> - 3.6.2-4
- include cstdio for std::snprintf

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> 3.6.2-2
- rebuild with new openssl

* Fri Sep  5 2008 Patrice Dumas <pertusus@free.fr> 3.6.2-1
- update to 3.6.2

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.5.3-4
- Autorebuild for GCC 4.3

* Wed Jan  2 2008 Patrice Dumas <pertusus@free.fr> 3.5.3-3
- Add Requires openssl-devel and zlib-devel since it is in bes-config --libs

* Mon Dec 17 2007 Patrice Dumas <pertusus@free.fr> 3.5.3-2
- update to 3.5.3

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 3.5.1-4
 - Rebuild for deps

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 3.5.1-3
- Rebuild for selinux ppc32 issue.

* Fri Jun  8 2007 Patrice Dumas <pertusus@free.fr> 3.5.1-2
- BuildRequires graphviz

* Sun Jun  3 2007 Patrice Dumas <pertusus@free.fr> 3.5.1-1
- update to 3.5.1

* Fri Dec  8 2006 Patrice Dumas <pertusus@free.fr> 3.2.0-2
- set License to LGPL

* Fri Dec  8 2006 Patrice Dumas <pertusus@free.fr> 3.2.0-2
- add BuildRequires for readline-devel and openssl-devel

* Sat Jul 22 2006 Patrice Dumas <pertusus@free.fr> 3.2.0-1
- initial packaging
