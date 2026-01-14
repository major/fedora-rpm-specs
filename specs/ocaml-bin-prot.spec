# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-bin-prot
Version:        0.17.0
Epoch:          1
Release:        %autorelease
Summary:        Read and write OCaml values in a type-safe binary protocol

# The project as a whole is MIT.
# Code in the src subdirectory is BSD-3-Clause.
License:        MIT AND BSD-3-Clause
URL:            https://github.com/janestreet/bin_prot
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/bin_prot-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppx-compare-devel >= 0.17
BuildRequires:  ocaml-ppx-custom-printf-devel >= 0.17
BuildRequires:  ocaml-ppx-fields-conv-devel >= 0.17
BuildRequires:  ocaml-ppx-optcomp-devel >= 0.17
BuildRequires:  ocaml-ppx-sexp-conv-devel >= 0.17
BuildRequires:  ocaml-ppx-stable-witness-devel >= 0.17
BuildRequires:  ocaml-ppx-variants-conv-devel >= 0.17

%description
This library contains functionality for reading and writing OCaml values in a
type-safe binary protocol.  These functions are extremely efficient and
provide users with a convenient and safe way of performing I/O on any
extensionally defined data type.  This means that functions, objects, and
values whose type is bound through a polymorphic record field are not
supported, but everything else is.

As of now, there is no support for cyclic or shared values.  Cyclic values
will lead to non-termination whereas shared values, besides requiring
significantly more space when encoded, may lead to a substantial increase in
memory footprint when they are read back in.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = 1:%{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-fieldslib-devel%{?_isa}
Requires:       ocaml-ppx-compare-devel%{?_isa}
Requires:       ocaml-ppx-sexp-conv-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}
Requires:       ocaml-ppx-stable-witness-devel%{?_isa}
Requires:       ocaml-variantslib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n bin_prot-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license COPYRIGHT.txt LICENSE.md LICENSE-Tywith.txt THIRD-PARTY.txt

%files devel -f .ofiles-devel

%changelog
%autochangelog
