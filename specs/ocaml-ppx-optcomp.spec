# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# This package is required by ocaml-time-now, which is required by
# ocaml-ppx-inline-test.  This package requires ocaml-ppx-inline-test to run
# its tests.  We break the circular dependency here.
%bcond test 0

Name:           ocaml-ppx-optcomp
Version:        0.17.1
Release:        %autorelease
Summary:        Optional compilation for OCaml

License:        MIT
URL:            https://github.com/janestreet/ppx_optcomp
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_optcomp-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppxlib-devel >= 0.36.0
BuildRequires:  ocaml-stdio-devel >= 0.17

%if %{with test}
BuildRequires:  ocaml-ppx-inline-test-devel
%endif

%description
Ppx_optcomp provides optional compilation for OCaml.  It is a tool used to
handle optional compilations of pieces of code depending of the word size, the
version of the compiler, etc.  The syntax is based on OCaml item extension
nodes, with keywords similar to cpp.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-stdio-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ppx_optcomp-%{version}

%build
%dune_build

%install
%dune_install

%if %{with test}
%check
%dune_check
%endif

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
