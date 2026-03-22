%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-store
Version:        0.1
Release:        %autorelease
Summary:        Snapshottable data structures

# The overarching project license is MIT.  Files with other license are present
# in the the bench and fuzzing subdirectories, but they are neither built nor
# shipped in any binary RPM.
# LGPL-2.1-only:
# - bench/vendor/colibri2/context.ml
# LGPL-2.1-or-later:
# - bench/vendor/facile/*.ml
# LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception:
# - bench/StoreBacktrackingRef.ml
# - bench/StoreMap.ml
# - bench/StoreRef.ml
# - bench/StoreTransactionalRef.ml
# - bench/StoreVector.ml
License:        MIT
SourceLicense:  %{license} AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://gitlab.com/basile.clement/store
VCS:            git:%{url}.git
Source:         %{url}/-/archive/v%{version}/store-v%{version}.tar.bz2

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.05
BuildRequires:  ocaml-dune >= 3.7

%description
`Store` is a library to add snapshotting capabilities to imperative data
structures with low runtime cost and safe, user-friendly APIs.  It is designed
for (and works best with) applications that exploit backtracking algorithms,
such as SMT solvers, type-checking and type-inference algorithms.

Currently, `Store` only provides snapshottable references; support for custom
built-in data structures that benefit from non-backtracked operations (such as
resizing a dynamic array) is planned.

The design of the Store library is described in the ICFP'24 paper:

    Clément Allain, Basile Clément, Alexandre Moine, and Gabriel Scherer. 2024.
    Snapshottable Stores.
    Proc. ACM Program. Lang. 8, ICFP, Article 248 (August 2024), 32 pages.
    https://doi.org/10.1145/3674637

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n store-v%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license LICENSE
%doc CHANGES.md README.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
