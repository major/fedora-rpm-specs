Name:           perl-Imager
Version:        1.025
Release:        2%{?dist}
Summary:        Perl extension for Generating 24 bit Images
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Imager
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TONYC/Imager-%{version}.tar.gz
BuildRequires:  freetype-devel
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel >= 4.0.8
BuildRequires:  t1lib-devel
# rgb.txt, c.f. lib/Imager/Color.pm
BuildRequires:  rgb
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
# Unused BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Liblist)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(vars)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(B)
BuildRequires:  perl(bignum)
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(threads)
BuildRequires:  perl(Tie::Handle)
# Optional tests only
BuildRequires:  perl(Affix::Infix2Postfix)
BuildRequires:  perl(CPAN::Meta) >= 2.110580
BuildRequires:  perl(Image::Math::Constrain)
BuildRequires:  perl(Inline)
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
Requires:       pkgconfig
Requires:       rgb
Requires:       perl(Devel::CheckLib)
# Unused Requires:       perl(File::Spec)
Requires:       perl(warnings::register)
Requires:       perl(XSLoader)

%{?perl_default_filter}

# Imager-1.020 disabled Imager::Font::T1 and Freetype 1.x fonts by default
# Installing Imager no longer installs Imager::Font::T1 by default.
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Imager::Font::T1\\)

%description
Imager is a module for creating and altering images. It can read and
write various image formats, draw primitive shapes like lines,and
polygons, blend multiple images together in various ways, scale, crop,
render text and more.

%package Test
Requires: perl-Imager = %{version}-%{release}
Summary: perl-Imager's Test module

%description Test
%{summary}.

%prep
%setup -q -n Imager-%{version}
find -executable -type f -exec chmod -x {} \;
perl -MConfig -pi -e 's|^#!perl|$Config{startperl}|' samples/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README samples
%{perl_vendorarch}/auto/Imager*
%exclude %{perl_vendorarch}/Imager/Test.pm
%{perl_vendorarch}/Imager*
%exclude %{_mandir}/man3/Imager::Test.3pm*
%{_mandir}/man3/Imager*

