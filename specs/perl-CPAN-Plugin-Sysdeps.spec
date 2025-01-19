Name:           perl-CPAN-Plugin-Sysdeps
Version:        0.79
Release:        2%{?dist}
Summary:        CPAN client plugin for installing system dependencies
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-Plugin-Sysdeps
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/CPAN-Plugin-Sysdeps-%{version}.tar.gz
# Prevent a build script from accidental execution in an author mode
Patch0:         CPAN-Plugin-Sysdeps-0.66-Disable-probing-for-an-author-mode.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
# dnf5 not used at tests
BuildRequires:  perl(constant)
# CPAN::Distribution not used at tests
BuildRequires:  perl(Data::Dumper)
# Getopt::Long not used at tests
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(warnings)
BuildRequires:  rpm
# Optional run-time:
BuildRequires:  perl(Hash::Util)
# The code prefers parsing /etc/os-release
%if 0%{?rhel}
BuildRequires:  redhat-release
%else
BuildRequires:  fedora-release-common
%endif
# sudo not used at tests
# Tests:
# CPAN::Distribution || CPAN
BuildRequires:  perl(CPAN::Distribution)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
Requires:       dnf5
Requires:       perl(Data::Dumper)
Recommends:     perl(Hash::Util)
Requires:       perl(IPC::Open3)
Requires:       perl(Symbol)
Requires:       rpm
%if 0%{?rhel}
Recommends:     redhat-release
%else
Recommends:     fedora-release-common
%endif
Recommends:     sudo

# Filter private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(TestUtil\\)

%description
CPAN::Plugin::Sysdeps is a plugin for CPAN Perl module to install non-CPAN
dependencies automatically. Currently, the list of required system
dependencies is maintained in a static data structure in
CPAN::Plugin::Sysdeps::Mapping.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# CPAN::Distribution || CPAN
Requires:       perl(CPAN::Distribution)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n CPAN-Plugin-Sysdeps-%{version}
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
unset CPAN_PLUGIN_SYSDEPS_DEBUG PERL_CPAN_SYSDEPS_UV_UTIL_NATIVE
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test


%check
unset CPAN_PLUGIN_SYSDEPS_DEBUG PERL_CPAN_SYSDEPS_UV_UTIL_NATIVE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README.md
%{_bindir}/cpan-sysdeps
%dir %{perl_vendorlib}/CPAN
%dir %{perl_vendorlib}/CPAN/Plugin
%{perl_vendorlib}/CPAN/Plugin/Sysdeps
%{perl_vendorlib}/CPAN/Plugin/Sysdeps.pm
%{_mandir}/man1/cpan-sysdeps.1*
%{_mandir}/man3/CPAN::Plugin::Sysdeps::*
%{_mandir}/man3/CPAN::Plugin::Sysdeps.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 22 2024 Petr Pisar <ppisar@redhat.com> - 0.79-1
- 0.79 bump

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Petr Pisar <ppisar@redhat.com> - 0.78-2
- Depend on dnf5 instead of dnf (bug #2209402)

* Mon Apr 29 2024 Petr Pisar <ppisar@redhat.com> - 0.78-1
- 0.78 bump

* Wed Mar 27 2024 Petr Pisar <ppisar@redhat.com> - 0.77-1
- 0.77 bump

* Mon Mar 11 2024 Petr Pisar <ppisar@redhat.com> - 0.76-1
- 0.76 bump

* Mon Mar 04 2024 Petr Pisar <ppisar@redhat.com> - 0.75-2
- Depend on fedora-release-common instead of system-release(releasever)

* Mon Mar 04 2024 Petr Pisar <ppisar@redhat.com> - 0.75-1
- 0.75 bump

* Wed Feb 21 2024 Petr Pisar <ppisar@redhat.com> - 0.73-1
- 0.73 bump

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.72-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.72-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 06 2023 Petr Pisar <ppisar@redhat.com> - 0.72-1
- 0.72 bump

* Mon Aug 28 2023 Petr Pisar <ppisar@redhat.com> - 0.71-1
- 0.71 bump

* Fri Jul 28 2023 Petr Pisar <ppisar@redhat.com> - 0.70-11
- Revert dnf to dnf5 migration (bug #2209402)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.70-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Petr Pisar <ppisar@redhat.com> - 0.70-9
- Port integration tests to DNF5

* Mon Jun 26 2023 Petr Pisar <ppisar@redhat.com> - 0.70-8
- Depend on dnf5 instead of dnf (bug #2209402)

* Wed May 24 2023 Petr Pisar <ppisar@redhat.com> - 0.70-7
- Name packaged files explicitly

* Wed May 24 2023 Petr Pisar <ppisar@redhat.com> - 0.70-6
- Convert a license tag to an SPDX format

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.70-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.70-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.70-3
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 15 2021 Petr Pisar <ppisar@redhat.com> - 0.70-1
- 0.70 bump

* Wed Sep 01 2021 Petr Pisar <ppisar@redhat.com> - 0.69-1
- 0.69 bump
- Package the tests

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.68-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Petr Pisar <ppisar@redhat.com> - 0.68-1
- 0.68 bump

* Mon Dec 14 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.67-1
- 0.67 bump

* Fri Oct 23 2020 Petr Pisar <ppisar@redhat.com> 0.66-1
- Specfile autogenerated by cpanspec 1.78.
