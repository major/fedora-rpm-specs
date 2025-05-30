# generated by cabal-rpm-2.3.0
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

Name:           bench
Version:        1.0.13
Release:        %autorelease
Summary:        Command-line benchmark tool

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/bench
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}.cabal#/%{name}-%{version}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-criterion-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-silently-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-turtle-devel
BuildRequires:  help2man
# End cabal-rpm deps

%description
Think of this as a more powerful alternative to the 'time' command.
Use this command-line tool to benchmark a command using Haskell's 'criterion'
library.


%prep
# Begin cabal-rpm setup:
%setup -q
dos2unix -k -n %{SOURCE1} %{name}.cabal
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_bin_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_bin_install

set noclobber
mkdir -p %{buildroot}%{bash_completions_dir}
%{buildroot}%{_bindir}/%{name} --bash-completion-script %{name} | sed s/filenames/default/ > %{buildroot}%{bash_completions_dir}/%{name}

mkdir -p %{buildroot}%{_mandir}/man1/
help2man --no-info %{buildroot}%{_bindir}/%{name} > %{buildroot}%{_mandir}/man1/%{name}.1
# End cabal-rpm install


%files
# Begin cabal-rpm files:
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{bash_completions_dir}/%{name}
%{_mandir}/man1/%{name}.1*
# End cabal-rpm files


%changelog
%autochangelog
