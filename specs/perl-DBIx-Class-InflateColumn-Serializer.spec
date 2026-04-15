Name:           perl-DBIx-Class-InflateColumn-Serializer
Version:        0.09
Release:        1%{?dist}
Summary:        Inflators to serialize data structures for DBIx::Class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/DBIx-Class-InflateColumn-Serializer
Source0:        https://www.cpan.org/authors/id/M/MR/MRUIZ/DBIx-Class-InflateColumn-Serializer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.0
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(JSON::MaybeXS) >= 1.002005
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Storable)
BuildRequires:  perl(YAML)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(JSON::MaybeXS\\)$
# Hide private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(DBICTest

%description
This DBIx::Class component helps you store and access serialized data
structures in the columns of your database from your DBIx classes. The
intention is to provide a suite of well proven and reusable inflators and
deflators which throw an exception if the serialization doesn't fit in the
field and throw an exception if the deserialization results in an error.

Various serialization formats (JSON, Storable, YAML) are packaged in dedicated
subpackages.

%package JSON
Summary:        JSON inflator for DBIx::Class::InflateColumn::Serializer
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(JSON::MaybeXS) >= 1.002005

%description JSON
The data structures you assign to "data_column" via
DBIx::Class::InflateColumn::Serializer component will be saved in the database
in JSON format.

%package Storable
Summary:        Storable inflator for DBIx::Class::InflateColumn::Serializer
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description Storable
The data structures you assign to "data_column" via
DBIx::Class::InflateColumn::Serializer component will be saved in the database
in Storable format.

%package YAML
Summary:        YAML inflator for DBIx::Class::InflateColumn::Serializer
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description YAML
The data structures you assign to "data_column" via
DBIx::Class::InflateColumn::Serializer component will be saved in the database
in YAML format.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-JSON = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-Storable = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-YAML = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(DBD::SQLite)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n DBIx-Class-InflateColumn-Serializer-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset DBICTEST_DBPASS DBICTEST_DBUSER DBICTEST_DSN DBICTEST_NODEPLOY DBICTEST_SQLITE_USE_FILE DBICTEST_SQLT_DEPLOY
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset DBICTEST_DBPASS DBICTEST_DBUSER DBICTEST_DSN DBICTEST_NODEPLOY DBICTEST_SQLITE_USE_FILE DBICTEST_SQLT_DEPLOY
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README TODO
%dir %{perl_vendorlib}/DBIx
%dir %{perl_vendorlib}/DBIx/Class
%dir %{perl_vendorlib}/DBIx/Class/InflateColumn
%dir %{perl_vendorlib}/DBIx/Class/InflateColumn/Serializer
%{perl_vendorlib}/DBIx/Class/InflateColumn/Serializer.pm
%{_mandir}/man3/DBIx::Class::InflateColumn::Serializer.*

%files JSON
%{perl_vendorlib}/DBIx/Class/InflateColumn/Serializer/JSON.pm
%{_mandir}/man3/DBIx::Class::InflateColumn::Serializer::JSON.*

%files Storable
%{perl_vendorlib}/DBIx/Class/InflateColumn/Serializer/Storable.pm
%{_mandir}/man3/DBIx::Class::InflateColumn::Serializer::Storable.*

%files YAML
%{perl_vendorlib}/DBIx/Class/InflateColumn/Serializer/YAML.pm
%{_mandir}/man3/DBIx::Class::InflateColumn::Serializer::YAML.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Wed Apr 08 2026 Petr Pisar <ppisar@redhat.com> 0.09-1
- 0.09 version packaged
