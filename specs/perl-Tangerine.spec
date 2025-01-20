Name:           perl-Tangerine
Version:        0.23
Release:        26%{?dist}
Summary:        Analyse perl files and report module-related information
License:        MIT
URL:            https://metacpan.org/release/Tangerine
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CONTYK/Tangerine-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(parent)
BuildRequires:  perl(PPI)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version) >= 0.77
# Tests only
BuildRequires:  perl(Test::More)
Requires:       perl(List::Util) >= 1.33

%description
Tangerine statically analyses perl files and reports various information
about provided, used (compile-time dependencies) and required (runtime
dependencies) modules.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Tangerine-%{version}
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove author tests
rm -f %{buildroot}%{_libexecdir}/%{name}/t/author-pod-syntax.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README.md TODO
%{perl_vendorlib}/*
%{_mandir}/man*/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Michal Josef Špaček <mspacek@redhat.com> - 0.23-21
- Package tests
- Remove dependency to old List::MoreUtils
- Simplify build and install phases

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-18
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-15
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Petr Šabata <contyk@redhat.com> - 0.23-1
- 0.23 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-2
- Perl 5.24 rebuild

* Thu Feb 25 2016 Petr Šabata <contyk@redhat.com> - 0.22-1
- 0.22 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Petr Šabata <contyk@redhat.com> - 0.21-1
- 0.21 bump

* Mon Aug 24 2015 Petr Šabata <contyk@redhat.com> - 0.19-1
- 0.19 bump

* Thu Jun 25 2015 Petr Šabata <contyk@redhat.com> - 0.18-1
- 0.18 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-2
- Perl 5.22 rebuild

* Mon May 18 2015 Petr Šabata <contyk@redhat.com> - 0.17-1
- 0.17 bump, metadata improvements

* Thu May 14 2015 Petr Šabata <contyk@redhat.com> - 0.16-1
- 0.16 bump

* Mon Apr 27 2015 Petr Šabata <contyk@redhat.com> - 0.15-1
- 0.15 bump
- The utility is now provided by a separate distribution/package

* Tue Mar 31 2015 Petr Šabata <contyk@redhat.com> - 0.14-1
- 0.14 bump

* Wed Feb 25 2015 Petr Šabata <contyk@redhat.com> - 0.13-1
- 0.13 bump

* Mon Jan 12 2015 Petr Šabata <contyk@redhat.com> - 0.12-1
- 0.12 bump

* Wed Nov 26 2014 Petr Šabata <contyk@redhat.com> - 0.11-1
- 0.11 bugfix bump

* Thu Oct 16 2014 Petr Šabata <contyk@redhat.com> - 0.10-1
- 0.10 bump

* Wed Oct 08 2014 Petr Šabata <contyk@redhat.com> - 0.06-1
- 0.06 bump, test suite enhancements

* Tue Sep 30 2014 Petr Šabata <contyk@redhat.com> - 0.05-1
- 0.05 bump

* Mon Sep 08 2014 Petr Šabata <contyk@redhat.com> - 0.03-1
- 0.03 bump
- Install the tangerine script

* Sun Sep 07 2014 Petr Šabata <contyk@redhat.com> 0.02-1
- Initial package
