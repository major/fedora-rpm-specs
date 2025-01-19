Name:           perl-Clownfish
Version:        0.6.3
Release:        25%{?dist}
Summary:        Apache Clownfish symbiotic object system
# The LICENSE file declares sinces 0.5.0 that portions of the libcmark libary
# from the CommonMark project are bundled. But I cannot find any of the code
# in the Clownfish. I believe the declaration concerns Clownfish-CFC sources
# instead.
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://metacpan.org/release/Clownfish
Source0:        https://cpan.metacpan.org/authors/id/N/NW/NWELLNHOF/Clownfish-%{version}.tar.gz
# There is charmonizer.c which is becoming a separate project
# <git://git.apache.org/lucy-charmonizer.git>. However, lucy-charmonizer has
# not yet been released <http://lucy.apache.org/download.html>.
# A build-time dependency Clownfish::CFC::Perl::Build::Charmonic
# still relies on the local location. Provided charmonizer.c is used only
# at build time and upstream code is not ready for external lucy-charmonizer
# (upstream treats it like a build-time only copy library) I'm not going to
# unbudle the charmonizer.c now.
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# Modules from buildlib are used when building
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clownfish::CFC::Perl::Build) >= 0.006003
BuildRequires:  perl(Clownfish::CFC::Perl::Build::Charmonic)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
# Module::Build not used (only when releasing a tar ball)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Generates perl binding, needs header files
BuildRequires:  perl-devel
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
# Generates perl binding, needs perl header files that are included from
# templates installed into _include directory.
Requires:       perl-devel%{?_isa}
Requires:       perl(DynaLoader)

%description
The Apache Clownfish "symbiotic" object system for C is designed to pair
with a "host" dynamic language environment, facilitating the development
of high performance host language extensions. Clownfish classes are
declared in header files with a .cfh extension. The Clownfish headers are
used by the Clownfish compiler to generate C header files and host
language bindings. Methods, functions and variables are defined in normal
C source files.

%prep
%setup -q -n Clownfish-%{version}

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc CONTRIBUTING.md NOTICE README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Clownfish*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.3-24
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.3-22
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.3-18
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.3-15
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.3-12
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.3-9
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.3-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.3-3
- Perl 5.28 rebuild

* Thu Mar  1 2018 Florian Weimer <fweimer@redhat.com> - 0.6.3-2
- Rebuild with new redhat-rpm-config/perl build flags

* Tue Feb 27 2018 Petr Pisar <ppisar@redhat.com> - 0.6.3-1
- 0.6.3 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 23 2017 Petr Pisar <ppisar@redhat.com> - 0.6.2-1
- 0.6.2 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.1-5
- Perl 5.26 rebuild

* Tue May 16 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.1-4
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Petr Pisar <ppisar@redhat.com> - 0.6.1-2
- Fix dependency declaration on Clownfish::CFC::Perl::Build

* Wed Dec 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.1-1
- 0.6.1 bump

* Fri Dec 02 2016 Petr Pisar <ppisar@redhat.com> - 0.6.0.5-1
- 0.6.0.5 bump

* Mon Oct 10 2016 Petr Pisar <ppisar@redhat.com> - 0.6.0.4-1
- 0.6.0.4 bump

* Thu Oct 06 2016 Petr Pisar <ppisar@redhat.com> - 0.6.0.3-1
- 0.6.0.3 bump

* Mon Oct 03 2016 Petr Pisar <ppisar@redhat.com> - 0.6.0-1
- 0.6.0 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.5.1-2
- Perl 5.24 rebuild

* Mon Apr 25 2016 Petr Pisar <ppisar@redhat.com> - 0.5.1-1
- 0.5.1 bump

* Mon Apr 04 2016 Petr Pisar <ppisar@redhat.com> - 0.5.0-1
- 0.5.0 bump

* Fri Feb 05 2016 Petr Pisar <ppisar@redhat.com> - 0.4.4-1
- 0.4.4 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Petr Pisar <ppisar@redhat.com> - 0.4.3-1
- 0.4.3 bump

* Thu Sep 17 2015 Petr Pisar <ppisar@redhat.com> 0.4.2-1
- Specfile autogenerated by cpanspec 1.78.
