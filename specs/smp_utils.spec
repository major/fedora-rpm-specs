Summary:        Utilities for SAS management protocol (SMP)
Name:           smp_utils
Version:        0.99
Release:        13%{?dist}
License:        BSD-3-Clause
URL:            http://sg.danny.cz/sg/smp_utils.html
Source0:        http://sg.danny.cz/sg/p/%{name}-%{version}.tgz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: make
BuildRequires:  gcc


%description
This is a package of utilities. Each utility sends a Serial Attached
SCSI (SAS) Management Protocol (SMP) request to a SMP target.
If the request fails then the error is decoded. If the request succeeds
then the response is either decoded, printed out in hexadecimal or
output in binary. This package supports multiple interfaces since
SMP passthroughs are not mature. This package supports the linux
2.4 and 2.6 series and should be easy to port to other operating
systems.

Warning: Some of these tools access the internals of your system
and the incorrect usage of them may render your system inoperable.


%package libs
Summary: Shared library for %{name}

%description libs
This package contains the shared library for %{name}.


%package devel
Summary: Development library and header files for the smp_utils library
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the %{name} library and its header files for
developing applications.


%prep
%autosetup -p1


%build
%configure --disable-static

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?smp_mflags} CFLAGS="%{optflags} -DSMP_UTILS_LINUX"


%install
make install \
        PREFIX=%{_prefix} \
        DESTDIR=%{buildroot}

rm -rf %{buildroot}%{_libdir}/*.la


%files
%doc ChangeLog COPYING COVERAGE CREDITS README
%{_bindir}/*
%{_mandir}/man8/*

%files libs
%doc COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/scsi/*.h
%{_libdir}/*.so


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 15 2024 Stephane Thiell <sthiell@stanford.edu> - 0.99-12
- use SPDX license BSD-3-Clause

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.99-11
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 21 2020 Dan Horák <dan[at]danny.cz> - 0.99-1
- updated to 0.99 (#1815273)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Dan Horák <dan[at]danny.cz> - 0.98-13
- fix build with new glibc - use sysmacros.h for major()/minor()

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 09 2017 Dan Horák <dan[at]danny.cz> - 0.98-8
- updated for #1230500

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.98-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Dan Horák <dan[at]danny.cz> - 0.98-1
- updated to 0.98 (#1102035)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 02 2013 Dan Horák <dan[at]danny.cz> - 0.97-4
- rebuilt for aarch64 (#926546)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 28 2012 Dan Horák <dan[at]danny.cz> 0.97-1
- updated to 0.97

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 18 2011 Dan Horák <dan[at]danny.cz> 0.96-1
- updated to 0.96

* Fri Feb 18 2011 Dan Horák <dan[at]danny.cz> 0.95-1
- updated to 0.95

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar  9 2009 Dan Horák <dan[at]danny.cz> 0.94-2
- update BuildRoot

* Mon Feb  2 2009 Dan Horák <dan[at]danny.cz> 0.94-1
- update for Fedora compliance

* Mon Dec 29 2008 - dgilbert at interlog dot com
- adjust sgv4 for lk 2.6.27, sync with sas2r15
  * smp_utils-0.94
* Sun Jan 06 2008 - dgilbert at interlog dot com
- sync with sas2r13, add 'sgv4' interface
  * smp_utils-0.93
* Fri Dec 08 2006 - dgilbert at interlog dot com
- sync against sas2r07, add smp_conf_general
  * smp_utils-0.92
* Tue Aug 22 2006 - dgilbert at interlog dot com
- add smp_phy_test and smp_discover_list, uniform exit status values
  * smp_utils-0.91
* Sun Jun 11 2006 - dgilbert at interlog dot com
- add smp_read_gpio, smp_conf_route_info and smp_write_gpio
  * smp_utils-0.90
