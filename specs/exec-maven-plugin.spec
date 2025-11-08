Name:           exec-maven-plugin
Version:        3.6.2
Release:        %autorelease
Summary:        Exec Maven Plugin

License:        Apache-2.0
URL:            https://www.mojohaus.org/exec-maven-plugin/
Source0:        https://repo1.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  maven-artifact-transfer
BuildRequires:  maven-dependency-plugin
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

%description
A plugin to allow execution of system and Java programs.

%javadoc_package

%prep
%setup -q -n exec-maven-plugin-%{version}

find . -name *.jar -delete

%pom_remove_plugin :animal-sniffer-maven-plugin

#Drop test part. sonatype-aerther not available
%pom_remove_dep :mockito-core
%pom_remove_dep :maven-plugin-testing-harness
%pom_remove_dep :slf4j-simple

%pom_remove_plugin :sisu-maven-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-toolchains-plugin

rm -rf src/test/

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%dir %{_javadir}/%{name}

%changelog
%autochangelog
