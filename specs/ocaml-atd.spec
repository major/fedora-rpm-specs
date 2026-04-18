# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-atd
Version:        4.1.0
Release:        %autorelease
Summary:        Adaptable Type Definitions for cross-language data types

License:        BSD-3-Clause
URL:            https://github.com/ahrefs/atd
VCS:            git:%{url}.git
Source:         %{url}/releases/download/%{version}/atd-%{version}.tbz

BuildRequires:  gcc-c++
BuildRequires:  ocaml >= 4.14
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-biniou-devel >= 1.0.6
BuildRequires:  ocaml-cmdliner-devel >= 1.1.0
BuildRequires:  ocaml-dune >= 3.18
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-menhir >= 20180523
BuildRequires:  ocaml-re-devel >= 1.9.0
BuildRequires:  ocaml-testo-devel >= 0.3.0
BuildRequires:  ocaml-yamlx-devel >= 0.1.0
BuildRequires:  ocaml-yojson-devel >= 3.0.0
BuildRequires:  pkgconfig(RapidJSON)
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

* atdgen: executable that generates OCaml code dealing with json and biniou
  data formats
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
Atdgen is a command-line program that takes as input type definitions in the
ATD syntax and produces OCaml code suitable for data serialization and
deserialization.  Two data formats are currently supported, these are biniou
and JSON.  Atdgen-biniou and Atdgen-json will refer to Atdgen used in one
context or the other.  Atdgen was designed with efficiency and durability in
mind.  Software authors are encouraged to use Atdgen directly and to write
tools that may reuse part of Atdgen’s source code.


%package -n     ocaml-atdcpp
Summary:        C++ code generation for ATD
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-atdcpp
Atdcpp takes type definitions in the ATD format and derives C++ classes that
can read and write JSON data.  This saves the developer the labor writing
boilerplate that converts between dicts and classes.

This allows safe interoperability with other languages supported by ATD such
as D, OCaml, Java, Python or Scala.


%package -n     ocaml-atdd
Summary:        DLang code generation for ATD
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-atdd
Atdd takes type definitions in the ATD format and derives `dlang` classes that
can read and write JSON data.  This saves the developer the labor writing
boilerplate that converts between dicts and classes.

This allows safe interoperability with other languages supported by ATD such
as C++, OCaml, Java, Python or Scala.


%package -n     ocaml-atdj
Summary:        Java code generation for ATD
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-atdj
Atdj is a program that generates a Java interface from type definitions.  In
particular, given a set of ATD type definitions, this tool generates a set of
Java classes representing those types with built-in JSON serializers and
deserializers.

The primary benefits of using the generated interface, over manually
manipulating JSON strings from within Java, are safety and ease of use.
Specifically, the generated interface offers the following features:

- JSON strings are automatically checked for correctness with respect to the
  ATD specification.

- Details such as optional fields and their associated default values are
  automatically handled.


%package -n     ocaml-atdml
Summary:        Generates efficient JSON serializers, deserializers and validators
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-atdml
Atdml generates OCaml .ml and .mli files from ATD type definitions.  Unlike
atdgen, it uses the standard `Yojson.Safe.t` intermediate representation
instead of semi-secret streaming parser functions, making the generated code
simpler and more maintainable at the cost of some performance.


%package -n     ocaml-atdpy
Summary:        Python/mypy code generation for ATD
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-atdpy
Atdpy is a program that generates a Python interface from type definitions.
In particular, given a set of ATD type definitions, this tool generates a set
of Python classes representing those types with built-in JSON serializers and
deserializers.

The primary benefits of using the generated interface, over manually
manipulating JSON strings from within Python, are safety and ease of use.
Specifically, the generated interface offers the following features:

- JSON strings are automatically checked for correctness with respect to the
  ATD specification.

- Details such as optional fields and their associated default values are
  automatically handled.


%package -n     ocaml-atds
Summary:        ATD Code generator for Scala
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-atds
Atds is a program that generates a Scala interface from type definitions.  In
particular, given a set of ATD type definitions, this tool generates a set of
Scala classes representing those types with built-in JSON serializers and
deserializers.

The primary benefits of using the generated interface, over manually
manipulating JSON strings from within Scala, are safety and ease of use.
Specifically, the generated interface offers the following features:

- JSON strings are automatically checked for correctness with respect to the
  ATD specification.

- Details such as optional fields and their associated default values are
  automatically handled.


%package -n     ocaml-atdts
Summary:        TypeScript code generation for ATD
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ocaml-atdts
Atdts takes type definitions in the ATD format and derives TypeScript classes
that can read and write JSON data.  This saves the developer the labor writing
boilerplate that converts between dicts and classes.

