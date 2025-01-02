%bcond_with bootstrap

Name:           maven-shared-io
Epoch:          1
Version:        3.0.0
Release:        %autorelease
Summary:        API for I/O support like logging, download or file scanning
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-shared-io
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Rejected upstream: https://issues.apache.org/jira/browse/MSHARED-490
Patch:          0001-Fix-running-tests-with-Maven-3.3.9.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.easymock:easymock)
%endif

%description
API for I/O support like logging, download or file scanning.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup -p1 -C

%build
%mvn_build -- -Dmaven.compiler.target=8

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
%autochangelog
