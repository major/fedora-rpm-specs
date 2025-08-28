Name:           javassist
Version:        3.30.2
Release:        %autorelease
Summary:        Java Programming Assistant for Java bytecode manipulation
License:        MPL-1.1 OR LGPL-2.1-or-later OR Apache-2.0

%global upstream_version rel_%(sed s/\\\\./_/g <<<"%{version}")_ga

URL:            https://www.javassist.org/
Source0:        https://github.com/jboss-%{name}/%{name}/archive/refs/tags/%{upstream_version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk21
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-all)

# TODO Remove in Fedora 47
Obsoletes:      %{name}-javadoc < 3.30.2-10

%description
Javassist enables Java programs to define a new class at runtime and to
modify a class file when the JVM loads it. Unlike other similar
bytecode editors, Javassist provides two levels of API: source level
and bytecode level. If the users use the source-level API, they can
edit a class file without knowledge of the specifications of the Java
bytecode. The whole API is designed with only the vocabulary of the
Java language. You can even specify inserted bytecode in the form of
source text; Javassist compiles it on the fly. On the other hand, the
bytecode-level API allows the users to directly edit a class file as
other editors.

%prep
%autosetup -p1 -C

# remove unnecessary maven plugins
%pom_remove_plugin :maven-source-plugin

# disable profiles that only add com.sun:tools dependency
%pom_xpath_remove "pom:profiles"

# add compatibility alias for old maven artifact coordinates
%mvn_alias : %{name}:%{name}

# add compatibility symlink for old classpath
%mvn_file : %{name}

%build
%mvn_build -j

# remove bundled jar and class files *after* they were used for running tests
rm javassist.jar src/test/resources/*.jar
find src/test -name "*.class" -print -delete

%install
%mvn_install

%files -f .mfiles
%license License.html
%doc README.md

%autochangelog
