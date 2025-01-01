%bcond_with bootstrap

Name:           plexus-xml
Version:        3.0.1
Release:        %autorelease
Summary:        Plexus XML Utilities
# Licensing breakdown:
# Apache-1.1: src/main/java/org/codehaus/plexus/util/xml/StringUtils.java
# xpp: src/main/java/org/codehaus/plexus/util/xml/pull/MXParser.java
# Everything else is Apache-2.0
License:        Apache-1.1 AND Apache-2.0 AND xpp
URL:            https://codehaus-plexus.github.io/plexus-xml/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
%endif

%description
A collection of various utility classes to ease working with XML.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup -p1 -C

%build
# Test dependencies are not packaged
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license NOTICE.txt LICENSE.txt

%files javadoc -f .mfiles-javadoc

%changelog
%autochangelog
