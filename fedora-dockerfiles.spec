%global commit     eab04ff2d6c3fcf729fe2d20c64e16b909b1b45e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}

Name:           fedora-dockerfiles
Version:        0
Release:        0.32.git%{shortcommit}%{?dist}
Summary:        Example dockerfiles to assist standing up containers quickly
License:        GPLv2
URL:            https://github.com/fedora-cloud/Fedora-Dockerfiles.git
Source0:        https://github.com/fedora-cloud/Fedora-Dockerfiles/archive/%{commit}/Fedora-Dockerfiles-%{shortcommit}.tar.gz
ExclusiveArch:  %{go_arches}
# no docker on ppc64:
# https://bugzilla.redhat.com/show_bug.cgi?id=1465174
ExcludeArch:    ppc64
Requires:       docker

%description
This package provides a community contributed set of examples that can
assist in learning about Docker containers. Use these examples to
stand up test environments using the Docker container engine.

%prep
%setup -n Fedora-Dockerfiles-%{commit}

%build

%install
rm -rf needs_work TODO
install -d -p -m 755 %{buildroot}%{_datadir}/%{name}
for d in Django ansible apache bind busybox cadvisor cockpit-ws container-best-practices firefox couchdb cups dhcpd earthquake flask hadoop haskell java-openjdk-8 jenkins lapis libvirt lighttpd mariadb maven memcached mesos mongodb mysql nginx nodejs owncloud pdftk postgresql python qpid rabbitmq redis registry ruby squid ssh systemd wordpress; do
        if [ -f $d/LICENSE* ]
        then
            mv $d/LICENSE* ./LICENSE-$d
        fi
        cp -pav $d %{buildroot}%{_datadir}/%{name}
done

%files 
%{!?_licensedir:%global license %%doc}
%license LICENSE-*
%doc README.md
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/*
%{_datadir}/%{name}/*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.32.giteab04ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.31.giteab04ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.30.giteab04ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.giteab04ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.28.giteab04ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.27.giteab04ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.giteab04ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.25.giteab04ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.giteab04ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.giteab04ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.giteab04ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.giteab04ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Till Maas <opensource@till.name> - 0-0.20.git
- ExcludeArch: ppc64: there is no docker there

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.giteab04ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.giteab04ff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep  1 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0-0.17.git
- Use go_arches to define ExclusiveArch
- Use %%license

* Tue Jul 07 2015 Aditya Patawari <adimania@fedoraproject.org> - 0-0.16.git
- update to master commit: eab04ff2d6c3fcf729fe2d20c64e16b909b1b45e

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.15.gitbd5429f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 28 2015 Aditya Patawari <adimania@fedoraproject.org> - 0-0.14.git
- update to master commit: bd5429fd4f00161b41a1dd77b9535d8a94739d9b

* Fri Dec 12 2014 Aditya Patawari <adimania@fedoraproject.org> - 0-0.13.git
- more dockerfiles
- fixing the upstream to the official fedora-cloud account

* Wed Sep 10 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.12.git
- update to master commit: f6cd84c2454208c8e0ba8c207f5eaaca37933b70
- preserve timestamps while copying files over

* Sat Aug 16 2014 Aditya Patawari <adimania@fedoraproject.org> - 0-0.11.git
- we don't want debug package since it is noarch

* Sat Aug 16 2014 Aditya Patawari <adimania@fedoraproject.org> - 0-0.10.git
- fixing the source file with a version bump

* Sat Aug 16 2014 Aditya Patawari <adimania@fedoraproject.org> - 0-0.9.git
- more dockerfiles with bugfixes

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git122ef5d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 01 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.7.git
- archful as per docker-io

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git122ef5d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 12 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.5.git
- require docker-io

* Sat Apr 12 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.4.git
- include bind, earthquake, hadoop, lighttpd, python, qpid, redis, registry

* Wed Feb 19 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.3.git7753bdf
- own main package directory

* Tue Feb 11 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.2.git7753bdf
- use a loop to install stuff
- include firefox and nodejs
- install separate license for each program

* Tue Jan 14 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.git202887b
- Initial fedora package
