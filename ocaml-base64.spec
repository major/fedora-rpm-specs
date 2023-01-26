%undefine _package_note_flags
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# Not a circular dependency, but useful to be able to build
# without odoc which has loads of dependencies.
%bcond_with doc

Name:           ocaml-base64
Version:        3.5.0
Release:        %autorelease
Summary:        Base64 library for OCaml

License:        ISC
URL:            https://github.com/mirage/ocaml-base64
Source0:        https://github.com/mirage/ocaml-base64/releases/download/v%{version}/base64-v%{version}.tbz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune-devel

%if %{with doc}
BuildRequires:  ocaml-odoc
%endif


%description
Base64 is a group of similar binary-to-text encoding schemes that
represent binary data in an ASCII string format by translating it into
a radix-64 representation. It is specified in RFC 4648.


%package devel
Summary:        Development files for %{name}.
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
Development files for %{name}.


%prep
%autosetup -n base64-v%{version}


%build
# Only build the source directory since the other directories
# require packages that we don't have or need.
rm -r bench fuzz test
dune build %{?_smp_mflags}
%if %{with doc}
dune build %{?_smp_mflags} @doc
%endif


%install
dune install --destdir=%{buildroot}

# We do not want the ml files
find %{buildroot}%{_libdir}/ocaml -name \*.ml -delete

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc


%files
%doc README.md
%{_libdir}/ocaml/base64
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/base64/*.a
%exclude %{_libdir}/ocaml/base64/*.cmx
%exclude %{_libdir}/ocaml/base64/*.cmxa
%exclude %{_libdir}/ocaml/base64/*.cmxs
%endif
%exclude %{_libdir}/ocaml/base64/*.mli


%files devel
%doc CHANGES.md
%if %{with doc}
%doc _build/default/_doc/*
%endif
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/base64/*.a
%{_libdir}/ocaml/base64/*.cmx
%{_libdir}/ocaml/base64/*.cmxa
%{_libdir}/ocaml/base64/*.cmxs
%endif
%{_libdir}/ocaml/base64/*.mli


%changelog
%autochangelog
