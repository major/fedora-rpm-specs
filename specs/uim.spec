%global inst_xinput %{_sbindir}/update-alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_sysconfdir}/X11/xinit/xinput.d/uim.conf 50
%global uninst_xinput %{_sbindir}/update-alternatives --remove xinputrc %{_sysconfdir}/X11/xinit/xinput.d/uim.conf
%global srcver	1.9.9

%bcond_with	canna

Name:		uim
Version:	1.9.9
Release:	%autorelease
# uim itself is licensed under BSD
# scm/py.scm, helper/eggtrayicon.[ch], qt/pref-kseparator.{cpp,h}
#   and qt/chardict/chardict-kseparator.{cpp,h} is licensed under LGPLv2+
# pixmaps/*.{svg,png} is licensed under BSD or LGPLv2
License:	BSD-3-Clause AND LGPL-2.1-or-later AND (BSD-3-Clause OR LGPL-2.1-or-later)
URL:		https://github.com/uim/uim/

BuildRequires:	libXft-devel libX11-devel libXext-devel libXrender-devel libXau-devel libXdmcp-devel libXt-devel
BuildRequires:	libgcroots-devel
BuildRequires:	gtk3-devel gtk4-devel ncurses-devel
%if %{with canna}
BuildRequires:	Canna-devel
%endif
BuildRequires:	anthy-unicode-devel eb-devel gettext desktop-file-utils
BuildRequires:	wayland-devel wayland-protocols-devel
BuildRequires:	qt-devel cmake extra-cmake-modules
BuildRequires:	qt5-qtbase-devel qt5-qtbase-private-devel qt5-qtx11extras-devel
BuildRequires:	qt6-qtbase-devel qt6-qtbase-private-devel
BuildRequires:	libedit-devel sqlite-devel expat-devel
BuildRequires:	m17n-lib-devel m17n-db-devel
BuildRequires:	m17n-db m17n-db-extras
BuildRequires:	ibus-devel
BuildRequires:	emacs libtool automake autoconf intltool
BuildRequires:	protobuf3-devel
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
Requires:	%{name}-common = %{version}-%{release}
Requires:	%{name}-cli%{?_isa} = %{version}-%{release}
Requires:	(%{name}-wayland = %{version}-%{release} if libwayland-client)
Requires:	(%{name}-xorg = %{version}-%{release} if xorg-x11-server-Xorg)
Requires:	(%{name}-gtk3 = %{version}-%{release} if gtk3)
Requires:	(%{name}-gtk4 = %{version}-%{release} if gtk4)
Requires:	(%{name}-qt4 = %{version}-%{release} if qt)
Requires:	(%{name}-qt5 = %{version}-%{release} if qt5-qtbase)
Requires:	(%{name}-qt6 = %{version}-%{release} if qt6-qtbase)
Recommends:	(%{name}-anthy or %{name}-canna or %{name}-skk or %{name}-m17n or %{name}-eb)

%package	libs
Summary:	Uim Library files
Requires(post):	/sbin/ldconfig
Requires(postun): /sbin/ldconfig

%package	devel
Summary:	Development files for the Uim library
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%package	common
Summary:	Shared files for Uim packages
BuildArch:	noarch
Requires:	%{name}-libs = %{version}-%{release}
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
Requires(post):	/usr/bin/uim-module-manager
Requires(postun): /usr/bin/uim-module-manager

%package	cli
Summary:	CLI tools for Uim
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Conflicts:	%{name} < 1.9.3-1

%package	-n ibus-%{name}
Summary:	Uim engine for IBus platform
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}

%package	wayland
Summary:	Wayland support for Uim
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}

%package	xorg
Summary:	Xorg support for Uim
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Requires:	imsettings im-chooser
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%package	gtk3
Summary:	GTK+3 support for Uim
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	%{name}-gnome < 1.8.5-4
Obsoletes:	%{name}-gtk2 < 1.9.5-1

%package	gtk4
Summary:	GTK+4 support for Uim
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}

