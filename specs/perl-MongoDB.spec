# Perform tests that use a MongoDB server
%if !(0%{?fedora} < 30)
%bcond_with perl_MongoDB_enables_server_test
%else
%bcond_without perl_MongoDB_enables_server_test
%endif

Name:           perl-MongoDB
Version:        2.2.2
Release:        14%{?dist}
Summary:        MongoDB driver for Perl
## Installed:
# lib/MongoDB/_Link.pm:             Apache-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
# Other files:                      Apache-2.0
## Not used:
# inc/CheckJiraInChanges.pm:        Apache-2.0
# inc/ExtUtils/HasCompiler.pm:      GPL-1.0-or-later OR Artistic-1.0-Perl
License:        Apache-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/MongoDB
Source0:        https://cpan.metacpan.org/authors/id/M/MO/MONGODB/MongoDB-v%{version}.tar.gz
# Revert "localhost is IPv4 only" <https://jira.mongodb.org/browse/PERL-715>
Patch0:         MongoDB-v2.2.0-Revert-PERL-715-Force-localhost-to-connect-via-IPv4.patch
# Remove useless dependency on ExtUtils::HasCompiler
Patch1:         MongoDB-v2.0.0-Remove-build-dependency-on-ExtUtils-HasCompiler.patch
# Skip tests on an unreachable server immediately
Patch2:         MongoDB-v2.2.0-Disable-retrying-connect-in-tests.patch
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(warnings)
# Runtime:
# Authen::SASL::SASLprep not used at tests
# Authen::SCRAM::Client 0.011 not used at tests
BuildRequires:  perl(boolean) >= 0.25
BuildRequires:  perl(BSON) >= 1.12.0
BuildRequires:  perl(BSON::Bytes)
BuildRequires:  perl(BSON::Code)
BuildRequires:  perl(BSON::DBRef)
BuildRequires:  perl(BSON::OID)
BuildRequires:  perl(BSON::Raw)
BuildRequires:  perl(BSON::Regex)
BuildRequires:  perl(BSON::Time)
BuildRequires:  perl(BSON::Timestamp)
BuildRequires:  perl(BSON::Types)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Socket)
# Prefer IO::Socket::IP over IO::Socket::INET
BuildRequires:  perl(IO::Socket::IP) >= 0.32
# IO::Socket::SSL 1.42 not used at tests
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Moo) >= 2
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(namespace::clean)
# Net::DNS not used at tests
# Net::SSLeay 1.49 not used at tests
BuildRequires:  perl(overload)
# re used only with perl 5.10.0
BuildRequires:  perl(Safe::Isa) >= 1.000007
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Sub::Defer)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Type::Library)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(UUID::URandom)
BuildRequires:  perl(version)
# Optional runtime:
# Authen::SASL not used at tests
# Mozilla::CA no used at tests
# Tests only:
%if %{with perl_MongoDB_enables_server_test}
BuildRequires:  mongodb-server
%endif
BuildRequires:  perl(BSON::Decimal128) >= 1
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(JSON::MaybeXS)
# Log::Any::Adapter used only if MONGOVERBOSE environment variable is true
BuildRequires:  perl(Path::Tiny) >= 0.058
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Deep) >= 0.111
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(utf8)
# Optional tests:
# CPAN::Meta not useful
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(JSON::Tiny)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Test::Harness) >= 3.31
BuildRequires:  perl(Time::Moment) >= 0.22
BuildRequires:  perl(Types::Serialiser)
Suggests:       perl(Authen::SASL)
Requires:       perl(Authen::SASL::SASLprep)
Requires:       perl(Authen::SCRAM::Client) >= 0.011
Requires:       perl(BSON) >= 1.12.0
Requires:       perl(BSON::Code)
Requires:       perl(BSON::DBRef)
Requires:       perl(BSON::Regex)
# Prefer IO::Socket::IP over IO::Socket::INET
Requires:       perl(IO::Socket::IP) >= 0.32
Requires:       perl(IO::Socket::SSL) >= 1.42
Requires:       perl(Moo) >= 2
# Hard-require Mozilla::CA to becase we hard-require IO::Socket::SSL
Requires:       perl(Mozilla::CA)
Requires:       perl(Net::DNS)
Requires:       perl(Net::SSLeay) >= 1.49

