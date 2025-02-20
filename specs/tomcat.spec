%global jspspec 3.1
%global major_version 10
%global minor_version 1
%global micro_version 34
%global packdname apache-tomcat-%{version}-src
%global servletspec 6.0
%global elspec 5.0
%global tcuid 53
# Recommended version is specified in java/org/apache/catalina/core/AprLifecycleListener.java
%global native_version 2.0.8

# FHS 3.0 compliant tree structure - http://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html
%global basedir %{_var}/lib/%{name}
%global baseconfdir %{basedir}/conf
%global baselogdir %{basedir}/logs
%global appdir %{basedir}/webapps
%global homedir %{_datadir}/%{name}
%global bindir %{homedir}/bin
%global confdir %{_sysconfdir}/%{name}
%global libdir %{_javadir}/%{name}
%global logdir %{_var}/log/%{name}
%global cachedir %{_var}/cache/%{name}
%global workdir %{basedir}/work

Name:          tomcat
Epoch:         1
Version:       %{major_version}.%{minor_version}.%{micro_version}
Release:       %autorelease
Summary:       Apache Servlet/JSP Engine, RI for Servlet %{servletspec}/JSP %{jspspec} API

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:       Apache-2.0
URL:           http://tomcat.apache.org/
Source0:       http://www.apache.org/dist/tomcat/tomcat-%{major_version}/v%{version}/src/%{packdname}.tar.gz
Source1:       %{name}-%{major_version}.%{minor_version}.conf
Source2:       %{name}-%{major_version}.%{minor_version}.logrotate
Source3:       %{name}-%{major_version}.%{minor_version}.service
Source4:       %{name}-%{major_version}.%{minor_version}-locate-java.sh
Source5:       %{name}-%{major_version}.%{minor_version}-start.sh

# https://bugzilla.redhat.com/show_bug.cgi?id=435829
Patch0:        %{name}-%{major_version}.%{minor_version}-bootstrap-MANIFEST.MF.patch
Patch1:        %{name}-%{major_version}.%{minor_version}-users-webapp.patch
Patch2:        %{name}-%{major_version}.%{minor_version}-build.patch
# catalina.policy patch to allow ECJ usage under the Security Manager
Patch3:        %{name}-%{major_version}.%{minor_version}-catalina-policy.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1857043
Patch4:        %{name}-%{major_version}.%{minor_version}-bnd-annotation.patch
# Fixes not available constants in ECJ
Patch5:        %{name}-%{major_version}.%{minor_version}-JDTCompiler.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1857043
Patch6:        rhbz-1857043.patch

BuildArch:     noarch
# Can't use noarch since we are packaging tomcat-jni.jar.
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Java/#_architecture_support
ExclusiveArch:  %{java_arches}

BuildRequires: ant
BuildRequires: ecj
BuildRequires: findutils
BuildRequires: java-devel
BuildRequires: javapackages-local
BuildRequires: aqute-bnd
BuildRequires: tomcat-jakartaee-migration
BuildRequires: systemd

Requires: (java-headless >= 11 or java >= 11)
Requires: %{name}-lib = %{epoch}:%{version}-%{release}
Recommends: tomcat-native >= %{native_version}
Requires: systemd

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License version 2.0. Tomcat is intended
to be a collaboration of the best-of-breed developers from around the world.

%package admin-webapps
Summary: The host-manager and manager web applications for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}

%description admin-webapps
The host-manager and manager web applications for Apache Tomcat.

%package docs-webapp
Summary: The docs web application for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}

%description docs-webapp
The docs web application for Apache Tomcat.

%package jsp-%{jspspec}-api
Summary: Apache Tomcat JavaServer Pages v%{jspspec} API Implementation Classes
Provides: jsp = %{jspspec}
Obsoletes: jsp < %{jspspec}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{epoch}:%{version}-%{release}
Conflicts: tomcat-jsp-2.3-api

%description jsp-%{jspspec}-api
Apache Tomcat JSP API Implementation Classes.

%package lib
Summary: Libraries needed to run the Tomcat Web container
Requires: %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{epoch}:%{version}-%{release}
Requires: ecj >= 4.20
Recommends: tomcat-jakartaee-migration

%description lib
Libraries needed to run the Tomcat Web container.

