Name:           pgbadger
Version:        13.0
Release:        %autorelease
Summary:        PostgreSQL log analyzer with fully detailed reports and graphs


# List of all licenses - each with an example of a file that uses it
# PostgreSQL: pgbadger
# MIT: resources/jqplot
# Artistic-2.0: pgbadger
# OFL-1.1: resources/fontawesome.css
# CC-BY-3.0: /resources/jqplot.canvasTextRenderer.js
# GPL-2.0-only: resources/jqplot.*
License:        PostgreSQL AND MIT AND Artistic-2.0 AND OFL-1.1 AND CC-BY-3.0 AND GPL-2.0-only
URL:            https://github.com/darold/%{name}
Source:         https://github.com/darold/%{name}/archive/refs/tags/v%{version}.tar.gz

# upstream commit: https://github.com/darold/pgbadger/commit/31978811d1ce4ef7f07813a17cf4e736d92d7428
Patch0:         %{name}-13.0-Fix-for-perl-5.40.patch
# Update Makefile.PL to not ignore command line arguments
Patch1:         %{name}-13.0-Update-Makefile.patch

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(constant)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(Text::CSV)
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

# podchecker
BuildRequires:  perl-Pod-Checker
# pod2markdown
BuildRequires:  perl-Pod-Markdown

Requires:       perl(Text::CSV_XS)

%description
PgBadger is a PostgreSQL log analyzer built for speed providing fully 
detailed reports based on your PostgreSQL log files. It's a small 
standalone Perl script that outperforms any other PostgreSQL log analyzer.


%prep
%autosetup

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} %{buildroot}/%{_bindir}/pgbadger

%check
make test

%files
%doc README
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1p.*


%changelog
%autochangelog
