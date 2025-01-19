Name:           perl-AnyEvent-Connector
Version:        0.04
Release:        6%{?dist}
Summary:        AnyEvent TCP connect with transparent proxy handling
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/AnyEvent-Connector
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOSHIOITO/AnyEvent-Connector-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(:VERSION) >= 5.006
BuildRequires:  perl-interpreter perl-generators coreutils
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(Module::Build::Prereqs::FromCPANfile) >= 0.02
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
AnyEvent::Connector object has tcp_connect method compatible with that from
AnyEvent::Socket, and it handles proxy settings transparently.

%prep
%setup -q -n AnyEvent-Connector-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/AnyEvent
%{_mandir}/man3/AnyEvent::Connector*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 08 2024 Chris Adams <linux@cmadams.net> 0.04-4
- additional spec file cleanups

* Thu Feb 01 2024 Chris Adams <linux@cmadams.net> 0.04-3
- additional spec file cleanups

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 0.04-2
- spec file cleanups

* Mon Nov 20 2023 Chris Adams <linux@cmadams.net> 0.04-1
- initial package
