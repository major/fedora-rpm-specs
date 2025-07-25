%global inst_xinput %{_sbindir}/update-alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_sysconfdir}/X11/xinit/xinput.d/uim.conf 50
%global uninst_xinput %{_sbindir}/update-alternatives --remove xinputrc %{_sysconfdir}/X11/xinit/xinput.d/uim.conf
%global srcver	1.9.6

%bcond_with	canna

Name:		uim
Version:	1.9.6
Release:	2%{?dist}
# uim itself is licensed under BSD
# scm/py.scm, helper/eggtrayicon.[ch], qt/pref-kseparator.{cpp,h}
#   and qt/chardict/chardict-kseparator.{cpp,h} is licensed under LGPLv2+
# pixmaps/*.{svg,png} is licensed under BSD or LGPLv2
License:	BSD-3-Clause AND LGPL-2.1-or-later AND (BSD-3-Clause OR LGPL-2.1-or-later)
URL:		https://github.com/uim/uim/

BuildRequires:	libXft-devel libX11-devel libXext-devel libXrender-devel libXau-devel libXdmcp-devel libXt-devel
BuildRequires:	libgcroots-devel
BuildRequires:	gtk3-devel ncurses-devel
%if %{with canna}
BuildRequires:	Canna-devel
%endif
BuildRequires:	anthy-unicode-devel eb-devel gettext desktop-file-utils
BuildRequires:	qt-devel cmake
BuildRequires:	libedit-devel libcurl-devel sqlite-devel expat-devel
BuildRequires:	m17n-lib-devel m17n-db-devel
BuildRequires:	m17n-db m17n-db-extras
BuildRequires:	emacs libtool automake autoconf intltool
%if 0%{?fedora} < 36
BuildRequires:	xemacs
%endif
BuildRequires:	gcc gcc-c++
Source0:	https://github.com/uim/uim/releases/download/%{version}/uim-%{version}.tar.bz2
Source1:	xinput.d-uim
Source2:	uim-init.el
Patch1:		uim-emacs-utf8.patch
#Patch4:		uim-ftbfs.patch


Summary:	A multilingual input method library
Requires(post): %{_sbindir}/update-alternatives /sbin/ldconfig
Requires(postun): %{_sbindir}/update-alternatives /sbin/ldconfig
Requires:	imsettings im-chooser
Requires:	emacs-filesystem >= %{_emacs_version}
%if 0%{?fedora} < 36
Requires:	xemacs-filesystem >= %{_xemacs_version}
%endif
Provides:	emacs-common-%{name} <= 1.8.6-7
Obsoletes:	emacs-common-%{name} <= 1.8.6-7
Provides:	emacs-%{name} <= 1.8.6-7, emacs-%{name}-el <= 1.8.6-7
Obsoletes:	emacs-%{name} <= 1.8.6-7, emacs-%{name}-el <= 1.8.6-7
Provides:	xemacs-%{name} <= 1.8.6-7, xemacs-%{name}-el <= 1.8.6-7
Obsoletes:	xemacs-%{name} <= 1.8.6-7, xemacs-%{name}-el <= 1.8.6-7
%if %{without canna}
Obsoletes:	%{name}-canna < %{version}-%{release}
%endif

%package	devel
Summary:	Development files for the Uim library
Requires:	uim = %{version}-%{release}

%package	gtk3
Summary:	GTK+3 support for Uim
Requires:	uim = %{version}-%{release}
# for update-gtk-immodules
Requires(post):	gtk3
Requires(postun): gtk3
Obsoletes:	%{name}-gnome < 1.8.5-4
Obsoletes:	%{name}-gtk2 < 1.9.5-1

%package	qt
Summary:	Qt4 support for Uim
Provides:	uim-qt3 = %{version}-%{release}
Obsoletes:	uim-qt3 < 1.8.6-11

%if 0
%package	kde
Summary:	KDE Applet for Uim
Requires:	uim = %{version}-%{release}
Requires:	uim-qt
Provides:	uim-kde3 = %{version}-%{release}
Obsoletes:	uim-kde3 < 1.8.6-11
%endif

%package	anthy
Summary:	Anthy support for Uim
Requires:	anthy-unicode
Requires:	uim = %{version}-%{release}
Requires(post):	gtk3 /usr/bin/uim-module-manager
Requires(postun): gtk3 /usr/bin/uim-module-manager

%if %{with canna}
%package	canna
Summary:	Canna support for Uim
Requires:	Canna
Requires:	uim = %{version}-%{release}
Requires(post):	gtk3 /usr/bin/uim-module-manager
Requires(postun): gtk3 /usr/bin/uim-module-manager
%endif # with canna

%package	skk
Summary:	SKK support for Uim
Requires:	skkdic
Requires:	uim = %{version}-%{release}
Requires(post):	gtk3 /usr/bin/uim-module-manager
Requires(postun): gtk3 /usr/bin/uim-module-manager

