# Some of the test dependencies are not available in Fedora
%bcond_with test

Name:           apache-commons-configuration
Version:        2.9.0
Release:        %autorelease
Summary:        Read configuration data from a variety of sources

License:        Apache-2.0
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
URL:            https://commons.apache.org/proper/commons-configuration/
Source0:        https://archive.apache.org/dist/commons/configuration/source/commons-configuration2-%{version}-src.tar.gz
Source1:        https://archive.apache.org/dist/commons/configuration/source/commons-configuration2-%{version}-src.tar.gz.asc
Source2:        https://downloads.apache.org/commons/KEYS

# Adapt to JEXL 3
Patch0:         %{name}-jexl3.patch

BuildRequires:  gnupg2
BuildRequires:  maven-local
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.commons:commons-text)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)

# Optional dependencies
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-jxpath:commons-jxpath)
BuildRequires:  mvn(org.apache.commons:commons-jexl3)
BuildRequires:  mvn(org.apache.commons:commons-vfs2)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-core)
BuildRequires:  mvn(org.yaml:snakeyaml)
BuildRequires:  mvn(xml-resolver:xml-resolver)

# Optional dependencies not available in Fedora
#BuildRequires:  mvn(org.springframework:spring-beans)
#BuildRequires:  mvn(org.springframework:spring-core)

# Test dependencies
%if %{with test}
BuildRequires:  mvn(com.sun.mail:mailapi)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.commons:commons-dbcp2)
BuildRequires:  mvn(org.apache.commons:commons-pool2)
BuildRequires:  mvn(org.dbunit:dbunit)
BuildRequires:  mvn(org.hamcrest:hamcrest)
BuildRequires:  mvn(org.hsqldb:hsqldb)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-ext)
BuildRequires:  mvn(org.slf4j:slf4j-log4j12)
BuildRequires:  mvn(org.slf4j:slf4j-nop)
BuildRequires:  mvn(org.springframework:spring-context)
BuildRequires:  mvn(org.springframework:spring-test)
%endif

%description
The Commons Configuration software library provides a generic
configuration interface which enables a Java application to read
configuration data from a variety of sources.  Commons Configuration
provides typed access to single, and multi-valued configuration
parameters as demonstrated by the following code:

Double double = config.getDouble("number");
Integer integer = config.getInteger("number");

Configuration parameters may be loaded from the following sources:
- Properties files
- XML documents
- Windows INI files
- Property list files (plist)
- JNDI
- JDBC Datasource
- System properties
- Applet parameters
- Servlet parameters

Configuration objects are created using configuration builders.
Different configuration sources can be mixed using a
CombinedConfigurationBuilder and a CombinedConfiguration.  Additional
sources of configuration parameters can be created by using custom
configuration objects.  This customization can be achieved by extending
AbstractConfiguration or AbstractHierarchicalConfiguration.

%javadoc_package

%prep
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -n commons-configuration2-%{version}-src -p1

# Not needed for RPM builds
%pom_xpath_remove //pom:reporting
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-scm-publish-plugin
%pom_remove_plugin :spotbugs-maven-plugin

# The Spring framework is not available in Fedora
%pom_remove_dep org.springframework:spring-core
%pom_remove_dep org.springframework:spring-beans
%pom_remove_dep org.springframework:spring-context
%pom_remove_dep org.springframework:spring-test
rm -fr src/{main,test}/java/org/apache/commons/configuration2/spring

%build
# We skip tests because we don't have test deps (dbunit in particular).
%if %{with test}
%mvn_build
%else
%mvn_build -f
%endif

%install
%mvn_install

%files -f .mfiles
%doc README.md RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt

%changelog
%autochangelog
