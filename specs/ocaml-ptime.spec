Name:           ocaml-ptime
Version:        1.2.0
Release:        %autorelease
Summary:        POSIX time for OCaml

License:        ISC
URL:            https://erratique.ch/software/ptime
VCS:            git:https://erratique.ch/repos/ptime.git
Source:         %{url}/releases/ptime-%{version}.tbz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel >= 1.0.3

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings

%description
Ptime provides platform-independent POSIX time support in pure OCaml.
It provides a type to represent a well-defined range of POSIX timestamps
with picosecond precision, conversion with date-time values, conversion
with RFC 3339 timestamps (https://datatracker.ietf.org/doc/html/rfc3339)
and pretty printing to a human-readable, locale-independent
representation.

The additional Ptime_clock library provides access to a system POSIX
clock and to the system's current time zone offset.

Ptime is not a calendar library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n ptime-%{version}

# Link with the math library and include debuginfo
echo $'\ntrue: cclib(-lm), debug' >> _tags

%build
ocaml pkg/pkg.ml build --dev-pkg false --tests true

%install
%ocaml_install

%check
ocaml pkg/pkg.ml test

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
