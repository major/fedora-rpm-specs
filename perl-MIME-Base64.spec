Name:           perl-MIME-Base64
Version:        3.16
Release:        499%{?dist}
Summary:        Encoding and decoding of Base64 and quoted-printable strings
# Base.xs:      (GPL-1.0-or-later OR Artistic-1.0-Perl) AND metamail
# Other files:  GPL-1.0-or-later OR Artistic-1.0-Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND metamail
URL:            https://metacpan.org/release/MIME-Base64
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/MIME-Base64-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional tests:
# Perl::API not yet packaged and does not work since perl 5.8.8
Conflicts:      perl < 4:5.22.0-347

%description
This package contains a Base64 encoder/decoder and a quoted-printable
encoder/decoder. These encoding methods are specified in RFC 2045 - MIME
(Multipurpose Internet Mail Extensions).

%prep
%setup -q -n MIME-Base64-%{version}

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
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/MIME*
%{_mandir}/man3/*

%changelog
* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.16-499
- Increase release to favour standalone package

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.16-490
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.16-489
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.16-488
- Increase release to favour standalone package

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.16-479
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.16-478
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.16-477
- Increase release to favour standalone package

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.16-1
- 3.16 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-458
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Petr Pisar <ppisar@redhat.com> - 3.15-457
- Modernize a spec file

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.15-456
- Increase release to favour standalone package

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.15-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.15-416
- Increase release to favour standalone package

* Wed Mar 07 2018 Petr Pisar <ppisar@redhat.com> - 3.15-397
- Modernize spec file

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.15-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-366
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.15-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-349
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 01 2015 Petr Pisar <ppisar@redhat.com> 3.15-348
- Specfile autogenerated by cpanspec 1.78.
