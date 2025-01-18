%global _hardened_build 1
# TODO: merge patches upstream where applicable

Name:           gnokii
Version:        0.6.31
Release:        44%{?dist}
Summary:        Linux/Unix tool suite for various mobile phones

License:        GPL-2.0-or-later
URL:            https://www.gnokii.org/
Source0:        https://www.gnokii.org/download/gnokii/%{name}-%{version}.tar.bz2
Source2:        %{name}-smsd.service
Source3:        %{name}-smsd.sysconfig
Source4:        %{name}-smsd.logrotate
Source5:        %{name}-smsd2mail.sh
Source6:        %{name}-smsd-README.smsd2mail
# Patch to make gnokii use "htmlview" instead of "mozilla" as default browser
Patch0:         %{name}-htmlview.patch
# Patch to remove port locking and apply the system-wide /usr/sbin directory
# to the path instead of the default /usr/local
Patch1:         %{name}-config.patch
Patch2:         %{name}-0.6.31-sqlite3.patch
Patch3:         %{name}-0.6.31-gcc5.patch
Patch4:         %{name}-0.6.31-gcc7.patch
Patch5: gnokii-configure-c99.patch

BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} > 7)
BuildRequires:  libpq-devel
BuildRequires:  mariadb-connector-c-devel
%else
BuildRequires:  postgresql-devel
BuildRequires:  mariadb-devel >= 5.5
%endif
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel
BuildRequires:  bluez-libs-devel
%if 0%{?fedora} >= 37 || 0%{?rhel} > 9
BuildRequires:  libusb-compat-0.1-devel
%else
BuildRequires:  libusb-devel
%endif
BuildRequires:  libical-devel >= 0.24
BuildRequires:  libXt-devel
BuildRequires:  libXpm-devel 
BuildRequires:  pcsc-lite-devel
BuildRequires:  readline-devel
BuildRequires:  perl(XML::Parser) intltool
BuildRequires:  make
BuildRequires:  chrpath
Requires(pre):  %{_sbindir}/groupadd

%description
Gnokii provides tools and a user space driver for use with mobile
phones under Linux, various unices and Win32. With gnokii you can do
such things as make data calls, update your address book, change
calendar entries, send and receive SMS messages and load ring tones
depending on the phone you have.

%package     -n xgnokii
Summary:        Graphical Linux/Unix tool suite for various mobile phones
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n xgnokii
Xgnokii is graphical Linux/Unix tool suite for various mobile
phones. It allows you to edit your contacts book, send/read SMS's
from/in computer and more other features.

%package        smsd
Summary:        Gnokii SMS daemon
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires(pre):  %{_sbindir}/useradd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires:  systemd

%description    smsd
The Gnokii SMS daemon receives and sends SMS messages.

%package        smsd-pgsql
Summary:        PostgreSQL support for Gnokii SMS daemon
Requires:       %{name}-smsd%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-smsd-postgresql < 0.6.4-0.lvn.2

%description    smsd-pgsql
%{summary}.

%package        smsd-mysql
Summary:        MySQL support for Gnokii SMS daemon
Requires:       %{name}-smsd%{?_isa} = %{version}-%{release}

%description    smsd-mysql
%{summary}.

%package        smsd-sqlite
Summary:        SQLite support for Gnokii SMS daemon
Requires:       %{name}-smsd%{?_isa} = %{version}-%{release}

%description    smsd-sqlite
%{summary}.

%package        devel
Summary:        Gnokii development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
%{summary}.


%prep
%setup -q
#%patch0 -p0
%patch -P1 -p0
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
install -pm 644 %{SOURCE5} smsd2mail.sh
install -pm 644 %{SOURCE6} README.smsd2mail

%build
%configure --enable-security --disable-static --disable-rpath
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' -i libtool
sed -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' -i libtool
%make_build
pushd xgnokii
%make_build
popd 

%install
%make_install

