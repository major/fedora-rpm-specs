%global tests_enabled 0

Name:           getdata
Version:        0.11.0
Release:        11%{?dist}
Summary:        Library for reading and writing dirfile data

License:        GPL-2.0-or-later
URL:            http://getdata.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:     gcc-gfortran libtool-ltdl-devel
BuildRequires:     bzip2-devel zlib-devel xz-devel zziplib-devel flac-devel
%ifarch %{ix86} x86_64
#slim is only available on ix86 and x86_64
BuildRequires:     slimdata-devel
%endif
BuildRequires: make

%description
The GetData Project is the reference implementation of the Dirfile Standards,
a filesystem-based database format for time-ordered binary data. The Dirfile
database format is designed to provide a fast, simple format for storing and
reading data.

%package devel
Summary: Headers required when building programs against getdata
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: gcc-gfortran%{_isa}

%description devel
Headers required when building a program against the GetData library.
Includes C++ and FORTRAN (77 & 95) bindings. 

%package fortran
Summary: getdata bindings for fortran
Requires: %{name} = %{version}-%{release}

%description fortran
The GetData library for fortran programs.  

%package gzip
Summary: Enables getdata read ability of gzip compressed dirfiles
Requires: %{name} = %{version}-%{release}

%description gzip
Enables getdata to read dirfiles that are encoded (compressed) with gzip.
Fields must be fully compressed with gzip, not actively being written to.
Does not yet allow writing of gzip encoded dirfiles.  

%package bzip2
Summary: Enables getdata read ability of bzip2 compressed dirfiles
Requires: %{name} = %{version}-%{release}

%description bzip2
Enables getdata to read dirfiles that are encoded (compressed) with bzip2.
Fields must be fully compressed with bzip2, not actively being written to.
Does not yet allow writing of bzip2 encoded dirfiles.

%ifarch %{ix86} x86_64 #slim is only available on for these.
%package slim
Summary: Enables getdata read ability of slim compressed dirfiles
Requires: %{name} = %{version}-%{release}

%description slim
Enables getdata to read dirfiles that are encoded (compressed) with slimdata.
%endif

%package lzma
Summary: Enables getdata read ability of lzma compressed dirfiles
Requires: %{name} = %{version}-%{release}

%description lzma
Enables getdata to read dirfiles that are encoded (compressed) with lzma.

%prep
%setup -q

%build
# FIXME: FFLAGS/FCFLAGS are not being honored; looking into it with upstream.
export FCFLAGS="$FCFLAGS -fallow-argument-mismatch"
%configure --disable-static --enable-modules --disable-perl --disable-python

# removing rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%if %{tests_enabled}
%check
LD_LIBRARY_PATH="%{buildroot}/%{_libdir}:%{buildroot}/%{_libdir}/getdata" make check
%endif

