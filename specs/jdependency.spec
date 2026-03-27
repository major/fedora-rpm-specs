Name:           jdependency
Version:        2.15
Release:        %autorelease
Summary:        Class dependency analysis library for Java
License:        Apache-2.0
URL:            https://github.com/tcurdt/%{name}
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/tcurdt/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-analysis)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.ow2.asm:asm-tree)
BuildRequires:  mvn(org.ow2.asm:asm-util)

# TODO Remove in Fedora 47
Obsoletes:      %{name}-javadoc < 2.12-5

%description
Jdependency is a small library that helps you analyze class level
dependencies, clashes and missing classes.

%prep
%autosetup -p1 -C

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin org.jacoco:jacoco-maven-plugin
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin

%mvn_file : %{name}

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%changelog
%autochangelog
