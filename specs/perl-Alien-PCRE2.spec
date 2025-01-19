Name:           perl-Alien-PCRE2
Version:        0.017000
Release:        8%{?dist}
Summary:        Install and locate PCRE2 library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-PCRE2
Source0:        https://cpan.metacpan.org/authors/id/W/WB/WBRASWELL/Alien-PCRE2-%{version}.tar.gz
# Disable Alien share mode, we always use system-provided libraries,
# not suitable for the upstream.
Patch0:         Alien-PCRE2-0.017000-Disable-shared-mode.patch
# This is an architecture-dependenant package because it stores data about
# architecture-specific library, but it has no XS code, hence no debuginfo.
%global debug_package %{nil}
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Alien::Build::MM) >= 0.32
# From ./alienfile
# Alien::Build::Plugin::Build::Autoconf not used
# From ./alienfile
# Alien::Build::Plugin::Download::GitHub 1.30 not used
# From ./alienfile
# Alien::Build::Plugin::Extract::Negotiate not used
# From ./alienfile
BuildRequires:  perl(Alien::Build::Plugin::PkgConfig::Negotiate)
# From ./alienfile
BuildRequires:  perl(alienfile)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# From ./alienfile
BuildRequires:  pkgconfig(libpcre2-8)
# Run-time:
# Alien modules' purpose is to ensure one can compile against a library
BuildRequires:  pcre2-devel
BuildRequires:  perl(Alien::Base) >= 0.038
BuildRequires:  perl(base)
# Tests:
# pcre2grep tests in t/03_pcre2grep.t skipped on system Alien installation.
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(Env)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Alien)
BuildRequires:  perl(Test::Alien::Diag)
BuildRequires:  perl(Test::More)
# Alien modules' purpose is to ensure one can compile against a library.
# We need to match an architecture,
Requires:       pcre2-devel%{?_isa}
%if "0" == "%(pkgconf --exist libpcre2-8 2>/dev/null; echo $?)"
# And we need to match a pkgconfig module version. Both compiled in.
Requires:       pkgconfig(libpcre2-8) = %(pkgconf --modversion libpcre2-8)
%endif
Requires:       perl(Alien::Base) >= 0.038

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Alien::Base\\)$

%description
This package can be used by other Perl modules that require PCRE2 library, the
new Perl Compatible Regular Expression engine.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Alien-PCRE2-%{version}
# Remove tests which are always skipped.
rm t/03_pcre2grep.t
perl -i -ne 'print $_ unless m{\A\Qt/03_pcre2grep.t\E}' MANIFEST
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
# Always use system PCRE2 no matter what version it is.
export ALIEN_PCRE2_MIN_VERSION=0
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Remove useless alienfile which would only pull unnwanted dependencies
rm %{buildroot}/%{perl_vendorarch}/auto/share/dist/Alien-PCRE2/_alien/alienfile
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Test::Alien writes into CWD
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README.md
%dir %{perl_vendorarch}/Alien
%{perl_vendorarch}/Alien/PCRE2
%{perl_vendorarch}/Alien/PCRE2.pm
%dir %{perl_vendorarch}/auto/Alien
%{perl_vendorarch}/auto/Alien/PCRE2
%dir %{perl_vendorarch}/auto/share
%dir %{perl_vendorarch}/auto/share/dist
%{perl_vendorarch}/auto/share/dist/Alien-PCRE2
%{_mandir}/man3/Alien::PCRE2.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.017000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.017000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 28 2024 Petr Pisar <ppisar@redhat.com> - 0.017000-6
- Rebuild against pcre2-10.44 (bug #2294618)

* Wed Mar 20 2024 Petr Pisar <ppisar@redhat.com> - 0.017000-5
- Rebuild against pcre2-10.43 (bug #2270432)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.017000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.017000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.017000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 06 2023 Petr Pisar <ppisar@redhat.com> - 0.017000-1
- 0.017000 bump

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.016000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Petr Pisar <ppisar@redhat.com> - 0.016000-4
- Rebuild against pcre2-10.42 (bug #2160911)
- Convert a License tag to an SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.016000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.016000-2
- Perl 5.36 rebuild

* Mon May 09 2022 Petr Pisar <ppisar@redhat.com> - 0.016000-1
- 0.016000 bump
- Package the tests

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.015000-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.015000-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.015000-13
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.015000-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.015000-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.015000-10
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.015000-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.015000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.015000-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.015000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.015000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 0.015000-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.015000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Petr Pisar <ppisar@redhat.com> - 0.015000-2
- Adjust tests to accept PCRE2 release candidates

* Thu Nov 09 2017 Petr Pisar <ppisar@redhat.com> - 0.015000-1
- 0.015000 bump

* Mon Nov 06 2017 Petr Pisar <ppisar@redhat.com> - 0.014000-1
- 0.014000 bump

* Mon Sep 04 2017 Petr Pisar <ppisar@redhat.com> 0.013000-1
- Specfile autogenerated by cpanspec 1.78.
