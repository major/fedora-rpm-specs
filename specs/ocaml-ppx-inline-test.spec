# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# This package is needed to build ppx_jane, but its tests require ppx_jane.
# Break the dependency cycle here.
%bcond test 0

Name:           ocaml-ppx-inline-test
Version:        0.17.1
Release:        %autorelease
Summary:        Syntax extension for writing inline tests in OCaml code

License:        MIT
URL:            https://github.com/janestreet/ppx_inline_test
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_inline_test-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppxlib-devel >= 0.36.0
BuildRequires:  ocaml-time-now-devel >= 0.17

%if %{with test}
BuildRequires:  ocaml-ppx-jane-devel
%endif

%description
Ppx_inline_test is a syntax extension for writing inline tests in OCaml
code.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-time-now-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n ppx_inline_test-%{version}

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
