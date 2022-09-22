Name: rudiments
Version: 1.3.1
Release: 6%{?dist}
Summary: C++ class library for developing systems and applications

# Library source code is LGLPv2.
License: LGPLv2
URL: http://rudiments.sourceforge.net
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc-c++, libedit-devel, pcre-devel, openssl-devel, libcurl-devel, krb5-devel, httpd-devel

%description
A C++ class library for developing systems and applications.  Rudiments includes
frameworks for processes, threads, clients, servers, loggers and compilers.  It
also includes data structures for buffers, arrays, linked lists and
dictionaries, and utility classes for processing text and binary data, regular
expressions, random numbers, encryption, date and time, system information,
files, directories, file-systems, inter-process communication, dynamic
libraries, and XML.


%package devel
License: LGPLv2
Summary: Development files for rudiments
Requires: %{name}%{?_isa} = %{version}-%{release}, libedit-devel, openssl-devel, libcurl-devel, krb5-devel, httpd-devel

%description devel
Development files for rudiments.

%package doc
# Documentation is GPLv2 except for example code in the documentation.
# Example code is FSFUL.
License: GPLv2 and FSFUL
Summary: Documentation for rudiments
BuildArch: noarch

%description doc
Documentation for rudiments.


%prep
%autosetup -p1

%build
chmod -x include/rudiments/private/permissions.h
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# create tmpfiles.d directories and config file
mkdir -p %{buildroot}/run/%{name}
mkdir -p %{buildroot}%{_tmpfilesdir}
echo "d /run/%{name} 0777 root root -" > %{buildroot}%{_tmpfilesdir}/%{name}.conf

%files
%{_libdir}/librudiments.so.7
%{_libdir}/librudiments.so.7.*
%{_libdir}/librudiments-apache.so.7
%{_libdir}/librudiments-apache.so.7.*
%doc AUTHORS ChangeLog
%exclude %{_libdir}/librudiments.la
%exclude %{_libdir}/librudiments-apache.la
%if 0%{?fedora}
%license COPYING
%exclude %{_datadir}/licenses/rudiments
%else
%{_datadir}/licenses/rudiments
%endif
%{_tmpfilesdir}/%{name}.conf
%exclude %{_localstatedir}/run

%files devel
%{_includedir}/rudiments
%{_libdir}/librudiments.so
%{_libdir}/librudiments-apache.so
%{_bindir}/rudiments-config
%{_libdir}/pkgconfig/rudiments.pc
%{_mandir}/man1/rudiments-config*

%files doc
%{_docdir}/%{name}

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.3.1-4
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 David Muse <david.muse@firstworks.com> - 1.3.1-1
- Updated to version 1.3.1.
- Added apache-realated packages to BuildRequires.

* Mon Aug 17 2020 David Muse <david.muse@firstworks.com> - 1.3.0-1
- Updated to version 1.3.0.
- Added tmpfiles.d configuration.
- Added librudiments-apache libraries.

* Mon Aug 12 2019 David Muse <david.muse@firstworks.com> - 1.2.2-1
- Updated to version 1.2.2.

* Wed May 22 2019 David Muse <david.muse@firstworks.com> - 1.2.1-1
- Updated to version 1.2.1.

* Wed Feb 20 2019 David Muse <david.muse@firstworks.com> - 1.2.0-1
- Removed globbing of library major version.
- Removed calls to /sbin/ldconfig.
- Updated to version 1.2.0.

* Wed Sep 05 2018 David Muse <david.muse@firstworks.com> - 1.1.0-1
- Updated to version 1.1.0.
- Added gcc-c++ to BuildRequires.

* Fri Sep 08 2017 David Muse <david.muse@firstworks.com> - 1.0.7-1
- Updated to version 1.0.7.

* Fri Sep 01 2017 David Muse <david.muse@firstworks.com> - 1.0.6-1
- Updated to version 1.0.6.

* Fri May 12 2017 David Muse <david.muse@firstworks.com> - 1.0.5-1
- Updated to version 1.0.5.

* Tue Feb 21 2017 David Muse <david.muse@firstworks.com> - 1.0.4-1
- Added fedora dist-tag conditional.
- Replaced readline with libedit.

* Wed Jan 25 2017 David Muse <david.muse@firstworks.com> - 1.0.4-1
- Updated to version 1.0.4.

* Fri Jan 20 2017 David Muse <david.muse@firstworks.com> - 1.0.3-1
- Updated to version 1.0.3.
- Removed call to make uninstall-license.
- Added a directive to exclude licenses installed by make install.
- Added Requires to devel subpackage.
- Escaped percent sign in changelog.

* Sun Dec 25 2016 David Muse <david.muse@firstworks.com> - 1.0.2-1
- Updated to version 1.0.2.
- Replaced buildroot macro in comment with (buildroot).

* Fri Dec 23 2016 David Muse <david.muse@firstworks.com> - 1.0.1-1
- Updated to version 1.0.1.
- Removed "parsers" from description text.
- Removed Requires from doc package.

* Tue Jul 26 2016 David Muse <dmuse@firstworks.com> - 0.56.0-1
- Added readline dependency

* Wed Dec 16 2015 David Muse <dmuse@firstworks.com> - 0.55.0-1
- Added krb5 dependencies
- Updated shared library name to reflect libtool versioning scheme.

* Tue Oct 06 2015 David Muse <dmuse@firstworks.com> - 0.54-1
- Added libcurl dependencies
- Removed mention of test/build-script licenses
- Made doc rpm noarch

* Fri Sep 25 2015 David Muse <dmuse@firstworks.com> - 0.53-4
- License updates

* Thu Sep 17 2015 Jens Lody <fedora@jenslody.de> - 0.53-3
- Added doc-package
- Removed obsolete cleaning of buildroot
- Removed docdir= from make install

* Fri Sep  11 2015 David Muse <dmuse@firstworks.com> - 0.53-2
- More Fedora Naming/Packaging/Review Guidelines compliance updates.
- configure patch for fedora 23

* Fri Aug  28 2015 David Muse <dmuse@firstworks.com> - 0.53-1
- Fedora Naming/Packaging/Review Guidelines compliance updates.

* Fri Jan  31 2003 David Muse <dmuse@firstworks.com>
- Made it so it could be distributed with rudiments.
- Added devel.

* Fri May  3 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Mon Apr 15 2002 Matthias Saou <matthias.saou@est.une.marmotte.net> 0.24-fr1
- Update to 0.24 at last.

* Wed May 16 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial RPM release.

