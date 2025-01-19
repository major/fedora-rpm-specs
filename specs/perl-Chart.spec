Name:           perl-Chart
Version:        2.403.9
Release:        7%{?dist}
Summary:        Series of charting modules
# lib/Chart.pm:         GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Chart/Manual.pod: GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Chart/Manual/Methods.pod: GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Chart/Manual/Workflows.pod    GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Chart/Setting.pm: GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:              GPL-1.0-or-later OR Artistic-1.0-Perl
# README:               GPL-1.0-or-later OR Artistic-1.0-Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Chart
Source0:        https://cpan.metacpan.org/authors/id/L/LI/LICHTKIND/Chart-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp) >= 1.35
BuildRequires:  perl(constant)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(GD) >= 2
BuildRequires:  perl(GD::Image)
BuildRequires:  perl(Graphics::Toolkit::Color) >= 1
BuildRequires:  perl(POSIX)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp) >= 0.19
Requires:       perl(Carp) >= 1.35
Requires:       perl(GD) >= 2
Requires:       perl(Graphics::Toolkit::Color) >= 1

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Carp|GD|Graphics::Toolkit::Color)\\)$

%description
This module is an attempt to build a general purpose graphing module that
is easily modified and expanded.  Chart uses Lincoln Stein's GD module for
all of its graphics primitives calls.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(GD) >= 2

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Chart-v%{version}
chmod -c 644 TODO
chmod +x t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
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
%doc Changes CONTRIBUTING README TODO
%{perl_vendorlib}/Chart.pm
%{perl_vendorlib}/Chart
%{_mandir}/man3/Chart.*
%{_mandir}/man3/Chart::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.403.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.403.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.403.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.403.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.403.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.403.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Petr Pisar <ppisar@redhat.com> - 2.403.9-1
- 2.403.9 bump

* Mon Oct 24 2022 Petr Pisar <ppisar@redhat.com> - 2.403.8-1
- 2.403.8 bump

* Mon Aug 01 2022 Petr Pisar <ppisar@redhat.com> - 2.403.7-1
- 2.403.7 bump

* Thu Jul 21 2022 Petr Pisar <ppisar@redhat.com> - 2.403.6-1
- 2.403.6 bump

* Mon Jul 18 2022 Petr Pisar <ppisar@redhat.com> - 2.403.5-1
- 2.403.5 bump

* Wed Jul 13 2022 Petr Pisar <ppisar@redhat.com> - 2.403.2-1
- 2.403.2 bump

* Wed Jul 13 2022 Petr Pisar <ppisar@redhat.com> - 2.403.1-1
- 2.403.1 bump

* Fri Jul 08 2022 Petr Pisar <ppisar@redhat.com> - 2.403.0-1
- 2.403.0 bump

* Mon Jun 20 2022 Petr Pisar <ppisar@redhat.com> - 2.402.3-1
- 2.402.3 bump

* Wed Jun 15 2022 Petr Pisar <ppisar@redhat.com> - 2.402.2-1
- 2.402.2 bump

* Thu Jun 09 2022 Petr Pisar <ppisar@redhat.com> - 2.402.1-1
- 2.402.1 bump

* Thu Jun 09 2022 Petr Pisar <ppisar@redhat.com> - 2.402.0-1
- 2.402.0 bump
- License changed to (GPL+ or Artistic)

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.401.1-2
- Perl 5.36 rebuild

* Tue Apr 05 2022 Petr Pisar <ppisar@redhat.com> - 2.401.1-1
- 2.401.1 bump

* Mon Apr 04 2022 Petr Pisar <ppisar@redhat.com> - 2.400.10-1
- 2.400.10 bump

* Fri Apr 01 2022 Petr Pisar <ppisar@redhat.com> - 2.400.5-1
- 2.400.5 bump
- Package the tests

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.10-20
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.10-17
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.10-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.10-11
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.10-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.10-6
- Perl 5.24 rebuild

* Fri Mar 18 2016 Petr Pisar <ppisar@redhat.com> - 2.4.10-5
- Modernize spec file

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.10-2
- Perl 5.22 rebuild

* Thu Mar 19 2015 Petr Šabata <contyk@redhat.com> - 2.4.10-1
- 2.4.10 bump, no changes

* Mon Feb 09 2015 Petr Šabata <contyk@redhat.com> - 2.4.9-1
- 2.4.9 bump, no changes

* Wed Nov 12 2014 Petr Šabata <contyk@redhat.com> - 2.4.8-1
- 2.4.8 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.4.6-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct  1 2013 Paul Howarth <paul@city-fan.org> - 2.4.6-1
- Update to 2.4.6
  - Corrections to imagemap production in Composite.pm and Lines.pm
  - The brush styles to points and linespoints are extended: not only circles
    represent the points but a number of different brush styles, linke donut,
    Star and so on
  - Typo in _draw_x_ticks corrected
  - Methods scalar_png(), scalar_jpeg() corrected for result
  - Test routine t/scalarImage.t added
  - Chart.pod corrected
  - Documentation.pdf explains the use of colors (appendix added)
  - Corrections in base.pm, routines _draw_bottom_legends, _draw_x_number_ticks
  - Corrections in LinesPoints.pm, routine _draw_data
- Add patch for warnings in Perl 5.16+ (CPAN RT#79658)
- Drop %%defattr, redundant since rpm 4.4
- Don't need to remove empty directories from the buildroot
- Use DESTDIR rather than PERL_INSTALL_ROOT

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.4.2-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 2.4.2-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.4.2-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.4.2-2
- Rebuild to fix problems with vendorarch/lib (#661697)

* Sun Dec 12 2010 Steven Pritchard <steve@kspei.com> 2.4.2-1
- Update to 2.4.2.
- Improve Summary and description.
- Use PERL_INSTALL_ROOT instead of DESTDIR while installing.

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.4.1-10
- Mass rebuild with perl-5.12.0
- remove two tests failing

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.4.1-9
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.4.1-6
- Rebuild for new perl

* Mon Apr 09 2007 Steven Pritchard <steve@kspei.com> 2.4.1-5
- Fix find option order.
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.
- Minor spec cleanup to more closely resemble cpanspec output.

* Mon Aug 28 2006 Michael J. Knox <michael[AT]knox.net.nz> - 2.4.1-4
- Rebuild for FC6

* Mon May 29 2006 Michael J. Knox <michael[AT]knox.net.nz> - 2.4.1-3
- rebuilt and reimported in to devel

* Wed Jan 25 2006 Ville Skyttä <ville.skytta at iki.fi> - 2.4.1-1
- 2.4.1.
- Don't ship rgb.txt in docs.
- Specfile cleanups.

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 2.3-3
- Rebuilt

* Sun Jul 11 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.3-2
- Bring up to date with current fedora.us Perl Spec template.

* Thu Jan 15 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.3-0.fdr.1
- Update to 2.3.
- Fix file permissions.

* Sat Oct 11 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.2-0.fdr.1
- First build.
