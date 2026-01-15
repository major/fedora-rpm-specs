# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-ppx-base
Version:        0.17.0
Release:        %autorelease
Summary:        Base set of OCaml ppx rewriters

License:        MIT
URL:            https://github.com/janestreet/ppx_base
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_base-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppx-cold-devel >= 0.17
BuildRequires:  ocaml-ppx-compare-devel >= 0.17
BuildRequires:  ocaml-ppx-enumerate-devel >= 0.17
BuildRequires:  ocaml-ppx-globalize-devel >= 0.17
BuildRequires:  ocaml-ppx-hash-devel >= 0.17
BuildRequires:  ocaml-ppx-sexp-conv-devel >= 0.17
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0

%description
Ppx_base is the set of ppx rewriters used for Base.  Note that Base doesn't
need ppx to build; it is only used as a verification tool.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-cold-devel%{?_isa}
Requires:       ocaml-ppx-compare-devel%{?_isa}
Requires:       ocaml-ppx-enumerate-devel%{?_isa}
Requires:       ocaml-ppx-globalize-devel%{?_isa}
Requires:       ocaml-ppx-hash-devel%{?_isa}
Requires:       ocaml-ppx-sexp-conv-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ppx_base-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
