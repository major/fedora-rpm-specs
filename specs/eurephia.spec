Name:           eurephia
Version:        1.1.1
Release:        15%{?betatag:.%{betatag}}%{?dist}.1
Summary:        An advanced and flexible OpenVPN user authentication plug-in

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.eurephia.net/
Source0:        http://downloads.sourceforge.net/project/eurephia/eurephia/v1.1/%{name}-%{version}%{?betatag:_%{betatag}}.tar.xz
Patch0:         0001-Fix-GCC-10-compiler-issues-fcommon-and-fPIC.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}{?betatag:_%{betatag}}-root-%(%{__id_u} -n)

BuildRequires:  libxml2-devel libxslt-devel openssl-devel
%if 0%{?rhel} > 5
BuildRequires:  cmake3 >= 3.13
%endif
%if 0%{?fedora} > 28
BuildRequires:  cmake >= 3.13
%endif
BuildRequires:  sqlite-devel >= 3.0.0
BuildRequires:  openvpn-devel
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires: make
Requires:       openvpn
Requires:       eurephia-sqlite3 = %{version}-%{release}
Provides:       eurephia-iptables >= 1.0.1-2

%description
This plug-in enhances OpenVPN by adding user name and password
authentication in addition. An eurephia user account is a combination of
minimum one OpenVPN SSL certificate and a user name with a password
assigned. It is also possible to setup several eurephia user names to use
a shared OpenVPN certificate.

In addition, eurephia will blacklist IP addresses, certificates and user names
on too many failed attempts and it supports dynamic update of iptables rules
which restricts network access per connection.

%package sqlite3
Summary: The eurephia SQLite3 database driver

%description sqlite3
This package contains the SQLite3 database driver for eurephia

%package admin
Summary: The eurephia command line administration utility
Requires: eurephia-sqlite3 = %{version}-%{release}

%description admin
This package contains the command line utility to administer and configure
eurephia

%package init
Summary: Utility for initializing a new eurephia database
Requires: eurephia-sqlite3 = %{version}-%{release}

%description init
This package provides a program which will initialize the eurephia
database for you.  It will guide you through several questions and
save the configuration in the database.  When you have configured
and initialized eurephia, this package should be removed from the
system.

%package utils
Summary: Misc. eurephia utilities

%description utils
This package contains useful utilities when debugging eurephia.
At the moment you will only find eurephia_saltdecode in this
package, which will provide some information about the password
hash salt.


%prep
%setup -q -n %{name}-%{version}%{?betatag:_%{betatag}}
%patch -P0 -p1

%build
%if 0%{?rhel} > 5
%define cmake_bin cmake3
%endif
%if 0%{?fedora} > 28
%define cmake_bin cmake
%endif

# The configure script is not an autotools script, but a cmake wrapper script.
CFLAGS="%{optflags} -std=gnu89" ./configure --prefix %{_prefix} --bin-dir %{_bindir} --xslt-path %{_datadir}/eurephia/xslt --plug-in-dir %{_libdir}/eurephia --plug-in --openvpn-src /usr/include --fw-iptables --db-sqlite3 --sqlite3-path %{_localstatedir}/lib/eurephia --eurephiadm --cmake-bin %{cmake_bin}

# We need to build eurephiacommon first, to avoid issues with parallel building
# the rest of eurephia
%{__make} VERBOSE=1 eurephiacommon
%{__make} VERBOSE=1

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Move the eurephia-auth.so file to the default OpenVPN plug-in directory
mkdir -p -m 755 %{buildroot}/%{_libdir}/openvpn
mv %{buildroot}/%{_libdir}/eurephia/eurephia-auth.so %{buildroot}/%{_libdir}/openvpn/

# These files are not installed by default, but we want to package them for Fedora/RHEL
install -p -m 755 utils/eurephia_init %{buildroot}/%{_bindir}
install -p -m 755 utils/eurephia_saltdecode %{buildroot}/%{_bindir}
install -p -m 644 utils/eurephia_init.7 %{buildroot}/%{_mandir}/man7/
install -p -m 644 utils/eurephia_saltdecode.7 %{buildroot}/%{_mandir}/man7/

%clean
rm -rf %{buildroot}


%files
%doc LICENSE.txt CREDITS.txt
%{_libdir}/openvpn/eurephia-auth.so
%{_mandir}/man7/eurephia-auth.7.gz
%{_mandir}/man7/eurephia-variables.7.gz
%{_libdir}/eurephia/efw-iptables.so

