%global git_revision 9ae8768

%bcond_with	evolution
%bcond_without	bundled_gob2

Name:           mail-notification
Version:        5.4
Release:        113.git.%{git_revision}%{?dist}
Summary:        Status icon that informs you if you have new mail

License:        GPL-3.0-or-later
URL:            http://www.nongnu.org/mailnotify/
#Source0:        http://savannah.nongnu.org/download/mailnotify/mail-notification-%{version}.tar.bz2
# Upstream isn't alive any more, use a github forked copy which contains all patches which
# have been collected over the past years: https://github.com/epienbroek/mail-notification
#
# To regenerate source tarball:
# wget https://github.com/epienbroek/mail-notification/tarball/$git_revision -O mail-notification-$git_revision.tar.gz
Source0:        mail-notification-%{git_revision}.tar.gz

%if %{with bundled_gob2}
Source1:        http://ftp.5z.com/pub/gob/gob2-2.0.19.tar.gz
%endif

# jb build system is turning on -Werror to build itself.  This patch fixes a
# warning with current gcc
Patch0: mail-notification-jb-gcc-format.patch

# build break when building with evolution 3.11.2
Patch2:         mail-notification-evo3_11_2.patch

# Fix FTBFS against latest glibc
Patch3:         mail-notification-dont-link-against-bsd-compat.patch

# Build against evolution-data-server 3.23.2
Patch4:         mail-notification-eds3_23_2.patch

# Use gstreamer-1.0 to play sound
Patch5:		mail-notification-gstreamer1.patch

Patch6:		mail-notification-jb-c99.patch
Patch7:		mail-notification-incompatible-pointer-types.patch
Patch8:		mail-notification-maybe-uninitialized.patch
Patch9:		mail-notification-libxml2.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  desktop-file-utils, scrollkeeper
BuildRequires:  openssl-devel >= 0.9.6
BuildRequires:  cyrus-sasl-devel >= 2.0
BuildRequires:  glib2-devel >= 2.14
BuildRequires:  gtk3-devel
BuildRequires:  GConf2-devel, libgnome-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  libnotify-devel >= 0.4.1
BuildRequires:  gmime-devel >= 2.4
BuildRequires:  libgnome-keyring-devel
BuildRequires:  perl-XML-Parser
%if %{without bundled_gob2}
BuildRequires:  gob2 >= 2.0.17
%endif
%if %{with evolution}
BuildRequires:  evolution-devel >= 3.45.1
BuildRequires:  evolution-data-server-devel >= 3.45.1
%endif

# needed for the gtk-builder-convert tool
BuildRequires:  gtk2-devel

# needed for the GConf RPM macros
BuildRequires:  GConf2

%if %{with bundled_gob2}
BuildRequires: bison, flex, flex-static
%endif

Requires:         hicolor-icon-theme

Requires(pre):    GConf2
Requires(post):   GConf2, scrollkeeper
Requires(preun):  GConf2
Requires(postun): scrollkeeper


%description
Mail Notification is a status icon (aka tray icon) that informs you if you
have new mail. It works with system trays implementing the freedesktop.org
System Tray Specification, such as the GNOME Panel Notification Area, the
Xfce Notification Area and the KDE System Tray.


%if %{with evolution}
%package        evolution-plugin
Summary:        Evolution plugin for Mail Notification
Requires:       %{name} = %{version}-%{release}

%description	evolution-plugin
Evolution support for Mail Notification.
%endif


%prep
%setup -q -n epienbroek-%{name}-%{git_revision} %{?with_bundled_gob2:-a 1}

%patch -P0 -p1
%patch -P2 -p1 -b .evo3_11_2
%patch -P3 -p0
%patch -P4 -p1 -b .eds3_23_2
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1 -b .incompatible-pointer-types
%patch -P8 -p1 -b .maybe-uninitialized
%patch -P9 -p1 -b .libxml2

# update config.{guess,sub} manually
cp -p /usr/lib/rpm/redhat/config.{guess,sub} jbsrc/tools/


%build

%if %{with bundled_gob2}
mkdir bin

pushd gob2-*
%configure
make
ln src/gob2 ../bin
popd

%endif

./jb configure \
  cc="%{__cc}" \
  cflags="$RPM_OPT_FLAGS -Wno-deprecated-declarations" \
  cppflags="-D_GNU_SOURCE -Wno-deprecated-declarations" \
  ldflags="$RPM_LD_FLAGS" \
  destdir=$RPM_BUILD_ROOT \
  prefix=%{_prefix} \
  bindir=%{_bindir} \
  libdir=%{_libdir} \
  libexecdir=%{_libexecdir} \
  datadir=%{_datadir} \
  sysconfdir=%{_sysconfdir} \
  localstatedir=%{_localstatedir} \
  gtk3=yes \
