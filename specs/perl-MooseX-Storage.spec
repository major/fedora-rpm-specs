Name:           perl-MooseX-Storage
Summary:        A serialization framework for Moose classes
Version:        0.53
Release:        16%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Storage-%{version}.tar.gz
URL:            https://metacpan.org/release/MooseX-Storage
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.7501
BuildRequires:  perl(IO::AtomicFile)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 0.99
BuildRequires:  perl(Moose::Meta::Attribute)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::RewritePrefix)
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML::Any)
BuildRequires:  sed
# test BR
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Deep::JSON)
BuildRequires:  perl(Test::Deep::Type)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Requires) >= 0.05
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(utf8)
BuildRequires:  perl(YAML::Syck)
BuildRequires:  perl(YAML::XS)
#BuildRequires:  perl(MooseX::Storage::Format::JSONpm)

%{?perl_default_filter}

%description
MooseX::Storage is a serialization framework for Moose, it provides a
very flexible and highly pluggable way to serialize Moose classes to a
number of different formats and styles. This is still an early release
of this module, so use with caution. It's outward facing serialization
API should be considered stable, but I still reserve the right to make
tweaks if I need too. Anything beyond the basic pack/unpack, freeze/thaw
and load/store should not be relied on. There are 3 levels to the
serialization, each of which builds upon the other and each of which
can be customized to the specific needs of your class.


%prep
%setup -q -n MooseX-Storage-%{version}

# silence rpmlint warnings
sed -i '1s,#!.*perl,#!/usr/bin/perl,' t/*.t
chmod 0644 t/*.t

%build
/usr/bin/perl Makefile.PL --skipdeps INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README t/
%license LICENSE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.53-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-8
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-2
- Perl 5.32 rebuild

* Sun Apr 19 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.53-1
- Update to 0.53
- Replace calls to %%{__perl} with /usr/bin/perl
- Replace calls to make pure_install with %%{make_install}
- Replace calls to make with %%{make_build}

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.52-3
- Perl 5.26 rebuild
- Specify all dependencies

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 24 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.52-1
- Update to 0.52

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.50-1
- Update to 0.50
- Minor cleanup in the spec file

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.49-2
- Perl 5.22 rebuild

* Sun Mar 29 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.49-1
- Update to 0.49

* Tue Nov 11 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.48-1
- Update to 0.48
- Use %%license tag
- Tighten files list

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.32-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.32-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Iain Arnell <iarnell@gmail.com> 0.32-1
- update to latest upstream version
- drop old tests sub-package obsoletes/provides
- clean up spec for modern rpmbuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Petr Pisar <ppisar@redhat.com> - 0.31-2
- Perl 5.16 rebuild

* Wed Feb 29 2012 Iain Arnell <iarnell@gmail.com> 0.31-1
- update to latest upstream version

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.30-3
- drop tests subpackage; move tests to main package documentation

* Tue Jan 17 2012 Iain Arnell <iarnell@gmail.com> - 0.30-2
- rebuilt again for F17 mass rebuild

* Sat Jan 14 2012 Iain Arnell <iarnell@gmail.com> 0.30-1
- update to latest upstream version
- additional BRs for better test coverage
- remove explicit requires

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.29-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.29-1
- update by Fedora::App::MaintainerTools 0.006
- PERL_INSTALL_ROOT => DESTDIR
- updating to latest GA CPAN version (0.29)
- altered br on perl(Moose) (0.39 => 0.99)
- added a new br on perl(String::RewritePrefix) (version 0)
- altered br on perl(Test::More) (0.42 => 0.88)
- added a new br on perl(Test::Requires) (version 0.05)
- dropped old BR on perl(Best)
- dropped old BR on perl(Digest)
- dropped old BR on perl(Encode)
- dropped old BR on perl(File::NFSLock)
- dropped old BR on perl(File::Spec::Functions)
- dropped old BR on perl(File::Temp)
- dropped old BR on perl(Moose::Util::TypeConstraints)
- dropped old BR on perl(Scalar::Util)
- dropped old BR on perl(Storable)
- dropped old BR on perl(Test::Pod)
- dropped old BR on perl(Test::Pod::Coverage)
- dropped old BR on perl(Test::TempDir)
- dropped old BR on perl(Test::YAML::Valid)
- dropped old BR on perl(YAML::Syck)
- altered req on perl(Moose) (0.39 => 0.99)
- added a new req on perl(String::RewritePrefix) (version 0)

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.21-4
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.21-3
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.21-2
- rebuild against perl 5.10.1

* Tue Aug 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.21-1
- auto-update to 0.21 (by cpan-spec-update 0.01)
- added a new req on perl(Moose) (version 0.39)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 04 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.18-2
- add br on CPAN until bundled M::I is updated

* Thu Jun 04 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.18-1
- auto-update to 0.18 (by cpan-spec-update 0.01)

* Sat Apr 18 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.17-2
- update grammatically poor summary

* Sun Apr 12 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.17-1
- update to 0.17

* Wed Apr 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.15-1
- update for submission

* Mon Mar 09 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.15-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)