# Rename smsd to gnokii-smsd
mv $RPM_BUILD_ROOT%{_bindir}/{,gnokii-}smsd
mv $RPM_BUILD_ROOT%{_mandir}/man8/{,gnokii-}smsd.8
sed -i 's,smsd ,gnokii-smsd ,' $RPM_BUILD_ROOT%{_mandir}/man8/gnokii-smsd.8
sed -i 's,smsd.,gnokii-smsd.,' $RPM_BUILD_ROOT%{_mandir}/man8/gnokii-smsd.8

# Remove libtool droppings
rm $RPM_BUILD_ROOT%{_libdir}{,/smsd}/lib*.la

# Fix up the default desktop file
desktop-file-install \
  --delete-original \
  --vendor "" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --mode 644 \
  --add-category X-Fedora \
  xgnokii/xgnokii.desktop

install -D -m 755 xgnokii/.libs/xgnokii $RPM_BUILD_ROOT%{_bindir}

install -D -m 644 common/gnokii.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gnokii.pc
install -D -m 644 xgnokii/xgnokii.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/xgnokii.pc

# Convert the default icons to PNG
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/pixmaps
convert Docs/sample/logo/gnokii.xpm \
  $RPM_BUILD_ROOT%{_datadir}/pixmaps/xgnokii.png
chmod 644 $RPM_BUILD_ROOT%{_datadir}/pixmaps/xgnokii.png

# Install the configuration files
install -Dpm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}/gnokii-smsd.service
install -Dpm 640 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/gnokii-smsd
install -Dpm 644 %{SOURCE4} \
  $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/gnokii-smsd
cp -a Docs/sample/gnokiirc $RPM_BUILD_ROOT%{_sysconfdir}/

# Install the docs
mv $RPM_BUILD_ROOT%{_datadir}/doc/gnokii/ temporary-gnokii-docs/

# Use last resort to remove -rpath usage that can't be removed from Makefiles
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/{gnokii,gnokiid,gnokii-smsd,xgnokii}

%find_lang %{name}

%pre
getent group %{name} > /dev/null || %{_sbindir}/groupadd -r %{name}

%pre smsd
getent passwd %{name} > /dev/null || %{_sbindir}/useradd -r -M -d / \
  -g %{name} -s /sbin/nologin -c "Gnokii system user" %{name}

%ldconfig_scriptlets

%post smsd
%systemd_post gnokii-smsd.service

%preun smsd
%systemd_preun gnokii-smsd.service

%postun smsd
%systemd_postun_with_restart gnokii-smsd.service

