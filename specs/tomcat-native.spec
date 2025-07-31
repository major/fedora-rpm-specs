Name:           tomcat-native
Epoch:          1
Version:        2.0.8
Release:        %autorelease
Summary:        Tomcat native library

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://tomcat.apache.org/native-doc/index.html
Source0:        http://www.apache.org/dist/tomcat/tomcat-connectors/native/%{version}/source/%{name}-%{version}-src.tar.gz
ExclusiveArch: %{java_arches}

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
BuildRequires:  apr-devel
BuildRequires:  openssl-devel
# Upstream compatibility:
Provides:       tcnative = %{version}-%{release}

%description
Tomcat can use the Apache Portable Runtime to provide superior
scalability, performance, and better integration with native server
technologies.  The Apache Portable Runtime is a highly portable library
that is at the heart of Apache HTTP Server 2.x.  APR has many uses,
including access to advanced IO functionality (such as sendfile, epoll
and OpenSSL), OS level functionality (random number generation, system
status, etc), and native process handling (shared memory, NT pipes and
Unix sockets).  This package contains the Tomcat native library which
provides support for using APR in Tomcat.


%prep
%setup -q -n %{name}-%{version}-src
f=CHANGELOG.txt ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f


%build
cd native
export CFLAGS="${CFLAGS} -DOPENSSL_NO_ENGINE"
%configure \
    --with-apr=%{_bindir}/apr-1-config \
    --with-java-home=%{_jvmdir}/java
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make -C native install DESTDIR=$RPM_BUILD_ROOT
# Perhaps a devel package sometime?  Not for now; no headers are installed.
rm -f $RPM_BUILD_ROOT%{_libdir}/libtcnative*.*a
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig
rm -rf ${RPM_BUILD_ROOT}%{_includedir}/*.h


%ldconfig_scriptlets


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE NOTICE
%doc CHANGELOG.txt README.txt
# Note: unversioned *.so needed here due to how Tomcat loads the lib :(
%{_libdir}/libtcnative*.so*


%changelog
%autochangelog
