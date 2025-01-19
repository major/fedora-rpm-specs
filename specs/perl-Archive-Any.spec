Name:		perl-Archive-Any
Version:	0.0946
Release:	18%{?dist}
Summary:	Single interface to deal with file archives
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Archive-Any
Source0:	https://cpan.metacpan.org/modules/by-module/Archive/Archive-Any-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:	perl(Archive::Tar) >= 0.22
BuildRequires:	perl(Archive::Zip) >= 1.07
BuildRequires:	perl(base)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::MMagic) >= 1.27
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(MIME::Types) >= 1.16
BuildRequires:	perl(Module::Find) >= 0.05
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More) >= 0.4
BuildRequires:	perl(Test::Warn)
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
# Runtime

%description
This module is a single interface for manipulating different archive
formats. Tarballs, zip files, etc.

%prep
%setup -q -n Archive-Any-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTORS README.md
%{perl_vendorlib}/Archive/
%{_mandir}/man3/Archive::Any.3*
%{_mandir}/man3/Archive::Any::Plugin.3*
%{_mandir}/man3/Archive::Any::Plugin::Tar.3*
%{_mandir}/man3/Archive::Any::Plugin::Zip.3*
%{_mandir}/man3/Archive::Any::Tar.3*
%{_mandir}/man3/Archive::Any::Zip.3*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0946-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0946-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0946-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0946-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0946-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0946-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0946-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.0946-11
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0946-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0946-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.0946-8
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0946-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0946-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.0946-5
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0946-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0946-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.0946-2
- Perl 5.30 rebuild

* Sat Apr  6 2019 Paul Howarth <paul@city-fan.org> - 0.0946-1
- Update to 0.0946
  - Added copyright holder/year meta to dist.ini (GH#6)
  - Auto generate META.yml using the plugin [MetaYAML] (GH#8)
- Switch to ExtUtils::MakeMaker flow
- Drop legacy spec file elements
  - Drop BuildRoot: and Group: tags
  - Drop explicit buildroot cleaning in %%install section
  - Drop explicit %%clean section
- Upstream renamed README as README.md
- Stop shipping test files

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0945-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0945-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.0945-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0945-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0945-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.0945-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0945-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.0945-2
- Perl 5.24 rebuild

* Tue May  3 2016 Paul Howarth <paul@city-fan.org> - 0.0945-1
- Update to 0.0945
  - Use 'base' rather than @ISA in Zip.pm

* Sat Apr  2 2016 Paul Howarth <paul@city-fan.org> - 0.0944-1
- Update to 0.0944
  - Use 'base' rather than @ISA
  - Use warnings in more modules

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0942-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0942-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.0942-2
- Perl 5.22 rebuild

* Thu Jan 29 2015 Paul Howarth <paul@city-fan.org> - 0.0942-1
- Update to 0.0942
  - Replace contents of archives in test folder with random noise in order to
    avoid any licensing issues
- Use %%license where possible

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.0941-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0941-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Nov  7 2013 Paul Howarth <paul@city-fan.org> - 0.0941-1
- Update to 0.0941
  - Fixes version number in lib/Archive/Any.pm
  - Previous release had broken permissions

* Fri Oct 18 2013 Paul Howarth <paul@city-fan.org> - 0.0940-1
- Update to 0.0940
  - Adds x-bzip2 (CPAN RT#67738)
  - Migrated to Dist::Zilla
- Package new CONTRIBUTORS and LICENSE files
- This release by OALDERS -> update source URL
- Add patch to fix module version number
- Drop now-redundant build requirements
- Drop %%defattr, redundant since rpm 4.4
- Don't need to remove empty directories from the buildroot

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0932-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.0932-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0932-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0932-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.0932-10
- Perl 5.16 rebuild

* Tue Jan 17 2012 Paul Howarth <paul@city-fan.org> - 0.0932-9
- Spec clean-up:
  - Drop redundant buildreq perl(Test::Perl::Critic)
  - Make %%files list more explicit
  - Group buildreqs by build/module/test
  - Don't use macros for commands
  - Use tabs

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0932-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.0932-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0932-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.0932-5
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.0932-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.0932-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0932-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 07 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.0932-1
- auto-update to 0.0932 (by cpan-spec-update 0.01)
- altered br on perl(Test::More) (0 => 0.4)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.093-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 08 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.093-3
- rebuild for new perl

* Wed May 09 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.093-2
- bump

* Sat May 05 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.093-1
- Specfile autogenerated by cpanspec 1.71.
