Name:           sblim-cmpi-rpm
Version:        1.0.1
Release:        40%{?dist}
Summary:        CIM access to installed software packages (currently RPMs)

License:        CPL-1.0
URL:            http://sblim.wiki.sourceforge.net/ProviderCmpiRpm
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
Patch0:         sblim_cmpi_rpm_ldl_library.patch
Patch1:         sblim-cmpi-rpm-1.0.1-docdir.patch
Patch2:         sblim-cmpi-rpm-1.0.1-page-size.patch
Patch3:         sblim-cmpi-rpm-configure-c99.patch
Patch4:         sblim-cmpi-rpm-1.0.1-gcc14-fix.patch
BuildRequires: make
BuildRequires:  sblim-cmpi-base-devel sblim-cmpi-devel rpm-devel
BuildRequires:  gcc
Requires:       sblim-cmpi-base
Requires:       cim-server

%description
These providers list the software packages installed in a GNU/Linux system
and provide some more details about them. 


%prep
%setup -q

# Patch added to fix the missing definitions of dlopen, dlsym, dlerror.
%autopatch -p1


%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/cmpi/*.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la 


%files
%{_libdir}/libcimrpm.so.0
%{_libdir}/libcimrpm.so.0.0.0
%{_libdir}/libcimrpmv4.so.0
%{_libdir}/libcimrpmv4.so.0.0.0
%{_libdir}/libcimrpm.so
%{_libdir}/libcimrpmv4.so
%{_libdir}/cmpi/libcmpiOSBase_RpmAssociatedFileProvider.so.0
%{_libdir}/cmpi/libcmpiOSBase_RpmAssociatedFileProvider.so.0.0.0
%{_libdir}/cmpi/libcmpiOSBase_RpmFileCheckProvider.so.0
%{_libdir}/cmpi/libcmpiOSBase_RpmFileCheckProvider.so.0.0.0
%{_libdir}/cmpi/libcmpiOSBase_RpmPackageProvider.so.0
%{_libdir}/cmpi/libcmpiOSBase_RpmPackageProvider.so.0.0.0
%{_libdir}/cmpi/libcmpiOSBase_RpmAssociatedFileProvider.so
%{_libdir}/cmpi/libcmpiOSBase_RpmFileCheckProvider.so
%{_libdir}/cmpi/libcmpiOSBase_RpmPackageProvider.so
%{_datarootdir}/sblim-cmpi-rpm/Linux_RpmPackage.mof
%{_datarootdir}/sblim-cmpi-rpm/Linux_RpmPackage.registration
%{_datarootdir}/sblim-cmpi-rpm/provider-register.sh
%{_includedir}/sblim/cimrpm.h
%{_includedir}/sblim/cimrpmfp.h
%doc COPYING NEWS INSTALL README AUTHORS


%global SCHEMA %{_datadir}/%{name}/Linux_RpmPackage.mof
%global REGISTRATION %{_datadir}/%{name}/Linux_RpmPackage.registration

%pre     
function unregister()
{
  %{_datadir}/%{name}/provider-register.sh -d \
        $1 \
        -m %{SCHEMA} \
        -r %{REGISTRATION} > /dev/null 2>&1 || :;
  # don't let registration failure when server not running fail upgrade!
}

# If upgrading, deregister old version
if [ $1 -gt 1 ]
then
        unregistered=no
        if [ -e /usr/sbin/cimserver ]; then
           unregister "-t pegasus";
           unregistered=yes
        fi  
         
        if [ -e /usr/sbin/sfcbd ]; then
           unregister "-t sfcb";
           unregistered=yes
        fi  
         
        if [ "$unregistered" != yes ]; then
           unregister
        fi  
fi


%post    
function register()
{        
  # The follwoing script will handle the registration for various CIMOMs.
  %{_datadir}/%{name}/provider-register.sh \
        $1 \
        -m %{SCHEMA} \
        -r %{REGISTRATION} > /dev/null 2>&1 || :;
  # don't let registration failure when server not running fail install!
}        
         
/sbin/ldconfig
if [ $1 -ge 1 ]
then     
        registered=no
        if [ -e /usr/sbin/cimserver ]; then
          register "-t pegasus";
          registered=yes
        fi
         
        if [ -e /usr/sbin/sfcbd ]; then
          register "-t sfcb";
          registered=yes
        fi
         
        if [ "$registered" != yes ]; then
          register
        fi
fi


%preun   
function unregister()
{        
  %{_datadir}/%{name}/provider-register.sh -d \
        $1 \
        -m %{SCHEMA} \
        -r %{REGISTRATION} > /dev/null 2>&1 || :;
  # don't let registration failure when server not running fail erase!
}        
         
if [ $1 -eq 0 ]
then     
        unregistered=no
        if [ -e /usr/sbin/cimserver ]; then
          unregister "-t pegasus";
          unregistered=yes
        fi
         
        if [ -e /usr/sbin/sfcbd ]; then
          unregister "-t sfcb";
          unregistered=yes
        fi
         
        if [ "$unregistered" != yes ]; then
          unregister
        fi
fi       
         
%postun -p /sbin/ldconfig


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.1-38
- Fix FTBFS with gcc 14
  Resolves: #2261679

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 29 2023 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.1-35
- SPDX migration

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 23 2022 Florian Weimer <fweimer@redhat.com> - 1.0.1-33
- Avoid undeclared exit function in configure

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.1-30
- Fix FTBFS (remove rpath)
  Resolves: #1987988

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.1-22
- Add BuildRequires gcc
- Remove Group tag

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.1-16
- Replace 'define' with 'global'

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.1-13
- Fix getting page size
  Resolves: #1107274

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 06 2013 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.1-11
- Fix FTBFS (documentation path change)
  Resolves: #993228

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 25 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.1-6
- Add mofs registration for various CIMOMs
- Remove -devel subpackage, those files should be in main package, otherwise
  the provider will not work
- Fix spec file formatting to make rpmlint happy

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 11 2009 Praveen K Paladugu <praveen_paladugu@dell.com> - 1.0.1-4
- Added a comment about the patch.
- fixed the description

* Mon Aug 10 2009 Praveen K Paladugu <praveen_paladugu@dell.com> - 1.0.1-3
- Added the scriplets
- Fixing some rpmlint errors.
- Added a patch to add ldl library while linking.
- Removed the .la and .a files.

* Mon Jul 13 2009 Praveen K Paladugu <praveen_paladugu@dell.com> - 1.0.1-2
- Adding BuildRequries sblim-base-devel

* Thu Jul 02 2009 Praveen K Paladugu <praveen_paladugu@dell.com> - 1.0.1-1
- Packaging for Fedora

