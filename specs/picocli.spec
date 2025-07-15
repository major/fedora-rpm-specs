%bcond_with bootstrap

%if %{without bootstrap} && %{undefined rhel}
%bcond_without picocli_shell
%else
%bcond_with picocli_shell
%endif

Name:           picocli
Version:        4.7.6
Release:        %autorelease
Summary:        Java command line parser with both an annotations API and a programmatic API
License:        Apache-2.0
URL:            https://github.com/remkop/picocli
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/info/picocli/%{name}/%{version}/%{name}-%{version}.pom
Source2:        https://repo1.maven.org/maven2/info/picocli/%{name}-codegen/%{version}/%{name}-codegen-%{version}.pom
Source3:        https://repo1.maven.org/maven2/info/picocli/%{name}-shell-jline2/%{version}/%{name}-shell-jline2-%{version}.pom
Source4:        https://repo1.maven.org/maven2/info/picocli/%{name}-shell-jline3/%{version}/%{name}-shell-jline3-%{version}.pom

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%endif
%if %{with picocli_shell}
BuildRequires:  mvn(jline:jline)
BuildRequires:  mvn(org.jline:jline-console)
BuildRequires:  mvn(org.jline:jline-reader)
BuildRequires:  mvn(org.jline:jline-terminal)
%endif

%description
Picocli is a modern library and framework, written in Java, that contains both
an annotations API and a programmatic API. It features usage help with ANSI
colors and styles, TAB auto-completion and nested sub-commands. In a single
file, so you can include it in source form. This lets users run picocli-based
applications without requiring picocli as an external dependency.

%package -n %{name}-codegen
Summary:        Tools to generate documentation, configuration, source code from a picocli model

%description -n %{name}-codegen
The picocli-codegen (Picocli Code Generation) module contains tools for
generating configuration files and documentation for picocli-based applications.

This module also includes an annotation processor that can build a model from
the picocli annotations at compile time rather than at runtime.

The annotation processor allows many of the tools to be invoked automatically as
part of the build without configuration. If a tool does not have an annotation
processor wrapper (yet), it can be invoked on the command line, and can be
scripted to be invoked automatically as part of building your project.

%if %{with picocli_shell}

%package -n %{name}-shell-jline2
Summary:        Easily build interactive shell applications with JLine 2 and picocli

%description -n %{name}-shell-jline2
Picocli Shell JLine2 contains components and documentation for building
interactive shell command line applications with JLine 2 and picocli.

JLine and picocli complement each other very well and have little or none
functional overlap.

JLine provides interactive shell functionality but has no built-in command line
parsing functionality. What it does provide is a tokenizer for splitting a
single command line String into an array of command line argument Strings.

Given an array of Strings, picocli can execute a command or subcommand.
Combining these two libraries makes it easy to build powerful interactive shell
applications.

%package -n %{name}-shell-jline3
Summary:        Easily build interactive shell applications with JLine 3 and picocli

%description -n %{name}-shell-jline3
Picocli Shell JLine3 contains components and documentation for building
interactive shell command line applications with JLine 3 and picocli.

JLine and picocli complement each other very well and have little or none
functional overlap.

JLine provides interactive shell functionality but has no built-in command line
parsing functionality. What it does provide is a tokenizer for splitting a
single command line String into an array of command line argument Strings.

Given an array of Strings, picocli can execute a command or subcommand.
Combining these two libraries makes it easy to build powerful interactive shell
applications.

%endif

%prep
%autosetup -p1 -C
# note:
# picocli is a gradle project, we need to transform it to maven.
# here, we create a parent pom according to maven project aggregation. (see 
# https://maven.apache.org/guides/introduction/introduction-to-the-pom.html#project-aggregation)

find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

# create directory for picocli
mkdir %{name}

# move picocli source code
mv src/ %{name}

cp -p %{SOURCE1} %{name}/pom.xml

cp -p %{SOURCE2} %{name}-codegen/pom.xml

cp -p %{SOURCE3} %{name}-shell-jline2/pom.xml

cp -p %{SOURCE4} %{name}-shell-jline3/pom.xml

# create parent from the simplest pom
cp -p %{SOURCE1} pom.xml

# set parent artifact id
%pom_xpath_set pom:artifactId %{name}-parent

# set parent name (optional: useful for debugging)
%pom_xpath_set pom:name %{name}-parent

# set parent packaging
%pom_xpath_inject pom:project '<packaging>pom</packaging>'

# add modules
%pom_xpath_inject pom:project '
  <modules>
    <module>%{name}</module>
    <module>%{name}-codegen</module>
%if %{with picocli_shell}
    <module>%{name}-shell-jline2</module>
    <module>%{name}-shell-jline3</module>
%endif
  </modules>'

# picocli: set the name to picocli
%pom_xpath_set pom:name %{name} %{name}

