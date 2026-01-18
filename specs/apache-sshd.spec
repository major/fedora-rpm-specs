%global bouncycastleJdk 18
%global bouncycastleVer 1.83

Epoch:          1
Name:           apache-sshd
Version:        2.16.0
Release:        4%{?dist}
Summary:        Apache SSHD

# One file has ISC licensing:
#   sshd-common/src/main/java/org/apache/sshd/common/config/keys/loader/openssh/kdf/BCrypt.java
# Automatically converted from old format: ASL 2.0 and ISC - review is highly recommended.
License:        Apache-2.0 AND ISC
URL:            http://mina.apache.org/sshd-project

Source0:        https://archive.apache.org/dist/mina/sshd/%{version}/apache-sshd-%{version}-src.tar.gz

# Avoid optional dep on tomcat native APR library
Patch0:         0001-Avoid-optional-dependency-on-native-tomcat-APR-libra.patch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.i2p.crypto:eddsa)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit47)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk%{bouncycastleJdk}on)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk%{bouncycastleJdk}on)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
Apache SSHD is a 100% pure java library to support the SSH protocols on both
the client and server side.

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
This package provides %{name}.

%prep
%setup -q

# Avoid optional dep on tomcat native APR library
%patch -P0 -p1
rm -rv sshd-core/src/main/java/org/apache/sshd/agent/unix

# Avoid unnecessary dep on spring framework
%pom_remove_dep :spring-framework-bom
%pom_remove_dep :testcontainers-bom sshd-sftp sshd-core sshd-scp

# Build the core modules only
%pom_disable_module assembly
%pom_disable_module sshd-mina
%pom_disable_module sshd-netty
%pom_disable_module sshd-ldap
%pom_disable_module sshd-git
%pom_disable_module sshd-contrib
%pom_disable_module sshd-spring-sftp
%pom_disable_module sshd-cli
%pom_disable_module sshd-openpgp
%pom_disable_module sshd-benchmarks

# Disable plugins we don't need for RPM builds
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-antrun-plugin
%pom_remove_plugin :impsort-maven-plugin
%pom_remove_plugin :formatter-maven-plugin . sshd-core
%pom_remove_plugin :maven-remote-resources-plugin
%pom_remove_plugin :maven-shade-plugin sshd-benchmarks

# Suppress generation of uses clauses
%pom_xpath_inject "pom:configuration/pom:instructions" "<_nouses>true</_nouses>" .
sed "s;<bouncycastle.version>.*;<bouncycastle.version>%{bouncycastleVer}</bouncycastle.version>;g" -i pom.xml

%build
# Can't run tests, they require ch.ethz.ganymed:ganymed-ssh2
%mvn_build -f -- -Dworkspace.root.dir=$(pwd)

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.md
%license LICENSE.txt NOTICE.txt assembly/src/main/legal/licenses/jbcrypt.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt assembly/src/main/legal/licenses/jbcrypt.txt

%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

%autochangelog
