%bcond_with protobuf
%global vertag release_%(echo %version | tr . _)

Name:           truth
Version:        1.0.1
Release:        6%{?dist}
Summary:        An assertion framework for Java unit tests
License:        ASL 2.0
URL:            https://github.com/google/truth
Source0:        https://github.com/google/truth/archive/%{vertag}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
# Test failure with openjdk17
BuildRequires:  maven-openjdk11
BuildRequires:  mvn(com.google.auto.value:auto-value)
BuildRequires:  mvn(com.google.auto.value:auto-value-annotations)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
# A number of annotation and testing deps are missing and are removed below
#BuildRequires:  mvn(com.google.errorprone:error_prone_annotations)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(com.google.guava:guava-testlib)
%if %{with protobuf}
BuildRequires:  mvn(com.google.protobuf:protobuf-java)
BuildRequires:  mvn(com.google.protobuf:protobuf-javalite)
%endif
#BuildRequires:  mvn(com.google.testing.compile:compile-testing)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(io.github.java-diff-utils:java-diff-utils)
#BuildRequires:  mvn(org.checkerframework:checker-qual)

%description
Truth is a library provides alternative ways to express assertions in
unit tests. It can be used as a replacement for JUnit's assertions or FEST
or it can be used alongside where other approaches seem more suitable.

%{?javadoc_package}

%prep
%setup -q -n %{name}-%{vertag}

# Remove items with unpackaged dependencies
%pom_remove_parent
%pom_disable_module re2j extensions
%if %{without protobuf}
%pom_disable_module liteproto extensions
%pom_disable_module proto extensions
%endif
%pom_remove_plugin :gwt-maven-plugin core
%pom_remove_dep -r :compile-testing
%pom_remove_dep -r :error_prone_annotations
%pom_remove_dep :gwt-user core
%pom_remove_dep :guava-gwt core
%pom_remove_dep -r org.checkerframework:
%pom_remove_plugin -r :protobuf-maven-plugin
%pom_change_dep :protobuf-lite :protobuf-javalite extensions/liteproto/pom.xml
# Fails with missing class TestMessageLite2
rm extensions/liteproto/src/test/java/com/google/common/truth/extensions/proto/LiteProtoSubjectTest.java
# Fails with missing class TestMessage2
rm extensions/proto/src/test/java/com/google/common/truth/extensions/proto/OverloadResolutionTest.java

# Remove kr.motd.maven:os-maven-plugin extension
%pom_xpath_remove "pom:build/pom:extensions" extensions/liteproto/pom.xml extensions/proto/pom.xml

# Needed to fix javadoc build
%pom_add_dep javax.annotation:javax.annotation-api extensions/proto

# Exclude tests with missing dependencies
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:testExcludes" "
            <testExclude>**/gwt/*.java</testExclude>
            <testExclude>**/ComparableSubjectCompileTest.java</testExclude>" core

# Bump to Java 8 to fix this:
# [ERROR] /home/orion/fedora/truth/truth-release_0_42/core/src/test/java/com/google/common/truth/TruthAssertThatTest.java:[54,40] error: <anonymous com.google.common.truth.TruthAssertThatTest$2> is not abstract and does not override abstract method test(Method) in Predicate
sed -i 's/1\.7/1.8/' pom.xml

# Fix difflib
%pom_change_dep com.googlecode.java-diff-utils:diffutils io.github.java-diff-utils:java-diff-utils . core
find -name '*.java' -exec sed -i -e '/^import/s/ difflib\.Patch/ com.github.difflib.patch.Patch/' \
    -e '/^import/s/ difflib\.DiffUtils\.generateUnifiedDiff;/ com.github.difflib.UnifiedDiffUtils.generateUnifiedDiff;/' \
    -e '/^import/s/ difflib\./ com.github.difflib./'  {} +

# truth uses quite a few annotation libraries for code quality, which
# we don't have. This ugly regex is supposed to remove their usage from the code
annotations=$(
    find -name '*.java' \
    | xargs grep -h \
        -e '^import com\.google\.j2objc\.annotations' \
        -e '^import com\.google\.errorprone\.annotation' \
        -e '^import com\.google\.errorprone\.annotations' \
        -e '^import com\.google\.common\.annotations' \
        -e '^import static jsinterop\.annotations' \
        -e '^import jsinterop\.annotations' \
        -e '^import org\.codehaus\.mojo\.animal_sniffer' \
        -e '^import org\.checkerframework' \
    | sort -u \
    | sed 's/.*\.\([^.]*\);/\1/' \
    | paste -sd\|
)
find -name '*.java' | xargs sed -ri \
    "s/^import .*\.($annotations);//;s/@($annotations)"'\>\s*(\((("[^"]*")|([^)]*))\))?//g'

%build
%mvn_build -- -DfailIfNoTests=false -Dtest='!SubjectTest*,!com.google.common.truth.ExpectFailureNonRuleTest$ExpectFailureThrowAfterSubject*,!com.google.common.truth.ExpectFailureNonRuleTest$ExpectFailureThrowIn*'

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Orion Poplawski <orion@nwra.com> - 1.0.1-4
- Add BR on auto-value-annotations and re-enable dep (FTBFS bz#2105384)
- Build with OpenJDK 11 due to test failure with 17

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.1-3
- Rebuilt for Drop i686 JDKs

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 30 2021 Orion Poplawski <orion@nwra.com> - 1.0.1-1
- Update to 1.0.1

* Sat Oct 30 2021 Orion Poplawski <orion@nwra.com> - 0.46-1
- Update to 0.46

* Fri Oct 29 2021 Orion Poplawski <orion@nwra.com> - 0.44-1
- Update to 0.44

* Wed Oct 27 2021 Orion Poplawski <orion@nwra.com> - 0.42-2
- Simplify spec from review
- Disable protobuf extensions

* Thu Oct 14 2021 Orion Poplawski <orion@nwra.com> - 0.42-1
- Update to 0.42

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.23-4
- Regenerate build-requires

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 3 2015 Noa Resare <noa@resare.com> - 0.23-1
- Initial packaging
