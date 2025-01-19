Name:           perl-Alien-wxWidgets
Version:        0.69
Release:        29%{?dist}
Summary:        Building, finding and using wxWidgets binaries
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-wxWidgets
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBARBON/Alien-wxWidgets-%{version}.tar.gz
BuildRequires:  gcc, gcc-c++
BuildRequires:  wxGTK-devel
# A lot of stuff used by inc/My/Build/Base.pm.
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 1.50
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(strict)
BuildRequires:  perl(LWP::Protocol::https)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

# No binaries in this package
%global debug_package %{nil}

%description
"Alien::wxWidgets" can be used to detect and get configuration
settings from an installed wxWidgets.


%prep
%setup -q -n Alien-wxWidgets-%{version}


%build
export WX_CONFIG="%{_bindir}/wx-config-3.2"
%{__perl} Build.PL installdirs=vendor < /dev/null
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
chmod -R u+w $RPM_BUILD_ROOT/*


%check
./Build test


%files
%doc Changes
%{perl_vendorarch}/Alien/
%{_mandir}/man3/*.3pm*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 0.69-28
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Scott Talbert <swt@techie.net> - 0.69-23
- Rebuild with wxWidgets 3.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.69-20
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.69-17
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.69-14
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.69-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Scott Talbert <swt@techie.net> - 0.69-9
- Remove BR on wxGTK as it is about to be retired

* Mon Jul 23 2018 Tom Callaway <spot@fedoraproject.org> - 0.69-8
- add BuildRequires: gcc, gcc-c++ to generate sane configs

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.69-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.69-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.69-2
- Perl 5.26 rebuild

* Tue Apr 18 2017 Tom Callaway <spot@fedoraproject.org> - 0.69-1
- update to 0.69

* Mon Apr 17 2017 Tom Callaway <spot@fedoraproject.org> - 0.68-1
- update to 0.68
- generate and package config profiles for wxGTK v2 and v3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.67-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Tom Callaway <spot@fedoraproject.org> - 0.67-4
- spec file cleanups

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.67-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.67-2
- Perl 5.22 rebuild

* Mon Mar 30 2015 Tom Callaway <spot@fedoraproject.org> - 0.67-1
- update to 0.67

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.51-14
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.51-10
- Perl 5.18 rebuild
- Specify some dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.51-7
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.51-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.51-3
- 661697 rebuild for fixing problems with vendorach/lib

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.51-2
- rebuilt against wxGTK-2.8.11-2

* Mon May 17 2010 Petr Pisar <ppisar@redhat.com> - 0.51-1
- Version bump
- Remove perl-Alien-wxWidgets-SONAME.patch

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.44-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.44-3
- rebuild against perl 5.10.1

* Mon Aug 24 2009 Stepan Kasal <skasal@redhat.com> - 0.44-2
- fix the soname patch

* Thu Aug 20 2009 Stepan Kasal <skasal@redhat.com> - 0.44-1
- new upstream version
- add patch to remember the canonical sonames of libraries, so that
  perl-Wx runs without wxGTK-devel

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.42-1
- 0.42

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.32-4
- Rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.32-3
- Autorebuild for GCC 4.3

* Tue Feb  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.32-2
- rebuild for new perl

* Wed Nov 28 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.32-1
- Update to 0.32

* Sat Mar 31 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.31-1
- Update to 0.31.

* Fri Mar 23 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.30-1
- Update to 0.30.

* Sun Mar 18 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.29-1
- Update to 0.29.

* Wed Dec 20 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.27-1
- Update to 0.27.

* Sat Dec 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.26-1
- Update to 0.26.

* Sat Dec 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.25-2
- Rebuild (wxGTK 2.8.0).

* Sat Nov 11 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.25-1
- Update to 0.25.

* Sat Oct 21 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.24-1
- Update to 0.24.

* Thu Oct 19 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.23-1
- Update to 0.23.

* Tue Oct  3 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.22-1
- Update to 0.22.
- Avoid creation of the debuginfo package (#209180).
- Dropped patch Alien-wxWidgets-0.21-Any_wx_config.pm.patch
  (http://rt.cpan.org/Public/Bug/Display.html?id=21854).

* Sun Oct  1 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.21-3
- Patch to add /usr/lib64 to the library search path.

* Thu Sep 28 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.21-2
- This is a binary RPM (see bug #208007 comment #2).

* Sun Sep 24 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.21-1
- First build.
