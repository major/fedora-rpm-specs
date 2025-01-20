# some tests require Internet access, don't enable by default
%bcond network_tests 0

Name:           perl-Net-DNS-Paranoid
Version:        0.09
Release:        4%{?dist}
Summary:        Paranoid DNS resolver
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Net-DNS-Paranoid/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Net-DNS-Paranoid-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter perl-generators coreutils
BuildRequires:  perl(:VERSION) >= 5.8.8
BuildRequires:  perl(Class::Accessor::Lite) >= 0.05
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Net::DNS) >= 0.68
# version req isn't added by RPM auto-dep
Requires:       perl(Net::DNS) >= 0.68
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
%if %{with network_tests}
BuildRequires:  perl(Net::DNS::Resolver)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(utf8)
%endif

%description
This is a wrapper module for Net::DNS.

This module detects IP address / host names for internal servers.

%prep
%setup -q -n Net-DNS-Paranoid-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
unset VERBOSE
%if %{without network_tests}
rm t/01_simple.t
%endif
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/Net/DNS/Paranoid*
%{_mandir}/man3/Net::DNS::Paranoid*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 13 2024 Chris Adams <linux@cmadams.net> 0.09-2
- additional spec file cleanups

* Fri Mar 08 2024 Chris Adams <linux@cmadams.net> 0.09-1
- update to new version
- additional spec file cleanups

* Thu Feb 01 2024 Chris Adams <linux@cmadams.net> 0.08-3
- additional spec file cleanups

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 0.08-2
- spec file cleanups

* Mon Nov 20 2023 Chris Adams <linux@cmadams.net> 0.08-1
- initial package
