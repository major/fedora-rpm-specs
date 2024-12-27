# Review: https://bugzilla.redhat.com/show_bug.cgi?id=567257

# Upstream git:
# git://pcmanfm.git.sourceforge.net/gitroot/pcmanfm/libfm
# add bootstrap, need to build menu-cache in epel7
%global         use_release  0
%global         use_gitbare  1

%if 0%{?use_gitbare} < 1
# force
%global         use_release  1
%endif

%global		git_version	%{nil}
%global		git_ver_rpm	%{nil}
%global		git_builddir	%{nil}

%global         main_version	1.3.2

%if 0%{?use_gitbare}
%global		gittardate		20241225
%global		gittartime		1644

%global		gitbaredate	20241221
%global		git_rev		37456d7d7839c55d2cf9d1c38d92c7571aeb463a
%global		git_short		%(echo %{git_rev} | cut -c-8)
%global		git_version	%{gitbaredate}git%{git_short}

%global		git_ver_rpm	^%{git_version}
%global		git_builddir	-%{git_version}
%endif


%global		main_version	1.3.2

%global         bootstrap   0
%global         build_doc   1

%undefine        _changelog_trimtime

Name:           libfm
Version:        %{main_version}%{git_ver_rpm}
Release:        1%{?dist}
Summary:        GIO-based library for file manager-like programs

# src/actions/	GPL-2.0-or-later
# src/base/	LGPL-2.1-or-later
# src/demo/	GPL-2.0-or-later
# src/extra/	LGPL-2.1-or-later
# src/fm-gtk.{c,h}	GPL-2.0-or-later
# src/gtk-compat.c	GPL-2.0-or-later
# src/*.c		(rest) LGPL-2.1-or-later
# src/gio/		GPL-2.0-or-later
# src/gtk/exo/	LGPL-2.1-or-later AND GPL-2.0-or-later
# src/gtk/		GPL-2.0-or-later AND LGPL-2.1-or-later
# src/job/		LGPL-2.1-or-later
# src/modules/	GPL-2.0-or-later
# src/tests/	GPL-2.0-or-later
# src/tools/	GPL-2.0-or-later
# src/udisks/	GPL-2.0-or-later

# SPDX confirmed
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            http://pcmanfm.sourceforge.net/
%if 0%{?use_release} >= 1
Source0:        http://downloads.sourceforge.net/pcmanfm/%{name}-%{mainver}%{?prever}.tar.xz
Source1:        https://raw.githubusercontent.com/lxde/libfm/master/autogen.sh
%endif
%if 0%{?use_gitbare} >= 1
Source0:        libfm-%{gittardate}T%{gittartime}.tar.gz
%endif
Source10:       create-libfm-git-bare-tarball.sh

# Make fm_config_load_from_key_file don't replace string key value
# when subsequent config file does not contain such key but previous key had
# (related to bug 2011471)
Patch1:         libfm-1.3.2-0001-fm_config_load_from_key_file-don-t-replace-string-va.patch
# http://sourceforge.net/p/pcmanfm/feature-requests/385/
#Patch1000:      http://sourceforge.net/p/pcmanfm/feature-requests/_discuss/thread/0a50a386/597e/attachment/libfm-1.2.3-moduledir-gtkspecific-v02.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2333955
# https://github.com/lxde/libfm/issues/104
Patch11:        libfm-pr105-Restore-ABI-for-libfm.so.patch
Patch1000:      libfm-1.3.0.2-moduledir-gtkspecific-v03.patch

BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.26.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.27.0
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(libexif)

%if ! 0%{?bootstrap}
BuildRequires:  pkgconfig(libmenu-cache) >= 0.3.2
%endif

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils

BuildRequires:  gtk-doc
BuildRequires:  libxslt
BuildRequires:  %{_bindir}/valac

# Patch1000 needs the below anyway
BuildRequires:  automake
BuildRequires:  libtool

# Anyway use git
BuildRequires:  git

%if 0%{?build_doc} < 1
Obsoletes:      %{name}-devel-docs < 0.1.15
%endif


