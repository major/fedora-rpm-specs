Name:		perl-Sub-Delete
Version:	1.00002
Release:	13%{?dist}
Summary:    Perl module to delete subroutines
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Sub-Delete
Source0:    https://cpan.metacpan.org/authors/id/S/SP/SPROUT/Sub-Delete-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:  perl(Exporter)
# Runtime

# Avoid doc-file dependency on perl(base)
%{?perl_default_filter}

%description
Sub::Delete provides one function, delete_sub, that deletes the
subroutine whose name is passed to it. (To load the module without
importing the function, write use Sub::Delete();.)

This does more than simply undefine the subroutine in the manner of
undef &foo, which leaves a stub that can trigger AUTOLOAD (and,
consequently, won't work for deleting methods). The subroutine is
completely obliterated from the symbol table (though there may be
references to it elsewhere, including in compiled code).

%prep
%setup -q -n Sub-Delete-%{version}

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
%doc Changes
%{perl_vendorlib}/Sub/
%{_mandir}/man3/Sub::Delete.3pm*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.00002-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.00002-12
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.00002-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.00002-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.00002-9
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.00002-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00002-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.00002-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.00002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.00002-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.00002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Andrea Veri <averi@fedoraproject.org> - 1.00002-1
- Initial package release.
