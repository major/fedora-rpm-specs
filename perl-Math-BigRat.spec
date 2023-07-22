Name:           perl-Math-BigRat
# Keep 4-digit version to compete with perl.spec
Version:        0.2624
Release:        500%{?dist}
Summary:        Arbitrary big rational numbers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-BigRat
Source0:        https://cpan.metacpan.org/authors/id/P/PJ/PJACKLAM/Math-BigRat-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigInt) >= 1.999824
BuildRequires:  perl(Math::Complex) >= 1.36
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Math::BigInt) >= 1.999824
Requires:       perl(Math::Complex) >= 1.36
Conflicts:      perl < 4:5.22.0-348

# Filter modules bundled for tests
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(.::t/bigratpm.inc\\)
%global __requires_exclude %{__requires_exclude}|perl\\(Math::BigRat::Test\\)
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

%description
Math::BigRat complements Math::BigInt and Math::BigFloat by providing
support for arbitrary big rational numbers.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Math-BigRat-%{version}

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
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/00sig.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING RELEASE_TESTING TEST_SIGNATURE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc BUGS CHANGES README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2624-500
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.2624-499
- Increase release to favour standalone package

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2624-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2624-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.2624-1
- 0.2624 bump

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.2623-2
- Perl 5.36 rebuild

* Mon May 16 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.2623-1
- 0.2623 bump

* Thu Apr 14 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.2622-1
- 0.2622 bump

* Wed Apr 13 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.2621-1
- 0.2621 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2620-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.2620-1
- 0.2620 bump

* Thu Sep 30 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.2618-1
- 0.2618 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2617-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.2617-1
- 0.2617 bump

* Tue Jul 13 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.2616-1
- 0.2616 bump

* Mon Jul 12 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.2615-1
- 0.2615 bump
- Package tests

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.2614-477
- Increase release to favour standalone package

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2614-458
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2614-457
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.2614-456
- Increase release to favour standalone package

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2614-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2614-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.2614-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2614-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2614-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.2614-2
- Perl 5.28 rebuild

* Wed Apr 18 2018 Petr Pisar <ppisar@redhat.com> - 0.2614-1
- 0.2614 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2613-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2613-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Petr Pisar <ppisar@redhat.com> - 0.2613-1
- 0.2613 bump

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.2612-2
- Perl 5.26 rebuild

* Thu Mar 02 2017 Petr Pisar <ppisar@redhat.com> - 0.2612-1
- 0.2612 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2611-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 23 2016 Petr Pisar <ppisar@redhat.com> 0.2611-1
- Specfile autogenerated by cpanspec 1.78.
