Name:           perl-Future-Mojo
Version:        1.003
Release:        3%{?dist}
Summary:        Use Future with Mojo::IOLoop
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Future-Mojo
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Future-Mojo-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter perl-generators coreutils
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Future) >= 0.49
BuildRequires:  perl(IO::Async::Loop) >= 0.56
BuildRequires:  perl(IO::Async::Loop::Mojo) >= 0.04
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojo::Promise)
BuildRequires:  perl(Mojolicious) >= 7.54
BuildRequires:  perl(Role::Tiny) >= 2.000002
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Identity)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# version some requires
Requires:       perl(Future) >= 0.49
Requires:       perl(Mojolicious) >= 7.54
Requires:       perl(Role::Tiny) >= 2.000002
%global __requires_exclude ^perl\\((Future|Mojolicious|Role::Tiny)\\)$

%description
This subclass of Future stores a reference to the associated Mojo::IOLoop
instance, allowing the await method to block until the Future is ready.

%prep
%setup -q -n Future-Mojo-%{version}

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
%license LICENSE
%{perl_vendorlib}/Future
%{_mandir}/man3/Future::Mojo*
%{_mandir}/man3/Future::Role*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 21 2024 Chris Adams <linux@cmadams.net> 1.003-1
- update to new version
- additional spec file cleanups

* Fri Mar 08 2024 Chris Adams <linux@cmadams.net> 1.002-4
- additional spec file cleanups

* Thu Feb 01 2024 Chris Adams <linux@cmadams.net> 1.002-3
- additional spec file cleanups

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 1.002-2
- spec file cleanups

* Mon Nov 20 2023 Chris Adams <linux@cmadams.net> 1.002-1
- initial package
