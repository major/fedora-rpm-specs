%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-ppx-deriving-yaml
Version:        0.5.0
Release:        %autorelease
Summary:        Derive conversion functions between OCaml types and YAML

License:        ISC
URL:            https://github.com/patricoferris/ppx_deriving_yaml
VCS:            git:%{url}.git
Source:         %{url}/releases/download/v%{version}/ppx_deriving_yaml-%{version}.tbz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildSystem: dune
BuildOption(build): -p ppx_deriving_yaml,ppx_deriving_yamlx
BuildOption(install): -s ppx_deriving_yaml ppx_deriving_yamlx
BuildOption(check): -p ppx_deriving_yaml,ppx_deriving_yamlx

BuildRequires:  ocaml >= 4.08.1
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune >= 3.21
BuildRequires:  ocaml-mdx-devel >= 2.4.1
BuildRequires:  ocaml-ppx-deriving-devel
BuildRequires:  ocaml-ppxlib-devel >= 0.36.0
BuildRequires:  ocaml-yaml-devel
BuildRequires:  ocaml-yamlx-devel >= 0.5.0

%description
This ppx is based on ppx_yojson [1] and ppx_deriving_yojson [2] because of the
many similarities between JSON and yaml.  In particular many of the ways OCaml
values are encoded to yaml types are the same as those implemented by the
Yojson ppx.

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

%package -n     %{name}x
Summary:        Derive conversion functions between OCaml types and YAML with YAMLx

%description -n %{name}x
This ppx is based on ppx_yojson [1] and ppx_deriving_yojson [2] because of the
many similarities between JSON and yaml.  In particular many of the ways OCaml
values are encoded to yaml types are the same as those implemented by the
Yojson ppx.  This package uses ocaml-yamlx instead of ocaml-yaml.

References:
[1] https://github.com/NathanReb/ppx_yojson
[2] https://github.com/ocaml-ppx/ppx_deriving_yojson

%package -n     %{name}x-devel
Summary:        Development files for %{name}
Requires:       %{name}x%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-deriving-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-yamlx-devel%{?_isa}

%description -n %{name}x-devel
The %{name}x-devel package contains libraries and signature
files for developing applications that use %{name}x.

%prep
%autosetup -n ppx_deriving_yaml-%{version}

%files -f .ofiles-ppx_deriving_yaml
%license LICENSE.md
%doc README.md CHANGES.md

%files devel -f .ofiles-ppx_deriving_yaml-devel

%files -n %{name}x -f .ofiles-ppx_deriving_yamlx
%license LICENSE.md
%doc README.md CHANGES.md

%files -n %{name}x-devel -f .ofiles-ppx_deriving_yamlx-devel

%changelog
%autochangelog
