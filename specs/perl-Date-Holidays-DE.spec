# Filter the Perl extension module
%{?perl_default_filter}

%global pkgname Date-Holidays-DE

Summary:        Perl module to determine German holidays
Name:           perl-Date-Holidays-DE
Version:        2.07
Release:        2%{?dist}
License:        MIT
URL:            https://metacpan.org/release/%{pkgname}
Source:         https://cpan.metacpan.org/authors/id/F/FR/FROGGS/%{pkgname}-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(warnings)
BuildArch:      noarch

%description
A perl module that creates a list of German holidays in a given year.
It knows about special holiday regulations for all of Germany's federal
states and also about "semi-holidays" and religious "silent days" that
will be treated as holidays on request. Holidays that occur on weekends
can be excluded from the generated list. The generated list can also be
freely formatted using regular strftime() format definitions.

%prep
%setup -q -n %{pkgname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
chmod -R u+w $RPM_BUILD_ROOT/*

# Don't add dependencies for %%doc
chmod -x example/*.pl

%check
make test

%files
%doc Changes README example
%{_mandir}/man3/*.3pm*
%{perl_vendorlib}/Date/Holidays/

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Apr 30 2025 Robert Scheck <robert@fedoraproject.org> 2.07-1
- Upgrade to 2.07 (#2363057)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 18 2023 Robert Scheck <robert@fedoraproject.org> 2.06-1
- Upgrade to 2.06 (#2169950)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.05-8
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.05-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.05-2
- Perl 5.32 rebuild

* Mon Apr 27 2020 Robert Scheck <robert@fedoraproject.org> 2.05-1
- Upgrade to 2.05 (#1828234)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-1
- 2.03 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.02-2
- Perl 5.30 rebuild

* Fri Mar 08 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.02-1
- 2.02 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 07 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.00-1
- 2.00 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.9-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.9-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.9-1
- 1.9 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.7-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Robert Scheck <robert@fedoraproject.org> 1.7-1
- Upgrade to 1.7 (#1297365)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.6-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.6-3
- Perl 5.20 rebuild

* Sat Jul 19 2014 Robert Scheck <robert@fedoraproject.org> 1.6-2
- Changes to match with Fedora Packaging Guidelines (#847420)

* Sat Aug 11 2012 Robert Scheck <robert@fedoraproject.org> 1.6-1
- Upgrade to 1.6 (#847420)
- Initial spec file for Fedora and Red Hat Enterprise Linux
