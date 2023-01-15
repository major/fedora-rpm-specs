Name:           perl-Date-Calc-XS
Version:        6.4
Release:        22%{?dist}
Summary:        XS wrapper and C library plug-in for Date::Calc
License:        LGPLv2+ and ( GPL+ or Artistic )
URL:            https://metacpan.org/release/Date-Calc-XS
Source0:        https://cpan.metacpan.org/modules/by-module/Date/Date-Calc-XS-%{version}.tar.gz
# glibc-common contains the iconv binary
BuildRequires:  gcc
BuildRequires:  glibc-common
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Bit::Vector) >= 7.1
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp::Clan) >= 6.01
BuildRequires:  perl(Config)
BuildRequires:  perl(Date::Calc) >= 6.3
BuildRequires:  perl(Date::Calc::Object)
BuildRequires:  perl(Date::Calendar)
BuildRequires:  perl(Date::Calendar::Profiles)
BuildRequires:  perl(Date::Calendar::Year)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)


%description
Date::Calc::XS is a XS wrapper and C library plug-in for Date::Calc

%prep
%setup -q -n Date-Calc-XS-%{version}
iconv --from=ISO-8859-1 --to=UTF-8 CREDITS.txt >CREDITS.fixed
mv CREDITS.fixed CREDITS.txt

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license license
%{perl_vendorarch}/*
%{_mandir}/man3/*
%doc CHANGES.txt README.txt CREDITS.txt

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 6.4-21
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 6.4-18
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.4-15
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.4-12
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.4-9
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 6.4-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 6.4-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 25 2015 Jitka Plesnikova <jplesnik@redhat.com> - 6.4-1
- 6.4 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 6.3-9
- Perl 5.22 rebuild

* Mon Jan 12 2015 Petr Šabata <contyk@redhat.com> - 6.3-8
- Adapt the test suite for the 2015-2115 era

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 6.3-7
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Sven Nierlein <sven.nierlein@consol.de> 6.3-4
- convert credits to utf8
- updated build requires

* Mon Apr 21 2014 Sven Nierlein <sven.nierlein@consol.de> 6.3-3
- added LGPLv2+ to license
- replaced multiple doc files with a single entry
- updated build requires to match versions from Makefile.PL
- changed source to non-author specific

* Sun Apr 06 2014 Sven Nierlein <sven.nierlein@consol.de> 6.3-2
- added perl build requires
- added Changes and README
- use DESTDIR as install target folder
- removed unnecessary build steps

* Sun Mar 23 2014 Sven Nierlein <sven.nierlein@consol.de> 6.3-1
- Specfile created
