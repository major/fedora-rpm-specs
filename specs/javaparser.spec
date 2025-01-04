%bcond_with bootstrap
%if !0%{?rhel} && %{without bootstrap}
%bcond_without bnd_maven_plugin
%else
%bcond_with bnd_maven_plugin
%endif

Name:           javaparser
Version:        3.26.3
Release:        %autorelease
Summary:        Java 1 to 13 Parser and Abstract Syntax Tree for Java
License:        LGPL-2.0-or-later OR Apache-2.0
URL:            https://javaparser.org
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/javaparser/javaparser/archive/%{name}-parent-%{version}.tar.gz

Patch:          0001-Port-to-OpenJDK-21.patch

%if %{with bnd_maven_plugin}
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
%endif
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.javacc:javacc)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
%endif

%description
This package contains a Java 1 to 13 Parser with AST generation and
visitor support. The AST records the source code structure, javadoc
and comments. It is also possible to change the AST nodes or create new
ones to modify the source code.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup -p1 -C


sed -i 's/\r//' readme.md

# Remove plugins unnecessary for RPM builds
%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin :maven-source-plugin

%if %{without bnd_maven_plugin}
%pom_remove_plugin :bnd-maven-plugin javaparser-core
mkdir -p javaparser-core/target/classes/META-INF/
touch javaparser-core/target/classes/META-INF/MANIFEST.MF
%endif

# Compatibility alias
%mvn_alias :javaparser-core com.google.code.javaparser:javaparser

# Fix javacc plugin name
sed -i \
  -e 's/ph-javacc-maven-plugin/javacc-maven-plugin/' \
  -e 's/com.helger.maven/org.codehaus.mojo/' \
  javaparser-core/pom.xml

# This plugin is not in Fedora, so use maven-resources-plugin to accomplish the same thing
%pom_remove_plugin :templating-maven-plugin javaparser-core
%pom_xpath_inject "pom:build" "
<resources>
  <resource>
    <directory>src/main/java-templates</directory>
    <filtering>true</filtering>
    <targetPath>\${basedir}/src/main/java</targetPath>
  </resource>
</resources>" javaparser-core

# Missing dep on jbehave for testing
%pom_disable_module javaparser-core-testing
%pom_disable_module javaparser-core-testing-bdd

# Don't build the symbol solver
%pom_disable_module javaparser-symbol-solver-core
#%pom_disable_module javaparser-symbol-solver-logic
#%pom_disable_module javaparser-symbol-solver-model
%pom_disable_module javaparser-symbol-solver-testing

# Only need to ship the core module
%pom_disable_module javaparser-core-generators
%pom_disable_module javaparser-core-metamodel-generator
%pom_disable_module javaparser-core-serialization

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc readme.md changelog.md
%license LICENSE LICENSE.APACHE LICENSE.GPL LICENSE.LGPL

%files javadoc -f .mfiles-javadoc
%license LICENSE LICENSE.APACHE LICENSE.GPL LICENSE.LGPL

%changelog
%autochangelog
