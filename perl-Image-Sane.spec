# Run optional test
%bcond_without perl_Image_Sane_enables_optional_test

Name:           perl-Image-Sane
Version:        5
Release:        11%{?dist}
Summary:        Perl extension for the SANE (Scanner Access Now Easy) Project
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Image-Sane
Source0:        https://cpan.metacpan.org/authors/id/R/RA/RATCLIFFE/Image-Sane-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Config)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  pkgconfig(sane-backends) >= 1.0.19
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8.5
BuildRequires:  perl(base)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(sigtrap)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
%if %{with perl_Image_Sane_enables_optional_test}
# Optional tests:
# ImageMagick for identify tool
BuildRequires:  ImageMagick
# Test::Perl::Critic not used
BuildRequires:  perl(Test::Pod) >= 1.00
# sane-backensds for scanimage tool
BuildRequires:  sane-backends
# sane-backends-drivers-scanners for "test" Sane driver
BuildRequires:  sane-backends-drivers-scanners
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
These Perl bindings for the SANE (Scanner Access Now Easy) Project allow
you to access SANE-compatible scanners in a Perlish and object-oriented
way, freeing you from the casting and memory management in C, yet remaining
very close in spirit to original API.

%prep
%setup -q -n Image-Sane-%{version}
chmod -x examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset TEST_AUTHOR
make test

%files
%doc Changes examples README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Image*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5-10
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 5-7
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5-4
- Perl 5.32 rebuild

* Thu Mar 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5-3
- Specify all dependencies

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Petr Pisar <ppisar@redhat.com> - 5-1
- Version 5 bump

* Thu Sep 12 2019 Petr Pisar <ppisar@redhat.com> - 4-1
- Version 4 bump

* Wed Sep 11 2019 Petr Pisar <ppisar@redhat.com> - 3-1
- Version 3 bump

* Tue Sep 10 2019 Petr Pisar <ppisar@redhat.com> - 2-1
- Version 2 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Petr Pisar <ppisar@redhat.com> - 0.14-1
- 0.14 bump

* Fri Jul 07 2017 Petr Pisar <ppisar@redhat.com> - 0.13-1
- 0.13 bump

* Mon Jul 03 2017 Petr Pisar <ppisar@redhat.com> 0.12-1
- Specfile autogenerated by cpanspec 1.78.
