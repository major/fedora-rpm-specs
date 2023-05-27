Name:           perl-Term-Shell
Version:        0.13
Release:        %autorelease
Summary:        Simple command-line shell framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-Shell
Source0:        https://cpan.metacpan.org/modules/by-module/Term/Term-Shell-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Module Run-time:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(Term::ReadLine)
# Optional, but upstream's metadata says required Run-Time:
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Text::Autoformat)
# Optional Run-time:
#BuildRequires: perl(Term::InKey)  not yet packaged in Fedora
#BuildRequires: perl(Term::Screen) not yet packaged in Fedora
BuildRequires:  perl(Term::Size)
# Test:
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
# Dependencies:
Requires:       perl(File::Temp)
Requires:       perl(Term::ReadKey)
Requires:       perl(Text::Autoformat)
Suggests:       perl(Term::InKey)
Suggests:       perl(Term::Screen)
Suggests:       perl(Term::Size)

# tests sub-package dropped during development phase for Fedora 32
Obsoletes:     perl-Term-Shell-tests < %{version}-%{release}
Provides:      perl-Term-Shell-tests = %{version}-%{release}

%description
Term::Shell lets you write simple command-line shells. All the boring
details like command-line parsing, terminal handling, and tab completion
are handled for you.

%prep
%setup -q -n Term-Shell-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes examples/ README t/
%{perl_vendorlib}/Term/
%{_mandir}/man3/Term::Shell.3*

%changelog
%autochangelog
