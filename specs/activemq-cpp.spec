Name:           activemq-cpp
Version:        3.9.5
Release:        3%{?dist}
Summary:        C++ implementation of JMS-like messaging client

License:        Apache-2.0
URL:            http://activemq.apache.org/cms/
Source0:        http://www.apache.org/dist/activemq/activemq-cpp/%{version}/activemq-cpp-library-%{version}-src.tar.gz
Patch:          activemq-cpp-3.8.2-system-zlib.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  apr-util-devel >= 1.3
BuildRequires:  cppunit-devel >= 1.10.2
BuildRequires:  libuuid-devel

%description
activemq-cpp is a JMS-like API for C++ for interfacing with Message
Brokers such as Apache ActiveMQ.  C++ messaging service helps to make your
C++ client code much neater and easier to follow. To get a better feel for
CMS try the API Reference.
ActiveMQ-CPP is a client only library, a message broker such as Apache
ActiveMQ is still needed for your clients to communicate.

%package devel
Summary:        C++ implementation header files for JMS-like messaging
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       libuuid-devel

%description devel
activemq-cpp is a JMS-like API for C++ for interfacing with Message
Brokers such as Apache ActiveMQ.  C++ messaging service helps to make
your C++ client code much neater and easier to follow. To get a better
feel for CMS try the API Reference.  ActiveMQ-CPP is a client only
library, a message broker such as Apache ActiveMQ is still needed
for your clients to communicate.

%{name}-devel contains development header files.


%prep
%autosetup -n activemq-cpp-library-%{version} -p1
rm -r src/main/decaf/internal/util/zip
chmod 644 LICENSE.txt
chmod 644 src/main/activemq/transport/mock/MockTransport.cpp

%configure --disable-static


%build
%make_build


%install
%make_install
rm %{buildroot}%{_libdir}/lib%{name}.la
rm %{buildroot}%{_bindir}/example


%check
make check

%ldconfig_scriptlets


%files
%{_libdir}/lib%{name}.so.*
%license LICENSE.txt
%doc NOTICE.txt README.txt RELEASE_NOTES.txt


%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}-%{version}
%{_libdir}/pkgconfig/%{name}.pc
%{_bindir}/activemqcpp-config


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 03 2024 Jonathan Wright <jonathan@almalinux.org> - 3.9.5-1
- Unorphan package
- Update to 3.9.5
- Overhaul spec file

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Steve Traylen <steve.traylen@cern.ch> - 3.9.4-1
- New from upstream
- Add patch for openssl1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.8.4-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Mar 11 2015 Steve Traylen <steve.traylen@cern.ch> - 3.8.4-1
- Upstream to 3.8.4

* Wed Aug 27 2014 Steve Traylen <steve.traylen@cern.ch> - 3.8.3-1
- Upstream to 3.8.3

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Ville Skyttä <ville.skytta@iki.fi> - 3.8.2-2
- Patch to use system zlib instead of bundled one

* Thu Jan 23 2014 Steve Traylen <steve.traylen@cern.ch> - 3.8.2-1
- Upstream to 3.8.2

* Wed Sep 4 2013 Steve Traylen <steve.traylen@cern.ch> - 3.7.1-1
- Upstream to 3.7.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 16 2012 Steve Traylen <steve.traylen@cern.ch> - 3.4.4-1
- Upstream to 3.4.4

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for c++ ABI breakage

* Sun Feb 12 2012 Steve Traylen <steve.traylen@cern.ch> - 3.4.1-1
- Upstream to 3.4.1
- Add patch for gcc47, AMQCPP-389

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 10 2011 Steve Traylen <steve.traylen@cern.ch> - 3.4.0-1
- Upstream to 3.4.0

* Mon Apr 18 2011 Steve Traylen <steve.traylen@cern.ch> - 3.3.0-1
- Upstream to 3.3.0

* Mon Mar 7 2011 Steve Traylen <steve.traylen@cern.ch> - 3.2.5-1
- autoconf step removed.
- Upstream to 3.2.5

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 6 2011 Steve Traylen <steve.traylen@cern.ch> - 3.2.4-1
- Upstream to 3.2.4

* Wed Nov 10 2010 Steve Traylen <steve.traylen@cern.ch> - 3.2.3-1
- Upstream to 3.2.3

* Thu Jul 22 2010 Steve Traylen <steve.traylen@cern.ch> - 3.2.1-1
- Upstream to 3.2.1
- Add BR of openssl-devel since library now supports ssl 
  connections.

* Sat Apr 3 2010 Steve Traylen <steve.traylen@cern.ch> - 3.1.2-1
- Upstream to 3.1.2

* Sat Jan 9 2010 Steve Traylen <steve.traylen@cern.ch> - 3.1.0-1
- Upstream to 3.1.0

* Fri Dec 11 2009 Steve Traylen <steve.traylen@cern.ch> - 3.0.1-1
- Upstream to 3.0.1
- Tar ball name change.

* Fri Dec 11 2009 Steve Traylen <steve.traylen@cern.ch> - 2.2.6-5
- Add libuuid-devel as Requires to -devel package.

* Sat Nov 14 2009 Steve Traylen <steve.traylen@cern.ch> - 2.2.6-4
- Remove patch to relocate headers from versioned directory.
- Add make smp options to make check.

* Fri Nov 6 2009 Steve Traylen <steve.traylen@cern.ch> - 2.2.6-3
- Relocate headers to non versioned directory with patch0

* Fri Nov 6 2009 Steve Traylen <steve.traylen@cern.ch> - 2.2.6-2
- Adapted to Fedora guidelines.

* Thu Feb 26 2009 Ricardo Rocha <ricardo.rocha@cern.ch> - 2.2.6-1
- First version of the spec file


