# The test fuse_ui.t doesn't work in mock, they can be run on local machine
%bcond_with test_fuse

Name:           perl-Config-Model
Version:        2.155
Release:        2%{?dist}
Summary:        Framework to create configuration validation tools and editors
License:        LGPL-2.1-or-later

URL:            https://metacpan.org/release/Config-Model
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDUMONT/Config-Model-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(boolean)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Assert::More)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::Model::Tester) >= 4.002
BuildRequires:  perl(Config::Model::Tester::Setup)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::testlib)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Fuse)
BuildRequires:  perl(Hash::Merge) >= 0.12
BuildRequires:  perl(IO::File)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Log4perl) >= 1.11
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Mouse::Util)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(MouseX::NativeTraits)
BuildRequires:  perl(MouseX::StrictConstructor)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Parse::RecDescent) >= v1.90.0
BuildRequires:  perl(Path::Tiny) >= 0.070
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Pod::Simple) >= 3.23
BuildRequires:  perl(Pod::Text)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Term::ReadLine::Gnu)
# Term::ReadLine::Perl - not used
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::File::Contents)
BuildRequires:  perl(Test::Log::Log4perl)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Synopsis::Expectation)
BuildRequires:  perl(Test::Warn) >= 0.11
BuildRequires:  perl(Text::Levenshtein::Damerau)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XXX)
BuildRequires:  perl(YAML::Tiny)
%if %{with test_fuse}
BuildRequires:  fuse
BuildRequires:  kmod
%endif
Requires:       perl(MouseX::NativeTraits)
Requires:       perl(Text::Levenshtein::Damerau)

# RPM 4.8 filters
# Fedora is not a Debian system
%filter_from_requires /perl(AptPkg::Config)/d; /perl(AptPkg::System)/d; /perl(AptPkg::Version)/d
%{?perl_default_filter}
# RPM 4.9 filters
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(AptPkg::.*\\)
%global __requires_exclude %__requires_exclude|perl\\(Log::Log4perl\\)\s*$


%description
Using Config::Model, a typical configuration validation tool will be made
of 3 parts :
1. The user interface
2. The validation engine which is in charge of validating all the 
configuration information provided by the user.
3. The storage facility that store the configuration information

%prep
%setup -q -n Config-Model-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset TEST_AUTHOR
%if %{with test_fuse}
modprobe fuse
%endif
./Build test

%files
%license LICENSE
%doc Changes MODELS README.md TODO CONTRIBUTING.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.155-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.155-1
- 2.155 bump

