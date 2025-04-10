%global jspspec 3.1
%global major_version 10
%global minor_version 1
%global micro_version 36
%global packdname apache-tomcat-%{version}-src
%global servletspec 6.0
%global elspec 5.0
%global tcuid 53
%global min_java_version 11
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
%global userinstancedir %{homedir}/user-instance

Name:          tomcat
Epoch:         1
Version:       %{major_version}.%{minor_version}.%{micro_version}
Release:       %autorelease
Summary:       Apache Tomcat - Servlet and JSP engine for system-wide deployment

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:       Apache-2.0
URL:           http://tomcat.apache.org/
Source0:       http://www.apache.org/dist/tomcat/tomcat-%{major_version}/v%{version}/src/%{packdname}.tar.gz
Source1:       http://www.apache.org/dist/tomcat/tomcat-%{major_version}/v%{version}/src/%{packdname}.tar.gz.asc
# https://www.apache.org/dist/tomcat/tomcat-10/KEYS
Source2:       KEYS
Source3:       %{name}-%{major_version}.%{minor_version}.conf
Source4:       %{name}-%{major_version}.%{minor_version}.service
Source5:       %{name}-%{major_version}.%{minor_version}-locate-java.sh
Source6:       %{name}-%{major_version}.%{minor_version}-run.sh
Source7:       %{name}-%{major_version}.%{minor_version}-RUNNING.txt
Source8:       %{name}-%{major_version}.%{minor_version}-user-instance-create.sh
Source9:       %{name}-%{major_version}.%{minor_version}-setenv.sh
Source10:       %{name}-%{major_version}.%{minor_version}-user-instance-create.asciidoc

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

BuildRequires: gnupg2
BuildRequires: ant
BuildRequires: ecj
BuildRequires: findutils
BuildRequires: java-devel
BuildRequires: javapackages-local
BuildRequires: aqute-bnd
BuildRequires: tomcat-jakartaee-migration
BuildRequires: systemd
BuildRequires: rubygem-asciidoctor

Requires: %{name}-common = %{epoch}:%{version}-%{release}
Requires: systemd

Recommends: tomcat-native >= %{native_version}

Suggests: %{name}-admin-webapps = %{epoch}:%{version}-%{release}
Suggests: %{name}-docs-webapp = %{epoch}:%{version}-%{release}
Suggests: %{name}-webapps = %{epoch}:%{version}-%{release}
Suggests: %{name}-user-instance = %{epoch}:%{version}-%{release}

%description
Apache Tomcat is an open-source implementation of the Java Servlet, JavaServer Pages (JSP), and WebSocket technologies.
It provides a pure Java HTTP web server environment for running Java applications.
This package includes only the startup scripts for managing a system-wide Tomcat daemon.
It does not include documentation or web applications.
    * To install the default web applications, use the tomcat-webapps package.
    * To access online documentation, install tomcat-docs-webapps package.
    * To create user instances without running Tomcat as a system service, use tomcat-user-instance package instead.

%package user-instance
Summary: Apache Tomcat - Tools for creating user-managed instances
Requires: %{name}-common = %{epoch}:%{version}-%{release}
Suggests: %{name} = %{epoch}:%{version}-%{release}
Suggests: %{name}-admin-webapps = %{epoch}:%{version}-%{release}
Suggests: %{name}-docs-webapp = %{epoch}:%{version}-%{release}
Suggests: %{name}-webapps = %{epoch}:%{version}-%{release}

%description user-instance
This package provides the tools necessary to create user-managed Tomcat instances,
allowing users to run Tomcat independently of the system-wide service.
A user instance includes its own configuration, libraries, and web applications,
which can be started and stopped using scripts inside the instance directory.

%package common
Summary: Apache Tomcat - Common files for Tomcat packages
Requires: (java-headless >= %{min_java_version} or java >= %{min_java_version})
Requires: %{name}-lib = %{epoch}:%{version}-%{release}

%description common
This package contains common files required by both tomcat and tomcat-user-instance packages, including essential Tomcat
scripts and libraries. Installing this package alone does not provide a functional Tomcat installation,
but is required as a dependency for other Tomcat-related packages.

%package lib
Summary: Apache Tomcat - Core libraries for embedding Tomcat
Requires: %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{epoch}:%{version}-%{release}
Requires: ecj >= 4.20
Recommends: tomcat-jakartaee-migration

