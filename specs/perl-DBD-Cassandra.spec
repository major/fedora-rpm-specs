Name:           perl-DBD-Cassandra
Version:        0.57
Release:        1%{?dist}
Summary:        DBI database backend for Cassandra
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/DBD-Cassandra
Source0:        https://www.cpan.org/modules/by-module/DBD/DBD-Cassandra-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(Cassandra::Client) >= 0.10
BuildRequires:  perl(DBI) >= 1.621
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)


%description
DBD::Cassandra is a Perl5 Database Interface driver for Cassandra, using
the CQL3 query language.


%prep
%setup -q -n DBD-Cassandra-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*


%check
unset AUTHOR_TESTING
unset CASSANDRA_HOS
make test


%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/DBD/
%{_mandir}/man3/DBD::Cassandra*.3pm*


%changelog
* Fri Jul 25 2025 Xavier Bachelot <xavier@bachelot.org> 0.57-1
- Initial spec file