%package servlet-%{servletspec}-api
Summary: Apache Tomcat Java Servlet v%{servletspec} API Implementation Classes
Provides: servlet = %{servletspec}
Obsoletes: servlet < %{servletspec}
Conflicts: tomcat-servlet-4.0-api

%description servlet-%{servletspec}-api
Apache Tomcat Servlet API Implementation Classes.

%package el-%{elspec}-api
Summary: Apache Tomcat Expression Language v%{elspec} API Implementation Classes
Provides: el_api = %{elspec}
Obsoletes: el_api < %{elspec}
Conflicts: tomcat-el-3.0-api

%description el-%{elspec}-api
Apache Tomcat EL API Implementation Classes.

%package webapps
Summary: The ROOT web application for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}

%description webapps
The ROOT web application for Apache Tomcat.

%prep
%setup -q -n %{packdname}
# remove pre-built binaries and windows files
find . -type f \( -name "*.bat" -o -name "*.class" -o -name Thumbs.db -o -name "*.gz" -o \
   -name "*.jar" -o -name "*.war" -o -name "*.zip" \) -delete

%patch 0 -p0
%patch 1 -p0
%patch 2 -p0
%patch 3 -p0
%patch 4 -p0
%patch 5 -p0
%patch 6 -p0

# Remove webservices naming resources as it's generally unused
%{__rm} -rf java/org/apache/naming/factory/webservices

# Create a sysusers.d config file
cat >tomcat.sysusers.conf <<EOF
u tomcat %{tcuid} 'Apache Tomcat' %{homedir} -
EOF

%build
# we don't care about the tarballs and we're going to replace jars
# so just create a dummy file for later removal
touch HACK

# who needs a build.properties file anyway
%{ant} -Dbase.path="." \
  -Dbuild.compiler="modern" \
  -Dcommons-daemon.jar="HACK" \
  -Dcommons-daemon.native.src.tgz="HACK" \
  -Djdt.jar="$(build-classpath ecj/ecj)" \
  -Dtomcat-native.tar.gz="HACK" \
  -Dtomcat-native.home="." \
  -Dcommons-daemon.native.win.mgr.exe="HACK" \
  -Dnsis.exe="HACK" \
  -Djaxrpc-lib.jar="HACK" \
  -Dwsdl4j-lib.jar="HACK" \
  -Dbnd.jar="$(build-classpath aqute-bnd/biz.aQute.bnd)" \
  -Dbnd-annotation.jar="$(build-classpath aqute-bnd/biz.aQute.bnd.annotation)" \
  -Dversion="%{version}" \
  -Dversion.build="%{micro_version}" \
  -Dmigration-lib.jar="$(build-classpath tomcat-jakartaee-migration/jakartaee-migration)" \
  deploy

# remove some jars that we'll replace with symlinks later
%{__rm} output/build/bin/commons-daemon.jar output/build/lib/ecj.jar output/build/lib/jakartaee-migration.jar
# Remove the example webapps per Apache Tomcat Security Considerations
# see https://tomcat.apache.org/tomcat-10.1-doc/security-howto.html
%{__rm} -rf output/build/webapps/examples

%install
# build initial path structure
# %{__install} -d ${RPM_BUILD_ROOT}%{_bindir}
%{__install} -d ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
%{__install} -d ${RPM_BUILD_ROOT}%{appdir}
%{__install} -d ${RPM_BUILD_ROOT}%{bindir}
%{__install} -d ${RPM_BUILD_ROOT}%{confdir}
%{__install} -d ${RPM_BUILD_ROOT}%{confdir}/Catalina/localhost
%{__install} -d ${RPM_BUILD_ROOT}%{confdir}/conf.d
/bin/echo "Place your custom *.conf files here. Shell expansion is supported." > ${RPM_BUILD_ROOT}%{confdir}/conf.d/README
%{__install} -d ${RPM_BUILD_ROOT}%{libdir}
%{__install} -d ${RPM_BUILD_ROOT}%{logdir}
%{__install} -d ${RPM_BUILD_ROOT}%{homedir}
%{__install} -d ${RPM_BUILD_ROOT}%{cachedir}
%{__install} -d ${RPM_BUILD_ROOT}%{_unitdir}
%{__install} -d ${RPM_BUILD_ROOT}%{_libexecdir}/%{name}

