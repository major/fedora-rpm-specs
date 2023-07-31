Name:           xml-maven-plugin
Summary:        Maven XML Plugin
Version:        1.1.0
Release:        %autorelease
License:        Apache-2.0

URL:            https://www.mojohaus.org/xml-maven-plugin/
Source0:        https://github.com/mojohaus/xml-maven-plugin/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-io)
BuildRequires:  mvn(org.codehaus.plexus:plexus-resources)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(xml-resolver:xml-resolver)

%description
A plugin for various XML related tasks like validation and transformation.


%package javadoc
Summary:       Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.


%prep
%autosetup

# Add the version
sed -i 's|stylesheet |stylesheet version="1.0" |'  src/it/it8/src/main/xsl/it8.xsl

%pom_xpath_set pom:mojo.java.target 8


%build
%mvn_build -f


%install
%mvn_install


%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt


%changelog
%autochangelog