%description lib
This package contains the core libraries of Apache Tomcat, which allow other Java applications to embed Tomcat
as a lightweight servlet container. It is primarily intended for use by developers and applications that need Tomcat
as an embedded runtime.

%package admin-webapps
Summary: Apache Tomcat - Administrative web applications
Requires: %{name} = %{epoch}:%{version}-%{release}

%description admin-webapps
This package provides the Tomcat Web Application Manager and Virtual Host Manager, which allow administrators to deploy,
manage, and configure web applications through a web interface.
These tools simplify application lifecycle management without requiring direct filesystem access.

%package docs-webapp
Summary: Apache Tomcat - Online documentation web application
Requires: %{name} = %{epoch}:%{version}-%{release}

%description docs-webapp
This package provides the Tomcat documentation web application, accessible via the Tomcat server.
It includes API references, configuration guidelines, and development documentation.

%package webapps
Summary: Apache Tomcat - Default ROOT web application
Requires: %{name} = %{epoch}:%{version}-%{release}

%description webapps
This package includes the default ROOT web applications bundled with Apache Tomcat,
which serves as the default homepage when accessing Tomcat in a browser.

%package jsp-%{jspspec}-api
Summary: Apache Tomcat JavaServer Pages v%{jspspec} API Implementation Classes
Provides: jsp = %{jspspec}
Obsoletes: jsp < %{jspspec}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{epoch}:%{version}-%{release}
Conflicts: tomcat-jsp-2.3-api

%description jsp-%{jspspec}-api
Apache Tomcat JSP API Implementation Classes.

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

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

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

sed -i -e "s/@VERSION@/%{version}/g" \
       -e "s/@VERSION_MAJOR_MINOR@/%{major_version}.%{minor_version}/g" \
       -e "s/@VERSION_MAJOR@/%{major_version}/g" \
       -e "s/@MIN_JAVA_VERSION@/%{min_java_version}/g" \
       -e "s/@JDT_VERSION@/x/g" RELEASE-NOTES

# Create a sysusers.d config file
cat >tomcat.sysusers.conf <<EOF
u tomcat %{tcuid} 'Apache Tomcat' %{homedir} -
EOF

sed -i -e "s/Server port=\"8005\" shutdown=\"SHUTDOWN\"/Server port=\"-1\" shutdown=\"SHUTDOWN\"/" "conf/server.xml"

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
%{__install} -d ${RPM_BUILD_ROOT}%{appdir}
%{__install} -d ${RPM_BUILD_ROOT}%{appdir}-javaee
%{__install} -d ${RPM_BUILD_ROOT}%{bindir}
%{__install} -d ${RPM_BUILD_ROOT}%{confdir}/Catalina/localhost
%{__install} -d ${RPM_BUILD_ROOT}%{confdir}/conf.d
/bin/echo "Place your custom *.conf files here. Shell expansion is supported." > ${RPM_BUILD_ROOT}%{confdir}/conf.d/README
%{__install} -d ${RPM_BUILD_ROOT}%{logdir}
%{__install} -d ${RPM_BUILD_ROOT}%{cachedir}

%{__install} -D -p %{SOURCE3} ${RPM_BUILD_ROOT}%{confdir}/%{name}.conf
%{__install} -D -p %{SOURCE4} ${RPM_BUILD_ROOT}%{_unitdir}/%{name}.service
%{__install} -D -p %{SOURCE5} ${RPM_BUILD_ROOT}%{_libexecdir}/%{name}/%{name}-locate-java.sh
%{__install} -D -p %{SOURCE6} ${RPM_BUILD_ROOT}%{_libexecdir}/%{name}/%{name}-run.sh
%{__install} -D -p %{SOURCE7} ${RPM_BUILD_ROOT}%{homedir}/doc/RUNNING.txt

%{__install} -D tomcat.sysusers.conf ${RPM_BUILD_ROOT}%{_sysusersdir}/tomcat.conf

%{__install} -d ${RPM_BUILD_ROOT}%{userinstancedir}/conf
%{__install} -D -p %{SOURCE8} ${RPM_BUILD_ROOT}%{_bindir}/tomcat-user-instance-create
%{__install} -D -p %{SOURCE9} ${RPM_BUILD_ROOT}%{userinstancedir}/bin/setenv.sh

