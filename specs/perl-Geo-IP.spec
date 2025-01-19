Name:             perl-Geo-IP
Summary:          Efficient Perl bindings for the GeoIP location database
Version:          1.51
Release:          26%{?dist}
URL:              https://metacpan.org/release/Geo-IP
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:          GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:          https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/Geo-IP-%{version}.tar.gz

BuildRequires:    findutils
BuildRequires:    gcc
BuildRequires:    make
BuildRequires:    sed
BuildRequires:    GeoIP-devel
BuildRequires:    perl-devel
BuildRequires:    perl-generators
BuildRequires:    perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:    perl(Test::More)


%{?perl_default_filter}

%description
This package contains Perl bindings for the GeoIP IP/host-name to
country/location/organization database.

This package requires Maxmind's GeoIP libraries but is often faster than other,
similar modules.


%prep
%setup -q -n Geo-IP-%{version}
sed -i -e '1s,#!.*perl,#!%{__perl},' example/netspeed.pl example/netspeedcell.pl


%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1
make %{?_smp_mflags}
# Avoid uneeded dependencies in the docs.
find example/ -type f | xargs chmod -x


%install
make pure_install DESTDIR=%{buildroot}
chmod -R u+w %{buildroot}/*


%check
make test


%files
%doc Changes example
%{perl_vendorarch}/Geo
%{perl_vendorarch}/auto/Geo
%{_mandir}/man3/Geo::IP*.3*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 1.51-25
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-23
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-19
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-16
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-13
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-10
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.51-4
- Perl 5.28 rebuild

* Sun Mar 11 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 1.51-3
- Add missing build-requirements

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 1.51-1
- Update to 1.51

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.50-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.50-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 23 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.50-2
- Use inline sed instead of patch

* Sat Jul 23 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 1.50-1
- Update to 1.50
- Pass NO_PACKLIST to Makefile.PL
- Use DESTDIR instead of PERL_INSTALL_ROOT

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.45-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.45-2
- Perl 5.22 rebuild

* Sun Oct 05 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.45-1
- Update to 1.45
- Drop Patch0 (no longer applies)

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.43-2
- Perl 5.20 rebuild

* Sun Aug 31 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.43-1
- Update to 1.43

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.42-5
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.42-1
- 1.42 bump

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.40-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 24 2012 Mathieu Bridon <bochecha@fedoraproject.org> - 1.40-1
- Update to latest upstream release:
  http://cpansearch.perl.org/src/BORISZ/Geo-IP-1.40/Changes

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.38-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.38-9
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.38-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.38-7
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.38-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.38-5
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.38-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.38-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Michael Fleming <mfleming+rpm@thatfleminggent.com> 1.38-1
- New upstream update (fixes some segfaults and .au timezone breakage)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Michael Fleming <mfleming+rpm@enlartenment.com> 1.36-1
- New upstream update

* Thu Aug 28 2008 Michael Fleming <mfleming+rpm@enlartenment.com> 1.34-1
- New upstream update
- Source0 updated (new upstream maintainer)

* Sun Apr 13 2008 Michael Fleming <mfleming+rpm@enlartenment.com> 1.31-1
- New upstream update

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.30-3
- Rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.30-2
- Autorebuild for GCC 4.3

* Mon Jan 28 2008 Michael Fleming <mfleming+rpm@enlartenment.com> 1.30-1
- Update to 1.30. This pulls in much of the PurePerl module for those
  using it (via third party repositories)

* Mon Sep 3 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 1.28-4
- Fix %%patch invocation to help avoid a bogus interpreter issue
- First build for Extras

* Sun Aug 26 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 1.28-3
- Actually apply the patch :-)
- Apply consistency in macro usage
- Remove explicit GeoIP dependency as it should be pulled in automagically
- Patch to example/netspeed to avoid bogus interpreter
- Update License to match current Fedora guidelines.

* Fri Jul 20 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 1.28-2
- Patch out mysterious and ephemeral test failure

* Sun Jul 8 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 1.28-1
- Update to 1.28

* Sun Jun 17 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 1.27-4.mf
- New URLs
- Fix MakeMaker build requirement
- Include test suite check
- Add examples directory in documentation

* Sat Nov 4 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 1.27-3.mf
- Fix version tag to go with my conventions
- Bump for FC6

* Sun Feb 19 2006 Michael Fleming <mfleming+rpm@enlartenment.com> 1.27-2
- Spin a version for Extras, removing the braindamage from my previous
  releases.

* Fri Sep 9 2005 mfleming@enlartenment.com - 1.27-1.fc4.mf
- 1.27

* Wed Aug 3 2005 mfleming@enlartenment.com - 1.26-2.fc4.mf
- Rebuilt against new geoip version

* Sun Jun 12 2005 mfleming@enlartenment.com - 1.26-1.fc4.mf
- Initial release

