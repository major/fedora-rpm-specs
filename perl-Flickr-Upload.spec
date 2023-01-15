Name:           perl-Flickr-Upload
Epoch:          2
Version:        1.6
Release:        19%{?dist}
Summary:        Flickr.com upload module and script
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Flickr-Upload
Source0:        https://cpan.metacpan.org/authors/id/S/SS/SSEVERIN/Flickr-Upload-%{version}.tar.gz
Patch0:         perl-Flickr-Upload-remotetests.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Flickr::API) >= 1.09
# Getopt::Long 1 not used at tests
BuildRequires:  perl(HTTP::Request::Common) >= 1
BuildRequires:  perl(LWP::UserAgent) >= 1
BuildRequires:  perl(Net::OAuth) >= 0.28
# Pod::Usage >= 1 not used at tests
BuildRequires:  perl(strict)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::Simple) >= 2
# Optional run-time:
# Term::ProgressBar 2.00 not used at tests
# Tests:
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
Requires:       perl(Flickr::API) >= 1.09
Requires:       perl(Getopt::Long) >= 1
Requires:       perl(HTTP::Request::Common) >= 1
Requires:       perl(LWP::UserAgent) >= 1
Requires:       perl(Net::OAuth) >= 0.28
Requires:       perl(Pod::Usage) >= 1
Requires:       perl(XML::Simple) >= 2
# Optional run-time:
Requires:       perl(Term::ProgressBar) >= 2.00

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Flickr::API|Getopt::Long|HTTP::Request::Common|LWP::UserAgent|Pod::Usage|XML::Simple|Net::OAuth)\\)$

%description
Module and script for uploading images to flickr.com web gallery.

%prep
%setup -q -n Flickr-Upload-%{version}
%patch0 -p0 -b .remotetests

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/flickr_upload
%{_mandir}/man1/flickr_upload.1.gz


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.6-18
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.6-15
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.6-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.6-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.6-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.6-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2:1.6-1
- 1.6 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.51-2
- Perl 5.24 rebuild

* Wed Mar 23 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.51-1
- 1.51 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 14 2015 Petr Pisar <ppisar@redhat.com> - 1:1.5-1
- 1.5 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.32-16
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.32-15
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.32-12
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 1.32-9
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.32-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.32-5
- 661697 rebuild for fixing problems with vendorach/lib

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.32-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.32-3
- rebuild against perl 5.10.1

* Wed Aug 12 2009 Michal Ingeli <mi@v3.sk> 1.32-2
- Added missing buildrequire for Test::Simple
- Removed test that interact with api.flickr.com

* Sun Jun 21 2009 Michal Ingeli <mi@v3.sk> 1.32-1
- Specfile autogenerated by cpanspec 1.77.