%if %{with evolution}
  evolution=yes \
%else
  evolution=no \
%endif
%if %{with bundled_gob2}
  gob2=$PWD/bin/gob2 \
%endif
  install-gconf-schemas=no

./jb build

# The build command above hides away all gcc commands and their warnings
# As they can be interesting show the build log manually
cat build/build.log


%install
# For GConf apps: prevent schemas from being installed at this stage
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

./jb install

#  clear /var/lib/scrollkeeper stuff here
rm -rf $RPM_BUILD_ROOT%{_localstatedir}

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%if %{with evolution}
chmod +x $RPM_BUILD_ROOT%{_libdir}/evolution/plugins/*.so
%endif

desktop-file-install \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
  --vendor fedora                   \
%endif
  --dir ${RPM_BUILD_ROOT}%{_datadir}/gnome/autostart/  \
  --delete-original                                    \
  ${RPM_BUILD_ROOT}%{_sysconfdir}/xdg/autostart/mail-notification.desktop

desktop-file-install \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
  --vendor fedora                   \
%endif
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications      \
  --delete-original                                    \
  --add-category X-GNOME-NetworkSettings               \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/mail-notification-properties.desktop

%find_lang %{name}


%pre
%gconf_schema_prepare %{name}

%post
%gconf_schema_upgrade %{name}
/usr/bin/scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :

%preun
%gconf_schema_remove %{name}

%postun
/usr/bin/scrollkeeper-update -q ||:

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README TODO
%{_sysconfdir}/gconf/schemas/mail-notification.schemas
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/gnome/autostart/*mail-notification.desktop
%{_datadir}/applications/*mail-notification-properties.desktop
%{_datadir}/gnome/help/mail-notification/
%dir %{_datadir}/omf/mail-notification/
%{_datadir}/omf/mail-notification/mail-notification-C.omf
%{_datadir}/icons/hicolor/*/apps/mail-notification.*


