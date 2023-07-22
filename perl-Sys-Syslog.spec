# Run optional tests
%if ! (0%{?rhel})
%bcond_without perl_Sys_Syslog_enables_optional_test
%else
%bcond_with perl_Sys_Syslog_enables_optional_test
%endif
Name:           perl-Sys-Syslog
Version:        0.36
Release:        501%{?dist}
Summary:        Perl interface to the UNIX syslog(3) calls
# README:               GPL+ or Artistic
# ppport.h:             GPL+ or Artistic
# Syslog.pm:            GPL+ or Artistic
## Unbundled
# fallback/syslog.h:    BSD
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sys-Syslog
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SAPER/Sys-Syslog-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl(XSLoader)
# DynaLoader not used
# Tests:
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
# Optional tests:
%if !%{defined perl_bootstrap} && %{with perl_Sys_Syslog_enables_optional_test}
%if !0%{?rhel}
BuildRequires:  perl(Test::Distribution)
%endif
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.06
BuildRequires:  perl(Test::Portability::Files)
# POE::Component::Server::Syslog is not packaged yet
%endif
Requires:       perl(Fcntl)
Requires:       perl(XSLoader)

%{?perl_default_filter}

%description
Sys::Syslog is an interface to the UNIX syslog(3) function. Call syslog() with
a string priority and a list of printf() arguments just like at syslog(3).

%prep
%setup -q -n Sys-Syslog-%{version}

chmod -x eg/*
# Inhibit bundled syslog.h
rm -rf fallback
perl -i -ne 'print $_ unless m{^fallback/}' MANIFEST
# Recode files
for F in Changes; do
    iconv -f ISO-8859-1 -t UTF-8 < "$F" >"${F}.utf8"
    touch -r "$F" "${F}.utf8"
    mv "${F}.utf8" "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes eg README 
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Sys*
%{_mandir}/man3/*

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-501
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-500
- Perl 5.38 re-rebuild of bootstrapped packages

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-499
- Increase release to favour standalone package

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-491
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-490
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-489
- Perl 5.36 re-rebuild of bootstrapped packages

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-488
- Increase release to favour standalone package

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-480
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-479
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-478
- Perl 5.34 re-rebuild of bootstrapped packages

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-477
- Increase release to favour standalone package

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-459
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-458
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-457
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-456
- Increase release to favour standalone package

* Thu Feb 06 2020 Tom Stellard <tstellar@redhat.com> - 0.36-3
- Spec file cleanups: Use make_build, make_install macros, and use NO_PACKLIST=1
- https://docs.fedoraproject.org/en-US/packaging-guidelines/#_parallel_make
- https://fedoraproject.org/wiki/Perl/Tips#ExtUtils::MakeMake

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 22 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-1
- 0.36 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-439
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-438
- Increase release to favour standalone package

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-419
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-417
- Perl 5.28 re-rebuild of bootstrapped packages

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-416
- Increase release to favour standalone package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-397
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-394
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.35-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 05 2016 Petr Pisar <ppisar@redhat.com> - 0.35-1
- 0.35 bump

* Wed Aug 03 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-4
- Avoid loading optional modules from default . (CVE-2016-1238)

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-3
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.34-2
- Perl 5.24 rebuild

* Fri May 06 2016 Petr Pisar <ppisar@redhat.com> - 0.34-1
- 0.34 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-312
- Perl 5.22 rebuild

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-311
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-7
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.33-4
- Perl 5.18 re-rebuild of bootstrapped packages

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 0.33-2
- Perl 5.18 rebuild

* Fri May 24 2013 Petr Pisar <ppisar@redhat.com> - 0.33-1
- 0.33 bump

* Tue Apr 09 2013 Petr Pisar <ppisar@redhat.com> 0.32-1
- Specfile autogenerated by cpanspec 1.78.