%description
LibFM is a GIO-based library used to develop file manager-like programs. It is
developed as the core of next generation PCManFM and takes care of all file-
related operations such as copy & paste, drag & drop, file associations or 
thumbnails support. By utilizing glib/gio and gvfs, libfm can access remote 
file systems supported by gvfs.

This package contains the generic non-gui functions of libfm.


%package        gtk
Summary:        File manager-related GTK+ widgets of %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gvfs

%description    gtk
libfm is a GIO-based library used to develop file manager-like programs. It is
developed as the core of next generation PCManFM and takes care of all file-
related operations such as copy & paste, drag & drop, file associations or 
thumbnail support. By utilizing glib/gio and gvfs, libfm can access remote 
file systems supported by gvfs.

This package provides useful file manager-related GTK+ 3 widgets.

%package        gtk2
Summary:        File manager-related GTK+ widgets of %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gvfs

%description    gtk2
libfm is a GIO-based library used to develop file manager-like programs. It is
developed as the core of next generation PCManFM and takes care of all file-
related operations such as copy & paste, drag & drop, file associations or 
thumbnail support. By utilizing glib/gio and gvfs, libfm can access remote 
file systems supported by gvfs.

This package provides useful file manager-related GTK+ 2 widgets.

%package        gtk-utils
Summary:        GTK+ related utility package for %{name}
Requires:       %{name}-gtk%{?isa} = %{version}-%{release}
Obsoletes:      lxshortcut < 0.1.3
Provides:       lxshortcut = %{version}-%{release}
Provides:       lxshortcut%{?_isa} = %{version}-%{release}

%description    gtk-utils
This package contains some GTK+ related utility files for
%{name}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        gtk-devel-common
Summary:        Common Development files for %{name}-gtk
Requires:       %{name}-devel = %{version}-%{release}
BuildArch:		noarch

%description    gtk-devel-common
The %{name}-gtk-devel package contains common header files for
developing applications that use %{name}-gtk.


%package        gtk-devel
Summary:        Development files for %{name}-gtk
Requires:       %{name}-gtk%{?_isa} = %{version}-%{release}
Requires:       %{name}-gtk-devel-common = %{version}-%{release}

%description    gtk-devel
The %{name}-gtk-devel package contains libraries files for
developing applications that use %{name}-gtk.

%package        gtk2-devel
Summary:        Development files for %{name}-gtk2
Requires:       %{name}-gtk2%{?_isa} = %{version}-%{release}
Requires:       %{name}-gtk-devel-common = %{version}-%{release}

%description    gtk2-devel
The %{name}-gtk2-devel package contains libraries files for
developing applications that use %{name}-gtk2.

%package        devel-docs
Summary:        Development documation for %{name}

%description    devel-docs
This package containg development documentation files for %{name}.


%prep
%if 0%{?use_release} >= 1
%setup -q -n %{name}-%{main_version}%{?prever}
cp -a %{SOURCE1} .
#%%patch0 -p1 -b .orig
git init
%endif

%if 0%{?use_gitbare}
%setup -q -c -T -n %{name}-%{main_version}%{git_builddir} -a 0
git clone ./%{name}.git/
cd %{name}

# Restore timestamps
set +x
echo "Restore timestamps"
git ls-tree -r --name-only HEAD | while read f
do
	unixtime=$(git log -n 1 --pretty='%ct' -- $f)
	touch -d "@${unixtime}" $f
done
set -x

cp -a [A-Z]* ..
%endif

git config user.name "libfm Fedora maintainer"
git config user.email "libfm-maintainer@fedoraproject.org"

%if 0%{?use_release} >= 1
# Once call autogen.sh to make git status clean
sh autogen.sh
git add .
git commit -m "Init tree" -q
%endif

%if 0%{?use_gitbare} >= 1
git checkout -b %{main_version}-fedora %{git_rev}
cat > GITHASH <<EOF
EOF

cat GITHASH | while read line
do
  commit=$(echo "$line" | sed -e 's|[ \t].*||')
  git cherry-pick $commit
