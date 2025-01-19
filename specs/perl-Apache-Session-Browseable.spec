Name:		perl-Apache-Session-Browseable
Version:	1.3.14
Release:	2%{?dist}
Summary:	Add index and search methods to Apache::Session
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Apache-Session-Browseable
Source0:	https://cpan.metacpan.org/modules/by-module/Apache/Apache-Session-Browseable-%{version}.tar.gz
Patch0:		Apache-Session-Browseable-1.3.6-synopsis-cafile.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build)
# Module Runtime
BuildRequires:	perl(Apache::Session)
BuildRequires:	perl(Apache::Session::Generate::MD5)
BuildRequires:	perl(Apache::Session::Lock::File)
BuildRequires:	perl(Apache::Session::Lock::Null)
BuildRequires:	perl(Apache::Session::Serialize::Base64)
BuildRequires:	perl(Apache::Session::Serialize::Storable)
BuildRequires:	perl(Apache::Session::Serialize::Sybase)
BuildRequires:	perl(Apache::Session::Store::DBI)
BuildRequires:	perl(Apache::Session::Store::File)
BuildRequires:	perl(Apache::Session::Store::Informix)
BuildRequires:	perl(Apache::Session::Store::MySQL)
BuildRequires:	perl(Apache::Session::Store::Oracle)
BuildRequires:	perl(Apache::Session::Store::Postgres)
BuildRequires:	perl(Apache::Session::Store::Sybase)
BuildRequires:	perl(AutoLoader)
BuildRequires:	perl(base)
BuildRequires:	perl(DBI)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(JSON)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Net::LDAP) >= 0.38
BuildRequires:	perl(Net::LDAP::Util)
BuildRequires:	perl(Redis)
BuildRequires:	perl(Storable)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(utf8)
BuildRequires:	perl(warnings)
# Optional Tests
BuildRequires:	perl(DBD::mysql)
BuildRequires:	perl(DBD::SQLite) > 1.19
# Dependencies
Requires:	perl(MIME::Base64)
Requires:	perl(Redis)
Requires:	perl(Storable)

%description
A virtual Apache::Session back-end providing some class methods to manipulate
all sessions and add the capability to index some fields to make re-search
faster.

%prep
%setup -q -n Apache-Session-Browseable-%{version}

# Fix certificate bundle location in SYNOPSIS
%patch -P 0

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license COPYRIGHT LICENSE
%doc Changes README.md
%{perl_vendorlib}/Apache/
%{perl_vendorlib}/auto/Apache/
%{_mandir}/man3/Apache::Session::Browseable.3*
%{_mandir}/man3/Apache::Session::Browseable::Cassandra.3*
%{_mandir}/man3/Apache::Session::Browseable::LDAP.3*
%{_mandir}/man3/Apache::Session::Browseable::MySQL.3*
%{_mandir}/man3/Apache::Session::Browseable::MySQLJSON.3*
%{_mandir}/man3/Apache::Session::Browseable::PgHstore.3*
%{_mandir}/man3/Apache::Session::Browseable::PgJSON.3*
%{_mandir}/man3/Apache::Session::Browseable::Postgres.3*
%{_mandir}/man3/Apache::Session::Browseable::SQLite.3*
%{_mandir}/man3/Apache::Session::Browseable::Store::Cassandra.3*
%{_mandir}/man3/Apache::Session::Browseable::Store::LDAP.3*
%{_mandir}/man3/Apache::Session::Browseable::Store::SQLite.3*
%{_mandir}/man3/Apache::Session::Browseable::Redis.3*
%{_mandir}/man3/Apache::Session::Browseable::Store::Redis.3*
%{_mandir}/man3/Apache::Session::Serialize::Hstore.3*
%{_mandir}/man3/Apache::Session::Serialize::JSON.3*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 19 2024 Xavier Bachelot <xavier@bachelot.org> - 1.3.14-1
- Update to 1.3.14

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul  6 2023 Paul Howarth <paul@city-fan.org> - 1.3.13-1
- Update to 1.3.13
  - Add Cassandra support via DBD::Cassandra
- Avoid use of deprecated patch syntax

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 27 2022 Paul Howarth <paul@city-fan.org> - 1.3.11-1
- Update to 1.3.11
  - Revert 1.3.10 changes
- Use SPDX-format license tag

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.10-2
- Perl 5.36 rebuild

* Wed Mar  9 2022 Paul Howarth <paul@city-fan.org> - 1.3.10-1
- Update to 1.3.10
  - Add quote for fields in INSERT query

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 10 2021 Paul Howarth <paul@city-fan.org> - 1.3.9-1
- Update to 1.3.9
  - Return number of deleted rows when called in array context
    https://gitlab.ow2.org/lemonldap-ng/lemonldap-ng/-/issues/2428
