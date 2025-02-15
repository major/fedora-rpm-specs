Name:           ncview
Version:        2.1.11
Release:        1%{?dist}
Summary:        A visual browser for netCDF format files
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://cirrus.ucsd.edu/ncview/
Source0:        https://cirrus.ucsd.edu/~pierce/ncview/ncview-%{version}.tar.gz
# Remove RPATH
Patch0:         ncview-rpath.patch
# Fix compilation with gcc 15
Patch1:         ncview-fixes.patch

BuildRequires: make
BuildRequires:  xorg-x11-proto-devel libXaw-devel libXt-devel libXext-devel
BuildRequires:  libXmu-devel libICE-devel libSM-devel libX11-devel
BuildRequires:  libpng-devel
BuildRequires:  netcdf-devel udunits2-devel
BuildRequires:  expat-devel
BuildRequires:  chrpath

%description
Ncview is a visual browser for netCDF format files.  Typically you
would use ncview to get a quick and easy, push-button look at your
netCDF files.  You can view simple movies of the data, view along
various dimensions, take a look at the actual data values, change
color maps, invert the data, etc.

%prep
%autosetup -p1


%build
# We need to pass X_CFLAGS to properly compile configure tests for X libraries
%configure X_CFLAGS="%{optflags}" --with-udunits2_incdir=%{_includedir}/udunits2 \
 --x-libraries=%{_libdir}  --datadir=%{_datadir}/ncview
#  WARNING!
#  The parallel build was tested and it does NOT work.
#  make %{?_smp_mflags}
make
sed s=NCVIEW_LIB_DIR=%{_datadir}/ncview= < data/ncview.1.sed > data/ncview.1


%install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/X11/app-defaults
cp -p Ncview-appdefaults ${RPM_BUILD_ROOT}%{_datadir}/X11/app-defaults/Ncview
%makeinstall NCVIEW_LIB_DIR=${RPM_BUILD_ROOT}%{_datadir}/ncview BINDIR=${RPM_BUILD_ROOT}%{_bindir} MANDIR=${RPM_BUILD_ROOT}%{_mandir}/man1
mkdir ${RPM_BUILD_ROOT}%{_datadir}/ncview/
install -m0644 -p *.ncmap ${RPM_BUILD_ROOT}%{_datadir}/ncview/
chmod 644 ${RPM_BUILD_ROOT}%{_datadir}/X11/app-defaults/Ncview
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1/
install -m0644 -p data/ncview.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/
# Absolutely no idea why this is needed for ppc64le
chrpath -l -d %{buildroot}%{_bindir}/ncview


%files
%license COPYING
%doc README
%{_bindir}/*
%{_datadir}/ncview/
%{_datadir}/X11/app-defaults/Ncview
%{_mandir}/man1/*


%changelog
* Wed Feb 12 2025 Orion Poplawski <orion@nwra.com> - 2.1.11-1
- Update to 2.1.11

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 18 2024 Orion Poplawski <orion@nwra.com> - 2.1.10-4
- Add patch to fix FTBFS (rhbz#2300985)

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.10-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb 07 2024 Orion Poplawski <orion@nwra.com> - 2.1.10-1
- Update to 2.1.10 (FTBFS bz#2261398)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 2.1.8-14
- Rebuild for netcdf 4.8.0

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 2.1.8-13
- Rebuild for netcdf 4.8.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com> - 2.1.8-7
- Rebuild for netcdf 4.6.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 8 2017 Orion Poplawski <orion@cora.nwra.com> - 2.1.8-1
- Update to 2.1.8

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 29 2016 Orion Poplawski <orion@cora.nwra.com> - 2.1.7-1
- Update to 2.1.7

* Mon Mar 28 2016 Orion Poplawski <orion@cora.nwra.com> - 2.1.6-1
- Update to 2.1.6
- Update license to GPLv3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.1.5-3
- Rebuild for netcdf 4.4.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Orion Poplawski <orion@cora.nwra.com> - 2.1.5-1
- Update to 2.1.5

* Fri Nov 14 2014 Orion Poplawski <orion@cora.nwra.com> - 2.1.4-1
- Update to 2.1.4

* Sat Nov 1 2014 Orion Poplawski <orion@cora.nwra.com> - 2.1.3-1
- Update to 2.1.3
- Cleanup spec

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 Orion Poplawski <orion@cora.nwra.com> - 2.1.2-1
- Update to 2.1.2

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.1.1-2
- Rebuild for new libpng

* Wed Aug 3 2011 Orion Poplawski <orion@cora.nwra.com> - 2.1.1-1
- Update to 2.1.1
- Drop cflags patch fixed upstream
- Add BR libpng-devel

* Thu Apr 14 2011 Orion Poplawski <orion@cora.nwra.com> - 2.0-0.2.beta4
- Add patch to use RPM_OPT_FLAGS (bug #696739)

* Wed Apr 6 2011 Orion Poplawski <orion@cora.nwra.com> - 2.0-0.1.beta4
- Update to 2.0beta4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.93c-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.93c-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.93c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 26 2008 Adam Jackson <ajax@redhat.com> 1.93c-4
- Drop Requires: xorg-x11-server-Xorg.

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.93c-3
- fix patch to apply with fuzz=0

* Thu Apr 10 2008 Patrice Dumas <pertusus@free.fr> - 1.93c-2
- update to 1.93c

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.92e-13
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Ed Hill <ed@eh3.com> - 1.92e-12
- add BR: netcdf-static

* Sat Aug 25 2007 Ed Hill <ed@eh3.com> - 1.92e-11
- rebuild for BuildID

* Tue Nov 14 2006 Ed Hill <ed@eh3.com> - 1.92e-10
- more cleanups for check-buildroot

* Tue Nov 14 2006 Ed Hill <ed@eh3.com> - 1.92e-9
- bz 215632

* Sat Sep  2 2006 Ed Hill <ed@eh3.com> - 1.92e-8
- rebuild for imminent FC-6 release

* Thu Feb 16 2006 Ed Hill <ed@eh3.com> - 1.92e-7
- rebuild for new gcc

* Sun Nov 20 2005 Ed Hill <ed@eh3.com> - 1.92e-6
- update for the new modular xorg-x11

* Wed Aug  3 2005 Ed Hill <ed@eh3.com> - 1.92e-5
- fix dist tag

* Wed Jul  6 2005 Ed Hill <ed@eh3.com> - 1.92e-4
- mkstemp() security fix and more cleanups

* Wed Jul  6 2005 Ed Hill <ed@eh3.com> - 1.92e-3
- move the data files to %%{_datadir} and add COPYING
- added xorg-x11 Requires and BuildRequires

* Tue Jul  5 2005 Ed Hill <ed@eh3.com> - 1.92e-2
- fix permissions, remove fortran dependency, and small cleanups

* Tue Jul  5 2005 Tom "spot" Callaway <tcallawa@redhat.com> - 1.92e-1
- Fedora Extras cleanups

* Sun Dec  5 2004 Ed Hill <eh3@mit.edu> - 0:1.92e-0.fdr.0
- Initial version

