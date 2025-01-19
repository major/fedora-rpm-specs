Name:           perl-Acme-Alien-DontPanic
%global cpan_version 2.7200
Version:        2.720.0
Release:        7%{?dist}
Summary:        Test module for Alien::Base
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Acme-Alien-DontPanic
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Acme-Alien-DontPanic-%{cpan_version}.tar.gz
# Full-arch for files storing architecture-specific paths
%global debug_package %{nil}
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
# Alien::Build::MM version from Alien::Build in Makefile.PL
BuildRequires:  perl(Alien::Build::MM) >= 2.59
# Alien::Build::Plugin::Digest::Negotiate not used
BuildRequires:  perl(Alien::Build::Plugin::Build::Autoconf)
BuildRequires:  perl(Alien::Build::Plugin::Probe::CommandLine)
BuildRequires:  perl(alienfile)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Use a system dontpanic library instead of downloading it from the Internet at
# build time.
BuildRequires:  pkgconfig(dontpanic)
# Run-time:
BuildRequires:  perl(Alien::Base) >= 2.59
BuildRequires:  perl(base)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Inline) >= 0.56
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(Inline::CPP)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(Test::Alien) >= 0.05
BuildRequires:  perl(Test::Alien::Diag)
# Optional tests:
# Test::More not helpful
Requires:       perl(Alien::Base) >= 2.59
# The maning of the package is have dontpanic library installed and
# application being able to build against it. Because we use system dontpanic
# library instead of bundling one that had been dowloaded and compiled at
# build time, we need to explicitly run-require the developmental files of the
# library.
Requires:       pkgconfig(dontpanic)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Alien::Base|Test2::V0)\\)$

%description
This Perl module is a toy module to test the efficacy of the Alien::Base system.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Inline::C)
Requires:       perl(Inline::CPP)
Requires:       perl(Test2::V0) >= 0.000121

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Acme-Alien-DontPanic-%{cpan_version}
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
#!/bin/bash
# ExtUtils::CBuilder::have_compiler() writes into CWD
# <https://github.com/Perl/perl5/issues/15697>.
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Acme
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.720.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.720.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.720.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.720.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.720.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.720.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 27 2022 Petr Pisar <ppisar@redhat.com> - 2.720.0-1
- 2.7200 bump

* Wed Aug 31 2022 Petr Pisar <ppisar@redhat.com> - 2.650.0-1
- 2.6500 bump

* Tue Aug 16 2022 Petr Pisar <ppisar@redhat.com> - 2.590.0-1
- 2.5900 bump

* Thu Aug 04 2022 Petr Pisar <ppisar@redhat.com> - 2.510.0-1
- 2.5100 bump
- Package the tests

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.290.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.290.0-6
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.290.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.290.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.290.0-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.290.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Petr Pisar <ppisar@redhat.com> - 2.290.0-1
- 2.2900 bump

* Mon Aug 17 2020 Petr Pisar <ppisar@redhat.com> - 2.260.0-1
- 2.2600 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.110.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.110.0-2
- Perl 5.32 rebuild

* Mon Mar 09 2020 Petr Pisar <ppisar@redhat.com> - 2.110.0-1
- 2.1100 bump

* Thu Feb 06 2020 Petr Pisar <ppisar@redhat.com> - 2.40.0-1
- 2.0400 bump

* Mon Feb 03 2020 Petr Pisar <ppisar@redhat.com> - 2-1
- 2.0000 bump

* Fri Jan 31 2020 Petr Pisar <ppisar@redhat.com> - 1.98.00-1
- 1.9800 bump

* Wed Jan 29 2020 Petr Pisar <ppisar@redhat.com> - 1.96-1
- 1.96 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-2
- Perl 5.28 re-rebuild of bootstrapped packages

* Tue May 15 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.03-1
- 1.03 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.044-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 Petr Pisar <ppisar@redhat.com> 0.044-1
- Specfile autogenerated by cpanspec 1.78.
