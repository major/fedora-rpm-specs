%undefine _package_note_flags

%global project_name atd
%global forgeurl https://github.com/ahrefs/%{project_name}

# The comment in atdgen/test/test_atdgen_main.ml lines 128-173 warns of a
# potential segfault if the compiler is too clever.  That is in fact happening,
# currently on i386 only.  Until upstream figures out how to address the issue,
# we disable tests on i386.  Note that Java tests can no longer run on i386
# anyway due to https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs.
%ifarch %{ix86}
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           ocaml-%{project_name}
Version:        2.2.1
Release:        8%{?dist}
Summary:        Static Types for Json APIs

License:        BSD
URL:            %{forgeurl}
Source0:        %{url}/archive/%{version}/%{project_name}-%{version}.tar.gz
# Testing requires an argonaut jar.  Upstream provides jars for scala 2.11 and
# 2.12, but Fedora is on 2.13, so we fetch our own jar.  Version 6.2.2 is no
# longer available, so we take the last of the 6.2.x series.
Source1:        https://repo1.maven.org/maven2/io/argonaut/argonaut_2.13/6.2.5/argonaut_2.13-6.2.5.jar
# Adapt to scala 2.13
Patch0:         %{name}-scala2.13.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-menhir
BuildRequires:  ocaml-biniou-devel
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-odoc
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-yojson-devel
%if %{with tests}
BuildRequires:  java-11-openjdk-devel
BuildRequires:  scala
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
%autosetup -p1 -n %{project_name}-%{version}
cp -p %{SOURCE1} atds/test/argonaut_2.13-6.2.2.jar

# Update the menhir version to gain type inference
sed -i 's/using menhir 1\.0/using menhir 2.0/' dune-project


%build
%dune_build
%dune_build @doc


%install
%dune_install -s

# atdj and atds do not ship libraries
# dune has a known issue where it generates empty META files
#
# we actually don't need to ship devel files at all so remove
# the directories entirely
#
# https://github.com/ocaml/dune/issues/2353
rm -rf %{buildroot}%{_libdir}/ocaml/atd{j,s}


%if %{with tests}
%check
%dune_check
%endif


%files -f .ofiles-atd
%license LICENSE.md
%doc CHANGES.md README.md


%files devel -f .ofiles-atd-devel
%doc CODEOWNERS _build/default/_doc/*


%files -n ocaml-atdgen -f .ofiles-atdgen


%files -n ocaml-atdgen-devel -f .ofiles-atdgen-devel


%files -n ocaml-atdj
%{_bindir}/atdj


%files -n ocaml-atds
%{_bindir}/atds


%files -n ocaml-atdgen-codec-runtime -f .ofiles-atdgen-codec-runtime


%files -n ocaml-atdgen-codec-runtime-devel -f .ofiles-atdgen-codec-runtime-devel


%files -n ocaml-atdgen-runtime -f .ofiles-atdgen-runtime


%files -n ocaml-atdgen-runtime-devel -f .ofiles-atdgen-runtime-devel


%changelog
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