%if %{with evolution}
%files evolution-plugin
%{_libdir}/evolution/plugins/*
%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-113.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-112.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.4-111.git.9ae8768
- fix incompatible-pointer-types patch (#2261363)
- rename patches properly

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-110.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-109.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 04 2023 Milan Crha <mcrha@redhat.com> 5.4-108.git.9ae8768
- Add patches to fix "incompatible-pointer-types" and "maybe-uninitialized" compiler warnings
- Add patch to adapt to libxml2 changes

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-107.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-106.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Florian Weimer <fweimer@redhat.com> - 5.4-105.git.9ae8768
- Port jb build tool to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-104.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Milan Crha <mcrha@redhat.com> - 5.4-103.git.9ae8768
- Rebuilt for evolution-data-server soname version bump

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-102.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 5.4-101.git.9ae8768
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-100.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-99.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-98.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-97.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
- Rebuild with bundled gob2-2.0.19

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-96.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-95.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-94.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-93.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug  3 2017 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.4-92.git.9ae8768
- Use gstreamer1 by default for playing sound (<wislufle@australiamail.com>, #1370188)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-91.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-90.git.9ae8768
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov  2 2016 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.4-89.git.9ae8768
- add patch for evolution-3.23.2 (Milan Crna <mcrha@redhat.com>, #1390590)

* Tue Aug 23 2016 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.4-88.git.9ae8768
- rebuild with the proper compiler and linker options (#1368912)

* Thu Aug 18 2016 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.4-87.git.9ae8768
- Update to the latest upstream git revision 9ae8768 (#1288891)
- Use gtk3=yes for build

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-86.git.eab5c13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Dan Horák <dan[at]danny.cz> - 5.4-85.git.eab5c13
- support secondary arches via updated config.{guess,sub} from system

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-84.git.eab5c13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 22 2014 Milan Crha <mcrha@redhat.com> 5.4-83.git.eab5c13
- Rebuild against newer evolution (changed folder structure)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-82.git.eab5c13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun  9 2014 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.4-81.git.eab5c13
- Drop evolution plugin for now (too hard to maintain it further)
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 03 2014 Milan Crha <mcrha@redhat.com> 5.4-80.git.eab5c13
- Rebuild against newer evolution-data-server

* Sun Jan 19 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4-79.git.eab5c13
- Fix FTBFS against latest glibc

* Tue Jan 14 2014 Milan Crha <mcrha@redhat.com> 5.4-78.git.eab5c13
- Rebuild against newer evolution-data-server

* Wed Nov 20 2013 Milan Crha <mcrha@redhat.com> 5.4-77.git.eab5c13
- Rebuild against newer evolution-data-server
- Add patch to be buildable against evolution 3.11.2 release

* Sat Oct 26 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4-76.git.eab5c13
- Rebuild against latest evolution

* Mon Aug 19 2013 Milan Crha <mcrha@redhat.com> 5.4-75.git.eab5c13
- Rebuild against newer evolution-data-server

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-74.git.eab5c13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 10 2013 Milan Crha <mcrha@redhat.com> 5.4-73.git.eab5c13
- Rebuild against newer evolution-data-server

* Sun Jun 23 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4-72.git.eab5c13
- Rebuild against latest evolution

* Sat May  4 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4-71.git.eab5c13
- Add support for aarch64 (RHBZ #926114)

* Mon Apr 29 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4-70.git.eab5c13
- Replaced BR: gnome-keyring-devel with libgnome-keyring-devel (RHBZ #956705)

* Fri Feb 15 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 5.4-69.git.eab5c13
- Fix FTBFS.  Patch is to the complex build scripts rather than the installed code.

* Thu Feb 14 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 5.4-68.git.eab5c13
- Remove --vendor from desktop-file-install on F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-67.git.eab5c13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Milan Crha <mcrha@redhat.com> 5.4-66.git.eab5c13
- Rebuild against newer evolution-data-server

* Wed Dec 26 2012 Kevin Fenzi <kevin@scrye.com> 5.4-65.git.eab5c13
- Rebuild for new evolution

* Wed Nov 21 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4-64.git.eab5c13
- Update to eab5c13 snapshot
- Fixes new e-mail detection in evolution 3.6
- Use a more efficient method to retrieve unread mails from
  evolution as suggested by Milan Crha (GNOME BZ #688429)
- Replaced the patch with a sed call to avoid multiple gcc -O optimalisation flags being used

* Tue Nov 20 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4-63.git72ad191
- Update to 72ad191 snapshot
- Fixes compatibility with GLib 2.35 (deprecated g_type_init)
- Fixes location of tooltip
- Trimmed old changelog entries from the .spec file

* Tue Nov 20 2012 Milan Crha <mcrha@redhat.com> - 5.4-62.gitb4ca832
- Rebuild against newer evolution-data-server

* Thu Oct 25 2012 Milan Crha <mcrha@redhat.com> - 5.4-61.gitb4ca832
- Rebuild against newer evolution-data-server

* Wed Aug 22 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4-60.gitb4ca832
- Switch to using a GitHub fork of mail-notification as upstream is dead:
  https://github.com/epienbroek/mail-notification
- Removed (almost) all patches as they're now part of the GitHub fork
- Removed hack to link against libX11 as a proper fix was applied in the GitHub fork
- Fixes compatibility with evolution 3.5.3 and higher
- Re-added the BR: gob2
- Removed ancient obsoletes tag
- Fixed mixed-use-of-spaces-and-tabs rpmlint warning

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4-58
- Drop Fedora >= 15 conditionals as older Fedora versions aren't supported any more
- Don't crash when the system tray manager (like gnome-shell) is restarted
  Patch created by Julien Danjou, http://bugs.debian.org/500880
- Fix segfault when the Polish translation is used
  Patch created by Przemysław, http://bugs.debian.org/523873

* Sun Jun 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4-57
- Another rebuild against the latest evolution

* Wed May  9 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4-56
- Fix compatibility with latest evolution (again..)

* Mon Apr  9 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4-55
- Adding mailboxes was broken with evolution 3.4. Fixed
- Various minor improvements in the gtk3 user interface

* Thu Apr  5 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4-54
- Fixed a stack overflow which occured while verifying SSL certificates
  for POP3 and IMAP mailboxes. RHBZ #810054

* Wed Mar 21 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.4-53
- Fixed a posible segfault in the evolution plugin

* Wed Feb 22 2012 Milan Crha <mcrha@redhat.com> - 5.4-52
- Rebuild against newer evolution-data-server

* Wed Feb 08 2012 Milan Crha <mcrha@redhat.com> - 5.4-51
- Rebuild against newer evolution-data-server
- Add patch to build with evolution-3.3.5's libemail

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Milan Crha <mcrha@redhat.com> - 5.4-49
- Rebuild against newer evolution-data-server