done
%endif

cat %PATCH1  | git am
cat %PATCH11 | git am
%patch -P1000 -p1 -Z
git commit -m "Use gtk version specific module directory" -a

# Need reporting upstream
# ref: https://github.com/lxde/libfm/commit/1af95bd8f26cab6848a74b7e02b53c6c79fb53a5
sed -i Makefile.am \
	-e '\@docs/reference/libfm/libfm-sections.txt@d'
git commit -m "Remove files entry to be regenerated" -a || true

sh autogen.sh
git commit -m "save modified files" -a || true

# treak rpath
sed -i.libdir_syssearch \
  -e '/sys_lib_dlsearch_path_spec/s|/usr/lib |/usr/lib /usr/lib64 /lib /lib64 |' \
  configure
git commit -m "Tweak library search path spec not to inject rpath" -a || true

# Ignore po/ directory make check error
sed -i.error po/Makefile.in.in \
	-e '\@check@,\@fi@s|exit 1|exit 0|'
git commit -m "ignore po/ directory make check error" -a || true

# Tell vala to regenerate C source
find . -name \*.vala | xargs touch


%build
%if 0%{?use_gitbare} >= 1
cd libfm
%endif

%if 0%{?use_gitbare} >= 1
# Workaround
# Once generate files anyway
./configure
make dist
rm -f config.status
%endif

for ver in \
	2 \
	3 \
	%{nil}
do
	rm -rf _BUILDDIR_gtk${ver}
	mkdir _BUILDDIR_gtk${ver}
	pushd _BUILDDIR_gtk${ver}
	ln -sf ../configure

	%configure \
	    --srcdir=$(pwd)/.. \
%if 0%{?bootstrap}
	    --with-extra-only \
%endif
	    --enable-gtk-doc \
	    --enable-udisks \
	    --with-gtk=${ver} \
%if 0
	    --enable-demo \
%endif
	    --disable-silent-rules \
	    --disable-static

	# To show translation status
	make -C po -j1 GMSGFMT="msgfmt --statistics"
	make %{?_smp_mflags} -k

	make install DESTDIR=$(pwd)/../INSTDIR-gtk${ver} INSTALL="install -p"
	popd
done

%install
TOPDIR=$(pwd)

%if 0%{?use_gitbare} >= 1
cd libfm
%endif

