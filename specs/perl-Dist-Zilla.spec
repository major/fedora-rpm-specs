Name:           perl-Dist-Zilla
Version:        6.032
Release:        3%{?dist}
Summary:        Distribution builder; installer not included!
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Dist-Zilla-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(App::Cmd::Command::version)
BuildRequires:  perl(App::Cmd::Setup) >= 0.330
BuildRequires:  perl(App::Cmd::Tester) >= 0.306
BuildRequires:  perl(App::Cmd::Tester::CaptureExternal)
# Archive::Tar is a fall-back for missing optional Archive::Tar::Wrapper 0.15
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(autodie)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::INI::Reader)
BuildRequires:  perl(Config::MVP) >= 2.200011
BuildRequires:  perl(Config::MVP::Assembler)
BuildRequires:  perl(Config::MVP::Assembler::WithBundles) >= 2.200010
BuildRequires:  perl(Config::MVP::Reader) >= 2.101540
BuildRequires:  perl(Config::MVP::Reader::Findable::ByExtension)
BuildRequires:  perl(Config::MVP::Reader::Finder)
BuildRequires:  perl(Config::MVP::Reader::INI) >= 2.101461
BuildRequires:  perl(Config::MVP::Section) >= 2.200009
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Converter) >= 2.101550
BuildRequires:  perl(CPAN::Meta::Merge)
BuildRequires:  perl(CPAN::Meta::Prereqs) >= 2.120630
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  perl(CPAN::Meta::Validator) >= 2.101550
BuildRequires:  perl(CPAN::Uploader) >= 0.103004
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Section) >= 0.200002
BuildRequires:  perl(DateTime) >= 0.44
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(experimental)
BuildRequires:  perl(ExtUtils::Manifest) >= 1.66
BuildRequires:  perl(File::Copy::Recursive) >= 0.41
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Log::Dispatchouli) >= 1.102220
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 0.92
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::LazyRequire)
BuildRequires:  perl(MooseX::Role::Parameterized) >= 1.01
BuildRequires:  perl(MooseX::SetOnce)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Perl)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Class) >= 0.22
BuildRequires:  perl(Path::Tiny) >= 0.052
BuildRequires:  perl(Perl::PrereqScanner) >= 1.016
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(PPI)
BuildRequires:  perl(PPI::Document) >= 1.222
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Software::License) >= 0.104001
BuildRequires:  perl(Software::LicenseUtils)
BuildRequires:  perl(String::Formatter) >= 0.100680
BuildRequires:  perl(String::RewritePrefix) >= 0.006
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::ForMethods)
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Term::Encoding)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Term::UI)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Text::Glob) >= 0.08
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(YAML::Tiny)
# Optional run-time:
# Archive::Tar::Wrapper 0.15
# Tests:
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(Software::License::None)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::File::ShareDir)
BuildRequires:  perl(Test::More) >= 0.96
# Archive::Tar is a fall-back for missing optional Archive::Tar::Wrapper 0.15
Requires:       perl(Archive::Tar)
#Requires:       perl(autobox) >= 2.53
Requires:       perl(Config::INI::Reader)
Requires:       perl(Config::MVP) >= 2.200011
Requires:       perl(Config::MVP::Assembler)
Requires:       perl(Config::MVP::Assembler::WithBundles) >= 2.200010
Requires:       perl(Config::MVP::Reader::Findable::ByExtension)
Requires:       perl(Config::MVP::Reader::Finder)
Requires:       perl(Config::MVP::Reader::INI) >= 2
Requires:       perl(CPAN::Meta::Converter) >= 2.101550
Requires:       perl(CPAN::Meta::Validator) >= 2.101550
Requires:       perl(CPAN::Uploader) >= 0.103004
Requires:       perl(DateTime)
Requires:       perl(ExtUtils::Manifest) >= 1.54
Requires:       perl(File::Path)
Requires:       perl(File::ShareDir::Install) >= 0.06
Requires:       perl(Hash::Merge::Simple)
Requires:       perl(Module::CoreList)
Requires:       perl(Path::Class) >= 0.22
Requires:       perl(Pod::Simple)
Requires:       perl(PPI::Document) >= 1.222
Requires:       perl(Software::LicenseUtils) >= 0.104001
Requires:       perl(Term::ANSIColor) >= 5.00
Requires:       perl(Term::Encoding)
Requires:       perl(Term::ReadKey)
Requires:       perl(Term::ReadLine)
Requires:       perl(Term::UI)

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((App::Cmd::Setup|CPAN::Meta::Requirements|Moose|Path::Class|String::RewritePrefix)\\)$
# Remove autogenerated nonsense
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}\\{

%description
Dist::Zilla builds distributions of code to be uploaded to the CPAN. In
this respect, it is like ExtUtils::MakeMaker, Module::Build, or
Module::Install. Unlike those tools, however, it is not also a system for
installing code that has been downloaded from the CPAN. Since it's only run
by authors, and is meant to be run on a repository checkout rather than on
published, released code, it can do much more than those tools, and is free
to make much more ludicrous demands in terms of prerequisites.

%prep
%setup -q -n Dist-Zilla-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# install bash_completion script
install -D -m 0644 misc/dzil-bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/dzil

%check
make test

%files
%license LICENSE
%doc Changes README todo
%{perl_vendorlib}/*
%{_bindir}/dzil
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_sysconfdir}/bash_completion.d

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.032-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.032-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 28 2024 Michal Josef Špaček <mspacek@redhat.com> - 6.032-1
- 6.032 bump

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.031-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.031-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 21 2023 Michal Josef Špaček <mspacek@redhat.com> - 6.031-1
- 6.031 bump

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.030-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Michal Josef Špaček <mspacek@redhat.com> - 6.030-1
- 6.030 bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.029-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Michal Josef Špaček <mspacek@redhat.com> - 6.029-1
- 6.029 bump

* Thu Sep 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 6.025-1
- 6.025 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.024-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 6.024-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.024-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Jitka Plesnikova <jplesnik@redhat.com> - 6.024-1
- 6.024 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.023-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Jitka Plesnikova <jplesnik@redhat.com> - 6.023-1
- 6.023 bump

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 6.017-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 03 2020 Petr Šabata <contyk@redhat.com> - 6.017-1
- 6.017 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.015-2
- Perl 5.32 rebuild

* Mon Jun 15 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.015-1
- 6.015 bump

* Tue Mar 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 6.014-1
- 6.014 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.012-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.012-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 6.012-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.012-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 6.012-2
- Perl 5.28 rebuild

* Sun Apr 22 2018 Petr Šabata <contyk@redhat.com> - 6.012-1
- 6.012 bump

* Mon Feb 12 2018 Petr Šabata <contyk@redhat.com> - 6.011-1
- 6.011 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Petr Šabata <contyk@redhat.com> - 6.010-1
- 6.010 bump

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 6.009-2
- Perl 5.26 rebuild

* Tue Apr 04 2017 Petr Šabata <contyk@redhat.com> - 6.009-1
- 6.009 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 10 2016 Petr Šabata <contyk@redhat.com> - 6.008-1
- 6.008 bump
- Fix build failures with the latest Moose

* Fri Aug 12 2016 Petr Šabata <contyk@redhat.com> - 6.007-1
- 6.007 bump

* Tue Jun 28 2016 Petr Šabata <contyk@redhat.com> - 6.005-1
- 6.005 bump
- This release introduces certain incompatible changes; plugins
  relying on the old internal path handling might break, as well as
  applications using the long obsoleted plugins (Prereq, AutoPrereq,
  BumpVersion)

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 5.047-2
- Perl 5.24 rebuild

* Mon Apr 25 2016 Petr Šabata <contyk@redhat.com> - 5.047-1
- 5.047 bump

* Fri Apr 22 2016 Petr Šabata <contyk@redhat.com> - 5.045-1
- 5.045 bump

* Mon Apr 11 2016 Petr Šabata <contyk@redhat.com> - 5.044-1
- 5.044 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.043-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Petr Šabata <contyk@redhat.com> - 5.043-1
- 5.043 bump

* Mon Nov 30 2015 Petr Šabata <contyk@redhat.com> - 5.042-1
- 5.042 bump

* Thu Oct 29 2015 Jitka Plesnikova <jplesnik@redhat.com> - 5.041-1
- 5.041 bump

* Wed Oct 14 2015 Jitka Plesnikova <jplesnik@redhat.com> - 5.040-1
- 5.040 bump

* Tue Aug 11 2015 Petr Šabata <contyk@redhat.com> - 5.039-1
- 5.039 bump

* Mon Aug 10 2015 Petr Šabata <contyk@redhat.com> - 5.038-1
- 5.038 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.037-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 5.037-2
- Perl 5.22 rebuild

* Fri Jun 05 2015 Petr Šabata <contyk@redhat.com> - 5.037-1
- 5.037 bump

* Mon May 04 2015 Petr Šabata <contyk@redhat.com> - 5.036-1
- 5.036 bump

* Thu Apr 23 2015 Petr Šabata <contyk@redhat.com> - 5.035-1
- 5.035 bump
- is_trial is now read-only

* Mon Mar 23 2015 Petr Šabata <contyk@redhat.com> - 5.034-1
- 5.034 bump

* Fri Mar 20 2015 Petr Šabata <contyk@redhat.com> - 5.033-1
- 5.033 bump

* Fri Jan 09 2015 Petr Šabata <contyk@redhat.com> - 5.031-1
- 5.031 bump, Win32 test suite fixes

* Thu Jan 08 2015 Petr Šabata <contyk@redhat.com> - 5.030-1
- 5.030 bump

* Thu Dec 18 2014 Petr Šabata <contyk@redhat.com> - 5.029-1
- 5.029 bump

* Wed Dec 10 2014 Petr Šabata <contyk@redhat.com> - 5.027-2
- Filter out bogus provides

* Wed Dec 10 2014 Petr Šabata <contyk@redhat.com> - 5.027-1
- 5.027 bump

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 5.015-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 Petr Pisar <ppisar@redhat.com> - 5.015-1
- 5.015 bump

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 4.300023-4
- Perl 5.18 rebuild
- Specify all dependencies

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.300023-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.300023-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 09 2012 Iain Arnell <iarnell@gmail.com> 4.300023-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.300018-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Petr Pisar <ppisar@redhat.com> - 4.300018-2
- Perl 5.16 rebuild

* Sat Jun 09 2012 Iain Arnell <iarnell@gmail.com> 4.300018-1
- update to latest upstream version

* Sat May 12 2012 Iain Arnell <iarnell@gmail.com> 4.300016-1
- update to latest upstream version

* Tue Apr 17 2012 Iain Arnell <iarnell@gmail.com> 4.300014-1
- update to latest upstream version

* Mon Mar 19 2012 Iain Arnell <iarnell@gmail.com> 4.300010-1
- update to latest upstream version

* Wed Feb 22 2012 Iain Arnell <iarnell@gmail.com> 4.300009-1
- update to latest upstream version

* Sun Feb 19 2012 Iain Arnell <iarnell@gmail.com> 4.300008-1
- update to latest upstream version

* Sat Feb 04 2012 Iain Arnell <iarnell@gmail.com> 4.300007-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.300006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jan  3 2012 Marcela Mašláňová <mmaslano@redhat.com> 4.30006-1
- update to the latest upstream version
- change BR and R according to new release

* Fri Sep 23 2011 Iain Arnell <iarnell@gmail.com> 4.300002-1
- update to latest upstream version

* Sun Aug 28 2011 Iain Arnell <iarnell@gmail.com> 4.300000-1
- update to latest upstream version

* Thu Aug 18 2011 Iain Arnell <iarnell@gmail.com> 4.200017-1
- update to latest upstream version

* Tue Jul 26 2011 Iain Arnell <iarnell@gmail.com> 4.200012-1
- update to latest upstream

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 4.200008-2
- Perl mass rebuild

* Sat Jun 25 2011 Iain Arnell <iarnell@gmail.com> 4.200008-1
- update to latest upstream version

* Sun Jun 05 2011 Iain Arnell <iarnell@gmail.com> 4.200007-1
- update to latest upstream version

* Sat Apr 30 2011 Iain Arnell <iarnell@gmail.com> 4.200006-1
- update to latest upstream version

* Fri Apr 08 2011 Iain Arnell <iarnell@gmail.com> 4.200004-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.200001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 21 2011 Iain Arnell <iarnell@gmail.com> 4.200001-1
- update to latest upstream version

* Tue Dec 14 2010 Iain Arnell <iarnell@gmail.com> 4.200000-1
- update to latest upstream version
- install bash_completion script

* Sat Nov 20 2010 Iain Arnell <iarnell@gmail.com> 4.102344-1
- update to latest upstream version

* Sun Oct 03 2010 Iain Arnell <iarnell@gmail.com> 4.102341-1
- update to latest upstream
- clean up spec for modern rpmbuild
- requires Moose::Autobox >= 0.10

* Tue Aug 24 2010 Iain Arnell <iarnell@gmail.com> 4.102340-1
- update to latest upstream

* Sun Jul 11 2010 Iain Arnell <iarnell@gmail.com> 4.101900-1
- update to latest upstream

* Sat Jul 03 2010 Iain Arnell <iarnell@gmail.com> 4.101831-1
- update to latest upstream
- BR perl(Term::ReadKey), perl(Term::ReadLine), and perl(Term::UI)
- dzil has a man page now

* Wed Jun 23 2010 Iain Arnell <iarnell@gmail.com> 4.101612-1
- update to latest upstream
- update BRs

* Fri May 14 2010 Iain Arnell - 2.101310-2
- bump for rebuild in dist-f14

* Thu May 13 2010 Iain Arnell <iarnell@gmail.com> 2.101310-1
- update to latest upstream version

* Wed Apr 21 2010 Iain Arnell <iarnell@gmail.com> 2.101040-1
- update to latest upstream

* Wed Apr 07 2010 Iain Arnell <iarnell@gmail.com> 2.100960-1
- Specfile autogenerated by cpanspec 1.78.
- use perl_default_filter and DESTDIR
