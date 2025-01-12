# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-atd
Version:        2.15.0
Release:        12%{?dist}
Summary:        Adaptable Type Definitions for cross-language data types

License:        BSD-3-Clause
URL:            https://github.com/ahrefs/atd
VCS:            git:%{url}.git
Source:         %{url}/releases/download/%{version}/atd-%{version}.tbz

BuildRequires:  ocaml >= 4.08
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-biniou-devel >= 1.0.6
BuildRequires:  ocaml-cmdliner-devel >= 1.1.0
BuildRequires:  ocaml-dune >= 2.8
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-menhir >= 20180523
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-yojson-devel >= 2.0.2
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist flake8}
BuildRequires:  %{py3_dist jsonschema}
BuildRequires:  %{py3_dist mypy}
BuildRequires:  %{py3_dist pytest}

%ifarch %{java_arches}
BuildRequires:  java-latest-openjdk-devel
%endif

%description
ATD stands for Adaptable Type Definitions. It is a syntax for defining
cross-language data types. It is used as input to generate efficient and
type-safe serializers, deserializers and validators. The current target
languages are OCaml and Java.

The following opam packages are provided by the atd project:

* atdgen: executable that generates OCaml code dealing with json and
  biniou data formats
* atdj: executable that generates Java code dealing with json
* atd: library for parsing atd files used by code generators


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-easy-format-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-yojson-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%package -n     ocaml-atdgen
Summary:        Generates efficient JSON serializers, deserializers and validators
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-atdgen-runtime%{?_isa} = %{version}-%{release}

%description -n ocaml-atdgen
Atdgen is a command-line program that takes as input type definitions in the ATD
syntax and produces OCaml code suitable for data serialization and
deserialization. Two data formats are currently supported, these are biniou and
JSON. Atdgen-biniou and Atdgen-json will refer to Atdgen used in one context or
the other. Atdgen was designed with efficiency and durability in mind. Software
authors are encouraged to use Atdgen directly and to write tools that may reuse
part of Atdgen’s source code.

%package -n     ocaml-atdgen-devel
Summary:        Development files for ocaml-atdgen
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-atdgen%{?_isa} = %{version}-%{release}
Requires:       ocaml-atdgen-runtime-devel%{?_isa} = %{version}-%{release}

%description -n ocaml-atdgen-devel
The ocaml-atdgen-devel package contains libraries and signature files for
developing applications that use ocaml-atdgen.


%package -n     ocaml-atdd
Summary:        DLang code generation for ATD
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-atdd
Atdd takes type definitions in the ATD format and derives `dlang`
classes that can read and write JSON data.  This saves the developer the
labor writing boilerplate that converts between dicts and classes.

This allows safe interoperability with other languages supported by ATD
such as OCaml, Java, Python or Scala.


%package -n     ocaml-atdj
Summary:        Java code generation for ATD
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-atdj
Atdj is a program that generates a Java interface from type definitions. In
particular, given a set of ATD type definitions, this tool generates a set of
Java classes representing those types with built-in JSON serializers and
deserializers.

The primary benefits of using the generated interface, over manually
manipulating JSON strings from within Java, are safety and ease of use.
Specifically, the generated interface offers the following features:

- JSON strings are automatically checked for correctness with respect to the ATD
  specification.

- Details such as optional fields and their associated default values are
  automatically handled.


%package -n     ocaml-atdpy
Summary:        Python/mypy code generation for ATD
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-atdpy
Atdpy is a program that generates a Python interface from type definitions. In
particular, given a set of ATD type definitions, this tool generates a set of
Python classes representing those types with built-in JSON serializers and
deserializers.

The primary benefits of using the generated interface, over manually
manipulating JSON strings from within Python, are safety and ease of use.
Specifically, the generated interface offers the following features:

- JSON strings are automatically checked for correctness with respect to the ATD
  specification.

- Details such as optional fields and their associated default values are
  automatically handled.


%package -n     ocaml-atds
Summary:        ATD Code generator for Scala
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-atds
Atds is a program that generates a Scala interface from type definitions. In
particular, given a set of ATD type definitions, this tool generates a set of
Scala classes representing those types with built-in JSON serializers and
deserializers.

The primary benefits of using the generated interface, over manually
manipulating JSON strings from within Scala, are safety and ease of use.
Specifically, the generated interface offers the following features:

- JSON strings are automatically checked for correctness with respect to the ATD
  specification.

- Details such as optional fields and their associated default values are
  automatically handled.


%package -n     ocaml-atdts
Summary:        TypeScript code generation for ATD
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-atdts
Atdts takes type definitions in the ATD format and derives TypeScript
classes that can read and write JSON data.  This saves the developer the
labor writing boilerplate that converts between dicts and classes.

This allows safe interoperability with other languages supported by
ATD such as OCaml, Java, Scala, or Python.


%package -n     ocaml-atdgen-codec-runtime
Summary:        Runtime for atdgen generated bucklescript converters
# Requires:

%description -n ocaml-atdgen-codec-runtime
This library contains the types that are used by atdgen's bucklescript backend.


%package -n     ocaml-atdgen-codec-runtime-devel
Summary:        Development files for ocaml-atdgen-codec-runtime
Requires:       ocaml-atdgen-codec-runtime%{?_isa} = %{version}-%{release}

