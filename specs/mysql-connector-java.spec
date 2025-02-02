Name:           mysql-connector-java
Epoch:          1
Version:        8.0.30
Release:        %autorelease
Summary:        Official JDBC driver for MySQL
License:        GPL-2.0-only
URL:            https://dev.mysql.com/downloads/connector/j/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# Generated with generate-tarball.sh
Source0:        %{name}-%{version}-nojars.tar.xz
Source1:        generate-tarball.sh

Patch:          0001-Remove-coverage-test.patch
Patch:          0002-Remove-authentication-plugin.patch
Patch:          0003-Remove-StatementsTest.patch
Patch:          0004-Port-to-Java-21.patch

BuildRequires:  javapackages-local-openjdk21
BuildRequires:  ant-junit5
BuildRequires:  javassist
BuildRequires:  protobuf-java
BuildRequires:  slf4j

%description
MySQL Connector/J is a native Java driver that converts JDBC (Java Database
Connectivity) calls into the network protocol used by the MySQL database.
It lets developers working with the Java programming language easily build
programs and applets that interact with MySQL and connect all corporate
data, even in a heterogeneous environment. MySQL Connector/J is a Type
IV JDBC driver and has a complete JDBC feature set that supports the
capabilities of MySQL.

%prep
%autosetup -p1 -C

# xmlstarlet ed -L -N pom="http://maven.apache.org/POM/4.0.0" -u "/project/version" -v "8.0.33" src/build/misc/pom.xml
%pom_xpath_set 'pom:project/pom:version' %{version} src/build/misc/pom.xml

# We currently need to disable jboss integration because of missing jboss-common-jdbc-wrapper.jar (built from sources).
# See BZ#480154 and BZ#471915 for details.
rm -rf src/main/user-impl/java/com/mysql/cj/jdbc/integration/jboss
rm src/test/java/testsuite/regression/ConnectionRegressionTest.java
rm src/test/java/testsuite/regression/DataSourceRegressionTest.java
rm src/test/java/testsuite/simple/StatementsTest.java

%build
ant -Dcom.mysql.cj.build.jdk=%{java_home} \
    -Dcom.mysql.cj.extra.libs=%{_javadir} \
    test dist

%install
# Install the Maven build information
%mvn_file mysql:mysql-connector-java %{name}
%mvn_artifact src/build/misc/pom.xml build/%{name}-%{version}-SNAPSHOT/%{name}-%{version}-SNAPSHOT.jar
%mvn_install

%files -f .mfiles
%doc CHANGES README README.md
%license LICENSE

%changelog
%autochangelog
