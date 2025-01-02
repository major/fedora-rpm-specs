%bcond_with bootstrap

Name:           maven-common-artifact-filters
Version:        3.4.0
Release:        %autorelease
Summary:        Maven Common Artifact Filters
License:        Apache-2.0
URL:            https://maven.apache.org/shared/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-util)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
%endif

%description
A collection of ready-made filters to control inclusion/exclusion of artifacts
during dependency resolution.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup -p1 -C

# Test depends on jmh performance benchmarking library
%pom_remove_dep org.openjdk.jmh:jmh-core
%pom_remove_dep org.openjdk.jmh:jmh-generator-annprocess

rm src/test/java/org/apache/maven/shared/artifact/filter/PatternFilterPerfTest.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
%autochangelog