%files -f %{name}.lang
%license COPY*
%doc ChangeLog MAINTAINERS TODO temporary-gnokii-docs/*
%config(noreplace) %{_sysconfdir}/gnokiirc
%attr(4750,root,gnokii) %{_sbindir}/mgnokiidev
%{_bindir}/gnokii
%{_bindir}/sendsms
%{_bindir}/gnokiid
%{_libdir}/libgnokii.so.*
%{_mandir}/man1/gnokii.1*
%{_mandir}/man1/sendsms.1*
%{_mandir}/man8/gnokiid.8*
%{_mandir}/man8/mgnokiidev.8*

%files -n xgnokii
%doc xgnokii/ChangeLog xgnokii/README.vcard
%{_bindir}/xgnokii
%{_datadir}/pixmaps/xgnokii.png
%{_datadir}/applications/*xgnokii.desktop
%{_mandir}/man1/xgnokii.1*

%files smsd
%doc smsd/action smsd/ChangeLog smsd/README README.smsd2mail smsd2mail.sh
%attr(-,gnokii,gnokii) %config(noreplace) %{_sysconfdir}/sysconfig/gnokii-smsd
%config(noreplace) %{_sysconfdir}/logrotate.d/gnokii-smsd
%{_unitdir}/gnokii-smsd.service
%{_bindir}/gnokii-smsd
%{_mandir}/man8/gnokii-smsd.8*
%dir %{_libdir}/smsd/
%{_libdir}/smsd/libsmsd_file.so

%files smsd-pgsql
%doc smsd/sms.tables.pq.sql
%{_libdir}/smsd/libsmsd_pq.so

%files smsd-mysql
%doc smsd/sms.tables.mysql.sql
%{_libdir}/smsd/libsmsd_mysql.so

%files smsd-sqlite
%doc smsd/sms.tables.sqlite.sql
%{_libdir}/smsd/libsmsd_sqlite.so

%files devel
%{_includedir}/gnokii*
%{_libdir}/libgnokii.so
%{_libdir}/pkgconfig/gnokii.pc
%{_libdir}/pkgconfig/xgnokii.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.6.31-39
- migrated to SPDX license

* Thu Feb 02 2023 Florian Weimer <fweimer@redhat.com> - 0.6.31-38
- Port configure script to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 27 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.6.31-33
- Disable RPATH.

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6.31-32
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 0.6.31-31
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.31-26
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.6.31-22
- libical rebuild.

* Wed Sep 20 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.6.31-21
- Switch to mariadb-connector-c, BZ 1493686.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sat Jul 29 2017 Robert Scheck <robert@fedoraproject.org> 0.6.31-19
- Switch to systemd scriptlets to make rebuilding working

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 12 2017 Robert Scheck <robert@fedoraproject.org> 0.6.31-17
- Added patch to make rebuilding with GCC 7 working
- Allow passing arguments to gnokii-smsd via sysconfig (#1112292)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.6.31-15
- Rebuild for readline 7.x

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.31-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Jon Ciesla <limburgher@gmail.com> - 0.6.31-13
- libical rebuild.

* Sat Jun 20 2015 Robert Scheck <robert@fedoraproject.org> 0.6.31-12
- Added patch to make rebuilding with GCC 5 working

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct 12 2014 Robert Scheck <robert@fedoraproject.org> 0.6.31-10
- Add missing SQL file for initializing the SQLite tables
- Fix configure script for proper linking against -lsqlite3

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.31-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.31-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 24 2013 Rex Dieter <rdieter@fedoraproject.org> 0.6.31-6
- rebuild (libical)

* Tue May 21 2013 Jon Ciesla <limburgher@gmail.com> - 0.6.31-5
- Add hardened build, BZ 965508.

* Wed Feb 27 2013 Jon Ciesla <limburgher@gmail.com> - 0.6.31-4
- Correct xgnokii installation.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 17 2012 Jon Ciesla <limburgher@gmail.com> - 0.6.31-1
- Migrate to systemd, BZ 781511.
- Latest upstream.
- Fixed up installation.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 09 2011 Robert Scheck <robert@fedoraproject.org> 0.6.30-1
- Update to 0.6.30 and added SQLite subpackage (#466880, #735717)

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 0.6.29-3
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Bastien Nocera <bnocera@redhat.com> 0.6.29-1
- Update to 0.6.29

* Mon Sep 07 2009 Bastien Nocera <bnocera@redhat.com> 0.6.28-1
- Update to 0.6.28

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.6.27-7
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Ville Skyttä <ville.skytta at iki.fi> - 0.6.27-5
- Build with pcsc-lite and readline support (#430387).

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Robert Scheck <robert@fedoraproject.org> 0.6.27-3
- Rebuild for MySQL 5.1

* Mon Oct 06 2008 - Bastien Nocera <bnocera@redhat.com> - 0.6.27-2
- Fix htmlview patch

* Mon Oct 06 2008 - Bastien Nocera <bnocera@redhat.com> - 0.6.27-1
- Update to 0.6.27

* Thu Sep 11 2008 - Bastien Nocera <bnocera@redhat.com> - 0.6.26-3
- Rebuild

* Thu Jun 19 2008 - Bastien Nocera <bnocera@redhat.com> - 0.6.26-2
- Rebuild with libical support

* Wed Jun 11 2008 - Bastien Nocera <bnocera@redhat.com> - 0.6.26-1
- Update to 0.6.26

* Fri May 23 2008 Robert Scheck <robert@fedoraproject.org> 0.6.25-2
- Set empty --vendor rather none for using desktop-file-install
- Fixed initscript as gnokii-smsd stays in /usr/bin not /usr/sbin

* Mon May 19 2008 - Bastien Nocera <bnocera@redhat.com> - 0.6.25-1
- Update to 0.6.25

* Thu Mar 20 2008 - Bastien Nocera <bnocera@redhat.com> - 0.6.24-1
- Update to 0.6.24

* Mon Feb 11 2008 - Linus Walleij <triad@df.lth.se> - 0.6.22-3
- Rebuild for GCC 4.3.

* Thu Dec 6 2007 - Linus Walleij <triad@df.lth.se> - 0.6.22-2
- Pick up new libssl .solib version dependency.

* Thu Nov 29 2007 - Bastien Nocera <bnocera@redhat.com> - 0.6.22-1
- Update to 0.6.22

* Thu Nov 01 2007 - Bastien Nocera <bnocera@redhat.com> - 0.6.20-1
- Update to 0.6.20

* Sun Oct 28 2007 Jeremy Katz <katzj@redhat.com> - 0.6.18-3
- Even better multilib fixing (#335161)

* Tue Oct 23 2007 - Jeremy Katz <katzj@redhat.com> - 0.6.18-2
- Quick fix to multilib conflict (#335161)

* Fri Aug 17 2007 - Linus Walleij <triad@df.lth.se> - 0.6.18-1
- New upstream release

* Fri Aug 17 2007 - Linus Walleij <triad@df.lth.se> - 0.6.17-2
- Update license field from GPL to GPLv2+

* Wed Jul 04 2007 - Bastien Nocera <bnocera@redhat.com> - 0.6.17-1
- New upstream release

* Mon Jul 02 2007 - Bastien Nocera <bnocera@redhat.com> - 0.6.16-1
- New upstream release
- Update smsd name change patch
- ppm2nokia, waitcall and todologo have moved to gnokii-extras, as per
  upstream

* Wed Dec 06 2006 Linus Walleij <triad@df.lth.se> - 0.6.14-3
- Rebuild to pick up new libpq IF

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.6.14-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sat Sep 23 2006 Linus Walleij <triad@df.lth.se> - 0.6.14-1
- New upstream release.

* Tue Aug 29 2006 Linus Walleij <triad@df.lth.se> - 0.6.13-3
- Rebuild for Fedora Extras 6.

* Fri Aug 11 2006 Linus Walleij <triad@df.lth.se> - 0.6.13-2
- Bump because tagged before committing sources and I just
  dont know how the f* you delete a tag in CVS at the moment
  and it does seem like a too big endavour to find out just
  in order to have a nice release tag.

* Thu Aug 10 2006 Linus Walleij <triad@df.lth.se> - 0.6.13-1
- New upstream release.
- New dependency on libusb for USB serial, DKU no longer needed/wanted
  so now we have that troublesome issue resolved once and for all.
- Remove patches to SQL files: these are now fixed upstream!

* Mon Jun 12 2006 Linus Walleij <triad@df.lth.se> - 0.6.12-4
- Rebuilding due to changed interface on libbluetooth.

* Sun Apr 2 2006 Linus Walleij <triad@df.lth.se> - 0.6.12-4
- Goofed up. Fixit it...

* Sun Apr 2 2006 Linus Walleij <triad@df.lth.se> - 0.6.12-3
- Post-import updates.

* Sat Apr 1 2006 Linus Walleij <triad@df.lth.se> - 0.6.12-2
- Updated after comments from Ville.

* Thu Mar 16 2006 Linus Walleij <triad@df.lth.se> - 0.6.12-1
- New upstream tarball

* Wed Mar 8 2006 Linus Walleij <triad@df.lth.se> - 0.6.11-2
- Updated after comments from Ville.

* Sun Mar 5 2006 Linus Walleij <triad@df.lth.se> - 0.6.11-1
- 0.6.11
- Modified to drop into the Fedora Extras as the nice package it now is
- Based work off Ville's good olde package

* Sun Nov 13 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.6.10-0.lvn.1
- 0.6.10.
- Clean up pkgconfig file and -devel dependencies from bits needed only
  for static libs.

* Thu Nov  3 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.6.9-0.lvn.1
- 0.6.9, desktop entry file included upstream.
- Drop zero Epochs.

* Sat Aug  6 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.6.8-0.lvn.1
- 0.6.8.
- Don't ship static libraries.
- Rename smsd to gnokii-smsd to avoid conflicts with smstools.
- Remove not included files instead of using %%exclude.

* Sat Jun  4 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.6.7-0.lvn.2
- BuildRequire openssl-devel to work around https://bugzilla.redhat.com/159569

* Thu Jun  2 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.6.7-0.lvn.1
- 0.6.7.
- Build unconditionally with bluetooth support.

* Mon May  2 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:0.6.5-0.lvn.1
- 0.6.5.

* Fri Nov  5 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.6.4-0.lvn.2
- Rename -smsd-postgresql to -smsd-pgsql for consistency with other similar
  packages in FC/Extras.

* Fri Oct 22 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.6.4-0.lvn.1
- Update to 0.6.4, perms and pgsql patches applied upstream.
- Xgnokii help locale symlink hack no longer necessary.
- Don't remove user/group on last erase, move smsd user to -smsd subpackage.
- Add libical support (disabled), rebuild with "--with libical" to enable.

* Mon Jul  5 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.6.3-0.lvn.1
- Update to 0.6.3.

* Sun Jun 20 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.6.1-0.lvn.4
- Improve Xgnokii desktop entry according to GNOME HIG.

* Sun Jun 13 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.6.1-0.lvn.3
- Remove duplicate gettext build dependency (bug 95).

* Sun Jun  6 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.6.1-0.lvn.2
- Fix chown syntax in smsd init script.
- Summary and description improvements.
- Trim $RPM_OPT_FLAGS out from gnokii.pc.
- Make -devel require XFree86-devel.

* Sun Apr 18 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.6.1-0.lvn.1
- Update to 0.6.1.

* Thu Mar 18 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.6.0-0.lvn.2
- Make -devel require pkgconfig.

* Mon Feb 23 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.6.0-0.lvn.1
- Update to 0.6.0.

* Mon Feb  2 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.5.10-0.lvn.1
- Update to 0.5.10.

* Tue Jan 27 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.5.9-0.lvn.1
- Update to 0.5.9.
- Specfile cleanups, small init script enhancements.

* Sat Dec 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.5.7-0.lvn.1
- Update to 0.5.7.
- Move smsd man page into -smsd subpackage.

* Sat Nov 15 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.5.6-0.lvn.1
- Update to 0.5.6.
- Include sample action script for forwarding SMSD messages to mail.
- s/fedora/livna/.
- Specfile and init script cleanups.

* Sat Jul 19 2003 Warren Togami <warren@togami.com> - 0:0.5.2-0.fdr.2
- Disable smp flags to prevent build failure

* Sun Jun 15 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.5.2-0.fdr.1
- Update to 0.5.2.

* Thu May 29 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.5.1-0.fdr.1
- Update to 0.5.1.
- Include init script, sysconfig and logrotate config for smsd.

* Tue May 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.5.0-0.fdr.1
- Update to 0.5.0.

* Sun Nov  3 2002 Ville Skyttä <ville.skytta at iki.fi> 0.4.3-1cr
- RedHat'ified PLD version.
