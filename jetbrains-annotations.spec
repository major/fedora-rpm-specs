Name:           jetbrains-annotations
Version:        24.0.1
Release:        %autorelease
Summary:        Annotations for JVM-based languages

License:        Apache-2.0
URL:            https://www.jetbrains.org/
Source0:        https://github.com/JetBrains/java-annotations/archive/%{version}/java-annotations-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/jetbrains/annotations/%{version}/annotations-%{version}.pom

BuildArch:      noarch
ExclusiveArch:  noarch %{java_arches}

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)

%description
This package contains a set of Java annotations which can be used in
JVM-based languages.  They serve as additional documentation and can be
interpreted by IDEs and static analysis tools to improve code analysis.

%javadoc_package

%prep
%autosetup -n java-annotations-%{version}
cp -p %{SOURCE1} pom.xml

%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin:3.10.1 . '<configuration><source>1.8</source><target>1.8</target></configuration>'

%mvn_file org.jetbrains:annotations %{name}
%mvn_alias org.jetbrains:annotations com.intellij:

# Assemble the sources to build
cp -a common/src src
cp -p java8/src/main/java/org/jetbrains/annotations/*.java \
      src/main/java/org/jetbrains/annotations

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%changelog
%autochangelog