%package	m17n
Summary:	m17n-lib support for Uim
Requires:	uim = %{version}-%{release}
Requires(post):	gtk3 /usr/bin/uim-module-manager
Requires(postun): gtk3 /usr/bin/uim-module-manager


%description
Uim is a multilingual input method library. Uim aims to
provide secure and useful input methods for all
languages. Currently, it can input to applications which
support Gtk+'s immodule, Qt's immodule and XIM.

This package provides the input method library, the XIM
bridge and most of the input methods.

For the Japanese input methods you need to install
- uim-anthy for Anthy Unicode
- uim-canna for Canna
- uim-skk for SKK.

%description	devel
Uim is a multilingual input method library. Uim aims to
provide secure and useful input methods for all
languages.

This package contains the header files and the libraries which is
needed for developing Uim applications.

%description	gtk3
Uim is a multilingual input method library. Uim aims to
provide secure and useful input methods for all
languages.

This package provides the Gtk IM module and helper program.

%description	qt
Uim is a multilingual input method library. Uim aims to
provide secure and useful input methods for all
languages.

This package provides the Qt4 IM module and helper programs.

%if 0
%description	kde
Uim is a multilingual input method library. Uim aims to
provide secure and useful input methods for all
languages.

This package provides the KDE applet.
%endif

%description	anthy
This package provides support for Anthy, a Japanese input method.

%if %{with canna}
%description	canna
This package provides support for Canna, a Japanese input method.
%endif

%description	skk
This package provides support for SKK, a Japanese input method.

%description	m17n
This package provides support for m17n-lib, which allows input of
many languages using the input table map from m17n-db.


%prep
%autosetup -p1 -n uim-%{srcver}
autoconf


%build
%configure --with-x --with-xft \
	--with-libgcroots=installed \
%if %{with canna}
	--with-canna \
%endif
	--without-anthy \
	--with-anthy-utf8 \
	--with-m17nlib \
	--with-eb --with-eb-conf=%{_libdir}/eb.conf \
	--without-scim \
	--with-gtk3 --enable-gnome3-applet \
	--with-qt4 --with-qt4-immodule \
	--enable-kde4-applet \
	--with-curl \
	--with-expat \
	--disable-openssl \
	--with-sqlite3 \
	--with-lispdir=%{_datadir}/emacs/site-lisp \
	--enable-pref \
	--enable-default-toolkit=gtk3
#sed -i -e 's/^\(hardcode_direct=\)$/\1yes/' -e 's/^\(hardcode_minus_L=\)$/\1no/' -e 's/^\(libext=\)$/\1"a"/' -e 's/^hardcode_libdir_flag_spec.*$'/'hardcode_libdir_flag_spec=" -D__LIBTOOL_IS_A_FOOL__ "/' libtool
sed -i -e 's/^\(hardcode_direct=\)$/\1no/' -e 's/^\(hardcode_minus_L=\)$/\1no/' -e 's/^\(libext=\)$/\1"a"/' libtool
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
%if 0%{?fedora} < 36
# For XEmacs
(cd emacs; make install DESTDIR=$RPM_BUILD_ROOT UIMEL_LISP_DIR=%{_datadir}/xemacs/site-packages/lisp/uim-el)
%endif

# remove .desktop file (#240706)
rm -f $RPM_BUILD_ROOT%{_datadir}/applications/uim.desktop

# remove unnecessary files
rm -rf $RPM_BUILD_ROOT%{_libdir}/lib*.la
rm -rf $RPM_BUILD_ROOT%{_libdir}/uim/plugin/*la
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/immodules/im-uim.*a
rm -rf $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/3.*/immodules/im-uim.*a
#rm -rf $RPM_BUILD_ROOT%{_libdir}/libgcroots.*
#rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gcroots.pc
#rm -rf $RPM_BUILD_ROOT%{_includedir}/gcroots.h
rm -rf $RPM_BUILD_ROOT%{_includedir}/sigscheme
rm -rf $RPM_BUILD_ROOT%{_docdir}/sigscheme
rm -rf $RPM_BUILD_ROOT%{_datadir}/uim/{installed-modules,loader}.scm
#rm -rf $RPM_BUILD_ROOT%{_libdir}/kde3/*.la
#rm -rf $RPM_BUILD_ROOT%{_datadir}/apps/kicker/applets/uimapplet.desktop
rm $RPM_BUILD_ROOT%{_datadir}/uim/scim.scm || :
rm $RPM_BUILD_ROOT%{_datadir}/uim/pixmaps/scim.{svg,png} || :

install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d
install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinput.d/uim.conf
install -d $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/site-start.d
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/site-start.d/
%if 0%{?fedora} < 36
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/lisp/site-start.d
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xemacs/site-packages/lisp/site-start.d/
%endif

