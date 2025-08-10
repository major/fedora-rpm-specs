Name:           ack
Version:        3.9.0
Release:        %autorelease
Summary:        A Grep-like source code search tool
# SPDX migration
License:        Artistic-2.0
URL:            http://beyondgrep.com/
Source:         https://github.com/beyondgrep/ack3/archive/v%{version}/ack3-%{version}.tar.gz
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
BuildRequires:  perl(Template)
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
BuildRequires:  perl(YAML::PP)
Requires:       perl(File::Basename) >= 1.00015
Requires:       perl(Config)
Requires:       perl(File::Next) >= 1.18
Requires:       perl(List::Util)
Requires:       perl(Pod::Usage) >= 1.26

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(File::Next\\)

%description
Ack is a grep-like search tool designed for use with large heterogeneous
trees of source code.  It searchs recursively and ignores common version
control directories.

%prep
%setup -q -n ack3-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

make completion.bash
make completion.zsh

%install
%{make_install}

install -D -p -m 0644 completion.bash %{buildroot}%{bash_completions_dir}/ack
install -D -p -m 0644 completion.zsh  %{buildroot}%{zsh_completions_dir}/_ack

%{_fixperms} %{buildroot}/*


%check
make test

%files
%doc Changes README.md
%license LICENSE.md
%{perl_vendorlib}/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{bash_completions_dir}/ack
%{zsh_completions_dir}/_ack


%changelog
%autochangelog
