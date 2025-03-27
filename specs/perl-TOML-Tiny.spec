Name:           perl-TOML-Tiny
Version:        0.20
Release:        %autorelease
Summary:        A minimal, pure perl TOML parser and serializer

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/TOML-Tiny
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/TOML-Tiny-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  /usr/bin/chmod
BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.18
BuildRequires:  perl(B)
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(DateTime::Format::RFC3339)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Math::BigInt) >= 1.999718
BuildRequires:  perl(TOML::Parser)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Unicode::GCString)
BuildRequires:  perl(charnames)
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

%{?perl_default_filter}


%description
TOML::Tiny implements a pure-perl parser and generator for the TOML data
format. It conforms to TOML v1.0 (with a few caveats)

%prep
%autosetup -n TOML-Tiny-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%license LICENSE
%doc Changes
%doc README
%{_mandir}/man3/TOML::Tiny.3pm*
%{_mandir}/man3/TOML::Tiny::Grammar.3pm*
%{_mandir}/man3/TOML::Tiny::Parser.3pm*
%{_mandir}/man3/TOML::Tiny::Tokenizer.3pm*
%{_mandir}/man3/TOML::Tiny::Util.3pm*
%{_mandir}/man3/TOML::Tiny::Writer.3pm*
%dir %{perl_vendorlib}/TOML
%dir %{perl_vendorlib}/TOML/Tiny
%{perl_vendorlib}/TOML/Tiny.pm
%{perl_vendorlib}/TOML/Tiny/Grammar.pm
%{perl_vendorlib}/TOML/Tiny/Parser.pm
%{perl_vendorlib}/TOML/Tiny/Tokenizer.pm
%{perl_vendorlib}/TOML/Tiny/Util.pm
%{perl_vendorlib}/TOML/Tiny/Writer.pm


%changelog
%autochangelog
