Name:           perl-Alien-Libxml2
Version:        0.19
Release:        18%{?dist}
Summary:        Install the C libxml2 library on your system
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-Libxml2/
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Alien-Libxml2-%{version}.tar.gz

%global debug_package %{nil}

# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Alien::Build::MM) >= 2.37
BuildRequires:  perl(Alien::Build::Plugin::Download::GitLab)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  pkgconfig(libxml-2.0)
# Run-time
BuildRequires:  perl(Alien::Base) >= 2.37
BuildRequires:  perl(Alien::Build) >= 2.37
BuildRequires:  perl(alienfile)
BuildRequires:  perl(base)
# Tests
BuildRequires:  perl(Config)
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(Test::Alien)
BuildRequires:  perl(Test::More)
Requires:       perl(Alien::Base) >= 2.37
# This RPM package ensures libxml2 is installed on the system
Requires:       pkgconfig(libxml-2.0) = %(type -p pkgconf >/dev/null && pkgconf --exists libxml-2.0 && pkg-config --modversion libxml-2.0 || echo 0)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Alien::Base\\)$

%description
This module provides libxml2 for other modules to use.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Alien-Libxml2-%{version}

# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
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
cp -a t corpus %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Alien*
%{_mandir}/man3/Alien::Libxml2*

%files tests
%{_libexecdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 02 2025 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-17
- Rebuild against libxml2-2.12.9 (rhbz#2334710)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 20 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-15
- Rebuild against libxml2-2.12.8 (rhbz#2292048)

* Tue May 21 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-14
- Rebuild against libxml2-2.12.7 (rhbz#2281010)

* Mon Mar 18 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-13
- Rebuild against libxml2-2.12.6 (rhbz#2270043)

* Tue Feb 06 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-12
- Rebuild against libxml2-2.12.5 (rhbz#2262863)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-8
- Rebuild against libxml2-2.12.3 (rhbz#2253557)

* Sun Nov 26 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-8
- Rebuild against libxml2-2.12.1

* Mon Nov 20 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-7
- Rebuild against libxml2-2.12.0 (rhbz#2250642)

* Mon Aug 28 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-6
- Rebuild against libxml2-2.11.5 (rhbz#2232594)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 20 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-4
- Rebuild against libxml2-2.10.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-2
- Rebuild against libxml2-2.10.3

* Mon Oct 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-1
- 0.19 bump
- Package tests

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-8
- Perl 5.36 rebuild

* Tue May 03 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-7
- Rebuild against libxml2-2.9.14

* Tue Mar 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-6
- Rebuild against libxml2-2.9.13

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-1
- 0.17 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-2
- Perl 5.32 rebuild

* Wed Apr 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-1
- 0.16 bump

* Thu Mar 19 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-1
- 0.15 bump

* Tue Mar 10 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-1
- 0.14 bump

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-1
- 0.12 bump

* Mon Nov 11 2019 Petr Pisar <ppisar@redhat.com> - 0.11-2
- Rebuild against libxml2-2.9.10

* Tue Oct 29 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.11-1
- 0.11 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-2
- Perl 5.30 rebuild

* Fri May 17 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-1
- 0.09 bump

* Thu Apr 04 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.07-1
- 0.07 bump

* Mon Mar 25 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.06-1
- Specfile autogenerated by cpanspec 1.78.