# Mongodb must run on a 32-bit little-endian or 64-bit any-endian CPU
# (see bug #630898)
ExcludeArch:    ppc %{sparc} s390

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((boolean|Moo)\\)$
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(BSON\\)

%description
This is a Perl client for accessing MongoDB servers.

Upstream claims it will drop support for this code on 2020-08-13.

%prep
%autosetup -p1 -n MongoDB-v%{version}
# Remove bundled modules
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
%if %{with perl_MongoDB_enables_server_test}
mkdir test_db
mongod --fork --logpath $PWD/mongod.log --pidfilepath $PWD/mongod.pid \
    --dbpath $PWD/test_db/ --smallfiles || test_rc=$?
if [ -n "$test_rc" ]; then
    printf "Error: Could not start mongod server\n"
    cat mongod.log
    exit 1
fi
unset MONGOD MONGOVERBOSE TEST_MONGO_SOCKET_HOST
export FAILPOINT_TESTING=1
%else
export FAILPOINT_TESTING=0
%endif
make test || test_rc=$?
%if %{with perl_MongoDB_enables_server_test}
kill `cat mongod.pid`
cat mongod.log
%endif
exit $test_rc

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README
%{perl_vendorlib}/MongoDB
%{perl_vendorlib}/MongoDB.pm
%{_mandir}/man3/MongoDB.*
%{_mandir}/man3/MongoDB::*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 02 2024 Petr Pisar <ppisar@redhat.com> - 2.2.2-13
- Modernize a spec file

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.2-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.2-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Petr Pisar <ppisar@redhat.com> - 2.2.2-1
- 2.2.2 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.2.1-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Petr Pisar <ppisar@redhat.com> - 2.2.1-1
- 2.2.1 bump

* Wed Aug 14 2019 Petr Pisar <ppisar@redhat.com> - 2.2.0-1
- 2.2.0 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.0.3-2
- Perl 5.30 rebuild

