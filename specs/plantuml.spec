Name:           plantuml
Version:        1.2025.3
Release:        %autorelease
Epoch:          1
Summary:        Program to generate UML diagram from a text description

License:        LGPL-3.0-or-later
URL:            http://plantuml.com/
Source:         https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/plantuml/plantuml/pull/2239
# https://github.com/plantuml/plantuml/pull/2241
Source1:        https://raw.githubusercontent.com/plantuml/plantuml/refs/heads/master/build.xml

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  ant
BuildRequires:  help2man
BuildRequires:  javapackages-local

Requires:       java
# Explicit requires for javapackages-tools since plantuml script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Requires:       graphviz

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

%prep
%autosetup
cp %{SOURCE1} build.xml


%build
# Encoding needs to be set to UTF-8 for epel builds
%if 0%{?rhel}
export ANT_OPTS=-Dfile.encoding=UTF-8
%endif
ant


%install
# Set jar location
%mvn_file net.sourceforge.%{name}:%{name} %{name}
# Configure maven depmap
%mvn_artifact net.sourceforge.%{name}:%{name}:%{version} %{name}.jar
%mvn_install

%jpackage_script net.sourceforge.plantuml.Run "" "" plantuml plantuml true

# Build man page
install -d "%{buildroot}%{_mandir}/man1"
help2man --help-option='-h' --version-option='--version' --no-info --output='%{buildroot}%{_mandir}/man1/plantuml.1' "java -jar plantuml.jar"

%files -f .mfiles
%{_bindir}/plantuml
%doc README.md
%{_mandir}/man1/plantuml.1*
%license COPYING plantuml-lgpl/lgpl-license.txt

%changelog
%autochangelog