%install
mkdir -p %{buildroot}
make DESTDIR=%{buildroot} SUID_ROOT="" install
# Remove .la files.  
rm -f %{buildroot}/%{_libdir}/lib*.la
rm -f %{buildroot}/%{_libdir}/getdata/lib*.la
# Remove simple docs, as we install them ourselves (along with others)
rm -f %{buildroot}/%{_datadir}/doc/%{name}/*
# Place fortran module in the correct location
mkdir -p %{buildroot}/%{_fmoddir}
mv %{buildroot}/%{_includedir}/getdata.mod  %{buildroot}/%{_fmoddir}/

%ldconfig_scriptlets

%files
%doc README NEWS COPYING AUTHORS TODO ChangeLog
%{_bindir}/dirfile2ascii
%{_bindir}/checkdirfile
%{_libdir}/libgetdata++.so.7*
%{_libdir}/libgetdata.so.8*

%dir %{_libdir}/getdata
%{_libdir}/getdata/libgetdataflac-0.11.0.so
%{_libdir}/getdata/libgetdatazzip-0.11.0.so
%{_mandir}/man5/*
%{_mandir}/man1/*

%files fortran
%{_libdir}/libf95getdata.so.7*
%{_libdir}/libfgetdata.so.6*

%files devel
%doc doc/README.cxx doc/README.f77 doc/unclean_database_recovery.txt
%{_libdir}/libgetdata.so
%{_libdir}/libf*getdata.so
%{_libdir}/libgetdata++.so
%{_includedir}/*
%{_mandir}/man3/*
%{_libdir}/pkgconfig/getdata.pc
%{_fmoddir}/getdata.mod
%{_libdir}/getdata/libgetdataflac.so
%{_libdir}/getdata/libgetdatazzip.so

%files gzip
%{_libdir}/getdata/libgetdatagzip.so
%{_libdir}/getdata/libgetdatagzip-0.11.0.so

%files bzip2
%{_libdir}/getdata/libgetdatabzip2.so
%{_libdir}/getdata/libgetdatabzip2-0.11.0.so

%ifarch %{ix86} x86_64
%files slim
%{_libdir}/getdata/libgetdataslim.so
%{_libdir}/getdata/libgetdataslim-0.11.0.so
%endif

%files lzma
%{_libdir}/getdata/libgetdatalzma.so
%{_libdir}/getdata/libgetdatalzma-0.11.0.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.11.0-6
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 13 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.11.0-4
- Rebuilt for flac 1.4.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.11.0-1
- 0.11.0
- Spec cleanup.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.10.0-13
- Fix FTBFS

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.10.0-9
- Drop python2.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.0-5
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.0-4
- Python 2 binary package renamed to python2-getdata
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 07 2017 Jon Ciesla <limburgher@gmail.com> - 0.10.0-1
- 0.10.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 16 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.4-2
- Rebuild (aarch64)

* Sat Sep 10 2016 Dan Horák <dan[at]danny.cz> - 0.9.4-1
- Updating to 0.9.4 (#1309917)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 Jaromir Capik <jcapik@redhat.com> - 0.9.0-1
- Updating to 0.9.0 (#1272626)

* Fri Aug 07 2015 Jaromir Capik <jcapik@redhat.com> - 0.8.9-1
- Updating to 0.8.9 (#1220587)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.6-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Jan 29 2015 Jaromir Capik <jcapik@redhat.com> - 0.8.6-1
- Update to 0.8.6 (#1175153)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 11 2013 Jaromir Capik <jcapik@redhat.com> - 0.8.5-1
- Update to 0.8.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Jaromir Capik <jcapik@redhat.com> - 0.8.4-1
- Update to 0.8.4

* Tue Mar 19 2013 Jaromir Capik <jcapik@redhat.com> - 0.8.3-1
- Update to 0.8.3

* Mon Jan 28 2013 Jaromir Capik <jcapik@redhat.com> - 0.8.2-1
- Update to 0.8.2
- Removing rpath

* Thu Sep 27 2012 Jaromir Capik <jcapik@redhat.com> - 0.8.1-1
- Update to 0.8.1
- Minor spec file changes according to the latest guidelines

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Apr 7 2011 Matthew Truch <matt at truch.net> - 0.7.3-0
- Upstream 0.7.3.  Several bugfixes.  

* Thu Feb 17 2011 Matthew Truch <matt at truch.net> - 0.7.1-0
- Upstream 0.7.1 release.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Mar 5 2010 Matthew Truch <matt at truch.net> - 0.6.3-1
- Upstream 0.6.3.

* Tue Feb 16 2010 Matthew Truch <matt at truch.net> - 0.6.2-1
- Upstream 0.6.2.  Fixes serious memory corruption bug in legacy API.

* Fri Feb 12 2010 Matthew Truch <matt at truch.net> - 0.6.1-2
- Bump for no reason.

* Fri Feb 12 2010 Matthew Truch <matt at truch.net> - 0.6.1-1
- Upstream 0.6.1.

* Wed Feb 10 2010 Matthew Truch <matt at truch.net> - 0.6.1-0rc2.1
- Upstream -rc2 which includes upstreamed patches to fix build and test issues.

* Sun Feb 7 2010 Matthew Truch <matt at truch.net> - 0.6.1-0rc1.2
- Include missing files in buildsys.

* Wed Feb 3 2010 Matthew Truch <matt at truch.net> - 0.6.1-0rc1
- Upstream 0.6.1rc1
-  Fixes minor bugs.
-  Fixes build issues with recent gcc discovered with Fedora buildsystem.

* Sat Jan 30 2010 Matthew Truch <matt at truch.net> - 0.6.0-2
- Use proper URL for Source0 at sourceforge.

* Tue Nov 3 2009 Matthew Truch <matt at truch.net> - 0.6.0-1
- Upstream 0.6.0 release.
- Split fortran dependancy into a sub-package.

* Mon Nov 2 2009 Matthew Truch <matt at truch.net> - 0.6.0-0rc4
- Upstream 0.6.0 release candidate 4.
- Include new numpy support in python bindings.
- Put python bindings in their own sub-package.

* Mon Oct 19 2009 Matthew Truch <matt at truch.net> - 0.6.0-0rc3
- Upstream 0.6.0 release candidate 3.
- Properly deal with slim's limited arch availability.

* Wed Oct 14 2009 Matthew Truch <matt at truch.net> - 0.6.0-0rc2
- Upstream 0.6.0 release candidate 2.
- Remove patch which is included in upstream release.
- Activate python bindings.
- Enable slimdata and lzma encoded dirfile read ability.

* Mon Sep 21 2009 Matthew Truch <matt at truch.net> - 0.5.0-5
- Include bugfix from upstream.
- Put fortran module in correct place. BZ 523539

* Mon Jul 27 2009 Matthew Truch <matt at truch.net> - 0.5.0-4
- Disable verbose debugging output.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Matthew Truch <matt at truch.net> - 0.5.0-2
- Bump for mass rebuild.

* Fri Jan 16 2009 Matthew Truch <matt at truch.net> - 0.5.0-1
- Upstream 0.5.0
-   Includes bugfixes.
-   New gzip and bzip2 encoded dirfile read ability.
-   Uses ltdl dynamic module loading for gzip and bzip2 modules.

* Tue Nov 18 2008 Matthew Truch <matt at truch.net> - 0.4.2-1
- Upstream 0.4.2.
-   Includes several bugfixes, especially to the legacy interface.

* Sat Nov 1 2008 Matthew Truch <matt at truch.net> - 0.4.0-1
- Upstream 0.4.0.

* Thu Oct 16 2008 Matthew Truch <matt at truch.net> - 0.3.1-2
- Remove mention of static libs in description
- Include TODO in doc.  
- Cleanup man-pages file glob.
- Include signature.

* Wed Sep 24 2008 Matthew Truch <matt at truch.net> - 0.3.1-1
- Upstream 0.3.1.
-   Includes former c++ compile fix patch
-   Includes bug fixes to legacy API.

* Fri Sep 19 2008 Matthew Truch <matt at truch.net> - 0.3.0-1
- Initial Fedora build.