* Fri Feb 08 2019 Petr Pisar <ppisar@redhat.com> - 2.0.3-1
- 2.0.3 bump
- Disable tests that need a server on recent Fedoras
  (<https://fedoraproject.org/wiki/Changes/MongoDB_Removal>, bug #1673849)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Petr Pisar <ppisar@redhat.com> - 2.0.2-1
- 2.0.2 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Petr Pisar <ppisar@redhat.com> - 2.0.1-1
- 2.0.1 bump

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.0.0-2
- Perl 5.28 rebuild

* Wed Jun 27 2018 Petr Pisar <ppisar@redhat.com> - 2.0.0-1
- 2.0.0 bump

* Tue Jun 26 2018 Petr Pisar <ppisar@redhat.com> - 1.8.3-1
- 1.8.3 bump

* Fri Jun  8 2018 Remi Collet <remi@remirepo.net> - 1.8.2-3
- rebuild with libbson 1.10.2 (soname back to 0)

* Mon May 28 2018 Remi Collet <remi@remirepo.net> - 1.8.2-2
- rebuild with libbson 1.10.0

* Wed May 23 2018 Petr Pisar <ppisar@redhat.com> - 1.8.2-1
- 1.8.2 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Petr Pisar <ppisar@redhat.com> - 1.8.1-1
- 1.8.1 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.0-2
- Perl 5.26 rebuild

* Tue Apr 11 2017 Petr Pisar <ppisar@redhat.com> - 1.8.0-1
- 1.8.0 bump
- Revert localhost is IPv4 only feature

* Fri Feb 24 2017 Petr Pisar <ppisar@redhat.com> - 1.6.1-2
- Enable builds on 64-bit big-endian platforms

* Fri Feb 24 2017 Petr Pisar <ppisar@redhat.com> - 1.6.1-1
- 1.6.1 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Petr Pisar <ppisar@redhat.com> - 1.4.5-3
- Adapt tests to MongoDB server 3.4.0-rc0

* Thu Oct 13 2016 Petr Pisar <ppisar@redhat.com> - 1.4.5-2
- Rebuild against libbson-1.5.0-rc2 (bug #1380063)

* Fri Sep 02 2016 Petr Pisar <ppisar@redhat.com> - 1.4.5-1
- 1.4.5 bump

* Mon Aug 29 2016 Petr Pisar <ppisar@redhat.com> - 1.4.4-2
- Rebuild against libbson-1.4.0 (bug #1361166)

* Mon Aug 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.4-1
- 1.4.4 bump

* Tue Jul 19 2016 Petr Pisar <ppisar@redhat.com> - 1.4.3-1
- 1.4.3 bump

* Tue Jun 14 2016 Petr Pisar <ppisar@redhat.com> - 1.4.2-1
- 1.4.2 bump

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.1-2
- Perl 5.24 re-rebuild of bootstrapped packages

* Thu May 19 2016 Petr Pisar <ppisar@redhat.com> - 1.4.1-1
- 1.4.1 bump
- Fix MongoDB::GridFSBucket::DownloadStream to work without Class::XSAccessor
- Recommend Class::XSAccessor for performance

* Tue May 17 2016 Petr Pisar <ppisar@redhat.com> - 1.4.0-3
- Enable grid tests and add an explicit dependency on Class::XSAccessor to avoid
  a Moo memory bug

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.0-2
- Perl 5.24 rebuild

* Fri May 13 2016 Petr Pisar <ppisar@redhat.com> - 1.4.0-1
- 1.4.0 bump
- Disable grid tests on x86

* Fri Apr 01 2016 Petr Pisar <ppisar@redhat.com> - 1.2.3-2
- Enable tests on ARM (bug #1303864)
- Do not override server's storage in tests (bug #1303846)

* Wed Mar 09 2016 Petr Pisar <ppisar@redhat.com> - 1.2.3-1
- 1.2.3 bump

* Tue Feb 16 2016 Petr Pisar <ppisar@redhat.com> - 1.2.2-1
- 1.2.2 bump
- License changed to (ASL 2.0 and (GPL+ or Artistic))

* Tue Feb 16 2016 Petr Pisar <ppisar@redhat.com> - 0.708.4.0-4
- Unbundle libbson
- Unbundle Perl modules

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.708.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Petr Pisar <ppisar@redhat.com> - 0.708.4.0-2
- Print log if server could not been started
- Use mmapv1 engine in tests (bug #1303846)
- Disable tests on ARM because of the server (bug #1303864)

* Wed Aug 12 2015 Petr Šabata <contyk@redhat.com> - 0.708.4.0-1
- 0.708.4.0 bump, fix the build
- Source URL updated
- Modernize the spec file

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.702.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.702.2-6
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.702.2-5
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.702.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.702.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 24 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.702.2-2
- Actually remove arm from ExcludeArch

* Tue Sep 24 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.702.2-1
- Update to 0.702.2, fix ARM build (BZ#997975)

* Tue Aug 13 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.702.1-1
- Update to 0.702.1
- ExcludeArch arm (BZ#997975)
- Make sure mongodb server is killed after tests
- Summary revised

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.702.0-2
- Perl 5.18 rebuild

* Sun Aug  4 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.702.0-1
- Update to 0.702.0, enable sasl support

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.700.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.700.0-2
- Use perldoc to find Module::Install::Compiler

* Mon Apr 22 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.700.0-1
- Update to 0.700.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.503.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 24 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.503.3-1
- Update to 0.503.3
- Enable SSL support

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.45-4
- Perl 5.16 rebuild

* Wed Feb 08 2012 Dan Horák <dan[at]danny.cz> - 0.45-3
- set ExcludeArch to all big-endian arches

* Wed Jan 11 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.45-2
- BR revised
- Prepare a MongoDB server to run the test suite
- Other minor cleanup

* Tue Sep 20 2011 Michal Ingeli <mi@v3.sk> 0.45-1
- Upstream upgrade 0.45
- removed ccflags patch, fixed in upstream

* Mon Aug 08 2011 Michal Ingeli <mi@v3.sk> 0.44-1
- Version update to 0.44
- Removing ccflags from Makefile.PL that breaks i686 build

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.41-5
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.41-4
- Perl mass rebuild

* Sat Jan 22 2011 Michal Ingeli <mi@v3.sk> 0.41-3
- Conditionalize perl_default_filter
- Added Try::Tiny, required for test phase

* Sat Jan 22 2011 Michal Ingeli <mi@v3.sk> 0.41-2
- Removed redundant requires

* Wed Jan 19 2011 Michal Ingeli <mi@v3.sk> 0.41-1
- Provides filtering
- Fixed license
- Specfile autogenerated by cpanspec 1.78.
