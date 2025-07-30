Name:           fop
Summary:        XSL-driven print formatter
Version:        2.9
Release:        %autorelease
# ASL 1.1:
# several files in fop-core/src/main/resources/org/apache/fop/render/awt/viewer/resources
# * Viewer_cs.properties
# * Viewer_fi.properties
# * Viewer_ja.properties
# * Viewer_pl.properties
# * Viewer_ru.properties
# * Viewer_tr.properties
# rest is ASL 2.0
License:        Apache-2.0 AND Apache-1.1
URL:            https://xmlgraphics.apache.org/fop
Source0:        https://www.apache.org/dist/xmlgraphics/%{name}/source/%{name}-%{version}-src.tar.gz
Source1:        https://www.apache.org/dist/xmlgraphics/%{name}/source/%{name}-%{version}-src.tar.gz.asc
Source2:        %{name}.script
Source3:        batik-pdf-MANIFEST.MF
Source4:        https://www.apache.org/licenses/LICENSE-1.1.txt
Source5:        5C9A30FF22B2C02F30261C305B93F1DF7CDB6DEA.gpg
Patch1:         0001-Main.patch
Patch2:         0002-Use-sRGB.icc-color-profile-from-colord-package.patch
Patch3:         0003-Port-to-QDox-2.0.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Requires:       java-21
Requires:       xalan-j2 >= 2.7.0
Requires:       xml-commons-apis >= 1.3.04
# Explicit requires for javapackages-tools since fop script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-logging
BuildRequires:  batik
BuildRequires:  fontbox
BuildRequires:  gnupg2
BuildRequires:  javapackages-local-openjdk21
BuildRequires:  junit
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-local-openjdk21
BuildRequires:  build-helper-maven-plugin
BuildRequires:  mvn(javax.servlet:servlet-api)
# For servlet, not packaged
#BuildRequires:  maven-war-plugin
BuildRequires:  pdfbox
BuildRequires:  qdox
BuildRequires:  xml-maven-plugin
BuildRequires:  xmlgraphics-commons >= 2.8
BuildRequires:  xmlunit
BuildRequires:  xmlunit-assertj
BuildRequires:  xmlunit-core

%description
FOP is the world's first print formatter driven by XSL formatting
objects. It is a Java application that reads a formatting object tree
and then turns it into a PDF document. The formatting object tree, can
be in the form of an XML document (output by an XSLT engine like XT or
Xalan) or can be passed in memory as a DOM Document or (in the case of
XT) SAX events.

%package javadoc
Summary:        Javadoc for %{name}

%description    javadoc
Javadoc for %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE5}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

cp %{SOURCE4} LICENSE-1.1

rm -f fop/lib/*.jar fop/lib/build/*.jar

# Not packaged
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_dep javax.media:jai-core fop-core
%pom_remove_dep com.sun.media:jai-codec fop-core
%pom_remove_dep net.sf.offo:fop-hyph fop-core
%pom_remove_dep net.sf.saxon:saxon fop-core
# Update to current xmlunit
%pom_change_dep xmlunit:xmlunit org.xmlunit:xmlunit-core fop-core
%pom_add_dep org.xmlunit:xmlunit-assertj3 fop-core
# Requires maven-war-plugin
%pom_disable_module fop-servlet
# Requires JAI, not packaged
rm fop-core/src/main/java/org/apache/fop/util/bitmap/JAIMonochromeBitmapConverter.java


%build
# Skip tests for now, make dirs needed by build but created by tests
mkdir -p fop-events/target/test-classes
%mvn_build -f


%install
%mvn_install
# inject OSGi manifest
jar ufm %{buildroot}%{_javadir}/%{name}/%{name}.jar %{SOURCE3}

# script
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 %{SOURCE2} %{buildroot}%{_bindir}/fop

# data
install -d -m 755 %{buildroot}%{_datadir}/%{name}/conf
cp -rp fop/conf/* %{buildroot}%{_datadir}/%{name}/conf

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/xmvn-apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files -f .mfiles
%doc README NOTICE
%license LICENSE LICENSE-1.1
%{_datadir}/%{name}
%{_bindir}/fop

%files javadoc
%doc %{_javadocdir}/%{name}
%license LICENSE LICENSE-1.1


%changelog
%autochangelog
