%bcond_with bootstrap

Name:           xmvn
Version:        4.3.0
Release:        %autorelease
Summary:        Local Extensions for Apache Maven
License:        Apache-2.0
URL:            https://fedora-java.github.io/xmvn/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/fedora-java/xmvn/releases/download/%{version}/xmvn-%{version}.tar.xz
Source25:       toolchains-openjdk25.xml

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
BuildRequires:  maven
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-util)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-model-builder)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.xmlunit:xmlunit-assertj3)
# Maven home is used as template for XMvn home
BuildRequires:  maven
%endif
Requires:       %{name}-minimal = %{version}-%{release}
Requires:       maven
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 4.3.0-15

%description
This package provides extensions for Apache Maven that can be used to
manage system artifact repository and use it to resolve Maven
artifacts in offline mode, as well as Maven plugins to help with
creating RPM packages containing Maven artifacts.

%package minimal
Summary:        Dependency-reduced version of XMvn
Requires:       %{name}-core = %{version}-%{release}
Requires:       apache-commons-cli
Requires:       apache-commons-codec
Requires:       google-guice
Requires:       guava
Requires:       jakarta-annotations
Requires:       jakarta-inject1.0
Requires:       jansi
Requires:       jcl-over-slf4j
Requires:       maven-jdk-binding
Requires:       maven-lib
Requires:       maven-resolver
Requires:       maven-shared-utils
Requires:       maven-wagon
Requires:       plexus-cipher
Requires:       plexus-classworlds
Requires:       plexus-containers-component-annotations
Requires:       plexus-interpolation
Requires:       plexus-sec-dispatcher
Requires:       plexus-utils
Requires:       sisu
Requires:       slf4j
Suggests:       maven-openjdk25

%description minimal
This package provides minimal version of XMvn, incapable of using
remote repositories.

%package core
Summary:        XMvn library

%description core
This package provides XMvn API and XMvn Core modules, which implement
the essential functionality of XMvn such as resolution of artifacts
from system repository.

%package mojo
Summary:        XMvn MOJO

%description mojo
This package provides XMvn MOJO, which is a Maven plugin that consists
of several MOJOs.  Some goals of these MOJOs are intended to be
attached to default Maven lifecycle when building packages, others can
be called directly from Maven command line.

%package tools
Summary:        XMvn tools

%description tools
This package provides various XMvn tools:
* XMvn Install, which is a command-line interface to XMvn installer.
  The installer reads reactor metadata and performs artifact
  installation according to specified configuration.
* XMvn Resolver, which is a very simple commald-line tool to resolve
  Maven artifacts from system repositories.  Basically it's just an
  interface to artifact resolution mechanism implemented by XMvn Core.
  The primary intended use case of XMvn Resolver is debugging local
  artifact repositories.
* XMvn Subst, which is a tool that can substitute Maven artifact files
  with symbolic links to corresponding files in artifact repository.

%prep
%autosetup -p1 -C

%mvn_package ::tar.gz: __noinstall
%mvn_package ":{xmvn,xmvn-connector}" xmvn
%mvn_package ":xmvn-{api,core,parent}" core
%mvn_package ":xmvn-mojo" mojo
%mvn_package ":xmvn-{install,resolve,subst,tools}" tools

# Don't put Class-Path attributes in manifests
%pom_remove_plugin :maven-jar-plugin xmvn-tools

# Copy Maven home packaged as RPM instead of unpacking Maven binary
# tarball with maven-dependency-plugin
%pom_remove_plugin :maven-dependency-plugin
maven_home=%{_datadir}/maven
mver=$(sed -n '/<mavenVersion>/{s/.*>\(.*\)<.*/\1/;p}' \
           xmvn-parent/pom.xml)
mkdir -p target/dependency/
cp -a "${maven_home}" target/dependency/apache-maven-$mver

%build
%{?jpb_env}
# Work around a conflict between XMvn 4 and XMvn 5 that prevents the
# install and builddep MOJOs to work.
xmvn -B -o -P\!quality verify
%mvn_artifact pom.xml
%mvn_artifact xmvn-parent/pom.xml
%mvn_artifact xmvn-tools/pom.xml
%mvn_artifact xmvn-api/pom.xml xmvn-api/target/xmvn-api-4.3.0.jar
%mvn_artifact xmvn-core/pom.xml xmvn-core/target/xmvn-core-4.3.0.jar
%mvn_artifact xmvn-connector/pom.xml xmvn-connector/target/xmvn-connector-4.3.0.jar
%mvn_artifact xmvn-mojo/pom.xml xmvn-mojo/target/xmvn-mojo-4.3.0.jar
%mvn_artifact xmvn-tools/xmvn-resolve/pom.xml xmvn-tools/xmvn-resolve/target/xmvn-resolve-4.3.0.jar
%mvn_artifact xmvn-tools/xmvn-subst/pom.xml xmvn-tools/xmvn-subst/target/xmvn-subst-4.3.0.jar
%mvn_artifact xmvn-tools/xmvn-install/pom.xml xmvn-tools/xmvn-install/target/xmvn-install-4.3.0.jar

