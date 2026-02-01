Name:           ocaml-ppx-bench
Version:        0.17.1
Release:        %autorelease
Summary:        Syntax extension for writing inline benchmarks in OCaml code

License:        MIT
URL:            https://github.com/janestreet/ppx_bench
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_bench-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppx-inline-test-devel >= 0.17
BuildRequires:  ocaml-ppxlib-devel >= 0.36.0

%description
Ppx_bench is an OCaml syntax extension for writing inline benchmarks in OCaml
code.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppx-inline-test-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ppx_bench-%{version}

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
