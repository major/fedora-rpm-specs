Name:           wgrib2
Version:        3.1.3
Release:        7%{?dist}
Summary:        Manipulate, inventory and decode GRIB2 files

# most files are public domain, geo.c and Netcdf.c are GPL+, gribtab.c is GPLv2+
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/
Source0:        http://ftp.cpc.ncep.noaa.gov/wd51we/wgrib2/wgrib2_nolib.tgz.v%{version}
Source1:        config.h
# Disable gctpc for now - bundled library
Patch0:         wgrib2-nogctpc.patch
# support jasper 2
Patch1:         wgrib2-jasper-2.patch
# jasper3 now hides internal encoder / decoder. Use wrapper entry point
# c.f. https://github.com/jasper-software/jasper/commit/5fe57ac5829ec31396e7eaab59a688da014660af
Patch2:         wgrib2-2.0.8-jasper3-use-wrapper-entry-point.patch

BuildRequires:  make
BuildRequires:  g2clib-static
BuildRequires:  hdf5-devel
BuildRequires:  libaec-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  netcdf-devel
BuildRequires:  proj-devel
BuildRequires:  zlib-devel

%description
Wgrib2 is a swiss army knife for grib2 files. You can use it inventory or
extract data. You can do basic database operations and other nifty things.


%prep
%setup -q -n grib2
%patch -P 0 -p1 -b .nogctpc
%patch -P 1 -p1 -b .jasper2
%patch -P 2 -p1 -b .jasper3

rm wgrib2/fnlist.c
rm -r wgrib2/{Gctpc,gctpc_ll2xy,new_grid_lambertc}.[ch]
cp %SOURCE1 wgrib2/config.h


%build
cd wgrib2
export CFLAGS="-I.. -I%{_includedir}/netcdf -I%{_includedir}/mysql $RPM_OPT_FLAGS -fopenmp"
export LDFLAGS="-l%{g2clib} -ljasper -lnetcdf -lpng -lmysqlclient -lsz -lz -lm -fopenmp"
%make_build fnlist.c
%make_build


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install wgrib2/wgrib2 $RPM_BUILD_ROOT%{_bindir}/wgrib2


%files
%doc README wgrib2/LICENSE-wgrib2
%{_bindir}/wgrib2


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 3.1.3-6
- Rebuild for hdf5 1.14.5

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.3-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 28 2023 Orion Poplawski <orion@nwra.com> - 3.1.3-2
- Rebuild for jasper 4.1

* Wed Oct 25 2023 Orion Poplawski <orion@nwra.com> - 3.1.3-1
- Update to 3.1.3

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Orion Poplawski <orion@nwra.com> - 3.1.2-2
- Build with AEC support

* Thu May 18 2023 Orion Poplawski <orion@nwra.com> - 3.1.2-1
- Update to 3.1.2

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 14 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.8-11
- jasper3: use wrapper entry point for jpeg2000 decoder

