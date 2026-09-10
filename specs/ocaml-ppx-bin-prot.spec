# This package is needed to build ppx_jane, which is needed to run the tests
# in this package.  Break the circular dependency here.
%bcond test 0

Name:           ocaml-ppx-bin-prot
Version:        0.17.1
Release:        %autorelease
Summary:        Generate binary protocol readers and writers from types

License:        MIT
URL:            https://github.com/janestreet/ppx_bin_prot
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_bin_prot-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildSystem:    dune
BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-bin-prot-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppx-here-devel >= 0.17
BuildRequires:  ocaml-ppxlib-devel >= 0.36.0
BuildRequires:  ocaml-ppxlib-jane-devel >= 0.17

%if %{with test}
BuildRequires:  ocaml-ppx-jane-devel
%endif

%description
This package supports generating binary serialization and deserialization
functions from type definitions.  For more information, see:

- https://github.com/janestreet/bin_prot/blob/master/README.md for the
  bin-prot format
- https://github.com/janestreet/bin_prot/blob/master/shape/README.md for
  bin-prot-shape, which is useful for checking compatibility of the
  `bin_prot` representations of different types.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-ppx-here-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-ppxlib-jane-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n ppx_bin_prot-%{version}

%check
%if %{with test}
%dune_check
%endif

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
