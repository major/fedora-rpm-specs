Name:           ocaml-integers
Version:        0.8.0
Release:        %autorelease
Summary:        Various signed and unsigned integer types for OCaml

License:        MIT
URL:            https://github.com/yallop/ocaml-integers
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Fedora does not need stdlib-shims, which is for older OCaml systems
Patch:          %{name}-stdlib-shims.patch

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildSystem:    dune
BuildRequires:  ocaml >= 4.03
BuildRequires:  ocaml-dune >= 1.0

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Data_types -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings

%description
The ocaml-integers library provides a number of 8-, 16-, 32- and 64-bit signed
and unsigned integer types, together with aliases such as `long` and `size_t`
whose sizes depend on the host platform.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -p1

%files -f .ofiles
%license LICENSE.md
%doc CHANGES.md README.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
