%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-logs
Version:        0.10.0
Release:        %autorelease
Summary:        Logging infrastructure for OCaml

License:        ISC
URL:            https://erratique.ch/software/logs
VCS:            git:https://erratique.ch/repos/logs.git
Source:         %{url}/releases/logs-%{version}.tbz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.14.0
BuildRequires:  ocaml-cmdliner-devel >= 1.3.0
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-fmt-devel >= 0.9.0
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-mtime-devel
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel >= 1.1.0

# Do not require ocaml-compiler-libs at runtime
%global __ocaml_requires_opts -i Asttypes -i Build_path_prefix_map -i Cmi_format -i Env -i Format_doc -i Ident -i Identifiable -i Load_path -i Location -i Longident -i Misc -i Outcometree -i Parsetree -i Path -i Primitive -i Shape -i Subst -i Toploop -i Type_immediacy -i Types -i Warnings

%description
Logs provides a logging infrastructure for OCaml.  Logging is performed
on sources whose reporting level can be set independently.  The log
message report is decoupled from logging and is handled by a reporter.

A few optional log reporters are distributed with the base library and
the API lets you easily implement your own.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-cmdliner-devel%{?_isa}
Requires:       ocaml-fmt-devel%{?_isa}
Requires:       ocaml-lwt-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n logs-%{version} -p1

%build
ocaml pkg/pkg.ml build \
  --dev-pkg false \
  --tests true \
  --with-js_of_ocaml-compiler false \
  --with-fmt true \
  --with-cmdliner true \
  --with-lwt true \
  --with-base-threads true

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
