%global jarname commons-text

Name:           apache-%{jarname}
Version:        1.9
Release:        5%{?dist}
Summary:        Apache Commons Text is a library focused on algorithms working on strings
License:        Apache-2.0
URL:            https://commons.apache.org/proper/%{jarname}
BuildArch:      noarch

Source0:        https://archive.apache.org/dist/commons/text/source/%{jarname}-%{version}-src.tar.gz
Source1:        https://archive.apache.org/dist/commons/text/source/%{jarname}-%{version}-src.tar.gz.asc
Source2:        https://archive.apache.org/dist/commons/KEYS
# disable url lookup in test
Patch0:         0001-disable-url-lookup.patch

BuildRequires:  gnupg2
BuildRequires:  maven-local-openjdk11
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.mockito:mockito-inline)

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

%build
%mvn_build -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc README.md RELEASE-NOTES.txt

%changelog
* Sat Apr 29 2023 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.9-5
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 23 2022 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.9-2
- Add BR on mockito-inline
- Patch the test files to disable url lookup
- Use maven-local-openjdk11 to be able to compile test files
- Reverse the order of %%autosetup and %%gpgverify

* Wed Jul 21 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.9-1
- Initial package