%package	qt4
Summary:	Qt4 support for Uim
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Provides:	uim-qt3 = %{version}-%{release}
Obsoletes:	uim-qt3 < 1.8.6-11
Provides:	uim-qt = %{version}-%{release}
Obsoletes:	uim-qt < 1.9.8-1

%package	qt5
Summary:	Qt5 support for Uim
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}

%package	qt6
Summary:	Qt6 support for Uim
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}

%package	eb
Summary:	EB dictionary support for Uim
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}

%package	anthy
Summary:	Anthy support for Uim
Requires:	anthy-unicode
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Requires(post):	/usr/bin/uim-module-manager
Requires(postun): /usr/bin/uim-module-manager

%if %{with canna}
%package	canna
Summary:	Canna support for Uim
Requires:	Canna
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Requires(post):	/usr/bin/uim-module-manager
Requires(postun): /usr/bin/uim-module-manager
%endif # with canna

%package	skk
Summary:	SKK support for Uim
Requires:	skkdic
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Requires(post):	/usr/bin/uim-module-manager
Requires(postun): /usr/bin/uim-module-manager

%package	m17n
Summary:	m17n-lib support for Uim
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Requires(post):	/usr/bin/uim-module-manager
Requires(postun): /usr/bin/uim-module-manager
Recommends:	m17n-db-extras

%package	mozc
Summary:	Mozc support for Uim
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Requires(post):	/usr/bin/uim-module-manager
Requires(postun): /usr/bin/uim-module-manager
Requires:	mozc


%global		common_desc	%{expand:
Uim is a multilingual input method library. Uim aims to
provide secure and useful input methods for all
languages.
}

%description
%{common_desc}
Currently, it can input to applications which
support Gtk+'s immodule, Qt's immodule and XIM.

This package provides the input method library, the XIM
bridge and most of the input methods.

For the Japanese input methods you need to install
- uim-anthy for Anthy Unicode
- uim-canna for Canna
- uim-skk for SKK.

%description	libs
%{common_desc}

This package contains the library files for Uim.

%description	devel
%{common_desc}

This package contains the header files and the libraries which is
needed for developing Uim applications.

%description	common
%{common_desc}

This package contains shared files for other uim sub packages.

%description	cli
%{common_desc}

This package contains CLI executables.

%description	-n ibus-%{name}
%{common_desc}

This package contains the uim engine for IBus.

%description	wayland
%{common_desc}

This package contains wayland support.

%description	xorg
%{common_desc}

This package contains Xorg support.

%description	gtk3
%{common_desc}

This package provides the Gtk3 IM module and helper program.

%description	gtk4
%{common_desc}

This package provides the Gtk4 IM module and helper program.

%description	qt4
%{common_desc}

This package provides the Qt4 IM module and helper programs.

%description	qt5
%{common_desc}

This package provides the Qt5 IM module and helper programs.

%description	qt6
%{common_desc}

This package provides the Qt6 IM module and helper programs.

%description	eb
%{common_desc}

This package provides the plugin for looking up EB format dictionaries.

%description	anthy
%{common_desc}

This package provides support for Anthy, a Japanese input method.

%if %{with canna}
%description	canna
%{common_desc}

This package provides support for Canna, a Japanese input method.
%endif

%description	skk
%{common_desc}

This package provides support for SKK, a Japanese input method.

%description	m17n
%{common_desc}

This package provides support for m17n-lib, which allows input of
many languages using the input table map from m17n-db.

%description	mozc
%{common_desc}

This package provides support for Mozc, a Japanese input method.


%prep
%autosetup -p1 -n uim-%{srcver}
autoconf


%build
%configure --with-x --with-xft \
	--with-libgcroots=installed \
%if %{with canna}
	--with-canna \
%endif
	--with-ibus \
	--without-anthy \
	--with-anthy-utf8 \
	--with-m17nlib \
	--with-mozc \
	--with-eb --with-eb-conf=%{_libdir}/eb.conf \
	--without-scim \
	--with-wayland \
	--with-gtk3 --enable-gnome3-applet \
	--with-gtk4 \
	--with-qt4 --with-qt4-immodule --disable-kde4-applet \
	--with-qt5 --with-qt5-immodule --disable-kde5-applet \
	--with-qt6 --with-qt6-immodule --enable-kde6-applet \
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
cp -a emacs/COPYING emacs/COPYING.emacs
cp -a emacs/README emacs/README.emacs

