Name:           perl-Markdown-Render
Version:        2.0.4
Release:        1%{?dist}
Summary:        Render markdown as HTML
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Markdown-Render
Source0:        http://www.cpan.org/modules/by-module/Markdown/Markdown-Render-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16.0
BuildRequires:  perl(Class::Accessor::Fast) >= 0.51
BuildRequires:  perl(CLI::Simple) >= v1.0.11
BuildRequires:  perl(CLI::Simple::Constants) >= v1.0.11
BuildRequires:  perl(Config::Tiny) >= 2.30
BuildRequires:  perl(Date::Format) >= 2.24
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(English)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(IO::Scalar) >= 2.113
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(JSON) >= 4.10
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(Readonly) >= 2.05
# runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(parent)
BuildRequires:  perl(Text::Markdown::Discount)
# tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(FindBin)

%description
Renders markdown as HTML using either GitHub's API or
Text::Markdown::Discount. Optionally adds additional metadata to markdown
document using custom tags.

%prep
%setup -q -n Markdown-Render-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog README.md
%{perl_vendorlib}/Markdown/
%{_mandir}/man1/md-utils.1*
%{_mandir}/man3/Markdown::Render.3pm*
%{_bindir}/md-utils.pl

%changelog
* Tue May 26 2026 Xavier Bachelot <xavier@bachelot.org> 2.0.4-1
- Initial specfile
