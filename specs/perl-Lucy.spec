Name:           perl-Lucy
Version:        0.6.2
Release:        24%{?dist}
Summary:        Search engine library
# other files:                              Apacge-2.0
# modules/unicode/ucd/WordBreak.tab:        Unicode-DFS-2015
# modules/unicode/utf8proc/utf8proc.c:      MIT
# modules/unicode/utf8proc/utf8proc_data.h: Unicode-DFS-2015
## Not distributed in binary package
# devel/bin/gen_word_break_data.pl:         Apache-2.0
# sample/us_constitution:                   Public domain
License:        Apache-2.0 AND MIT AND Unicode-DFS-2015
URL:            https://metacpan.org/release/Lucy
# There is charmonizer.c which is becoming a separate project
# <git://git.apache.org/lucy-charmonizer.git>. However, lucy-charmonizer has
# not yet been released <http://lucy.apache.org/download.html>.
# Provided charmonizer.c is used only at build time and upstream code is not
# ready for external lucy-charmonizer (upstream treats it like a build-time
# only copy library) I'm not going to unbudle the charmonizer.c now.
Source0:        https://cpan.metacpan.org/authors/id/N/NW/NWELLNHOF/Lucy-%{version}.tar.gz
# Use system lemon instead of bundled one. See
# <https://issues.apache.org/jira/browse/CLOWNFISH-60> for similar
# perl-Clownfish-CFC issue and upstream reaction.
Patch0:         Lucy-0.6.0-Use-system-lemon.patch
Patch1:         Lucy-0.6.1-Fix-building-on-Perl-without-dot-in-INC.patch
BuildRequires:  coreutils
BuildRequires:  findutils
# This package should not use GCC directly, it uses Clownfish-CFC instead.
BuildRequires:  gcc
BuildRequires:  lemon
BuildRequires:  perl-interpreter
# This package should not use any Perl headers, it uses Clownfish-CFC instead.
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clownfish::CFC::Perl::Build) >= 0.006002
BuildRequires:  perl(Clownfish::CFC::Perl::Build::Charmonic)
BuildRequires:  perl(Config)
# CPAN::Meta not used
BuildRequires:  perl(Cwd)
# Data::Dumper not used
BuildRequires:  perl(Devel::PPPort) >= 3.14
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.21
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.18
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
# Module::Build not used
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(bytes)
BuildRequires:  perl(Clownfish) >= 0.006002
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
# Tests
BuildRequires:  perl(CGI)
BuildRequires:  perl(Clownfish::Err)
BuildRequires:  perl(Clownfish::Obj)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(utf8)

%{?perl_default_filter}

# Remove unversioned provides
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Lucy::Object::Obj\\)$

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Clownfish\\)$

%description
Lucy is a loose port of the Java search engine library Apache Lucene,
written in Perl and C. The archetypal application is website search, but it
can be put to many different uses.

%prep
%setup -q -n Lucy-%{version}
%patch -P0 -p1
%patch -P1 -p1
# Unbundle lemon
rm -rf lemon
sed -i -e '/^lemon\//d' MANIFEST
# Correct shellbangs
for F in sample/indexer.pl sample/search.cgi; do
    sed -i -e \
    's|^#!/usr/local/bin/perl|%(perl -MConfig -e 'print $Config{startperl}')|' \
    "$F"
 done

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
# Remove empty files
rm -f $RPM_BUILD_ROOT/%{perl_vendorarch}/auto/Lucy/Lucy.bs
# %%{perl_vendorarch}/Clownfish files are needed for building third-party
# extension against perl-Lucy. They could be moved into a subpackage.
# <https://issues.apache.org/jira/browse/LUCY-283>
%{_fixperms} $RPM_BUILD_ROOT/*


%check
./Build test

%files
%license LICENSE
%doc CHANGES CONTRIBUTING README sample
%{perl_vendorarch}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.2-22
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.2-18
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Michal Josef Špaček <mspacek@redhat.com> - 0.6.2-16
- Update license to SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.2-14
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.2-11
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.2-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.2-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.2-2
- Perl 5.28 rebuild

* Fri Mar 16 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.2-1
- 0.6.2 bump

* Fri Feb 09 2018 Petr Pisar <ppisar@redhat.com> - 0.6.1-8
- Adapt to changes in lemon-3.22.0 (bug #1543288)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.1-4
- Perl 5.26 rebuild

* Wed May 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.1-3
- Fix building on Perl without '.' in @INC

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.1-1
- 0.6.1 bump

* Mon Oct 03 2016 Petr Pisar <ppisar@redhat.com> - 0.6.0-1
- 0.6.0 bump

* Tue Jun 21 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.5.1-1
- 0.5.1 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.5.0-2
- Perl 5.24 rebuild

* Thu Apr 07 2016 Petr Pisar <ppisar@redhat.com> - 0.5.0-1
- 0.5.0 bump (license changed to "ASL 2.0 and MIT")

* Thu Mar 24 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.4.4-1
- 0.4.4 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 17 2015 Petr Pisar <ppisar@redhat.com> - 0.4.2-1
- 0.4.2 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.3-5
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.3.3-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 17 2014 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 0.3.3-1
- Lucy package based on KinoSearch package

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.31.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.31.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 1:0.31.5-2
- Perl 5.16 rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 1:0.31.5-1
- 0.315 bump

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 1:0.31-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:0.31-3
- Perl mass rebuild

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:0.31-2
- 661697 rebuild for fixing problems with vendorach/lib
- add BR

* Sun Dec 12 2010 Lubomir Rintel <lkundrak@v3.sk> - 1:0.31-1
- BR Time::HiRes to fix el6 build
- Rebase to later version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.165-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 13 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.165-1
- Upstream applied our PowerPC patch

* Sun Mar 29 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.164-1
- Update to 0.164
- Add missing Pod::Coverage BRs (Robert Scheck)
- Fix a PowerPC signedness issue
- Clarify licensing, re-add ApacheLicense2.0.txt

* Sat Feb 14 2009 Ian Burrell <ianburrell@gmail.com> - 0.163-2
- remove empty KinoSearch.bs
- remove ApacheLicense2.0.txt

* Thu Feb 05 2009 Ian Burrell <ianburrell@gmail.com> 0.163-1
- Change to perl_vendorarch
- Remove devel, src from doc
- Specfile autogenerated by cpanspec 1.77.
