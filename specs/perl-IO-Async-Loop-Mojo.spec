Name:           perl-IO-Async-Loop-Mojo
Version:        0.07
Release:        4%{?dist}
Summary:        Use IO::Async with Mojolicious
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-Async-Loop-Mojo/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/IO-Async-Loop-Mojo-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter perl-generators coreutils
BuildRequires:  perl(IO::Async::Loop) >= 0.49
BuildRequires:  perl(IO::Async::LoopTests) >= 0.76
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Mojolicious) >= 2.65
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
This subclass of IO::Async::Loop uses Mojo::Reactor to perform its IO
operations. It allows the use of IO::Async-based code or modules from
within a Mojolicious application.

%prep
%setup -q -n IO-Async-Loop-Mojo-%{version}

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
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 0.04-2
- spec file cleanups

* Mon Nov 20 2023 Chris Adams <linux@cmadams.net> 0.07-1
- initial package
