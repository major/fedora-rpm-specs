# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-ppx-stable-witness
Version:        0.17.0
Release:        %autorelease
Summary:        Derive a witness that a type is intended to be stable

License:        MIT
URL:            https://github.com/janestreet/ppx_stable_witness
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_stable_witness-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0

%description
Ppx_stable_witnesss is a ppx extension for deriving a witness that a type is
intended to be stable.  In this context, stable means that the serialization
format will never change.  This allows programs running at different versions
of the code to communicate safely.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n ppx_stable_witness-%{version}

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
