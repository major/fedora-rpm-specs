# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-fmt
Version:        0.11.0
Release:        %autorelease
Summary:        OCaml Format pretty-printer combinators

License:        ISC
URL:            https://erratique.ch/software/fmt
VCS:            git:https://erratique.ch/repos/fmt.git
Source:         %{url}/releases/fmt-%{version}.tbz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-cmdliner-devel >= 1.3.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel >= 1.1.0

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings

%description
Fmt exposes combinators to devise `Format` pretty-printing functions.

Fmt depends only on the OCaml standard library.  The optional Fmt_tty
library that enables setting up formatters for terminal color output
depends on the Unix library.  The optional Fmt_cli library that provides
command line support for Fmt depends on Cmdliner.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-cmdliner-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n fmt-%{version} -p1

%conf
# link with the math library
sed -i 's/safe_string/&, cclib(-lm)/' _tags

%build
# Build the library and the tests
ocaml pkg/pkg.ml build \
  --dev-pkg false \
  --tests true \
  --with-base-unix true \
  --with-cmdliner true

# Build the documentation
mkdir html
ocamldoc -html -d html -I +cmdliner -I _build/src _build/src/*.mli

%install
%ocaml_install

%check
ocaml pkg/pkg.ml test

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel
%doc html/*

%changelog
%autochangelog
