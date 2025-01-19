Name:           grib_api
Version:        1.27.0
Release:        24%{?dist}
Summary:        WMO FM-92 GRIB (v1,v2) interface accessible from C and FORTRAN programs

License:        Apache-2.0
URL:            https://software.ecmwf.int/wiki/display/GRIB/Home
Source0:        https://software.ecmwf.int/wiki/download/attachments/3473437/grib_api-%{version}-Source.tar.gz
Source1:        http://download.ecmwf.org/test-data/grib_api/grib_api_test_data.tar.gz
# Fix up some (not all) linking issues
# https://software.ecmwf.int/issues/browse/SUP-839
Patch0:         grib_api-link.patch
# Do not wrap system headers in extern "C" {}
# https://software.ecmwf.int/issues/browse/SUP-1792
Patch1:         grib_api-extern.patch
# add support jasper-2
# https://software.ecmwf.int/issues/browse/SUP-1849
Patch2:         grib_api-jasper-2.patch
# jasper3 now hides internal encoder / decoder. Use wrapper entry point
# c.f. https://github.com/jasper-software/jasper/commit/5fe57ac5829ec31396e7eaab59a688da014660af
# Also, now with jasper3, calling jas_stream_memopen (for example) always needs jasper
# library initialization
Patch3:         grib_api-1.27.0-jasper3-use-wrapper-entry-point.patch
BuildRequires:  gcc-gfortran
BuildRequires:  netcdf-devel
BuildRequires:  jasper-devel
BuildRequires:  libpng-devel
# For autoreconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires: make

%description
The ECMWF GRIB API is an application program interface accessible from C
and FORTRAN programs developed for encoding and decoding WMO FM-92 GRIB
edition 1 and edition 2 messages. A useful set of command line tools is
also provided to give quick access to grib messages.

%package devel
Summary:    GRIB API development headers
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   gcc-gfortran%{?_isa}
Requires:   jasper-devel%{?_isa}

%description devel
Header files and libraries for building a extension library.

%package static
Summary:    GRIB API static libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   %{name}-devel%{?_isa} = %{version}-%{release}
Requires:   libpng-devel%{?_isa}

%description static
Static libraries for %{name}.

%prep
%setup -q -n %{name}-%{version}-Source
tar xf %SOURCE1
%patch -P0 -p1 -b .link
%patch -P1 -p1 -b .extern
%patch -P2 -p1 -b .jasper2
%patch -P3 -p1 -b .jasper3

# Fix rpath issues by using Fedora's libtool
rm m4/libtool.m4
autoreconf -f -i
# Fix ksh path
find -name \*.ksh | xargs sed -i -e 's,/usr/bin/ksh,/bin/ksh,'

# Fix permissions
find -name \*.c | xargs chmod -x


%build
export FCFLAGS="%{build_fflags} -fallow-argument-mismatch"
%{configure} --with-ifs-samples=%{_datadir}/%{name}/ifs_samples \
  --with-netcdf=%{_libdir} --with-pic --with-png-support
# Parallel make fails sometimes building fortran module:
# Fatal Error: Can't delete temporary module file 'grib_api.mod0': No such file or directory
make


%install
%make_install

find %{buildroot} -name \*.la -delete

# Convert ISO88591 text to UTF-8
for file in `find %{buildroot}%{_datadir}/%{name}/definitions/`; do
    iconv -f ISO88591 -t utf-8 $file > $file.new && mv $file.new $file || rm -f $file.new
done

# Give these files some normal permissions
chmod 644 README LICENSE COPYING ChangeLog AUTHORS

# Move the fortran module into _fmoddir
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/%{name}.mod %{buildroot}%{_fmoddir}

# Fix permission
chmod +x %{buildroot}%{_datadir}/%{name}/definitions/installDefinitions.sh

%check
# ls.sh test is failing
# https://software.ecmwf.int/issues/browse/SUP-521
make check


%ldconfig_scriptlets