# GTK3
cp -a INSTDIR-gtk3/* $RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/pkgconfig/libfm-gtk.pc

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%if ! 0%{?bootstrap}
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
( 
cd $TOPDIR
%find_lang %{name}
)
%endif

echo '%%defattr(-,root,root,-)' > $TOPDIR/base-header.files
echo '%%defattr(-,root,root,-)' > $TOPDIR/gtk-header.files

for f in $RPM_BUILD_ROOT%_includedir/%name-1.0/*.h
do
  bf=$(basename $f)
  for dir in actions base job extra .
  do
    if [ -f src/$dir/$bf ]
    then
	echo %_includedir/%name-1.0/$bf >> $TOPDIR/base-header.files
    fi
  done
  for dir in gtk
  do
    if [ -f src/$dir/$bf ]
    then
	echo %_includedir/%name-1.0/$bf >> $TOPDIR/gtk-header.files
    fi
  done
done

# GTK2
%if ! 0%{?bootstrap}
pushd INSTDIR-gtk2

find . -name '*.la' -exec rm -f {} ';'
rm -f .%{_libdir}/pkgconfig/libfm-gtk3.pc

diff -urNp .%{_includedir}/%{name}-1.0 $RPM_BUILD_ROOT%{_includedir}/%name-1.0
diff -urNp .%{_datadir}/%{name} $RPM_BUILD_ROOT/%{_datadir}/%{name}

cp -a ./%{_libdir}/libfm-gtk* $RPM_BUILD_ROOT%{_libdir}
cp -a ./%{_libdir}/pkgconfig/libfm-gtk.pc \
	$RPM_BUILD_ROOT%{_libdir}/pkgconfig/
cp -a ./%{_libdir}/libfm/modules/gtk/ \
	$RPM_BUILD_ROOT%{_libdir}/libfm/modules/
popd
%endif

/usr/lib/rpm/check-rpaths

%check
%if 0%{?use_gitbare} >= 1
cd libfm
%endif

for ver in \
	2 \
	3 \
	%{nil}
do
	pushd _BUILDDIR_gtk${ver}
	make check
	popd
done

%pre devel
# Directory -> symlink
if [ -d %{_includedir}/libfm ] ; then
  rm -rf %{_includedir}/libfm
fi

%if 0%{?bootstrap}
%files
%else
%files -f %{name}.lang
%endif
# FIXME: Add ChangeLog if not empty
%doc AUTHORS
%license COPYING
%doc NEWS
%doc README

%if ! 0%{?bootstrap}
%dir %{_sysconfdir}/xdg/libfm/
%config(noreplace) %{_sysconfdir}/xdg/libfm/libfm.conf

%{_datadir}/%{name}/
%{_libdir}/%{name}.so.4*

%dir %{_libdir}/libfm
%dir %{_libdir}/libfm/modules
%{_libdir}/libfm/modules/vfs-*.so
%{_datadir}/mime/packages/libfm.xml
%endif

%{_libdir}/%{name}-extra.so.4*

%if ! 0%{?bootstrap}
%files gtk
%{_libdir}/%{name}-gtk3.so.4*
%{_libdir}/libfm/modules/gtk3/

%files gtk-utils
%{_mandir}/man1/libfm-pref-apps.1.*
%{_mandir}/man1/lxshortcut.1.*

%{_bindir}/libfm-pref-apps
%{_bindir}/lxshortcut
%{_datadir}/applications/libfm-pref-apps.desktop
%{_datadir}/applications/lxshortcut.desktop
%endif

%files devel -f base-header.files
%doc TODO
%{_includedir}/libfm
%dir %{_includedir}/libfm-1.0/

%if ! 0%{?bootstrap}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/libfm.pc
%endif
%{_libdir}/%{name}-extra.so
%{_libdir}/pkgconfig/libfm-extra.pc

%if ! 0%{?bootstrap}
%files gtk-devel-common -f gtk-header.files
%{_includedir}/libfm-1.0/fm-gtk.h

%files gtk-devel
%{_libdir}/%{name}-gtk3.so
%{_libdir}/pkgconfig/libfm-gtk3.pc

%files gtk2
%{_libdir}/%{name}-gtk.so.4*
%{_libdir}/libfm/modules/gtk/

%files gtk2-devel
%{_libdir}/%{name}-gtk.so
%{_libdir}/pkgconfig/libfm-gtk.pc

%if 0%{?build_doc}
%files devel-docs
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/%{name}
%endif
%endif

%changelog
* Wed Dec 25 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20241221git37456d7d-1
- Update to the latest git
- Restore libfm.so ABI (bug 2333955)

* Thu Dec 19 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20241216gitfb651b87-1
- Update to the latest git

* Fri Dec 06 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20241203gitcea66071-1
- Update to the latest git

* Sun Nov 10 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20241107gitd9935ec1-1
- Update to the latest git

* Sun Aug 25 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20240823git4d2f7b41-1
- Update to the latest git

* Tue Aug 13 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20240812gitfbcd1833-1
- Update to the latest git

* Thu Jul 18 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20240714gitee33947e-1
- Update to the latest git (20240714gitee33947e)

* Tue Jun 04 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20230916git5346a539-3
- Ignore po/ directory make check error with autoconf 2.72

* Tue May 14 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20230916git5346a539-2
- Restore timestamps for git ls files

* Tue Feb 27 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2^20230916git5346a539-1
- Update to the latest git (20230916git5346a539)

* Fri Feb 23 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2-8
- Handle gcc14 -Werror=incompatible-pointer-types
- Make vala regenerate C source related to -Werror=incompatible-pointer-types
  workaround for vala source

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2-5
- Change -Wincompatible-pointer-types from error to warning

* Mon Dec 11 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2-4
- SPDX migration

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2-2
- Make fm_config_load_from_key_file don't replace string key value
  when subsequent config file does not contain such key but previous key had
  (related to bug 2011471)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb  7 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2-1
- 1.3.2 release

* Thu Feb  4 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-4.D20210202git54cd5fc
- Update to the latest git

* Mon Feb  1 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-3.D20210129git1d79967
- Update to the latest git

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2.D20200401git8914a52.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2.D20200401git8914a52.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr  8 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-2.D20200401git8914a52
- Update to the latest git

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-1
- 1.3.1 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 29 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.0.2-1
- 1.3.0.2 release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5.gitD20171230.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan  2 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.5-5.gitD20171230
- Better cherry-pick description
- Backport one more fixes

* Sat Dec 30 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.5-4.gitD20171230
- Backport various fixes from master to 1.2.5
- Use bare repository directly

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3.100.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3.100.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr  7 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.5-3
- Fix crash when pasting large string when completion matches (bug 1437443)
- Build error fix with vala 0.36

* Mon Feb  6 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.5-2
- spec file fix for bootstrap mode on fedora (bug 1419338)

* Sun Dec 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.5-1
- 1.2.5 released.

* Sun Dec 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-13.D20161209gitab583d7800
- Update to the latest master (with 2 patch from 1.2)

* Wed Dec  7 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-12.D20161206gita24389f804
- Update to the latest master (with 2 patch from 1.2)

* Mon Dec  5 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-11.D20161204git275559f196
- Update to the lastest master branch, with cherry-picking patches from 1.2 branch
  to revert some enhancement change on master

* Thu Nov 10 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-10.D20161105gitc2989af015
- Remove duplicate files

* Tue Nov  8 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-9.D20161105gitc2989af015
- Update to the latest git 1.2 branch

* Sat Oct 22 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-8.D20161017git82b3a1a201
- Update to the latest git
- Switch to 1.2 branch

* Sun Aug 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-7.D20160627git2a537414de
- Pull github:libfm#11 fix

* Thu Aug 18 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-6.D20160627git2a537414de
- Properly initialize GError with NULL (bug 1357213)

* Thu Jul 14 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-5.D20160627git2a537414de
- Update to the latest git to pull in upstream bug fixes

* Tue Jun 21 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-4.D20160618gitb22c0995e7
- Update to the latest git to pull in upstream bug fixes

* Wed Jun 15 2016 Than Ngo <than@redhat.com> - 1.2.4-3
- disable bootstrap in epel7

* Wed Jun 15 2016 Than Ngo <than@redhat.com> - 1.2.4-2.1
- bootstrap in epel7

* Wed Jun 01 2016 Than Ngo <than@redhat.com> - 1.2.4-2
- add bootstrap support (need to build menu-cache in epel7 branch)

* Sun Feb 28 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-1
- 1.2.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-13.D20150728git47d0c1dd7d.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 30 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-13.D20150728git47d0c1dd7d
- Update to the latest git (the previous patch accepted by the upstream)

* Tue Jul 28 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-12.D20150713gitf47c9ae7ae
- Workaround for highlighting issue on icon view (bug 1211585, upstream bug 921)

* Thu Jul 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-11.D20150713gitf47c9ae7ae
- Update to the latest git
- Build gtk2 also on F-22

* Wed Jun 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-10.D20150607gite1de98ccba
- F-23: build also gtk2 library
- Move data files to main package

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-9.D20150607gite1de98ccba.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-9.D20150607gite1de98ccba
- Update to the latest git

* Sun May 31 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-8.D20150525git8f38f90e04
- Update to the latest git, removing patches applied upstream

* Sun May 24 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-7.D20150521git577806e29d
- Fix another GTK3 related bug

* Sat May 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-6.D20150521git577806e29d
- Fix two other GTK3 related bugs

* Sat May 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-5.D20150521git577806e29d
- Make search dialog work

* Thu May 21 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-4.D20150521git577806e29d
- Again try the latest git

* Thu May 21 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-3.D20150519git699810d3bd
- Make libfm-pref-apps work

* Thu May 21 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-2.D20150519git699810d3bd
- Try latest git (2015-05-19)

* Fri Oct 17 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-1
- 1.2.3

* Sun Aug 24 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.2-1
- 1.2.2

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2.1-2
- update mime scriptlets

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul  4 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-1
- 1.2.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.0-1
- 1.2.0

* Mon Feb 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.0-0.1.rc1
- 1.2.0 rc1
- Split out executable binaries into gtk-utils

* Tue Dec 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.4-1
- 1.1.4
 
* Tue Dec  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.3-1
- 1.1.3
 
* Mon Nov 11 2013 Christoph Wickert <wickert@kolabsys.com> - 1.1.2.2-3
- Rebuild for new menu-cache 0.5.x

* Fri Aug 30 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.2.2-2
- Workaround for column collapse issue when double-clicking separator

* Wed Aug 21 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.2.2-1
- 1.1.2.2

* Wed Aug 21 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.2.1-1
- 1.1.2.1

* Thu Aug 15 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.2-1
- 1.1.2

* Sun Aug 11 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.1-2
- Regenerate desktop file from .in file using intltool

* Thu Aug  8 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.1-1
- 1.1.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 25 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.1.0-2
- Rebuild against menu-cache 0.4.x

* Sun Nov  4 2012 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-1
- 1.1.0

* Thu Sep 27 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0.1-1
- 1.0.1

* Wed Aug 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.0-1
- 1.0 release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.1.17-1
- 0.1.17

* Sun Aug 28 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.1.16-1
- 0.1.16 release

* Sun Aug  7 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.1.15-7
- Update to the latest git

* Sun May 29 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.1.15-6
- Update to the latest git, to support treeview on pcmanfm

* Tue May 03 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.1.15-5
- Update to the latest git

* Sun Apr 24 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.1.15-4
- Update to the latest git

* Sat Apr 09 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.1.15-3
- Update to the latest git

* Sun Feb 20 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.1.15-2
- Update to the latest git

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.15-1.git3ec0a717ad.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec  5 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Update to the latest git

* Wed Oct 13 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.1.14-1
- Update to 0.1.14, drop patches

* Fri Jun 25 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.1.12-4
- Fix crash with --desktop mode when clicking volume icon
  (bug 607069)

* Thu Jun 10 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.1.12-3
- Fix an issue that pcmanfm // crashes (upstream bug 3012747)

* Fri Jun  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.1.12-2
- Fix an issue in sorting by name in cs_CZ.UTF-8 (upstream bug 3009374)

* Sat May 29 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.1.12-1
- Update to 0.1.12, drop upstreamed patches

* Sat May 29 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.1.11-7
- Fix crash of gnome-terminal wrapper with certain path settings
  (bug 596598, 597270)

* Tue May 25 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.1.11-5
- Translation update from git
- Fix an issue in sorting by name in ja_JP.UTF-8 (upstream bug 3002788)

* Sun May  9 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.1.11-4
- Translation update from git

* Fri May  7 2010 Mamrou Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.1.11-3
- Remove runpath_var=... trick on libtool which causes internal
  linkage error,
  and treak sys_lib_dlsearch_path_spec instead for rpath issue on x86_64

* Fri May  7 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.1.11-2
- Fix crash of wrapper of gnome-terminal when libfm.conf doesn't exist or so
  (bug 589730)

* Thu Apr 29 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.1.11-1
- Update to 0.1.11

* Sun Apr 18 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.10-1
- Update to 0.1.10

* Sun Mar 21 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.9-2
- Own %%{_libdir}/libfm
- Validate desktop file

* Fri Mar 19 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.9-1
- Update to 0.1.9 (Beta 1)

* Sat Mar 13 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5 (Alpha 2)

* Fri Mar 05 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.1-1
- Update to 0.1.1 (Alpha 1)

* Mon Feb 22 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1-1
- Initial packaging

