Name:           perl-Pod-PseudoPod
Version:        0.19
Release:        17%{?dist}
Summary:        Framework for extending the POD tags for book manuscripts
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-PseudoPod
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/Pod-PseudoPod-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Simple) >= 3.02
BuildRequires:  perl(Test::More)
Requires:       perl(Pod::Simple) >= 3.02


%description
PseudoPod is an extended set of Pod tags used for book manuscripts.
Standard Pod doesn't have all the markup options you need to mark up files
for publishing production. PseudoPod adds a few extra tags for footnotes,
tables, sidebars, etc. For further information see Pod::PseudoPod::Tutorial.


%prep
%setup -q -n Pod-PseudoPod-%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
%{__rm} -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

# Added to remove the waring messages from rpmlint
%{_fixperms} $RPM_BUILD_ROOT/*


%check
./Build test



%files
%doc Changes LICENSE README Todo
%{perl_vendorlib}/Pod/PseudoPod.pm
%{perl_vendorlib}/Pod/PseudoPod
%{_mandir}/man3/*
%{_bindir}/ppod2docbook
%{_bindir}/ppod2txt
%{_bindir}/ppodchecker
%{_bindir}/ppod2html


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.19-16
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-9
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-6
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 04 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.19-1
- update to 0.19

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-16
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-13
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-10
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-5
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-4
- Perl 5.20 rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.18-1
- 0.18 bump

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.16-12
- Perl 5.18 rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.16-9
- Perl 5.16 rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.16-7
- Perl mass rebuild

* Thu Jan 27 2011 Gerd Pokorra <gp@zimt.uni-siegen.de> - 0.16-5
- rebuild to fix broken perl dependencies

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-4
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Dec 12 2010 Iain Arnell <iarnell@gmail.com> 0.16-3
- doesn't require perl(Test::More)

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-2
- Mass rebuild with perl-5.12.0

* Mon May 03 2010 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.16-1
- update to 0.16

* Mon Nov 30 2009 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.15-1
- add perl_vendorlib files more explicit
- changed Summary-, Source0- and License-lines
- add ppod*-binaries to files-section
- Specfile autogenerated by cpanspec 1.78.
