Name:           maven-doxia-sitetools
Version:        2.1.0
Release:        %autorelease
Summary:        Doxia content generation framework
License:        Apache-2.0
URL:            https://maven.apache.org/doxia/
VCS:            git:https://github.com/apache/maven-doxia-sitetools.git
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/doxia/doxia-sitetools/%{version}/doxia-sitetools-%{version}-source-release.zip
Source1:        https://repo1.maven.org/maven2/org/apache/maven/doxia/doxia-sitetools/%{version}/doxia-sitetools-%{version}-source-release.zip.asc
Source2:        https://downloads.apache.org/maven/KEYS

Patch:          0001-Remove-dependency-on-velocity-tools.patch

BuildRequires:  gpgverify
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-resolver-provider)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-xhtml5)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-connector-basic)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-impl)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-transport-wagon)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http)
BuildRequires:  mvn(org.apache.velocity:velocity-engine-core)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-i18n)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity)
BuildRequires:  mvn(org.codehaus.plexus:plexus-xml)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.junit:junit-bom:pom:)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)

%description
Doxia is a content generation framework which aims to provide its users with
powerful techniques for generating static and dynamic content.  Doxia can be
used to generate static sites in addition to being incorporated into dynamic
content generation systems like blogs, wikis and content management systems.

%package        javadoc
# Apache-2.0: the content
# MIT: jquery and jquery-ui
# GPL-2.0-only: script.js, search.js, jquery-ui.overrides.css
License:        Apache-2.0 AND MIT AND GPL-2.0-only WITH Classpath-exception-2.0
Summary:        Javadoc for %{name}

%description    javadoc
API documentation for %{name}.

%prep
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -p1 -n doxia-sitetools-%{version}

# Unavailable plugins
%pom_remove_plugin org.apache.maven.plugins:maven-scm-publish-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin
%pom_remove_plugin org.apache.rat:apache-rat-plugin

# Unavailable dependencies
%pom_remove_dep org.htmlunit:htmlunit doxia-site-renderer
%pom_remove_dep org.apache.velocity.tools:velocity-tools-generic doxia-site-renderer

# This module has unavailable dependencies
%pom_disable_module doxia-site-scm-context

# Add a missing dependency
%pom_add_dep org.codehaus.plexus:plexus-utils doxia-skin-model

# Not actually used in the build or needed at runtime
%pom_remove_dep -r org.apache.maven.doxia:doxia-module-apt
%pom_remove_dep -r org.apache.maven.doxia:doxia-module-fml
%pom_remove_dep -r org.apache.maven.doxia:doxia-module-markdown
%pom_remove_dep -r org.apache.maven.doxia:doxia-module-xdoc
%pom_remove_dep -r org.apache.maven.plugin-testing:maven-plugin-testing-harness
%pom_remove_dep -r org.codehaus.plexus:plexus-testing

%build
# tests can't run because of missing deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
%autochangelog
