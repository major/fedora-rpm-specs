Name:           grads
Version:        2.0.2
Release:        41%{?dist}
Summary:        Tool for easy acces, manipulation, and visualization of data

# gxeps is under the MIT, other programs are GPLv2
License:        GPLv2 and MIT
URL:            http://cola.gmu.edu/grads/

Source0:        ftp://cola.gmu.edu/grads/2.0/grads-%{version}-src.tar.gz

Patch0:		grads-use-system-libshp_libsx.patch
Patch1:		grads-libpng.patch
Patch2:		grads-format-security.patch
# Use udunits2 library
Patch3:		grads-udunits2.patch
# Fix compilation with -Werror=implicit-function-declaration
Patch4:         grads-implicit.patch

BuildRequires:  hdf-static hdf-devel hdf5-devel netcdf-devel
BuildRequires:  g2clib-static g2clib-devel
BuildRequires:  udunits2-devel
BuildRequires:  readline-devel ncurses-devel
BuildRequires:  shapelib-devel gd-devel libgeotiff-devel
BuildRequires:  zlib-devel libjpeg-devel libpng-devel
BuildRequires:  libXmu-devel libX11-devel libXaw-devel
BuildRequires:  pkgconfig
BuildRequires:  automake
BuildRequires: make

# in a separate package now
Requires:       wgrib

%description
The Grid Analysis and Display System (GrADS) is an interactive desktop tool
that is used for easy access, manipulation, and visualization of earth science
data. The format of the data may be either binary, GRIB, NetCDF, or HDF-SDS
(Scientific Data Sets). GrADS has been implemented worldwide on a variety of
commonly used operating systems and is freely distributed over the Internet.


%prep
%setup -q
%patch0 -p0 -b .sys
%patch1 -p0 -b .png
%patch2 -p0 -b .fmt
%patch3 -p1 -b .udunits2
%patch4 -p1 -b .implicit
# Use proper grib2c lib name
sed -i -e 's/LIB(grib2c/LIB(%{g2clib}/' -e 's/-lgrib2c/-l%{g2clib}/' m4/grib2.m4
# change path to datas to %{_datadir}/%{name}
sed -i -e 's@/usr/local/lib/grads@%{_datadir}/%{name}@' src/gxsubs.c
autoreconf -f -i

%build
#./bootstrap
%configure --enable-dyn-supplibs	\
	--without-gui --with-geotiff --with-sdf --with-shp	\
	--with-netcdf-include=%{_includedir} --with-netcdf-libdir=%{_libdir}\
	LDFLAGS="-L%{_libdir}/hdf/"	\
	CPPFLAGS="-I%{_includedir}/hdf -I%{_includedir}/libshp -I%{_includedir}/udunits2 -DH5_USE_110_API"

%make_build

rm -rf __dist_docs
mkdir __dist_docs
cp -a doc __dist_docs/html


