Name:       perl-Monkey-Patch
Version:    0.03
Release:    13%{?dist}
Summary:    Scoped monkey-patching Perl module
License:    GPL+ or Artistic
URL:        https://metacpan.org/release/Monkey-Patch
Source0:    https://cpan.metacpan.org/authors/id/F/FR/FRODWITH/Monkey-Patch-%{version}.tar.gz
BuildArch:  noarch
# Module Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(SUPER)
BuildRequires:  perl(Sub::Delete)
# Tests
BuildRequires:  perl(Test::More)
# Runtime
Requires:  perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:  perl(SUPER)
Requires:  perl(Sub::Delete)
Patch0:    01_fix_pod.patch

# Avoid doc-file dependency on perl(base)
%{?perl_default_filter}

%description
Monkey patching is a way to extend or modify the runtime code
of a program or library without altering the original source code.

Monkey::Patch provides lexical scope monkey-patching so that you can
wrap any other package's subroutine with your own code and still have
access to the original subroutine.

%prep
%setup -q -n Monkey-Patch-%{version}
%patch0 -p1

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
%doc CHANGES README
%{perl_vendorlib}/Monkey/
%{_mandir}/man3/Monkey::Patch.3pm*
%{_mandir}/man3/Monkey::Patch::Handle.3pm*
%{_mandir}/man3/Monkey::Patch::Handle::Class.3pm*
%{_mandir}/man3/Monkey::Patch::Handle::Object.3pm*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-12
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-9
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Andrea Veri <averi@fedoraproject.org> - 0.03-1
- Initial package release.
