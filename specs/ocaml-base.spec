# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# This package is needed to build ppx_jane, but its tests require ppx_jane.
# Break the dependency cycle here.
%bcond test 0

%global giturl  https://github.com/janestreet/base

Name:           ocaml-base
Version:        0.17.2
Release:        %autorelease
Summary:        Jane Street standard library for OCaml

# MIT: The project as a whole
# Apache-2.0: src/map.ml, src/random.mli, src/set.ml
License:        MIT AND Apache-2.0
URL:            https://opensource.janestreet.com/base/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/base-%{version}.tar.gz
# Expose a dependency on the math library so RPM can see it
Patch:          %{name}-mathlib.patch
# Do not use the popcount instruction until Fedora moves to x86_64-v2
Patch:          %{name}-popcount.patch

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-intrinsics-kernel-devel
BuildRequires:  ocaml-sexplib0-devel

%if %{with test}
BuildRequires:  ocaml-core-devel
BuildRequires:  ocaml-expect-test-helpers-core-devel
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-ppx-jane-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-stdio-devel
%endif

%description
Base is a standard library for OCaml.  It provides a standard set of
general purpose modules that are well-tested, performant, and
fully-portable across any environment that can run OCaml code.  Unlike
other standard library projects, Base is meant to be used as a wholesale
replacement of the standard library distributed with the OCaml compiler.
In particular it makes different choices and doesn't re-export features
that are not fully portable such as I/O, which are left to other
libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-intrinsics-kernel-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n base-%{version} -p1

%build
%dune_build

%install
%dune_install

%if %{with test}
%check
%dune_check
%endif

%files -f .ofiles
%doc CHANGES.md README.org ROADMAP.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