This allows safe interoperability with other languages supported by ATD such
as C++, OCaml, Java, Scala, or Python.


%package -n     ocaml-atdgen-codec-runtime
Summary:        Runtime for atdgen generated Melange converters
# Requires:

%description -n ocaml-atdgen-codec-runtime
This library contains the types that are used by atdgen's Melange backend.


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
This package should be used only in conjunction with the atdgen code
generator.


%package -n     ocaml-atdgen-runtime-devel
Summary:        Development files for ocaml-atdgen-runtime
Requires:       ocaml-atdgen-runtime%{?_isa} = %{version}-%{release}
Requires:       ocaml-biniou-devel%{?_isa}
Requires:       ocaml-yojson-devel%{?_isa}

# This can be removed when F45 reaches EOL
Obsoletes:      ocaml-atdgen-devel < 2.16.0
Provides:       ocaml-atdgen-devel = %{version}-%{release}

%description -n ocaml-atdgen-runtime-devel
The ocaml-atdgen-runtime-devel package contains libraries and signature files
for developing applications that use ocaml-atdgen-runtime.


%package        jsonlike
Summary:        Generic JSON-like AST for use with ATD code generators

%description    jsonlike
This library provides a generic tree type for representing JSON-like data
(JSON, YAML, TOML, etc.) for use as a target type in code generated by ATD
tools such as atdml.


%package        jsonlike-devel
Summary:        Development files for ocaml-atd-jsonlike
Requires:       ocaml-atd-jsonlike%{?_isa} = %{version}-%{release}
Requires:       ocaml-re-devel%{?_isa}

%description    jsonlike-devel
The ocaml-atd-jsonlike-devel package contains libraries and signature files
for developing applications that use ocaml-atd-jsonlike.


%package        yamlx
Summary:        YAML-to-jsonlike bridge for use with ATD code generators
Requires:       ocaml-atd-jsonlike%{?_isa} = %{version}-%{release}

%description    yamlx
This library translates a parsed YAML value (`YAMLx.value` from the yamlx
library) into the generic `Atd_jsonlike.AST.t` tree type, preserving source
locations at every node so that ATD-generated reader functions can report
precise file/line/column error messages.


%package        yamlx-devel
Summary:        Development files for ocaml-atd-yamlx
Requires:       ocaml-atd-yamlx%{?_isa} = %{version}-%{release}
Requires:       ocaml-atd-jsonlike-devel%{?_isa} = %{version}-%{release}
Requires:       ocaml-yamlx-devel%{?_isa}

%description    yamlx-devel
The ocaml-atd-yamlx-devel package contains libraries and signature files for
developing applications that use ocaml-atd-yamlx.


%prep
%autosetup -p1 -n atd-%{version}


%build
%dune_build


%install
%dune_install -s

# atdcpp, atdd, atdgen, atdj, atdml, atdpy, atds & atdts do not ship libraries
# dune has a known issue where it generates empty META files
#
# we actually don't need to ship devel files at all so remove
# the directories entirely
#
# https://github.com/ocaml/dune/issues/2353
rm -rf %{buildroot}%{_libdir}/ocaml/atd{cpp,d,gen,j,ml,py,s,ts}


%check
# Do not run the scala tests to avoid a dependency on scala
%ifarch %{java_arches}
%dune_check -p atd{,cpp,d,gen,gen-runtime,gen-codec-runtime,j,ml,py,ts}
%else
%dune_check -p atd{,cpp,d,gen,gen-runtime,gen-codec-runtime,ml,py,ts}
%endif


%files -f .ofiles-atd
%license LICENSE.md
%doc CHANGES.md README.md


%files devel -f .ofiles-atd-devel
%doc CODEOWNERS


%files -n ocaml-atdgen
%{_bindir}/atdgen
%{_bindir}/atdgen-cppo
%{_bindir}/cppo-json


%files -n ocaml-atdcpp
%{_bindir}/atdcpp


%files -n ocaml-atdd
%{_bindir}/atdd


%files -n ocaml-atdj
%{_bindir}/atdj


%files -n ocaml-atdml
%{_bindir}/atdml


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


%files jsonlike -f .ofiles-atd-jsonlike


%files jsonlike-devel -f .ofiles-atd-jsonlike-devel


%files yamlx -f .ofiles-atd-yamlx


%files yamlx-devel -f .ofiles-atd-yamlx-devel


%changelog
%autochangelog