* Mon Sep 16 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.154-1
- 2.154 bump (rhbz#2295344)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.153-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.153-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.153-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Jitka Plesnikova <jplesnik@redhat.com> - 2.153-1
- 2.153 bump (rhbz#2224540)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.152-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.152-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.152-1
- 2.152 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.150-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.150-2
- Perl 5.36 rebuild

* Mon May 09 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.150-1
- 2.150 bump

* Thu Apr 28 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.149-1
- 2.149 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.148-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.148-1
- 2.148 bump

* Thu Nov 11 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.145-1
- 2.145 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.142-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.142-2
- Perl 5.34 rebuild

* Sat Apr 10 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 2.142-1
- Update to 2.142

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.141-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.141-1
- Update to 2.141

* Sun Aug 02 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.140-1
- Update to 2.140

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.138-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.138-4
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.138-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 29 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 2.138-2
- Bump to build in koji

* Sun Dec 29 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 2.138-1
- Update to 2.138

* Wed Dec 04 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.137-1
- 2.137 bump

* Sun Aug 04 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 2.136-1
- Update to 2.136
- Replace calls to %%{__perl} to /usr/bin/perl

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.135-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.135-1
- 2.135 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.134-2
- Perl 5.30 rebuild

* Thu May 09 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.134-1
- 2.134 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.133-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.133-1
- 2.133 bump

* Sun Dec 23 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.132-1
- Update to 2.132

* Tue Dec 18 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.131-1
- 2.131 bump

* Tue Dec 11 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.130-1
- 2.130 bump

* Thu Dec 06 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.129-1
- 2.129 bump

* Thu Nov 22 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.128-1
- 2.128 bump

* Thu Oct 04 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.127-1
- 2.127 bump

* Tue Aug 21 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.126-1
- 2.126 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.125-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.125-2
- Perl 5.28 rebuild

* Mon Jun 25 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.125-1
- 2.125 bump

* Tue Jun 12 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.124-1
- 2.124 bump

* Thu May 10 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.123-1
- Update to 2.123

* Tue Apr 17 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.121-1
- Update to 2.121

* Fri Apr 13 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.120-1
- Update to 2.120

* Tue Feb 06 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.117-1
- Update to 2.117

* Sun Dec 17 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 2.116-1
- Update to 2.116

* Wed Nov 15 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.114-1
- Update to 2.114

* Fri Oct 13 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.113-1
- Update to 2.113

* Sun Oct 01 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 2.112-1
- Update to 2.112
- Drop Group tag

* Sun Sep 24 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 2.111-1
- Update to 2.111

* Sun Sep 03 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 2.108-1
- Update to 2.108

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.106-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.106-1
- 2.106 bump

* Tue Jun 13 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.105-1
- 2.105 bump

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.103-2
- Perl 5.26 rebuild

* Thu Jun 01 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.103-1
- 2.103 bump

* Mon May 22 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 2.102-1
- Update to 2.102

* Tue May 02 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.101-1
- 2.101 bump

* Tue Mar 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.100-1
- 2.100 bump

* Mon Mar 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.099-1
- 2.099 bump

* Fri Mar 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.098-1
- 2.098 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.097-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.097-1
- 2.097 bump

* Tue Nov 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.094-1
- 2.094 bump

* Tue Sep 27 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.092-1
- 2.092 bump

* Tue Aug 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.088-1
- 2.088 bump

* Tue Jun 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.086-1
- 2.086 bump

* Mon May 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.083-1
- 2.083 bump

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.082-2
- Perl 5.24 rebuild

* Mon Apr 04 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.082-1
- 2.082 bump

* Tue Mar 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.081-1
- 2.081 bump

* Tue Feb 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.079-1
- 2.079 bump

* Wed Feb 10 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.078-1
- 2.078 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.076-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.076-1
- 2.076 bump

* Thu Nov 12 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.074-1
- 2.074 bump

* Wed Jul 29 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.073-1
* 2.073 bump

* Wed Jun 24 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.071-2
- Added run-requires MouseX::NativeTraits

* Mon Jun 22 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.071-1
- 2.071 bump
- Updated the list of build-requires

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.235-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.235-14
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.235-13
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.235-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 1.235-11
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.235-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.235-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.235-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Petr Pisar <ppisar@redhat.com> - 1.235-7
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.235-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Petr Sabata <contyk@redhat.com> - 1.235-5
- RPM 4.9 dependency filtering added

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.235-4
- Perl mass rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.235-3
- Perl mass rebuild

* Thu Apr 07 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.235-2
- Remove BuildRoot and clean macro (no longer used)
- Add perl default filter
- Filter out uneeded requirements
- Update and apply patch for YAML::Any requirement

* Tue Mar 08 2011 David Hannequin <david.hannequin@gmail.com> 1.235-1
- Update from upstream.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.205-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.205-5
- 661697 rebuild for fixing problems with vendorach/lib

* Tue Aug 17 2010 David Hannequin <david.hannequin@gmail.com> 1.205-4
- Add forgotten apply patch YAML::Any version (thank for patch).

* Tue Aug 10 2010 Marcela Mašláňová <mmaslano@redhat.com> 1.205-3
- inside module is needed YAML::Any > 0.303. 0.70 < 0.303 for rpm

* Mon Jul 26 2010 David Hannequin david.hannequin@gmail.com 1.205-2
- Fix tag.

* Mon Jul 26 2010 David Hannequin david.hannequin@gmail.com 1.205-1
- Updated to a new upstream version.

* Mon Jun 28 2010 David Hannequin david.hannequin@gmail.com 1.001-1
- Updated to a new upstream version.

* Sun Jun 20 2010 David Hannequin david.hannequin@gmail.com 0.644-4
- Fix wrong syntax.

* Sun Jun 20 2010 David Hannequin david.hannequin@gmail.com 0.644-2
- Add build requires.

* Mon Jun 14 2010 David Hannequin david.hannequin@gmail.com 0.644-1
- Updated to a new upstream version.

* Sun Aug 09 2009 David Hannequin david.hannequin@gmail.com 0.638-4
- Modify license.

* Sat Aug 08 2009 David Hannequin david.hannequin@gmail.com 0.638-3
- Add missing build require.

* Sun Aug 02 2009 David Hannequin david.hannequin@gmail.com 0.638-2
- Fix wrong path.

* Fri Jul 31 2009 David Hannequin <david.hannequin@gmail.com> 0.638-1
- First release.

