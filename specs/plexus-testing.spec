%bcond_with bootstrap

Name:           plexus-testing
Version:        1.3.0
Release:        %autorelease
Summary:        Plexus Testing
License:        Apache-2.0
URL:            https://github.com/codehaus-plexus/plexus-testing
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
%endif

%description
The Plexus Testing contains the necessary classes to be able to test
Plexus components.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup -p1 -C

# Some tests rely on Jakarta Injection API, which is not packaged
rm src/test/java/org/codehaus/plexus/testing/TestJakartaComponent.java
rm src/test/java/org/codehaus/plexus/testing/PlexusTestJakartaTest.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
%autochangelog