%files sqlite3
%doc LICENSE.txt CREDITS.txt
%dir %{_libdir}/eurephia/
%{_libdir}/eurephia/edb-sqlite.so
%{_localstatedir}/lib/eurephia/
%{_mandir}/man7/edb-sqlite.7.gz

%files init
%doc LICENSE.txt CREDITS.txt
%{_bindir}/eurephia_init
%{_mandir}/man7/eurephia_init.7.gz

%files admin
%doc LICENSE.txt CREDITS.txt
%{_bindir}/eurephiadm
%dir %{_datadir}/eurephia/
%dir %{_datadir}/eurephia/xslt
%{_datadir}/eurephia/xslt/eurephiadm
%{_mandir}/man7/eurephiadm.7.gz
%{_mandir}/man7/eurephiadm-*.7.gz

%files utils
%doc LICENSE.txt CREDITS.txt
%{_bindir}/eurephia_saltdecode
%{_mandir}/man7/eurephia_saltdecode.7.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-15.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.1-14.1
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.1.1-7
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 2020 David Sommerseth <dazo@eurephia.org> - 1.1.1-3
- Fix GCC 10 build issues (RHBZ#1799330)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 09 2019 David Sommerseth <dazo@eurephia.org> - 1.1.1-1
- Update to latest upstream release
- Fix FTBFS issues (RHBZ#1735198)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 David Sommerseth <davids@redhat.com> - 1.1.0-11
- Fix build issues with GCC 5.  Enforce -std=gnu89 for now.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 28 2013 David Sommerseth <dazo@users.sourceforge.net> - 1.1.0-7
- Removed superfluous Obsolete tag.  This is not relevant any more in Fedora.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 19 2012 David Sommerseth <dazo@users.sourceforge.net> - 1.1.0-4
- Added upstream fixes

* Tue Oct  9 2012 David Sommerseth <dazo@users.sourceforge.net> - 1.1.0-3
- Hack to make it build on Fedora 16+

* Tue Oct  9 2012 David Sommerseth <dazo@users.sourceforge.net> - 1.1.0-2
- Corrected wrong download URL for eurephia v1.1 source code

* Tue Oct  9 2012 David Sommerseth <dazo@users.sourceforge.net> - 1.1.0-1
- Corrected wrong download URL for eurephia v1.1 source code

* Tue Oct  9 2012 David Sommerseth <dazo@users.sourceforge.net> - 1.1.0-1
- Updated to upstream v1.1.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 20 2010 David Sommerseth <dazo@users.sourceforge.net> - 1.0.1-2
- Obsolete the eurephia-iptables RPM and move efw-iptables into eurephia.rpm

* Thu Jul 15 2010 David Sommerseth <davids@redhat.com> - 1.0.0-8
- Fixed silly mistakes
  - Forgot to move over /usr/lib/eurephia from eurephia to eurephia-sqlite3
  - Double '=' in eurephia-init

* Thu Jul 15 2010 David Sommerseth <davids@redhat.com> - 1.0.0-7
- More review fixes
  - Relocated ownership of directories
  - Don't hard-code version number in intra-package deps
  - Use proper fully qualified version number (including revision)

* Thu Jul 15 2010 David Sommerseth <davids@redhat.com> - 1.0.0-6
- Fixed file duplication between eurephia and eurephia-admin

* Thu Jul 15 2010 David Sommerseth <davids@redhat.com> - 1.0.0-5
- More review comments from mattias.ellert@fysast.uu.se
  - Own /usr/lib{,64}/eurephia, /usr/share/eurephia/ and /usr/share/eurephia/xslt
  - Intra-packages use fully qualified versions

* Thu Jul 15 2010 David Sommerseth <davids@redhat.com> - 1.0.0-4
- Review comments from mattias.ellert@fysast.uu.se
  - Better way to copy source1
  - Removed -b0 from setup macro

* Thu Jul  8 2010 David Sommerseth <davids@redhat.com> - 1.0.0-3
- Added missing Group tags
- Added stricter cmake version requirement

* Thu Jul  8 2010 David Sommerseth <davids@redhat.com> - 1.0.0-2
- Added missing build dependency for openssl-devel

* Wed Jun 30 2010 David Sommerseth <dazo@users.sourceforge.net> - 1.0.0-1
- Updated and prepared for the eurephia-1.0.0 release

* Wed Nov 18 2009 David Sommerseth <dazo@users.sourceforge.net> - 0.9.6-1.beta
- Updated for eurephia-0.9.6_beta and using openvpn-2.1_rc21 source tree

* Tue Oct  6 2009 David Sommerseth <dazo@users.sourceforge.net> - 0.9.5-1.beta
- Initial eurephia spec file

