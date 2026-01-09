%global classpath batik:xml-commons-apis:xml-commons-apis-ext:xmlgraphics-commons

Name:           batik
Version:        1.19
Release:        1%{?dist}
Summary:        Scalable Vector Graphics for Java
# Automatically converted from old format: ASL 2.0 and W3C - review is highly recommended.
License:        Apache-2.0 AND W3C
URL:            https://xmlgraphics.apache.org/batik/
Source0:        http://archive.apache.org/dist/xmlgraphics/batik/source/batik-src-%{version}.zip
Source1:        %{name}-security.policy

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.xmlgraphics:xmlgraphics-commons)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(xml-apis:xml-apis)
BuildRequires:  mvn(xml-apis:xml-apis-ext)

%description
Batik is a Java(tm) technology based toolkit for applications that want
to use images in the Scalable Vector Graphics (SVG) format for various
purposes, such as viewing, generation or manipulation.

%package util
Summary:        Batik utility library

%description util
Util component of the Apache Batik SVG manipulation and rendering library.

%package css
Summary:        Batik CSS engine

%description css
CSS component of the Apache Batik SVG manipulation and rendering library.

%package        squiggle
Summary:        Batik SVG browser
# Explicit requires for javapackages-tools since squiggle-script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
# Requires AWT, so can't rely on java-headless alone
Requires:       java-25

%description    squiggle
The Squiggle SVG Browser lets you view SVG file, zoom, pan and rotate
in the content and select text items in the image and much more.

%package        svgpp
Summary:        Batik SVG pretty printer
# Explicit requires for javapackages-tools since svgpp-script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

%description    svgpp
The SVG Pretty Printer lets developers "pretty-up" their SVG files and
get their tabulations and other cosmetic parameters in order. It can
also be used to modify the DOCTYPE declaration on SVG files.

%package        ttf2svg
Summary:        Batik SVG font converter
# Explicit requires for javapackages-tools since ttf2svg-script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

%description    ttf2svg
The SVG Font Converter lets developers convert character ranges from
the True Type Font format to the SVG Font format to embed in SVG
documents. This allows SVG document to be fully self-contained be
rendered exactly the same on all systems.

%package        rasterizer
Summary:        Batik SVG rasterizer
# Explicit requires for javapackages-tools since rasterizer-script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

%description    rasterizer
The SVG Rasterizer is a utility that can convert SVG files to a raster
format. The tool can convert individual files or sets of files, making
it easy to convert entire directories of SVG files. The supported
formats are JPEG, PNG, and TIFF, however the design allows new formats
to be added easily.

%package        slideshow
Summary:        Batik SVG slideshow
# Explicit requires for javapackages-tools since slideshow-script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
# Requires AWT, so can't rely on java-headless alone
Requires:       java-25

%description    slideshow
Batik SVG slideshow.

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
Javadoc for %{name}.

%package        demo
Summary:        Samples for %{name}
Requires:       %{name} = %{version}-%{release}

%description    demo
Demonstrations and samples for %{name}.


%prep
%setup -q -n %{name}-%{version}

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

cp -p %{SOURCE1} batik-svgrasterizer/src/main/resources/org/apache/batik/apps/rasterizer/resources/rasterizer.policy
cp -p %{SOURCE1} batik-svgbrowser/src/main/resources/org/apache/batik/apps/svgbrowser/resources/svgbrowser.policy

# Generate OSGi metadata
for pom in `find -mindepth 2 -name pom.xml -not -path ./batik-all/pom.xml`; do
    %pom_add_plugin org.apache.felix:maven-bundle-plugin $pom "
        <extensions>true</extensions>
        <configuration>
            <instructions>
                <Bundle-SymbolicName>org.apache.batik.$(sed 's:./batik-::;s:/pom.xml::' <<< $pom)</Bundle-SymbolicName>
            </instructions>
        </configuration>
    "
    %pom_xpath_inject pom:project '<packaging>bundle</packaging>' $pom
done

# The "old-test" module cannot be built due to missing deps in Fedora
%pom_disable_module batik-test-old

# Remove optional deps on rhino and jython
%pom_remove_dep :rhino batik-{bridge,script}
%pom_remove_dep :jython batik-script
rm -rf batik-script/src/main/java/org/apache/batik/script/{jpython,rhino}
rm batik-bridge/src/main/java/org/apache/batik/bridge/BatikWrapFactory.java
rm batik-bridge/src/main/java/org/apache/batik/bridge/SVG12RhinoInterpreter.java
rm batik-bridge/src/main/java/org/apache/batik/bridge/RhinoInterpreter.java
rm batik-bridge/src/main/java/org/apache/batik/bridge/RhinoInterpreterFactory.java
rm batik-bridge/src/main/java/org/apache/batik/bridge/EventTargetWrapper.java
rm batik-bridge/src/main/java/org/apache/batik/bridge/GlobalWrapper.java
rm batik-bridge/src/main/java/org/apache/batik/bridge/WindowWrapper.java

%mvn_package :batik-squiggle squiggle
%mvn_package :batik-squiggle-ext squiggle
%mvn_package :batik-svgpp svgpp
%mvn_package :batik-ttf2svg ttf2svg
%mvn_package :batik-rasterizer rasterizer
%mvn_package :batik-rasterizer-ext rasterizer
%mvn_package :batik-slideshow slideshow
%mvn_package :batik-css css
%mvn_package :batik-constants util
%mvn_package :batik-shared-resources util
%mvn_package :batik-i18n util
%mvn_package :batik-util util
%mvn_package ':batik-test*' __noinstall

%mvn_file :batik-all batik-all

#no jacl rpm and it breaks javadoc
rm batik-script/src/main/java/org/apache/batik/script/jacl/JaclInterpreter.java

%build
%mvn_build

%install
%mvn_install

%jpackage_script org.apache.batik.apps.svgbrowser.Main '' '' %{classpath}:rhino squiggle true
%jpackage_script org.apache.batik.apps.svgpp.Main '' '' %{classpath} svgpp true
%jpackage_script org.apache.batik.apps.ttf2svg.Main '' '' %{classpath} ttf2svg true
%jpackage_script org.apache.batik.apps.rasterizer.Main '' '' %{classpath}:rhino rasterizer true
%jpackage_script org.apache.batik.apps.slideshow.Main '' '' %{classpath} slideshow true

# Demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/
cp -pr samples $RPM_BUILD_ROOT%{_datadir}/%{name}/


%files -f .mfiles
%license LICENSE NOTICE
%doc CHANGES MAINTAIN README

%files css -f .mfiles-css
%files util -f .mfiles-util

%files squiggle -f .mfiles-squiggle
%{_bindir}/squiggle

%files svgpp -f .mfiles-svgpp
%{_bindir}/svgpp

%files ttf2svg -f .mfiles-ttf2svg
%{_bindir}/ttf2svg

%files rasterizer -f .mfiles-rasterizer
%{_bindir}/rasterizer

%files slideshow -f .mfiles-slideshow
%{_bindir}/slideshow

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%files demo
%{_datadir}/%{name}


%changelog
%autochangelog
