Name:		voms-clients-java
Version:	3.3.3
Release:	2%{?dist}
Summary:	Virtual Organization Membership Service Java clients

License:	Apache-2.0
URL:		https://wiki.italiangrid.it/VOMS
Source0:	https://github.com/italiangrid/voms-clients/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
ExclusiveArch:	%{java_arches} noarch

BuildRequires:	maven-local
BuildRequires:	mvn(commons-cli:commons-cli)
BuildRequires:	mvn(commons-io:commons-io)
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.italiangrid:voms-api-java)
BuildRequires:	voms-api-java >= 3.3.3
Requires:	voms-api-java >= 3.3.3
Requires:	java-headless

Requires(post):		%{_sbindir}/update-alternatives
Requires(postun):	%{_sbindir}/update-alternatives

# Older versions of voms-clients did not have alternatives
Conflicts:	voms-clients < 2.0.12

Provides:	voms-clients = %{version}-%{release}

%description
The Virtual Organization Membership Service (VOMS) is an attribute authority
which serves as central repository for VO user authorization information,
providing support for sorting users into group hierarchies, keeping track of
their roles and other attributes in order to issue trusted attribute
certificates and SAML assertions used in the Grid environment for
authorization purposes.

This package provides the Java version of the command line clients for VOMS:
voms-proxy-init, voms-proxy-destroy and voms-proxy-info.

%prep
%setup -q -n voms-clients-%{version}

# Remove maven-javadoc-plugin configuration
# We are not building the javadoc for this package
# And its presence causes the EPEL 8 build to fail
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin

# Do not create source jars
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

# Don't do assembly
%pom_remove_plugin :maven-assembly-plugin

# Remove license plugin
%pom_remove_plugin com.mycila.maven-license-plugin:maven-license-plugin

%build
%mvn_build -j

%install
%mvn_install

mkdir -p %{buildroot}%{_bindir}

%if %{?rhel}%{!?rhel:0} == 8
guava_cp="guava20"
bc_cp="bcpkix bcprov"
%else
guava_cp="guava/guava"
bc_cp="bcpkix bcutil bcprov"
%endif

cat > %{buildroot}%{_bindir}/voms-proxy-init3 << EOF
#!/bin/sh
VOMS_CLIENTS_JAVA_OPTIONS=\${VOMS_CLIENTS_JAVA_OPTIONS:-"-XX:+UseSerialGC -Xmx16m"}
java \$VOMS_CLIENTS_JAVA_OPTIONS -cp \$(build-classpath voms-clients-java voms-api-java canl-java ${guava_cp} ${bc_cp} commons-cli commons-io) org.italiangrid.voms.clients.VomsProxyInit "\$@"
EOF
chmod 755 %{buildroot}%{_bindir}/voms-proxy-init3

cat > %{buildroot}%{_bindir}/voms-proxy-info3 << EOF
#!/bin/sh
VOMS_CLIENTS_JAVA_OPTIONS=\${VOMS_CLIENTS_JAVA_OPTIONS:-"-XX:+UseSerialGC -Xmx16m"}
java \$VOMS_CLIENTS_JAVA_OPTIONS -cp \$(build-classpath voms-clients-java voms-api-java canl-java ${guava_cp} ${bc_cp} commons-cli commons-io) org.italiangrid.voms.clients.VomsProxyInfo "\$@"
EOF
chmod 755 %{buildroot}%{_bindir}/voms-proxy-info3

cat > %{buildroot}%{_bindir}/voms-proxy-destroy3 << EOF
#!/bin/sh
VOMS_CLIENTS_JAVA_OPTIONS=\${VOMS_CLIENTS_JAVA_OPTIONS:-"-XX:+UseSerialGC -Xmx16m"}
java \$VOMS_CLIENTS_JAVA_OPTIONS -cp \$(build-classpath voms-clients-java voms-api-java canl-java ${guava_cp} ${bc_cp} commons-cli commons-io) org.italiangrid.voms.clients.VomsProxyDestroy "\$@"
EOF
chmod 755 %{buildroot}%{_bindir}/voms-proxy-destroy3

mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 644 man/voms-proxy-init.1 \
    %{buildroot}%{_mandir}/man1/voms-proxy-init3.1
install -p -m 644 man/voms-proxy-info.1 \
    %{buildroot}%{_mandir}/man1/voms-proxy-info3.1
install -p -m 644 man/voms-proxy-destroy.1 \
    %{buildroot}%{_mandir}/man1/voms-proxy-destroy3.1

mkdir -p %{buildroot}%{_sysconfdir}/alternatives
for b in voms-proxy-init voms-proxy-info voms-proxy-destroy; do
  ln -s %{_bindir}/${b}3 %{buildroot}%{_sysconfdir}/alternatives/${b}
  ln -s %{_sysconfdir}/alternatives/${b} %{buildroot}%{_bindir}/${b}
  ln -s %{_mandir}/man1/${b}3.1.gz %{buildroot}%{_sysconfdir}/alternatives/${b}.1.gz
  ln -s %{_sysconfdir}/alternatives/${b}.1.gz %{buildroot}%{_mandir}/man1/${b}.1.gz