%{__install} %{SOURCE1} ${RPM_BUILD_ROOT}%{confdir}/%{name}.conf
%{__sed} -e "s|\@\@\@TCLOG\@\@\@|%{logdir}|g" %{SOURCE2} > ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}.disabled
%{__install} %{SOURCE3} ${RPM_BUILD_ROOT}%{_unitdir}/%{name}.service
%{__install} %{SOURCE4} ${RPM_BUILD_ROOT}%{_libexecdir}/%{name}/%{name}-locate-java.sh
%{__install} %{SOURCE5} ${RPM_BUILD_ROOT}%{_libexecdir}/%{name}/%{name}-start.sh

%{__install} -D tomcat.sysusers.conf ${RPM_BUILD_ROOT}%{_sysusersdir}/tomcat.conf

for jar in output/build/lib/*.jar; do
    # Skip Jar if empty, applies to tomcat-coyote-ffm.jar atm
    jar tf ${jar} | grep -E -q '.*\.class' || continue

    jarname=$(basename $jar .jar)

    case "${jarname}" in
        jasper) pom="res/maven/tomcat-jasper.pom" ;;
        catalina-tribes) pom="res/maven/tomcat-tribes.pom" ;;
        catalina-ssi) pom="res/maven/tomcat-ssi.pom" ;;
        catalina-storeconfig) pom="res/maven/tomcat-storeconfig.pom" ;;
        *) pom=$(ls res/maven/*"${jarname}".pom 2>/dev/null) ;;
    esac

    sed -i "s/@MAVEN.DEPLOY.VERSION@/%{version}/g" ${pom}

    case "${jarname}" in
        tomcat-jni) %mvn_file org.apache.tomcat:tomcat-jni tomcat/tomcat-jni %{libdir}/tomcat-jni ;;
        jsp-api) %mvn_file org.apache.tomcat:tomcat-jsp-api tomcat/jsp-api tomcat/%{name}-jsp-%{jspspec}-api %{name}-jsp-%{jspspec}-api %{name}-jsp-api ;;
        servlet-api) %mvn_file org.apache.tomcat:tomcat-servlet-api tomcat/servlet-api tomcat/%{name}-servlet-%{servletspec}-api %{name}-servlet-%{servletspec}-api %{name}-servlet-api ;;
        el-api) %mvn_file org.apache.tomcat:tomcat-el-api tomcat/el-api tomcat/%{name}-el-%{servletspec}-api %{name}-el-%{servletspec}-api %{name}-el-api ;;
        catalina-tribes) %mvn_file org.apache.tomcat:tomcat-tribes tomcat/catalina-tribes ;;
        catalina-ssi) %mvn_file org.apache.tomcat:tomcat-ssi tomcat/catalina-ssi ;;
        catalina-storeconfig) %mvn_file org.apache.tomcat:tomcat-storeconfig tomcat/catalina-storeconfig ;;
        *) %mvn_file org.apache.tomcat:$(sed -n "/<artifactId>.*${jarname}.*<\/artifactId>/ { s/.*<artifactId>\(.*${jarname}.*\)<\/artifactId>.*/\1/; p; q; }" "${pom}" 2>/dev/null) tomcat/${jarname} ;;
    esac

    %mvn_artifact ${pom} ${jar}
done

sed -i "s/@MAVEN.DEPLOY.VERSION@/%{version}/g" res/maven/tomcat-juli.pom
%mvn_artifact res/maven/tomcat-juli.pom output/build/bin/tomcat-juli.jar
# bootstrap does not have a pom, generate one
%mvn_artifact 'org.apache.tomcat:tomcat-bootstrap:%{version}' output/build/bin/bootstrap.jar

%mvn_file org.apache.tomcat:tomcat-bootstrap tomcat/tomcat-bootstrap
%mvn_file org.apache.tomcat:tomcat-juli tomcat/tomcat-juli

# tomcat-parent pom
sed -i "s/@MAVEN.DEPLOY.VERSION@/%{version}/g" res/maven/tomcat.pom
%mvn_artifact res/maven/tomcat.pom

