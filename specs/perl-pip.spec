Name:           perl-pip
Summary:        Perl Installation Program, for scripted and distribution installation
Version:        1.19
Release:        40%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/pip-%{version}.tar.gz 
URL:            https://metacpan.org/release/pip
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::Scripts)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Archive::Zip) >= 1.29
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN) >= 1.76
BuildRequires:  perl(CPAN::Inject) >= 0.07
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::pushd) >= 0.32
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Temp) >= 0.14
BuildRequires:  perl(File::Which) >= 1.08
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Zlib)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(PAR::Dist) >= 0.25
BuildRequires:  perl(Params::Util) >= 1.00
BuildRequires:  perl(strict)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(LWP::Online) >= 1.06
BuildRequires:  perl(Test::More) >= 0.42
BuildRequires:  perl(Test::Script) >= 1.02

Requires:       perl(Archive::Zip) >= 1.29
Requires:       perl(CPAN) >= 1.76
Requires:       perl(CPAN::Inject) >= 0.07
Requires:       perl(File::pushd) >= 0.32
Requires:       perl(File::Spec) >= 0.80
Requires:       perl(File::Temp) >= 0.14
Requires:       perl(File::Which) >= 1.08
Requires:       perl(IO::Zlib)
Requires:       perl(LWP::Simple)
Requires:       perl(PAR::Dist) >= 0.25
Requires:       perl(Params::Util) >= 1.00

%{?perl_default_filter}

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CPAN\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(File::Spec\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(File::Temp\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(File::Which\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(File::pushd\\)\s*$
%global __requires_exclude %__requires_exclude|^perl\\(Params::Util\\)\s*$

%description
The pip ("Perl Installation Program") console application is used to
install Perl distributions in a wide variety of formats, both from CPAN and
from external third-party locations, while supporting module dependencies
that go across the boundary from third-party to CPAN.

%prep
%setup -q -n pip-%{version}

# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
mv $RPM_BUILD_ROOT%{_bindir}/pip $RPM_BUILD_ROOT%{_bindir}/perl-pip
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# too long response time
%{?!_with_network_tests: rm t/03_uri.t }
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/perl-pip

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-33
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-30
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-27
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-24
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-21
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-18
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-16
- Perl 5.24 rebuild

* Fri Feb 26 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-15
- Package cleanup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-12
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.19-11
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 Petr Pisar <ppisar@redhat.com> - 1.19-9
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 1.19-5
- Perl 5.16 rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.19-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 02 2010 Marcela Mašláňová <mmaslano@redhat.com> 1.19-1
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (1.19)
- added a new br on perl(Carp) (version 0)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- added a new br on perl(File::Basename) (version 0)
- added a new br on perl(File::Spec) (version 0.80)
- added a new br on perl(File::Temp) (version 0.14)
- added a new br on perl(Getopt::Long) (version 0)
- added a new br on perl(PAR::Dist) (version 0.25)
- added a new req on perl(Carp) (version 0)
- added a new req on perl(File::Basename) (version 0)
- added a new req on perl(File::Spec) (version 0.80)
- added a new req on perl(File::Temp) (version 0.14)
- added a new req on perl(Getopt::Long) (version 0)

* Thu Sep 16 2010 Petr Pisar <ppisar@redhat.com> - 1.18-1
- 1.18 bump
- Remove autodetected perl(Archive::Tar) and perl(URI) Requires

* Wed Aug  4 2010 Marcela Mašláňová <mmaslano@redhat.com> 1.16-3
- rename pip to perl-pip because it conflicts with python-pip 616626

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.16-2
- Mass rebuild with perl-5.12.0

* Tue Jan 12 2010 Marcela Mašláňová <mmaslano@redhat.com> 1.16-1
- fix bugs for review

* Wed Nov 18 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.13-1
- Specfile autogenerated by cpanspec 1.78.