- Use %%license unconditionally

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.8-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep  7 2020 Paul Howarth <paul@city-fan.org> - 1.3.8-1
- Update to 1.3.8
  - Fix ldap+tls:// regression in 1.3.6 (GH#27)
  - Add specific error handling for old versions (GH#28)

* Fri Sep  4 2020 Paul Howarth <paul@city-fan.org> - 1.3.6-1
- Update to 1.3.6
  - Improve logs (GH#26)
  - Add ldapVerify option for SSL certificate validation (GH#25)
- Add patch to fix example certificate bundle location in SYNOPSIS to reflect
  distribution defaults

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.5-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Paul Howarth <paul@city-fan.org> - 1.3.5-1
- Update to 1.3.5
  - Update cast syntax for vanilla MySQL (GH#21)
  - Redis: doc and tests improvements (GH#23)

* Thu Nov 21 2019 Paul Howarth <paul@city-fan.org> - 1.3.4-1
- Update to 1.3.4
  - Don't stop parsing sessions when one is bad

* Fri Sep 20 2019 Paul Howarth <paul@city-fan.org> - 1.3.3-1
- Update to 1.3.3
  - LDAP: Add ldapRaw parameter (GH#20)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul  5 2019 Paul Howarth <paul@city-fan.org> - 1.3.2-1
- Update to 1.3.2
  - Allow sentinel list to be passed as a comma-delimited string (GH#19)

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.3.1-2
- Perl 5.30 rebuild

* Sat May  4 2019 Paul Howarth <paul@city-fan.org> - 1.3.1-1
- Update to 1.3.1
  - Fix typo in Oracle.pm (GH#15)
  - Postgres: Ensure that returned @fields keep their original case (GH#17)

* Fri Feb  8 2019 Paul Howarth <paul@city-fan.org> - 1.3.0-1
- Update to 1.3.0
  - Also fix PgHstore error when searchOn is used without fields

* Fri Feb  8 2019 Paul Howarth <paul@city-fan.org> - 1.2.9-1
- Update to 1.2.9
  - Use either Redis::Fast or Redis
  - Fix error when searchOn is used without fields

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.8-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct  3 2017 Paul Howarth <paul@city-fan.org> - 1.2.8-1
- Update to 1.2.8
  - Missing UTF-8 hook

* Tue Oct  3 2017 Paul Howarth <paul@city-fan.org> - 1.2.7-1
- Update to 1.2.7
  - Force UTF-8
- This release by GUIMARD → update source URL

* Wed Sep 13 2017 Paul Howarth <paul@city-fan.org> - 1.2.6-1
- Update to 1.2.6
  - Force allow_nonref option (GH#14)
- This release by COUDOT → update source URL

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.5-2
- Perl 5.26 rebuild

* Tue Apr  4 2017 Paul Howarth <paul@city-fan.org> - 1.2.5-1
- Update to 1.2.5
  - PostgreSQL "hstore" and "json" support
  - Add "deleteIfLowerThan" method
- Drop EL-5 support
  - Drop Group: and BuildRoot: tags
  - No longer need to clean buildroot in %%install
  - Support Redis unconditionally
  - Always run DBD::SQLite test

* Sun Feb 19 2017 Paul Howarth <paul@city-fan.org> - 1.2.4-1
- Update to 1.2.4
  - Fix incorrect logic for old database formats (GH#11)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jun 12 2016 Paul Howarth <paul@city-fan.org> - 1.2.3-1
- Update to 1.2.3
  - Replace "/" for Windows

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.2-2
- Perl 5.24 rebuild

* Sat Apr  2 2016 Paul Howarth <paul@city-fan.org> - 1.2.2-1
- Update to 1.2.2
  - Manage old session format for databases

* Thu Mar 10 2016 Paul Howarth <paul@city-fan.org> - 1.2.1-1
- Update to 1.2.1
  - Add an empty Browseable.pm due to new Pause restrictions

* Wed Mar  9 2016 Paul Howarth <paul@city-fan.org> - 1.2-1
- Update to 1.2
  - Replace MD5 by SHA256
  - Replace serialization by JSON
- This release by GUIMARD → update source URL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jun 20 2015 Paul Howarth <paul@city-fan.org> - 1.1-1
- Update to 1.1
- This release by COUDOT → update source URL

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.2-3
- Perl 5.22 rebuild

* Tue Jan 20 2015 Paul Howarth <paul@city-fan.org> - 1.0.2-2
- Include upstream docs (#1182960)

* Fri Jan 16 2015 Paul Howarth <paul@city-fan.org> - 1.0.2-1
- Initial RPM package
