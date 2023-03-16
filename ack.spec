Name:           ack
Version:        3.7.0
%global cpan_version v%{version}
Release:        %autorelease
Summary:        Grep-like text finder
# SPDX migration
License:        Artistic-2.0
URL:            http://beyondgrep.com/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/%{name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd) >= 3.00
BuildRequires:  perl(File::Basename) >= 1.00015
BuildRequires:  perl(File::Next) >= 1.18
BuildRequires:  perl(File::Spec) >= 3.00
BuildRequires:  perl(filetest)
BuildRequires:  perl(Getopt::Long) >= 2.39
BuildRequires:  perl(if)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Usage) >= 1.26
BuildRequires:  perl(Text::ParseWords) >= 3.1
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp) >= 1.04
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Command::MM)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(IO::Pty)
BuildRequires:  perl(lib)
BuildRequires:  perl(Pod::Perldoc) >= 3.20
BuildRequires:  perl(Pod::Text)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Term::ANSIColor) >= 1.10
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Harness) >= 2.5
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(File::Basename) >= 1.00015
Requires:       perl(Config)
Requires:       perl(File::Next) >= 1.18
Requires:       perl(List::Util)
Requires:       perl(Pod::Usage) >= 1.26

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(File::Next\\)

%description
Ack is designed as a replacement for grep.

%prep
%setup -q -n %{name}-%{cpan_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README.md
%license LICENSE.md
%{perl_vendorlib}/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
%autochangelog
