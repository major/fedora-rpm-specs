Name:           perl-Catalyst-Plugin-Session
Summary:        Catalyst generic session plugin
Version:        0.43
Release:        10%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Catalyst-Plugin-Session-%{version}.tar.gz 
URL:            https://metacpan.org/release/Catalyst-Plugin-Session
BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Runtime) >= 5.71001
BuildRequires:  perl(Catalyst::Exception)
BuildRequires:  perl(Class::MOP)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(inc::Module::Install) >= 0.87
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Moose) >= 0.76
BuildRequires:  perl(MooseX::Emulate::Class::Accessor::Fast) >= 0.00801
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(namespace::clean) >= 0.10
BuildRequires:  perl(Object::Signature)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Tie::RefHash) >= 1.34
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  sed
%if !0%{?perl_bootstrap}
# these cause circular builddeps
BuildRequires:  perl(Catalyst::Plugin::Authentication)
BuildRequires:  perl(Catalyst::Plugin::Session::State::Cookie) >= 0.03
BuildRequires:  perl(Catalyst::Test)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Test::WWW::Mechanize::Catalyst) >= 0.51
BuildRequires:  perl(Test::WWW::Mechanize::PSGI)
%endif

Requires:       perl(Catalyst::Runtime) >= 5.71001
Requires:       perl(MooseX::Emulate::Class::Accessor::Fast) >= 0.00801

%{?perl_default_filter}

%description
This plugin is the base of two related parts of functionality
required for session management in web applications.

The first part, the State, is getting the browser to repeat back a
session key, so that the web application can identify the client and
logically string several requests together into a session.

The second part, the Store, deals with the actual storage of information
about the client. This data is stored so that the it may be revived for
every request made by the same client.

This plugin links the two pieces together.

%prep
%setup -q -n Catalyst-Plugin-Session-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 0.43-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 06 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.43-2
- Perl 5.36 re-rebuild of bootstrapped packages

* Sun Jun 05 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 0.43-1
- Update to 0.43
- Use %%{make_build} and %%{make_install} where appropriate
- Replace %%{__perl} with /usr/bin/perl

* Fri Jun 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-16
- Perl 5.36 re-rebuild of bootstrapped packages

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-15
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 24 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-12
- Perl 5.34 re-rebuild of bootstrapped packages

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-11
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-8
- Perl 5.32 re-rebuild of bootstrapped packages

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-7
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-4
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.41-1
- Update to 0.41

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-15
- Perl 5.28 re-rebuild of bootstrapped packages

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-14
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-11
- Perl 5.26 re-rebuild of bootstrapped packages

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-10
- Perl 5.26 rebuild

* Wed May 24 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-9
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-7
- Perl 5.24 re-rebuild of bootstrapped packages

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.40-2
- Perl 5.22 rebuild

* Sun Feb 01 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.40-1
- Update to 0.40

* Sat Nov 22 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.39-1
- Update to 0.39

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-7
- Perl 5.20 re-rebuild of bootstrapped packages

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-6
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-4
- Perl 5.18 re-rebuild of bootstrapped packages

* Tue Aug 06 2013 Petr Pisar <ppisar@redhat.com> - 0.37-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 01 2013 Iain Arnell <iarnell@gmail.com> 0.37-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 21 2012 Iain Arnell <iarnell@gmail.com> 0.36-1
- update to latest upstream version
- drop obsoletes/provides for old test sub-package

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 0.35-4
- Perl 5.16 re-rebuild of bootstrapped packages

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 0.35-3
- Perl 5.16 rebuild

* Sat May 19 2012 Iain Arnell <iarnell@gmail.com> 0.35-2
- add notes to spec regarding Plack::Middleware::ForceEnv

* Sun Apr 29 2012 Iain Arnell <iarnell@gmail.com> 0.35-1
- update to latest upstream version

* Fri Mar 30 2012 Iain Arnell <iarnell@gmail.com> 0.33-1
- update to latest upstream version

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.32-2
- drop tests subpackage; move tests to main package documentation

* Fri Jan 20 2012 Iain Arnell <iarnell@gmail.com> 0.32-1
- update to latest upstream version
- remove unnecessary explicit dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.31-4
- Perl mass rebuild

* Fri Jul 15 2011 Iain Arnell <iarnell@gmail.com> 0.31-3
- restore circular deps and wrap with perl_bootstrap macro

* Wed Jul 13 2011 Iain Arnell <iarnell@gmail.com> 0.31-2
- drop additional BRs again - they cause circular build deps

* Sun Mar 13 2011 Iain Arnell <iarnell@gmail.com> 0.31-1
- update to latest upstream version
- clean up spec for modern rpmbuild
- BR Catalyst::Plugin::Session::State::Cookie and
  Test::WWW::Mechanize::Catalyst for improved test coverage

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.29-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.29-4
- Mass rebuild with perl-5.12.0

* Sat Feb 27 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.29-3
- update by Fedora::App::MaintainerTools 0.004
- PERL_INSTALL_ROOT => DESTDIR
- dropped old BR on perl(Catalyst)
- dropped old BR on perl(Test::Pod::Coverage)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.29-2
- rebuild against perl 5.10.1

* Sun Dec 06 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.29-1
- auto-update to 0.29 (by cpan-spec-update 0.01)

* Sat Oct 10 2009 Iain Arnell <iarnell@gmail.com> 0.27-1
- update to 0.27
- remove buildreq on perl(Text::MockObject)

* Sat Aug 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.25-1
- switch to new filtering system (perl_default_filter)
- auto-update to 0.25 (by cpan-spec-update 0.01)
- added a new req on perl(Catalyst::Runtime) (version 5.71001)
- added a new req on perl(Digest) (version 0)
- added a new req on perl(File::Spec) (version 0)
- added a new req on perl(File::Temp) (version 0)
- added a new req on perl(MRO::Compat) (version 0)
- added a new req on perl(Moose) (version 0.76)
- altered req on perl(MooseX::Emulate::Class::Accessor::Fast) (0 => 0.00801)
- added a new req on perl(Object::Signature) (version 0)
- added a new req on perl(Tie::RefHash) (version 1.34)
- added a new req on perl(namespace::clean) (version 0.10)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 26 2009 Iain Arnell <iarnell@gmail.com> 0.22-2
- add missing requires perl(MooseX::Emulate::Class::Accessor::Fast)

* Mon May 25 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.22-1
- auto-update to 0.22 (by cpan-spec-update 0.01)
- added a new br on perl(File::Temp) (version 0)
- added a new br on perl(File::Spec) (version 0)
- added a new br on perl(namespace::clean) (version 0.10)
- added a new br on perl(Moose) (version 0.76)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- added a new br on perl(Catalyst::Runtime) (version 5.71001)
- added a new br on perl(MooseX::Emulate::Class::Accessor::Fast) (version 0.00801)

* Fri Feb 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.20-1
- update to 0.20

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May 30 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.19-2
- bump

* Tue Mar 18 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.19-1
- Specfile autogenerated by cpanspec 1.74.
