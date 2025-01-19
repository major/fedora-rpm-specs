%global aprversion 1
%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn || echo 0-0)}}

%global commit 1200598c92c2ef7990b64d3f30f26c9fe1c25c35
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gridsite
Version:        3.0.0
Release:        0.32.20240125git%{shortcommit}%{?dist}
Summary:        Grid Security for the Web, Web platforms for Grids

#  - src/gsexec.c ASL 2.0 (not used)
#  - src/gsexec.h ASL 2.0 (not used)
#  - src/mod_gridsite.c BSD but includes ASL 2.0 based code.
#  - src/mod_ssl-private.h BSD but includes ASL 2.0 based code.
# All other files are BSD
License:        Apache-2.0 AND BSD-2-Clause
URL:            http://www.gridsite.org
Source0:        https://github.com/CESNET/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        gridsite-httpd.conf
Source2:        gridsitehead.txt
Source3:        gridsitefoot.txt
Source4:        root-level.gacl
Source5:        gridsitelogo.png

BuildRequires:  make
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel
BuildRequires:  httpd-devel
BuildRequires:  doxygen
BuildRequires:  openssl-devel >= 1.1
BuildRequires:  gsoap-devel
BuildRequires:  canl-c-devel >= 3.0.0
BuildRequires:  libtool

Requires:       httpd-mmn = %{_httpd_mmn}
Requires:       mod_ssl
Requires:       gridsite-libs = %{version}-%{release}

Provides:       gridsite-apache = %{version}-%{release}
Obsoletes:      gridsite-apache <= 1.7.20
Provides:       gridsite-services = %{version}-%{release}
Obsoletes:      gridsite-services <= 1.7.20

%description
GridSite was originally a web application developed for managing and formatting
the content of the http://www.gridpp.ac.uk/ website. Over the past years it
has grown into a set of extensions to the Apache web server and a toolkit for
Grid credentials, GACL access control lists and HTTP(S) protocol operations.

This package gridsite contains apache httpd modules for enabling
mod_gridsite.


%package  libs
Summary:  Run time libraries for mod_gridsite and gridsite-clients

%description libs
GridSite was originally a web application developed for managing and formatting
the content of the http://www.gridpp.ac.uk/ website. Over the past years it
has grown into a set of extensions to the Apache web server and a toolkit for
Grid credentials, GACL access control lists and HTTP(S) protocol operations.

This package contains the runtime libraries.


%package  clients
Summary:  Clients to gridsite including htcp, htrm, htmv
Requires: gridsite-libs = %{version}-%{release}
Provides: gridsite-commands = %{version}-%{release}
Obsoletes:gridsite-commands <= 1.7.20

%description  clients
GridSite was originally a web application developed for managing and formatting
the content of the http://www.gridpp.ac.uk/ website. Over the past years it
has grown into a set of extensions to the Apache web server and a toolkit for
Grid credentials, GACL access control lists and HTTP(S) protocol operations.

This package gridsite-clients, contains clients for using against gridsite,
htcp, htrm, ...


%package  devel
Summary:  Developers tools for gridsite
Requires: gridsite-libs = %{version}-%{release}
Requires: openssl-devel

%description  devel
GridSite was originally a web application developed for managing and formatting
the content of the http://www.gridpp.ac.uk/ website. Over the past years it
has grown into a set of extensions to the Apache web server and a toolkit for

This package gridsite-devel, contains developer tools for using gridsite.


%package   doc
Summary:   Developers Documentation for gridsite
BuildArch: noarch

%description  doc
GridSite was originally a web application developed for managing and formatting
the content of the http://www.gridpp.ac.uk/ website. Over the past years it
has grown into a set of extensions to the Apache web server and a toolkit for

This package gridsite-doc, contains developer documentation for gridsite.


%prep
%setup -q -n %{name}-%{commit}
# Copy in apache configuration.
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .
cp -p %{SOURCE4} .
cp -p %{SOURCE5} .


%build
(cd src && make prefix=%{_usr} CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}" HTTPD_FLAGS="-I%{_includedir}/httpd -I%{_includedir}/apr-%{aprversion}")


%install
(cd src && make install prefix=%{_usr} libdir=%{_lib} DESTDIR=%{buildroot})
(cd src && make install-ws prefix=%{_usr} libdir=%{_lib} DESTDIR=%{buildroot})

