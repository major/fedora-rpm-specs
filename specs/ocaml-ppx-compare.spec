# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# This package is now a transitive dependency of ocaml-ppx-inline-test, so using
# it to test this package creates a circular dependency.
%bcond test 0

Name:           ocaml-ppx-compare
Version:        0.17.0
Release:        %autorelease
Summary:        Generate comparison functions from types

License:        MIT
URL:            https://github.com/janestreet/ppx_compare
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_compare-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0
BuildRequires:  ocaml-ppxlib-jane-devel >= 0.17

%if %{with test}
BuildRequires:  ocaml-ppx-inline-test-devel
%endif

%description
Ppx_compare is a ppx rewriter that derives comparison and equality functions
from type representations.  The scaffolded functions are usually much faster
than OCaml's `Stdlib.compare` and `Stdlib.(=)`.  Scaffolding functions also
give more flexibility by allowing them to be overridden for a specific type,
and more safety by making sure that only comparable values are compared.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-ppxlib-jane-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ppx_compare-%{version} -p1

%build
%dune_build

%install
%dune_install

%if %{with test}
# The tests require a native build.
%ifnarch %{ocaml_native_compiler}
%check
%dune_check
%endif
%endif

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
