Name:           plantuml
Version:        1.2023.13
Release:        %autorelease
Epoch:          1
Summary:        Program to generate UML diagram from a text description

License:        LGPL-3.0-or-later
URL:            http://plantuml.com/
Source:         https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz
# Manually add build.xml as it is not included in the latest version
# https://github.com/plantuml/plantuml/issues/1542
Source1:        build.xml

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  ant
Requires:       java >= 1.8.0
BuildRequires:  javapackages-local
# Explicit requires for javapackages-tools since plantuml script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

%description
PlantUML is a program allowing to draw UML diagrams, using a simple
and human readable text description. It is extremely useful for code
documenting, sketching project architecture during team conversations
and so on.

PlantUML supports the following diagram types
  - sequence diagram
  - use case diagram
  - class diagram
  - activity diagram
  - component diagram
  - state diagram

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup
mv %{SOURCE1} .


%build
ant

# build javadoc
export CLASSPATH=$(build-classpath ant):plantuml.jar
%javadoc -source 1.8 -encoding UTF-8 -Xdoclint:none -d javadoc $(find src -name "*.java") -windowtitle "PlantUML %{version}"

%install
# Set jar location
%mvn_file net.sourceforge.%{name}:%{name} %{name}
# Configure maven depmap
%mvn_artifact net.sourceforge.%{name}:%{name}:%{version} %{name}.jar
%mvn_install -J javadoc

%jpackage_script net.sourceforge.plantuml.Run "" "" plantuml plantuml true

%files -f .mfiles
%{_bindir}/plantuml
%doc README.md
%license COPYING plantuml-lgpl/lgpl-license.txt

%files javadoc -f .mfiles-javadoc
%doc README.md
%license COPYING plantuml-lgpl/lgpl-license.txt

%changelog
%autochangelog
