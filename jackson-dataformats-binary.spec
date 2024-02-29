# Allow conditionally building extra data format modules
# that require additional external dependencies
%bcond_with extra_dataformats
# Extra formats are disabled for now because deps in
# Fedora are not uptodate enough

Name:          jackson-dataformats-binary
Version:       2.9.8
Release:       16%{?dist}
Summary:       Jackson standard binary data format backends
# One file is BSD licensed: protobuf/src/main/resources/descriptor.proto
License:       ASL 2.0 and BSD
URL:           https://github.com/FasterXML/jackson-dataformats-binary
Source0:       https://github.com/FasterXML/jackson-dataformats-binary/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= %{version}
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%if %{with extra_dataformats}
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(com.squareup:protoparser)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.apache.avro:avro)
%endif

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
Parent pom for Jackson binary dataformats.

%if %{with extra_dataformats}
%package -n jackson-dataformat-avro
Summary: Support for reading and writing AVRO-encoded data via Jackson abstractions

%description -n jackson-dataformat-avro
Jackson extension component for reading and writing data encoded using Apache
Avro data format. Project adds necessary abstractions on top to make things
work with other Jackson functionality. It relies on standard Avro library for
Avro Schema handling, and some parts of deserialization/serialization.

%package -n jackson-dataformat-protobuf
Summary: Support for reading and writing protobuf-encoded data via Jackson abstractions

%description -n jackson-dataformat-protobuf
Jackson extension component for reading and writing Protobuf encoded data
(see protobuf encoding spec). This project adds necessary abstractions on top
to make things work with other Jackson functionality; mostly just low-level
Streaming components (JsonFactory, JsonParser, JsonGenerator).
%endif

%package -n jackson-dataformat-cbor
Summary: Support for reading and writing Concise Binary Object Representation

%description -n jackson-dataformat-cbor
Jackson data format module that supports reading and writing CBOR ("Concise
Binary Object Representation") encoded data. Module extends standard Jackson
streaming API (JsonFactory, JsonParser, JsonGenerator), and as such works
seamlessly with all the higher level data abstractions (data binding, tree
model, and pluggable extensions).

%package -n jackson-dataformat-smile
Summary: Support for reading and writing Smile encoded data using Jackson abstractions

%description -n jackson-dataformat-smile
This Jackson extension handles reading and writing of data encoded in Smile
data format ("binary JSON"). It extends standard Jackson streaming API
(JsonFactory, JsonParser, JsonGenerator), and as such works seamlessly with
all the higher level data abstractions (data binding, tree model, and
pluggable extensions).

%package javadoc
Summary: Javadoc for %{name}
# Obsoletes standalone jackson-dataformat-* packages since F28
Obsoletes: jackson-dataformat-cbor-javadoc < %{version}-%{release}
Provides:  jackson-dataformat-cbor-javadoc = %{version}-%{release}
Obsoletes: jackson-dataformat-smile-javadoc < %{version}-%{release}
Provides:  jackson-dataformat-smile-javadoc = %{version}-%{release}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p ion/LICENSE .
cp -p ion/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

%if %{without extra_dataformats}
%pom_disable_module avro
%pom_disable_module protobuf
%endif

# Test dep lombok is not in Fedora
%pom_remove_dep org.projectlombok:lombok avro

# Deps are not available in Fedora for this module
%pom_disable_module ion

%mvn_file ":{*}" jackson-dataformats/@1

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-jackson-dataformats-binary
%doc README.md release-notes/*
%license LICENSE NOTICE

%if %{with extra_dataformats}
%files -n jackson-dataformat-avro -f .mfiles-jackson-dataformat-avro
%doc avro/README.md avro/release-notes/*
%license LICENSE NOTICE

%files -n jackson-dataformat-protobuf -f .mfiles-jackson-dataformat-protobuf
%doc protobuf/README.md protobuf/release-notes/*
%license LICENSE NOTICE
%endif

%files -n jackson-dataformat-cbor -f .mfiles-jackson-dataformat-cbor
%doc cbor/README.md cbor/release-notes/*
%license LICENSE NOTICE

%files -n jackson-dataformat-smile -f .mfiles-jackson-dataformat-smile
%doc smile/README.md smile/release-notes/*
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 2.9.8-16
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.9.8-10
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.9.8-9
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.9.8-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 06 2019 Mat Booth <mat.booth@redhat.com> - 2.9.8-1
- Update to latest upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Mat Booth <mat.booth@redhat.com> - 2.9.4-2
- Correct license for package review

* Wed Jan 24 2018 Mat Booth <mat.booth@redhat.com> - 2.9.4-1
- Update to latest upstream release

* Wed Jan 24 2018 Mat Booth <mat.booth@redhat.com> - 2.9.3-1
- Initial packaging

