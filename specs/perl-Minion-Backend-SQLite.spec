Name:           perl-Minion-Backend-SQLite
Version:        5.0.7
Release:        8%{?dist}
Summary:        SQLite backend for Minion job queue
License:        Artistic-2.0

URL:            https://metacpan.org/release/Minion-Backend-SQLite/
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Minion-Backend-SQLite-v%{version}.tar.gz

BuildArch:      noarch
# build deps
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Carp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::SQLite) >= 3.000
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(strict)
# test deps
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Minion) >= 9.0
BuildRequires:  perl(Minion::Backend)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(constant)

%{?perl_default_filter}

%description
Minion::Backend::SQLite is a backend for Minion based on Mojo::SQLite. All
necessary tables will be created automatically with a set of migrations
named minion. If no connection string or :temp: is provided, the database
will be created in a temporary directory.

%prep
%setup -q -n Minion-Backend-SQLite-v%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes CONTRIBUTING.md examples README
%license LICENSE
%{perl_vendorlib}/Minion*
%{_mandir}/man3/Minion*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 5.0.7-6
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 14 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.7-1
- Update to 5.0.7

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.6-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 14 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.6-1
- Update to 5.0.6

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 19 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.5-1
- Update to 5.0.5

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.4-2
- Perl 5.34 rebuild

* Sun Feb 21 2021 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.4-1
- Update to 5.0.4

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 09 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.3-1
- Update to 5.0.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.2-1
- Update to 5.0.2

* Mon Jun 29 2020 Jitka Plesnikova <jplesnik@redhat.com> - 5.0.1-2
- Perl 5.32 re-rebuild updated packages

* Sun Jun 28 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 5.0.1-1
- Update to 5.0.1

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.005-3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 4.005-1
- Update to 4.005
- Replace calls to %%{__perl} to /usr/bin/perl

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 4.004-1
- Update to 4.004

* Sun Jun 23 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 4.003-1
- Update to 4.003

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.002-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Emmanuel Seyman <emmanuel@seyman.fr> 4.002-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.
