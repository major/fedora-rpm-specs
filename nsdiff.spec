Name:		nsdiff
Version:	1.82
Release:	4%{?dist}
Summary:	create an "nsupdate" script from DNS zone file differences

License:	Public Domain
URL:		https://dotat.at/prog/nsdiff/
# Alternative:
#Source0:	https://github.com/fanf2/%%{name}/archive/%%{name}-%%{version}.tar.gz
Source0:	https://dotat.at/prog/%{name}/DNS-%{name}-%{version}.tar.gz

BuildRequires:	perl >= 5.10
BuildRequires:	perl(Pod::Man) perl(Pod::Html)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	make
BuildArch:	noarch
Requires:	perl >= 5.10
Requires:	bind-utils
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version+`"; echo $version))
Provides:	perl(DNS::nsdiff)

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
%{__perl} Makefile.PL
make INSTALLDIRS=vendor


%install
%make_install INSTALLDIRS=vendor

rm -f %{buildroot}%{perl_archlib}/perllocal.pod
# .packlist
rm -rf %{buildroot}%{perl_vendorarch}/auto/

%files
%doc README*
%{_bindir}/ns*
%{_mandir}/man1/ns*.1*
%{_mandir}/man3/DNS::ns*.3*
%{perl_vendorlib}/*


%changelog
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


