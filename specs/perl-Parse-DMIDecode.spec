# Perform optional tests
%bcond_without perl_Parse_DMIDecode_enables_optional_tests

Name:           perl-Parse-DMIDecode
Version:        0.03
Release:        39%{?dist}
Summary:        Interface to SMBIOS using dmidecode
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://metacpan.org/release/Parse-DMIDecode
Source0:        https://cpan.metacpan.org/modules/by-module/Parse/Parse-DMIDecode-%{version}.tar.gz
# Pod fixing patch from RT 52296 -> https://rt.cpan.org/Ticket/Attachment/699959/360879/fix-pod-urls.patch
Patch1:         fix-pod-urls.patch
# Fix a memory leak when destructing Parse::DMIDecode::Handle objects,
# CPAN RT#125088
Patch2:         Parse-DMIDecode-0.03-handle_leak.patch
# Fix supressing portability warnings, CPAN RT#143252, proposed to the upstream
Patch3:         Parse-DMIDecode-0.03-Disable-portability-warnings-lexically.patch
# Do not warn on SMBIOS version 3, bug #1661251, CPAN RT#54956, proposed to
# the upstream
Patch4:         Parse-DMIDecode-0.03-Emulate-number-of-structures-if-not-reported-by-dmid.patch
# This mirrors the ExclusiveArch in the dmidecode spec file
ExclusiveArch:  %{ix86} x86_64 ia64 aarch64
# A debug package is not required as there are no binaries in this package. We
# are not noarch because of dmidecode
%global debug_package %{nil}
BuildRequires:  coreutils
BuildRequires:  dmidecode
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# Config not used
# LWP::UserAgent not used
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Which) >= 0.05
BuildRequires:  perl(warnings)
# Optional run-time:
BuildRequires:  perl(Data::Dumper)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
%if %{with perl_Parse_DMIDecode_enables_optional_tests}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.2
BuildRequires:  perl(Test::Pod::Coverage) >= 1.06
%endif
Requires:       dmidecode
Suggests:       perl(Data::Dumper)
Requires:       perl(File::Which) >= 0.05

%description
This module provides an OO interface to SMBIOS information through the
dmidecode command which is known to work under a number of Linux, BSD and
BeOS variants.

%prep
%autosetup -p1 -n Parse-DMIDecode-%{version}
%if !%{with perl_Parse_DMIDecode_enables_optional_tests}
rm t/10pod.t t/11pod_coverage.t
perl -i -ne 'print $_ unless m{^t/1[01]pod}' MANIFEST
%endif

%build
AUTOMATED_TESTING=1 %{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset DEBUG
./Build test

%files
%license LICENSE
%doc Changes NOTICE README TODO examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.03-38
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Petr Pisar <ppisar@redhat.com> - 0.03-31
- Fix supressing portability warnings (CPAN RT#143252)
- Do not warn on SMBIOS version 3 (bug #1661251)

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-30
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-27
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-24
- Perl 5.32 rebuild

* Thu Mar 26 2020 Petr Pisar <ppisar@redhat.com> - 0.03-23
- Fix a memory leak when destructing Parse::DMIDecode::Handle objects
  (CPAN RT#125088)

* Wed Mar 25 2020 Petr Pisar <ppisar@redhat.com> - 0.03-22
- Modernize a spec file

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-19
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-16
- Perl 5.28 rebuild

* Fri Mar 02 2018 Petr Pisar <ppisar@redhat.com> - 0.03-15
- Adapt to removing GCC from a build root (bug #1547165)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-11
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-9
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-6
- Perl 5.22 rebuild

* Sat Oct 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.03-5
- dmidecode supported on aarch64

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 David Dick <ddick@cpan.org> - 0.03-1
- Initial release
