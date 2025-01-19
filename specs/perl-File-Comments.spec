Summary:	Recognizes file formats and extracts format-specific comments
Name:		perl-File-Comments
Version:	0.08
Release:	42%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
Url:		https://metacpan.org/release/File-Comments
Source0:	https://cpan.metacpan.org/modules/by-module/File/File-Comments-%{version}.tar.gz
Patch0:		File-Comments-0.08-provides.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(HTML::TokeParser) >= 2.28
BuildRequires:	perl(HTML::TreeBuilder)
BuildRequires:	perl(Log::Log4perl) >= 0.50
BuildRequires:	perl(Module::Pluggable) >= 2.4
BuildRequires:	perl(Pod::Parser) >= 1.14
BuildRequires:	perl(PPI) >= 1.115
BuildRequires:	perl(strict)
BuildRequires:	perl(Sysadm::Install) >= 0.11
BuildRequires:	perl(warnings)
# Examples
BuildRequires:	perl(Getopt::Std)
# Test Suite
BuildRequires:	perl(Test::More)
# Dependencies
Requires:	perl(HTML::TreeBuilder)
Requires:	perl(Pod::Parser) >= 1.14
Requires:	perl(PPI) >= 1.115

%description
File::Comments guesses the type of a given file, determines the format
used for comments, extracts all comments, and returns them as a
reference to an array of chunks. Alternatively, it strips all comments
from a file.

Currently supported are Perl scripts, C/C++ programs, Java, makefiles,
JavaScript, Python and PHP.

%prep
%setup -q -n File-Comments-%{version}

# Note: not turning off exec bits in examples because they don't
# introduce any unwanted dependencies (nor any dependencies that
# are not satisfied by packages that are already required)

# Remove provide for local package not in regular search path
%patch -P 0

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test TEST_VERBOSE=1

%files
%doc Changes README eg/
%{perl_vendorlib}/File/
%{_mandir}/man3/File::Comments.3*
%{_mandir}/man3/File::Comments::Plugin.3*
%{_mandir}/man3/File::Comments::Plugin::C.3*
%{_mandir}/man3/File::Comments::Plugin::HTML.3*
%{_mandir}/man3/File::Comments::Plugin::Java.3*
%{_mandir}/man3/File::Comments::Plugin::JavaScript.3*
%{_mandir}/man3/File::Comments::Plugin::Makefile.3*
%{_mandir}/man3/File::Comments::Plugin::PHP.3*
%{_mandir}/man3/File::Comments::Plugin::Perl.3*
%{_mandir}/man3/File::Comments::Plugin::Python.3*
%{_mandir}/man3/File::Comments::Plugin::Shell.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 12 2023 Paul Howarth <paul@city-fan.org> - 0.08-37
- Spec tidy-up
  - Use SPDX-format license tag
  - Use author-independent source URL
  - Avoid use of deprecated patch syntax
  - Simplify find command using -delete
  - Fix permissions verbosely

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-34
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-31
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-28
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-25
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-22
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-19
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-17
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Paul Howarth <paul@city-fan.org> - 0.08-15
- Spec clean-up
  - Patch code to hide private module and avoid need for provides filter
  - Classify buildreqs by usage
  - Drop %%defattr, redundant since rpm 4.4
  - No need to remove empty directories from the buildroot
  - Drop Group and BuildRoot tags, redundant since rpm 4.6
  - Drop buildroot cleaning, redundant since rpm 4.8

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-13
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-12
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.08-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Petr Pisar <ppisar@redhat.com> - 0.08-6
- Perl 5.16 rebuild

* Thu Jan 12 2012 Paul Howarth <paul@city-fan.org> - 0.08-5
- Spec clean-up:
  - Nobody else likes macros for commands
  - Use DESTDIR rather than PERL_INSTALL_ROOT
  - Use %%{_fixperms} macro rather than our own chmod incantation
  - Update provides filter to work with rpm ≥ 4.9

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.08-4
- Perl mass rebuild

* Tue Feb  8 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-2
- Rebuild to fix problems with vendorarch/lib (#661697)

* Fri Dec 10 2010 Paul Howarth <paul@city-fan.org> - 0.08-1
- Update to 0.08
  - Adapt to HTML::Element >=4 change that omits trailing newline in generated
    HTML (CPAN RT#63788)
- Resolves FTBFS issue in Rawhide (#661088)

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.07-7
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.07-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.07-5
- Rebuild against perl 5.10.1

* Fri Sep 18 2009 Paul Howarth <paul@city-fan.org> 0.07-4
- Add runtime dependencies not determined automatically by RPM

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 0.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct  9 2008 Paul Howarth <paul@city-fan.org> 0.07-1
- Initial RPM version
