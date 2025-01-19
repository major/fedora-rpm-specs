Name:           perl-AnyEvent-Future
Version:        0.05
Release:        6%{?dist}
Summary:        Use Future with AnyEvent
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/AnyEvent-Future/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/AnyEvent-Future-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter perl-generators coreutils
BuildRequires:  perl(:VERSION) >= 5.14.0
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Future) >= 0.49
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Timer)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
This subclass of Future integrates with AnyEvent, allowing the await method
to block until the future is ready. It allows AnyEvent-using code to be
written that returns Future instances, so that it can make full use of
Future's abilities, including Future::Utils, and also that modules using it
can provide a Future-based asynchronous interface of their own.

%prep
%setup -q -n AnyEvent-Future-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes examples README
%license LICENSE
%{perl_vendorlib}/AnyEvent
%{_mandir}/man3/AnyEvent::Future*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 08 2024 Chris Adams <linux@cmadams.net> 0.05-4
- additional spec file cleanups

* Thu Feb 01 2024 Chris Adams <linux@cmadams.net> 0.05-3
- additional spec file cleanups

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 0.05-2
- spec file cleanups

* Mon Nov 20 2023 Chris Adams <linux@cmadams.net> 0.05-1
- initial package
