%bcond cifs   0
%bcond ftp    0
%bcond hadoop 0
%bcond mina   0

Name:           apache-commons-vfs
Version:        2.9.0
Release:        %autorelease
Summary:        Commons Virtual File System
License:        Apache-2.0
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

URL:            https://commons.apache.org/proper/commons-vfs/
VCS:            git:https://github.com/apache/commons-vfs.git
Source0:        https://archive.apache.org/dist/commons/vfs/source/commons-vfs-%{version}-src.tar.gz
Source1:        https://archive.apache.org/dist/commons/vfs/source/commons-vfs-%{version}-src.tar.gz.asc
Source2:        https://downloads.apache.org/commons/KEYS

# Migrate from the old commons-httpclient, which is no longer available in
# Fedora, to the newer httpcomponents httpclient.
Patch:          %{name}-httpclient.patch

BuildRequires:  gnupg2
BuildRequires:  maven-local
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.sun.mail:jakarta.mail)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(commons-net:commons-net)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-collections4)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore-nio)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-core)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-slf4j-impl)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:  mvn(org.apache.sshd:sshd-core)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk16)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)
%if %{with hadoop}
BuildRequires:  mvn(javax.ws.rs:jsr311-api)
BuildRequires:  mvn(org.apache.hadoop:hadoop-common)
BuildRequires:  mvn(org.apache.hadoop:hadoop-hdfs)
BuildRequires:  mvn(org.apache.hadoop:hadoop-hdfs-client)
%endif
%if %{with ftp}
BuildRequires:  mvn(org.apache.ftpserver:ftpserver-core)
%endif
%if %{with cifs}
BuildRequires:  mvn(jcifs:jcifs)
%endif
%if %{with mina}
BuildRequires:  mvn(org.apache.mina:mina-core)
%endif

Provides:       %{name}2 = %{version}-%{release}

%description
Commons VFS provides a single API for accessing various file systems.
It presents a uniform view of the files from various sources, such as
the files on local disk, on an HTTP server, or inside a Zip archive.

Some of the features of Commons VFS are:
* A single consistent API for accessing files of different types.
* Support for numerous file system types.
* Caching of file information.  Caches information in-JVM, and
  optionally can cache remote file information on the local file
  system (replicator).
* Event delivery.
* Support for logical file systems made up of files from various file
  systems.
* Utilities for integrating Commons VFS into applications, such as a
  VFS-aware ClassLoader and URLStreamHandlerFactory.
* A set of VFS-enabled Ant tasks.

%package       ant
Summary:       Development files for Commons VFS
Requires:      %{name} = %{version}-%{release}
Requires:      ant

%description   ant
This package enables support for the Commons VFS ant tasks.

%package       examples
Summary:       Commons VFS Examples
Requires:      %{name} = %{version}-%{release}

%description   examples
VFS is a Virtual File System library - Examples.

%package       project
Summary:       Commons VFS Parent POM

%description   project
Commons VFS Parent POM.

%{?javadoc_package}

%prep
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -n commons-vfs-%{version} -p1

%conf
# Not needed for RPM builds
%pom_xpath_remove //pom:reporting
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :japicmp-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-project-info-reports-plugin
%pom_remove_plugin :spotbugs-maven-plugin

# Disable unwanted module
%pom_disable_module commons-vfs2-distribution

# Fix ant gId
%pom_change_dep -r :ant org.apache.ant:

# Remove webdav client (jackrabbit not packaged)
%pom_remove_dep -r org.apache.jackrabbit:
%pom_disable_module commons-vfs2-jackrabbit1
%pom_disable_module commons-vfs2-jackrabbit2

# Remove http3 client.  It needs the old commons-httpclient, which is no
# longer available in Fedora.  We support the http4 client.
%pom_remove_dep -r commons-httpclient:commons-httpclient
rm -r commons-vfs2/src/{main,test}/java/org/apache/commons/vfs2/provider/http
rm -r commons-vfs2/src/{main,test}/java/org/apache/commons/vfs2/provider/https

# Remove http5 client (httpclient5 not packaged)
%pom_remove_dep -r org.apache.httpcomponents.client5:httpclient5
rm -r commons-vfs2/src/{main,test}/java/org/apache/commons/vfs2/provider/http5
rm -r commons-vfs2/src/{main,test}/java/org/apache/commons/vfs2/provider/http5s

# hadoop has been retired
%if %{without hadoop}
%pom_remove_dep -r org.apache.hadoop
%pom_remove_dep -r javax.ws.rs
rm -r commons-vfs2/src/{main,test}/java/org/apache/commons/vfs2/provider/hdfs
%endif

# ftpserver is not available
%if %{without ftp}
%pom_remove_dep -r :ftpserver-core
rm -r commons-vfs2/src/{main,test}/java/org/apache/commons/vfs2/provider/ftps
%endif

# jcifs not packaged and also export controlled in the US
%if %{without cifs}
%pom_remove_dep :jcifs
%endif

# mina is not available
%if %{without mina}
%pom_remove_dep :mina-core
%endif

# Fix installation directory and symlink
%mvn_file :commons-vfs2 %{name}
%mvn_file :commons-vfs2 %{name}2
%mvn_file :commons-vfs2 commons-vfs
%mvn_file :commons-vfs2 commons-vfs2
%mvn_file :commons-vfs2-examples %{name}-examples
%mvn_file :commons-vfs2-examples %{name}2-examples
%mvn_file :commons-vfs2-examples commons-vfs-examples
%mvn_file :commons-vfs2-examples commons-vfs2-examples

%mvn_alias :commons-vfs2 "org.apache.commons:commons-vfs" "commons-vfs:commons-vfs"
%mvn_alias :commons-vfs2-examples "org.apache.commons:commons-vfs-examples" "commons-vfs:commons-vfs-examples"

%build
%mvn_build -sf

%install
%mvn_install

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "ant commons-logging commons-vfs" > commons-vfs
install -p -m 644 commons-vfs %{buildroot}%{_sysconfdir}/ant.d/commons-vfs

%files -f .mfiles-commons-vfs2
%doc README.md RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt

%files examples -f .mfiles-commons-vfs2-examples

%files project -f .mfiles-commons-vfs2-project
%license LICENSE.txt NOTICE.txt

%files ant
%config(noreplace) %{_sysconfdir}/ant.d/commons-vfs

%changelog
%autochangelog