done

mkdir -p %{buildroot}%{_mandir}/man5
install -p -m 644 man/vomsdir.5 %{buildroot}%{_mandir}/man5/vomsdir.5
install -p -m 644 man/vomses.5 %{buildroot}%{_mandir}/man5/vomses.5

%post
%{_sbindir}/update-alternatives --install %{_bindir}/voms-proxy-init \
    voms-proxy-init %{_bindir}/voms-proxy-init3 90 \
    --slave %{_mandir}/man1/voms-proxy-init.1.gz voms-proxy-init-man \
    %{_mandir}/man1/voms-proxy-init3.1.gz
%{_sbindir}/update-alternatives --install %{_bindir}/voms-proxy-info \
    voms-proxy-info %{_bindir}/voms-proxy-info3 90 \
    --slave %{_mandir}/man1/voms-proxy-info.1.gz voms-proxy-info-man \
    %{_mandir}/man1/voms-proxy-info3.1.gz
%{_sbindir}/update-alternatives --install %{_bindir}/voms-proxy-destroy \
    voms-proxy-destroy %{_bindir}/voms-proxy-destroy3 90 \
    --slave %{_mandir}/man1/voms-proxy-destroy.1.gz voms-proxy-destroy-man \
    %{_mandir}/man1/voms-proxy-destroy3.1.gz

%postun
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove voms-proxy-init \
    %{_bindir}/voms-proxy-init3
    %{_sbindir}/update-alternatives --remove voms-proxy-info \
    %{_bindir}/voms-proxy-info3
    %{_sbindir}/update-alternatives --remove voms-proxy-destroy \
    %{_bindir}/voms-proxy-destroy3
fi

%files -f .mfiles
%{_bindir}/voms-proxy-destroy3
%{_bindir}/voms-proxy-info3
%{_bindir}/voms-proxy-init3
%ghost %{_bindir}/voms-proxy-destroy
%ghost %{_bindir}/voms-proxy-info
%ghost %{_bindir}/voms-proxy-init
%ghost %{_sysconfdir}/alternatives/voms-proxy-destroy
%ghost %{_sysconfdir}/alternatives/voms-proxy-info
%ghost %{_sysconfdir}/alternatives/voms-proxy-init
%{_mandir}/man1/voms-proxy-destroy3.1*
%{_mandir}/man1/voms-proxy-info3.1*
%{_mandir}/man1/voms-proxy-init3.1*
%ghost %{_mandir}/man1/voms-proxy-destroy.1*
%ghost %{_mandir}/man1/voms-proxy-info.1*
%ghost %{_mandir}/man1/voms-proxy-init.1*
%ghost %{_sysconfdir}/alternatives/voms-proxy-destroy.1*
%ghost %{_sysconfdir}/alternatives/voms-proxy-info.1*
%ghost %{_sysconfdir}/alternatives/voms-proxy-init.1*
%{_mandir}/man5/vomsdir.5*
%{_mandir}/man5/vomses.5*
%doc AUTHORS README.md
%license LICENSE

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Aug 03 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.3-1
- Update to version 3.3.3

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 24 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.2-15
- Update License tags (SPDX)
- Add additional ghost files to package (rpmlint)

* Thu May 23 2024 Marian Koncek <mkoncek@redhat.com> - 3.3.2-14
- Add Requires on java-headless

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 3.3.2-13
- Rebuilt for java-21-openjdk as system jdk

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 3.3.2-8
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.3.2-7
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.2-5
- Add bcutil to classpath

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.2-3
- Add missing build requires mvn(junit:junit)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.2-1
- Update to version 3.3.2
- Drop patches voms-clients-java-use-a-more-sensible-timeout.patch and
  voms-clients-java-change-default-proxy-cert-key-length-to-2048-bits.patch

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 3.3.0-8
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.0-6
- Remove maven-javadoc-plugin configuration

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.0-3
- Change default proxy cert key length to 2048 bits
- Use a more sensible timeout

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.3.0-1
- Update to version 3.3.0
- Drop patches voms-clients-java-except.patch and -canl-2.5.patch

* Fri Jan 05 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.0.7-5
- Adapt to canl-java 2.5

* Tue Aug 08 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.0.7-4
- Don't do assembly

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 10 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.0.7-1
- Update to version 3.0.7
- Drop patch voms-clients-java-javadoc.patch

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jul 11 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0.6-3
- Fix javadoc warnings

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0.6-1
- Update to version 3.0.6
- Implement new license packaging guidelines
- Add virtual provides voms-clients (the old voms-clients package was
  renamed voms-clients-cpp)

* Mon Nov 17 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.0.5-1
- Initial build
