Name:		libvpd
Version:	2.2.10
Release:	2%{?dist}
Summary:	VPD Database access library for lsvpd

License:	LGPL-2.0-or-later
URL:		https://github.com/power-ras/%{name}/releases
Source:		https://github.com/power-ras/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	sqlite-devel zlib-devel libstdc++-devel libtool
BuildRequires: make

ExclusiveArch:	%{power64}

%description
The libvpd package contains the classes that are used to access a vpd database
created by vpdupdate in the lsvpd package.

%package devel
Summary:	Header files for libvpd
Requires:	%{name} = %{version}-%{release} sqlite-devel pkgconfig
%description devel
Contains header files for building with libvpd.

%prep
%setup -q

%build
./bootstrap.sh
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find %{buildroot} -type f -name "*.la" -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README
%{_libdir}/libvpd_cxx-2.2.so.*
%{_libdir}/libvpd-2.2.so.*
%{_sysconfdir}/udev/rules.d/90-vpdupdate.rules

%files devel
%{_includedir}/libvpd-2
%{_libdir}/libvpd_cxx.so
%{_libdir}/libvpd.so
%{_libdir}/pkgconfig/libvpd-2.pc
%{_libdir}/pkgconfig/libvpd_cxx-2.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 29 2024 Than Ngo <than@redhat.com> - 2.2.10-1
- Update to 2.2.10
  * Fix displaying duplicate VPD details

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 16 2023 Than Ngo <than@redhat.com> - 2.2.9-5
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 07 2022 Dan Horák <dan[at]danny.cz> - 2.2.9-2
- fix development symlinks

* Wed Apr 06 2022 Than Ngo <than@redhat.com> - 2.2.9-1
- rebase to 2.2.9

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Than Ngo <than@redhat.com> - 2.2.8-1
- rebase to 2.2.8

* Tue Oct 27 2020 Jeff Law <law@redhat.com> - 2.2.7-3
- Force C++14 as this code is not C++17 ready

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Than Ngo <than@redhat.com> - 2.2.7-1
- rebase to 2.2.7

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 02 2019 Than Ngo <than@redhat.com> - 2.2.6-6
- Update Url and Source

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Sinny Kumari <sinnykumari@fedoraproject.org> - 2.2.6-3
- Add gcc-c++ as BuildRequires

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Sinny Kumari <sinnykumari@fedoraproject.org> - 2.2.6-1
- Rebase to 2.2.6
- run.vpdupdate is now created in /run instead of /var/lib/lsvpd/

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 11 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.2.5-4
- Spec cleanups
- Use %%license

* Mon Mar 21 2016 Than Ngo <than@redhat.com> - 2.2.5-3
- re-symlink *.so to SONAME, fix the symlinks issue by downgrade/upgrade

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.2.5
- Update to latest upstream 2.2.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.4-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Sep 22 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.2.4-2
- Remove NEWS file

* Mon Sep 22 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.2.4
- Update to latest upstream 2.2.4

* Fri Aug 01 2014 Brent Baude <bbaude@redhat.com> - 2.2.3-3
- NVR bump for Fedora 21 build on merged koji

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 12 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.2.3
- Update to latest upstream 2.2.3

* Tue Nov 05 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.2.2
- Update to latest upstream 2.2.2

* Wed Oct 09 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.2.1-4
- Add ppc64le architecture

* Sun Sep 15 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.2.1-3
- Remove TODO file from spec

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 18 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 2.2.1
- Update to latest upstream 2.2.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-5
- Rebuilt for c++ ABI breakage

* Wed Jan 18 2012 Jiri Skala <jskala@redhat.com> 2.1.3-4
- fix for gcc-4.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 23 2011 Jiri Skala <jskala@redhat.com> 2.1.3-2
- added ExclusiveArch for ppc[64]

* Wed Aug 10 2011 Jiri Skala <jskala@redhat.com> 2.1.3-1
- update to latest upstream 2.1.3

* Mon Feb 14 2011 Jiri Skala <jskala@redhat.com> 2.1.2-2
- rebuild due to tag correction

* Mon Feb 14 2011 Jiri Skala <jskala@redhat.com> 2.1.2-1
- Update to latest upstream 2.1.2
- fixes library numbering

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 02 2009 Eric Munson <ebmunson@us.ibm.com> - 2.1.1-1
- Update to latest libvpd release

* Wed Nov 18 2009 Eric Munson <ebmunson@us.ibm.com> - 2.1.0-5
- Bump dist for rebuild for broken dependencies

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Eric Munson <ebmunson@us.ibm.com> 2.1.0-3
- Bump dist for rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Mar 17 2008 Eric Munson <ebmunson@us.ibm.com> 2.0.1-1
- Update for libvpd-2.0.1

* Tue Feb 26 2008 Eric Munson <ebmunson@us.ibm.com> 2.0.0-2
- Updating release number for new build in FC

* Mon Feb 25 2008 Eric Munson <ebmunson@us.ibm.com> 2.0.0-1
- Updated library to use sqlite instead of berkeley db.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.5.0-2
- Autorebuild for GCC 4.3

* Mon Jan 7 2008 Eric Munson <ebmunson@us.ibm.com> -1.5.0-1
- Moved pkgconfig to devel Requires
- Updated %%defattrs to -,root,root,-
- Added AUTHORS to %%doc

* Thu Jan 3 2008 Eric Munson <ebmunson@us.ibm.com> - 1.5.0-0
- Updated Requires and Provides fields per fedora community request

* Fri Dec 7 2007 Brad Peters <bpeters@us.ibm.com> - 1.4.2-0
- Added functions to helper_functions class
- Mnior changes necessary to support new device discovery method

* Fri Nov 16 2007 Eric Munson <ebmunson@us.ibm.com> - 1.4.1-1
- Removing INSTALL from docs and docs from -devel package
- Fixing Makfile.am so libraries have the .so extension
- Using %%configure, %%{__make}, and %%{__rm} calls
- Changing source URL

* Wed Oct 31 2007 Eric Munson <ebmunson@us.ibm.com> - 1.4.0-2
- Changing files lists for libdirs to match library file names

* Tue Oct 30 2007 Eric Munson <ebmunson@us.ibm.com> - 1.4.0-1
- Adding C Library to files lists.

* Sat Oct 20 2007 Ralf Corsepius <rc040203@freenet.de>	- 1.3.5-4
- Various spec-file fixes.

* Fri Oct 19 2007 Eric Munson <ebmunson@us.ibm.com> - 1.3.5-3
- Removed hard coded /usr/lib from spec file
- Install now sets all headers to 644
- Updated license
