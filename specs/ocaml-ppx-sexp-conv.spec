# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# This package is now a transitive dependency of ocaml-ppx-inline-test, so using
# it to test this package creates a circular dependency.
%bcond test 0

Name:           ocaml-ppx-sexp-conv
Version:        0.17.1
Release:        %autorelease
Summary:        Generate S-expression conversion functions from type definitions
License:        MIT
URL:            https://github.com/janestreet/ppx_sexp_conv
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_sexp_conv-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppxlib-devel >= 0.36.0
BuildRequires:  ocaml-ppxlib-jane-devel >= 0.17
BuildRequires:  ocaml-sexplib0-devel >= 0.17

%if %{with test}
BuildRequires:  ocaml-ppx-inline-test-devel
%endif

%description
Ppx_sexp_conv is a PPX syntax extension that generates code for
converting OCaml types to and from s-expressions, as defined in the
sexplib0 library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-ppxlib-jane-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n ppx_sexp_conv-%{version}

%build
%dune_build

%install
%dune_install

%if %{with test}
%check
%dune_check
%endif

%files -f .ofiles
%doc CHANGES.md README.org
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
