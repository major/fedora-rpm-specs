# Support drivers based on what's available
%global have_cassandra 0
%global have_redis     1

Name:		perl-Apache-Session-NoSQL
Version:	0.3
Release:	6%{?dist}
Summary:	(Deprecated) NoSQL implementation of Apache::Session
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Apache-Session-NoSQL
Source0:	https://cpan.metacpan.org/modules/by-module/Apache/Apache-Session-NoSQL-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Apache::Session)
BuildRequires:	perl(Apache::Session::Generate::MD5)
BuildRequires:	perl(Apache::Session::Lock::Null)
BuildRequires:	perl(Apache::Session::Serialize::Base64)
BuildRequires:	perl(base)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(Test::More)
# Runtime
Requires:	perl(Apache::Session::NoSQL)-Driver = %{version}-%{release}

%description
NoSQL implementation of Apache::Session. Sessions are stored in NoSQL
bases, either Redis or Cassandra.

Note that this package is deprecated and Apache::Session::Browseable should
be used in preference to it.

%if %{have_cassandra}
%package -n perl-Apache-Session-Cassandra
Summary:	Cassandra driver for Apache::Session::NoSQL
BuildRequires:	perl(Net::Cassandra)
Requires:	perl-Apache-Session-NoSQL = %{version}-%{release}
Provides:	perl(Apache::Session::NoSQL)-Driver = %{version}-%{release}

%description -n perl-Apache-Session-Cassandra
%{summary}.
%endif

%if %{have_redis}
%package -n perl-Apache-Session-Redis
Summary:	Redis driver for Apache::Session::NoSQL
BuildRequires:	perl(Redis)
Requires:	perl-Apache-Session-NoSQL = %{version}-%{release}
Provides:	perl(Apache::Session::NoSQL)-Driver = %{version}-%{release}

%description -n perl-Apache-Session-Redis
%{summary}.
%endif

%prep
%setup -q -n Apache-Session-NoSQL-%{version}

%if ! %{have_cassandra} && ! %{have_redis}
%{error:At least one of Cassandra or Redis must be available}
exit 1
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes examples/
%dir %{perl_vendorlib}/Apache/
%dir %{perl_vendorlib}/Apache/Session/
%dir %{perl_vendorlib}/Apache/Session/Store/
%dir %{perl_vendorlib}/Apache/Session/Store/NoSQL/
%{perl_vendorlib}/Apache/Session/NoSQL.pm
%{perl_vendorlib}/Apache/Session/Store/NoSQL.pm
%{_mandir}/man3/Apache::Session::NoSQL.3*
%{_mandir}/man3/Apache::Session::Store::NoSQL.3*

%if %{have_cassandra}
%files -n perl-Apache-Session-Cassandra
%{perl_vendorlib}/Apache/Session/Cassandra.pm
%{perl_vendorlib}/Apache/Session/Store/NoSQL/Cassandra.pm
%{_mandir}/man3/Apache::Session::Cassandra.3*
%{_mandir}/man3/Apache::Session::Store::NoSQL::Cassandra.3*
%else
%exclude %{perl_vendorlib}/Apache/Session/Cassandra.pm
%exclude %{perl_vendorlib}/Apache/Session/Store/NoSQL/Cassandra.pm
%exclude %{_mandir}/man3/Apache::Session::Cassandra.3*
%exclude %{_mandir}/man3/Apache::Session::Store::NoSQL::Cassandra.3*
%endif

%if %{have_redis}
%files -n perl-Apache-Session-Redis
%{perl_vendorlib}/Apache/Session/Redis.pm
%{perl_vendorlib}/Apache/Session/Store/NoSQL/Redis.pm
%{_mandir}/man3/Apache::Session::Redis.3*
%{_mandir}/man3/Apache::Session::Store::NoSQL::Redis.3*
%else
%exclude %{perl_vendorlib}/Apache/Session/Redis.pm
%exclude %{perl_vendorlib}/Apache/Session/Store/NoSQL/Redis.pm
%exclude %{_mandir}/man3/Apache::Session::Redis.3*
%exclude %{_mandir}/man3/Apache::Session::Store::NoSQL::Redis.3*
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 26 2023 Paul Howarth <paul@city-fan.org> - 0.3-1
- Update to 0.3
  - Mark as deprecated

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-21
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-18
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-15
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Paul Howarth <paul@city-fan.org> - 0.2-13
- EL-5 is EOL so Redis can be assumed to be available everywhere now
- Drop now-redundant buildroot cleaning
- Simplify find command using -delete

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.2-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 23 2015 Paul Howarth <paul@city-fan.org> - 0.2-1
- Update to 0.2
  - Fix argument setting in session configuration (CPAN RT#94613)
- This release by COUDOT → update source URL

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.1-3
- Perl 5.22 rebuild

* Thu Jan 29 2015 Paul Howarth <paul@city-fan.org> - 0.1-2
- Incorporate review feedback (#1186725)
  - Ship Changes, README and examples files
  - BR: perl(base)

* Wed Jan 28 2015 Paul Howarth <paul@city-fan.org> - 0.1-1
- Initial RPM version