install -d $RPM_BUILD_ROOT%{_localstatedir}/lib/uim
touch $RPM_BUILD_ROOT%{_localstatedir}/lib/uim/{installed-modules,loader}.scm
ln -sf %{_localstatedir}/lib/uim/installed-modules.scm $RPM_BUILD_ROOT%{_datadir}/uim/
ln -sf %{_localstatedir}/lib/uim/loader.scm $RPM_BUILD_ROOT%{_datadir}/uim/

pushd $RPM_BUILD_ROOT
find . -type l | while read -r link; do
	target=$(readlink "$link")
	if [[ "$target" == /* ]]; then
		link_dir=$(dirname "$link")
		rel_target=$(realpath -m --relative-to="$link_dir" "./${target#/}")
		ln -sfn "$rel_target" "$link"
		echo "Converted: $link -> $rel_target"
	fi
done
popd

# https://fedoraproject.org/wiki/packagingDrafts/UsingAlternatives
touch $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinputrc
%find_lang %{name}

find $RPM_BUILD_ROOT -name "*.scm" -type f | egrep -v ".*/(anthy|canna|m17n|skk|wnn|installed-modules|loader)" > scm.list
cat scm.list | sed -e s,$RPM_BUILD_ROOT,,g >> %{name}.lang
find $RPM_BUILD_ROOT -name "*.png" -type f | egrep -v ".*/(anthy|canna|m17n|skk|wnn)" > png.list
cat png.list | sed -e s,$RPM_BUILD_ROOT,,g >> %{name}.lang
find $RPM_BUILD_ROOT -name "*.svg" -type f | egrep -v ".*/(anthy|canna|m17n|skk|wnn)" > svg.list
cat svg.list | sed -e s,$RPM_BUILD_ROOT,,g >> %{name}.lang


%ldconfig_post libs
%ldconfig_postun libs

%post common
/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --register tcode trycode tutcode byeoru latin pyload hangul viqr ipa-x-sampa > /dev/null 2>&1 || :

%postun common
if [ "$1" = "0" ]; then
	/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --unregister tcode trycode tutcode byeoru latin pyload hangul viqr ipa-x-sampa > /dev/null 2>&1 || :
fi

%post xorg
%{inst_xinput}

%postun xorg
if [ "$1" = "0" ]; then
	%{uninst_xinput}
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

%post mozc
/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --register mozc > /dev/null 2>&1 || :

%postun mozc
if [ "$1" = "0" ]; then
	/usr/bin/uim-module-manager --path %{_localstatedir}/lib/uim --unregister uim > /dev/null 2>&1 || :
fi


%files
%doc AUTHORS NEWS README
%license COPYING

%files libs
%doc AUTHORS NEWS README
%license COPYING
%dir %{_libdir}/uim
%dir %{_libdir}/uim/plugin
%{_libdir}/libuim-custom.so.2*
%{_libdir}/libuim-scm.so.0*
%{_libdir}/libuim.so.8*
%{_bindir}/uim-help
%{_bindir}/uim-module-manager
%{_bindir}/uim-el-agent
%{_bindir}/uim-el-helper-agent
%{_libdir}/uim/plugin/libuim-custom-enabler.so
%{_libdir}/uim/plugin/libuim-expat.so
%{_libdir}/uim/plugin/libuim-fileio.so
%{_libdir}/uim/plugin/libuim-lolevel.so
%{_libdir}/uim/plugin/libuim-look.so
%{_libdir}/uim/plugin/libuim-process.so
%{_libdir}/uim/plugin/libuim-socket.so
%{_libdir}/uim/plugin/libuim-sqlite3.so
%{_libdir}/uim/plugin/libuim-tutcode.so
%{_libexecdir}/uim-helper-server

%files wayland
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/uim-wayland
%{_datadir}/applications/uim-wayland.desktop

%files xorg
%doc AUTHORS NEWS README xim/README.xim
%license COPYING
%{_bindir}/uim-xim
%{_sysconfdir}/X11/xinit/xinput.d
%ghost %{_sysconfdir}/X11/xinit/xinputrc
%{_libdir}/uim/plugin/libuim-xkb.so
%{_mandir}/man1/uim-xim.1*

%files cli
%doc AUTHORS NEWS README fep/README.fep fep/README.fep.key
%lang(ja) %doc fep/README.fep.ja
%license COPYING
%{_bindir}/uim-custom-cli
%{_bindir}/uim-fep*
%{_bindir}/uim-im-switcher-cli
%{_libdir}/uim/plugin/libuim-editline.so

%files -f %{name}.lang common
%doc AUTHORS NEWS README
%license COPYING
%dir %{_datadir}/uim
%dir %{_datadir}/uim/lib
%dir %{_datadir}/uim/pixmaps
%dir %{_localstatedir}/lib/uim
%{_datadir}/uim/byeoru-data/byeoru-dict
%{_datadir}/uim/helperdata
%verify(not md5 size mtime) %{_datadir}/uim/installed-modules.scm
%verify(not md5 size mtime) %{_datadir}/uim/loader.scm
%ghost %{_localstatedir}/lib/uim/*.scm
%exclude %{_datadir}/uim/anthy*.scm
%exclude %{_datadir}/uim/canna*.scm
%exclude %{_datadir}/uim/m17nlib.scm
%exclude %{_datadir}/uim/mozc*.scm
%exclude %{_datadir}/uim/skk*.scm
%exclude %{_datadir}/uim/wnn*.scm
## pixmaps are licensed under BSD or LGPLv2
%exclude %{_datadir}/uim/pixmaps/anthy*.png
%exclude %{_datadir}/uim/pixmaps/canna.png
%exclude %{_datadir}/uim/pixmaps/m17n*png
%exclude %{_datadir}/uim/pixmaps/skk.png
%exclude %{_datadir}/uim/pixmaps/skk.svg
%exclude %{_datadir}/uim/pixmaps/wnn.png
%exclude %{_datadir}/uim/pixmaps/wnn.svg
%doc emacs/README.emacs
%lang(ja) %doc emacs/README.ja
%license emacs/COPYING.emacs
%{_datadir}/emacs/site-lisp/uim-el
%{_datadir}/emacs/site-lisp/site-start.d/uim-init.el
%if 0%{?fedora} < 36
%{_datadir}/xemacs/site-packages/lisp/uim-el
%{_datadir}/xemacs/site-packages/lisp/site-start.d/uim-init.el
%endif

%files	devel
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/uim-sh
%{_includedir}/uim/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%files -n ibus-%{name}
%doc AUTHORS NEWS README
%license COPYING
%{_libexecdir}/ibus-engine-uim
%{_datadir}/ibus/component/uim.xml

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

%files	gtk4
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/gtk-4.0/4.*/immodules/*.so

%files qt4
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/uim-chardict-qt4
%{_bindir}/uim-im-switcher-qt4
%{_bindir}/uim-pref-qt4
%{_bindir}/uim-toolbar-qt4
%{_libexecdir}/uim-candwin-qt4
%{_libdir}/qt4/plugins/inputmethods/libuiminputcontextplugin.so

%files qt5
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/uim-chardict-qt5
%{_bindir}/uim-im-switcher-qt5
%{_bindir}/uim-pref-qt5
%{_bindir}/uim-toolbar-qt5
%{_libexecdir}/uim-candwin-qt5
%{_libdir}/qt5/plugins/platforminputcontexts/libuimplatforminputcontextplugin.so

%files qt6
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/uim-chardict-qt6
%{_bindir}/uim-im-switcher-qt6
%{_bindir}/uim-pref-qt6
%{_bindir}/uim-toolbar-qt6
%{_libexecdir}/uim-candwin-qt6
%{_libdir}/qt6/plugins/platforminputcontexts/libuimplatforminputcontextplugin.so

%files	eb
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/uim/plugin/libuim-eb.so

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

%files mozc
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/uim-mozc-helper
%{_datadir}/uim/mozc*.scm

%changelog
%autochangelog
