# generated by cabal-rpm-2.3.0
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name dhall
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

# testsuite missing deps: generic-random special-values spoon tasty-expected-failure tasty-silver

Name:           %{pkg_name}
Version:        1.42.2
Release:        %autorelease
Summary:        A configuration language guaranteed to terminate

License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/dhall
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-atomic-write-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-cborg-json-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-cryptohash-sha256-devel
BuildRequires:  ghc-data-fix-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-dotgen-devel
BuildRequires:  ghc-either-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-half-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-haskeline-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-indexed-traversable-devel
BuildRequires:  ghc-lens-family-core-devel
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-mmorph-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-parser-combinators-devel
BuildRequires:  ghc-parsers-devel
BuildRequires:  ghc-pretty-simple-devel
BuildRequires:  ghc-prettyprinter-devel
BuildRequires:  ghc-prettyprinter-ansi-terminal-devel
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-repline-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-serialise-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-manipulate-devel
BuildRequires:  ghc-text-short-devel
BuildRequires:  ghc-th-lift-instances-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-compat-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
%if %{with ghc_prof}
BuildRequires:  ghc-Diff-prof
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-aeson-pretty-prof
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-atomic-write-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base16-bytestring-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-cborg-prof
BuildRequires:  ghc-cborg-json-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-contravariant-prof
BuildRequires:  ghc-cryptohash-sha256-prof
BuildRequires:  ghc-data-fix-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-dotgen-prof
BuildRequires:  ghc-either-prof
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-half-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-haskeline-prof
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-http-client-tls-prof
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-indexed-traversable-prof
BuildRequires:  ghc-lens-family-core-prof
BuildRequires:  ghc-megaparsec-prof
BuildRequires:  ghc-mmorph-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-parser-combinators-prof
BuildRequires:  ghc-parsers-prof
BuildRequires:  ghc-pretty-simple-prof
BuildRequires:  ghc-prettyprinter-prof
BuildRequires:  ghc-prettyprinter-ansi-terminal-prof
BuildRequires:  ghc-profunctors-prof
BuildRequires:  ghc-repline-prof
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-serialise-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-text-manipulate-prof
BuildRequires:  ghc-text-short-prof
BuildRequires:  ghc-th-lift-instances-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-unix-compat-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-prof
%endif
Requires:       %{name}-common = %{version}-%{release}
# End cabal-rpm deps

%description
Dhall is an explicitly typed configuration language that is not Turing
complete. Despite being Turing incomplete, Dhall is a real programming language
with a type-checker and evaluator.

Use this library to parse, type-check, evaluate, and pretty-print the Dhall
configuration language. This package also includes an executable which
type-checks a Dhall file and reduces the file to a fully evaluated normal form.

Read "Dhall.Tutorial" to learn how to use this library.


%package common
Summary:        %{name} common files
BuildArch:      noarch

%description common
This package provides the %{name} common data files.


%package -n ghc-%{name}
Summary:        Haskell %{name} library
Requires:       %{name}-common = %{version}-%{release}

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.


%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Provides:       ghc-%{name}-static = %{version}-%{release}
Provides:       ghc-%{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       ghc-%{name}%{?_isa} = %{version}-%{release}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.


%if %{with haddock}
%package -n ghc-%{name}-doc
Summary:        Haskell %{name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem

%description -n ghc-%{name}-doc
This package provides the Haskell %{name} library documentation.
%endif


%if %{with ghc_prof}
%package -n ghc-%{name}-prof
Summary:        Haskell %{name} profiling library
Requires:       ghc-%{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (ghc-%{name}-devel and ghc-prof)

%description -n ghc-%{name}-prof
This package provides the Haskell %{name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
mv %{buildroot}%{_ghcdocdir}{,-common}

set noclobber
mkdir -p %{buildroot}%{bash_completions_dir}
%{buildroot}%{_bindir}/%{name} --bash-completion-script %{name} | sed s/filenames/default/ > %{buildroot}%{bash_completions_dir}/%{name}

mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 -p -t %{buildroot}%{_mandir}/man1/ ./man/dhall.1
# End cabal-rpm install


%files
# Begin cabal-rpm files:
%{_bindir}/%{name}
%{bash_completions_dir}/%{name}
%{_mandir}/man1/dhall.1*
# End cabal-rpm files


%files common
# Begin cabal-rpm files:
%license LICENSE
%doc CHANGELOG.md
%{_datadir}/%{pkgver}
# End cabal-rpm files


%files -n ghc-%{name} -f ghc-%{name}.files


%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files


%if %{with haddock}
%files -n ghc-%{name}-doc -f ghc-%{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files -n ghc-%{name}-prof -f ghc-%{name}-prof.files
%endif


%changelog
%autochangelog
