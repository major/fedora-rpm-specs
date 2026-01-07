%bcond_with bootstrap

Name:           xbean
Version:        4.24
Release:        %autorelease
Summary:        Java plugin based web server
License:        Apache-2.0
URL:            https://geronimo.apache.org/xbean/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/%{name}/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch:          0001-Unbundle-ASM.patch
Patch:          0002-Remove-dependency-on-log4j-and-commons-logging.patch

# TODO Remove in Fedora 47
Obsoletes:      %{name}-javadoc < 4.24-9

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.osgi:org.osgi.core)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.slf4j:slf4j-api)
%endif

%description
The goal of XBean project is to create a plugin based server
analogous to Eclipse being a plugin based IDE. XBean will be able to
discover, download and install server plugins from an Internet based
repository. In addition, we include support for multiple IoC systems,
support for running with no IoC system, JMX without JMX code,
lifecycle and class loader management, and a rock solid Spring
integration.

%prep
%autosetup -p1 -C

cp xbean-asm-util/src/main/java/org/apache/xbean/asm9/original/commons/AsmConstants.java xbean-reflect/src/main/java/org/apache/xbean/recipe/

# Parent POM is not packaged
%pom_remove_parent

%pom_disable_module xbean-classloader
%pom_disable_module xbean-classpath
%pom_disable_module xbean-bundleutils
%pom_disable_module xbean-asm9-shaded
%pom_disable_module xbean-finder-shaded
%pom_disable_module xbean-naming
%pom_disable_module xbean-blueprint
%pom_disable_module xbean-spring
%pom_disable_module xbean-telnet
%pom_disable_module maven-xbean-plugin

%pom_remove_dep :commons-logging-api xbean-reflect
%pom_remove_dep :log4j xbean-reflect
%pom_remove_dep :xbean-asm9-shaded xbean-reflect
find -name CommonsLoggingConverter.java -delete
find -name Log4jConverter.java -delete

# Plugins useful for upstream only
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-source-plugin

%pom_remove_dep :xbean-bundleutils xbean-finder
rm -r xbean-finder/src/main/java/org/apache/xbean/finder{,/archive}/Bundle*

# Disable one test that fails on JVM 11
sed -i '/testGetBytecode/i@org.junit.Ignore' xbean-finder/src/test/java/org/apache/xbean/finder/archive/MJarJarArchiveTest.java

%build
%mvn_build --force -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%autochangelog
