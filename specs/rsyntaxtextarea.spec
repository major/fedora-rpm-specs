%global upname RSyntaxTextArea

Name:           rsyntaxtextarea
Version:        3.6.0
Release:        1%{?dist}
Summary:        A syntax highlighting, code folding text editor for Java Swing applications

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/bobbylight/%{upname}
Source0:        https://github.com/bobbylight/%{upname}/archive/%{version}.tar.gz
Source1:        pom.xml.in

BuildRequires:  java-25-devel
BuildRequires:  maven-local-openjdk25

# Apply workaround until gradle doesn't exists in repos
Provides:       mvn(com.fifesoft:rsyntaxtextarea)
Provides:       osgi(com.fifesoft.rsyntaxtextarea)

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
%{upname} is a customizable, syntax highlighting text component for Java
Swing applications. Out of the box, it supports syntax highlighting for 40+
programming languages, code folding, search and replace, and has add-on
libraries for code completion and spell checking. Syntax highlighting for
additional languages can be added via tools such as JFlex.

%package        javadoc
Summary:        Javadoc for %{upname}

%description    javadoc
This package contains the API documentation for %{name}.


%prep
%autosetup -n %{upname}-%{version} -p1

# Drop included jars
find . -name "*.jar" -delete

%build
d=`mktemp -d`
f=`find %{upname}/src/main/java -type f | grep \.java$`
javac --source 8 --target 8 -d $d $f
cp -rv %{upname}/src/main/resources/* $d
l=`pwd`
pushd $d
jar -cf $l/%{name}.jar *
popd
cat  %{SOURCE1} | sed "s/VERSION/%{version}/g" > pom.xml
%mvn_artifact pom.xml %{name}.jar

%install
%mvn_install




%files -f .mfiles
%license LICENSE.md
%doc README.md
%{_datadir}/java/%{name}/%{name}.jar



%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

%autochangelog
