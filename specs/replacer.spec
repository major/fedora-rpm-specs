Name:           replacer
Version:        1.6
Release:        %autorelease
Summary:        Replacer Maven Mojo
License:        MIT
URL:            https://github.com/beiliubei/maven-replacer-plugin
# http://code.google.com/p/maven-replacer-plugin/
Source0:        https://github.com/beiliubei/maven-replacer-plugin/archive/%{version}.tar.gz
Patch1:         0001-Fix-build-with-Mockito-2.x.patch
Patch2:         0002-Port-to-maven-plugin-annotations-from-Javadoc-tags.patch
Patch3:         0003-Port-to-apache-commons-lang3.patch
Patch4:         0004-Port-to-hamcrest-3.patch
Patch5:         0005-Port-to-mockito-5.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.mockito:mockito-all)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(xerces:xercesImpl)

%description
Maven plugin to replace tokens in a given file with a value.

This plugin is also used to automatically generating PackageVersion.java
in the FasterXML.com project.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%autosetup -p1 -n maven-replacer-plugin-%{version}

# remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin :dashboard-maven-plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_change_dep :commons-lang org.apache.commons:commons-lang3

# remove hard-coded compiler settings
%pom_remove_plugin :maven-compiler-plugin

# "No mojo definitions were found for plugin" with maven-plugin-plugin 3.9
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-plugin-plugin']" '
<configuration><skipErrorNoDescriptorsFound>true</skipErrorNoDescriptorsFound></configuration>'

%mvn_file :%{name} %{name}
%mvn_alias :%{name} com.google.code.maven-replacer-plugin:maven-replacer-plugin

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
%autochangelog
