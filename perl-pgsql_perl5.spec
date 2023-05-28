Name:           perl-pgsql_perl5
Version:        1.9.0
Release:        %autorelease
Summary:        Pg – Perl5 extension for PostgreSQL

# https://docs.fedoraproject.org/en-US/legal/license-field/#_perl_packages
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/pgsql_perl5
Source0:        https://cpan.metacpan.org/modules/by-module/Pg/pgsql_perl5-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76

# Tests: cannot run because we cannot run postgresql server as a normal user
#BuildRequires:  perl(AutoLoader)
#BuildRequires:  postgresql-server

BuildRequires:  libpq-devel


%description
The Pg module permits you to access all functions of the Libpq interface of
PostgreSQL. Libpq is the programmer’s interface to PostgreSQL. For examples of
how to use this module, look at the file test.pl.


%prep
%autosetup -n pgsql_perl5-%{version}

# Fix shebangs and permissions on examples and tests
sed -r -i 's|^#!/usr/local/bin/perl\b|#!%{_bindir}/perl|' eg/*.pl test.pl
chmod -v a+x eg/*.pl test.pl


%build
export POSTGRES_INCLUDE='%{_includedir}'
export POSTGRES_LIB='%{_libdir}'
perl Makefile.PL \
    INSTALLDIRS=vendor \
    NO_PACKLIST=1 \
    NO_PERLLOCAL=1 \
    OPTIMIZE="${RPM_OPT_FLAGS}"
%make_build


%install
# Based on %%make_install, but with pure_install as the target
make pure_install DESTDIR='%{buildroot}' INSTALL='install -p'

find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*


# Tests: cannot run because we cannot run postgresql server as a normal user
# %%check
# %%make_build test


%files
%doc Changes
%doc README
%doc eg/
%doc test.pl
%{perl_vendorarch}/auto/Pg/
%{perl_vendorarch}/Pg.pm
%{_mandir}/man3/Pg.3pm*


%changelog
%autochangelog
