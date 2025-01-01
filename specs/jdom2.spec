%bcond_with bootstrap

Name:           jdom2
Version:        2.0.6.1
Release:        %autorelease
Summary:        Java manipulation of XML made easy
License:        Saxpath
URL:            http://www.jdom.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
# Bnd tool configuration
Source3:        bnd.properties
# Remove bundled jars that might not have clear licensing
Source4:        generate-tarball.sh

# Use system libraries
# Disable gpg signatures
# Process contrib and junit pom files
Patch:          0001-Adapt-build.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  ant-junit
%endif

%description
JDOM is a Java-oriented object model which models XML documents.
It provides a Java-centric means of generating and manipulating
XML documents. While JDOM inter-operates well with existing
standards such as the Simple API for XML (SAX) and the Document
Object Model (DOM), it is not an abstraction layer or
enhancement to those APIs. Rather, it seeks to provide a robust,
light-weight means of reading and writing XML data without the
complex and memory-consumptive options that current API
offerings provide.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%autosetup -p1 -C


sed -i 's/\r//' LICENSE.txt

# Unable to run coverage: use log4j12 but switch to log4j 2.x
sed -i.coverage "s|coverage, jars|jars|" build.xml

# XPath functionality is not needed
rm -rf core/src/java/org/jdom2/xpath/
sed -i '/import org.jdom2.xpath.XPathFactory/d' core/src/java/org/jdom2/JDOMConstants.java

%build
mkdir lib
%ant -Dversion=%{version} -Dcompile.source=1.8 -Dcompile.target=1.8 -Dj2se.apidoc=%{_javadocdir}/java maven

# Make jar into an OSGi bundle
# XXX disabled until BND is fixed
#bnd wrap --output build/package/jdom-%{version}.bar --properties %{SOURCE3} \
#         --version %{version} build/package/jdom-%{version}.jar
#mv build/package/jdom-%{version}.bar build/package/jdom-%{version}.jar

%install
%mvn_artifact build/maven/core/%{name}-%{version}.pom build/package/jdom-%{version}.jar
%mvn_install -J build/apidocs

%files -f .mfiles
%doc CHANGES.txt COMMITTERS.txt README.md TODO.txt
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
%autochangelog
