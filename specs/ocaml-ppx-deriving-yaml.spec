# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-ppx-deriving-yaml
Version:        0.4.0
Release:        %autorelease
Summary:        Derive conversion functions between OCaml types and YAML

License:        ISC
URL:            https://github.com/patricoferris/ppx_deriving_yaml
VCS:            git:%{url}.git
Source:         %{url}/releases/download/v%{version}/ppx_deriving_yaml-%{version}.tbz

BuildRequires:  ocaml >= 4.08.1
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune >= 3.14
BuildRequires:  ocaml-mdx-devel >= 2.4.1
BuildRequires:  ocaml-ppx-deriving-devel
BuildRequires:  ocaml-ppxlib-devel >= 0.25.0
BuildRequires:  ocaml-yaml-devel

%description
This ppx is based on ppx_yojson [1] and ppx_deriving_yojson [2] because
of the many similarities between JSON and yaml.  In particular many of
the ways OCaml values are encoded to yaml types are the same as those
implemented by the Yojson ppx.

References:
[1] https://github.com/NathanReb/ppx_yojson
[2] https://github.com/ocaml-ppx/ppx_deriving_yojson

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-deriving-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-yaml-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n ppx_deriving_yaml-%{version}

%build
%dune_build -p ppx_deriving_yaml

%install
%dune_install ppx_deriving_yaml

%check
%dune_check -p ppx_deriving_yaml

%files -f .ofiles
%license LICENSE.md
%doc README.md CHANGES.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