%description -n ocaml-atdgen-codec-runtime-devel
The ocaml-atdgen-codec-runtime-devel package contains libraries and signature
files for developing applications that use ocaml-atdgen-codec-runtime.


%package -n     ocaml-atdgen-runtime
Summary:        Runtime library for code generated by atdgen
# Requires:

%description -n ocaml-atdgen-runtime
This package should be used only in conjunction with the atdgen code generator.


%package -n     ocaml-atdgen-runtime-devel
Summary:        Development files for ocaml-atdgen-runtime
Requires:       ocaml-atdgen-runtime%{?_isa} = %{version}-%{release}
Requires:       ocaml-biniou-devel%{?_isa}
Requires:       ocaml-yojson-devel%{?_isa}

%description -n ocaml-atdgen-runtime-devel
The ocaml-atdgen-runtime-devel package contains libraries and signature files
for developing applications that use ocaml-atdgen-runtime.


%prep
%autosetup -p1 -n atd-%{version}


%build
%dune_build


%install
%dune_install -s

# atdd, atdj, atdpy, atds, and atdts do not ship libraries
# dune has a known issue where it generates empty META files
#
# we actually don't need to ship devel files at all so remove
# the directories entirely
#
# https://github.com/ocaml/dune/issues/2353
rm -rf %{buildroot}%{_libdir}/ocaml/atd{d,j,py,s,ts}


%check
# Do not run the scala tests to avoid a dependency on scala
%ifarch %{java_arches}
%dune_check -p atd{,d,gen,gen-runtime,gen-codec-runtime,j,py,ts}
%else
%dune_check -p atd{,d,gen,gen-runtime,gen-codec-runtime,py,ts}
%endif


%files -f .ofiles-atd
%license LICENSE.md
%doc CHANGES.md README.md


%files devel -f .ofiles-atd-devel
%doc CODEOWNERS


%files -n ocaml-atdgen -f .ofiles-atdgen


%files -n ocaml-atdgen-devel -f .ofiles-atdgen-devel


%files -n ocaml-atdd
%{_bindir}/atdd


%files -n ocaml-atdj
%{_bindir}/atdj


%files -n ocaml-atdpy
%{_bindir}/atdpy


%files -n ocaml-atds
%{_bindir}/atds


%files -n ocaml-atdts
%{_bindir}/atdts


%files -n ocaml-atdgen-codec-runtime -f .ofiles-atdgen-codec-runtime


%files -n ocaml-atdgen-codec-runtime-devel -f .ofiles-atdgen-codec-runtime-devel


%files -n ocaml-atdgen-runtime -f .ofiles-atdgen-runtime


%files -n ocaml-atdgen-runtime-devel -f .ofiles-atdgen-runtime-devel


%changelog
* Fri Jan 10 2025 Jerry James <loganjerry@gmail.com> - 2.15.0-12
- OCaml 5.3.0 rebuild for Fedora 42

* Sun Oct  6 2024 Jerry James <loganjerry@gmail.com> - 2.15.0-11
- Rebuild for ocaml-re 1.13.3

* Mon Aug  5 2024 Jerry James <loganjerry@gmail.com> - 2.15.0-10
- Rebuild for ocaml-menhir 20240715 and ocaml-yojson 2.2.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 2.15.0-8
- OCaml 5.2.0 ppc64le fix

* Wed Jun 05 2024 Richard W.M. Jones <rjones@redhat.com> - 2.15.0-7
- Use latest JDK instead of ancient version 11

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 2.15.0-6
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 2.15.0-3
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 2.15.0-2
- OCaml 5.1.1 rebuild for Fedora 40

* Mon Oct 30 2023 Jerry James <loganjerry@gmail.com> - 2.15.0-1
- Version 2.15.0

* Wed Oct 25 2023 Jerry James <loganjerry@gmail.com> - 2.14.1-1
- Version 2.14.1

* Fri Oct 20 2023 Jerry James <loganjerry@gmail.com> - 2.14.0-1
- Version 2.14.0

* Wed Oct 18 2023 Jerry James <loganjerry@gmail.com> - 2.13.0-1
- Version 2.13.0
- Add support for the D language

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 2.12.0-4
- OCaml 5.1 rebuild for Fedora 40

* Wed Oct  4 2023 Jerry James <loganjerry@gmail.com> - 2.12.0-3
- Reenable flake8 tests

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 2.12.0-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 2.12.0-1
- Version 2.12.0
- New atdpy and atdts subpackages
- Drop test dependency on scala
- Drop doc dependency on odoc

* Wed Feb 15 2023 Jerry James <loganjerry@gmail.com> - 2.2.1-11
- Convert License tag to SPDX

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 2.2.1-11
- Bump release and rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 2.2.1-10
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul  7 2022 Jerry James <loganjerry@gmail.com> - 2.2.1-7
- Rebuild to fix FTI (rhbz#2098760)
- Use new OCaml macros

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.2.1-6
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 2.2.1-4
- Rebuild for ocaml-menhir 20211223
- Enable testing with scala 2.13
- Minor spec file cleanups

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 30 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.2.1-3
- Temporarily disable tests on i686

* Fri Apr 23 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.2.1-2
- Create subpackages per OPAM module
- Optionally compile and test `atds`
- Skip shipping empty META files; known Dune issue
  https://github.com/ocaml/dune/issues/2353

* Wed Apr 07 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.2.1-1
- Initial package
