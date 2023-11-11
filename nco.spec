%global builddocs 1

Name:           nco
Version:        5.1.9
Release:        1%{?dist}
Summary:        Suite of programs for manipulating NetCDF/HDF4 files
License:        BSD-3-Clause
URL:            http://nco.sourceforge.net/

Source0:        https://github.com/nco/nco/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         nco-install_C_headers.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  bison, flex, gawk
BuildRequires:  netcdf-devel
%ifarch %java_arches
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:  antlr-C++
%else
BuildRequires:  antlr
%endif
%endif
BuildRequires:  chrpath
BuildRequires:  gsl-devel
BuildRequires:  texinfo
BuildRequires:  udunits2-devel
%if 0%{?builddocs}
BuildRequires:  texinfo-tex
%endif

%package devel
Summary:        Development files for NCO
Requires:       %{name} = %{version}-%{release}

%package static
Summary:        Static libraries for NCO
Requires:       %{name}-devel = %{version}-%{release}

%description
The netCDF Operators, NCO, are a suite of command line programs known
as operators.  The operators facilitate manipulation and analysis of
self-describing data stored in the freely available netCDF and HDF
formats (http://www.unidata.ucar.edu/packages/netcdf and
http://hdf.ncsa.uiuc.edu, respectively).  Each NCO operator (e.g.,
ncks) takes netCDF or HDF input file(s), performs an operation (e.g.,
averaging, hyperslabbing, or renaming), and outputs a processed netCDF
file.  Although most users of netCDF and HDF data are involved in
scientific research, these data formats, and thus NCO, are generic and
are equally useful in fields from agriculture to zoology.  The NCO
User's Guide illustrates NCO use with examples from the field of
climate modeling and analysis.  The NCO homepage is
http://nco.sourceforge.net/.

%description devel
This package contains the NCO header and development files.

%description static
This package contains the NCO static libs.

%prep
%setup -q
%patch -P0 -p1 -b .install_C_headers


%build
export CPPFLAGS=-I%{_includedir}/udunits2
%configure \
%ifarch %java_arches
  HAVE_ANTLR=yes \
%endif
  --disable-dependency-tracking --includedir=%{_includedir}/nco
%make_build
%if 0%{?builddocs}
make -C doc html pdf
%endif


