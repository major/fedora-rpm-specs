# Perform optional tests
%bcond_without perl_IO_Interactive_enables_optional_test

Name:           perl-IO-Interactive
Version:        1.026
Release:        1%{?dist}
Summary:        Utilities for interactive I/O
# lib/IO/Interactive.pm:    GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:                  (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Artistic-2.0
# license_clarification:    Artistic-2.0 (brian d foy's explanation)
# README.pod:               "see LICENSE file and the modules files"
# IO-Ineractive-1.021 added the ambiguous LICENSE file. Because there are
# still files only referring to Perl, but not referring to Artistic-2.0,
# I keep the (GPL-1.0-or-later OR Artistic-1.0-Perl) part in the License tag.
# <https://github.com/briandfoy/io-interactive/issues/2>
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Artistic-2.0
URL:            https://metacpan.org/release/IO-Interactive
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/IO-Interactive-%{version}.tar.gz
Source1:        license_clarification
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(strict)
# Test::Manifest not used
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(IO::Handle)
# Tests:
BuildRequires:  perl(Test::More) >= 1
%if %{with perl_IO_Interactive_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
%endif
Requires:       perl(Carp)

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$

%description
This module provides utility subroutines that make it easier to develop
interactive applications.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 1

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n IO-Interactive-%{version}
install -m 0644 %{SOURCE1} .
%if !%{with perl_IO_Interactive_enables_optional_test}
rm t/pod*
perl -i -ne 'print $_ unless m{^t/pod}' MANIFEST
%endif
chmod +x t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_IO_Interactive_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod*
%endif
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes examples license_clarification README.pod SECURITY.md
%dir %{perl_vendorlib}/IO
%{perl_vendorlib}/IO/Interactive.pm
%{_mandir}/man3/IO::Interactive.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Mon Jan 27 2025 Petr Pisar <ppisar@redhat.com> - 1.026-1
- 1.026 bump

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.025-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.025-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.025-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.025-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.025-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Petr Pisar <ppisar@redhat.com> - 1.025-1
- 1.025 bump

* Mon Apr 17 2023 Petr Pisar <ppisar@redhat.com> - 1.023-8
- Convert a licene tag to an SPDX format
- Package the tests

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.023-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.023-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.023-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.023-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.023-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.023-2
- Perl 5.34 rebuild

* Fri Feb 05 2021 Petr Pisar <ppisar@redhat.com> - 1.023-1
- 1.023 bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.022-13
- Perl 5.32 rebuild

* Thu Jun 18 2020 Petr Pisar <ppisar@redhat.com> - 1.022-12
- Moderize a spec file

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.022-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.022-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.022-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 05 2016 Petr Pisar <ppisar@redhat.com> - 1.022-1
- 1.022 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.021-4
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.021-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Petr Pisar <ppisar@redhat.com> - 1.021-2
- License clarification added

* Thu Jan 28 2016 Petr Pisar <ppisar@redhat.com> - 1.021-1
- 1.021 bump
- License changed to ((GPL+ or Artistic) and (Artistic 2.0))

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.6-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.6-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Petr Pisar <ppisar@redhat.com> 0.0.6-1
- Specfile autogenerated by cpanspec 1.78.
