# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-ppx-fields-conv
Version:        0.17.0
Release:        %autorelease
Summary:        Generate accessor & iteration functions for OCaml records

License:        MIT
URL:            https://github.com/janestreet/ppx_fields_conv
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppx_fields_conv-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-base-devel >= 0.17
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-fieldslib-devel >= 0.17
BuildRequires:  ocaml-ppxlib-devel >= 0.28.0
BuildRequires:  ocaml-ppx-inline-test-devel

%description
Ppx_fields_conv is a ppx rewriter that can be used to define first-class
values representing record fields, and additional routines, to get and set
record fields, iterate and fold over all fields of a record and create new
record values.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-base-devel%{?_isa}
Requires:       ocaml-fieldslib-devel%{?_isa}
Requires:       ocaml-ppxlib-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%prep
%autosetup -n ppx_fields_conv-%{version}

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
