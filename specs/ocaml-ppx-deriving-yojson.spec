# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-ppx-deriving-yojson
Version:        3.9.1
Release:        %autorelease
Summary:        JSON codec generator for OCaml

License:        MIT
URL:            https://github.com/ocaml-ppx/ppx_deriving_yojson
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_deriving_yojson-%{version}.tar.gz

BuildRequires:  ocaml >= 4.05.0
BuildRequires:  ocaml-dune >= 1.0
BuildRequires:  ocaml-ounit-devel >= 2.0.0
BuildRequires:  ocaml-ppx-deriving-devel >= 5.1
BuildRequires:  ocaml-ppxlib-devel >= 0.30.0
BuildRequires:  ocaml-yojson-devel >= 1.6.0

# This can be removed when F40 reaches EOL
Obsoletes:      ocaml-ppx-deriving-yojson-doc < 3.6.1-15

%description
Deriving_Yojson is a ppx_deriving plugin that generates JSON serializers
and deserializers that use the Yojson library from an OCaml type
definition.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-deriving-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-yojson-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and
signature files for developing applications that use
%{name}.

%prep
%autosetup -n ppx_deriving_yojson-%{version} -p1

# Fix version number
sed -i.orig 's/3\.7\.0/%{version}/' ppx_deriving_yojson.opam
touch -r ppx_deriving_yojson.opam.orig ppx_deriving_yojson.opam
rm ppx_deriving_yojson.opam.orig

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGELOG.md README.md
%license LICENSE.txt

%files devel -f .ofiles-devel

%changelog
%autochangelog