* Sun Feb 13 2022 Josef Ridky <jridky@redhat.com> - 2.0.8-10
- Rebuilt for libjasper.so.6

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 2.0.8-8
- Rebuild for netcdf 4.8.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 05 2021 Orion Poplawski <orion@nwra.com> - 2.0.8-6
- Use mariadb-connector-c-devel on EL8+

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 17 2019 Orion Poplawski <orion@nwra.com> - 2.0.8-1
- Update to 2.0.8

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Orion Poplawski <orion@nwra.com> - 2.0.6c-1
- Update to 2.0.6c
- Use mariadb-connector-c on Fedora 28+ (Bug #1494081)
- Use %%g2clib

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Orion Poplawski <orion@cora.nwra.com> - 2.0.5-4
- Rebuild for MariaDB 10.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Than Ngo <than@redhat.com> - 2.0.5-2
- add support jasper-2.0.0

* Sun Dec 04 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.5-1
- Update to 2.0.5

* Sun Dec 04 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.3-3
- Rebuild for jasper 2.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.3-1
- Update to 2.0.3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 2 2014 Orion Poplawski <orion@cora.nwra.com> - 2.0.1-3
- Enable PNG and JPEG2000 support (bug #1159591)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Orion Poplawski <orion@cora.nwra.com> - 2.0.1-1
- Update to 2.0.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 3 2013 Orion Poplawski <orion@cora.nwra.com> - 1.9.9-2
- Fix -Werror=format-security (bug #1037383)

* Fri Sep 20 2013 Orion Poplawski <orion@cora.nwra.com> - 1.9.9-1
- Update to 1.9.9

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Orion Poplawski <orion@cora.nwra.com> - 1.9.8-1
- Update to 1.9.8
- Specfile cleanup

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Orion Poplawski <orion@cora.nwra.com> - 1.9.7a-2
- Rebuild with g2clib-1.4.0-3 bugfix

* Fri Nov 16 2012 Orion Poplawski <orion@cora.nwra.com> - 1.9.7a-1
- Update to 1.9.7a

* Tue Nov 13 2012 Orion Poplawski <orion@cora.nwra.com> - 1.9.7-1
- Update to 1.9.7

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.6a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 6 2012 Orion Poplawski <orion@cora.nwra.com> - 1.9.6a-1
- Update to 1.9.6a

* Fri May 18 2012 Orion Poplawski <orion@cora.nwra.com> - 1.9.6-1
- Update to 1.9.6
- Disable gctpc support for now - bundled library

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 3 2011 Orion Poplawski <orion@cora.nwra.com> - 1.9.5.1-1
- Update to 1.9.5.1

* Fri Dec 2 2011 Orion Poplawski <orion@cora.nwra.com> - 1.9.5-1
- Update to 1.9.5

* Tue Aug 16 2011 Orion Poplawski <orion@cora.nwra.com> - 1.9.4-1
- Update to 1.9.4

* Fri May 27 2011 Orion Poplawski <orion@cora.nwra.com> - 1.9.3a-1
- Update to 1.9.3a
- Upstream now provides tarball without other library tarballs
- Drop ifdef patch fixed upstream

* Thu May 26 2011 Orion Poplawski <orion@cora.nwra.com> - 1.9.3-1
- Update to 1.9.3
- Add patch to fix ifdef typo
- Drop parallel make, not safe

* Thu Mar 31 2011 Orion Poplawski <orion@cora.nwra.com> - 1.9.1.c-1
- Update to 1.9.1.c

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 1.9.1-5
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Fri Feb 18 2011 Orion Poplawski <orion@cora.nwra.com> - 1.9.1-4
- Rebuild for new g2clib - fix grib handling on 64-bit machines

* Thu Feb 17 2011 Orion Poplawski <orion@cora.nwra.com> - 1.9.1-3
- Rebuild for new g2clib - fix grib handling on 64-bit machines

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 2 2010 Orion Poplawski <orion@cora.nwra.com> - 1.9.1-1
- Update to 1.9.1

* Mon Nov 8 2010 Orion Poplawski <orion@cora.nwra.com> - 1.9.0-1
- Update to 1.9.0

* Wed Aug 11 2010 Orion Poplawski <orion@cora.nwra.com> - 1.8.6-1
- Update to 1.8.6

* Thu Jul 1 2010 Orion Poplawski <orion@cora.nwra.com> - 1.8.5-1
- Update to 1.8.5

* Mon May 17 2010 Orion Poplawski <orion@cora.nwra.com> - 1.8.4-1
- Update to 1.8.4

* Mon Mar 8 2010 Orion Poplawski <orion@cora.nwra.com> - 1.8.3-1
- Update to 1.8.3

* Tue Dec  8 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.8.2-3
- Explicitly BR g2clib-static in accordance with the Packaging
  Guidelines (g2clib-devel is still static-only).

* Thu Nov 12 2009 Orion Poplawski <orion@cora.nwra.com> - 1.8.2-2
- Rebuild for netcdf 4.1.0

* Fri Nov 6 2009 Orion Poplawski <orion@cora.nwra.com> - 1.8.2-1
- Update to 1.8.2

* Mon Aug 24 2009 Orion Poplawski <orion@cora.nwra.com> - 1.8.1-1
- Update to 1.8.1

* Thu Aug 20 2009 Orion Poplawski <orion@cora.nwra.com> - 1.8.0-1
- Update to 1.8.0
- Only ship the wgrib2 source
- Compile with mysql and netcdf4 support

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.8j-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Orion Poplawski <orion@cora.nwra.com> - 1.7.8j-1
- Update to 1.7.8j
- Drop flags patch, can now pass flags to make

* Fri Apr 10 2009 Orion Poplawski <orion@cora.nwra.com> - 1.7.8g-1
- Update to 1.7.8g
- Fix up flags patch to preserve CFLAGS from environment

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.7.i-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 Orion Poplawski <orion@cora.nwra.com> - 1.7.7.i-1
- Update to 1.7.7.i

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.7.2b-2
- Fix Patch0:/%%patch mismatch.

* Mon May 19 2008 Orion Poplawski <orion@cora.nwra.com> - 1.7.2b-1
- Update to 1.7.2b
- Update makefile patch

* Wed Mar 19 2008 Orion Poplawski <orion@cora.nwra.com> - 1.7.2-1
- Initial Fedora package
