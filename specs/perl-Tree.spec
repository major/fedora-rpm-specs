# Perform optional tests
%bcond_without perl_Tree_enables_optional_test

Name:           perl-Tree
Version:        1.16
Release:        5%{?dist}
Summary:        Tree data structure
# lib/Tree/Binary2.pm:  GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Tree/DeepClone.pm:    GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Tree/Fast.pm:     GPL-1.0-or-later OR Artistic-1.0-Perl
# lib/Tree.pm:          GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:              GPL-1.0-or-later OR Artistic-1.0-Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tree
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Tree-%{version}.tgz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# I deliberately striped dependency versions because upstream blindly copies
# versions from his machine, and that prevents from pushing this software into
# older distributions, CPAN RT#117858
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
%if %{with perl_Tree_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Memory::Cycle) >= 1.02
%endif

# Filter private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Tests\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Tests\\)

%description
This implements a full-featured N-ary tree representation with configurable
error-handling and a simple events system that allows for transparent
persistence to a variety of data stores.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_Tree_enables_optional_test}
Requires:       perl(Test::Memory::Cycle) >= 1.02
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Tree-%{version}
perl -MConfig -pi -e 's/\A#!.*/$Config{startperl}/' scripts/print.tree.pl
# Help generators to recognize Perl scripts
for F in t/*.t t/Tree*/*.t; do
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
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
# README not useful
%doc Changes scripts
%{perl_vendorlib}/Tree
%{perl_vendorlib}/Tree.pm
%{_mandir}/man3/Tree.*
%{_mandir}/man3/Tree::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 26 2023 Petr Pisar <ppisar@redhat.com> - 1.16-1
- 1.16 bump
- Package the tests

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.15-2
- Perl 5.34 rebuild

* Tue Feb 02 2021 Petr Pisar <ppisar@redhat.com> - 1.15-1
- 1.15 bump

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-4
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Petr Pisar <ppisar@redhat.com> - 1.14-1
- 1.14 bump

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.13-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Petr Pisar <ppisar@redhat.com> - 1.13-1
- 1.13 bump

* Tue Nov 13 2018 Petr Pisar <ppisar@redhat.com> - 1.12-1
- 1.12 bump

* Mon Nov 12 2018 Petr Pisar <ppisar@redhat.com> - 1.11-1
- 1.11 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.10-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 15 2016 Petr Pisar <ppisar@redhat.com> - 1.10-1
- 1.10 bump

* Thu Sep 15 2016 Petr Pisar <ppisar@redhat.com> - 1.09-2
- Remove useless dependency version contrains (CPAN RT#117858)

* Thu Sep 15 2016 Petr Pisar <ppisar@redhat.com> - 1.09-1
- 1.09 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.08-2
- Perl 5.24 rebuild

* Thu May 05 2016 Petr Pisar <ppisar@redhat.com> - 1.08-1
- 1.08 bump
- License changed to (GPL+ or Artistic)

* Fri Apr 15 2016 Petr Pisar <ppisar@redhat.com> 1.07-1
- Specfile autogenerated by cpanspec 1.78.
