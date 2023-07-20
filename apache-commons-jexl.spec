Name:           apache-commons-jexl
Version:        3.3
Release:        %autorelease
Summary:        Java Expression Language

License:        Apache-2.0
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
URL:            https://commons.apache.org/proper/commons-jexl/
Source0:        https://archive.apache.org/dist/commons/jexl/source/commons-jexl-%{version}-src.tar.gz
Source1:        https://archive.apache.org/dist/commons/jexl/source/commons-jexl-%{version}-src.tar.gz.asc
Source2:        https://downloads.apache.org/commons/KEYS

# Use the codehaus version of javacc-maven-plugin, which is available from
# Fedora, instead of ph-javacc-maven-plugin, which is not.
Patch0:         %{name}-javacc.patch

BuildRequires:  gnupg2
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:  mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires:  mvn(org.junit.vintage:junit-vintage-engine)

%description
JEXL is a library intended to facilitate the implementation of scripting
features in applications and frameworks written in Java.  JEXL
implements an Expression Language based on some extensions to the JSTL
Expression Language supporting most of the constructs seen in shell
script or ECMAScript.  Its goal is to expose scripting features usable
by technical operatives or consultants working with enterprise
platforms.

%javadoc_package

%prep
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -n commons-jexl3-%{version}-src -p1

# Remove workaround for fixed JavaCC bug.
# The workaround now causes build failure.
%pom_remove_plugin :maven-antrun-plugin

# Work around @{argLine} expansion failure
%pom_xpath_remove //pom:argLine

# Not needed for RPM builds
%pom_xpath_remove //pom:reporting
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :japicmp-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-scm-publish-plugin
%pom_remove_plugin :spotbugs-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt

%changelog
%autochangelog
