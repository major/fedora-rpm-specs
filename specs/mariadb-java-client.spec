Name:           mariadb-java-client
Version:        3.5.6
Release:        %autorelease
Summary:        Connects applications developed in Java to MariaDB and MySQL databases
License:        LGPL-2.1-only
URL:            https://mariadb.com/kb/en/mariadb/about-mariadb-connector-j/
Source0:        https://github.com/mariadb-corporation/mariadb-connector-j/archive/refs/tags/%{version}.tar.gz#/mariadb-connector-j-%{version}.tar.gz
# optional dependency not in Fedora
Patch:          0001-Remove_waffle-jna.patch
Patch:          0002-Remove-usage-of-junit-pioneer.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.java.dev.jna:jna-platform)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.slf4j:slf4j-api)

# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.5.0-7

%description
MariaDB Connector/J is a Type 4 JDBC driver, also known as the Direct to
Database Pure Java Driver. It was developed specifically as a lightweight
JDBC connector for use with MySQL and MariaDB database servers.

%package        tests
Summary:        Tests for %{name}

%description    tests
This package contains tests for %{name}.

%prep
%autosetup -p1 -n mariadb-connector-j-%{version}

%pom_remove_dep ch.qos.logback:logback-classic
grep -l -r '^import ch\.qos\.logback\.classic' src/test | xargs rm -v

%pom_remove_dep com.github.waffle:waffle-jna
%pom_remove_dep software.amazon.awssdk:bom
%pom_remove_dep software.amazon.awssdk:rds

# upstream uses two crypto implementations: bouncycastle and one from JDK15+
%pom_remove_dep org.bouncycastle:bcpkix-jdk18on
mv src/main/java15/org/mariadb/jdbc/plugin/authentication/standard/ParsecPasswordPluginTool.java src/main/java/org/mariadb/jdbc/plugin/authentication/standard/ParsecPasswordPluginTool.java
sed -i '/requires.*org\.bouncycastle.*;/d' src/main/java9/module-info.java

# used in buildtime for generating OSGI metadata
%pom_remove_plugin biz.aQute.bnd:bnd-maven-plugin

%pom_add_dep net.java.dev.jna:jna
%pom_add_dep net.java.dev.jna:jna-platform

# make the slf4j dependency version-independent
%pom_remove_dep org.slf4j:slf4j-api
%pom_add_dep org.slf4j:slf4j-api
%pom_add_dep org.junit.jupiter:junit-jupiter-params

# use the latest OSGi implementation
%pom_change_dep -r :org.osgi.core org.osgi:osgi.core
%pom_change_dep -r :org.osgi.compendium org.osgi:osgi.cmpn

rm -r src/main/java/org/mariadb/jdbc/plugin/credential/aws

# removing dependencies and 'provides', which mariadb-java-client cannot process from module-info.java
sed -i -e '/aws/d' -e '/waffle/d' src/main/java9/module-info.java

# removing missing dependencies form META-INF, so that the mariadb-java-client module would be valid
sed -i '/aws/d' src/{main,test}/resources/META-INF/services/org.mariadb.jdbc.plugin.CredentialPlugin
rm -f src/main/java/org/mariadb/jdbc/plugin/authentication/addon/gssapi/WindowsNativeSspiAuthentication.java

# disable tests using junit.pioneer annotations
%pom_remove_dep org.junit-pioneer:junit-pioneer

%mvn_file org.mariadb.jdbc:%{name} %{name}
%mvn_alias org.mariadb.jdbc:%{name} mariadb:mariadb-connector-java

%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin -r :maven-gpg-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

# Install -tests Jar as well
%pom_xpath_inject 'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-jar-plugin"]' '
<executions>
  <execution>
    <goals>
      <goal>test-jar</goal>
    </goals>
  </execution>
</executions>'
%mvn_package org.mariadb.jdbc:mariadb-java-client::tests: tests

%build
# tests are skipped, while they require running application server
# NOTE this parameter skips running tests but still compiles them (instead of -f)
%mvn_build -j -- -DskipTests=true

xmvn -Dmdep.outputFile=tests-classpath dependency:build-classpath --offline

%install
%mvn_install
install -m 644 -D tests-classpath %{buildroot}/%{_datadir}/%{name}-tests/classpath

%files -f .mfiles
%doc README.md
%license LICENSE

%files tests -f .mfiles-tests
%{_datadir}/%{name}-tests
%license LICENSE

%changelog
%autochangelog
