# Break dependency loops in a bootstrap situation
%bcond bootstrap 0

# Disable Maven reporting in bootstrap mode and in RHEL
%bcond maven_reporting %[!(%{with bootstrap} || 0%{?rhel})]

%global giturl  https://github.com/mojohaus/javacc-maven-plugin

Name:           javacc-maven-plugin
Version:        3.1.0
Release:        %autorelease
Summary:        JavaCC Maven Plugin

License:        Apache-2.0
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
URL:            https://www.mojohaus.org/javacc-maven-plugin/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.javacc:javacc)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-xml)
%endif

%if %{with maven_reporting}
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
%endif

%description
Maven Plugin for processing JavaCC grammar files.

%{?javadoc_package}

%prep
%autosetup -p1 -C

%conf
cp -p %{SOURCE1} .

# Do not use jtb, which is unmaintained.  It is accessed only via reflection to
# avoid depending on Java 1.5 for compilation.
%pom_remove_dep edu.ucla.cs.compilers:jtb

# Disable integration tests
%pom_remove_plugin org.apache.maven.plugins:maven-invoker-plugin
rm -fr src/it

# Disable building the web site
rm -fr src/site

# In bootstrap mode, disable documentation and reporting
%if %{without maven_reporting}
%pom_remove_dep org.apache.maven.doxia:
%pom_remove_dep org.apache.maven.reporting:
rm src/main/java/org/codehaus/mojo/javacc/JJDocMojo.java
%endif

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE-2.0.txt src/main/resources/NOTICE

%changelog
%autochangelog
