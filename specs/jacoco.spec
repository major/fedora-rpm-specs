%global forgeurl https://github.com/jacoco/jacoco
Version:        0.8.15
%forgemeta

Name:           jacoco
Release:        %autorelease
Summary:        Java Code Coverage for Eclipse
License:        EPL-2.0
URL:            https://www.eclemma.org/jacoco/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        %{forgesource}
# Adapt to maven-doxia 2.0.0
# The deprecated org.codehaus.doxia.sink.Sink interface was removed
Patch:          %{name}-maven-doxia-2.patch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-analysis)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.ow2.asm:asm-tree)

# required by wrapper scripts
Requires:       javapackages-tools

%description
JaCoCo is a free code coverage library for Java, 
which has been created by the EclEmma team based on the lessons learned 
from using and integration existing libraries over the last five years. 

%package    maven-plugin
Summary:    A Jacoco plugin for maven
%description maven-plugin
A Jacoco plugin for maven.

%{?javadoc_package}

%prep

# -p1: strip one level dir in patch(es)
%autosetup -p1
%pom_remove_dep :asm-bom org.jacoco.build
# disable unnecessary modules
%pom_disable_module ../jacoco org.jacoco.build
%pom_disable_module ../org.jacoco.doc org.jacoco.build
%pom_disable_module ../org.jacoco.examples org.jacoco.build
%pom_disable_module ../org.jacoco.tests org.jacoco.build

# Remove unnecessary dependency on maven-javadoc-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

# Remove enforcer plugin that causes build failure of 'Jacoco :: Maven Plugin'
%pom_remove_plugin -r :maven-enforcer-plugin

# Don't build jars with classifier ":nodeps:"
%pom_remove_plugin :maven-shade-plugin \
    org.jacoco.ant \
    org.jacoco.cli

# remove unnecessary plugin
%pom_remove_plugin -r :spotless-maven-plugin

# remove beanshell plugin
# later, we need to redefine various properties defined by it
%pom_remove_plugin :beanshell-maven-plugin \
    org.jacoco.build

# buildnumber plugin was removed from f38
%pom_remove_plugin :buildnumber-maven-plugin \
    org.jacoco.build

# Remove "requires osgi(org.apache.ant)"
%pom_xpath_remove 'pom:configuration/pom:instructions/pom:Require-Bundle' \
    org.jacoco.ant

# Remove requires on maven-plugin-plugin:report
%pom_xpath_remove 'pom:execution[pom:id = "report"]' \
    jacoco-maven-plugin

# Define properties
%pom_xpath_inject 'pom:properties' '
    <unqualifiedVersion>${project.version}</unqualifiedVersion>
    <buildQualifier>${maven.build.timestamp}</buildQualifier>
    <qualified.bundle.version>${unqualifiedVersion}.${buildQualifier}</qualified.bundle.version>
    <jacoco.runtime.package.name>org.jacoco.agent.rt.internal_fedora</jacoco.runtime.package.name>' \
      org.jacoco.build

# install jacoco-maven-plugin package
%mvn_package ":jacoco-maven-plugin:{jar,pom}:{}:" maven-plugin

# install jacoco package
%mvn_package ":{org.}*:{jar,pom}:runtime:"

# don't install parent package
%mvn_package :root __noinstall
%mvn_package :org.jacoco.build __noinstall

for x in `find | grep pom.xml$` ; do
  if cat $x | grep -e "<bytecode.version>.*7" ; then
    sed "s;<bytecode.version>.*7.*;<bytecode.version>8</bytecode.version>;g" -i $x;
  fi
done


%build
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8 -Dbuild.date=$(date +%Y/%m/%d)

%install
%mvn_install

# ant config
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo %{name} %{name}/org.jacoco.ant objectweb-asm/asm > %{buildroot}%{_sysconfdir}/ant.d/%{name}

# wrapper script
%jpackage_script org.jacoco.cli.internal.Main "" "" jacoco/org.jacoco.cli:args4j:objectweb-asm:jacoco/org.jacoco.core:jacoco/org.jacoco.report jacococli true

%check
# The Jacoco test suite has missing/unpackaged dependencies (e.g. JMH, JOL, Kotlin/Groovy/Scala compilers)
# and attempts self-instrumentation and VM forking that fail in restricted mock/chroot container sandboxes.
# Therefore, tests cannot be run at build time, this is why we cannot enable the tests in Fedora for now.
:

%files -f .mfiles
%config(noreplace) %{_sysconfdir}/ant.d/%{name}
%doc README.md
%license LICENSE.md
%{_bindir}/jacococli

%files maven-plugin -f .mfiles-maven-plugin

%changelog
%autochangelog
