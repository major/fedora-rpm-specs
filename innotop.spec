Name:           innotop
Version:        1.13.0
Release:        9%{?dist}
Summary:        A MySQL and InnoDB monitor program
BuildArch:      noarch
License:        GPLv2+ or Artistic
URL:            https://github.com/innotop/innotop
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

%if 0%{?el5}
%endif

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(DBI)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(sigtrap)
BuildRequires:  perl(strict)
# Term::ANSIColor not used at tests
BuildRequires:  perl(Term::ReadKey)
# Term::ReadLine not used at tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)

Requires:       perl(DBD::mysql)
Requires:       perl(Term::ANSIColor)
Requires:       perl(Term::ReadLine)

%description
innotop connects to a MySQL database server and retrieves information from it,
then displays it in a manner similar to the UNIX top program.  innotop uses
the data from SHOW VARIABLES, SHOW GLOBAL STATUS, SHOW FULL PROCESSLIST, and
SHOW ENGINE INNODB STATUS, among other things.

%prep
%autosetup

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

%check
make test

%files
%license COPYING
%doc README.md
%{_bindir}/innotop
%{_mandir}/man1/innotop.1*

%changelog
* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.13.0-5
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.13.0-2
- Perl 5.34 rebuild

* Wed Apr 07 2021 Luis Bazan <lbazan@fedoraproject.org> - 1.13.0-1
- New upstream version

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.12.0-7
- Perl 5.32 rebuild

* Fri Mar 20 2020 Petr Pisar <ppisar@redhat.com> - 1.12.0-6
- Specify all dependencies

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.12.0-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Luis Bazan <lbazan@fedoraproject.org> - 1.12.0-1
- New upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.11.4-6
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.11.4-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.4-1
- Update to 1.11.4

* Wed Jun 15 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.11.1-1
- New upstream release

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.10.0-0.5.81da83f
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-0.4.81da83f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.0-0.3.81da83f
- Add patch for MariaDB 10.1 and 10.2 compatibility

* Fri Jul 31 2015 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.0-0.2.4131ed5
- Improve dependencies

* Sun Jul 26 2015 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.10.0-0.1.4131ed5
- Bump to current dev version since a lot of updates have been made since last release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.9.1-9
- Perl 5.22 rebuild

* Sun Sep 28 2014 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.9.1-8
- Add patch innotop-fix-hostname-width-in-querylist made by me (already got in touch with upstream)
- Add patch innotop-fix-host-in-transactions made by me (already got in touch with upstream)

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.9.1-7
- Perl 5.20 rebuild

* Thu Aug 21 2014 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.9.1-6
- Solving last pieces of mess

* Wed Aug 20 2014 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.9.1-5
- Fix bogous date in changelog
- Fix mixture of spaces and tabs

* Wed Aug 20 2014 Fabio Alessandro Locati <fale@fedoraproject.org> - 1.9.1-4
- Fix previously bad applied patch

* Mon Aug 11 2014 Luis Bazan <lbazan@fedoraproject.org> - 1.9.1-3
- fix changelog

* Mon Aug 11 2014 Luis Bazan <lbazan@fedoraproject.org> - 1.9.1-2
- add patch fix BZ# 1128704

* Wed Jan 15 2014 Eduardo Echeverria <echevemaster@gmail.com> - 1.9.1-1
- Update to 1.9.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.9.0-4
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 05 2012 Luis Bazan <lbazan@fedoraproject.org> 1.9.0-2
- Add BuildRequires

* Fri Oct 05 2012 Eduardo Echeverria <echevemaster@fedoraproject.org> 1.9.0-3
- Add BuildRequires perl_Time_HiRes

* Fri Oct 05 2012 Eduardo Echeverria <echevemaster@fedoraproject.org> 1.9.0-2
- Add BuildRequires

* Fri Sep 21 2012 Luis Bazan <lbazan@fedoraproject.org> 1.9.0-1
- New Upstream version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Luis Bazan <lbazan@fedoraproject.org> - 1.8.1-4
- back to original state man3 and man1

* Tue Jul 10 2012 Luis Bazan <lbazan@fedoraproject.org> - 1.8.1-3
- remove man3

* Tue Jul 10 2012 Luis Bazan <lbazan@fedoraproject.org> - 1.8.1-2
- Change man3 and man1

* Mon Jul 09 2012 Luis Bazán <lbazan@fedoraproject.org> - 1.8.1-1
- New Upstream Version 1.8.1

* Sun Jun 17 2012 Petr Pisar <ppisar@redhat.com> - 1.6.0-10
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.6.0-8
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.6.0-6
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.6.0-5
- rebuild against perl 5.10.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6.0-2
Rebuild for new perl

* Tue Jan 29 2008 Michael Fleming <mfleming+rpm@enlartenment.com> 1.6.0-1
- New upstream release.
- Update License

* Sun Jul 29 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 1.4.3-2
- New upstream release.
- Remove README from docs (removed upstream)

* Fri Jun 29 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 1.4.2-4
- First import into Fedora

* Sun Jun 17 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 1.4.2-3.mf
- Fix BuildRequires.
- Explict Requires for DBD::mysql and Term::Readkey as RPM is not smart enough
  to pick them up on it's own.

* Fri May 4 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 1.4.2-1.mf
- New upstream release

* Fri Apr 6 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 1.4.1-1.mf
- New upstream release

* Mon Mar 5 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 1.4.0-1.mf
- New stable upstream release

* Mon Feb 5 2007 Michael Fleming <mfleming+rpm@enlartenment.com> 1.3.5-1.mf
- Initial release
