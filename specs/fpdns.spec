%global gittag 20190131

Name:          fpdns
Epoch:         1
Version:       0.10.0
Release:       19.%{gittag}%{?dist}
Summary:       Fingerprint DNS servers
License:       BSD-3-Clause
URL:           https://github.com/kirei/fpdns
Source0:       https://github.com/kirei/fpdns/archive/%{gittag}/%{name}-%{version}.tar.gz
BuildArch:     noarch
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Net::DNS)
BuildRequires: make


%description 
fpdns is a program that remotely determines DNS server versions. It does this 
by sending a series of borderline DNS queries which are compared against a 
table of responses and server versions.

%prep
%autosetup -n fpdns-%{gittag}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc LICENSE
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_bindir}/fpdns

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.0-19.20190131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 26 2024 Mark McKinstry <mmckinst@fedoraproject.org> - 1:0.10.0-18.20190131
- change license to BSD-3-Clause

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.10.0-17.20190131
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.0-16.20190131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.0-15.20190131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.0-14.20190131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.0-13.20190131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.0-12.20190131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.0-11.20190131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.10.0-10.20190131
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.0-9.20190131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.0-8.20190131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1:0.10.0-7.20190131
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.10.0-6.20190131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Petr Pisar <ppisar@redhat.com> - 1:0.10.0-5.20190131
- Bump an epoch to keep ascending NEVRAs (bug #1864486)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4.20190131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.0-3.20190131
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2.20190131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Mark McKinstry <mmckinst@fedoraproject.org> - 0.10.0-1.20190131
- fix release tag

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-20190131.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.0-20190131.1
- Perl 5.30 rebuild

* Mon Apr 15 2019 Mark McKinstry <mmckinst@fedoraproject.org> - 0.10.0-20190131
- update homepage URL
- new version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-20131132.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-20131131.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.0-20131130.1
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-20131129.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-20131128.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.0-20131127.1
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-20131126.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.0-20131125.1
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-20131124.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-20131123.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.0-20131122.1
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.10.0-20131121.1
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-20131120.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan  8 2014 Mark McKinstry <mmckinst@nexcess.net> - 0.10.0-20131119.1
- upgrade to 20131119

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-20121022.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Petr Pisar <ppisar@redhat.com> - 0.10.0-20121021.1
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-20121020.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec  4 2012 Mark McKinstry <mmckinst@nexcess.net> - 0.10.0-20121010.1
- upgrade to 20121019

* Thu Jun 14 2012 Mark McKinstry <mmckinst@nexcess.net> - 0.10.0-1
- upgrade to 0.10.0 from github checked out 20120503

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.9.3-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.9.3-2
- Perl mass rebuild

* Mon Nov 22 2010 Mark McKinstry <mmckinst@nexcess.net> 0.9.3-1
- Specfile autogenerated by cpanspec 1.78.
