Name:           perl-Test-Exports
Version:        1
Release:        12%{?dist}
Summary:        Test that modules export the right symbols
# lib/Test/Exports.pm:  BSD-2-Clause
License:        BSD-2-Clause
URL:            https://metacpan.org/dist/Test-Exports
Source0:        https://cpan.metacpan.org/authors/id/B/BM/BMORROW/Test-Exports-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More) >= 0.65
BuildRequires:  perl(Test::Most) >= 0.23
BuildRequires:  perl(Test::Tester) >= 0.08

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::(More|Most|Tester)\\)$

%description
This module provides simple test functions for testing other modules' import
methods. Testing is currently limited to checking which subroutines have been
imported.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.65
Requires:       perl(Test::Most) >= 0.23
Requires:       perl(Test::Tester) >= 0.08

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Test-Exports-%{version}
# Correct permisions
chmod a+x t/*.t

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
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
./Build test

%files
%doc Changes README
%dir %{perl_vendorlib}/Test
%{perl_vendorlib}/Test/Exports.pm
%{_mandir}/man3/Test::Exports.*

%files tests
%{_libexecdir}/%{name}

%changelog
* Thu Jun 11 2026 Petr Pisar <ppisar@redhat.com> - 1-12
- Modernize a spec file
- Package the tests

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Ralf Corsépius <corsepiu@fedoraproject.org> - 1-3
- Convert license to SPDX.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Ralf Corsépius <corsepiu@fedoraproject.org> 1-1
- Inital Fedora package.
