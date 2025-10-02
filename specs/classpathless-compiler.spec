%global cli_tool cplc

Name:           classpathless-compiler
Version:        2.4
Release:        %autorelease
Summary:        Tool for recompiling java sources with customizable class providers
License:        Apache-2.0
URL:            https://github.com/mkoncek/classpathless-compiler
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  jurand
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.ow2.asm:asm-tree)

Requires:       beust-jcommander
Requires:       javapackages-tools

# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.3-5

%description
Classpathless compiler (CPLC) is a compiler wrapper used for compiling java
sources with customizable class providers. This tool works differently from the
traditional java compiler in that it doesn't use provided classpath but instead
pulls dependencies using an API.

%prep
%setup -q -n classpathless-compiler-%{version}

%java_remove_annotations -s -n SuppressFBWarnings .

%pom_remove_dep :spotbugs-annotations

%pom_remove_plugin :maven-assembly-plugin impl
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin

%build
%mvn_build -j

%install
%mvn_install

%jpackage_script io.github.mkoncek.classpathless.Tool "" "" classpathless-compiler/classpathless-compiler:classpathless-compiler/classpathless-compiler-api:classpathless-compiler/classpathless-compiler-util:beust-jcommander %{cli_tool}

%files -f .mfiles
%{_bindir}/%{cli_tool}

%license LICENSE
%doc README.md

%changelog
%autochangelog
