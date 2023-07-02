%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# Fedora does not have ezjsonm
%global run_tests 0

Name:           ocaml-ppx-deriving-yaml
Version:        0.2.1
Release:        %autorelease
Summary:        Derive conversion functions between OCaml types and YAML

License:        ISC
URL:            https://github.com/patricoferris/ppx_deriving_yaml
Source0:        %{url}/releases/download/v%{version}/ppx_deriving_yaml-%{version}.tbz

BuildRequires:  ocaml >= 4.08.1
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-ppx-deriving-devel
BuildRequires:  ocaml-ppxlib-devel >= 0.14.0
BuildRequires:  ocaml-yaml-devel

# Test dependencies
%if %{run_tests}
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-bos-devel
BuildRequires:  ocaml-mdx-devel
BuildRequires:  ocaml-ezjsonm-devel
%endif

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
%dune_build

%install
%dune_install

%if %{run_tests}
%check
%dune_check
%endif

%files -f .ofiles
%license LICENSE.md
%doc README.md CHANGES.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
