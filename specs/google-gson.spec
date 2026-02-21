%bcond_with bootstrap

Name:           google-gson
Version:        2.12.1
Release:        %autorelease
Summary:        Java lib for conversion of Java objects into JSON representation
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/google/gson
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/google/gson/archive/gson-parent-%{version}.tar.gz

BuildRequires:  jurand
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(javax.annotation:jsr250-api)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.12.1-3

%description
Gson is a Java library that can be used to convert a Java object into its
JSON representation. It can also be used to convert a JSON string into an
equivalent Java object. Gson can work with arbitrary Java objects including
pre-existing objects that you do not have source-code of.

%prep
%autosetup -p1 -C

%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :spotless-maven-plugin
%pom_remove_plugin -r :maven-artifact-plugin
%pom_remove_plugin -r :maven-failsafe-plugin
%pom_remove_plugin :bnd-maven-plugin gson
%pom_remove_plugin :maven-jar-plugin gson
%pom_remove_plugin :maven-compiler-plugin

%pom_remove_dep -r :error_prone_annotations
jurand -i -s -a gson extras -p com[.]google[.]errorprone[.]annotations[.]

# The test EnumWithObfuscatedTest requires the plugins copy-rename-maven-plugin, proguard-maven-plugin and maven-resources-plugin to work correctly because it tests Gson interaction with a class obfuscated by ProGuard.
# https://github.com/google/gson/issues/2045
rm ./gson/src/test/java/com/google/gson/functional/EnumWithObfuscatedTest.java

# to check later
rm ./gson/src/test/java/com/google/gson/internal/bind/DefaultDateTypeAdapterTest.java
# remove unnecessary dependency on parent POM
# POM doesn't specify parent.
#%%pom_remove_parent

%pom_remove_plugin :copy-rename-maven-plugin gson
%pom_remove_plugin :proguard-maven-plugin gson

%pom_remove_plugin  :moditect-maven-plugin gson

# Remove dependency on unavailable templating-maven-plugin
%pom_remove_plugin  org.codehaus.mojo:templating-maven-plugin gson
sed 's/${project.version}/%{version}/' gson/src/main/java-templates/com/google/gson/internal/GsonBuildConfig.java >gson/src/main/java/com/google/gson/internal/GsonBuildConfig.java

#depends on com.google.caliper
%pom_disable_module metrics

#depends on com.google.protobuf:protobuf-java:jar:4.0.0-rc-2 and com.google.truth:truth:jar:1.1.3
%pom_disable_module proto

%pom_disable_module test-jpms
%pom_disable_module test-graal-native-image
%pom_disable_module test-shrinker

%build
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md CHANGELOG.md UserGuide.md

%changelog
%autochangelog