# picocli-shell-jline3: fedora has a split jline3, so split up the dependency
%pom_remove_dep org.jline:jline %{name}-shell-jline3
%pom_add_dep org.jline:jline-console %{name}-shell-jline3
%pom_add_dep org.jline:jline-reader %{name}-shell-jline3
%pom_add_dep org.jline:jline-terminal %{name}-shell-jline3

%pom_add_plugin org.codehaus.mojo:build-helper-maven-plugin:3.2.0 %{name} '
  <executions>
    <execution>
      <id>add-source</id>
      <phase>generate-sources</phase>
      <goals>
        <goal>add-source</goal>
      </goals>
      <configuration>
        <sources>
          <source>src/main/java9</source>
        </sources>
      </configuration>
    </execution>
  </executions>'

# set up compiler plugin
%pom_add_plugin :maven-compiler-plugin:3.8.1 %{name} '
  <configuration>
      <release>9</release>
  </configuration>
  <executions>
      <execution>
          <id>base-compile</id>
          <goals>
              <goal>compile</goal>
          </goals>
          <configuration>
              <release>8</release>
              <excludes>
                  <exclude>module-info.java</exclude>
              </excludes>
          </configuration>
      </execution>
  </executions>'

# picocli-codegen: don't perform annotation processing
%pom_add_plugin :maven-compiler-plugin:3.8.1 %{name}-codegen '
  <configuration>
    <proc>none</proc>
  </configuration>'

# set up jar plugin
%pom_add_plugin :maven-jar-plugin:3.2.0 %{name} '
  <configuration>
    <archive>
      <manifestEntries>
        <Specification-Title>picocli</Specification-Title>
        <Specification-Version>${project.version}</Specification-Version>
        <Specification-Vendor>Remko Popma</Specification-Vendor>
        <Implementation-Title>picocli</Implementation-Title>
        <Implementation-Version>${project.version}</Implementation-Version>
        <Implementation-Vendor>Remko Popma</Implementation-Vendor>
        <Main-Class>picocli.AutoComplete</Main-Class>
        <Multi-Release>true</Multi-Release>
      </manifestEntries>
    </archive>
  </configuration>'

%pom_add_plugin :maven-jar-plugin:3.2.0 %{name}-codegen '
  <configuration>
    <archive>
      <manifestEntries>
        <Specification-Title>Picocli Code Generation</Specification-Title>
        <Specification-Version>${project.version}</Specification-Version>
        <Specification-Vendor>Remko Popma</Specification-Vendor>
        <Implementation-Title>Picocli Code Generation</Implementation-Title>
        <Implementation-Version>${project.version}</Implementation-Version>
        <Implementation-Vendor>Remko Popma</Implementation-Vendor>
        <Automatic-Module-Name>info.picocli.codegen</Automatic-Module-Name>
      </manifestEntries>
    </archive>
  </configuration>'

%pom_add_plugin :maven-jar-plugin:3.2.0 %{name}-shell-jline2 '
  <configuration>
    <archive>
      <manifestEntries>
        <Specification-Title>Picocli Shell JLine2</Specification-Title>
        <Specification-Version>${project.version}</Specification-Version>
        <Specification-Vendor>Remko Popma</Specification-Vendor>
        <Implementation-Title>Picocli Shell JLine2</Implementation-Title>
        <Implementation-Version>${project.version}</Implementation-Version>
        <Implementation-Vendor>Remko Popma</Implementation-Vendor>
        <Automatic-Module-Name>info.picocli.shell.jline2</Automatic-Module-Name>
      </manifestEntries>
    </archive>
  </configuration>'

%pom_add_plugin :maven-jar-plugin:3.2.0 %{name}-shell-jline3 '
  <configuration>
    <archive>
      <manifestEntries>
        <Specification-Title>Picocli Shell JLine3</Specification-Title>
        <Specification-Version>${project.version}</Specification-Version>
        <Specification-Vendor>Remko Popma</Specification-Vendor>
        <Implementation-Title>Picocli Shell JLine3</Implementation-Title>
        <Implementation-Version>${project.version}</Implementation-Version>
        <Implementation-Vendor>Remko Popma</Implementation-Vendor>
        <Automatic-Module-Name>info.picocli.shell.jline3</Automatic-Module-Name>
      </manifestEntries>
    </archive>
  </configuration>'

# don't install parent pom and tests module
%mvn_package :%{name}-parent __noinstall

%build
%mvn_build -s -f -j

%install
%mvn_install

%files -n %{name} -f .mfiles-%{name}
%license LICENSE
%doc README.md RELEASE-NOTES.md

%files -n %{name}-codegen -f .mfiles-%{name}-codegen
%license LICENSE
%doc %{name}-codegen/README.adoc

%if %{with picocli_shell}

%files -n %{name}-shell-jline2 -f .mfiles-%{name}-shell-jline2
%license LICENSE
%doc %{name}-shell-jline2/README.md

%files -n %{name}-shell-jline3 -f .mfiles-%{name}-shell-jline3
%license LICENSE
%doc %{name}-shell-jline3/README.md

%endif

%changelog
%autochangelog
