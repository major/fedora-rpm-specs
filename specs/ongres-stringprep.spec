Name:           ongres-stringprep
Version:        2.2
Release:        %autorelease
Summary:        RFC 3454 Preparation of Internationalized Strings in pure Java
License:        BSD-2-Clause
URL:            https://github.com/ongres/stringprep
Source0:        https://github.com/ongres/stringprep/archive/%{version}/stringprep-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)

# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.2-3

%description
The stringprep protocol does not stand on its own; it has to be used by other
protocols at precisely-defined places in those other protocols.

%prep
%autosetup -p1 -n "stringprep-%{version}"
find \( -name '*.jar' -o -name '*.class' \) -delete

%pom_remove_dep org.junit:junit-bom parent

%pom_remove_plugin -r :maven-javadoc-plugin

# codegenerator is only needed at build time, and has extra dependencies
%mvn_package com.ongres.stringprep:codegenerator __noinstall

# codegen is only needed for specific build profile that we do not use
rm -r codegen

%pom_xpath_inject 'pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:configuration/pom:archive' '
<manifestEntries>
  <Multi-Release>true</Multi-Release>
</manifestEntries>
' parent

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%changelog
%autochangelog
