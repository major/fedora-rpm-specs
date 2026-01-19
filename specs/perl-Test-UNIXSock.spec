Name:           perl-Test-UNIXSock
Version:        0.4
Release:        2%{?dist}
Summary:        Testing UNIX domain socket program
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-UNIXSock
Source0:        https://www.cpan.org/modules/by-module/Test/Test-UNIXSock-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::SharedFork) >= 0.29
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(lib)
Requires:       perl(Test::More) >= 0.98
Requires:       perl(Test::SharedFork) >= 0.29

# Filter under-specified requires
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Test::More\\)|Test::SharedFork\\) >= 0\\.12)$

%description
Test::UNIXSock is a test utility to test UNIX domain socket server
programs.

%prep
%setup -q -n Test-UNIXSock-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::UNIXSock.3pm*

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Apr 14 2025 Xavier Bachelot <xavier@bachelot.org> 0.4-1
- Initial spec file
