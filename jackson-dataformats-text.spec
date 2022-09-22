Name:          jackson-dataformats-text
Version:       2.9.8
Release:       11%{?dist}
Summary:       Jackson standard text-format data format backends
License:       ASL 2.0
URL:           https://github.com/FasterXML/jackson-dataformats-text
Source0:       https://github.com/FasterXML/jackson-dataformats-text/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= %{version}
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.yaml:snakeyaml)

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
Parent pom for Jackson text-format dataformats.

%package -n jackson-dataformat-csv
Summary: Support for reading and writing CSV-encoded data via Jackson abstractions

%description -n jackson-dataformat-csv
Jackson data format module for reading and writing CSV encoded data, either
as "raw" data (sequence of String arrays), or via data binding to/from Java
Objects (POJOs).

%package -n jackson-dataformat-properties
Summary: Support for reading and writing content of "Java Properties" files

%description -n jackson-dataformat-properties
Jackson data format module that supports reading and writing Java Properties
files, using naming convention to determine implied structure (by default
assuming dotted notation, but configurable from non-nested to other
separators).

%package -n jackson-dataformat-yaml
Summary: Support for reading and writing YAML-encoded data via Jackson abstractions

%description -n jackson-dataformat-yaml
Jackson extension component for reading and writing YAML encoded data.
SnakeYAML library is used for low-level YAML parsing. This project adds
necessary abstractions on top to make things work with other Jackson
functionality.

%package javadoc
Summary: Javadoc for %{name}
# Obsoletes standalone jackson-dataformat-* packages since F28
Obsoletes: jackson-dataformat-csv-javadoc < %{version}-%{release}
Provides:  jackson-dataformat-csv-javadoc = %{version}-%{release}
Obsoletes: jackson-dataformat-properties-javadoc < %{version}-%{release}
Provides:  jackson-dataformat-properties-javadoc = %{version}-%{release}
Obsoletes: jackson-dataformat-yaml-javadoc < %{version}-%{release}
Provides:  jackson-dataformat-yaml-javadoc = %{version}-%{release}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p yaml/src/main/resources/META-INF/{NOTICE,LICENSE} .
sed -i 's/\r//' LICENSE NOTICE

%mvn_file ":{*}" jackson-dataformats/@1

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-jackson-dataformats-text
%doc README.md release-notes/*
%license LICENSE NOTICE

%files -n jackson-dataformat-csv -f .mfiles-jackson-dataformat-csv
%doc csv/README.md csv/release-notes/*
%license LICENSE NOTICE

%files -n jackson-dataformat-properties -f .mfiles-jackson-dataformat-properties
%doc properties/README.md properties/release-notes/*
%license LICENSE NOTICE

%files -n jackson-dataformat-yaml -f .mfiles-jackson-dataformat-yaml
%doc yaml/README.md yaml/release-notes/*
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
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
- Fix rpmlint nits from package review

* Wed Jan 24 2018 Mat Booth <mat.booth@redhat.com> - 2.9.4-1
- Update to latest upstream release

* Wed Jan 24 2018 Mat Booth <mat.booth@redhat.com> - 2.9.3-1
- Initial packaging

