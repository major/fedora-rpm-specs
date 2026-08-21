Name:           jmock
Version:        2.14.0
Release:        %autorelease
Summary:        Java library for testing code with mock objects
# BSD 3-Clause license; see LICENSE.txt.
License:        BSD-3-Clause
URL:            https://www.jmock.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/jmock-developers/jmock-library/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-Port-to-jakarta.xml.ws-4.0.0.patch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(cglib:cglib)
BuildRequires:  mvn(com.google.auto.service:auto-service)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.thoughtworks.qdox:qdox)
BuildRequires:  mvn(jakarta.xml.ws:jakarta.xml.ws-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(org.apache-extras.beanshell:bsh)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.ow2.asm:asm)

%description
Mock objects help you design and test the interactions between the objects in
your programs.
The jMock library:
  * makes it quick and easy to define mock objects, so you don't break the
    rhythm of programming.
  * lets you precisely specify the interactions between your objects, reducing
    the brittleness of your tests.
  * works well with the auto-completion and re-factoring features of your IDE
  * plugs into your favorite test framework
  * is easy to extend.

%package example
Summary:        jMock Examples
%description example
jMock Examples.

%package imposters
Summary:        jMock imposters
%description imposters
jMock imposters.

%package junit3
Summary:        jMock JUnit 3 Integration
%description junit3
jMock JUnit 3 Integration.

%package junit4
Summary:        jMock JUnit 4 Integration
%description junit4
jMock JUnit 4 Integration.

%package junit5
Summary:        jMock JUnit 5 Integration
%description junit5
jMock JUnit 5 Integration.

%package legacy
Summary:        jMock Legacy Plugins
%description legacy
Plugins that make it easier to use jMock with legacy code.

%package testjar
Summary:        jMock Test Jar
%description testjar
Source for JAR files used in jMock Core tests.

%{?javadoc_package}

%prep
# -p1: strip one level directory in patch
# -n: base directory name
%autosetup -p1 -n %{name}-library-%{version}
# remove maven plugins that are not required for RPM builds
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin -r :versions-maven-plugin
%pom_remove_plugin :maven-gpg-plugin testjar
# Scala acceptance-test data is not available in Fedora and is not installed.
%pom_disable_module jmock-imposters-tests
%pom_disable_module jmock-imposters-testdata
# change dep artifact
%pom_change_dep :jaxws-api jakarta.xml.ws:jakarta.xml.ws-api jmock
# use correct maven artifact for @javax.annotations.Nullable
%pom_change_dep com.google.code.findbugs:annotations com.google.code.findbugs:jsr305 testjar
# don't install imposters-tests and parent package
%mvn_package :jmock-imposters-tests __noinstall
%mvn_package :jmock-parent __noinstall

%build
%mvn_build -s

%install
%mvn_install

%files           -f .mfiles-%{name}
%doc README*
%license LICENSE.txt
%files example   -f .mfiles-%{name}-example
%files imposters -f .mfiles-%{name}-imposters
%files junit3    -f .mfiles-%{name}-junit3
%files junit4    -f .mfiles-%{name}-junit4
%files junit5    -f .mfiles-%{name}-junit5
%files legacy    -f .mfiles-%{name}-legacy
%files testjar   -f .mfiles-%{name}-testjar
%license LICENSE.txt

%changelog
%autochangelog
