Name:           perl-CLI-Simple
Version:        2.1.1
Release:        1%{?dist}
Summary:        Minimalist object oriented base class for CLI applications
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/CLI-Simple
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BIGFOOT/CLI-Simple-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(Class::Accessor::Fast) >= 0.51
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir) >= 1.118
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Which) >= 1.23
BuildRequires:  perl(IO::Interactive)
BuildRequires:  perl(IO::Pager)
BuildRequires:  perl(JSON) >= 4.07
BuildRequires:  perl(List::Util) >= 1.56
BuildRequires:  perl(Log::Log4perl) >= 1.57
BuildRequires:  perl(Log::Log4perl::Level)
BuildRequires:  perl(Readonly) >= 2.05
BuildRequires:  perl(Role::Tiny) >= 2.002004
BuildRequires:  perl(Test::Exit) >= 0.11
BuildRequires:  perl(Test::Output) >= 1.036
BuildRequires:  perl(YAML::Tiny) >= 1.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::ShareDir) >= 1.118
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(JSON) >= 4.07
BuildRequires:  perl(List::Util) >= 1.56
BuildRequires:  perl(Log::Log4perl) >= 1.57
BuildRequires:  perl(Log::Log4perl::Level)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Readonly) >= 2.05
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(YAML::Tiny) >= 1.76
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# tests
BuildRequires:  perl(FindBin)
Requires:       perl(File::ShareDir) >= 1.118
Requires:       perl(YAML::Tiny) >= 1.76
Recommends:     perl(IO::Pager)
Recommends:     perl(Term::ANSIColor)

%description
Tired of writing the same 'ol boilerplate code for command line scripts?
Want a standard, simple way to create a Perl script that takes options and
commands? CLI::Simple makes it easy to create scripts that take options,
commands and arguments.

%prep
%setup -q -n CLI-Simple-%{version}
> postamble

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
ln -sf ../CLI::Simple.3pm $RPM_BUILD_ROOT%{_mandir}/man3/cli-simple.3pm

%check
make test

%files
%doc ChangeLog README.md
%{perl_vendorlib}/CLI/
%{_mandir}/man3/cli-simple.3pm*
%{_mandir}/man3/CLI::Simple*3pm*
%{_bindir}/cli-simple
%{_bindir}/create-modulino

%changelog
* Fri Jul 24 2026 Xavier Bachelot <xavier@bachelot.org> 2.1.1-1
- Update to 2.1.1

* Fri Jul 17 2026 Xavier Bachelot <xavier@bachelot.org> 2.0.14-1
- Initial specfile
