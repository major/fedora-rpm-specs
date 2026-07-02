%global giturl  https://github.com/jakartaee/jsonp-api

Name:           jakarta-json
Version:        2.1.3
Release:        %autorelease
Summary:        Jakarta JSON Processing

License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://projects.eclipse.org/projects/ee4j.jsonp
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}-RELEASE.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
Jakarta JSON Processing provides portable APIs to parse, generate, transform,
and query JSON documents.

%{?javadoc_package}

%prep
%autosetup -n jsonp-api-%{version}-RELEASE

%conf
# org.eclipse.ee4j:project is not available in Fedora
%pom_remove_parent api

# Unnecessary plugins for an RPM build
%pom_remove_plugin org.glassfish.copyright:glassfish-copyright-maven-plugin api
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin api
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin api

# This plugin is not available in Fedora
%pom_remove_plugin com.github.spotbugs:spotbugs-maven-plugin api

%build
cd api
%mvn_build
cd -

%install
cd api
%mvn_install
cd -
ln -s api/.mfiles-javadoc .
rm -rf %{buildroot}%{_javadocdir}/%{name}/legal

%files -f api/.mfiles
%doc README.md
%license LICENSE.md NOTICE.md

%changelog
%autochangelog
