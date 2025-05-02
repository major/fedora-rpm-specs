Name:           perl-App-perlimports
Version:        0.000057
Release:        %autorelease
Summary:        A command line utility for cleaning up imports in your Perl code

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/App-perlimports
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/App-perlimports-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  /usr/bin/chmod
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.18
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Class::Inspector) >= 1.36
BuildRequires:  perl(Cpanel::JSON::XS)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions) >= 3.75
BuildRequires:  perl(File::XDG) >= 1.01
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Geo::IP)
BuildRequires:  perl(Getopt::Long) >= 2.40
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(HTML::TableExtract)
BuildRequires:  perl(HTTP::Status) >= 6.28
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(Import::Into)
BuildRequires:  perl(LWP::UserAgent) >= 5
BuildRequires:  perl(Lingua::EN::Inflect)
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Dispatch) >= 2.70
BuildRequires:  perl(Log::Dispatch::Array)
BuildRequires:  perl(Memoize)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Mojolicious) >= 8.25
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::StrictConstructor)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(PPI) >= 1.276
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(PPI::Dumper)
BuildRequires:  perl(PPIx::Utils::Classification)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Path::Iterator::Rule)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Perl::Tidy) >= 20220613
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sereal::Decoder)
BuildRequires:  perl(Sereal::Encoder)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::HandlesVia)
BuildRequires:  perl(Symbol::Get) >= 0.10
BuildRequires:  perl(TOML::Tiny) >= 0.16
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::HTML::Lint)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(Test::Script) >= 1.29
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(Text::SimpleTable::AutoWidth)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(UUID)
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

## These are required to run optional tests, but, at the time of
## writing, are not packaged for Fedora:
# BuildRequires:  perl(IP::Random) >= 1.200230
# BuildRequires:  perl(MetaCPAN::Moose)
# BuildRequires:  perl(MooseX::Types::UUID)
# BuildRequires:  perl(Object::Tap)
# BuildRequires:  perl(Pithub)

Requires:  perl(File::XDG) >= 1.01
Requires:  perl(Perl::Tidy) >= 20220613
Requires:  perl(Symbol::Get) >= 0.10
Requires:  perl(TOML::Tiny) >= 0.16

%{?perl_default_filter}


%description
This distribution provides the perlimports command line interface (CLI),
which automates the cleanup and maintenance of Perl use and require
statements. Loosely inspired by goimports, this tool aims to be part of
your linting and tidying workflow, in much the same way you might use
perltidy or perlcritic.


%prep
%autosetup -n App-perlimports-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*


%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test


%files
%license LICENSE
%doc CONTRIBUTORS
%doc Changes
%doc README.md
%{_bindir}/dump-perl-exports
%{_bindir}/perlimports
%{_mandir}/man1/dump-perl-exports.1*
%{_mandir}/man1/perlimports.1*
%{_mandir}/man3/App::perlimports.3pm*
%{_mandir}/man3/App::perlimports::Annotations.3pm*
%{_mandir}/man3/App::perlimports::CLI.3pm*
%{_mandir}/man3/App::perlimports::Config.3pm*
%{_mandir}/man3/App::perlimports::Document.3pm*
%{_mandir}/man3/App::perlimports::ExportInspector.3pm*
%{_mandir}/man3/App::perlimports::Include.3pm*
%{_mandir}/man3/App::perlimports::Role::Logger.3pm*
%{_mandir}/man3/App::perlimports::Sandbox.3pm*
%dir %{perl_vendorlib}/App
%dir %{perl_vendorlib}/App/perlimports
%dir %{perl_vendorlib}/App/perlimports/Role
%{perl_vendorlib}/App/perlimports.pm
%{perl_vendorlib}/App/perlimports/Annotations.pm
%{perl_vendorlib}/App/perlimports/CLI.pm
%{perl_vendorlib}/App/perlimports/Config.pm
%{perl_vendorlib}/App/perlimports/Document.pm
%{perl_vendorlib}/App/perlimports/ExportInspector.pm
%{perl_vendorlib}/App/perlimports/Include.pm
%{perl_vendorlib}/App/perlimports/Role/Logger.pm
%{perl_vendorlib}/App/perlimports/Sandbox.pm


%changelog
%autochangelog