cp -a fep/README fep/README.fep
cp -a fep/README.ja fep/README.fep.ja
cp -a fep/README.key fep/README.fep.key
cp -a xim/README xim/README.xim

install -d $RPM_BUILD_ROOT%{_localstatedir}/lib/uim
touch $RPM_BUILD_ROOT%{_localstatedir}/lib/uim/{installed-modules,loader}.scm
ln -sf %{_localstatedir}/lib/uim/installed-modules.scm $RPM_BUILD_ROOT%{_datadir}/uim/
ln -sf %{_localstatedir}/lib/uim/loader.scm $RPM_BUILD_ROOT%{_datadir}/uim/

# https://fedoraproject.org/wiki/packagingDrafts/UsingAlternatives
touch $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinputrc
%find_lang %{name}

find $RPM_BUILD_ROOT -name "*.scm" -type f | egrep -v ".*/(anthy|canna|m17n|mana|prime|scim|sj3|skk|wnn|installed-modules|loader)" > scm.list
cat scm.list | sed -e s,$RPM_BUILD_ROOT,,g >> %{name}.lang
find $RPM_BUILD_ROOT -name "*.png" -type f | egrep -v ".*/(anthy|canna|m17n|mana|prime|scim|sj3|skk|wnn)" > png.list
cat png.list | sed -e s,$RPM_BUILD_ROOT,,g >> %{name}.lang
find $RPM_BUILD_ROOT -name "*.svg" -type f | egrep -v ".*/(anthy|canna|m17n|mana|prime|scim|sj3|skk|wnn)" > svg.list
cat svg.list | sed -e s,$RPM_BUILD_ROOT,,g >> %{name}.lang


%post
/sbin/ldconfig
%{inst_xinput}
/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --register tcode trycode tutcode byeoru latin pyload hangul viqr ipa-x-sampa > /dev/null 2>&1 || :

%postun
/sbin/ldconfig
if [ "$1" = "0" ]; then
	%{uninst_xinput}
	/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --unregister tcode trycode tutcode byeoru latin pyload hangul viqr ipa-x-sampa > /dev/null 2>&1 || :
fi

%post anthy
# since F-13
## get rid of anthy for inconvenience, because anthy-utf8 is default now.
/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --unregister anthy > /dev/null 2>&1 || :
/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --register anthy-utf8 > /dev/null 2>&1 || :

%postun anthy
if [ "$1" = "0" ]; then
	/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --unregister anthy-utf8 > /dev/null 2>&1 || :
fi

%if %{with canna}
%post canna
/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --register canna > /dev/null 2>&1 || :

%postun canna
if [ "$1" = "0" ]; then
	/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --unregister canna > /dev/null 2>&1 || :
fi
%endif

%post skk
/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --register skk > /dev/null 2>&1 || :

%postun skk
if [ "$1" = "0" ]; then
	/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --unregister skk > /dev/null 2>&1 || :
fi

%post m17n
/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --register m17nlib > /dev/null 2>&1 || :

%postun m17n
if [ "$1" = "0" ]; then
	/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --unregister m17nlib > /dev/null 2>&1 || :
fi


