Name:           jakarta-activation1
Version:        1.2.2
Release:        9%{?dist}
Summary:        Jakarta Activation Specification and Implementation
License:        BSD
URL:            https://jakartaee.github.io/jaf-api/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/eclipse-ee4j/jaf/archive/%{version}/jaf-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
Jakarta Activation lets you take advantage of standard services to:
determine the type of an arbitrary piece of data; encapsulate access to
it; discover the operations available on it; and instantiate the
appropriate bean to perform the operation(s).

%prep
%setup -q -n jaf-api-%{version}

%pom_remove_parent
%pom_disable_module demo

%pom_remove_plugin -r :maven-enforcer-plugin

%pom_remove_plugin :directory-maven-plugin
sed -i 's/${main.basedir}/${basedir}/' pom.xml

# Remove custom doclet configuration
%pom_remove_plugin :maven-javadoc-plugin activation

# Set bundle version manually instead of with osgiversion-maven-plugin
# (the plugin is only used to strip off -SNAPSHOT or -Mx qualifiers)
%pom_remove_plugin :osgiversion-maven-plugin
sed -i "s/\${activation.osgiversion}/%{version}/g" activation/pom.xml

%mvn_compat_version jakarta*: 1 %{version} 1.2.1 1.2.0 1.1.1

# TODO delete
%mvn_file com.sun.activation:jakarta.activation %{name}/jakarta.activation javax.activation

%build
# Javadoc fails:
# /builddir/build/BUILD/jaf-api-1.2.2/activation/src/main/java/module-info.java:11: error: duplicate module: jakarta.activation
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.md NOTICE.md

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Marian Koncek <mkoncek@redhat.com> - 1.2.2-8
- Add major compat version

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Marian Koncek <mkoncek@redhat.com> - 1.2.2-6
- Provide a javax.activation.jar symlink

* Mon Jan 09 2023 Marian Koncek <mkoncek@redhat.com> - 1.2.2-5
- Remove noncompat javax provides
- Add more compat jakarta provides

* Tue Dec 20 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.2-4
- Fix incorrect Maven metadata

* Thu Dec 08 2022 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.2-3
- Add non-compat javax.activation:activation alias

* Thu Dec 01 2022 Marian Koncek <mkoncek@redhat.com> - 1.2.2-2
- Use only the major version in maven compat version

* Wed Nov 30 2022 Marian Koncek <mkoncek@redhat.com> - 1.2.2-1
- Initial package renamed from jakarta-activation
