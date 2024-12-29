# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-mtime
Version:        2.1.0
Release:        %autorelease
Summary:        Monotonic wall-clock time for OCaml

License:        ISC
URL:            https://erratique.ch/software/mtime
VCS:            git:https://erratique.ch/repos/mtime.git
Source:         %{url}/releases/mtime-%{version}.tbz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel >= 1.0.3

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Oprint -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Unit_info -i Warnings

%description
Mtime has platform independent support for monotonic wall-clock time in
pure OCaml.  This time increases monotonically and is not subject to
operating system calendar time adjustments.  The library has types to
represent nanosecond precision timestamps and time spans.

The additional Mtime_clock library provide access to a system
monotonic clock.

Mtime has no dependencies.  Mtime_clock depends on your system library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n mtime-%{version}

# link with the math library
echo $'\ntrue: cclib(-lm)' >> _tags

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
%if %{with docs}
%doc _build/default/_doc/*
%endif

%changelog
%autochangelog
