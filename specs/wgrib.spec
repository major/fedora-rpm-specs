Name:           wgrib
Version:        1.8.5
Release:        5%{?dist}
Summary:        Manipulate, inventory and decode GRIB files

License:        LicenseRef-Fedora-Public-Domain
URL:            https://www.cpc.ncep.noaa.gov/products/wesley/wgrib.html
Source0:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/wgrib.c.v%{version}
Source1:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/Changes
Source2:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/NOTICE
Source3:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/double_prec.txt
Source4:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/formats.txt
Source5:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/formats_update.txt
Source6:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/grib2ieee.txt
Source7:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/misc.txt
Source8:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/porting.txt
Source9:        https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/usertables.txt
Source10:       https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/tricks.wgrib
Source11:       https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/land.grb
Source12:       https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/testbin.c
Source13:       https://ftp.cpc.ncep.noaa.gov/wd51we/wgrib/testbin.f
Source14:       testbin.out
# Include <stdlib.h> and set int return for main() for C99 compliance
Patch0:         wgrib-c99.patch
BuildRequires:  gcc


%description
WGRIB is a program to manipulate, inventory and decode GRIB files.


%prep
%setup -q -c -T
cp %SOURCE0 wgrib.c
cp %SOURCE1 .
cp %SOURCE2 .
cp %SOURCE3 .
cp %SOURCE4 .
cp %SOURCE5 .
cp %SOURCE6 .
cp %SOURCE7 .
cp %SOURCE8 .
cp %SOURCE9 .
cp %SOURCE10 .
cp %SOURCE11 .
cp %SOURCE12 .
cp %SOURCE13 .
%patch -P0 -p0 -b .c99


%build
gcc %{build_cflags} %{build_ldflags} -o wgrib wgrib.c


%install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 wgrib $RPM_BUILD_ROOT%{_bindir}/


%check
./wgrib land.grb -d 1
gcc %{build_cflags} %{build_ldflags} -o testbin testbin.c -lm
./testbin > testbin.out && diff %SOURCE14 testbin.out



%files
%doc Changes *.txt tricks.wgrib testbin.[cf] land.grb
%{_bindir}/wgrib


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 19 2024 Orion Poplawski <orion@nwra.com> - 1.8.5-4
- Use SPDX license tag

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 11 2023 Orion Poplawski <orion@nwra.com> - 1.8.5-1
- Update to 1.8.5

* Mon Sep 11 2023 Orion Poplawski <orion@nwra.com> - 1.8.4-1
- Update to 1.8.4

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 02 2023 Orion Poplawski <orion@nwra.com> - 1.8.3-2
- Add ldflags to build for proper hardening

* Fri May 26 2023 Orion Poplawski <orion@nwra.com> - 1.8.3-1
- Update to 1.8.3

* Fri Feb 17 2023 Florian Weimer <fweimer@redhat.com> - 1.8.2-10
- Add missing #include <stdlib.h> for C99 compatibility

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr  9 2019 Orion Poplawski <orion@nwra.com> - 1.8.2-1
- Update to 1.8.2

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1.2c-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Orion Poplawski <orion@nwra.com> - 1.8.1.2c-11
- Add BR gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1.2c-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1.2c-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1.2c-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1.2c-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1.2c-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1.2c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1.2c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1.2c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1.2c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 15 2013 - Orion Poplawski <orion@cora.nwra.com> - 1.8.1.2c-1
- Update to 1.8.1.2c

* Wed Oct 16 2013 - Orion Poplawski <orion@cora.nwra.com> - 1.8.1.2b-1
- Update to 1.8.1.2b

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1.2a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1.2a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1.2a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1.2a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 29 2011 - Orion Poplawski <orion@cora.nwra.com> - 1.8.1.2a-1
- Update to 1.8.1.2a

* Thu May 26 2011 - Orion Poplawski <orion@cora.nwra.com> - 1.8.1.0h-1
- Update to 1.8.1.0h

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1.0d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 2 2010 - Orion Poplawski <orion@cora.nwra.com> - 1.8.1.0d-1
- Update to 1.8.1.0d

* Mon May 17 2010 - Orion Poplawski <orion@cora.nwra.com> - 1.8.1.0b-1
- Update to 1.8.1.0b

* Tue Mar 30 2010 - Orion Poplawski <orion@cora.nwra.com> - 1.8.0.13f-1
- Update to 1.8.0.13f

* Wed Feb 24 2010 - Orion Poplawski <orion@cora.nwra.com> - 1.8.0.13e-1
- Update to 1.8.0.13e

* Thu Sep 24 2009 - Orion Poplawski <orion@cora.nwra.com> - 1.8.0.13d-1
- Update to 1.8.0.13d

* Mon Aug 24 2009 - Orion Poplawski <orion@cora.nwra.com> - 1.8.0.13b-1
- Update to 1.8.0.13b

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0.12u-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0.12u-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep  4 2008 - Orion Poplawski <orion@cora.nwra.com> - 1.8.0.12u-1
- Update to 1.8.0.12u

* Fri Feb  8 2008 - Orion Poplawski <orion@cora.nwra.com> - 1.8.0.12q-1
- Update to 1.8.0.12q

* Thu Aug 23 2007 - Orion Poplawski <orion@cora.nwra.com> - 1.8.0.12o-2
- Rebuild for BuildID

* Wed Aug  8 2007 - Orion Poplawski <orion@cora.nwra.com> - 1.8.0.12o-1
- Update to 1.8.0.12o

* Tue Dec  5 2006 - Orion Poplawski <orion@cora.nwra.com> - 1.8.0.12g-2
- Compile testbin with -lm, needed on x86_64

* Fri Nov 17 2006 - Orion Poplawski <orion@cora.nwra.com> - 1.8.0.12g-1
- Update to 1.8.0.12g
- Ship testbin.c, testbin.f, and lang.grb for local testing

* Thu Nov 16 2006 - Orion Poplawski <orion@cora.nwra.com> - 1.8.0.12b-2
- Add check

* Wed Nov 15 2006 - Orion Poplawski <orion@cora.nwra.com> - 1.8.0.12b-1
- Initial version
