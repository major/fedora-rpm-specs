Summary:	Pull out the modules a module explicitly uses
Name:		perl-Module-Extract-Use
Version:	1.053
Release:	2%{?dist}
License:	Artistic-2.0
URL:		https://metacpan.org/release/Module-Extract-Use
Source0:	https://cpan.metacpan.org/modules/by-module/Module/Module-Extract-Use-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter >= 4:5.10.0
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(Test::Manifest) >= 1.21
# Module Runtime
BuildRequires:	perl(PPI)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(Test::More) >= 1.0
# Optional Tests
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.00
# Dependencies
Requires:	perl(PPI)

%description
Extract the names of the modules used in a file using a static analysis. Since
this module does not run code, it cannot find dynamic uses of modules, such as
eval "require $class". It only reports modules that the file loads directly.
Modules loaded with parent or base, for instance, will be in the import list
for those pragmas but won't have separate entries in the data this module
returns.

%prep
%setup -q -n Module-Extract-Use-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes examples/ README.pod
%{perl_vendorlib}/Module/
%{_mandir}/man3/Module::Extract::Use.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.053-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Aug 17 2024 Paul Howarth <paul@city-fan.org> - 1.053-1
- Update to 1.053
  - More upstream metadata changes

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.052-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb  6 2024 Paul Howarth <paul@city-fan.org> - 1.052-1
- Update to 1.052
  - Refresh distro, update email addresses

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.051-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.051-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.051-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.051-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.051-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.051-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.051-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Paul Howarth <paul@city-fan.org> - 1.051-1
- Update to 1.051
  - Fix up t/rt/79273.t regression (GH#7)

* Sun Jan  9 2022 Paul Howarth <paul@city-fan.org> - 1.049-1
- Update to 1.049
  - Fix a link in the README.pod
- Add patch to fix test failures in t/rt/79273.t (GH#7)
- Use %%license unconditionally

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.047-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.047-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.047-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.047-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.047-2
- Perl 5.32 rebuild

* Sun Apr 26 2020 Paul Howarth <paul@city-fan.org> - 1.047-1
- Update to 1.047
  - Example 'extract_modules' now has a -e switch to exclude core modules
  - Small pod fix

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.045-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Paul Howarth <paul@city-fan.org> - 1.045-1
- Update to 1.045
  - Fix test for extracting modules from parent and base

* Wed Dec 18 2019 Paul Howarth <paul@city-fan.org> - 1.044-1
- Update to 1.044
  - Handle a couple of new cases:
    - Include the modules specified by parent or base
    - Find the requires in expressions, like 'my $r = require Foo'
  - Small documentation and examples updates
- Add patch to fix t/rt/79273.t (GH#5)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.043-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.043-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.043-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.043-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.043-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.043-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.043-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.043-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.043-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb  3 2017 Paul Howarth <paul@city-fan.org> - 1.043-1
- Update to 1.043
  - Clarified license as Artistic 2.0
    (https://github.com/briandfoy/module-extract-use/issues/3)

* Wed Feb  1 2017 Paul Howarth <paul@city-fan.org> - 1.04.2-1
- Update to 1.042
  - The -l and -j options work on the list of namespaces from all files
    together instead of the list per file; otherwise, strict and warnings
    for example always show up multiple times
  - Add JSON and simple list outputs for examples/extract_modules

* Fri Nov 25 2016 Paul Howarth <paul@city-fan.org> - 1.04-2
- Sanitize for Fedora submission

* Fri Nov 25 2016 Paul Howarth <paul@city-fan.org> - 1.04-1
- Initial RPM version
