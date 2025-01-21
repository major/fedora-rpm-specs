%global provider_dir %{_libdir}/cmpi/

Name:           sblim-smis-hba
Version:        1.0.0
Release:        37%{?dist}
Summary:        SBLIM SMIS HBA HDR Providers

License:        EPL-1.0
URL:            http://sblim.wiki.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2

# Patch0: upstream tarball doesn't contain testsuite but default Makefile is going to build it
Patch0:         sblim-smis-hba-1.0.0-no-testsuite.patch
Patch1:         sblim-smis-hba-1.0.0-include.patch
Patch2:         sblim-smis-hba-1.0.0-registration-fix.patch
# Patch3: upstream
Patch3:         sblim-smis-hba-1.0.0-pegasus-registration.patch
# Patch4: fix documentation path
Patch4:         sblim-smis-hba-1.0.0-doc-path.patch
# Patch5: call systemctl in provider registration
Patch5:         sblim-smis-hba-1.0.0-prov-reg-sfcb-systemd.patch
# Patch6: use Pegasus root/interop instead of root/PG_Interop
Patch6:         sblim-smis-hba-1.0.0-pegasus-interop.patch
# Patch7: fixes multiple definiton of variables (FTBFS with GCC 10)
Patch7:         sblim-smis-hba-1.0.0-fix-multiple-definition.patch
Patch8: sblim-smis-hba-c99.patch

BuildRequires: make
BuildRequires:  sblim-cmpi-devel, sblim-cmpi-base-devel
BuildRequires:  libhbaapi-devel
BuildRequires:  autoconf, automake, libtool
BuildRequires:  curl-devel, perl-interpreter, libsysfs-devel
BuildRequires:  binutils-devel, autoconf, automake, libtool, flex, bison

Requires:       libhbaapi
Requires:       sblim-cmpi-base cim-server

%description
SMI-S standards based HBA CMPI Providers.

%prep
%setup -q
%autopatch -p1
autoreconf -if


%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
%configure \
   TESTSUITEDIR=%{_datadir}/sblim-testsuite \
   PROVIDERDIR=%{provider_dir} \
   LDFLAGS="-L${RPM_BUILD_ROOT}%{_libdir}/cmpi";
# workaround libtool issue
sed -i -e '/not ending/ s/.*/true/' libtool
# do not use smp_flags!
make


%install
make install DESTDIR=$RPM_BUILD_ROOT
# remove unused libtool files
rm -f $RPM_BUILD_ROOT/%{_libdir}/*a
rm -f $RPM_BUILD_ROOT/%{_libdir}/cmpi/*a


%files
%doc AUTHORS COPYING README
%{_datadir}/%{name}
%{_libdir}/cmpi/libcmpiLinux_Common.so*
%{_libdir}/cmpi/libcmpiLinux_ECTP_Provider.so*
%{_libdir}/cmpi/libcmpiSMIS_HBA_HDR_Provider.so*

%global SCHEMA %{_datadir}/%{name}/Linux_SMIS_HBA_HDR.mof %{_datadir}/%{name}/Linux_SMIS_ECTP.mof
%global REGISTRATION %{_datadir}/%{name}/Linux_SMIS_HBA_HDR.reg %{_datadir}/%{name}/Linux_SMIS_ECTP.reg

%pre
%sblim_pre

%post
%sblim_post

%preun
%sblim_preun

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 29 2023 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.0-33
- SPDX migration

* Fri Apr 14 2023 Florian Weimer <fweimer@redhat.com> - 1.0.0-32
- Port to C99

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.0-28
- Fix FTBFS with autoconf-2.71

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 2020 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.0-24
- Fix multiple definiton of variables (FTBFS with GCC 10)
  Resolves: #1800075

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 05 2015 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.0-13
- Update provider registration script to use systemctl to stop/start sfcb
- Use new macros for %%pre/%%post/%%preun from sblim-cmpi-devel
- Require cim-server instead of tog-pegasus, don't BuildRequire tog-pegasus-devel

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 27 2013 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.0-10
- Fix registration with Pegasus
- Fix path to documentation

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.0-7
- Remove bogus BuildRequire of sblim-tools-libra-devel

* Mon Sep 10 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.0-6
- Fix issues found by fedora-review utility in the spec file

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.0-3
- Build with -fno-strict-aliasing, fix requires, fix registration files

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.0.0-1
- Initial support