%files -f %{name}.lang
%doc AUTHORS NEWS README fep/README.fep fep/README.fep.key xim/README.xim
%license COPYING
%lang(ja) %doc fep/README.fep.ja
%dir %{_libdir}/uim
%dir %{_libdir}/uim/plugin
%dir %{_datadir}/uim
%dir %{_datadir}/uim/lib
%dir %{_datadir}/uim/pixmaps
%dir %{_localstatedir}/lib/uim
%{_bindir}/uim-fep*
%{_bindir}/uim-help
%{_bindir}/uim-module-manager
%{_bindir}/uim-sh
%{_bindir}/uim-xim
%{_libdir}/libuim-custom.so.2*
%{_libdir}/libuim-scm.so.0*
%{_libdir}/libuim.so.8*
%{_datadir}/uim/byeoru-data/byeoru-dict
%{_datadir}/uim/helperdata
%{_datadir}/uim/tables/*.table
%verify(not md5 size mtime) %{_datadir}/uim/installed-modules.scm
%verify(not md5 size mtime) %{_datadir}/uim/loader.scm
%ghost %{_localstatedir}/lib/uim/*.scm
%exclude %{_datadir}/uim/anthy*.scm
%exclude %{_datadir}/uim/canna*.scm
%exclude %{_datadir}/uim/m17nlib.scm
%exclude %{_datadir}/uim/mana*.scm
%exclude %{_datadir}/uim/prime*.scm
%exclude %{_datadir}/uim/scim.scm
%exclude %{_datadir}/uim/sj3*.scm
%exclude %{_datadir}/uim/skk*.scm
%exclude %{_datadir}/uim/wnn*.scm
## pixmaps are licensed under BSD or LGPLv2
%exclude %{_datadir}/uim/pixmaps/anthy*.png
%exclude %{_datadir}/uim/pixmaps/canna.png
%exclude %{_datadir}/uim/pixmaps/m17n*png
%exclude %{_datadir}/uim/pixmaps/mana.png
%exclude %{_datadir}/uim/pixmaps/mana.svg
%exclude %{_datadir}/uim/pixmaps/prime*.png
%exclude %{_datadir}/uim/pixmaps/prime*.svg
%exclude %{_datadir}/uim/pixmaps/scim.png
%exclude %{_datadir}/uim/pixmaps/scim.svg
%exclude %{_datadir}/uim/pixmaps/sj3.png
%exclude %{_datadir}/uim/pixmaps/sj3.svg
%exclude %{_datadir}/uim/pixmaps/skk.png
%exclude %{_datadir}/uim/pixmaps/skk.svg
%exclude %{_datadir}/uim/pixmaps/wnn.png
%exclude %{_datadir}/uim/pixmaps/wnn.svg
%{_sysconfdir}/X11/xinit/xinput.d
%ghost %{_sysconfdir}/X11/xinit/xinputrc
%{_libdir}/uim/plugin/libuim-curl.so
%{_libdir}/uim/plugin/libuim-custom-enabler.so
%{_libdir}/uim/plugin/libuim-eb.so
%{_libdir}/uim/plugin/libuim-editline.so
%{_libdir}/uim/plugin/libuim-expat.so
%{_libdir}/uim/plugin/libuim-fileio.so
%{_libdir}/uim/plugin/libuim-lolevel.so
%{_libdir}/uim/plugin/libuim-look.so
%{_libdir}/uim/plugin/libuim-process.so
%{_libdir}/uim/plugin/libuim-socket.so
%{_libdir}/uim/plugin/libuim-sqlite3.so
%{_libdir}/uim/plugin/libuim-xkb.so
%{_libexecdir}/uim-helper-server
%{_mandir}/man1/uim-xim.1*
%doc emacs/README
%lang(ja) %doc emacs/README.ja
%license emacs/COPYING
%{_bindir}/uim-el-agent
%{_bindir}/uim-el-helper-agent
%{_datadir}/emacs/site-lisp/uim-el
%{_datadir}/emacs/site-lisp/site-start.d/uim-init.el
%if 0%{?fedora} < 36
%{_datadir}/xemacs/site-packages/lisp/uim-el
%{_datadir}/xemacs/site-packages/lisp/site-start.d/uim-init.el
%endif

%files	devel
%doc AUTHORS NEWS README
%license COPYING
%{_includedir}/uim/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%files	gtk3
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/uim-im-switcher-gtk3
%{_bindir}/uim-input-pad-ja-gtk3
%{_bindir}/uim-pref-gtk3
%{_bindir}/uim-toolbar-gtk3
%{_bindir}/uim-toolbar-gtk3-systray
%{_libdir}/gtk-3.0/3.*/immodules/*.so
%{_libexecdir}/uim-candwin-gtk3
%{_libexecdir}/uim-candwin-horizontal-gtk3
%{_libexecdir}/uim-candwin-tbl-gtk3

%files qt
%doc AUTHORS NEWS
%license COPYING
%{_bindir}/uim-chardict-qt4
%{_bindir}/uim-im-switcher-qt4
%{_bindir}/uim-pref-qt4
%{_bindir}/uim-toolbar-qt4
%{_libexecdir}/uim-candwin-qt4
%{_libdir}/qt4/plugins/inputmethods/libuiminputcontextplugin.so

%if 0
%files	kde
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/kde4/plasma_applet_uim.so
%{_datadir}/kde4/services/plasma-applet-uim.desktop
%endif

%files	anthy
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/uim/plugin/libuim-anthy-utf8.so
%{_datadir}/uim/anthy*.scm
# BSD or LGPLv2
%{_datadir}/uim/pixmaps/anthy*.png
%dir %{_datadir}/uim

%if %{with canna}
%files	canna
%doc AUTHORS NEWS README
%license COPYING
%{_datadir}/uim/canna*.scm
# BSD or LGPLv2
%{_datadir}/uim/pixmaps/canna.png
%dir %{_datadir}/uim
%endif

%files	skk
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/uim/plugin/libuim-skk.so
%{_datadir}/uim/skk*.scm
%{_datadir}/uim/pixmaps/skk*.png
%{_datadir}/uim/pixmaps/skk*.svg
%dir %{_datadir}/uim

%files m17n
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/uim-m17nlib-relink-icons
%{_libdir}/uim/plugin/libuim-m17nlib.so
%{_datadir}/uim/m17nlib.scm
%{_datadir}/uim/m17nlib-custom.scm
# BSD or LGPLv2
%{_datadir}/uim/pixmaps/m17n*png
%dir %{_datadir}/uim

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun  3 2025 Akira TAGOH <tagoh@redhat.com> - 1.9.6-1
- New upstream release.
  Resolves: rhbz#2366917

* Tue May 13 2025 Akira TAGOH <tagoh@redhat.com> - 1.9.5-1
- New upstream release.
  Resolves: rhbz#2363935
- Upstream dropped gtk2 support.

* Fri Apr 18 2025 Akira TAGOH <tagoh@redhat.com> - 1.9.1-1
- New upstream release.
  Resolves: rhbz#2359276

* Sat Mar 22 2025 Takao Fujiwara <tfujiwar@redhat.com> - 1.9.0-2
- Replace anthy with anthy-unicode

* Tue Feb 25 2025 Akira TAGOH <tagoh@redhat.com> - 1.9.0-1
- New upstream release.
  Resolves: rhbz#2347165
- Disable OpenSSL support.
  OpenSSL plugin isn't packaged. should be no harm.

* Wed Jan 29 2025 Akira TAGOH <tagoh@redhat.com> - 1.8.9-10
- Fix FTBFS
  Resolves: rhbz#2341480

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 28 2023 Akira TAGOH <tagoh@redhat.com> - 1.8.9-6
- Fix symbol error on Emacs 29.
  Resolves: rhbz#2251120

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec  5 2022 Akira TAGOH <tagoh@redhat.com> - 1.8.9-3
- Convert License tag to SPDX.

* Tue Nov 29 2022 Florian Weimer <fweimer@redhat.com> - 1.8.9-2
- Port configure script to C99

* Thu Aug 25 2022 Akira TAGOH <tagoh@redhat.com> - 1.8.9-1
- New upstream release.
  Resolves: rhbz#2119935

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-11.20200828git0c2fbfa6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-10.20200828git0c2fbfa6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov  9 2021 Jerry James <loganjerry@gmail.com> - 1.8.8-9.20200828git0c2fbfa6
- Drop XEmacs support in F36 and later

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-8.20200828git0c2fbfa6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-7.20200828git0c2fbfa6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Akira TAGOH <tagoh@redhat.com> - 1.8.8-6.20200828git0c2fbfa6
- Rebase to snapshot of git 0c2fbfa6.
- Fix aborting in emacs.
  Resolves: rhbz#1872512

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Akira TAGOH <tagoh@redhat.com> - 1.8.8-1
- New upstream release.

* Wed Nov 07 2018 Akira TAGOH <tagoh@redhat.com> - 1.8.6-20
- Add Obsoletes: uim-canna to uim package. (#1635455)

* Tue Aug 28 2018 Akira TAGOH <tagoh@redhat.com> - 1.8.6-19
- Make canna subpackage conditional.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 27 2018 Akira TAGOH <tagoh@redhat.com> - 1.8.6-17
- Add BR: gcc gcc-c++
- Fix the buffer overflow. (#1549478)

* Wed Feb 14 2018 Akira TAGOH <tagoh@redhat.com> - 1.8.6-16
- Fix the build fail.
- Disable uim-kde sub-package.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.6-14
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Akira TAGOH <tagoh@redhat.com> - 1.8.6-11
- Fix FTBFS. (#1424232)
- Drop uim-qt3/uim-kde3 sub-packages due to the build issue.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Akira TAGOH <tagoh@redhat.com>
- Use %%global instead of %%define.

* Wed Jun 24 2015 Akira TAGOH <tagoh@redhat.com> - 1.8.6-8
- Merge emacs sub-packages into main (#1234580)
- Revert the icon path for m17n

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 11 2014 Akira TAGOH <tagoh@redhat.com> - 1.8.6-5
- Fix FTBFS (#1107024)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep  3 2013 Akira TAGOH <tagoh@redhat.com> - 1.8.6-3
- Drop older Obsoletes and Conflicts lines (#1002125)
- Rebuilt against the latest eb.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul  5 2013 Akira TAGOH <tagoh@redhat.com> - 1.8.6-1
- New upstream release. (#981433)

* Mon Apr 22 2013 Akira TAGOH <tagoh@redhat.com> - 1.8.5-4
- Obsoletes uim-gnome. (#953986)

* Mon Apr 15 2013 Akira TAGOH <tagoh@redhat.com> - 1.8.5-3
- Create a socket file under XDG_RUNTIME_DIR. (#924005)

* Sun Apr 14 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.8.5-1
- Drop gnome-panel support as it's obsolete with gnome 3.8

* Mon Apr  1 2013 Akira TAGOH <tagoh@redhat.com> - 1.8.5-1
- New upstream release. (#946901)

* Wed Feb 20 2013 Akira TAGOH <tagoh@redhat.com> - 1.8.4-3
- Fix a crash issue in GTK+ immodule. (#879499)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan  4 2013 Akira TAGOH <tagoh@redhat.com> - 1.8.4-1
- New upstream release. (#890990)

* Mon Oct  1 2012 Akira TAGOH <tagoh@redhat.com> - 1.8.3-1
- New upstream release. (#861738)

* Tue Jul 31 2012 Akira TAGOH <tagoh@redhat.com> - 1.8.2-1
- New upstream release. (#844144)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun  5 2012 Akira TAGOH <tagoh@redhat.com> - 1.8.1-1
- New upstream release. (#828281)

* Mon Apr  2 2012 Akira TAGOH <tagoh@redhat.com> - 1.8.0-1
- New upstream release. (#808727)

* Fri Feb 17 2012 Akira TAGOH <tagoh@redhat.com> - 1.7.3-1
- New upstream release. (#790407)

* Wed Jan 18 2012 Akira TAGOH <tagoh@redhat.com> - 1.7.2-1
- New upstream release.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.7.1-3
- Rebuild for new libpng

* Mon Aug  8 2011 Akira TAGOH <tagoh@redhat.com> - 1.7.1-2
- check if gtk3 version of the prefs tool and immodule is available.

* Thu Aug  4 2011 Akira TAGOH <tagoh@redhat.com> - 1.7.1-1
- New upstream release.

* Tue May 24 2011 Akira TAGOH <tagoh@redhat.com> - 1.7.0-1
- New upstream release.

* Wed May 11 2011 Akira TAGOH <tagoh@redhat.com> - 1.7.0-0.1.20110511svn
- Update to the snapshot for gtk3 support.

* Tue Mar 22 2011 Akira TAGOH <tagoh@redhat.com> - 1.6.1-3
- backport patch from upstream to fix the modeline issue with
  other leim-enabled IM on Emacs.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Akira TAGOH <tagoh@redhat.com> - 1.6.1-1
- New upstream release.

* Thu Aug 12 2010 Akira TAGOH <tagoh@redhat.com> - 1.6.0-1
- new upstream release.

* Mon Mar 15 2010 Akira TAGOH <tagoh@redhat.com> - 1.5.7-3
- Use anthy-utf8 instead of anthy.
- Set the appropriate encoding for uim.el.

* Mon Feb 15 2010 Akira TAGOH <tagoh@redhat.com> - 1.5.7-2
- Fix the implicit DSO Linking issue. (#565169)

* Fri Dec 18 2009 Akira TAGOH <tagoh@redhat.com> - 1.5.7-1
- New upstream release.
  - Fix a crash in firefox. (#543813)
- uim-1.4.2-emacs23.patch: removed. it's not needed anymore.

* Mon Aug 31 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.5.6-2
- F-12: Rebuild against new eb

* Fri Aug 14 2009 Akira TAGOH <tagoh@redhat.com> - 1.5.6-1
- New upstream release.
- Remove patches because it has been applied in this release.
  - uim-qt-destdir.patch
  - uim-1.5.5-applet.patch
- Update the usage of alternatives according to PackagingDrafts/UsingAlternatives.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Akira TAGOH <tagoh@redhat.com> - 1.5.5-1
- New upstream release.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 10 2008 Akira TAGOH <tagoh@redhat.com> - 1.5.3-1
- New upstream release.
- Add im-chooser to Requires again.

* Fri Aug 29 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.5.2-2
- Include directories /usr/share/uim/pixmaps and /usr/share/uim/lib

* Mon Aug 11 2008 Akira TAGOH <tagoh@redhat.com> - 1.5.2-1
- New upstream release.

* Tue Jul 15 2008 Akira TAGOH <tagoh@redhat.com> - 1.5.0-4
- Requires: imsettings instead of im-chooser.
- Add ICON parameter to uim.conf.
- Use Qt implementation of candidate window if the desktop
  session is KDE.
- set the appropriate immodule for multilib as scim does.

* Mon Jul 14 2008 Akira TAGOH <tagoh@redhat.com> - 1.5.0-3
- Add missing files. (#454957)

* Wed Jun  4 2008 Akira TAGOH <tagoh@redhat.com> - 1.5.0-2
- Obsoletes uim-el and uim-el-common.

* Thu May 22 2008 Akira TAGOH <tagoh@redhat.com> - 1.5.0-1
- New upstream release.
- Add xemacs-uim sub-package.
- Qt4 immodule is available in uim-qt now. (#440172)
- Build with --with-anthy-utf8 and --with-eb.
- Rename uim-el and uim-el-common to emacs-uim and emacs-common-uim.

* Tue Apr 22 2008 Akira TAGOH <tagoh@redhat.com> - 1.4.2-3
- uim-1.4.2-emacs23.patch: Apply to get uim.el working on Emacs 23. (#443572)

* Wed Apr  2 2008 Akira TAGOH <tagoh@redhat.com> - 1.4.2-2
- Move Qt3 immodule plugin to uim-qt3.
- Move the helper applications for Qt to uim-qt-common.
- Rebuild against qt3-devel. (#440870)

* Wed Mar  5 2008 Akira TAGOH <tagoh@redhat.com> - 1.4.2-1
- New upstream release.
- Remove patches because of no longer needed.
  - uim-1.4.1-m17n-not-list-nil-im.patch
  - uim-1.4.1-gcc43.patch
- Remove libgcroots.so.* (#436751)

* Thu Jan 31 2008 Akira TAGOH <tagoh@redhat.com> - 1.4.1-11
- Use full path to bring up XIM server.
- uim-1.4.1-gcc43.patch: Fix a build fail with gcc-4.3.

* Wed Oct 31 2007 Akira TAGOH <tagoh@redhat.com>
- Update the upstream URL.

* Fri Sep 28 2007 Akira TAGOH <tagoh@redhat.com> - 1.4.1-9
- Add Requires: uim-gtk2 in uim-gnome.

* Thu Sep 20 2007 Akira TAGOH <tagoh@redhat.com> - 1.4.1-8
- Add Requires: im-chooser and drop xorg-x11-xinit dependency. (#297231)
- Correct License tag. (Todd Zullinger)

* Mon Sep 10 2007 Akira TAGOH <tagoh@redhat.com> - 1.4.1-7
- Update the xinput script to support the new im-chooser.
  - bring up uim-toolbar-gtk-systray as the auxiliary program
  - support the config button.

* Mon Aug 20 2007 Akira TAGOH <tagoh@redhat.com> - 1.4.1-6
- uim-1.4.1-m17n-not-list-nil-im.patch: Fix appearing m17n-nil IME and crashing
  when it's selected. (#235331)

* Fri Aug 10 2007 Akira TAGOH <tagoh@redhat.com> - 1.4.1-5
- Update License tag.
- Update BuildReq.

* Tue May 29 2007 Akira TAGOH <tagoh@redhat.com> - 1.4.1-4
- Remove uim.desktop file. (#240706)

* Tue Apr  3 2007 Akira TAGOH <tagoh@redhat.com> - 1.4.1-3
- Register/Unregister the modules at %%post/%%postun. (#234804)
- Add X-GNOME-PersonalSettings to the desktop file categories.

* Mon Mar 26 2007 Akira TAGOH <tagoh@redhat.com> - 1.4.1-2
- Own %%{_libdir}/uim/plugin. (#233817)

* Mon Mar 19 2007 Akira TAGOH <tagoh@redhat.com> - 1.4.1-1
- New upstream release.
- add m17n-db-* and gettext to BR.

* Tue Jan 30 2007 Akira TAGOH <tagoh@redhat.com> - 1.4.0-1
- New upstream release.

* Mon Dec 18 2006 Akira TAGOH <tagoh@redhat.com> - 1.3.0-1
- New upstream release.

* Fri Sep 15 2006 Akira TAGOH <tagoh@redhat.com> - 1.2.1-2
- rebuilt

* Fri Sep  1 2006 Akira TAGOH <tagoh@redhat.com> - 1.2.1-1
- New upstream release.

* Fri Aug  4 2006 Akira TAGOH <tagoh@redhat.com> - 1.2.0-1
- New upstream release.

* Mon Jul 24 2006 Akira TAGOH <tagoh@redhat.com> - 1.1.1-2
- install a xinput file with .conf suffix.

* Fri Jul  7 2006 Akira TAGOH <tagoh@redhat.com> - 1.1.1-1
- New upstream release.

* Wed Jul  5 2006 Akira TAGOH <tagoh@redhat.com> - 1.1.0-2
- use %%{_host} not %%{_target_platform} for update-gtk-immodules.
- add PreReq: gtk2 >= 2.9.1-2 and ignore update-gtk-immodules errors.
- follow the new xinput.sh and added Requires: xorg-x11-xinit >= 1.0.2-5.fc6.
- removed the unnecessary %%post and %%postun.

* Mon Jun 19 2006 Akira TAGOH <tagoh@redhat.com> - 1.1.0-1
- New upstream release.

* Thu Mar  2 2006 Akira TAGOH <tagoh@redhat.com> - 1.0.1-2
- rebuilt.

* Tue Dec 27 2005 Akira TAGOH <tagoh@redhat.com> - 1.0.1-1
- New upstream release.

* Fri Dec 16 2005 Akira TAGOH <tagoh@redhat.com> - 1.0.0-0.2.beta
- updates to 1.0.0-beta.

* Thu Dec 15 2005 Akira TAGOH <tagoh@redhat.com> - 1.0.0-0.1.alpha
- New upstream release.
- added uim-m17n package. (#175600)
- added uim-el package.
- uim-0.4.6-dont-require-devel-pkgs.patch: removed.

* Fri Sep 30 2005 Akira TAGOH <tagoh@redhat.com> - 0.4.9.1-1
- New upstream release.

* Wed Aug 17 2005 Akira TAGOH <tagoh@redhat.com> - 0.4.8-1
- New upstream release.

* Thu Aug  4 2005 Akira TAGOH <tagoh@redhat.com> - 0.4.7.1-2
- removed Requires: Canna-devel from uim-canna. this is no longer needed
  since 0.4.6-4. (Warren Togami, #165088)

* Wed Aug  3 2005 Akira TAGOH <tagoh@redhat.com> - 0.4.7.1-1
- New upstream release.

* Tue Jul 12 2005 Akira TAGOH <tagoh@redhat.com> - 0.4.7-1
- New upstream release.
- removed the patches. fixed in upstream.
  - uim-0.4.6-multilib.patch
  - uim-0.4.6-fix-typo-in-configure.patch

* Wed Jun 29 2005 Akira TAGOH <tagoh@redhat.com> - 0.4.6-5
- built with --without-scim explicitly. it doesn't work actually.

* Mon Jun 13 2005 Akira TAGOH <tagoh@redhat.com> - 0.4.6-4
- uim-0.4.6-fix-typo-in-configure.patch: applied to get uim-pref-gtk building.
- uim-0.4.6-dont-require-devel-pkgs.patch: applied to be able to dlopen
  the shared libraries without -devel packages.

* Mon May 16 2005 Akira TAGOH <tagoh@redhat.com> - 0.4.6-3
- uim-0.4.6-multilib.patch: applied to fix a build issue for
  libquiminputcontextplugin.so. (John Thacker, #156880)

* Fri May  6 2005 Akira TAGOH <tagoh@redhat.com> - 0.4.6-2
- added BuildRequires: ncurses-devel. (#156880)

* Mon Apr 18 2005 Akira TAGOH <tagoh@redhat.com> - 0.4.6-1
- New upstream release. (#155173)
  - fixed missing return statement issue. (#150304)
- Updated upstream URL.
- ensure to build with Canna and anthy.
- enabled Qt immodule.
- added QT_IM_MODULE=uim to xinput.d-uim

* Fri Apr  1 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.4.5.1-2
- Include headers directory in -devel package.

* Fri Mar  4 2005 Ville Skyttä <ville.skytta at iki.fi>
- Split context marked dependency syntax to work around #118773.
- Add ldconfig scriptlet dependencies.

* Thu Feb 24 2005 Akira TAGOH <tagoh@redhat.com> - 0.4.5.1-1
- New upstream release.
  - security fix.
- support xinput script.

* Sun Feb 20 2005 Thorsten Leemhuis <fedora[AT]leemhuis[dot]info> 0.4.5-2
- Added autoreconf-patch; fixes build on x86_64

* Wed Jan 12 2005 Akira TAGOH <tagoh@redhat.com> 0.4.5-1
- New upstream release.

* Wed Sep 08 2004 Akira TAGOH <tagoh@redhat.com> 0.4.3-1
- New upstream release.
- moved out gtk2 related files to uim-gtk2 package.

* Mon Jul 12 2004 Jens Petersen <petersen@redhat.com> - 0.4.0-1
- no longer need to remove screen files
- include console fep programs

* Fri Jul  2 2004 Jens Petersen <petersen@redhat.com> - 0.3.9-3
- support both update-gtk-immodules of newer gtk2 and older
  gtk-query-immodules-2.0 with new %%gtk_im_update added

* Wed Jun 30 2004 Jens Petersen <petersen@redhat.com> - 0.3.9-2
- add uim-applet-category-cjk.patch to put applet in right submenu
- improve the summaries and descriptions
- make the Requires(postun) be Requires(post,postun)
- file ownership and other minor cleanup

* Wed Jun 23 2004 Akira TAGOH <tagoh@redhat.com> 0.3.9-1
- New upstream release.

* Fri Jun 04 2004 Akira TAGOH <tagoh@redhat.com> 0.3.8-4
- wrote the descriptions.
- uim-skk: fixed the dependency.

* Fri Jun 04 2004 Nils Philippsen <nphilipp@redhat.com> 0.3.8-3
- more spec cleanups

* Fri Jun 04 2004 Warren Togami <wtogami@redhat.com> 0.3.8-2
- many spec cleanups

* Thu Jun 03 2004 Akira TAGOH <tagoh@redhat.com> 0.3.8-1
- Initial package.
