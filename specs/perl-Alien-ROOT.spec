Name:           perl-Alien-ROOT
Version:        5.34.36.1
Release:        35%{?dist}
Summary:        Utility package to install and locate CERN's ROOT library
# README:               GPLv2+
# lib/Alien/ROOT.pm:    GPLv2+
## Not in the binary package
# inc/inc_Params-Check/Params/Check.pm: GPL+ or Artistic
# inc/inc_Locale-Maketext-Simple/Locale/Maketext/Simple.pm: MIT with exception
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Alien-ROOT
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Alien-ROOT-v%{version}.tar.gz
Patch0:         Alien-ROOT-v5.34.36.1-Disable-build-time-check-for-Root.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Archive::Extract)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Env)
BuildRequires:  perl(Exporter)
# ExtUtils::Command not used
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Fetch)
BuildRequires:  perl(Getopt::Long)
# inc::latest not used
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IPC::Open3)
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(Config)
Requires:       perl(ExtUtils::MakeMaker)
Requires:       perl(File::Spec)
Requires:       perl(IPC::Open3)
Requires:       root-core

%description
The original intention is to install and detect CERN's ROOT library. This
package always requires the ROOT library provided with your distribution.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Alien::ROOT)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Alien-ROOT-v%{version}
%patch -P0 -p1
# Remove bundled modules
find inc -depth -mindepth 1 -maxdepth 1 \! -name Alien -exec rm -rf -- {} +
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
find inc -type f >> MANIFEST
# Bypass inc::latest as it requires packlists
perl -i -pe "s/use inc::latest '([^']*)'/use \$1/" Build.PL

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 5.34.36.1-34
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.34.36.1-27
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 30 2021 Petr Pisar <ppisar@redhat.com> - 5.34.36.1-25
- Enable building for s390x (bug #1482813)
- Package the tests

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 5.34.36.1-23
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.34.36.1-20
- Perl 5.32 rebuild

* Mon Mar 16 2020 Petr Pisar <ppisar@redhat.com> - 5.34.36.1-19
- Enable on 32-bit ARM (bug #1004354)

* Mon Mar 09 2020 Petr Pisar <ppisar@redhat.com> - 5.34.36.1-18
- Disable on 32-bit ARM becausee of root package (bug #1004354)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 5.34.36.1-15
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 5.34.36.1-12
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Petr Pisar <ppisar@redhat.com> - 5.34.36.1-10
- Enable support for PowerPC because root becomes available there
  (bugs #1392475, #1392479)

* Fri Aug 18 2017 Petr Pisar <ppisar@redhat.com> - 5.34.36.1-9
- Disable building for s390x platform because of missing root (bug #1482813)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Petr Pisar <ppisar@redhat.com> - 5.34.36.1-6
- Make the package architecture specific (https://pagure.io/releng/issue/6359)

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 5.34.36.1-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.36.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Petr Pisar <ppisar@redhat.com> - 5.34.36.1-3
- Enable on AArch64 platform (bug #1392467)

* Mon Nov 07 2016 Petr Pisar <ppisar@redhat.com> - 5.34.36.1-2
- Exclude from AArch64 and 64-bit PowerPC platforms because root does not work
  there (bugs #1392467, #1392475, #1392479)

* Thu Sep 08 2016 Petr Pisar <ppisar@redhat.com> - 5.34.36.1-1
- 5.34.36.1 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 5.34.3.1-12
- Perl 5.24 rebuild

* Tue Apr 12 2016 Petr Pisar <ppisar@redhat.com> - 5.34.3.1-11
- Enable building on ARM because root-6 works there (bug #1004354)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.34.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.34.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 5.34.3.1-8
- Perl 5.22 rebuild

* Mon Sep 15 2014 Petr Pisar <ppisar@redhat.com> - 5.34.3.1-7
- Disable generating debuginfo sub-package (bug #1141466)

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 5.34.3.1-6
- Perl 5.20 rebuild
- Made packages architecture specific

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.34.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 04 2013 Petr Pisar <ppisar@redhat.com> - 5.34.3.1-4
- Disable on ARM due to root (bug #1004354)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.34.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 5.34.3.1-2
- Perl 5.18 rebuild

* Tue May 14 2013 Petr Pisar <ppisar@redhat.com> 5.34.3.1-1
- Specfile autogenerated by cpanspec 1.78.