%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
# Ignore non-ELF files
chrpath -d -k $RPM_BUILD_ROOT%{_bindir}/* || :


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license doc/LICENSE
%doc README* doc/rtfm.txt doc/nco.html doc/nco.pdf doc/nco.css
%doc doc/index.shtml doc/TODO doc/ChangeLog doc/nco.png doc/nco_news.shtml
%doc doc/nsf.png
%ifarch %java_arches
%{_bindir}/ncap2
%endif
%{_bindir}/ncatted
%{_bindir}/ncbo
%{_bindir}/ncclimo
%{_bindir}/ncdiff
%{_bindir}/ncea
%{_bindir}/ncecat
%{_bindir}/nces
%{_bindir}/ncflint
%{_bindir}/ncks
%{_bindir}/ncpdq
%{_bindir}/ncra
%{_bindir}/ncrcat
%{_bindir}/ncremap
%{_bindir}/ncrename
%{_bindir}/ncwa
%{_bindir}/ncz2psx
%{_mandir}/man1/ncap2.1*
%{_mandir}/man1/ncatted.1*
%{_mandir}/man1/ncbo.1*
%{_mandir}/man1/ncclimo.1*
%{_mandir}/man1/ncecat.1*
%{_mandir}/man1/nces.1*
%{_mandir}/man1/ncflint.1*
%{_mandir}/man1/ncks.1*
%{_mandir}/man1/nco.1*
%{_mandir}/man1/ncpdq.1*
%{_mandir}/man1/ncra.1*
%{_mandir}/man1/ncrcat.1*
%{_mandir}/man1/ncremap.1*
%{_mandir}/man1/ncrename.1*
%{_mandir}/man1/ncwa.1*
%{_mandir}/man1/ncz2psx.1*
%{_infodir}/*
%{_libdir}/libnco*[0-9]*.so

%files devel
%{_libdir}/libnco.so

%files static
%{_libdir}/libnco*.a


%changelog
* Thu Nov 09 2023 Orion Poplawski <orion@nwra.com> - 5.1.9-1
- Update to 5.1.9

* Tue Sep 19 2023 Orion Poplawski <orion@nwra.com> - 5.1.8-1
- Update to 5.1.8

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 16 2023 Orion Poplawski <orion@nwra.com> - 5.1.6-1
- Update to 5.1.6

* Thu Mar 16 2023 Orion Poplawski <orion@nwra.com> - 5.1.5-1
- Update to 5.1.5

* Fri Jan 20 2023 Orion Poplawski <orion@nwra.com> - 5.1.4-1
- Update to 5.1.4
- Change license to BSD-3-Clause

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 04 2022 Orion Poplawski <orion@nwra.com> - 5.1.3-1
- Update to 5.1.3

* Sat Oct 29 2022 Orion Poplawski <orion@nwra.com> - 5.1.1-1
- Update to 5.1.1

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.1.0-4
- Restrict BR: antlr and result binary ncap2 to %%java_arches

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.1.0-3
- Rebuild for gsl-2.7.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Orion Poplawski <orion@nwra.com> - 5.1.0-1
- Update to 5.1.0

* Wed May 04 2022 Orion Poplawski <orion@nwra.com> - 5.0.7-1
- Update to 5.0.7

* Thu Feb 03 2022 Orion Poplawski <orion@nwra.com> - 5.0.6-1
- Update to 5.0.6

* Wed Jan 26 2022 Orion Poplawski <orion@nwra.com> - 5.0.5-1
- Update to 5.0.5

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 05 2021 Orion Poplawski <orion@nwra.com> - 5.0.4-1
- Update to 5.0.4

* Thu Oct 07 2021 Orion Poplawski <orion@nwra.com> - 5.0.3-1
- Update to 5.0.3

* Mon Sep 27 2021 Orion Poplawski <orion@nwra.com> - 5.0.2-1
- Update to 5.0.2

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 5.0.1-1
- Update to 5.0.1

* Mon Aug 09 2021 Orion Poplawski <orion@nwra.com> - 5.0.0-1
- Update to 5.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 05 2021 Orion Poplawski <orion@nwra.com> - 4.9.8-1
- Update to 4.9.8

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Orion Poplawski <orion@nwra.com> - 4.9.7-1
- Update to 4.9.7

* Sun Dec 20 2020 Orion Poplawski <orion@nwra.com> - 4.9.6-1
- Update to 4.9.6

* Thu Sep 24 2020 Orion Poplawski <orion@nwra.com> - 4.9.5-1
- Update to 4.9.5

* Sun Sep 06 2020 Orion Poplawski <orion@nwra.com> - 4.9.4-1
- Update to 4.9.4

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Orion Poplawski <orion@nwra.com> - 4.9.3-1
- Update to 4.9.3

* Sat Feb 15 2020 Orion Poplawski <orion@nwra.com> - 4.9.2-1
- Update to 4.9.2

* Sun Feb 02 2020 Orion Poplawski <orion@nwra.com> - 4.9.1-1
- Update to 4.9.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 4 2019 Orion Poplawski <orion@cora.nwra.com> 4.9.0-1
- Update to 4.9.0

* Mon Aug 26 2019 Orion Poplawski <orion@cora.nwra.com> 4.8.1-1
- Update to 4.8.1

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.8.0-3
- Rebuilt for GSL 2.6.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Orion Poplawski <orion@cora.nwra.com> 4.8.0-1
- Update to 4.8.0

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 4.7.9-2
- Rebuild for netcdf 4.6.3

* Fri Feb 22 2019 Orion Poplawski <orion@cora.nwra.com> 4.7.9-1
- Update to 4.7.9

* Tue Feb 12 2019 Orion Poplawski <orion@nwra.com> 4.7.8-2
- Add patch to fix compilation with GCC 9

* Sat Feb 2 2019 Orion Poplawski <orion@cora.nwra.com> 4.7.8-1
- Update to 4.7.8

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Orion Poplawski <orion@nwra.com> - 4.7.5-4
- Add BR gcc-c++ (FTBFS bug #1604926)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Orion Poplawski <orion@cora.nwra.com> 4.7.5-2
- Cleanup spec

* Sun Jun 17 2018 Orion Poplawski <orion@cora.nwra.com> 4.7.5-1
- Update to 4.7.5

* Mon Apr 09 2018 Orion Poplawski <orion@cora.nwra.com> 4.7.4-1
- Update to 4.7.4
- Drop ncap

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 4.7.1-3
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 30 2017 Orion Poplawski <orion@cora.nwra.com> 4.7.1-1
- Update to 4.7.1

* Fri Nov 17 2017 Orion Poplawski <orion@cora.nwra.com> 4.7.0-1
- Update to 4.7.0

* Wed Aug 16 2017 Orion Poplawski <orion@cora.nwra.com> 4.6.8-1
- Update to 4.6.8

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> 4.6.7-1
- Update to 4.6.7

* Thu Mar 16 2017 Orion Poplawski <orion@cora.nwra.com> 4.6.5-1
- Update to 4.6.5

* Wed Feb 8 2017 Orion Poplawski <orion@cora.nwra.com> 4.6.4-1
- Update to 4.6.4

* Fri Dec 23 2016 Orion Poplawski <orion@cora.nwra.com> 4.6.3-1
- Update to 4.6.3

* Wed Nov 16 2016 Orion Poplawski <orion@cora.nwra.com> 4.6.2-1
- Update to 4.6.2

* Wed Aug 10 2016 Orion Poplawski <orion@cora.nwra.com> 4.6.1-1
- Update to 4.6.1
- Drop version patch fixed upstream

* Fri Jun 3 2016 Orion Poplawski <orion@cora.nwra.com> 4.6.0-1
- Update to 4.6.0
- Add patch to fix library version variable

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 4.5.5-2
- Rebuild for gsl 2.1

* Sun Feb 21 2016 Orion Poplawski <orion@cora.nwra.com> 4.5.5-1
- Update to 4.5.5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 4.5.4-2
- Rebuild for netcdf 4.4.0

* Thu Jan 7 2016 Orion Poplawski <orion@cora.nwra.com> 4.5.4-1
- Update to 4.5.4

* Wed Oct 21 2015 Orion Poplawski <orion@cora.nwra.com> 4.5.3-1
- Update to 4.5.3

* Sun Sep 6 2015 Orion Poplawski <orion@cora.nwra.com> 4.5.2-1
- Update to 4.5.2

* Wed Aug 12 2015 Orion Poplawski <orion@cora.nwra.com> 4.5.1-1
- Update to 4.5.1
- Build docs

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.4.8-2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 21 2015 Orion Poplawski <orion@cora.nwra.com> 4.4.8-1
- Update to 4.4.8

* Mon Dec 1 2014 Orion Poplawski <orion@cora.nwra.com> 4.4.7-1
- Update to 4.4.7

* Wed Aug 27 2014 Orion Poplawski <orion@cora.nwra.com> 4.4.5-1
- Update to 4.4.5

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 23 2014 Orion Poplawski <orion@cora.nwra.com> 4.4.4-1
- Update to 4.4.4
- Strip rpaths

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 2 2014 Orion Poplawski <orion@cora.nwra.com> 4.4.3-1
- Update to 4.4.3

* Mon Feb 24 2014 Orion Poplawski <orion@cora.nwra.com> 4.4.2-1
- Update to 4.4.2

* Wed Jan 29 2014 Orion Poplawski <orion@cora.nwra.com> 4.4.1-1
- Update to 4.4.1

* Thu Dec 19 2013 Orion Poplawski <orion@cora.nwra.com> 4.3.9-1
- Update to 4.3.9
- Fix build with -Werror=format-security

* Tue Oct 22 2013 Orion Poplawski <orion@cora.nwra.com> 4.3.7-2
- No need to build docs
- Drop BR version requirement for netcdf-devel, all up to date

* Fri Oct 18 2013 Orion Poplawski <orion@cora.nwra.com> 4.3.7-1
- Update to 4.3.7

* Mon Sep 30 2013 Orion Poplawski <orion@cora.nwra.com> 4.3.6-1
- Update to 4.3.6

* Wed Sep 25 2013 Orion Poplawski <orion@cora.nwra.com> 4.3.5-1
- Update to 4.3.5

* Thu Aug 1 2013 Orion Poplawski <orion@cora.nwra.com> 4.3.4-1
- Update to 4.3.4

* Sun Jul 28 2013 Orion Poplawski <orion@cora.nwra.com> 4.3.3-1
- Update to 4.3.3

* Tue Jul 9 2013 Orion Poplawski <orion@cora.nwra.com> 4.3.2-1
- Update to 4.3.2

* Sun Mar 31 2013 - Orion Poplawski <orion@cora.nwra.com> - 4.3.0-1
- Update to 4.3.0

* Wed Jan 30 2013 - Orion Poplawski <orion@cora.nwra.com> - 4.2.5-1
- Update to 4.2.5

* Thu Nov 15 2012 - Orion Poplawski <orion@cora.nwra.com> - 4.2.3-1
- Update to 4.2.3

* Mon Oct 29 2012 - Orion Poplawski <orion@cora.nwra.com> - 4.2.2-1
- Update to 4.2.2

* Fri Aug 3 2012 - Orion Poplawski <orion@cora.nwra.com> - 4.2.1-1
- Update to 4.2.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 - Orion Poplawski <orion@cora.nwra.com> - 4.2.0-1
- Update to 4.2.0

* Tue Apr 3 2012 - Orion Poplawski <orion@cora.nwra.com> - 4.1.0-1
- Update to 4.1.0

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.9-2
- Rebuilt for c++ ABI breakage

* Tue Feb 14 2012 - Orion Poplawski <orion@cora.nwra.com> - 4.0.9-1
- Update to 4.0.9

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 - Orion Poplawski <orion@cora.nwra.com> - 4.0.8-2
- Really enable netcdf4 support

* Tue May 17 2011 - Orion Poplawski <orion@cora.nwra.com> - 4.0.8-1
- Update to 4.0.8
- Rebuild for hdf5 1.8.7

* Wed Apr 6 2011 - Orion Poplawski <orion@cora.nwra.com> - 4.0.7-1
- Update to 4.0.7

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 6 2011 - Orion Poplawski <orion@cora.nwra.com> - 4.0.6-3
- Rebuild with fixed hdf5 for netcdf4 support

* Sat Feb 5 2011 - Orion Poplawski <orion@cora.nwra.com> - 4.0.6-2
- Fixup more EL5 tests

* Sat Feb 5 2011 - Orion Poplawski <orion@cora.nwra.com> - 4.0.6-1
- Update to 4.0.6
- Really only use libnc-dap for EL5

* Thu Dec 16 2010 - Orion Poplawski <orion@cora.nwra.com> - 4.0.5-3
- BR antlr-C++ on Fedora 14+

* Mon Dec 13 2010 - Orion Poplawski <orion@cora.nwra.com> - 4.0.5-2
- Use libnc-dap only for EL5
- Other EL5 fixes

* Fri Dec 10 2010 - Orion Poplawski <orion@cora.nwra.com> - 4.0.5-1
- Update to 4.0.5

* Fri Oct 1 2010 - Orion Poplawski <orion@cora.nwra.com> - 4.0.4-1
- Update to 4.0.4

* Tue Sep 7 2010 - Orion Poplawski <orion@cora.nwra.com> - 4.0.3-1
- Update to 4.0.3
- Rebase install_C_headers patch

* Mon Jun 28 2010 - Orion Poplawski <orion@cora.nwra.com> - 4.0.2-1
- Update to 4.0.2

* Tue Apr 20 2010 - Orion Poplawski <orion@cora.nwra.com> - 4.0.1-1
- Update to 4.0.1

* Wed Jan 6 2010 - Orion Poplawski <orion@cora.nwra.com> - 4.0.0-4
- Enable netcdf4 support

* Wed Jan 6 2010 - Orion Poplawski <orion@cora.nwra.com> - 4.0.0-3
- Enable udunits2 support - add proper include path

* Wed Jan 6 2010 - Orion Poplawski <orion@cora.nwra.com> - 4.0.0-2
- Enable udunits2 support
- Updated 4.0.0 tarball

* Wed Jan 6 2010 - Orion Poplawski <orion@cora.nwra.com> - 4.0.0-1
- Update to 4.0.0

* Thu Nov 12 2009 - Orion Poplawski <orion@cora.nwra.com> - 3.9.9-2
- Drop LIBS, linkage fixed in netcdf package

* Wed Nov 11 2009 - Orion Poplawski <orion@cora.nwra.com> - 3.9.9-1
- Update to 3.9.9
- Build against netcdf 4.1.0
- Add needed netcdf libraries to LIBS

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 30 2009 - Orion Poplawski <orion@cora.nwra.com> - 3.9.8-1
- Update to 3.9.8
- Update install headers patch

* Mon Mar 30 2009 - Orion Poplawski <orion@cora.nwra.com> - 3.9.7-2
- Drop include patch fixed in antlr 2.7.7-5

* Wed Mar 25 2009 - Orion Poplawski <orion@cora.nwra.com> - 3.9.7-1
- Update to 3.9.7 - download tarball from nco site
- Add BR on gsl-devel to enable GSL support
- Force antlr detection to override bad configure test
- Rework install_C_headers patch to not require autotool run
- Report include patch upstream

* Fri Mar 06 2009 - Caolán McNamara <caolanm@redhat.com> - 3.9.5-5
- include cstdio for EOF

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 - Patrice Dumas <pertusus@free.fr> - 3.9.5-3
- call libtoolize
- remove unneeded dependencies on curl-devel, libxml2-devel, librx-devel
- ship more documentation

* Thu Sep 11 2008 - Patrice Dumas <pertusus@free.fr> - 3.9.5-2
- rebuild for newer libnc-dap

* Thu Jul 10 2008 - Patrice Dumas <pertusus@free.fr> - 3.9.5-1
- update to 3.9.5

* Sat Mar  1 2008 - Patrice Dumas <pertusus@free.fr> - 3.9.3-1
- update to 3.9.3
- separate static sub-package 

* Mon Aug 27 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.9.1-1
- Update to 3.9.1
- Drop udunits patch no longer needed
- Add BR libnc-dap-devel to enable DAP support
- Add BR antlr
- Add BR gawk

* Sat Sep  2 2006 Ed Hill <ed@eh3.com> - 3.1.5-3
- br bison as well

* Sat Sep  2 2006 Ed Hill <ed@eh3.com> - 3.1.5-2
- buildrequire flex

* Sat Sep  2 2006 Ed Hill <ed@eh3.com> - 3.1.5-1
- new upstream 3.1.5

* Fri Apr 21 2006 Ed Hill <ed@eh3.com> - 3.1.2-1
- update to new upstream 3.1.2

* Thu Feb 16 2006 Ed Hill <ed@eh3.com> - 3.0.2-2
- rebuild for new gcc

* Mon Sep  5 2005 Ed Hill <ed@eh3.com> - 3.0.2-1
- update to new upstream 3.0.2

* Wed Aug  3 2005 Ed Hill <ed@eh3.com> - 3.0.1-4
- remove (hopefully only temporarily) opendap support

* Thu Jul 21 2005 Ed Hill <ed@eh3.com> - 3.0.1-3
- add LICENSE file

* Sat Jul  9 2005 Ed Hill <ed@eh3.com> - 3.0.1-2
- add BuildRequires: opendap-devel

* Sun Jun 19 2005 Ed Hill <ed@eh3.com> - 3.0.1-1
- update to upstream 3.0.1
- comment & fixes for BuildRequires

* Sat Apr 23 2005 Ed Hill <ed@eh3.com> - 3.0.0-2
- add BuildRequires and fix CXXFLAGS per Tom Callaway
- add udunits patch per Tom Callaway

* Sat Apr 16 2005 Ed Hill <ed@eh3.com> - 3.0.0-1
- update to ver 3.0.0
- devel package fixes per D.M. Kaplan and M. Schwendt
- fix info post/postun

* Sun Dec  5 2004 Ed Hill <eh3@mit.edu> - 0:2.9.9-0.fdr.4
- sync with netcdf-3.6.0beta6-0.fdr.0
- split into devel and non-devel

* Wed Dec  1 2004 Ed Hill <eh3@mit.edu> - 0:2.9.9-0.fdr.3
- sync with netcdf-0:3.5.1-0.fdr.11
- added '-fpermissive' for GCC 3.4.2 warnings
- added "Provides:nco-devel" for the headers and libs

* Mon Oct  4 2004 Ed Hill <eh3@mit.edu> - 0:2.9.9-0.fdr.2
- Add some of Michael Schwendt's suggested INC/LIB path fixes and 
  sync with the netcdf-3.5.1-0.fdr.10 dependency.

* Thu Sep 23 2004 Ed Hill <eh3@mit.edu> - 0:2.9.9-0.fdr.1
- add NETCDF_INC and NETCDF_LIB to work on systems where old
  versions of netcdf may exist in /usr/local

* Wed Sep  8 2004 Ed Hill <eh3@mit.edu> - 0:2.9.9-0.fdr.0
- updated to ver 2.9.9

* Sat Aug  7 2004 Ed Hill <eh3@mit.edu> - 0:2.9.8-0.fdr.0
- updated to ver 2.9.8

* Sat Jul 17 2004 Ed Hill <eh3@mit.edu> - 0:2.9.7-0.fdr.2
- removed unneeded %%ifarch

* Sat Jul 17 2004 Ed Hill <eh3@mit.edu> - 0:2.9.7-0.fdr.1
- Add %%post,%%postun

* Sat Jul 17 2004 Ed Hill <eh3@mit.edu> - 0:2.9.7-0.fdr.0
- Initial working version

