%global giturl  https://github.com/mojo-executor/mojo-executor

Name:           mojo-executor
Version:        2.4.1
Release:        %autorelease
Summary:        Execute other plugins within a maven plugin

License:        Apache-2.0
URL:            https://mojo-executor.github.io/mojo-executor/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{name}-parent-%{version}.tar.gz
# Fix a javadoc comment
Patch:          %{name}-javadoc.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
BuildRequires:  maven-local
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-embedder)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)

%description
The Mojo Executor provides a way to to execute other Mojos (plugins)
within a Maven plugin, allowing you to easily create Maven plugins that
are composed of other plugins.

%package parent
Summary:        Parent POM for mojo-executor

%description parent
%{summary}.

%package maven-plugin
Summary:        Maven plugin for mojo-executor

%description maven-plugin
%{summary}.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains %{summary}.

%prep
%autosetup -n %{name}-%{name}-parent-%{version} -p1

%conf
# Not needed for an RPM build
%pom_remove_plugin org.apache.maven.plugins:maven-deploy-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-install-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-release-plugin
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin

# These tests want maven-install-plugin to be installed.  I don't know why.
rm -fr mojo-executor-maven-plugin/src/it/mojo-executor-test-project-{quiet,with-dependencies}

%build
%mvn_build -s

# We end up with duplicate mojo-executor-parent entries in the reactor.  Why?
sed -i '4,13d' .xmvn-reactor

%install
%mvn_install

%files -f .mfiles-%{name}
%license LICENSE.txt
%doc README.md

%files parent -f .mfiles-%{name}-parent

%files maven-plugin -f .mfiles-%{name}-maven-plugin

%files javadoc -f .mfiles-javadoc

%changelog
%autochangelog