version=4.*
tar --delay-directory-restore -xvf target/xmvn-*-bin.tar.gz
chmod -R +rwX %{name}-${version}
# These are installed as doc
rm -f %{name}-${version}/{AUTHORS-XMVN,README-XMVN.md,LICENSE,NOTICE,NOTICE-XMVN}
# Not needed - we use JPackage launcher scripts
rm -Rf %{name}-${version}/lib/{installer,resolver,subst}/
# Irrelevant Maven launcher scripts
rm -f %{name}-${version}/bin/*

%install
%mvn_install

version=4.*
maven_home=%{_datadir}/maven

install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -r%{?with_bootstrap:L} %{name}-${version}/* %{buildroot}%{_datadir}/%{name}/

for cmd in mvn mvnDebug; do
    cat <<EOF >%{buildroot}%{_datadir}/%{name}/bin/$cmd
#!/bin/sh -e
export _FEDORA_MAVEN_HOME="%{_datadir}/%{name}"
exec %{_datadir}/maven%{?maven_version_suffix}/bin/$cmd "\${@}"
EOF
    chmod 755 %{buildroot}%{_datadir}/%{name}/bin/$cmd
done

# helper scripts
%jpackage_script org.fedoraproject.xmvn.tools.install.cli.InstallerCli "" "" xmvn/xmvn-install:xmvn/xmvn-api:xmvn/xmvn-core:beust-jcommander:slf4j/api:slf4j/simple:objectweb-asm/asm:commons-compress:commons-lang3:commons-io xmvn-install
%jpackage_script org.fedoraproject.xmvn.tools.resolve.ResolverCli "" "" xmvn/xmvn-resolve:xmvn/xmvn-api:xmvn/xmvn-core:beust-jcommander xmvn-resolve
%jpackage_script org.fedoraproject.xmvn.tools.subst.SubstCli "" "" xmvn/xmvn-subst:xmvn/xmvn-api:xmvn/xmvn-core:beust-jcommander xmvn-subst

# copy over maven boot and lib directories
cp -r%{?with_bootstrap:L} ${maven_home}/boot/* %{buildroot}%{_datadir}/%{name}/boot/
cp -r%{?with_bootstrap:L} ${maven_home}/lib/* %{buildroot}%{_datadir}/%{name}/lib/
ln -sf %{_prefix}/lib/jansi/libjansi.so %{buildroot}%{_datadir}/%{name}/lib/jansi-native/

# possibly recreate symlinks that can be automated with xmvn-subst
%if %{without bootstrap}
%{name}-subst -s -R %{buildroot} %{buildroot}%{_datadir}/%{name}/
%endif

# /usr/bin/xmvn
ln -s %{_datadir}/%{name}/bin/mvn %{buildroot}%{_bindir}/%{name}

# mvn-local symlink
ln -s %{name} %{buildroot}%{_bindir}/mvn-local

# make sure our conf is identical to maven so yum won't freak out
install -d -m 755 %{buildroot}%{_datadir}/%{name}/conf/
cp -P ${maven_home}/conf/settings.xml %{buildroot}%{_datadir}/%{name}/conf/
cp -P ${maven_home}/bin/m2.conf %{buildroot}%{_datadir}/%{name}/bin/

# Make sure javapackages config is not bundled
rm -rf %{buildroot}%{_datadir}/%{name}/{configuration.xml,config.d/,conf/toolchains.xml,maven-metadata/}

# Toolchains
ln -sf %{_jpbindingdir}/xmvn-toolchains.xml %{buildroot}%{_datadir}/%{name}/conf/toolchains.xml
install -p -m 644 %{SOURCE25} %{buildroot}%{_datadir}/%{name}/conf/toolchains-openjdk25.xml
%jp_binding --verbose --base-pkg xmvn-minimal --binding-pkg xmvn-toolchain-openjdk25 --variant openjdk25 --ghost xmvn-toolchains.xml --target %{_datadir}/%{name}/conf/toolchains-openjdk25.xml --requires java-25-openjdk-devel

%files
%{_bindir}/mvn-local

%files minimal -f .mfiles-xmvn
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%dir %{_datadir}/%{name}/lib
%{_datadir}/%{name}/lib/*.jar
%{_datadir}/%{name}/lib/ext
%{_datadir}/%{name}/lib/jansi-native
%{_datadir}/%{name}/bin/m2.conf
%{_datadir}/%{name}/bin/mvn
%{_datadir}/%{name}/bin/mvnDebug
%{_datadir}/%{name}/boot
%{_datadir}/%{name}/conf

%files core -f .mfiles-core
%license LICENSE NOTICE
%doc AUTHORS README.md

%files mojo -f .mfiles-mojo

%files tools -f .mfiles-tools
%{_bindir}/%{name}-install
%{_bindir}/%{name}-resolve
%{_bindir}/%{name}-subst

%changelog
%autochangelog
