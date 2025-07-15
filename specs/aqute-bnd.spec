%bcond_with bootstrap

%if %{without bootstrap} && %{undefined rhel}
%bcond_without bnd_maven_plugin
%else
%bcond_with bnd_maven_plugin
%endif

Name:           aqute-bnd
Version:        6.3.1
Release:        %autorelease
Summary:        BND Tool
# Part of jpm is under BSD, but jpm is not included in binary RPM
License:        Apache-2.0 OR EPL-2.0
URL:            https://bnd.bndtools.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{name}-%{version}.tar.gz
# removes bundled jars from upstream tarball
# run as:
# ./generate-tarball.sh
Source1:        generate-tarball.sh

# Auxiliary parent pom, packager-written
Source2:        aggregator.pom
Source3:        https://repo1.maven.org/maven2/biz/aQute/bnd/aQute.libg/%{version}/aQute.libg-%{version}.pom
Source4:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd/%{version}/biz.aQute.bnd-%{version}.pom
Source5:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bndlib/%{version}/biz.aQute.bndlib-%{version}.pom
Source6:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd.annotation/%{version}/biz.aQute.bnd.annotation-%{version}.pom
Source7:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd.ant/%{version}/biz.aQute.bnd.ant-%{version}.pom
Source8:        https://repo1.maven.org/maven2/biz/aQute/bnd/biz.aQute.bnd.util/%{version}/biz.aQute.bnd.util-%{version}.pom

Patch:          0001-Disable-removed-commands.patch
Patch:          0002-Port-to-OSGI-7.0.0.patch
Patch:          0003-Remove-unmet-dependencies.patch
Patch:          0004-Port-to-OpenJDK-21.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.junit:junit-bom:pom:)
BuildRequires:  mvn(org.osgi:osgi.annotation)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
%endif
%if %{with bnd_maven_plugin}
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-mapping)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
%endif

# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 6.3.1-23

%description
The bnd tool helps you create and diagnose OSGi bundles.
The key functions are:
- Show the manifest and JAR contents of a bundle
- Wrap a JAR so that it becomes a bundle
- Create a Bundle from a specification and a class path
- Verify the validity of the manifest entries
The tool is capable of acting as:
- Command line tool
- File format
- Directives
- Use of macros

%package -n aqute-bndlib
Summary:        BND library

%description -n aqute-bndlib
%{summary}.

%if %{with bnd_maven_plugin}
%package -n bnd-maven-plugin
Summary:        BND Maven plugin

%description -n bnd-maven-plugin
%{summary}.
%endif

%prep
%autosetup -p1 -C

# the commands pull in more dependencies than we want (felix-resolver, jetty)
rm biz.aQute.bnd/src/aQute/bnd/main/{ExportReportCommand,MbrCommand,RemoteCommand,ReporterLogger,ResolveCommand,Shell}.java

cp %SOURCE2 pom.xml
sed -i 's|${Bundle-Version}|%{version}|' biz.aQute.bndlib/src/aQute/bnd/osgi/bnd.info

%if %{without bnd_maven_plugin}
%pom_disable_module maven
%endif

# libg
pushd aQute.libg
cp -p %{SOURCE3} pom.xml
%pom_add_parent org.fedoraproject.xmvn.aqute-bnd:aggregator:any
%pom_add_dep org.osgi:osgi.cmpn
popd

# bnd.annotation
pushd biz.aQute.bnd.annotation
cp -p %{SOURCE6} pom.xml
%pom_add_parent org.fedoraproject.xmvn.aqute-bnd:aggregator:any
%pom_add_dep org.osgi:osgi.core
%pom_add_dep org.osgi:osgi.cmpn
popd

# bndlib
pushd biz.aQute.bndlib
cp -p %{SOURCE5} pom.xml
%pom_add_parent org.fedoraproject.xmvn.aqute-bnd:aggregator:any
%pom_add_dep org.osgi:osgi.cmpn
%pom_add_dep biz.aQute.bnd:aQute.libg:%{version}
%pom_add_dep biz.aQute.bnd:biz.aQute.bnd.annotation:%{version}
popd

# bnd.ant
pushd biz.aQute.bnd.ant
cp -p %{SOURCE7} pom.xml
%pom_add_parent org.fedoraproject.xmvn.aqute-bnd:aggregator:any
popd

