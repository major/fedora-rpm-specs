%global cpan_version 2.003000

Name:       perl-XML-LibXSLT
# NOTE: also update perl-XML-LibXML to a compatible version.  See below why.
Version:    %(echo '%{cpan_version}' | sed 's/\(\....\)\(.\)/\1.\2/')
Release:    5%{?dist}
Summary:    Perl module for interfacing to GNOME's libxslt
# lib/XML/LibXSLT.pm: GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/XML/LibXSLT/Quick.pm: MIT
License:    ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND MIT
URL:        https://metacpan.org/release/XML-LibXSLT
Source0:    https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/XML-LibXSLT-%{cpan_version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Path) >= 2.06
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(autodie)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Socket::INET)
# the package shares code with perl-XML-LibXML, we have to require a compatible version
# see https://bugzilla.redhat.com/show_bug.cgi?id=469480
# for testing is needed the same version of XML::LibXML
# BUT XML::LibXML has new bugfix releases, but XML::LibXSLT not
BuildRequires:  perl(XML::LibXML::Boolean)
BuildRequires:  perl(XML::LibXML::Literal)
BuildRequires:  perl(XML::LibXML::NodeList)
BuildRequires:  perl(XML::LibXML::Number)
BuildRequires:  perl(XML::LibXML) >= %{version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxslt) >= 1.1.28
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
Requires:   perl(DynaLoader)
Requires:   perl(Exporter)
Requires:   perl(XML::LibXML) >= %{version}

%description
This module is a fast XSLT library, based on the Gnome libxslt engine
that you can find at http://www.xmlsoft.org/XSLT/

%package tests
Summary:        Tests for %{name}
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND MIT
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%{?perl_default_filter}

