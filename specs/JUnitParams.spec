%global giturl  https://github.com/Pragmatists/JUnitParams

Name:           JUnitParams
Version:        1.1.1
Release:        %autorelease
Summary:        Parameterized Java tests

License:        Apache-2.0
URL:            https://pragmatists.github.io/JUnitParams/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{name}-%{version}.tar.gz
## Post-release bug fixes
# Release notes and Readme updated
Patch:          %{giturl}/commit/c060976.patch
# Add language identifiers to README.md for syntax highlighting
Patch:          %{giturl}/commit/280ee05.patch
# Show original exception thrown from test class constructor
Patch:          %{giturl}/commit/6bab69a.patch
# Better exception for missing parameters
Patch:          %{giturl}/commit/f0772e7.patch
# Better exception message for missing parameters
Patch:          %{giturl}/commit/90d47a5.patch

## Patches to fix testing with junit 4.13.  See:
## - https://github.com/Pragmatists/JUnitParams/issues/172
## - https://github.com/Pragmatists/JUnitParams/pull/182
# Fix parsing of strings into BigDecimal values
Patch:          %{name}-parse-bigdecimal.patch
# Fix single method test filters
Patch:          %{name}-single-method-filter.patch
# Use hasMessageContaining instead of hasMessage
Patch:          %{name}-has-message-containing.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:  mvn(org.assertj:assertj-core)

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
The JUnitParams project adds a new runner to JUnit and provides much
easier and more readable parameterized tests for JUnit >= 4.12.

The main differences with the standard JUnit Parameterized runner are:
- more explicit - params are in test method params, not class fields
- less code - you don't need a constructor to set up parameters
- you can mix parameterized with non-parameterized methods in one class
- params can be passed as a CSV string or from a parameters provider
  class
- parameters provider class can have as many parameters providing
  methods as you want, so that you can group different cases
- you can have a test method that provides parameters (no external
  classes or statics anymore)
- you can see actual parameter values in your IDE (in JUnit's
  Parameterized, it's only consecutive numbers of parameters)

%prep
%autosetup -n %{name}-%{name}-%{version} -p1

%conf
# sonatype-oss-parent is deprecated in Fedora
%pom_remove_parent

# Unnecessary plugins for an RPM build
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-release-plugin
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin

# Build for Java 1.8 at a minimum
%pom_xpath_set '//pom:source' 1.8
%pom_xpath_set '//pom:target' 1.8

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc README.md RELEASES.md
%license LICENSE.txt

%changelog
%autochangelog
