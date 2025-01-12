# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/ocaml-ppx/ppx_deriving

Name:           ocaml-ppx-deriving
Version:        6.0.3
Release:        %autorelease
Summary:        Type-driven code generation for OCaml

License:        MIT
URL:            https://ocaml-ppx.github.io/ppx_deriving/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/ppx_deriving-%{version}.tar.gz

BuildRequires:  ocaml >= 4.05.0
BuildRequires:  ocaml-cppo >= 1.1.0
BuildRequires:  ocaml-dune >= 1.6.3
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-ppx-derivers-devel
BuildRequires:  ocaml-ppxlib-devel >= 0.32.0

%description
Deriving is a library simplifying type-driven code generation on OCaml.
It includes a set of useful plugins: show, eq, ord (eq), enum, iter,
map (iter), fold (iter), make, yojson, and protobuf.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-derivers-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ppx_deriving-%{version} -p1

%build
%dune_build

%install
%dune_install

# Help the debuginfo generator find the source files
cd _build/default
ln -s ../../src/ppx_deriving_main.cppo.ml
ln -s ../../src/api/ppx_deriving.cppo.ml .
ln -s ../../src/runtime/ppx_deriving_runtime.cppo.ml .
ln -s ../../src_plugins/create/ppx_deriving_create.cppo.ml .
ln -s ../../src_plugins/enum/ppx_deriving_enum.cppo.ml .
ln -s ../../src_plugins/eq/ppx_deriving_eq.cppo.ml .
ln -s ../../src_plugins/fold/ppx_deriving_fold.cppo.ml .
ln -s ../../src_plugins/iter/ppx_deriving_iter.cppo.ml .
ln -s ../../src_plugins/make/ppx_deriving_make.cppo.ml .
ln -s ../../src_plugins/map/ppx_deriving_map.cppo.ml .
ln -s ../../src_plugins/ord/ppx_deriving_ord.cppo.ml
ln -s ../../src_plugins/show/ppx_deriving_show.cppo.ml
cd -

%check
%dune_check

%files -f .ofiles
%doc CHANGELOG.md README.md
%license LICENSE.txt

%files devel -f .ofiles-devel

%changelog
%autochangelog
