Name:           perl-Carmel
Version:        0.1.56
Release:        %autorelease
Summary:        CPAN Artifact Repository Manager

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Carmel
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Carmel-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.129
BuildRequires:  perl(Carton) >= 1.0.35
BuildRequires:  perl(Class::Tiny) >= 1.001
BuildRequires:  perl(Config)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::Install) >= 1.47
BuildRequires:  perl(ExtUtils::InstallPaths)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::pushd) >= 1.009
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Menlo::CLI::Compat) >= 1.9018
BuildRequires:  perl(Module::CPANfile) >= 1.1000
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Metadata) >= 1.000003
BuildRequires:  perl(Module::Runtime) >= 0.014
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Path::Tiny) >= 0.068
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(Try::Tiny) >= 0.20
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

Requires:       perl(Carton::Dist)
Requires:       perl(Carton::Index)
Requires:       perl(Carton::Package)
Requires:       perl(Class::Tiny) >= 1.001
Requires:       perl(Data::Dumper)
Requires:       perl(ExtUtils::Install) >= 1.47
Requires:       perl(ExtUtils::InstallPaths)
Requires:       perl(File::pushd) >= 1.009
Requires:       perl(IO::Compress::Gzip)
Requires:       perl(Menlo::CLI::Compat) >= 1.9018
Requires:       perl(Module::CPANfile) >= 1.1000
Requires:       perl(Module::Metadata) >= 1.000003
Requires:       perl(Module::Runtime) >= 0.014
Requires:       perl(Path::Tiny) >= 0.068
Requires:       perl(Try::Tiny) >= 0.20
Requires:       perl(lib)
Recommends:     perl(Text::Diff)

%global __requires_exclude ^perl\\(((Class|Path|Try)::Tiny|File::pushd|Module::(CPANfile|Metadata|Runtime))
%{?perl_default_filter}


%description
Carmel is yet another CPAN module manager.

Unlike traditional CPAN module installer, Carmel keeps the build of your
dependencies in a central repository, then select the library paths to
include upon runtime in development.

Carmel also allows you to rollout all the files in a traditional perl
INC directory structure, which is useful to use in a production
environment, such as containers.


%prep
%autosetup -n Carmel-v%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} %{buildroot}/*


%check
make test


%files
%license LICENSE
%doc Changes README
%{_bindir}/carmel
%{_mandir}/man1/carmel.1*
%{_mandir}/man3/Carmel.3*
%{_mandir}/man3/Carmel::Preload.3*
%{_mandir}/man3/Carmel::Setup.3*
%dir %{perl_vendorlib}/Carmel
%{perl_vendorlib}/Carmel.pm
%{perl_vendorlib}/Carmel/App.pm
%{perl_vendorlib}/Carmel/Artifact.pm
%{perl_vendorlib}/Carmel/Builder.pm
%{perl_vendorlib}/Carmel/CPANfile.pm
%{perl_vendorlib}/Carmel/Difftool.pm
%{perl_vendorlib}/Carmel/Preload.pm
%{perl_vendorlib}/Carmel/ProgressBar.pm
%{perl_vendorlib}/Carmel/Repository.pm
%{perl_vendorlib}/Carmel/Resolver.pm
%{perl_vendorlib}/Carmel/Runner.pm
%{perl_vendorlib}/Carmel/Runtime.pm
%{perl_vendorlib}/Carmel/Setup.pm


%changelog
%autochangelog