%files Test
%dir %{perl_vendorarch}/Imager
%{perl_vendorarch}/Imager/Test.pm
%{_mandir}/man3/Imager::Test.3pm*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.025-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 18 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.025-1
- 1.025 bump (rhbz#2326658, rhbz#2320127)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.024-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.024-2
- Perl 5.40 rebuild

* Mon Apr 08 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.024-1
- 1.024 bump (rhbz#2273751)

* Thu Jan 25 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.023-1
- 1.023 bump (rhbz#2259087)

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 04 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.022-1
- 1.022 bump (rhbz#2252605)

* Fri Dec 01 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.021-1
- 1.021 bump (rhbz#2252370)

* Mon Nov 13 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.020-1
- 1.020 bump (rhbz#2249324)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.019-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.019-4
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.019-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.019-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.019-1
- 1.019 bump

* Mon Jun 20 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.018-1
- 1.018 bump

* Tue Jun 14 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.017-1
- 1.017 bump

* Mon Jun 13 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.016-1
- 1.016 bump

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.015-2
- Perl 5.36 rebuild

* Mon May 09 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.015-1
- 1.015 bump

* Thu Apr 28 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.014-1
- 1.014 bump

* Wed Apr 27 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.013-1
- 1.013 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.012-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.012-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.012-2
- Perl 5.32 rebuild

* Mon Jun 15 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.012-1
- 1.012 bump

* Thu Mar 12 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.011-5
- Add BR: perl(blib)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.011-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.011-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.011-2
- Perl 5.30 rebuild

* Thu Mar 07 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.011-1
- 1.011 bump

* Mon Feb 18 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.010-1
- 1.010 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.009-1
- 1.009 bump

* Wed Jan 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.008-1
- 1.008 bump

* Mon Nov 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.007-1
- 1.007 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.006-5
- Perl 5.28 rebuild

* Mon Feb 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.006-4
- Add build-require gcc

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 1.006-3
- Rebuild (giflib)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 28 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.006-1
- 1.006 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.005-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.005-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.005-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.005-2
- Perl 5.24 rebuild

* Mon Apr 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.005-1
- 1.005 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Petr Šabata <contyk@redhat.com> - 1.004-1
- 1.004 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Petr Šabata <contyk@redhat.com> - 1.003-1
- 1.003 bump, performance enhancements

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.001-2
- Perl 5.22 rebuild

* Tue Jan 06 2015 Petr Šabata <contyk@redhat.com> - 1.001-1
- 1.001 bump

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.000-3
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.000-1
- Upstream update.

* Sat Jun 28 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.99-1
- Upstream update.
- Remove 2014-06-18's changes (went upstream).

* Wed Jun 18 2014 Petr Pisar <ppisar@redhat.com> - 0.98-3
- Adjusts tests to libpng-1.6.10 (bug #1099392)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 03 2014  Ralf Corsépius <corsepiu@fedoraproject.org> - 0.98-1
- Upstream update.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Pisar <ppisar@redhat.com> - 0.97-2
- Perl 5.18 rebuild

* Wed Jul 17 2013  Ralf Corsépius <corsepiu@fedoraproject.org> - 0.97-1
- Upstream update.

* Tue May 21 2013  Ralf Corsépius <corsepiu@fedoraproject.org> - 0.96-1
- Upstream update.

* Sun Apr 21 2013  Ralf Corsépius <corsepiu@fedoraproject.org> - 0.95-1
- Upstream update.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.94-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.94-2
- rebuild due to "jpeg8-ABI" feature drop

* Sat Dec 22 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.94-1
- Upstream update.

* Wed Nov 07 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.93-1
- Upstream update.
- Activate AUTOMATED_TESTING=1.

* Fri Aug 17 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.92-1
- Upstream update.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 0.91-2
- Perl 5.16 rebuild

* Sun Jun 10 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.91-1
- Upstream update.

* Mon Mar 19 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.89-1
- Upstream update.
- Split out perl(Imager::Test) (Avoid *-devel deps).

* Mon Mar 05 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.88-1
- Upstream update.

* Thu Jan 05 2012 Ralf Corsépius <corsepiu@fedoraproject.org> 0.87-1
- Upstream update.

* Wed Nov 09 2011 Iain Arnell <iarnell@gmail.com> 0.86-1
- Update to latest upstream version

* Tue Sep 06 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.85-1
- Upstream update.

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.84-2
- Perl mass rebuild

* Mon Jun 27 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.84-1
- Upstream update.
- Modernize spec-file.

* Sun May 22 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.83-1
- Upstream update.

* Wed Mar 30 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.82-1
- Upstream update.

* Fri Feb 18 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.81-1
- Upstream update.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 21 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 0.80-1
- Upstream update.
- BR: giflib-devel instead of libungif-devel.
- spec file massage.
- Add perl_default_filter.

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.79-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Dec 12 2010 Steven Pritchard <steve@kspei.com> 0.79-1
- Update to 0.79.

* Fri Dec 10 2010 Steven Pritchard <steve@kspei.com> 0.78-1
- Update to 0.78.

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.67-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.67-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.67-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.67-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Steven Pritchard <steve@kspei.com> 0.67-1
- Update to 0.67.

* Sat May 31 2008 Steven Pritchard <steve@kspei.com> 0.65-1
- Update to 0.65.

* Thu Apr 24 2008 Steven Pritchard <steve@kspei.com> 0.64-2
- Rebuild.

* Thu Apr 24 2008 Steven Pritchard <steve@kspei.com> 0.64-1
- Update to 0.64 (CVE-2008-1928).
- Add versioned Test::More BR.

* Thu Mar  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.62-3
- rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.62-2
- Autorebuild for GCC 4.3

* Tue Dec 11 2007 Steven Pritchard <steve@kspei.com> 0.62-1
- Update to 0.62.
- Update License tag.

* Mon Sep 17 2007 Steven Pritchard <steve@kspei.com> 0.60-1
- Update to 0.60.

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.59-2
- Rebuild for selinux ppc32 issue.

* Tue Jun 26 2007 Steven Pritchard <steve@kspei.com> 0.59-1
- Update to 0.59.

* Fri May 18 2007 Steven Pritchard <steve@kspei.com> 0.58-1
- Update to 0.58.
- Drop hack to change location of rgb.txt (fixed upstream).
- BR Image::Math::Constrain and Affix::Infix2Postfix for better test coverage.

* Tue May 01 2007 Steven Pritchard <steve@kspei.com> 0.57-1
- Update to 0.57.
- BR gdbm-devel.

* Mon Apr 02 2007 Steven Pritchard <steve@kspei.com> 0.56-2
- BR Inline, Test::Pod, and Test::Pod::Coverage perl modules and rgb
  (for rgb.txt) for better test coverage.
- Fix path to rgb.txt in lib/Imager/Color.pm and t/t15color.t.

* Mon Apr 02 2007 Steven Pritchard <steve@kspei.com> 0.56-1
- Update to 0.56.
- BR ExtUtils::MakeMaker.

* Tue Dec 26 2006 Steven Pritchard <steve@kspei.com> 0.55-1
- Update to 0.55.
- Cleanup to more closely resemble current cpanspec output.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.54-2
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Steven Pritchard <steve@kspei.com> 0.54-1
- Update to 0.54.
- Fix find option order.

* Fri Apr 07 2006 Gavin Henry <ghenry[AT]suretecsystems.com> - 0.50-1
- Updated version for security fix

* Tue Feb 28 2006 Gavin Henry <ghenry[AT]suretecsystems.com> - 0.47-1
- Updated version

* Wed Sep 14 2005 Gavin Henry <ghenry[AT]suretecsystems.com> - 0.45-2
- Applied Steven Pritchard's kind patch to cleanup -
  https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=166254

* Thu Aug 18 2005 Gavin Henry <ghenry[AT]suretecsystems.com> - 0.45-1
- First build.