# change cgi scripts location
mkdir -p %{buildroot}%{_libexecdir}/gridsite/cgi-bin
mv %{buildroot}%{_sbindir}/*.cgi %{buildroot}%{_libexecdir}/gridsite/cgi-bin
rmdir %{buildroot}%{_sbindir}

# Remove static libs
rm  %{buildroot}/%{_libdir}/libgridsite.a
# Remove docs we don't want now but will move it in %%doc later.
rm -rf %{buildroot}/%{_defaultdocdir}
# Remove the built against globus-openssl libs since
# we don't actually do that.
rm  %{buildroot}/%{_libdir}/libgridsite_globus.*

# Set up a root area to serve files from.
mkdir -p %{buildroot}%{_var}/lib/gridsite
install -p -m 0644 gridsitehead.txt %{buildroot}%{_var}/lib/gridsite/gridsitehead.txt
install -p -m 0644 gridsitefoot.txt %{buildroot}%{_var}/lib/gridsite/gridsitefoot.txt
install -p -m 0644 root-level.gacl  %{buildroot}%{_var}/lib/gridsite/.gacl

mkdir -p %{buildroot}%{_sysconfdir}/grid-security/dn-lists

mkdir -p %{buildroot}%{_var}/cache/mod_gridsite
# Copy in apache configuration, we must name it zgridsite.conf
# so it is loaded after mod_ssl in ssl.conf.
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -p -m 0644 gridsite-httpd.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/zgridsite.conf

mkdir -p %{buildroot}%{_var}/www/icons
install -p -m 0644 gridsitelogo.png %{buildroot}%{_var}/www/icons

# These were work arounds for an old bug in some other
# software never ever in Fedora anyway.
rm -f %{buildroot}%{_libdir}/libgridsite_nossl*

# Add an empty /etc/grid-security/vomsdir since this gridsite version
# supports .lsc files.
mkdir -p %{buildroot}%{_sysconfdir}/grid-security/vomsdir


%ldconfig_scriptlets libs


%files
%{_libdir}/httpd/modules/mod_gridsite.so
%dir %{_libexecdir}/gridsite
%dir %{_libexecdir}/gridsite/cgi-bin
%{_libexecdir}/gridsite/cgi-bin/gridsite-delegation.cgi
%{_libexecdir}/gridsite/cgi-bin/real-gridsite-admin.cgi
%dir %{_var}/www/icons
%{_var}/www/icons/gridsitelogo.png
%dir %attr(0755,apache,apache) %{_var}/lib/gridsite
%dir %attr(0755,root,root) %{_sysconfdir}/grid-security
%dir %attr(0755,apache,apache) %{_sysconfdir}/grid-security/dn-lists
%dir %attr(0755,apache,apache) %{_var}/cache/mod_gridsite
%dir %{_sysconfdir}/grid-security/vomsdir

%{_mandir}/man8/mod_gridsite.8.*
%{_mandir}/man8/gridsite-*.8.*

%config(noreplace) %{_sysconfdir}/httpd/conf.d/zgridsite.conf
%config(noreplace) %attr(-,apache,apache) %{_var}/lib/gridsite/.gacl
%config(noreplace) %attr(-,apache,apache) %{_var}/lib/gridsite/gridsitehead.txt
%config(noreplace) %attr(-,apache,apache) %{_var}/lib/gridsite/gridsitefoot.txt

%license LICENSE

%doc doc/httpd-fileserver.conf doc/httpd-webserver.conf
%doc doc/httpd-storage.conf

%doc CHANGES

%files libs
%{_libdir}/libgridsite.so.6
%{_libdir}/libgridsite.so.6.*
%license LICENSE

%files  clients
%{_bindir}/findproxyfile
%{_bindir}/htcp
%{_bindir}/htfind
%{_bindir}/htll
%{_bindir}/htls
%{_bindir}/htmkdir
%{_bindir}/htmv
%{_bindir}/htping
%{_bindir}/htproxydestroy
%{_bindir}/htproxyinfo
%{_bindir}/htproxyput
%{_bindir}/htproxyrenew
%{_bindir}/htproxytime
%{_bindir}/htproxyunixtime
%{_bindir}/htrm
%{_bindir}/urlencode

%{_mandir}/man1/findproxyfile.1*
%{_mandir}/man1/htcp.1*
%{_mandir}/man1/htfind.1*
%{_mandir}/man1/htll.1*
%{_mandir}/man1/htls.1*
%{_mandir}/man1/htmkdir.1*
%{_mandir}/man1/htmv.1*
%{_mandir}/man1/htping.1*
%{_mandir}/man1/htproxydestroy.1*
%{_mandir}/man1/htproxyinfo.1*
%{_mandir}/man1/htproxyput.1*
%{_mandir}/man1/htproxyrenew.1*
%{_mandir}/man1/htproxytime.1*
%{_mandir}/man1/htproxyunixtime.1*
%{_mandir}/man1/htrm.1*
%{_mandir}/man1/urlencode.1*

%files devel
%{_includedir}/gridsite-gacl.h
%{_includedir}/gridsite.h
%{_libdir}/libgridsite.so
%{_libdir}/pkgconfig/*

%files doc
%license LICENSE
%doc src/doxygen


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.32.20240125git1200598
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 01 2024 František Dvořák <valtri@civ.zcu.cz> - 3.0.0-0.31.20240125git1200598
- Rebuild for new gsoap

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.30.20240125git1200598
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 František Dvořák <valtri@civ.zcu.cz> - 3.0.0-0.29.20240125git1200598
- Rebuild to fix release version

* Thu Jan 25 2024 František Dvořák <valtri@civ.zcu.cz> - 3.0.0-0.28.20230125git1200598
- New upstream snapshot (OpenSSL 3.1.4)
- Rebuild for new gsoap

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.27.20230214gitee81151
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.26.20230214gitee81151
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 14 2023 František Dvořák <valtri@civ.zcu.cz> - 3.0.0-0.25.20230214gitee81151
- Update license field to SPDX identifier
- New upstream snapshot

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.24.20180202git2fdbc6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 František Dvořák <valtri@civ.zcu.cz> - 3.0.0-0.23.20180202git2fdbc6f
- Rebuild for new gsoap

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.22.20180202git2fdbc6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.21.20180202git2fdbc6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.0.0-0.20.20180202git2fdbc6f
- Rebuilt with OpenSSL 3.0.0

* Sun Aug 22 2021 František Dvořák <valtri@civ.zcu.cz> - 3.0.0-0.19.20180202git2fdbc6f
- Rebuild for new gsoap

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.18.20180202git2fdbc6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.17.20180202git2fdbc6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.16.20180202git2fdbc6f
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.15.20180202git2fdbc6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.14.20180202git2fdbc6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Steve Traylen <steve.traylen@cern.ch> - 3.0.0-0.13.20180202git2fdbc6f
- Rebuild for new gsoap

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.12.20180202git2fdbc6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.11.20180202git2fdbc6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.10.20180202git2fdbc6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.9.20180202git2fdbc6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 František Dvořák <valtri@civ.zcu.cz> - 3.0.0-0.8.20180202git2fdbc6f
- Rebuild for new gsoap
- New upstream snapshot (compatibility with gSOAP >= 2.8.60)

* Fri Oct 13 2017 František Dvořák <valtri@civ.zcu.cz> - 3.0.0-0.7.20171013git2038a25
- New upstream snapshot (SSL 1.1 version of 2.3.4 release + QA patches)
- Simplify macro names

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.6.20170225gitd51b2fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-0.5.20170225gitd51b2fd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 František Dvořák <valtri@civ.zcu.cz> - 3.0.0-0.4.20170225gitd51b2fd
- Rebuild for new gsoap

* Sun Jun 25 2017 František Dvořák <valtri@civ.zcu.cz> - 3.0.0-0.3.20170225gitd51b2fd
- Rebuild for new gsoap

* Sat Feb 25 2017 František Dvořák <valtri@civ.zcu.cz> - 3.0.0-0.20170225gitd51b2fd
- Upstream 3.0.0 (development snapshot)
- Major version update
- OpenSSL 1.1 (fixed #1423689)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 26 2016 František Dvořák <valtri@civ.zcu.cz> - 2.3.2-2
- Removed gsexec obsolete
- Rebuild for new gsoap

* Tue Aug 16 2016 František Dvořák <valtri@civ.zcu.cz> - 2.3.2-1
- Upstream 2.3.2

* Fri Aug 05 2016 František Dvořák <valtri@civ.zcu.cz> - 2.3.1-1
- Upstream 2.3.1

* Tue Apr 19 2016 František Dvořák <valtri@civ.zcu.cz> - 2.2.6-4
- Rebuild for new gsoap

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 František Dvořák <valtri@civ.zcu.cz> - 2.2.6-2
- Using %%global in macros
- %%license tag

* Sat Jun 27 2015 František Dvořák <valtri@civ.zcu.cz> - 2.2.6-1
- Upstream to 2.2.6
- Removed curl patch merged upstream

* Tue Jun 16 2015 František Dvořák <valtri@civ.zcu.cz> - 2.2.5-4
- Rebuild for new gsoap

* Sun Jan 25 2015 František Dvořák <valtri@civ.zcu.cz> - 2.2.5-3
- Rebuild for new gsoap

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 František Dvořák <valtri@civ.zcu.cz> - 2.2.5-1
- Gridsite 2.2.5 Release, several bugfixes
- Patch to build with newer curl 7.37.1
- Removed cgi-bin-location.patch, move files in %%install instead
- Replace MYFLAGS by CFLAGS, removed gridsite internal build flags
- Owning icons dir
- Only major version needed in library wildcard now (libgridsite.so.2.*)
- Cleanups (EL5, noarch doc subpackage, buildroot macro, formatting)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 28 2014 Adrien Devresse <adevress@cern.ch>
- Gridsite 2.2.1 Release, fix issue related to TLS support in mod_gridsite

* Thu Jan 23 2014 Joe Orton <jorton@redhat.com> - 2.2.0-2
- fix _httpd_mmn expansion in absence of httpd-devel

* Wed Dec 18 2013 Steve Traylen <steve.traylen@cern.ch> - 2.2.0-1
- New upstream 2.2.0
- Source URL now changed to github project.
- Drop gridsite-httpd24_v3.patch since fixed upstream.

* Wed Oct 23 2013 Steve Traylen <steve.traylen@cern.ch> - 2.0.4-2
- Rebuild for new gsoap

* Thu Sep 19 2013 steve.traylen@cern.ch - 2.0.4-1
- Upstream to 2.0.4
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Adrien Devresse <adevress at cern.ch> - 1.7.25-2
 - Upstream to 1.7.25
 - Fix httpd 24 patch, remove a risk of segfault on >=EL6

* Sat Jan 26 2013 Kevin Fenzi <kevin@scrye.com> 1.7.21-4
- Rebuild for new gsoap

* Thu Sep 13 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 1.7.21-3
- Added patch for segfault under high load

* Mon Jul 16 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 1.7.21-2
- Rebuild with proper tarballs

* Mon Jul 16 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 1.7.21-1
- Upstream to 1.7.21, compliance with EMI project gridsite packaging
- Removed unused patches

* Mon Apr 16 2012 steve.traylen@cern.ch - 1.7.20-1
- Upstream to 1.7.20, Add gridsite-httpd24.patch

* Sun Mar 18 2012 Steve Traylen <steve.traylen@cern.ch>  - 1.7.19-1
- Upstream 1.7.19
- Drop EPEL4 support since EOL.
- Requires httpd-mmn, rhbz#803062

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 3 2011 Steve Traylen <steve.traylen@cern.ch>  - 1.7.16-1
- Upstream 1.7.16, drop compat package from .spec only.

* Wed Jul 6 2011 Steve Traylen <steve.traylen@cern.ch>  - 1.7.15-4
- devel package require openssl devel rhbz#719174

* Sun Jul 3 2011 Steve Traylen <steve.traylen@cern.ch>  - 1.7.15-3
- Correct dependency mistake.

* Thu Jun 30 2011 Steve Traylen <steve.traylen@cern.ch>  - 1.7.15-2
- Add a gridsite-compat-1.5 package on EPEL4 & EPEL5.
- Remove doc package requiring devel package.

* Thu Jun 30 2011 Steve Traylen <steve.traylen@cern.ch>  - 1.7.15-1
- Upstream 1.7.15, drop gridsite-include-1.7.9.patch since upstream,
  redo cgi-location patch.

* Mon Jun 27 2011 Steve Traylen <steve.traylen@cern.ch>  - 1.7.13-1
- Upstream 1.7.13

* Wed Apr 6 2011 Steve Traylen <steve.traylen@cern.ch>  - 1.7.12-1
- Upstream 1.7.12

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Steve Traylen <steve.traylen@cern.ch>  - 1.7.9-1
- Add empty /etc/grid-security/vomsdir since this gridsite
  support .lsc files.
- Upstream to 1.7.9
- Update gridsite-include.patch for 1.7.9
  https://savannah.cern.ch/bugs/index.php?69632

* Wed Sep 29 2010 jkeating - 1.5.19-2
- Rebuilt for gcc bug 634757

* Tue Sep 21 2010 Steve Traylen <steve.traylen@cern.ch> - 1.5.19-1
- Upstream to 1.5.19.
- Add gridsite-include.patch
  https://savannah.cern.ch/bugs/index.php?69632
  https://bugzilla.redhat.com/show_bug.cgi?id=612109
- Alter default .gacl
  https://bugzilla.redhat.com/show_bug.cgi?id=612187
- Change setuid binary from 4510 to 4754

* Thu May 20 2010 Steve Traylen <steve.traylen@cern.ch> - 1.5.18-4
- For .el4 use /usr/include/apr-0 rather than apr-1

* Wed May 19 2010 Steve Traylen <steve.traylen@cern.ch> - 1.5.18-3
- Don't use _sharedstatedir macro for .el4,5 support.

* Wed May 19 2010 Steve Traylen <steve.traylen@cern.ch> - 1.5.18-2
- Split docs of to a seperate package.
- License corrected to ASL 2.0 and BSD

* Mon May 17 2010 Steve Traylen <steve.traylen@cern.ch> - 1.5.18-1
- Initial package.


