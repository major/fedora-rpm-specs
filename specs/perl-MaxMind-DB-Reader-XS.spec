# Perform optional tests
%bcond_without perl_MaxMind_DB_Reader_XS_enables_optional_test

Name:           perl-MaxMind-DB-Reader-XS
Version:        1.000009
Release:        12%{?dist}
Summary:        Fast XS implementation of MaxMind DB reader
# Build.PL:                 Artistic-2.0
# c/perl_math_int128.c:     LicenseRef-Fedora-Public-Domain
# c/perl_math_int64.c:      LicenseRef-Fedora-Public-Domain
# c/ppport.h:               GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:                  Artistic-2.0 text
# lib/MaxMind/DB/Reader/XS.pm:  Artistic-2.0
# maxmind-db/LICENSE:       CC-BY-SA-3.0
# maxmind-db/MaxMind-DB-spec.md:    CC-BY-SA-3.0
# README.md:                Artistic-2.0
## Unbundled
# inc/Capture/Tiny.pm:      Apache-2.0
# inc/Config/AutoConf.pm:   GPL-1.0-or-later OR Artistic-1.0-Perl
License:        Artistic-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/MaxMind-DB-Reader-XS
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/MaxMind-DB-Reader-XS-%{version}.tar.gz
# Do not hardcore debugging
Patch0:         MaxMind-DB-Reader-XS-1.000008-Do-not-hardcode-debugging.patch
# Adapt to changes in libmaxminddb-1.12.0, bug #2336619, proposed upstream
# <https://github.com/maxmind/MaxMind-DB-Reader-XS/pull/39>.
Patch1:         MaxMind-DB-Reader-XS-1.000009-Do-not-call-MMDB_free_entry_data_list-on-libmaxmindd.patch
# Math::Int128 is not supported on 32-bit platforms, bugs #1871719, #1871720
ExcludeArch:    %{arm} %{ix86}
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  libmaxminddb-devel >= 1.2.0
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::AutoConf)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.10
BuildRequires:  perl(Math::Int128)
BuildRequires:  perl(Math::Int64)
BuildRequires:  perl(MaxMind::DB::Metadata) >= 0.040001
BuildRequires:  perl(MaxMind::DB::Reader::Role::HasMetadata)
BuildRequires:  perl(MaxMind::DB::Types)
BuildRequires:  perl(Moo)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(autodie)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(MaxMind::DB::Reader)
BuildRequires:  perl(Module::Implementation)
BuildRequires:  perl(Path::Class) >= 0.27
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::MaxMind::DB::Common::Util)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Number::Delta)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
%if %{with perl_MaxMind_DB_Reader_XS_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Net::Works::Network) >= 0.21
%endif
Requires:       perl(MaxMind::DB::Reader::Role::HasMetadata)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(Test::MaxMind::DB::Reader\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Test::MaxMind::DB::Reader\\)

%description
Simply installing this module causes MaxMind::DB::Reader to use the XS
implementation, which is much faster than the Perl implementation.

This Perl module is deprecated and will only receive fixes for major bugs and
security vulnerabilities. New features and functionality will not be added.

%package tests
Summary:        Tests for %{name}
License:        Artistic-2.0 AND CC-BY-SA-3.0
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.96
%if %{with perl_MaxMind_DB_Reader_XS_enables_optional_test}
Requires:       perl(Net::Works::Network) >= 0.21
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n MaxMind-DB-Reader-XS-%{version}
# Remove bundled modules
rm -r ./inc
perl -i -ne 'print $_ unless m{\Ainc/}' MANIFEST
# Remove an unused script we do not want to package because its dependencies
# are not available
rm maxmind-db/test-data/write-test-data.pl
perl -i -ne 'print $_ unless m{\Amaxmind-db/test-data/write-test-data.pl}' MANIFEST
# Help generators to recognize Perl scripts
for F in $(find -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a maxmind-db t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README.md valgrind.supp
%dir %{perl_vendorarch}/auto/MaxMind
%dir %{perl_vendorarch}/auto/MaxMind/DB
%dir %{perl_vendorarch}/auto/MaxMind/DB/Reader
%{perl_vendorarch}/auto/MaxMind/DB/Reader/XS
%dir %{perl_vendorarch}/MaxMind
%dir %{perl_vendorarch}/MaxMind/DB
%dir %{perl_vendorarch}/MaxMind/DB/Reader
%{perl_vendorarch}/MaxMind/DB/Reader/XS.pm
%{_mandir}/man3/MaxMind::DB::Reader::XS.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 10 2025 Petr Pisar <ppisar@redhat.com> - 1.000009-12
- Adapt to changes in libmaxminddb-1.12.0 (bug #2336619)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.000009-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.000009-10
- Perl 5.40 rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 1.000009-9
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.000009-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.000009-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.000009-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.000009-5
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.000009-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.000009-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.000009-2
- Perl 5.36 rebuild

* Tue Apr 12 2022 Petr Pisar <ppisar@redhat.com> - 1.000009-1
- 1.000009 bump
- Package the tests

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.000008-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.000008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.000008-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.000008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 07 2020 Petr Pisar <ppisar@redhat.com> 1.000008-1
- Specfile autogenerated by cpanspec 1.78.
