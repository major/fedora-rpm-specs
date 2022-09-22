Name:           perl-Module-Install-RDF
Version:        0.009
Release:        19%{?dist}
Summary:        Advanced meta-data for your distribution
# CONTRIBUTING: CC-BY-SA
# Other files:  GPL+ or Artistic
License:        (GPL+ or Artistic) and CC-BY-SA
URL:            https://metacpan.org/release/Module-Install-RDF
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Module-Install-RDF-%{version}.tar.gz
# To boostrap this package without bundling
Patch0:         Module-Install-RDF-0.009-Build-without-bundled-Module-Package-modules.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Package)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
# 1.00 version from Module::Install in META.yml
BuildRequires:  perl(Module::Install::Base) >= 1.0
BuildRequires:  perl(Object::ID)
BuildRequires:  perl(RDF::Trine) >= 0.135
# RDF::TrineX::Parser::Pretdsl not used at tests
BuildRequires:  perl(strict)
BuildRequires:  perl(URI::file) >= 4.0
BuildRequires:  perl(warnings)
# Optional run-time:
# RDF::TrineX::Serializer::MockTurtleSoup
# Tests:
BuildRequires:  perl(Test::More) >= 0.61
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# 1.00 version from Module::Install in META.yml
Requires:       perl(Module::Install::Base) >= 1.0
Requires:       perl(RDF::Trine) >= 0.135
Requires:       perl(RDF::TrineX::Parser::Pretdsl)
Requires:       perl(URI::file) >= 4.0
Requires:       perl(warnings)
# Optional run-time:
Suggests:       perl(RDF::TrineX::Serializer::MockTurtleSoup)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Module::Install::Base|RDF::Trine|URI::file)\\)

%description
These Perl modules read all the RDF files it can find in the distribution's
"meta" directory and expose them for other modules to make use of them. They
also allow you to write out a combined graph using Turtle.

%prep
%setup -q -n Module-Install-RDF-%{version}
%patch0 -p1
# Remove bundled modules.
# And remove inc/Module/Package/Dist/RDF.pm because it's a 
# Module::Package::RDF plug-in that run-depends on this (Module::Install::RDF)
# package. Fortunatelly, the inc/Module/Package/Dist/RDF.pm is not good for
# anything so the patch makes not to load it.
rm -r ./inc
sed -i -e '/^inc/d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-18
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-15
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.009-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 16 2016 Petr Pisar <ppisar@redhat.com> 0.009-1
- Specfile autogenerated by cpanspec 1.78.
