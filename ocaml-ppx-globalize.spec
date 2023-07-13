# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-ppx-globalize
Version:        0.16.0
Release:        %autorelease
Summary:        Generate functions to copy local values to the global heap

License:        MIT
URL:            https://github.com/janestreet/ppx_globalize
Source0:        %{url}/archive/v%{version}/ppx_globalize-%{version}.tar.gz

BuildRequires:  ocaml >= 4.14.0
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  ocaml-base-devel
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0

%description
Ppx_globalize is a ppx rewriter that generates functions to copy local
values to the global heap.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n ppx_globalize-%{version}

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
