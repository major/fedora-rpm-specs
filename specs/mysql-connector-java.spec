Name:           mysql-connector-java
Epoch:          1
Version:        9.7.0
Release:        %autorelease
Summary:        Official JDBC driver for MySQL
License:        GPL-2.0-only WITH Universal-FOSS-exception-1.0
URL:            https://dev.mysql.com/downloads/connector/j/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# Generated with generate-tarball.sh
Source0:        %{name}-%{version}.tar.zst
Source1:        generate-tarball.sh

Patch:          Remove-authentication-plugin.patch
Patch:          Port-to-Java-21.patch
Patch:          Remove-usage-of-io.opentelemetry.api.patch
Patch:          Add-package-tests-target.patch

BuildRequires:  javapackages-local-openjdk25
BuildRequires:  ant-junit
BuildRequires:  ant-junit5
BuildRequires:  javassist
BuildRequires:  protobuf-java
BuildRequires:  slf4j
BuildRequires:  hamcrest

%description
MySQL Connector/J is a native Java driver that converts JDBC (Java Database
Connectivity) calls into the network protocol used by the MySQL database.
It lets developers working with the Java programming language easily build
programs and applets that interact with MySQL and connect all corporate
data, even in a heterogeneous environment. MySQL Connector/J is a Type
IV JDBC driver and has a complete JDBC feature set that supports the
capabilities of MySQL.

%package tests
Summary: Tests for %{name}

%description tests
This package contains tests for %{name}.

%prep
%autosetup -p1 -C

# xmlstarlet ed -L -N pom="http://maven.apache.org/POM/4.0.0" -u "/project/version" -v "8.0.33" src/build/misc/pom.xml
%pom_xpath_set 'pom:project/pom:version' %{version} src/build/misc/pom.xml

# Remove usage of 'io.opentelemetry.api'
rm -rv src/main/core-impl/java/com/mysql/cj/otel

%build
ant package-no-sources \
 -Dcom.mysql.cj.build.jdk=%{java_home} \
 -Dcom.mysql.cj.extra.libs=%{_javadir} \
 -Dcom.mysql.cj.dist.noMaven=true \
;

# Compile test suite and create tests JAR + classpath file
ant package-tests \
 -Dcom.mysql.cj.build.jdk=%{java_home} \
 -Dcom.mysql.cj.extra.libs=%{_javadir} \
 -Dcom.mysql.cj.build.noCleanBetweenCompiles=yes \
;

%install
%mvn_file mysql:mysql-connector-java %{name}
%mvn_artifact build/mysql-connector-j-%{version}-SNAPSHOT/pom.xml build/mysql-connector-j-%{version}-SNAPSHOT/mysql-connector-j-%{version}-SNAPSHOT.jar
%mvn_install
install -m 644 -D build/mysql-connector-j-tests.jar %{buildroot}%{_javadir}/%{name}-tests.jar
install -m 644 -D build/tests-classpath %{buildroot}%{_datadir}/%{name}-tests/classpath
cp -a src/test/config/ssl-test-certs %{buildroot}%{_datadir}/%{name}-tests/ssl-test-certs

%files -f .mfiles
%doc CHANGES README README.md
%license LICENSE

%files tests
%{_javadir}/%{name}-tests.jar
%{_datadir}/%{name}-tests
%license LICENSE

%changelog
%autochangelog
