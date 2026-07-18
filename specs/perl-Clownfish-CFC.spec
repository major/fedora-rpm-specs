Name:           perl-Clownfish-CFC
Version:        0.6.4
Release:        2%{?dist}
Summary:        Compiler for Apache Clownfish
# other files:          Apache-2.0
## Unbundled
# lemon:                Apache-2.0
# modules/CommonMark:   BSD-2-Clause AND MIT
License:        Apache-2.0
SourceLicense:  Apache-2.0 AND BSD-2-Clause and MIT
URL:            https://metacpan.org/release/Clownfish-CFC
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KARMAN/Clownfish-CFC-%{version}.tar.gz
# Use system lemon, <https://issues.apache.org/jira/browse/CLOWNFISH-60>
Patch0:         Clownfish-CFC-0.6.0-Use-system-lemon-if-possible.patch
# Handle pkg-config output with multiple arguments, bug #1416443,
# <https://issues.apache.org/jira/browse/CLOWNFISH-113>
Patch1:         Clownfish-CFC-0.6.1-Segment-ExtUtils-PkgConfig-output-into-arguments.patch
# There is charmonizer.c which is becoming a separate project
# <https://git-wip-us.apache.org/repos/asf/lucy-charmonizer.git>. However,
# lucy-charmonizer has not yet been released
# <http://lucy.apache.org/download.html>. Also Clownfish-CFC'c
# lib/Clownfish/CFC/Perl/Build/Charmonic.pm still relies on
# the local location. charmonizer.c is used only at build time.
# Therefore I'm not going to unbudle the charmonizer.c now.
BuildRequires:  cmark-devel
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  lemon
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# Modules from buildlib and Clownfish::CFC::Perl::Build::Charmonic from lib
# are used for building
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::PPPort) >= 3.14
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Clownfish not used at tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.18
# Yes, ExtUtils::CBuilder::Platform::Windows::GCC is required
BuildRequires:  perl(ExtUtils::CBuilder::Platform::Windows::GCC)
BuildRequires:  perl(ExtUtils::Mkbootstrap)
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.00
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Test::More)
# Clownfish not used. I believe it's used only when Clownfish-CFC is called
# from the Clownfish. Adding symetric dependency between Clownfish-CFC and
# Clownfish would create a cycle which is not desired for bulding and
# idempotent at run-time.
Requires:       perl(Devel::PPPort) >= 3.14
Requires:       perl(ExtUtils::CBuilder) >= 0.18
# Yes, ExtUtils::CBuilder::Platform::Windows::GCC is required
Requires:       perl(ExtUtils::CBuilder::Platform::Windows::GCC)
Requires:       perl(ExtUtils::Mkbootstrap)
Requires:       perl(ExtUtils::ParseXS) >= 3.00

# Filter non-versioned provides. Clownfish/CFC.pm extends name spaces of all
# the other modules that are defined with version in their respective files.
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\([^)]*\\)$

# Hide private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Clownfish::CFC::Test::
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Clownfish::CFC::Test::

%description
This is a compiler for Apache Clownfish.

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
%autosetup -p1 -n Clownfish-CFC-%{version}
# Unbundle lemon
rm -rf lemon
perl -i -ne 'print $_ unless m{^lemon/}' MANIFEST
# Unbundle cmark
rm -rf modules/CommonMark
perl -i -ne 'print $_ unless m{^modules/CommonMark/}' MANIFEST
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS" \
    --with_system_cmark=1
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/000-load.t
mkdir -p %{buildroot}%{_libexecdir}/%{name}/buildlib/Clownfish/CFC
cp -a buildlib/Clownfish/CFC/Test %{buildroot}%{_libexecdir}/%{name}/buildlib/Clownfish/CFC
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests, e.g. t/001-util.t, write into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
unset CHARM_VALGRIND CHARM_VERBOSITY CLOWNFISH_INCLUDE
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset CHARM_VALGRIND CHARM_VERBOSITY CLOWNFISH_INCLUDE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc CONTRIBUTING.md NOTICE README.md
%dir %{perl_vendorarch}/auto/Clownfish
%{perl_vendorarch}/auto/Clownfish/CFC
%dir %{perl_vendorarch}/Clownfish
%{perl_vendorarch}/Clownfish/CFC
%{perl_vendorarch}/Clownfish/CFC.{pm,pod}
%{_mandir}/man3/Clownfish::CFC.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Mon Jun 29 2026 Petr Pisar <ppisar@redhat.com> - 0.6.4-1
- 0.6.4 bump
- Package the tests

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Jan 05 2026 Jens Petersen <petersen@redhat.com> - 0.6.3-31
- rebuild for F44 https://fedoraproject.org/wiki/Changes/cmark-0.31

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 07 2025 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.3-29
- Perl 5.42 rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.3-27
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.3-25
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.3-21
- Perl 5.38 rebuild

* Mon Jan 30 2023 Jens Petersen <petersen@redhat.com> - 0.6.3-20
- rebuild

* Fri Jan 27 2023 Jens Petersen <petersen@redhat.com> - 0.6.3-19
- rebuild f38 against newer cmark

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.3-16
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.3-13
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.3-10
- Perl 5.32 rebuild

* Tue Feb 04 2020 Petr Pisar <ppisar@redhat.com> - 0.6.3-9
- Rebuild against cmark 0.29.0 (bug #1697593)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.3-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.3-3
- Perl 5.28 rebuild

* Thu Mar  1 2018 Florian Weimer <fweimer@redhat.com> - 0.6.3-2
- Rebuild with new redhat-rpm-config/perl build flags

* Tue Feb 27 2018 Petr Pisar <ppisar@redhat.com> - 0.6.3-1
- 0.6.3 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Jens Petersen <petersen@redhat.com> - 0.6.2-2
- rebuild against newer cmark

* Thu Nov 23 2017 Petr Pisar <ppisar@redhat.com> - 0.6.2-1
- 0.6.2 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.1-5
- Perl 5.26 rebuild

* Tue Feb 28 2017 Petr Pisar <ppisar@redhat.com> - 0.6.1-4
- Rebuild against cmark-0.27

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Petr Pisar <ppisar@redhat.com> - 0.6.1-2
- Handle pkg-config output with multiple arguments (bug #1416443)

* Wed Dec 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.6.1-1
- 0.6.1 bump

* Thu Dec 01 2016 Petr Pisar <ppisar@redhat.com> - 0.6.0.5-1
- 0.6.0.5 bump

* Mon Oct 10 2016 Petr Pisar <ppisar@redhat.com> - 0.6.0.4-1
- 0.6.0.4 bump

* Thu Sep 29 2016 Petr Pisar <ppisar@redhat.com> - 0.6.0-1
- 0.6.0 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.5.1-3
- Perl 5.24 rebuild

* Mon May 02 2016 Petr Pisar <ppisar@redhat.com> - 0.5.1-2
- Rebuild against cmark-0.25.2

* Mon Apr 25 2016 Petr Pisar <ppisar@redhat.com> - 0.5.1-1
- 0.5.1 bump

* Mon Apr 04 2016 Petr Pisar <ppisar@redhat.com> - 0.5.0-1
- 0.5.0 bump

* Thu Feb 04 2016 Petr Pisar <ppisar@redhat.com> - 0.4.4-1
- 0.4.4 bump

* Mon Jan 25 2016 Petr Pisar <ppisar@redhat.com> - 0.4.3-1
- 0.4.3 bump

* Thu Sep 17 2015 Petr Pisar <ppisar@redhat.com> 0.4.2-1
- Specfile autogenerated by cpanspec 1.78.
