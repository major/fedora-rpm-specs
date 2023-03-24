%undefine _package_note_flags

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-opam-file-format
Version:        2.1.6
Release:        %autorelease
Summary:        Parser and printer for the opam file syntax

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://github.com/ocaml/opam-file-format/
Source0:        https://github.com/ocaml/%{libname}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# for tests
BuildRequires:  ocaml-alcotest-devel

%description
Parser and printer for the opam file syntax.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n %{libname}-%{version} -p1

%build
%{dune_build}

%check
%{dune_check}

%install
%{dune_install}

%files -f .ofiles
%doc README.md CHANGES
%license LICENSE

%files devel -f .ofiles-devel
%license LICENSE

%changelog
%autochangelog