# bnd
cp -r biz.aQute.bnd.exporters/src/aQute/bnd/exporter biz.aQute.bnd/src/aQute/bnd/
pushd biz.aQute.bnd
cp -p %{SOURCE4} pom.xml
%pom_add_parent org.fedoraproject.xmvn.aqute-bnd:aggregator:any
%pom_remove_dep :biz.aQute.resolve
%pom_remove_dep :biz.aQute.repository
%pom_remove_dep :biz.aQute.bnd.exporters
%pom_remove_dep :biz.aQute.bnd.reporter
%pom_remove_dep :biz.aQute.remote.api
%pom_remove_dep :snakeyaml
%pom_remove_dep :jline
%pom_remove_dep org.osgi:org.osgi.service.coordinator
%pom_remove_dep org.osgi:org.osgi.service.resolver
popd

# bnd.util
pushd biz.aQute.bnd.util
cp -p %{SOURCE8} pom.xml
%pom_add_parent org.fedoraproject.xmvn.aqute-bnd:aggregator:any
%pom_add_dep biz.aQute.bnd:aQute.libg:%{version}
popd

%pom_remove_dep -r org.osgi:org.osgi.dto
%pom_remove_dep -r org.osgi:org.osgi.framework
%pom_remove_dep -r org.osgi:org.osgi.namespace.contract
%pom_remove_dep -r org.osgi:org.osgi.namespace.extender
%pom_remove_dep -r org.osgi:org.osgi.namespace.implementation
%pom_remove_dep -r org.osgi:org.osgi.namespace.service
%pom_remove_dep -r org.osgi:org.osgi.resource
%pom_remove_dep -r org.osgi:org.osgi.service.log
%pom_remove_dep -r org.osgi:org.osgi.service.repository
%pom_remove_dep -r org.osgi:org.osgi.service.serviceloader
%pom_remove_dep -r org.osgi:org.osgi.util.function
%pom_remove_dep -r org.osgi:org.osgi.util.promise
%pom_remove_dep -r org.osgi:org.osgi.util.tracker

%pom_xpath_remove -r pom:project/pom:dependencies/pom:dependency/pom:scope

# maven-plugins
cp -r biz.aQute.bnd.maven/src/aQute/bnd/maven/lib/configuration maven/bnd-maven-plugin/src/main/java/aQute/bnd/maven/lib
cp -r biz.aQute.bnd.maven/src/aQute/bnd/maven/lib/executions maven/bnd-maven-plugin/src/main/java/aQute/bnd/maven/lib
pushd maven
%pom_remove_dep -r :biz.aQute.bnd.maven
# Unavailable reactor dependency - org.osgi.impl.bundle.repoindex.cli
%pom_disable_module bnd-indexer-maven-plugin
# Requires unbuilt parts of bnd
%pom_disable_module bnd-export-maven-plugin
%pom_disable_module bnd-reporter-maven-plugin
%pom_disable_module bnd-resolver-maven-plugin
%pom_disable_module bnd-run-maven-plugin
%pom_disable_module bnd-testing-maven-plugin
# Integration tests require Internet access
%pom_remove_plugin -r :maven-invoker-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_remove_plugin -r :flatten-maven-plugin
popd

%mvn_alias biz.aQute.bnd:biz.aQute.bnd :bnd biz.aQute:bnd
%mvn_alias biz.aQute.bnd:biz.aQute.bndlib :bndlib biz.aQute:bndlib

%mvn_package biz.aQute.bnd:biz.aQute.bndlib bndlib
%mvn_package biz.aQute.bnd:biz.aQute.bnd.annotation bndlib
%mvn_package biz.aQute.bnd:aQute.libg bndlib
%mvn_package org.fedoraproject.xmvn.aqute-bnd:aggregator __noinstall
%mvn_package biz.aQute.bnd:bnd-plugin-parent __noinstall
%if %{with bnd_maven_plugin}
%mvn_package biz.aQute.bnd:bnd-maven-plugin maven
%mvn_package biz.aQute.bnd:bnd-baseline-maven-plugin maven
%endif

%build
%mvn_build -j

%install
%mvn_install

install -d -m 755 %{buildroot}%{_sysconfdir}/ant.d
echo "aqute-bnd slf4j/api slf4j/simple osgi-annotation osgi-core osgi-compendium" >%{buildroot}%{_sysconfdir}/ant.d/%{name}

%jpackage_script aQute.bnd.main.bnd "" "" aqute-bnd:slf4j/slf4j-api:slf4j/slf4j-simple:osgi-annotation:osgi-core:osgi-compendium bnd 1

%files -f .mfiles
%license LICENSE
%{_bindir}/bnd
%config(noreplace) %{_sysconfdir}/ant.d/*

%files -n aqute-bndlib -f .mfiles-bndlib
%license LICENSE

%if %{with bnd_maven_plugin}
%files -n bnd-maven-plugin -f .mfiles-maven
%endif

%changelog
%autochangelog
