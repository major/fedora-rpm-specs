Name:           perl-Apache-Session
Version:        1.94
Release:        14%{?dist}
Summary:        Persistence framework for session data
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Apache-Session
Source0:        https://cpan.metacpan.org/modules/by-module/Apache/Apache-Session-%{version}.tar.gz
# https://bugzilla.redhat.com/bugzilla/attachment.cgi?id=118577, from Chris Grau
Patch0:         Apache-Session-mp2.patch
BuildArch:      noarch
# Build
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI::Cookie)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Semaphore)
BuildRequires:  perl(IPC::SysV)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(vars)
# mod_perl interaction
# mod_perl won't work properly in recent Fedora/EL releases (https://bugzilla.redhat.com/show_bug.cgi?id=2030601#c2)
%if (0%{?rhel} && 0%{?rhel} <= 8) || (0%{?fedora} && 0%{?fedora} <= 35)
BuildRequires:  perl(Apache)
BuildRequires:  perl(Apache2::RequestUtil)
%endif
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBD::mysql)
# Not available in Fedora yet; tests skipped automatically
%if 0
BuildRequires:  perl(DBD::Oracle)
%endif
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(File::Temp)
%if 0%{?fedora}
BuildRequires:  perl(Test::Database)
%endif
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.41

%description
Apache::Session is a persistence framework that is particularly useful for
tracking session data between httpd requests. Apache::Session is designed
to work with Apache and mod_perl, but it should work under CGI and other
web servers, and it also works outside of a web server altogether.

%prep
%setup -q -n Apache-Session-%{version}
find -type f -exec perl -pi -e 's/\r//g' {} +

# Workaround for mod_perl 2.x compatibility (CPAN RT#14504)
%patch -P0 -p1

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc CHANGES Contributing.txt README TODO
%doc eg/
%{perl_vendorlib}/Apache/
%{_mandir}/man3/Apache::Session*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.94-7
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan  7 2022 Paul Howarth <paul@city-fan.org> - 1.94-5
- Don't pull in modules from mod_perl as it will not work with the default
  httpd setup in recent Fedora/EL releases and will not be available in EL-9
  (https://bugzilla.redhat.com/show_bug.cgi?id=2030601#c2)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.94-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 19 2020 Paul Howarth <paul@city-fan.org> - 1.94-1
- Update to 1.94
  - Better error if LockDataSource is missing in Apache::Session::Lock::MySQL

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.93-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.93-17
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.93-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.93-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.93-14
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.93-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.93-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.93-11
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.93-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.93-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.93-8
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.93-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.93-6
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.93-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.93-3
- Perl 5.22 rebuild

* Thu Nov 27 2014 Paul Howarth <paul@city-fan.org> - 1.93-2
- Exclude Test::Database from EPEL builds as it's not available there

* Tue Nov 11 2014 Petr Šabata <contyk@redhat.com> - 1.93-1
- 1.93 bump
- Modernize spec

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.89-12
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.89-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.89-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 1.89-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.89-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.89-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 16 2012 Petr Pisar <ppisar@redhat.com> - 1.89-6
- Perl 5.16 rebuild

* Thu Mar 22 2012 Tom Callaway <spot@fedoraproject.org> - 1.89-5
- fix missing BR

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.89-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.89-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.89-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Steven Pritchard <steve@kspei.com> 1.89-1
- Update to 1.89.
- Build with Module::Build.
- Add examples in eg/.
- Convert everything to Unix line endings and patch afterwards.

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.88-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.88-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.88-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 04 2009 Steven Pritchard <steve@kspei.com> 1.88-1
- Update to 1.88.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.87-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Steven Pritchard <steve@kspei.com> 1.87-1
- Update to 1.87.
- Explicitly BR Test::More.
- Get rid of DOS line endings in Contributing.txt.

* Tue Feb 05 2008 Steven Pritchard <steve@kspei.com> 1.86-1
- Update to 1.86.

* Sat Feb 02 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.85-2
- rebuild for new perl

* Mon Jan 07 2008 Steven Pritchard <steve@kspei.com> 1.85-1
- Update to 1.85.
- BR Test::Pod.

* Mon Oct 15 2007 Steven Pritchard <steve@kspei.com> 1.84-1
- Update to 1.84.
- License changed to GPL+ or Artistic.
- Package Contributing.txt doc.

* Mon May 28 2007 Steven Pritchard <steve@kspei.com> 1.83-1
- Update to 1.83.

* Wed Apr 18 2007 Steven Pritchard <steve@kspei.com> 1.82-2
- BR ExtUtils::MakeMaker.

* Thu Feb 22 2007 Steven Pritchard <steve@kspei.com> 1.82-1
- Update to 1.82.
- Use fixperms macro instead of our own chmod incantation.
- Minor spec cleanup to more closely resemble current cpanspec output.

* Sat Sep 16 2006 Steven Pritchard <steve@kspei.com> 1.81-2
- Fix find option order.

* Wed May 24 2006 Steven Pritchard <steve@kspei.com> 1.81-1
- Update to 1.81.

* Tue Apr 11 2006 Steven Pritchard <steve@kspei.com> 1.80-1
- Update to 1.80.
- Spec cleanup.

* Thu Sep 08 2005 Steven Pritchard <steve@kspei.com> 1.6-2
- Add patch for mod_perl2 compatibility from Chris Grau (#167753, comment #3).
- Re-enable "make test".

* Wed Aug 31 2005 Steven Pritchard <steve@kspei.com> 1.6-1
- Specfile autogenerated.
