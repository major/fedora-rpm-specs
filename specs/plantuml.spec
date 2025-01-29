Name:           plantuml
Version:        1.2025.0
Release:        %autorelease
Epoch:          1
Summary:        Program to generate UML diagram from a text description

License:        LGPL-3.0-or-later
URL:            http://plantuml.com/
Source:         https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  ant
BuildRequires:  help2man
BuildRequires:  javapackages-local

Requires:       java >= 1.8.0
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
# Don't set Class-Path when building jar
sed --in-place '/<attribute name="Class-Path"/d' build.xml


%build
# Encoding needs to be set to UTF-8 for epel builds
%if 0%{?rhel}
export ANT_OPTS=-Dfile.encoding=UTF-8
%endif
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

# Build man page
install -d "%{buildroot}%{_mandir}/man1"
help2man --help-option='-h' --version-option='--version' --no-info --output='%{buildroot}%{_mandir}/man1/plantuml.1' "java -jar plantuml.jar"

%files -f .mfiles
%{_bindir}/plantuml
%doc README.md
%{_mandir}/man1/plantuml.1*
%license COPYING plantuml-lgpl/lgpl-license.txt

%files javadoc -f .mfiles-javadoc
%doc README.md
%license COPYING plantuml-lgpl/lgpl-license.txt

%changelog
%autochangelog
