Name:           perl-SNMP-Info
%global cpan_version 3.972002
Version:        3.972.2
Release:        2%{?dist}
Summary:        Object Oriented Perl5 Interface to Network devices and MIBs through SNMP
License:        BSD-3-Clause
URL:            https://metacpan.org/release/SNMP-Info
Source0:        https://cpan.metacpan.org/authors/id/O/OL/OLIVER/SNMP-Info-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# Class::ISA not used at tests
# constant not used at tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BigInt)
# Module::Info not used at tests
# Module::Load not used at tests
# mro not used at tests
BuildRequires:  perl(NetAddr::IP) >= 4.068
BuildRequires:  perl(NetAddr::IP::Lite)
# PPI not used at tests
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(SNMP)
BuildRequires:  perl(Socket)
# Tests:
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests:
# File::Find not used
# Test::Distribution not used

Requires:       perl(mro)
Requires:       perl(NetAddr::IP) >= 4.068

%description
SNMP::Info gives an object oriented interface to information obtained
through SNMP.

%prep
%setup -q -n SNMP-Info-%{cpan_version}
find contrib -type f | xargs chmod -x 

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes contrib README
%{perl_vendorlib}/SNMP*
%{_mandir}/man3/SNMP::Info*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.972.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 05 2024 Jitka Plesnikova <jplesnik@redhat.com> - 3.972.2-1
- 3.972002 bump (rhbz#2322558)

* Mon Sep 16 2024 Jitka Plesnikova <jplesnik@redhat.com> - 3.972.0-1
- 3.972000 bump (rhbz#2312047)

* Tue Sep 03 2024 Jitka Plesnikova <jplesnik@redhat.com> - 3.971.0-1
- 3.971000 bump (rhbz#2309125)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.970.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 04 2024 Jitka Plesnikova <jplesnik@redhat.com> - 3.970.1-1
- 3.970001 bump (rhbz#2266126)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.95-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 04 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.95-1
- 3.95 bump (rhbz#2237016)

* Tue Jul 25 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.94-1
- 3.94 bump (rhbz#2225475)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.93-1
- 3.93 bump (rhbz#2223015)

* Thu Apr 27 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.92-1
- 3.92 bump; Update license to SPDX format

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.89-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.89-1
- 3.89 bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.82-2
- Perl 5.36 rebuild

* Thu May 19 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.82-1
- 3.82 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 13 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.78-1
- 3.78 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.71-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.71-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.71-1
- 3.71 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.70-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.70-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.70-1
- 3.70 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.68-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.68-2
- Perl 5.30 rebuild

* Mon May 06 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.68-1
- 3.68 bump

* Thu Apr 04 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.66-1
- 3.66 bump

* Thu Mar 07 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.65-1
- 3.65 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.64-1
- 3.64 bump

* Thu Nov 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.63-1
- 3.63 bump

* Thu Nov 08 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.62-1
- 3.62 bump

* Tue Aug 07 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.61-1
- 3.61 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.54-2
- Perl 5.28 rebuild

* Thu Apr 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.54-1
- 3.54 bump

* Fri Mar 02 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.47-1
- 3.47 bump

* Tue Feb 06 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.43-1
- 3.43 bump

* Thu Jan 04 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.39-1
- 3.39 bump

* Tue Oct 24 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.38-1
- 3.38 bump

* Mon Aug 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.37-1
- 3.37 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.34-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.34-1
- 3.34 bump

* Tue Jun 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.33-1
- 3.33 bump

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.31-2
- Perl 5.24 rebuild

* Tue Mar 22 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.31-1
- 3.31 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.30-1
- 3.30 bump

* Thu Jun 25 2015 Petr Pisar <ppisar@redhat.com> - 3.28-1
- 3.28 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.24-2
- Perl 5.22 rebuild

* Sun Feb 08 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.24-1
- Update to 3.24 (RHBZ #1190423)

* Wed Dec 10 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.23-1
- Update to 3.23 (RHBZ #1172631)

* Sat Dec 06 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.22-1
- Update to 3.22 (RHBZ #1171044)
- Use %%license macro
- Remove explicit BuildRoot definition
- Remove "rm -rf buildroot" cruft

* Wed Sep 10 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.20-1
- Update to 3.20 (RHBZ #1125871)

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.18-2
- Perl 5.20 rebuild

* Sun Jul 06 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.18-1
- Update to 3.18 (RHBZ #1116607)

* Mon Jun 30 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.17-1
- Update to 3.17 (RHBZ #1114330)

* Wed Jun 11 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.15-1
- Update to 3.15 (RHBZ #1105811)
- rm %%defattr

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 03 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.13-1
- Update to 3.13 (RHBZ #1082309)

* Tue Feb 11 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.12-1
- Update to 3.12 (RHBZ #1063776)

* Wed Feb 05 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.11-1
- Update to 3.11 (RHBZ #1059639)

* Mon Dec 23 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.10-1
- Update to 3.10 (RHBZ #1044434)

* Wed Oct 23 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.08-1
- Update to 3.08 (RHBZ #1022681)

* Thu Oct 03 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.07-1
- Update to 3.07

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 2.11-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 26 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.11-1
- upgrade to 2.11

* Thu Dec 06 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 2.09-1
- upgrade to 2.09

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.06-3
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 06 2011 <walt@gouldfamily.org> 2.06-1
- upgrade to 2.06
* Thu Jun 18 2009 <walt@gouldfamily.org> 2.01-1
- upgrade to 2.01