%prep
%autosetup -p1 -n XML-LibXSLT-%{cpan_version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="%{optflags}" NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t example %{buildroot}%{_libexecdir}/%{name}
# Remove release tests
rm %{buildroot}%{_libexecdir}/%{name}/t/cpan-changes.t
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t
rm %{buildroot}%{_libexecdir}/%{name}/t/style-trailing-space.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README benchmark example
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/XML
%{_mandir}/man3/*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.003.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 07 2025 Jitka Plesnikova <jplesnik@redhat.com> - 2.003.000-4
- Perl 5.42 rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.003.000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.003.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 21 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.003.000-1
- 2.003000 bump (rhbz#2291310)

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.002.001-6
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.002.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.002.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.002.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 2.002.001-2
- Perl 5.38 rebuild

* Mon Feb 13 2023 Jitka Plesnikova <jplesnik@redhat.com> - 2.002.001-1
- 2.002001 bump
- Update license to SPDX format

* Thu Feb 09 2023 Florian Weimer <fweimer@redhat.com> - 2.002.000-5
- Port configure stage to C99

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.002.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.002.000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.002.000-2
- Perl 5.36 rebuild

* Wed May 18 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.002.000-1
- 2.002000 bump

* Mon May 16 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.001.000-1
- 2.001000 bump

* Mon Apr 11 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.000.000-1
- 2.000000 bump
- Package tests

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.99-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.99-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.99-1
- 1.99 bump

* Thu Jan 16 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.98-1
- 1.98 bump

* Tue Jan 14 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.97-1
- 1.97 bump

* Tue Jan 14 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.96-7
- Fixed tests for perl(XML::LibXML) = 2.0202

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.96-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.96-5
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.96-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.96-2
- Perl 5.28 rebuild

* Wed Feb 21 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.96-1
- 1.96 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 18 2017 Petr Pisar <ppisar@redhat.com> - 1.95-7
- Do not link against perllibs too (bugs #905482, #1481324)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.95-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Petr Pisar <ppisar@redhat.com> - 1.95-2
- Do not break tests by updating libxml2 library (CPAN RT#86398)

* Mon Aug 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.95-1
- 1.95 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.94-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.94-2
- Perl 5.22 rebuild

* Tue Feb 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.94-1
- 1.94 bump

* Thu Jan 08 2015 Petr Pisar <ppisar@redhat.com> - 1.92-5
- Do not link against perl extension libraries

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.92-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.92-1
- 1.92 bump

* Mon Mar 10 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.89-1
- 1.89 bump

* Wed Feb 19 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.88-1
- 1.88 bump

* Mon Feb 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.87-1
- 1.87 bump

* Thu Jan 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.84-1
- 1.84 bump

* Mon Nov 11 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.82-1
- 1.82 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.81-1
- 1.81 bump
- Specify all dependencies

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.80-2
- Perl 5.18 rebuild

* Thu Jan 24 2013 Petr Šabata <contyk@redhat.com> - 1.80-1
- 1.80 bump

* Mon Nov 26 2012 Petr Pisar <ppisar@redhat.com> - 1.79-1
- 1.79 bump

* Fri Sep 14 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.78-1
- 1.78 bump

* Mon Aug 27 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.77-4
- Update source link.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.77-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.77-2
- Perl 5.16 rebuild

* Mon Feb 27 2012 Petr Šabata <contyk@redhat.com> - 1.77-1
- 1.77 bump
- Remove some ugly macros

* Fri Jan 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.76-1
- 1.76 bump

* Mon Oct 31 2011 Petr Sabata <contyk@redhat.com> - 1.75-1
- 1.75 bump

* Wed Oct 26 2011 Petr Sabata <contyk@redhat.com> - 1.74-1
- 1.74 bump

* Tue Oct 11 2011 Petr Sabata <contyk@redhat.com> - 1.73-1
- 1.73 bump

* Fri Oct 07 2011 Petr Sabata <contyk@redhat.com> - 1.72-1
- 1.72 bump
- benchmark.pl moved to benchmark/

* Mon Sep 19 2011 Petr Sabata <contyk@redhat.com> - 1.71-1
- 1.71 bump
- Remove BuildRoot tag
- Remove useless vendorarch macro definition

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.70-8
- Perl mass rebuild

* Fri Jun 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.70-7
- clean spec, comment BR on XML::LibXML, use filter on *.so

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.70-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov  5 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1.70-5
- add BR

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.70-4
- Mass rebuild with perl-5.12.0

* Thu Mar 11 2010 Paul Howarth <paul@city-fan.org> - 1.70-3
- rebuild for new gdbm

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.70-2
- rebuild against perl 5.10.1

* Fri Nov 20 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1:1.70-1
- update to fix 539102

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.68-4
- rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 18 2009 Stepan Kasal <skasal@redhat.com> - 1.68-3
- patch to fix a refcounting bug leading to segfaults (#490781)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.68-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 20 2008 Paul Howarth <paul@city-fan.org> - 1.68-1
- update to 1.68
- relax hard version requirement on XML::LibXML, which is at 1.69 upstream
  but 1.67 or above will suffice (care will still have to be taken to keep
  the packages in sync, particularly when XML::LibXML is updated)
- specify $RPM_OPT_FLAGS once rather than twice
- drop historical perl version requirement, which is met even by EL-3
- explicitly buildreq ExtUtils::MakeMaker rather than just perl-devel

* Mon Nov  3 2008 Stepan Kasal <skasal@redhat.com> - 1.66-2
- require XML::LibXML of the same version

* Fri Aug  8 2008 Zing <zing@fastmail.fm> - 1.66-1
- update to 1.66

* Sat May 31 2008 Zing <zing@fastmail.fm> - 1.63-6
- rpm check stage barfs on || :

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.63-5
- rebuild for new perl (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.63-4
- Autorebuild for GCC 4.3

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.63-3
- rebuild for new perl

* Sat Jan 19 2008 Zing <zing@fastmail.fm> - 1.63-2
- build requires gdbm-devel

* Fri Jan 18 2008 Zing <zing@fastmail.fm> - 1.63-1
- update to 1.63

* Sat Aug 11 2007 Zing <zing@fastmail.fm> - 1.62-2
- require perl-devel

* Tue Aug  7 2007 Zing <zing@fastmail.fm> - 1.62-1
- update to 1.62
- Conform to Fedora Licensing Guideline

* Fri Sep  8 2006 Zing <zing@fastmail.fm> - 1.58-3
- rebuild for FE6

* Tue Feb 14 2006 Zing <shishz@hotpop.com> - 1.58-2
- rebuild for FE5

* Wed Aug 17 2005 Zing <shishz@hotpop.com> - 1.58-1
- new upstream
- use dist macro

* Fri Apr  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat Mar  5 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.57-3
- Drop pre-FC2 LD_RUN_PATH hack.
- Install benchmark.pl only as %%doc.

* Fri Feb 25 2005 Zing <shishz@hotpop.com> - 1.57-2
- QA from Ville Skyttä
-   BuildRequires XML::LibXML >= 1.57
-   BuildRequires libxslt-devel
-   put benchmark.pl in %%doc

* Fri Feb 25 2005 Zing <shishz@hotpop.com> - 1.57-1
- First build.
