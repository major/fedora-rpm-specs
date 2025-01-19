Name:		nsdiff
Version:	1.85
Release:	2%{?dist}
Summary:	create an "nsupdate" script from DNS zone file differences

License:	0BSD OR MIT-0
URL:		https://dotat.at/prog/nsdiff/
# Alternative:
#Source0:	https://github.com/fanf2/%%{name}/archive/%%{name}-%%{version}.tar.gz
Source0:	https://dotat.at/prog/%{name}/DNS-%{name}-%{version}.tar.gz

BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl(:VERSION) >= 5.10
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(Pod::Man)
BuildRequires:	perl(Pod::Html)
BuildArch:	noarch
Requires:	bind-utils
Requires:	perl(:VERSION) >= 5.10

%description
The nsdiff program examines the old and new versions of a DNS zone, and
outputs the differences as a script for use by BIND's nsupdate program.
It provides a bridge between static zone files and dynamic updates.

The nspatch script is a wrapper around `nsdiff | nsupdate` that checks
and reports errors in a manner suitable for running from cron.

The nsvi script makes it easy to edit a dynamic zone.

%prep
%autosetup -n DNS-%{name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%files
%doc README*
%{_bindir}/ns*
%{_mandir}/man1/ns*.1*
%{_mandir}/man3/DNS::ns*.3*
%{perl_vendorlib}/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.85-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 05 2024 Petr Menšík <pemensik@redhat.com> - 1.85-1
- Update to 1.85

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.82-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.82-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.82-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.82-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.82-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.82-5
- Update dependencies due to Fedora Guidelines for Perl

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.82-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.82-3
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Petr Menšík <pemensik@redhat.com> - 1.82-1
- Update to 1.82

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.81-4
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Petr Menšík <pemensik@redhat.com> - 1.81-1
- Update to 1.81

* Wed Jun 24 2020 Petr Menšík <pemensik@redhat.com> - 1.79-2
- Do not depend on bind-dnssec-utils, bind-utils is sufficient

* Wed Jun 24 2020 Petr Menšík <pemensik@redhat.com> - 1.79-1
- Update to 1.79

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.77-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.77-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Petr Menšík <pemensik@redhat.com> - 1.77-1
- Initial version


