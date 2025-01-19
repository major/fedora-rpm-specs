Name:           perl-Astro-FITS-CFITSIO
Version:        1.18
Release:        7%{?dist}
Summary:        Perl extension for using the cfitsio library
# tarball m51 doesn't state license https://rt.cpan.org/Public/Bug/Display.html?id=66226
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Astro-FITS-CFITSIO
Source0:        https://cpan.metacpan.org/authors/id/P/PR/PRATZLAFF/Astro-FITS-CFITSIO-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Alien::Base::Wrapper)
BuildRequires:  perl(Alien::CFITSIO)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  cfitsio-devel

%description
Perl interface to William Pence's cfitsio subroutine library. For more
information on cfitsio, see http://heasarc.gsfc.nasa.gov/fitsio.

%prep
%setup -q -n Astro-FITS-CFITSIO-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS -I%{_includedir}/cfitsio"
%make_build

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
#works locally
#make test

%files
%license README
%doc ChangeLog NOTES README TODO examples
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Astro*
%{_mandir}/man3/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 1.18-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.18-4
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 02 2023 Orion Poplawski <orion@nwra.com> - 1.18-1
- Update to 1.18

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-2
- Perl 5.38 rebuild

* Tue Apr 18 2023 Orion Poplawski <orion@nwra.com> - 1.17-1
- Update to 1.17

* Sun Jan 22 2023 Orion Poplawski <orion@nwra.com> - 1.16-1
- Update to 1.16

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Maxwell G <gotmax@e.email> - 1.15-9
- Rebuild for cfitsio 4.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-7
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-4
- Perl 5.34 rebuild

* Wed Feb 03 2021 Orion Poplawski <orion@nwra.com> - 1.15-3
- Rebuild for cfitsio 3.490

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 22 2020 Orion Poplawski <orion@nwra.com> - 1.15-1
- Update to 1.15

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Orion Poplawski <orion@nwra.com> - 1.14-1
- Update to 1.14

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-6
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.12-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 6 2018 Orion Poplawski <orion@nwra.com> - 1.12-1
- Update to 1.12

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-10
- Perl 5.28 rebuild

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 1.11-9
- rebuilt for cfitsio 3.450

* Thu Mar  1 2018 Florian Weimer <fweimer@redhat.com> - 1.11-8
- Rebuild with new redhat-rpm-config/perl build flags

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 1.11-7
- rebuilt for cfitsio 3.420 (so version bump)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Orion Poplawski <orion@cora.nwra.com> - 1.11-1
- Update to 1.11

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-11
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-8
- Perl 5.22 rebuild

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-7
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 08 2014 Orion Poplawski <orion@cora.nwra.com> - 1.10-4
- Rebuild for cfitsio 3.360

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.10-2
- Perl 5.18 rebuild

* Thu Jul 11 2013 Orion Poplawski <orion@cora.nwra.com> - 1.10-1
- Update to 1.10, build with cfitsio 3.350

* Sat Mar 23 2013 Orion Poplawski <orion@cora.nwra.com> - 1.09-3
- Add BR perl(Carp)

* Fri Mar 22 2013 Orion Poplawski <orion@cora.nwra.com> - 1.09-2
- Rebuild with cfitsio 3.340

* Wed Mar 20 2013 Orion Poplawski <orion@cora.nwra.com> - 1.09-1
- Update to 1.09, build with cfitsio 3.330

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.08-2
- Perl 5.16 rebuild

* Wed Apr 25 2012 Orion Poplawski <orion@cora.nwra.com> - 1.08-1
- Update to 1.08, build with cfitsio 3.300

* Fri Jan 6 2012 Orion Poplawski <orion@cora.nwra.com> - 1.07-1
- Update to 1.07, build with cfitsio 3.290

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.06-1
- update to 1.06, switch off tests (working only locally), clean spec
- link to license problem

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.05-11
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.05-9
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.05-8
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.05-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.05-4
Rebuild for new perl

* Sat Feb  9 2008 Orion Poplawski <orion@cora.nwra.com> 1.05-3
- Rebuild for gcc 3.4

* Thu Aug 23 2007 Orion Poplawski <orion@cora.nwra.com> 1.05-2
- Update license tag to GPL+ or Artistic
- Rebuild for BuildID

* Tue Jul 31 2007 Orion Poplawski 1.05-1
- Specfile autogenerated by cpanspec 1.73.
