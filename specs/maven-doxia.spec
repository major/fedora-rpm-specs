Name:           maven-doxia
Epoch:          0
Version:        2.1.0
Release:        %autorelease
Summary:        Content generation framework
License:        Apache-2.0

URL:            https://maven.apache.org/doxia/
VCS:            git:https://github.com/apache/maven-doxia.git
Source0:        https://repo1.maven.org/maven2/org/apache/maven/doxia/doxia/%{version}/doxia-%{version}-source-release.zip
Source1:        https://repo1.maven.org/maven2/org/apache/maven/doxia/doxia/%{version}/doxia-%{version}-source-release.zip.asc
Source2:        https://downloads.apache.org/maven/KEYS

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  gpgverify
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.vladsch.flexmark:flexmark)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-abbreviation)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-autolink)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-definition)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-escaped-character)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-footnotes)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-gfm-strikethrough)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-tables)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-typographic)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-wikilink)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-ext-yaml-front-matter)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-util-ast)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-util-data)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-util-misc)
BuildRequires:  mvn(com.vladsch.flexmark:flexmark-util-sequence)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing)
BuildRequires:  mvn(org.codehaus.plexus:plexus-xml)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.jetbrains:annotations)
BuildRequires:  mvn(org.jsoup:jsoup)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)

# This can be removed when F45 reaches EOL
Obsoletes:      %{name}-logging-api < 1.13.0
Provides:       %{name}-logging-api = %{version}-%{release}
Obsoletes:      %{name}-module-confluence < 1.13.0
Provides:       %{name}-module-confluence = %{version}-%{release}
Obsoletes:      %{name}-module-docbook-simple < 1.13.0
Provides:       %{name}-module-docbook-simple = %{version}-%{release}
Obsoletes:      %{name}-module-fo < 1.13.0
Provides:       %{name}-module-fo = %{version}-%{release}
Obsoletes:      %{name}-module-latex < 1.13.0
Provides:       %{name}-module-latex = %{version}-%{release}
Obsoletes:      %{name}-module-rtf < 1.13.0
Provides:       %{name}-module-rtf = %{version}-%{release}
Obsoletes:      %{name}-module-twiki < 1.13.0
Provides:       %{name}-module-twiki = %{version}-%{release}
Obsoletes:      %{name}-module-xhtml < 1.13.0
Provides:       %{name}-module-xhtml = %{version}-%{release}
Obsoletes:      %{name}-tests < 1.13.0
Provides:       %{name}-tests = %{version}-%{release}

%global _desc %{expand:Doxia is a content generation framework which aims to provide its users with
powerful techniques for generating static and dynamic content.  Doxia can be
used to generate static sites in addition to being incorporated into dynamic
content generation systems like blogs, wikis and content management systems.}

%description
%_desc

%package        core
Summary:        Core classes and interfaces for %{name}
Requires:       %{name}-sink-api = %{version}-%{release}

%description    core
%_desc

This package contains the core classes and interfaces for %{name}.

%package        modules
Summary:        Doxia modules for several markup languages
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-sink-api = %{version}-%{release}

%description    modules
%_desc

This package provides doxia modules for several markup languages.

%package        module-apt
Summary:        Almost Plain Text module for %{name}
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-sink-api = %{version}-%{release}

%description    module-apt
%_desc

This package contains a doxia module for Almost Plain Text (APT) source
documents.  APT format is supported both as source and target formats.

%package        module-fml
Summary:        FML module for %{name}
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-sink-api = %{version}-%{release}

%description    module-fml
%_desc

This package contains a doxia module for FML source documents.  FML
format is only supported as a source format.

%package        module-markdown
Summary:        Markdown module for %{name}
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-module-xhtml5 = %{version}-%{release}
Requires:       %{name}-sink-api = %{version}-%{release}

%description    module-markdown
%_desc

This package contains a doxia module for Markdown source documents.

%package        module-xdoc
Summary:        Xdoc module for %{name}
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-sink-api = %{version}-%{release}

%description    module-xdoc
%_desc

This package contains a doxia module for Xdoc source documents.  Xdoc
format is supported both as source and target formats.

%package        module-xhtml5
Summary:        XHTML5 module for %{name}
Requires:       %{name}-core = %{version}-%{release}
Requires:       %{name}-sink-api = %{version}-%{release}

%description    module-xhtml5
%_desc

This package contains a doxia module for XHTML5 source documents.
XHTML5 format is supported both as source and target formats.

%package        sink-api
Summary:        Sink API for %{name}

%description    sink-api
%_desc

This package contains the sink API for %{name}.  The supported output
document formats are accessed via this API.

%package        test-docs
Summary:        Test documents for %{name}

%description    test-docs
%_desc

This package contains several test documents to check syntax structures
under Doxia.

%package        javadoc
# Apache-2.0: the content
# MIT: jquery and jquery-ui
# GPL-2.0-only: script.js, search.js, jquery-ui.overrides.css
License:        Apache-2.0 AND MIT AND GPL-2.0-only WITH Classpath-exception-2.0
Summary:        API documentation for %{name}

%description    javadoc
API documentation for %{name}.

%prep
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -p1 -n doxia-%{version}

# Convert to Unix line terminators
for f in $(find . -name '*.java' -o -name '*.xml'); do
  sed -i.orig 's/\r//' $f
  touch -r $f.orig $f
  rm -f $f.orig
done

# Plugins not needed for an RPM build
%pom_remove_plugin org.apache.maven.plugins:maven-scm-publish-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin
%pom_remove_plugin org.apache.rat:apache-rat-plugin
%pom_remove_plugin :maven-install-plugin doxia-modules/doxia-module-markdown

# Needed for the tests
%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:test

# requires network
rm doxia-core/src/test/java/org/apache/maven/doxia/util/XmlValidatorTest.java

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-doxia
%doc README.md
%license LICENSE NOTICE
%files core -f .mfiles-doxia-core
%license LICENSE NOTICE
%files module-apt -f .mfiles-doxia-module-apt
%files module-fml -f .mfiles-doxia-module-fml
%files module-markdown -f .mfiles-doxia-module-markdown
%files modules -f .mfiles-doxia-modules
%files module-xdoc -f .mfiles-doxia-module-xdoc
%files module-xhtml5 -f .mfiles-doxia-module-xhtml5
%files sink-api -f .mfiles-doxia-sink-api
%files test-docs -f .mfiles-doxia-test-docs
%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
%autochangelog
