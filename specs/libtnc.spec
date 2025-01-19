%global _hardened_build 1

Name:		libtnc
Version:	1.25
Release:	47%{?dist}
Summary:	Library implementation of the Trusted Network Connect (TNC) specification
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0:		libtnc-1.25-bootstrap.patch
Patch1:		libtnc-1.25-syserror.patch
Patch2:		libtnc-1.25-symbolfix.patch
URL:		http://libtnc.sourceforge.net/
BuildRequires:  gcc
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	libxml2-devel, zlib-devel, perl(ExtUtils::MakeMaker)
BuildRequires: make

%description
This library provides functions for loading and interfacing with loadable IMC
Integrity Measurement Collector (IMC) and Integrity Measurement Verifier (IMV)
modules as required by the Trusted Network Computing (TNC) IF-IMC and IF-IMV 
interfaces as described in: https://www.trustedcomputinggroup.org/specs/TNC

%package devel
Summary:	Development headers and libraries for libtnc
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header and library files used for developing with (or linking to) libtnc.

%package -n perl-Interface-TNC
Version:	1.0
Summary:	Perl module for TNC interfaces
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl

%description -n perl-Interface-TNC
Perl module for TNC interfaces

%prep
%setup -q

pushd Interface-TNC
tar xf Interface-TNC-1.0.tar.gz
popd

%patch -P0 -p1 -b .bootstrap
%patch -P1 -p1 -b .syserror
%patch -P2 -p1 -b .symbolfix

%build
# Switch to C89 mode due to many C99 compatibility issues.
%global build_type_safety_c 0
%set_build_flags
CC="$CC -std=gnu89"
CFLAGS="%{optflags} -fPIC -DPIC"
%configure --with-pic
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

pushd Interface-TNC/Interface-TNC-1.0
%{__perl} Makefile.PL INSTALLDIRS=vendor
# Switch to C89 mode due to undefined functions.  See bug #2154693.
make CC="$CC" %{?_smp_mflags}
popd

%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/%{_libdir}/*.la
# It is easier to delete the static libs here than to disable them in configure
# Autoconf makes my brain bleed.
rm -rf %{buildroot}/%{_libdir}/*.a

pushd Interface-TNC/Interface-TNC-1.0
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
popd

%check
# Doesn't work properly until libraries are installed.
# make check

%ldconfig_scriptlets

%files
%doc COPYING README
%{_libdir}/libosc_im*.so.*
%{_libdir}/libsample_im*.so.*
%{_libdir}/libtnc.so.*

%files devel
%doc doc/libtnc.pdf
%{_includedir}/libtnc*.h
%{_includedir}/tnc*.h
%{_libdir}/libosc_im*.so
%{_libdir}/libsample_im*.so
%{_libdir}/libtnc.so

%files -n perl-Interface-TNC
%doc Interface-TNC/Interface-TNC-1.0/README
%{perl_vendorarch}/auto/Interface/
%{perl_vendorarch}/Interface/
%{_mandir}/man3/Interface::TNC*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0-46
- convert license to SPDX

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0-45
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-43
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 16 2023 Florian Weimer <fweimer@redhat.com> - 1.25-40
- Set build_type_safety_c to 0 (#2154692)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-38
- Perl 5.38 rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Tom Callaway <spot@fedoraproject.org> - 1.25-36
- fix missing symbols that the perl module was looking for in this crufty old dinosaur

* Sun Dec 18 2022 Florian Weimer <fweimer@redhat.com> - 1.25-35
- Build in C89 due to C99 compatibility issues (#2154692)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-33
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-30
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-28
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Callaway <spot@fedoraproject.org> - 1.25-26
- use syserror instead of sys_errlist because sys_errlist is gone in latest glibc

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-25
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-22
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-19
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-15
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-13
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-10
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.25-9
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Tom Callaway <spot@fedoraproject.org> - 1.25-6
- harden-build
- cleanup spec
- package perl bits
- run make check

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Feb 17 2011 Tom Callaway <tcallawa@redhat.com> 1.25-1
- update to 1.25

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Mar 19 2010 Tom "spot" Callaway <tcallawa@redhat.com> 1.24-1
- update to 1.24

* Fri Jan 29 2010 Tom "spot" Callaway <tcallawa@redhat.com> 1.23-1
- update to 1.23

* Wed Sep  2 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.22-1
- update to 1.22

* Tue May 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.19-1
- initial Fedora package
