Name:           fishbowl
Version:        1.4.1
Release:        11%{?dist}
Summary:        A collection of helper methods for dealing with exceptions in Java 8
License:        MIT
URL:            https://stefanbirkner.github.io/fishbowl
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/stefanbirkner/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.testng:testng)

%description
Fishbowl provides helper methods for dealing with exceptions.

%{?javadoc_package}

%prep
%autosetup -n %{name}-%{name}-%{version}

find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

%pom_remove_parent

# add groupId as consequences of removing parent
# see: http://maven.apache.org/guides/introduction/introduction-to-the-pom.html#the-solution
%pom_xpath_inject pom:project '<groupId>com.github.stefanbirkner</groupId>'

# remove test deps not available in repo
%pom_remove_dep com.google.truth:truth
%pom_remove_dep de.bechte.junit:junit-hierarchicalcontextrunner
%pom_remove_dep org.easytesting:fest-assert

# remove junit-hierarchicalcontextrunner annotations as consequences of removing deps
find -name '*.java' | xargs sed -ri 's/^import .*\.HierarchicalContextRunner;//;s/@.*\(HierarchicalContextRunner.*\)//g'

# remove tests since truth and fest-assert is unavailable
rm ./src/test/java8/com/github/stefanbirkner/fishbowl/FishbowlJUnitReadmeTest.java
rm ./src/test/java8/com/github/stefanbirkner/fishbowl/FishbowlTestNgReadmeTest.java

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.4.1-9
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.4.1-3
- Rebuilt for Drop i686 JDKs

* Fri Oct 22 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.4.1-2
- Add BRs: mockito, testng, assertj
- Fix TestSuite

* Fri Sep 17 2021 Didik Supriadi <didiksupriadi41@gmail.com> - 1.4.1-1
- Initial package
