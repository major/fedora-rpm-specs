Name:           apache-logging-parent
Summary:        Parent pom for Apache Logging Services projects
Version:        9
Release:        1%{?dist}
License:        Apache-2.0

URL:            https://logging.apache.org/
Source0:        https://repo1.maven.org/maven2/org/apache/logging/logging-parent/%{version}/logging-parent-%{version}-source-release.zip
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache:apache:pom:)

# jboss-logging packages now use this parent rather than jboss-parent
Obsoletes: jboss-parent = 20

%description
Parent pom for Apache Logging Services projects.


%prep
%setup -q -n logging-parent-logging-parent-%{version}
cp -p %SOURCE1 LICENSE

%pom_remove_plugin com.diffplug.spotless:spotless-maven-plugin

%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%license LICENSE


%changelog
* Tue Jun 13 2023 Chris Kelley <ckelley@redhat.com> - 9-1
- Unretire package; update to version 9.

* Mon Jul 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2-1
- Update to version 2.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 29 2017 Michael Simacek <msimacek@redhat.com> - 1-1
- Initial packaging

