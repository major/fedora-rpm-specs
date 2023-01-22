Name:           perl-Marpa-XS
Version:        1.008000
Release:        37%{?dist}
Summary:        Language grammar parser module for Perl
License:        LGPLv3+
URL:            https://metacpan.org/release/Marpa-XS
Source0:        https://cpan.metacpan.org/authors/id/J/JK/JKEGL/Marpa-XS-%{version}.tar.gz
Patch1:         0001-Require-2.124-Data-Dumper.patch
# Adjust to Perl 5.32, bug #1851334
Patch2:         Marpa-XS-1.008000-Adjust-to-Perl-5.32.patch
# Suppress the warnings about an intentionally used smartmatch operator
Patch3:         Marpa-XS-1.008000-Suppress-warnings-about-an-experimental-smartmatch-o.patch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-Glib-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.27
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Spec) >= 0.82
BuildRequires:  perl(Glib::Install::Files)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Time::Piece)
# Run-time
BuildRequires:  perl(Carp) >= 1.08
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper) >= 2.125
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.12
BuildRequires:  perl(Glib) >= 1.223
# Bareword Glib::Log exported from Glib probably
BuildRequires:  perl(List::Util) >= 1.21
BuildRequires:  perl(Scalar::Util) >= 1.21
# Using ExtUtils::PkgConfig instead of perl(XSLoader)
BuildRequires:  pkgconfig(glib-2.0)
# Tests
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(YAML::XS)
# Optional tests
BuildRequires:  perl(PPI) >= 1.206
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Task::Weaken)
# perl(Test::Weaken) >= 3.004000 not packaged yet
# AFAIK the PPI is used at test-time only. Do not require it?
Requires:       perl(PPI) >= 1.206
Provides:       perl(Marpa::XS::Version) = %{version}

%{?perl_default_filter}

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Carp\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Marpa::XS\\)$
  

%description
Marpa::XS is a XS version of Marpa.

Marpa parses any language whose grammar can be written in BNF. That 
includes recursive grammars, ambiguous grammars, infinitely ambiguous 
grammars and grammars with useless or empty productions.


%prep
%setup -q -n Marpa-XS-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Update the various config.guess to upstream release for newer arch support
find ./ -name config.guess -exec cp /usr/lib/rpm/redhat/config.guess {} ';'
find ./ -name config.sub -exec cp /usr/lib/rpm/redhat/config.sub {} ';'

%build
# Switch to C89 mode because the implementation relies on implicit
# function declarations.
%set_build_flags
CC="$CC -std=gnu89"
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build


%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*


%check
./Build test


%files
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Marpa*
%{_mandir}/man3/*
%license COPYING COPYING.LESSER LICENSE
%doc Changes README


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.008000-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec  7 2022 Florian Weimer <fweimer@redhat.com> - 1.008000-36
- Build in C89 mode (#2151502)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.008000-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.008000-34
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.008000-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.008000-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.008000-31
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.008000-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.008000-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Petr Pisar <ppisar@redhat.com> - 1.008000-28
- Adjust to Perl 5.32 (bug #1851334)
- Suppress the warnings about an intentionally used smartmatch operator
- Copy autoconf cache from /usr/lib/rpm/redhat

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.008000-27
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.008000-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.008000-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.008000-24
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.008000-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.008000-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.008000-21
- Perl 5.28 rebuild

* Mon Feb 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.008000-20
- Add build-require gcc

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.008000-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.008000-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.008000-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.008000-16
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.008000-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.008000-14
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.008000-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008000-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.008000-11
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.008000-10
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008000-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 29 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.008000-8
- Update config.guess/sub for newer arch support

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Petr Pisar <ppisar@redhat.com> - 1.008000-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 1.008000-2
- Perl 5.16 rebuild

* Fri Apr  6 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.008000-1
- bump to 1.008000

* Wed Mar 14 2012 Petr Pisar <ppisar@redhat.com> - 1.006000-1
- 1.006000 bump

* Mon Feb 27 2012 Petr Pisar <ppisar@redhat.com> - 1.004000-1
- 1.004000 bump
- Clean spec file
- Declare all dependencies

* Mon Feb 13 2012 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 1.002000-2.1
- BR IPC::Cmd

* Thu Jan 12 2012 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 1.002000-2
- Add a missing BR (Marcela Mašláňová, #772503)
- Filter out redundant provides/requires (Marcela Mašláňová, #772503)

* Tue Jan 03 2012 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> 1.002000-1
- Specfile autogenerated by cpanspec 1.78.
- Cosmetic fixes
