# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-ppx-let
Version:        0.17.1
Release:        %autorelease
Summary:        Monadic let-bindings for OCaml

License:        MIT
URL:            https://github.com/janestreet/ppx_let
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_let-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppx-here-devel >= 0.17
BuildRequires:  ocaml-ppxlib-devel >= 0.36.0

%description
Ppx_let is a ppx rewriter for monadic and applicative let bindings, match
expressions, and if expressions.

The aim of this rewriter is to make monadic and applicative code look nicer by
writing custom binders the same way that we normally bind variables.  In
OCaml, the common way to bind the result of a computation to a variable is:
```
  let VAR = EXPR in BODY
```
ppx_let simply adds two new binders: `let%%bind` and `let%%map`.  These are
rewritten into calls to the bind and map functions respectively.  These
functions are expected to have
```
  val map  : 'a t -> f:('a -> 'b)   -> 'b t
  val bind : 'a t -> f:('a -> 'b t) -> 'b t
```
for some type `t`, as one might expect.

These functions are to be provided by the user, and are generally expected to
be part of the signatures of monads and applicatives modules.  This is the
case for all monads and applicatives defined by the Jane Street's Core suite
of libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppx-here-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ppx_let-%{version}

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
