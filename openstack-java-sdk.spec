# % global git_hash git10597f7

Name:           openstack-java-sdk
Version:        3.2.9
Release:        14%{?git_hash}%{?dist}
Summary:        OpenStack Java SDK

License:        ASL 2.0
URL:            https://github.com/woorea/%{name}
Source0:        https://github.com/woorea/%{name}/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  jackson-annotations >= 2.9.0
BuildRequires:  jackson-core >= 2.9.0
BuildRequires:  jackson-databind >= 2.9.0
BuildRequires:  jackson-jaxrs-json-provider >= 2.9.0
BuildRequires:  maven-local
BuildRequires:  junit
BuildRequires:  mvn(org.apache.httpcomponents:httpclient) >= 4.5.0
BuildRequires:  mvn(org.jboss.resteasy:resteasy-jaxrs)

Requires:  jackson-annotations >= 2.9.0
Requires:  jackson-core >= 2.9.0
Requires:  jackson-databind >= 2.9.0
Requires:  jackson-jaxrs-json-provider >= 2.9.0

%description
OpenStack client implementation in Java.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.

%package -n openstack-java-client
Summary:        OpenStack Java Client

%description -n openstack-java-client
This package contains the %{summary}.


%package -n openstack-java-resteasy-connector
Summary:        OpenStack Java RESTEasy Connector

%description -n openstack-java-resteasy-connector
This package contains the %{summary}.
Requires:  mvn(org.apache.httpcomponents:httpclient) >= 4.5.0


%package -n openstack-java-ceilometer-client
Summary:        OpenStack Java Ceilometer Client

%description -n openstack-java-ceilometer-client
This package contains the %{summary}.


%package -n openstack-java-ceilometer-model
Summary:        OpenStack Java Ceilometer Model

%description -n openstack-java-ceilometer-model
This package contains the %{summary}.


%package -n openstack-java-glance-client
Summary:        OpenStack Java Glance Client

%description -n openstack-java-glance-client
This package contains the %{summary}.


%package -n openstack-java-glance-model
Summary:        OpenStack Java Glance Model

%description -n openstack-java-glance-model
This package contains the %{summary}.


%package -n openstack-java-cinder-client
Summary:        OpenStack Java Cinder Client

%description -n openstack-java-cinder-client
This package contains the %{summary}.


%package -n openstack-java-cinder-model
Summary:        OpenStack Java Cinder Model

%description -n openstack-java-cinder-model
This package contains the %{summary}.


%package -n openstack-java-keystone-client
Summary:        OpenStack Java Keystone Client

%description -n openstack-java-keystone-client
This package contains the %{summary}.


%package -n openstack-java-keystone-model
Summary:        OpenStack Java Keystone Model

%description -n openstack-java-keystone-model
This package contains the %{summary}.


%package -n openstack-java-nova-client
Summary:        OpenStack Java Nova Client

%description -n openstack-java-nova-client
This package contains the %{summary}.


%package -n openstack-java-nova-model
Summary:        OpenStack Java Nova Model

%description -n openstack-java-nova-model
This package contains the %{summary}.


%package -n openstack-java-quantum-client
Summary:        OpenStack Java Quantum Client

%description -n openstack-java-quantum-client
This package contains the %{summary}.


%package -n openstack-java-quantum-model
Summary:        OpenStack Java Quantum Model

%description -n openstack-java-quantum-model
This package contains the %{summary}.


%package -n openstack-java-swift-client
Summary:        OpenStack Java Swift Client

%description -n openstack-java-swift-client
This package contains the %{summary}.


%package -n openstack-java-swift-model
Summary:        OpenStack Java Swift Model

%description -n openstack-java-swift-model
This package contains the %{summary}.


%package -n openstack-java-heat-client
Summary:        OpenStack Java Heat Client

%description -n openstack-java-heat-client
This package contains the %{summary}.


%package -n openstack-java-heat-model
Summary:        OpenStack Java Heat Model

%description -n openstack-java-heat-model
This package contains the %{summary}.


%prep
%setup -q -n %{name}-%{name}-%{version}

# remove unnecessary dependency on parent POM
%pom_remove_parent

%mvn_package ":{openstack-java-sdk,openstack-client-connectors}" __noinstall


%build
%mvn_build -s -- -P "!console,!examples,!jersey2,!jersey,resteasy" -DskipTests


%install
%mvn_install

%files javadoc -f .mfiles-javadoc