asciidoctor -b manpage -D ${RPM_BUILD_ROOT}%{_mandir}/man1 -o tomcat-user-instance-create.1 %{SOURCE10}

for jar in output/build/lib/*.jar; do
    # Skip Jar if empty, applies to tomcat-coyote-ffm.jar atm since it requires to be built with Java>=23
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
%mvn_package ":tomcat-bootstrap" tomcat-common
%mvn_package ":tomcat-juli" tomcat-common

%mvn_install

# Fixes JAR must have Javapackages-GroupId manifest attribute error
jar ufm ${RPM_BUILD_ROOT}%{libdir}/el-api.jar <(echo "JavaPackages-GroupId: org.apache.tomcat")
jar ufm ${RPM_BUILD_ROOT}%{libdir}/jsp-api.jar <(echo "JavaPackages-GroupId: org.apache.tomcat")
jar ufm ${RPM_BUILD_ROOT}%{libdir}/servlet-api.jar <(echo "JavaPackages-GroupId: org.apache.tomcat")

# move things into place
pushd output/build
    rm -f bin/daemon.sh
    %{__cp} -ap bin/* ${RPM_BUILD_ROOT}%{bindir}
    %{__cp} -ap conf/*.{policy,properties,xml} ${RPM_BUILD_ROOT}%{confdir}
    %{__cp} -ap conf/*.{policy,properties,xml} ${RPM_BUILD_ROOT}%{userinstancedir}/conf
    %{__cp} -ap webapps/* ${RPM_BUILD_ROOT}%{appdir}
popd

ln -sr $(build-classpath ecj/ecj) ${RPM_BUILD_ROOT}%{libdir}/ecj-x.jar
ln -sr $(build-classpath tomcat-jakartaee-migration/jakartaee-migration) ${RPM_BUILD_ROOT}%{libdir}/jakartaee-migration-x.jar
ln -sr $(build-classpath apache-commons-compress/commons-compress) ${RPM_BUILD_ROOT}%{libdir}/commons-compress.jar
ln -sr $(build-classpath apache-commons-io/commons-io) ${RPM_BUILD_ROOT}%{libdir}/commons-io.jar
ln -sr $(build-classpath bcel/bcel) ${RPM_BUILD_ROOT}%{libdir}/bcel.jar
ln -sr $(build-classpath apache-commons-lang3/commons-lang3) ${RPM_BUILD_ROOT}%{libdir}/commons-lang3.jar

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
%license LICENSE
%{homedir}/doc/RUNNING.txt
%{_unitdir}/%{name}.service
%{_libexecdir}/%{name}/tomcat-run.sh
%{_sysusersdir}/tomcat.conf
%{baseconfdir}
%{baselogdir}
%{workdir}
%attr(2770,tomcat,adm) %dir %{logdir}
%attr(750,tomcat,tomcat) %dir %{cachedir}
%attr(2775,tomcat,tomcat) %dir %{appdir}
%attr(2775,tomcat,tomcat) %dir %{appdir}-javaee

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

%files user-instance
%license LICENSE
%{userinstancedir}
%{_bindir}/tomcat-user-instance-create
%{_mandir}/man1/tomcat-user-instance-create.1*

%files common -f .mfiles-tomcat-common
%license LICENSE
%doc {NOTICE,RELEASE-NOTES}
%{_libexecdir}/%{name}/tomcat-locate-java.sh
%{homedir}/bin

%files lib -f .mfiles
%license LICENSE
%{homedir}/lib
%{libdir}/jakartaee-migration-x.jar
%{libdir}/commons-compress.jar
%{libdir}/commons-io.jar
%{libdir}/bcel.jar
%{libdir}/commons-lang3.jar
%{libdir}/ecj-x.jar
%exclude %{libdir}/tomcat-jni.pom

%files admin-webapps
%license LICENSE
%{appdir}/host-manager
%{appdir}/manager

%files docs-webapp
%license LICENSE
%{appdir}/docs

%files webapps
%license LICENSE
%{appdir}/ROOT

%files jsp-%{jspspec}-api -f .mfiles-tomcat-jsp-api
%license LICENSE

%files servlet-%{servletspec}-api -f .mfiles-tomcat-servlet-api
%license LICENSE

%files el-%{elspec}-api -f .mfiles-tomcat-el-api
%license LICENSE

%changelog
%autochangelog
