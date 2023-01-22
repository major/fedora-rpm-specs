Name:           perl-Test-mysqld
Version:        1.0013
Release:        10%{?dist}
Summary:        Mysqld runner for tests
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-mysqld

Source0:        https://cpan.metacpan.org/authors/id/S/SO/SONGMU/Test-mysqld-%{version}.tar.gz
# Adjust to changes in MariaDB 10.4.3, bug #1793917,
# <https://github.com/kazuho/p5-test-mysqld/issues/32>
Patch0:         Test-mysqld-1.0012-Use-UNIX-socket-authentication-with-MariaDB-10.4.3.patch
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)

# Run-time
BuildRequires:  perl(Class::Accessor::Lite)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBI)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
BuildRequires:  mariadb-server

# Testing
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::SharedFork) >= 0.06

Requires:       perl(DBD::mysql)
Requires:       perl(File::Basename)
Requires:       perl(File::Spec)
Requires:       mariadb-server

%description
Test::mysqld automatically setups a mysqld instance in a temporary
directory, and destroys it when the perl script exits.

%prep
%setup -q -n Test-mysqld-%{version}
%patch0 -p1

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%check
AUTHOR_TESTING=1 RELEASE_TESTING=1 ./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0013-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0013-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.0013-8
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0013-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0013-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.0013-5
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0013-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0013-2
- Perl 5.32 rebuild

* Fri Apr 10 2020 Denis Fateyev <denis@fateyev.com> - 1.0013-1
- Update to 1.0013 release

* Wed Apr 01 2020 Petr Pisar <ppisar@redhat.com> - 1.0012-6
- Adjust to changes in MariaDB 10.4.3 (bug #1793917)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0012-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.0012-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0012-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Denis Fateyev <denis@fateyev.com> - 1.0012-1
- Update to 1.0012 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.0000-2
- Perl 5.28 rebuild

* Wed May 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.0000-1
- 1.0000 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-2
- Perl 5.26 rebuild

* Fri Apr 14 2017 Denis Fateyev <denis@fateyev.com> - 0.21-1
- Update to 0.21 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 24 2016 Denis Fateyev <denis@fateyev.com> - 0.20-1
- Update to 0.20 release

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Denis Fateyev <denis@fateyev.com> - 0.17-3
- Small spec cleanup

* Wed Nov 18 2015 Denis Fateyev <denis@fateyev.com> - 0.17-2
- Fixing mysql-server dependency, RHBZ #1282956

* Mon Nov 16 2015 Denis Fateyev <denis@fateyev.com> - 0.17-1
- Initial release