%mvn_package ":tomcat-el-api" tomcat-el-api
%mvn_package ":tomcat-jsp-api" tomcat-jsp-api
%mvn_package ":tomcat-servlet-api" tomcat-servlet-api

%mvn_install

# Fixes JAR must have Javapackages-GroupId manifest attribute error
jar ufm ${RPM_BUILD_ROOT}%{libdir}/el-api.jar <(echo "JavaPackages-GroupId: org.apache.tomcat")
jar ufm ${RPM_BUILD_ROOT}%{libdir}/jsp-api.jar <(echo "JavaPackages-GroupId: org.apache.tomcat")
jar ufm ${RPM_BUILD_ROOT}%{libdir}/servlet-api.jar <(echo "JavaPackages-GroupId: org.apache.tomcat")

# move things into place
pushd output/build
    %{__cp} -a bin/* ${RPM_BUILD_ROOT}%{bindir}
    %{__cp} -a conf/*.{policy,properties,xml} ${RPM_BUILD_ROOT}%{confdir}
    %{__cp} -a webapps/* ${RPM_BUILD_ROOT}%{appdir}
popd

ln -sr $(build-classpath ecj/ecj) ${RPM_BUILD_ROOT}%{libdir}/ecj-x.jar
ln -sr $(build-classpath tomcat-jakartaee-migration/jakartaee-migration) ${RPM_BUILD_ROOT}%{libdir}/jakartaee-migration-x.jar

ln -sr %{confdir} ${RPM_BUILD_ROOT}%{baseconfdir}
ln -sr %{cachedir} ${RPM_BUILD_ROOT}%{workdir}
ln -sr %{logdir} ${RPM_BUILD_ROOT}%{baselogdir}
ln -sr %{libdir} ${RPM_BUILD_ROOT}%{homedir}/lib

%post
# install but don't activate
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc {LICENSE,NOTICE,RELEASE-NOTES,RUNNING.txt}
%{_unitdir}/%{name}.service
%{_libexecdir}/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}.disabled
%{_sysusersdir}/tomcat.conf
%{homedir}
%{baseconfdir}
%{baselogdir}
%{workdir}
%attr(2770,tomcat,adm) %dir %{logdir}
%attr(750,tomcat,tomcat) %dir %{cachedir}
%attr(2775,tomcat,tomcat) %dir %{appdir}

%{confdir}/conf.d
%config(noreplace) %{confdir}/%{name}.conf
# Configuration files should not be modifiable by the tomcat user, as this can be
# a security issue (an attacker may insert code in a webapp and rewrite the tomcat
# configuration) but those files should be readable by tomcat, so we set the group to tomcat.
%attr(640,root,tomcat) %config(noreplace) %{confdir}/tomcat-users.xml
%attr(640,root,tomcat) %config(noreplace) %{confdir}/web.xml
%attr(640,root,tomcat) %config(noreplace) %{confdir}/server.xml
%attr(640,root,tomcat) %config(noreplace) %{confdir}/logging.properties
%attr(640,root,tomcat) %config(noreplace) %{confdir}/catalina.properties
%attr(640,root,tomcat) %config(noreplace) %{confdir}/context.xml
%attr(640,root,tomcat) %config(noreplace) %{confdir}/jaspic-providers.xml
%attr(640,root,tomcat) %config(noreplace) %{confdir}/catalina.policy
%attr(2775,root,tomcat) %dir %{confdir}/Catalina
%attr(2775,root,tomcat) %dir %{confdir}/Catalina/localhost

%files admin-webapps
%{appdir}/host-manager
%{appdir}/manager

%files docs-webapp
%{appdir}/docs

%files lib -f .mfiles
%{libdir}/jakartaee-migration-x.jar
%{libdir}/ecj-x.jar
%exclude %{libdir}/tomcat-jni.pom

%files jsp-%{jspspec}-api -f .mfiles-tomcat-jsp-api
%doc LICENSE

%files servlet-%{servletspec}-api -f .mfiles-tomcat-servlet-api
%doc LICENSE

%files el-%{elspec}-api -f .mfiles-tomcat-el-api
%doc LICENSE

%files webapps
%defattr(0644,tomcat,tomcat,0755)
%{appdir}/ROOT

%changelog
%autochangelog
