Name:           dirgra
Version:        0.4
Release:        %autorelease
Summary:        Simple Directed Graph
License:        EPL-1.0
URL:            https://github.com/jruby/%{name}
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local

%description
Simple Directed Graph Implementation.

%{?javadoc_package}

%prep
%autosetup -n %{name}-%{name}-%{version}

find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

%pom_remove_parent

%pom_xpath_remove pom:extensions

%pom_remove_plugin :maven-source-plugin

%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%changelog
%autochangelog
