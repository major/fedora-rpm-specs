Name:		perl-TeX-Encode
Version:	2.010
Release:	12%{?dist}
Summary:	Encoding to LaTeX escapes
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/TeX-Encode
Source0:	https://cpan.metacpan.org/authors/id/A/AT/ATHREEF/TeX-Encode-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(blib)
BuildRequires:	perl(Carp)
BuildRequires:	perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:	perl(Encode)
BuildRequires:	perl(Encode::Encoding) >= 0.1
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Module::Metadata)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::More) >= 0.1
BuildRequires:	perl(utf8)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)

%description
This module provides encoding to LaTeX escapes from utf8 using mapping tables
in Pod::LaTeX and HTML::Entities. This covers only a subset of the Unicode 
character table (undefined warnings will occur for non-mapped chars).

Mileage will vary when decoding (converting LaTeX to utf8), as LaTeX is in
essence a programming language, and this module does not implement LaTeX.

%prep
%setup -q -n TeX-Encode-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README
%license LICENSE
%{perl_vendorlib}/TeX/
%{_mandir}/man3/*.3pm*

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.010-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.010-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug  6 2024 Miroslav Suchý <msuchy@redhat.com> - 2.010-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.010-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.010-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.010-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.010-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.010-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.010-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.010-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 17 2021 Tom Callaway <spot@fedoraproject.org> - 2.010-1
- update to 2.010

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.009-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.009-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.009-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.009-2
- Perl 5.32 rebuild

* Wed May 27 2020 Tom Callaway <spot@fedoraproject.org> - 2.009-1
- update to 2.009

* Mon Mar 16 2020 Tom Callaway <spot@fedoraproject.org> - 2.008-1
- update to 2.008

* Thu Mar 12 2020 Petr Pisar <ppisar@redhat.com> - 2.007-3
- Build-require blib for the tests

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Tom Callaway <spot@fedoraproject.org> - 2.007-1
- update to 2.007

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.006-1
- 2.006 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.005-2
- Perl 5.30 rebuild

* Tue Feb 12 2019 Petr Pisar <ppisar@redhat.com> - 2.005-1
- 2.005 bump (bug #1669119)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.004-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 04 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.004-1
- 2.004 bump

* Tue Oct 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.003-1
- update to 2.003

* Tue Sep 12 2017 Tom Callaway <spot@fedoraproject.org> - 2.002-1
- update to 2.002

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.001-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Tom Callaway <spot@fedoraproject.org> - 2.001-1
- update to 2.001

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.3-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 15 2015 Tom Callaway <spot@fedoraproject.org> - 1.3-2
- minor specfile cleanups

* Mon Sep 14 2015 Tom Callaway <spot@fedoraproject.org> - 1.3-1
- initial package
