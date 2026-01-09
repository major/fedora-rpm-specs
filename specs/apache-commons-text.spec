%global jarname commons-text

Name:           apache-%{jarname}
Version:        1.15.0
Release:        1%{?dist}
Summary:        Apache Commons Text is a library focused on algorithms working on strings
License:        Apache-2.0
URL:            https://commons.apache.org/proper/%{jarname}
BuildArch:      noarch

Source0:        https://archive.apache.org/dist/commons/text/source/%{jarname}-%{version}-src.tar.gz
Source1:        https://archive.apache.org/dist/commons/text/source/%{jarname}-%{version}-src.tar.gz.asc
Source2:        https://archive.apache.org/dist/commons/KEYS
# disable url lookup in test
#Patch0:         0001-disable-url-lookup.patch

BuildRequires:  gnupg2
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.mockito:mockito-core)

%description
The Commons Text library provides additions to the standard JDK's text handling.
Our goal is to provide a consistent set of tools for processing text generally
from computing distances between Strings to being able to efficiently do String
escaping of various types.

%{?javadoc_package}

%prep
# verify signed sources
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

# -p1: strip one level directory in patch(es)
# -n: base directory name
%autosetup -p1 -n %{jarname}-%{version}-src

# delete precompiled jar and class files
find -type f '(' -name '*.jar' -o -name '*.class' ')' -print -delete

# mockito-inline was merged into mockito-core
%pom_change_dep :mockito-inline :mockito-core

%build
# disable test: some test deps can't be installed
%mvn_build -f -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc README.md RELEASE-NOTES.txt

%changelog
%autochangelog
