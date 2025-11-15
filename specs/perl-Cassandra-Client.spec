# cassandra server is currently not packaged
%global cassandra_available 0

Name:           perl-Cassandra-Client
Version:        0.21
Release:        3%{?dist}
Summary:        Perl library for accessing Cassandra using its binary network protocol
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Cassandra-Client
Source0:        https://cpan.metacpan.org/authors/id/T/TV/TVDW/Cassandra-Client-%{version}.tar.gz
Patch0:         https://sources.debian.org/data/main/libc/libcassandra-client-perl/0.20-1~bpo12%2B1/debian/patches/remove-Sub%3A%3ACurrent.patch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::XSPromises)
BuildRequires:  perl(Clone) >= 0.36
BuildRequires:  perl(constant)
BuildRequires:  perl(Devel::GlobalDestruction) >= 0.11
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(feature)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::INET6)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Net::SSLeay) >= 1.63
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Ref::Util) >= 0.008
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
# Dropped, see Patch0
#BuildRequires:  perl(Sub::Current)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Runtime
BuildRequires:  perl(EV) >= 4
# Tests
%if 0%{cassandra_available}
BuildRequires:  perl(Benchmark)
# Orphan: BuildRequires:  perl(Compress::LZ4)
# Orphan: BuildRequires:  perl(Compress::Snappy)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Cycle)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Exception)
%endif
BuildRequires:  perl(Test::More)
Requires:       perl(AnyEvent)
Requires:       perl(EV) >= 4
Requires:       perl(Math::BigInt)


%description
Cassandra::Client is a Perl library giving its users access to the
Cassandra database, through the native protocol. Both synchronous and
asynchronous querying is supported, through various common calling styles.


%prep
%setup -q -n Cassandra-Client-%{version}
%patch -P0 -p1

# All these tests require a cassandra server
%if ! 0%{cassandra_available}
rm \
  t/01-connect.t \
  t/02-sync-basic-crud.t \
  t/04-batch.t \
  t/05-no-metadata.t \
  t/07-named-parameters.t \
  t/08-retries.t \
  t/10-queue.t \
  t/20-memleak.t \
  t/40-multiple-async-queries-response.t \
  t/50-bench.t \
  t/99-long-loop.t
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*


%check
unset AUTHOR_TESTING
unset BENCHMARK
unset CASSANDRA_HOST
make test


%files
%doc Changes README
%license LICENSE
%{perl_vendorarch}/auto/Cassandra/
%{perl_vendorarch}/Cassandra/
%{_mandir}/man3/Cassandra::Client*.3pm*


%changelog
* Thu Nov 13 2025 Xavier Bachelot <xavier@bachelot.org> 0.21-3
- Fix typo (RHBZ#2414652)

* Fri Nov 07 2025 Xavier Bachelot <xavier@bachelot.org> 0.21-2
- Review fixes

* Mon Jul 28 2025 Xavier Bachelot <xavier@bachelot.org> 0.21-1
- Initial spec file
