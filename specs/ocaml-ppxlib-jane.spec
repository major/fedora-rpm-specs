%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-ppxlib-jane
Version:        0.17.2
Release:        %autorelease
Summary:        Utilities for working with Jane Street AST constructs

License:        MIT
URL:            https://github.com/janestreet/ppxlib_jane
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppxlib_jane-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 5.3.0
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0

%description
A library for use in ppxes for constructing and matching on ASTs
corresponding to the augmented parsetree that is recognized by the Jane
Street OCaml compiler (flambda).

ASTs constructed using this library are compatible with the standard
OCaml compiler.  Any syntax change known to this library is encoded as
attributes, and the standard OCaml compiler's interpretation of the ASTs
constructed by these library (which amounts to ignoring the attributes)
is reasonable.  That is, we only expose "unsurprising" things in this
library.  For example, if you construct an *n*-ary function using this
library, the standard OCaml compiler will interpret it as *n* nested
unary functions in the normal way.

Likewise, ppxes that use this library to match on Jane Street ASTs can
also be used with the standard OCaml compiler.  (The Jane Street AST
cases of the match will just never be triggered when using the standard
OCaml compiler.)

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ppxlib_jane-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
