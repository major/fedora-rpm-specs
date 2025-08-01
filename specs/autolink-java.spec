Name:           autolink-java
Version:        0.12.0
Release:        %autorelease
Summary:        Java library to extract links from plain text

License:        MIT
URL:            https://github.com/robinst/autolink-java
VCS:            git:%{url}.git
Source:         %{url}/archive/autolink-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  noarch %{java_arches}

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)

%description
Autolink is a Java library to extract links such as URLs and email
addresses from plain text.  It's smart about where a link ends, such as
with trailing punctuation.

%{?javadoc_package}

%prep
%autosetup -n %{name}-autolink-%{version}

%conf
# Not needed for an RPM build
%pom_remove_plugin com.github.siom79.japicmp:japicmp-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-release-plugin
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin

# We do not want to run benchmarks
%pom_remove_dep org.openjdk.jmh:jmh-core
rm src/test/java/org/nibor/autolink/AutolinkBenchmark.java

# Needed for the tests
%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:test

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG.md README.md
%license LICENSE

%changelog
%autochangelog
