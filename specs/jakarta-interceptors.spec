%global srcname interceptor-api

Name:           jakarta-interceptors
Version:        2.0.0
Release:        15%{?dist}
Summary:        Jakarta Interceptors
# Automatically converted from old format: EPL-2.0 or GPLv2 with exceptions - review is highly recommended.
License:        EPL-2.0 OR LicenseRef-Callaway-GPLv2-with-exceptions

%global upstream_version %{version}-RELEASE

URL:            https://github.com/eclipse-ee4j/interceptor-api
Source0:        %{url}/archive/%{upstream_version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

# package renamed in fedora 33, remove in fedora 35
Provides:       geronimo-interceptor = %{version}-%{release}
Obsoletes:      geronimo-interceptor < 1.0.1-25

%description
Jakarta Interceptors defines a means of interposing on business method
invocations and specific events—such as lifecycle events and timeout
events—that occur on instances of Jakarta EE components and other
managed classes.


%package javadoc
Summary:        Javadoc for %{name}

# package renamed in fedora 33, remove in fedora 35
Provides:       geronimo-interceptor-javadoc = %{version}-%{release}
Obsoletes:      geronimo-interceptor-javadoc < 1.0.1-25

%description javadoc
API documentation for %{name}.


%prep
%autosetup -n %{srcname}-%{upstream_version} -p1

# remove unnecessary dependencies on parent POM
%pom_remove_parent . api

# do not install useless parent POM
%mvn_package :interceptor-api-parent __noinstall

# do not build specification documentation
%pom_disable_module spec

# remove unnecessary maven plugins
%pom_remove_plugin :maven-enforcer-plugin api .
%pom_remove_plugin :maven-javadoc-plugin api
%pom_remove_plugin :maven-source-plugin api

# disable spec verification (fails because spec-version-maven-plugin is too old)
%pom_xpath_remove 'pom:goal[text()="check-module"]' api

# provide javax.interceptor packages in addition to jakarta.interceptor
cp -pr api/src/main/java/jakarta api/src/main/java/javax
sed -i -e 's/jakarta\./javax./g' $(find api/src/main/java/javax -name *.java)

# add compatibility alias for old maven artifact coordinates
%mvn_alias :jakarta.interceptor-api \
    org.apache.geronimo.specs:geronimo-interceptor_1.1_spec \
    org.apache.geronimo.specs:geronimo-interceptor_3.0_spec

# add compatibility symlink for old classpath
%mvn_file : %{name}/jakarta.interceptor-api geronimo-interceptor


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md NOTICE.md


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.0-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 2.0.0-12
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.0.0-6
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.0.0-5
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 23 2020 Fabio Valentini <decathorpe@gmail.com> - 2.0.0-1
- Initial package renamed from geronimo-interceptor.

