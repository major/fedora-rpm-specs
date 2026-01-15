# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-ppx-variants-conv
Version:        0.17.1
Release:        %autorelease
Summary:        Generate accessor & iteration functions for OCaml variant types

License:        MIT
URL:            https://github.com/janestreet/ppx_variants_conv
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_variants_conv-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppxlib-devel >= 0.36.0
BuildRequires:  ocaml-ppx-inline-test-devel
BuildRequires:  ocaml-variantslib-devel >= 0.17

%description
Ppx_variants_conv is a ppx rewriter that can be used to define first-class
values representing variant constructors, and additional routines to fold,
iterate and map over all constructors of a variant type.  It provides
corresponding functionality for variant types as ppx_fields_conv provides for
record types.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-variantslib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n ppx_variants_conv-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
