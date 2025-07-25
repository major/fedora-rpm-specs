Name:           perl-SVG
Version:        2.87
Release:        10%{?dist}
Summary:        An extension to generate stand-alone or inline SGV
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SVG
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/SVG-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(Test::More) >= 0.94

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(SVG::Element\\)$

%description
SVG.pm is a Perl extension to generate stand-alone or inline SVG
(scaleable vector graphics) images using the W3C SVG XML recommendation

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n SVG-%{version}

# avoid extra dependencies
chmod 644 examples/*

# Fix line-endings
for i in SVG_02_sample.pl image_sample.pl inline_sample.pl inlinesvg.pl starpath.cgi sun_text_sample.pl svgtest2.pl ; do
    perl -pi -e 's/\r//' examples/$i
done

# Help file to recognise the Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc README Changes examples
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.87-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.87-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.87-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.87-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.87-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.87-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.87-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.87-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.87-2
- Perl 5.36 rebuild

* Sun May 22 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.87-1
- 2.87 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.86-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.86-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.86-2
- Perl 5.34 rebuild

* Thu Apr 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.86-1
- 2.86 bump
- Package tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.85-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.85-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.85-1
- 2.85 bump

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.84-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.84-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.84-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.84-2
- Perl 5.28 rebuild

* Tue Feb 20 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.84-1
- 2.84 bump

* Tue Feb 13 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.83-1
- 2.83 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.82-1
- 2.82 bump

* Mon Dec 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.80-1
- 2.80 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.78-1
- 2.78 bump

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.77-2
- Perl 5.26 rebuild

* Thu Jun 01 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.77-1
- 2.77 bump

* Tue May 09 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.76-1
- 2.76 bump

* Fri May 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.74-1
- 2.74 bump

* Thu May 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.73-1
- 2.73 bump

* Wed May 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.72-1
- 2.72 bump

* Tue May 02 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.71-1
- 2.71 bump

* Fri Apr 28 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.70-1
- 2.70 bump

* Fri Apr 21 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.69-1
- 2.69 bump

* Thu Apr 20 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.68-1
- 2.68 bump

* Wed Apr 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.67-1
- 2.67 bump

* Tue Apr 18 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.66-1
- 2.66 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.64-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.64-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 16 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.64-1
- 2.64 bump
- Modernize spec

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.49-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.49-17
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.49-16
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.49-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.49-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.49-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.49-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.49-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.49-10
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.49-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.49-8
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.49-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.49-6
- 661697 rebuild for fixing problems with vendorach/lib

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.49-5
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.49-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb  2 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.49-1
- Update to upstream 2.49

* Tue Jun  3 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.44-1
- Update to latest upstream (2.44)
- Fix spec file syntax (#449663)
- Add BR: perl(Test::More)

* Tue Mar 18 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.37-1
- New upstream release (2.37)

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.36-3
- rebuild for new perl

* Sat Oct 13 2007 Alex Lancaster <alexl@users.sourceforge.net> 2.36-2
- Add missing BR: perl(ExtUtils::MakeMaker)

* Sat Oct 13 2007 Alex Lancaster <alexl@users.sourceforge.net> 2.36-1
- Update to 2.36

* Thu Aug 23 2007 Alex Lancaster <alexl@users.sourceforge.net> 2.34-2
- License tag to GPL+ or Artistic as per new guidelines.

* Sat Aug 18 2007 Alex Lancaster <alexl@users.sourceforge.net> 2.34-1
- Update to latest upstream

* Fri Mar 23 2007 Alex Lancaster <alexl@users.sourceforge.net> 2.33-2
- Filter extra non-explicit (SVG::Element) provides

* Wed Mar 14 2007 Alex Lancaster <alexl@users.sourceforge.net> 2.33-1
- Update to 2.33
- Fix rpmlint issues

* Wed Apr 06 2005 Hunter Matthews <thm@duke.edu> 2.32-2
- Review suggestions from José Pedro Oliveira

* Fri Mar 18 2005 Hunter Matthews <thm@duke.edu> 2.32-1
- Initial packaging.