%files -n openstack-java-client -f .mfiles-openstack-client
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-resteasy-connector -f .mfiles-resteasy-connector
%doc LICENSE.txt README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-ceilometer-client -f .mfiles-ceilometer-client
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-ceilometer-model -f .mfiles-ceilometer-model
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-glance-client -f .mfiles-glance-client
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-glance-model -f .mfiles-glance-model
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-cinder-client -f .mfiles-cinder-client
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-cinder-model -f .mfiles-cinder-model
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-keystone-client -f .mfiles-keystone-client
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-keystone-model -f .mfiles-keystone-model
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-nova-client -f .mfiles-nova-client
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-nova-model -f .mfiles-nova-model
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-quantum-client -f .mfiles-quantum-client
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-quantum-model -f .mfiles-quantum-model
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-swift-client -f .mfiles-swift-client
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-swift-model -f .mfiles-swift-model
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%files -n openstack-java-heat-client -f .mfiles-heat-client
%license LICENSE.txt
%doc README.textile

%files -n openstack-java-heat-model -f .mfiles-heat-model
%license LICENSE.txt
%doc README.textile
%dir %{_javadir}/%{name}

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 3.2.9-12
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.2.9-11
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 15 2021 Dominik Holler <dholler@redhat.com> - 3.2.9-9
- Added direct dependency to junit

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 30 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.9-6
- Remove unnecessary dependency on parent POM.

* Wed Jul 29 2020 Dominik Holler <dholler@redhat.com> - 3.2.9-5
- adding a packaging-guidelines conformant -javadoc subpackage

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 3.2.9-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri May 15 2020 Dominik Holler <dholler@redhat.com> - 3.2.9-2
- disable openstack-java-javadoc

* Wed Apr 15 2020 Dominik Holler <dholler@redhat.com> - 3.2.9-1
- update to openstack-java-sdk-3.2.9

* Sat Feb 01 2020 Dominik Holler <dholler@redhat.com> - 3.2.8-1
- update to openstack-java-sdk-3.2.8

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Dominik Holler <dholler@redhat.com> - 3.2.7-3
- Change build dependency to jboss-annotations-1.2-api on rhel8 and fedora

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 2019 Dominik Holler <dholler@redhat.com> - 3.2.7-1
- update to openstack-java-sdk-3.2.7

* Fri May 03 2019 Dominik Holler <dholler@redhat.com> - 3.2.6-1
- update to openstack-java-sdk-3.2.6

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Dominik Holler <dholler@redhat.com> - 3.2.5-1
- update to openstack-java-sdk-3.2.5

* Tue Aug 14 2018 Dominik Holler <dholler@redhat.com> - 3.2.4-1
- update to openstack-java-sdk-3.2.4

* Mon Jul 23 2018 Dominik Holler <dholler@redhat.com> - 3.2.3-1
- update to openstack-java-sdk-3.2.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Dominik Holler <dholler@redhat.com> - 3.1.3-1
- update to openstack-java-sdk-3.1.3

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Dominik Holler <dholler@redhat.com> - 3.1.2-1
- update to openstack-java-sdk-3.1.2
- add build-time dependency sonatype-oss-parent

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar  8 2015 Federico Simoncelli <fsimonce@redhat.com> - 3.1.1-1
- update to openstack-java-sdk-3.1.1

* Wed Jan 14 2015 Federico Simoncelli <fsimonce@redhat.com> - 3.0.6-1
- update to openstack-java-sdk-3.0.6

* Fri Jun 27 2014 Federico Simoncelli <fsimonce@redhat.com> - 3.0.5-1
- update to openstack-java-sdk-3.0.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Federico Simoncelli <fsimonce@redhat.com> - 3.0.4-1
- update to openstack-java-sdk-3.0.4

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 3.0.2-2
- Use Requires: java-headless rebuild (#1067528)

* Tue Jan  7 2014 Federico Simoncelli <fsimonce@redhat.com> - 3.0.2-1
- update to openstack-java-sdk-3.0.2

* Fri Oct  4 2013 Federico Simoncelli <fsimonce@redhat.com> - 3.0.1-1
- update to openstack-java-sdk-3.0.1

* Thu Aug 29 2013 Federico Simoncelli <fsimonce@redhat.com> - 3.0.0-2
- resteasy: add support for resteasy 3

* Wed Aug 28 2013 Federico Simoncelli <fsimonce@redhat.com> - 3.0.0-1
- update to openstack-java-sdk-3.0.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-0.1.git10597f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 23 2013 Federico Simoncelli <fsimonce@redhat.com> - 3.0.0-0.0.git10597f7
- Initial build