%install
%make_install
%{__install} -d -m755 $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__install} -p -m644 data/*.dat data/*res $RPM_BUILD_ROOT%{_datadir}/%{name}


%files
%license COPYRIGHT
%doc __dist_docs/html
%{_bindir}/bufrscan
%{_bindir}/grads
%{_bindir}/gribmap
%{_bindir}/grib2scan
%{_bindir}/gribscan
%{_bindir}/gxeps
%{_bindir}/gxps
%{_bindir}/gxtran
%{_bindir}/stnmap
# wgrib is in a separate package
%exclude %{_bindir}/wgrib
%{_datadir}/grads/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 13 2022 Josef Ridky <jridky@redhat.com> - 2.0.2-40
- Rebuilt for libjasper.so.6

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Orion Poplawski <orion@nwra.com> - 2.0.2-38
- Rebuild for hdf5 1.12.1

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 2.0.2-37
- Rebuild for hdf5 1.10.7/netcdf 4.8.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 2.0.2-33
- Rebuild for hdf5 1.10.6

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 2.0.2-30
- Rebuild for hdf5 1.10.5

* Wed Mar 13 2019 Orion Poplawski <orion@nwra.com> - 2.0.2-29
- Use proper g2clib name (bugz #1483299)
- Use %%license

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.2-28
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 2.0.2-21
- Rebuild (libwebp)

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.0.2-20
- Rebuild for readline 7.x

* Sun Dec 11 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.0.2-19
- Rebuild for shapelib SONAME bump

* Sun Dec 04 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.2-18
- Add patch to compile with -Werror=implicit-function-declaration
- Update URL and Source URL

* Sun Dec 04 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.2-18
- Rebuild for jasper 2.0

* Fri Jul 22 2016 Tom Callaway <spot@fedoraproject.org> - 2.0.2-17
- rebuild to drop libvpx dep

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.2-15
- Rebuild for netcdf 4.4.0

* Tue Dec  1 2015 Tom Callaway <spot@fedoraproject.org> - 2.0.2-14
- rebuild for libvpx 1.5.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 2.0.2-12
- Rebuild for hdf5 1.8.15

* Mon Apr  6 2015 Tom Callaway <spot@fedoraproject.org> - 2.0.2-11
- rebuild for libvpx 1.4.0

* Wed Jan 07 2015 Orion Poplawski <orion@cora.nwra.com> - 2.0.2-10
- Rebuild for hdf5 1.8.14

* Mon Aug 25 2014 Devrim Gündüz <devrim@gunduz.org> - 2.0.2-9
- Rebuilt for libgeotiff 

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Orion Poplawski <orion@cora.nwra.com> - 2.0.5-7
- Update libpng patch to use generic libpng

* Mon Aug 11 2014 Orion Poplawski <orion@cora.nwra.com> - 2.0.5-6
- Compile with the udunits2 library

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 24 2014 Deji Akingunola <dakingun@gmail.com> - 2.0.2-4
- Apply patch to fix format-security build error (Bug 1037101)

* Thu Aug 15 2013 Deji Akingunola <dakingun@gmail.com> - 2.0.2-3
- Update libpng patch for libpng16

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Deji Akingunola <dakingun@gmail.com> - 2.0.2-1
- Update to 2.0.2

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 2.0.1-8
- rebuild for new GD 2.1.0

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 2.0.1-7
- Rebuild for hdf5 1.8.11

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2.0.1-5
- rebuild due to "jpeg8-ABI" feature drop

* Mon Dec 03 2012 Orion Poplawski <orion@cora.nwra.com> - 2.0.1-4
- Rebuild for hdf5 1.8.10

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 22 2012 Deji Akingunola <dakingun@gmail.com> - 2.0.1-2
- Disable gui build option (again), it depends on the orphaned libsx

* Thu Jan 26 2012 Deji Akingunola <dakingun@gmail.com> - 2.0.1-1
- Update to 2.0.1
- Remove grads-README.xorg - the info is no more relevant for current (popular) Linux Desktops (KDE4 and GNOME 3).
- Remove grads-copyright_summary - Already sorted out upstream. 

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.a9-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.0.a9-0.6
- Rebuild for new libpng

* Mon Jun 27 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.a9-0.5
- Add BR udunits-static to meet guidelines (#610798)
  on linking with static libs.

* Tue May 17 2011 Orion Poplawski <orion@cora.nwra.com> - 2.0.a9-0.4
- Rebuild for hdf5 1.8.7

* Wed Apr 6 2011 Orion Poplawski <orion@cora.nwra.com> - 2.0.a9-0.3
- Rebuild for netcdf 4.1.2
- Remove libnc-dap-devel BR, functionality now provided in netcdf

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.a9-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 03 2010 Deji Akingunola <dakingun@gmail.com> - 2.0.a9-0.1
- Update to 2.0.a9
- Remove upstreamed patches

* Wed Apr 28 2010 Deji Akingunola <dakingun@gmail.com> - 2.0.a8-0.1
- Update to 2.0.a8

* Tue Dec  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.a7.1-0.3
- Same as below with hdf-static.
- Explicitly BR g2clib-static in accordance with the Packaging
  Guidelines (g2clib-devel is still static-only).

* Fri Nov 27 2009 Deji Akingunola <dakingun@gmail.com> - 2.0.a7.1-0.1
- Update to 2.0.a7 (See http://grads.iges.org/grads/changelog-2.0.txt for 
  detailed list of changes in 2.0.x release)
- Cleanup the spec

* Mon Feb 23 2009 Deji Akingunola <dakingun@gmail.com> - 2.0.a5-0.1
- Update to 2.x series

* Thu Sep 11 2008 - Patrice Dumas <pertusus@free.fr> 1.9b4-25
- rebuild for new libnc-dap
- rediff patches
- use new netcdf devel file locations

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.9b4-23
- Autorebuild for GCC 4.3

* Fri Jan  4 2008 Patrice Dumas <pertusus@free.fr> 1.9b4-22
- rebuild for new libdap soname (indirect dependency through libnc-dap)

* Wed Aug 22 2007 Patrice Dumas <pertusus@free.fr> 1.9b4-21
- source is modified, use another name than upstream
- clarify licenses
- keep timestamps
- rework patches
- use newer libdap and libnc-dap autoconf macros

* Thu Feb  1 2007 Patrice Dumas <pertusus@free.fr> 1.9b4-20
- rebuild to link against ncurses instead termcap (#226759)

* Thu Nov 16 2006 Patrice Dumas <pertusus@free.fr> 1.9b4-19
- don't ship wgrib but depend on it

* Tue Oct 31 2006 Patrice Dumas <pertusus@free.fr> 1.9b4-18
- rebuild for new libcurl soname (indirect dependency through libnc-dap)

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 1.9b4-17
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 Patrice Dumas <pertusus@free.fr> 1.9b4-16
- rebuild against libdap 3.7.2

* Mon Sep 11 2006 Patrice Dumas <pertusus@free.fr> 1.9b4-15
- rebuild for FC6

* Sat Jul 22 2006 Patrice Dumas <pertusus@free.fr> 1.9b4-14
- Update for newer libnc-dap

* Fri Jul  7 2006 Patrice Dumas <pertusus@free.fr> 1.9b4-12
- Added BR automake, fix #197942 

* Fri Apr 21 2006 Patrice Dumas <pertusus@free.fr> 1.9b4-11
- Add needed X related BR

* Fri Apr 21 2006 Patrice Dumas <pertusus@free.fr> 1.9b4-10
- remove unneeded X related BR and configure flags since the gui isn't built

* Sat Mar 11 2006 Patrice Dumas <pertusus@free.fr> 1.9b4-9
- rebuild for newer libdap

* Fri Feb 17 2006 Patrice Dumas <pertusus@free.fr> 1.9b4-8
- enable hdf for ppc, now that it is there
- use a wrapper include file to prepend sd_ to netcdf symbols for
  hdf if it is required

* Thu Jan 19 2006 Patrice Dumas <pertusus@free.fr> 1.9b4-6
- add BR on readline-devel close #178285

* Wed Dec 21 2005 Patrice Dumas <pertusus@free.fr> 1.9b4-5
- don't build the hdf interface on ppc, there is no hdf package

* Tue Dec 13 2005 Patrice Dumas <pertusus@free.fr> 1.9b4-4
- simplify handling of data, as they are in the tarball

* Tue Dec 13 2005 Patrice Dumas <pertusus@free.fr> 1.9b4-3
- remove files with GPL incompatible licences

* Tue Aug 16 2005 Patrice Dumas <pertusus@free.fr> 1.9b4-2
- use libsx without freq

* Fri Aug 12 2005 Patrice Dumas <pertusus@free.fr> 1.9b4-1
- initial release