%files
%license LICENSE COPYING
%doc README ChangeLog AUTHORS
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/definitions/
%doc %{_datadir}/%{name}/ifs_samples/
%doc %{_datadir}/%{name}/samples/
%{_libdir}/*.so.1*

%files devel
%{_includedir}/*
%{_fmoddir}/%{name}.mod
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}_f90.pc

%files static
%{_libdir}/*.a

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 26 2023 Jos de Kloe <josdekloe@gmail.com> 1.27.0-20
- rebuild after so name jump of libjasper

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 28 2022 Jos de Kloe <josdekloe@gmail.com> 1.27.0-17
- SPDX migration: change ASL 2.0 to Apache-2.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 14 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.27.0-15
- jasper3: use wrapper entry point for jpeg2000 decoder

* Sun Feb 13 2022 Josef Ridky <jridky@redhat.com> - 1.27.0-14
- Rebuilt for libjasper.so.6

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 1.27.0-12
- Rebuild for netcdf 4.8.0

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 1.27.0-11
- Rebuild for netcdf 4.8.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Orion Poplawski <orion@nwra.com> - 1.27.0-6
- Drop BR on numpy

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 1.27.0-4
- Rebuild for netcdf 4.6.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild


* Thu Sep 13 2018 Jos de Kloe <josdekloe@gmail.com> 1.27.0-2
- remove python2 sub-package as per Mass Python 2 Package Removal for f30

* Sun Jul 22 2018 Orion Poplawski <orion@nwra.com> - 1.27.0-1
- Update to 1.27.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 21 2018 Orion Poplawski <orion@nwra.com> - 1.26.1-1
- Update to 1.26.1

* Thu Feb 15 2018 Jos de Kloe <josdekloe@gmail.com> - 1.25.0-4
- Rebuild after mass rebuild caused dependency troubles

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Jos de Kloe <josdekloe@gmail.com> - 1.25.0-2
- Rebuild for gcc 8

* Wed Dec 20 2017 Orion Poplawski <orion@nwra.com> - 1.25.0-1
- Update to 1.25.0

* Mon Nov 20 2017 Orion Poplawski <orion@nwra.com> - 1.24.0-1
- Update to 1.24.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Orion Poplawski <orion@cora.nwra.com> - 1.23.0-1
- Update to 1.23.0

* Wed May 24 2017 Orion Poplawski <orion@cora.nwra.com> - 1.22.0-1
- Update to 1.22.0

* Fri Mar 24 2017 Orion Poplawski <orion@cora.nwra.com> - 1.21.0-1
- Update to 1.21.0

* Wed Feb 01 2017 Orion Poplawski <orion@cora.nwra.com> - 1.19.0-4
- Rebuild for gcc 7

* Mon Dec 05 2016 Than Ngo <than@redhat.com> - 1.19.0-3
- fix api change in jasper-2

* Thu Dec 01 2016 Orion Poplawski <orion@cora.nwra.com> - 1.19.0-2
- Rebuild for jasper 2.0

* Tue Nov 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1.19.0-1
- Update to 1.19.0

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 1.18.0-2
- Add patch to not wrap system headers in extern "C" {} in grib_api.h

* Tue Oct 11 2016 Orion Poplawski <orion@cora.nwra.com> - 1.18.0-1
- Update to 1.18.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 29 2016 Orion Poplawski <orion@cora.nwra.com> - 1.16.0-1
- Update to 1.16.0

* Thu Apr 28 2016 Orion Poplawski <orion@cora.nwra.com> - 1.15.0-1
- Update to 1.15.0
- Drop python patch - install changed upstream

* Fri Mar 18 2016 Orion Poplawski <orion@cora.nwra.com> - 1.14.7-1
- Update to 1.14.7
- Ship python2-grib_api
- Use %%license

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Orion Poplawski <orion@cora.nwra.com> - 1.14.5-1
- Update to 1.14.5

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1.14.4-2
- Rebuild for netcdf 4.4.0

* Tue Dec 1 2015 Orion Poplawski <orion@cora.nwra.com> - 1.14.4-1
- Update to 1.14.4

* Tue Nov 17 2015 Orion Poplawski <orion@cora.nwra.com> - 1.14.3-1
- Update to 1.14.3

* Wed Oct 21 2015 Orion Poplawski <orion@cora.nwra.com> - 1.14.2-1
- Update to 1.14.2

* Wed Jul 15 2015 Orion Poplawski <orion@cora.nwra.com> - 1.14.0-1
- Update to 1.14.0, soname bump
- Drop format patch applied upstream
- Rebase link patch
- Fixup ksh paths

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 22 2015 Orion Poplawski <orion@cora.nwra.com> - 1.13.1-1
- Update to 1.13.1

* Mon Dec 15 2014 Orion Poplawski <orion@cora.nwra.com> - 1.13.0-1
- Update to 1.13.0

* Mon Oct 20 2014 Orion Poplawski <orion@cora.nwra.com> - 1.12.3-5
- Add BR libpng-devel

* Fri Oct 17 2014 Orion Poplawski <orion@cora.nwra.com> - 1.12.3-4
- Add png support (bug #1154192)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 7 2014 Orion Poplawski <orion@cora.nwra.com> - 1.12.3-2
- Fix python install location (bug #1098516)

* Fri Jul 11 2014 Orion Poplawski <orion@cora.nwra.com> - 1.12.3-1
- Update to 1.12.3

* Fri Jun 27 2014 Orion Poplawski <orion@cora.nwra.com> - 1.12.1-1
- Add requires numpy to grib_api-python (bug #1098510)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 8 2014 Orion Poplawski <orion@cora.nwra.com> - 1.12.1-1
- Update to 1.12.1

* Thu Apr 17 2014 Orion Poplawski <orion@cora.nwra.com> - 1.12.0-3
- Add patch to fix some linking issues
- Re-enable parallel builds

* Wed Apr 16 2014 Orion Poplawski <orion@cora.nwra.com> - 1.12.0-2
- Fix some file permission issues
- Add missing post scripts
- Do not install static python archive file

* Wed Mar 5 2014 Orion Poplawski <orion@cora.nwra.com> - 1.12.0-1
- Update to 1.12.0
- Update libtool to fix rpath issues

* Fri Aug 23 2013 Orion Poplawski <orion@cora.nwra.com> - 1.11.0-1
- Update to 1.11.0
- Build shared libraries
- Enable python support
- Run tests (but ignore failure for now)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 8 2013 Orion Poplawski <orion@cora.nwra.com> - 1.9.16-7
- Build with -fPIC on ARM (bug #919614)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Orion Poplawski <orion@cora.nwra.com> - 1.9.16-4
- Revert to /bin/ksh

* Mon Jul 9 2012 Orion Poplawski <orion@cora.nwra.com> - 1.9.16-3
- Definitions are not documentation
- Drop INSTALL from docs
- Add Requires jasper-devel to -devel package
- Don't change ksh path on Fedora 17+

* Fri Jul 6 2012 Orion Poplawski <orion@cora.nwra.com> - 1.9.16-2
- Build fortran interface

* Tue Mar 13 2012 Orion Poplawski <orion@cora.nwra.com> - 1.9.16-1
- Update to 1.9.16

* Sat Jan 14 2012 Orion Poplawski <orion@cora.nwra.com> - 1.9.9-2
- Fix ksh path

* Fri Jan 13 2012 Orion Poplawski <orion@cora.nwra.com> - 1.9.9-1
- Update to 1.9.9
- Fix directory ownership

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 15 2010 Orion Poplawski <orion@cora.nwra.com> - 1.7.0-5
- Compile with -fPIC on x86_64 (bug #561914)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 04 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.7.0-3
- Fix file conflict (#492936)

* Tue Mar 17 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.7.0-1
- New upstream version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec  3 2008 Patrice Dumas <pertusus@free.fr> 1.6.4-1
- update to 1.6.4

* Tue Sep 30 2008 Patrice Dumas <pertusus@free.fr> 1.6.1-1
- update to 1.6.1

* Sat Feb 23 2008 Patrice Dumas <pertusus@free.fr> 1.4.0-1
- update to 1.4.0

* Sat Dec 29 2007 Patrice Dumas <pertusus@free.fr> 1.3.0-1
- initial release
