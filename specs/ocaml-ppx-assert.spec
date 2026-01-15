# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-ppx-assert
Version:        0.17.0
Release:        %autorelease
Summary:        Assert-like extension nodes that raise useful errors on failure

License:        MIT
URL:            https://github.com/janestreet/ppx_assert
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_assert-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppx-cold-devel >= 0.17
BuildRequires:  ocaml-ppx-compare-devel >= 0.17
BuildRequires:  ocaml-ppx-here-devel >= 0.17
BuildRequires:  ocaml-ppx-sexp-conv-devel >= 0.17
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0

%description
Ppx_assert is a ppx rewriter that defines assert-like extension nodes that
raise useful errors on failure.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppx-compare-devel%{?_isa}
Requires:       ocaml-ppx-here-devel%{?_isa}
Requires:       ocaml-ppx-sexp-conv-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ppx_assert-%{version}

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
