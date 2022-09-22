%undefine _package_note_flags
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-opam-file-format
Version:        2.1.4
Release:        %autorelease
Summary:        Parser and printer for the opam file syntax

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

# This is apparently a standard "OCaml exception" and is detailed
# in the license file.
License:        LGPLv2 with exceptions
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

%files
%doc README.md CHANGES
%license LICENSE
%{_libdir}/ocaml/%{libname}
%exclude %{_libdir}/ocaml/%{libname}/dune-package
%exclude %{_libdir}/ocaml/%{libname}/opam
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%endif
%exclude %{_libdir}/ocaml/%{libname}/*.mli

%files devel
%license LICENSE
%{_libdir}/ocaml/%{libname}/dune-package
%{_libdir}/ocaml/%{libname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%endif
%{_libdir}/ocaml/*/*.mli

%changelog
%autochangelog
