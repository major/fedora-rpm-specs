Summary:   NSS library for MySQL
Name:      libnss-mysql
Version:   1.5
Release:   52%{?dist}
Source0:   http://prdownloads.sourceforge.net/libnss-mysql/libnss-mysql-%{version}.tar.gz
Source1:   README
Source2:   nsswitch.conf
Patch1:    libnss-mysql-multiarch.patch
Patch2:    libnss-mysql-mariadb10.2.patch
URL:       http://libnss-mysql.sourceforge.net
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:   GPL-2.0-or-later

BuildRequires: mariadb-connector-c-devel, libtool, autoconf, automake
BuildRequires: make
BuildRequires: authselect, authselect-libs

%description
Store your UNIX user accounts in MySQL. "libnss-mysql" enables the following:

* System-wide authentication and name service using a MySQL database.
  Applications do not need to be MySQL-aware or modified in any way.

* Storing authentication information in a database instead of text files.

* Creation of a single authentication database for multiple servers.
  This is often referred to as the "Single Sign-on" problem.

* Writing data-modification routines (IE self-management web interface).

libnss-mysql is similar to NIS or LDAP. It provides the same centralized
authentication service through a database. What does this mean? Username,
uid, gid, password, etc comes from a MySQL database instead of
/etc/password, /etc/shadow, and /etc/group. A user configured in MySQL will
look and behave just like a user configured in /etc/passwd. Your
applications such as ls, finger, sendmail, qmail, exim, postfix, proftpd,
X, sshd, etc. will all 'see' these users!

%prep
%autosetup -p1

%build
libtoolize -f
autoreconf -f -i
%configure
%make_build
# remove non linux samples
rm -rf sample/freebsd sample/solaris

%install
mkdir -p $RPM_BUILD_ROOT/{etc,lib}
%make_install

# install authselect files
%define authselect_vendor %{_datadir}/authselect/vendor/%{name}
mkdir -p $RPM_BUILD_ROOT%{authselect_vendor}
# Base on minimal or nis profile
if [ -d %{_datadir}/authselect/default/nis ]; then
  cp -ar %{_datadir}/authselect/default/nis/* \
    $RPM_BUILD_ROOT%{authselect_vendor}/
elif [ -d %{_datadir}/authselect/default/minimal ]; then
  cp -ar %{_datadir}/authselect/default/minimal/* \
    $RPM_BUILD_ROOT%{authselect_vendor}/
elif [ -d %{_datadir}/authselect/default/local ]; then
  cp -ar %{_datadir}/authselect/default/local/* \
    $RPM_BUILD_ROOT%{authselect_vendor}/
else
  echo "Missing authselect default profile!"
  exit 1
fi
cp -af %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{authselect_vendor}/

%ldconfig_scriptlets

%files
%exclude %{_libdir}/libnss_mysql.la
%exclude %{_libdir}/*.so
%{_libdir}/*.so.*
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/libnss-mysql.cfg
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/libnss-mysql-root.cfg
%doc README ChangeLog AUTHORS THANKS NEWS COPYING FAQ DEBUGGING UPGRADING TODO
%doc sample
%dir %{_datadir}/authselect/vendor/%{name}
%{_datadir}/authselect/vendor/%{name}/*

%changelog
* Wed Jan 08 2025 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-52
- Allow local authselect profile for EPEL10

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5-51
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 08 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-47
- Use mysql for initgroups nsswich.conf entry too

* Fri Sep 29 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-46
- Build against the 'mariadb-connector-c-devel' package (PR#1)
- Replace setup and patchN with autosetup macro
- Use make macros

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-41
- Allow building without nis profile (not present in epel9).

* Mon Dec 27 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-40
- Add authselect configuration.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-35
- Change mariadb-connector-c-devel to mariadb-devel (RHBZ#1495998)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-30
- Rebuild against mariadb-connector-c (rhbz#1493631)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-27
- Updated for MariaDB 10.2 (rhbz#1470133)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-22
- Install autoconf missing files.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-19
- added autoreconf to prep section (bz#925827)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 1.5-15
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Wed Mar 23 2011 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-14
- Rebuild agains new mysql

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-10
- added libtoolize -f and readded autoreconf -f

* Fri Jan 23 2009 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-9
- build fails with autoreconf, removed

* Fri Jan 23 2009 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-8
- rebuild against new mysql

* Sat Feb 9 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-7
- rebuild against gcc4.3

* Tue Nov 27 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-6
- updated buildroot according to packaging guidelines
- removed comment before ldconfig
- removed provides libnss_mysql (compatibility with my old packages)
- autoreconf used
- description bullets updated

* Sun Nov 18 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-5
- added a patch to build on x86_64 and may be other
- regenerated autoconf to use added patch
- provides cleanup

* Sun Nov 18 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-4
- buildroot changed

* Sat Nov 17 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-3
- removed devel files
- removed non-linux documentation
- added buildrequires

* Fri Aug 31 2007 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-2
- Fedora updates

* Sat Sep 3 2005 Ben Goodwin <cinergi@users.sourceforge.net> - 1.5-1
- Update to 1.4

* Sat Apr 10 2004 Ben Goodwin <cinergi@users.sourceforge.net> - 1.4-1
- Update to 1.4

* Sat Apr 10 2004 Ben Goodwin <cinergi@users.sourceforge.net> - 1.3-1
- Update to 1.3
- Remove manual static re-link (1.3 relieves the need for this)
- doc += TODO

* Sun Mar 28 2004 Ben Goodwin <cinergi@users.sourceforge.net> - 1.2-1
- Update to 1.2

* Tue Mar 02 2004 Ben Goodwin <cinergi@users.sourceforge.net> - 1.1-1
- s#exports.linux#.libs/libnss_mysql.ver#
- Oops, libs/*.o not *.lo

* Sat Jul 12 2003 Ben Goodwin <cinergi@users.sourceforge.net> - 1.0-2
- Link with version script

* Sat Jul 12 2003 Ben Goodwin <cinergi@users.sourceforge.net> - 1.0-1
- Update to 1.0
- Use *.lo instead of individual .lo names in re-link
- Removed -Bgroup and --allow-shlib-undefined linker options

* Thu Jun 19 2003 Ben Goodwin <cinergi@users.sourceforge.net> - 0.9-2
- Added ugly hack to relink some libraries static.  It will probably
  break rpm builds on some hosts ...

* Wed Jun 18 2003 Ben Goodwin <cinergi@users.sourceforge.net> - 0.9-1
- Update to 0.9

* Sun Dec 29 2002 Ben Goodwin <cinergi@users.sourceforge.net> - 0.8-1
- Initial version
