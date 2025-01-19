# Please check again if someone wants to import
# this also to EPEL.

# Upstream uses hg for SCM
# googlecode now no longer provide source, create
# it from SCM
#
# hg clone https://code.google.com/p/gphotoframe/
# cd gphotoframe/
# hg archive -t tbz2 "gphotoframe-<version>-hg%h.tar.bz2"

%global	hghash		2084299dffb6

%global	mainver	2.0.2
#%%define	minorver	-b1

%global	baserelease	33

%global	rpmminorver	%(echo "%minorver" | sed -e 's|^-||' | sed -e 's|\\\.||')
%global	fedorarel	%{?minorver:0.}%{baserelease}%{?minorver:.%rpmminorver}%{?hghash:.hg%hghash}

Name:		gphotoframe
Version:	%{mainver}
Release:	%{fedorarel}%{?dist}
Summary:	Photo Frame Gadget for the GNOME Desktop

# Overall	GPL-3.0-or-later
# help/C/gphotoframe.xml	GFDL-1.1-or-later
# lib/utils/EXIF.py	BSD-3-Clause
# lib/utils/urlget.py	MIT
# share/history/jquery.lazyload.js	MIT
# Some images (see COPYING)	GPL-2.0-or-later
# SPDX confirmed
License:	GPL-3.0-or-later AND GPL-2.0-or-later AND MIT AND BSD-3-Clause AND GFDL-1.1-or-later
URL:		http://code.google.com/p/gphotoframe/
#Source0:	http://gphotoframe.googlecode.com/files/%{name}-%{mainver}%{?minorver}.tar.gz
Source:	%{name}-%{mainver}%{?minorver}%{?hghash:-hg%hghash}.tar.bz2
# bug 1078155
# The following file missing
#Source1:	https://gphotoframe.googlecode.com/hg/share/assistant_facebook.glade

# Handle exif file with zero denominator on geometry information
# bug 845418
Patch2:	gphotoframe-2.0a2-parseexif-geom-zerovalue.patch
# Fix yet another case on exif information with zero denominator
# bug 885377
Patch3:	gphotoframe-1.5.1-parseexif-fraction-zerodiv.patch
# Support python-twisted 13.x API
#Patch4:	gphotoframe-2.0-a3-twisted-13-API.patch
# https://git.gnome.org/browse/gdk-pixbuf/commit/?id=112eab418137df2d2f5f97e75fb48f17e7f771e7
# gdk-pixbuf 2.31.2 changed API
Patch4:	gphotoframe-2.0.1-gdk-pixbuf2-2_31_2_API.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1296817
# disable libproxy support for now
Patch5:	gphotoframe-2.0.2-disable-libproxy.patch
# F-26+: Switch to WebKit2 (on Fedora: it is webkitgtk4)
Patch6:	gphotoframe-2.0.2-WebKit2.patch
# F-31+: Switch to python3
Patch100:	gphotoframe-2.0.2-python3.patch
# F-34: Patch to support feedparser 6
Patch101:	gphotoframe-2.0.2-feedparser-6.patch
# F-33+: Patch for python3x: bunch of fixes for plugins, mainly for authentification
Patch102:	gphotoframe-2.0.2-plugin-bunch-fix-py3x.patch
# Limit number of times for checking idle status when service is not available
# to shutdown warning
Patch103:	gphotoframe-2.0.2-idle-check-limit-time.patch
# python3x: fix for urlget
Patch104:	gphotoframe-2.0.2-urlget-py3.patch
# Move help URL according to freedesktop specification
Patch105:	gphotoframe-2.0.2-help-url-spec.patch
# Again, Patch for python3x: fixes for plugins, mainly for configuring plugins
Patch106:	gphotoframe-2.0.2-plugin-bunch-fix-py3x-02.patch
# Don't try to open file with double click on window at startup, when
# no photo is loaded yet:
# Fixes https://retrace.fedoraproject.org/faf/reports/61954/
Patch107:	gphotoframe-2.0.2-fix-double-click-at-startup.patch
# Borrow python-twisted 21.7 HTTPDownloader for now
Patch108:	gphotoframe-twisted-2107-HTTPDownloader.patch
# Port to setuptools: PEP632
Patch109:	gphotoframe-2.0.2-pep632-distutils-port.patch
# randrange argument needs to be int, python 3.12 causes error when
# argument is float
Patch110:	gphotoframe-2.0.2-python312-random-argument-int.patch
# Rescue GdkPixbuf.Pixbuf.new error
Patch111:	gphotoframe-2.0.2-gdkpixbuf_error-handling.patch
# Remove obsolete cgi module
Patch112:	gphotoframe-2.0.2-python308-remove-cgi.patch
# When loading rss is taking loong time (then aborted),
# trying to show rss photo causes exception
Patch113:	gphotoframe-2.0.2-rss-taking-long-time-exception.patch
Provides:	bundle(python3-twisted) = 21.7

BuildRequires:	GConf2
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	python3-devel
BuildRequires:	python3-distutils-extra
# For creating symlink -> python-bytecompiling
#BuildRequires:	python3-exif
# From 1.2-b6: setup.py needs this
BuildRequires:	python3-pyxdg
BuildRequires:	python3-setuptools
# Documents
BuildRequires:	%{_bindir}/xsltproc
BuildRequires:	%{_bindir}/xml2po
# F-35+: use fixed xml2po (ref: bug 2014227)
BuildRequires:	gnome-doc-utils >= 0.20.10-27

# Mandatory
Requires:	python3-gobject
#Requires:	python3-exif
Requires:	python3-twisted
# twisted favors service-identity
Requires:	python3-service-identity
# twisted/internet/ssl.py
Requires:	python3-pyOpenSSL
Requires:	python3-pyxdg
# lib/plugins/tumblr/account.py
#Requires:	python2-oauth

# girepository
Requires:	gtk3
# https://fedoraproject.org/wiki/Changes/Remove_webkit2gtk-4.0_API_Version
# Use webkit2gtk-4.1 for F-39+
%if 0%{?fedora} >= 39
Requires:		webkit2gtk4.1
%else
Requires:		webkit2gtk4.0
%endif
# Optional
# see bug 1296817
# Requires:	libproxy-python
# girepository
Requires:	clutter-gtk
Requires:	python3-feedparser
# girepository
Requires:	libchamplain-gtk
# .ico image files
%if 0%{?fedora} >= 41
Requires:	gdk-pixbuf2-modules-extra
%endif
# Scriptlets
Requires(pre):	GConf2

BuildArch:	noarch

%description
Gnome Photo Frame is a photo frame gadget for the GNOME Desktop.

%prep
%setup -q -n %{name}-%{mainver}%{?minorver}%{?hghash:-hg%hghash}

%patch -P2 -p2 -b .zeroden -Z
%patch -P3 -p1 -b .zeroden2 -Z
%patch -P4 -p1 -b .pixbuf_23102 -Z
%patch -P5 -p1 -b .libproxy_disable -Z
%patch -P6 -p1 -b .wk2 -Z

# Remove unneeded shebangs
grep -rl '^#![ \t]*%{_bindir}' lib/ | \
	xargs sed -i -e '\@^#![ \t]*%{_bindir}@d'

# install missing glade file
# bug 1078155
#cp -p %%{SOURCE1} share/
sed -i.glade \
	-e "s|'share/menu.ui',|'share/menu.ui','share/assistant_facebook.glade',|" \
	setup.py

# Explicitly don't use clutter-gtk for now
# Enable again with 2.0-a3
%if 0
grep -rl 'import clutter' lib/ | \
	xargs sed -i -e 's|import clutter|import dont_use_clutter|'
%endif

%if 0
# Use system-wide EXIF
ln -sf %{python_sitelib}/EXIF.py lib/utils/EXIF.py
%endif

# Once doing this
grep -rlZ "/usr/bin/python$" . | xargs --null sed -i -e 's|/usr/bin/python$|/usr/bin/python2|'
# Then patch
%patch -P100 -p1 -b .py3 -Z
%patch -P101 -p1 -b .feedparser6 -Z
%patch -P102 -p1 -b .bunchfix -Z
%patch -P103 -p1 -b .idle -Z
%patch -P104 -p1 -b .urlget_py3 -Z
%patch -P105 -p1 -b .helpurl -Z
%patch -P106 -p1 -b .py3_config -Z
%patch -P107 -p1 -b .open_startup -Z
%patch -P108 -p1 -Z
%patch -P109 -p1 -Z
%patch -P110 -p1 -b .py312 -Z
%patch -P111 -p1 -b .pixbuf_err -Z
%patch -P112 -p1 -b .cgi -Z
%patch -P113 -p1 -b .rss_loong -Z

%build
# Do nothing
#%%{__python} setup.py build

%install
mkdir -p %{buildroot}

%{__python3} setup.py install \
	--root %{buildroot} \
	--prefix %{_prefix} \
	%{nil}

%if 0
# And again use system-wide EXIF.py
ln -sf %{python_sitelib}/EXIF.py \
	%{buildroot}%{python_sitelib}/%{name}/utils/EXIF.py
%endif

# Gsettings Schemas
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas
install -cpm 0644 \
	share/com.googlecode.gphotoframe.gschema.xml.in \
	%{buildroot}%{_datadir}/glib-2.0/schemas/com.googlecode.gphotoframe.gschema.xml

# Desktop
desktop-file-validate \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

# Move help documents according to freedesktop specification
for lang in \
	C it ja \
	%{nil}
do
	mkdir -p %{buildroot}%{_datadir}/help/${lang}/%{name}
	mv \
		%{buildroot}%{_datadir}/gnome/help/%{name}/${lang}/* \
		%{buildroot}%{_datadir}/help/${lang}/%{name}
	if [ -f %{buildroot}%{_datadir}/help/${lang}/%{name}/%{name}.xml ]
	then
		mv \
			%{buildroot}%{_datadir}/help/${lang}/%{name}/%{name}.xml \
			%{buildroot}%{_datadir}/help/${lang}/%{name}/index.docbook
	fi
done
# Cleanups
find %{buildroot}%{_datadir}/gnome/help/ -type d | sort -r | xargs rmdir

# gnome-screensver related
# FIXME: I don't use gnome-screensaver...
mkdir -p \
	%{buildroot}%{_libexecdir}/gnome-screensaver
# ignore failure (if any) for screensaver desktop
desktop-file-validate \
	%{buildroot}%{_datadir}/applications/screensavers/gphotoframe-screensaver.desktop || true
# lib/ is hardcoded in setup.py
mv %{buildroot}%{_prefix}/lib/gnome-screensaver/gnome-screensaver/gphotoframe-screensaver \
	%{buildroot}%{_libexecdir}/gnome-screensaver/

rm -rf \
	%{buildroot}%{_libexecdir}/gnome-screensaver/ \
	%{buildroot}%{_datadir}/applications/screensavers/ \
	%{nil}

find %{buildroot}%{_prefix} -name \*.py3 -delete

%find_lang %{name}

%if 0
# Treak brp-python-bytecompile
%global	__os_install_post_orig		%{__os_install_post}
%global	__os_install_post \
	%__os_install_post_orig \
	for f in %{python_sitelib}/EXIF.py* \
	do \
		ln -sf $f %{buildroot}%{python_sitelib}/%{name}/utils/$(basename $f) \
	done \
	%{nil}
%endif

%pre
%gconf_schema_obsolete %{name}

%files	-f %{name}.lang
%defattr(-,root,root,-)
%license	COPYING
%license	GPL
%doc	README
%doc	changelog

%{_bindir}/%{name}
%{python3_sitelib}/%{name}-*.egg-info
%{python3_sitelib}/%{name}/

%dir	%{_datadir}/%{name}/
%{_datadir}/%{name}/*.ui
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.glade
%{_datadir}/%{name}/extra/
%{_datadir}/%{name}/history/

%{_datadir}/help/*/%{name}/
%{_datadir}/omf/%{name}/

#%%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_datadir}/glib-2.0/schemas/com.googlecode.%{name}.gschema.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*

%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-33.hg2084299dffb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-32.hg2084299dffb6
- Fix exception when loading rss is taking too much time

* Wed Aug 28 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-31.hg2084299dffb6
- Fix previous cgi removal patch
- Also fix Patch102 import usage

* Tue Aug 27 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-30.hg2084299dffb6
- Remove obsolete cgi module

* Mon Aug 26 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-29.hg2084299dffb6
- Require gdk-pixbuf2-modules-extra if available

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-28.hg2084299dffb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.2-27.hg2084299dffb6
- Rebuilt for Python 3.13

* Tue May 07 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-26.hg2084299dffb6
- More error handling wrt icon loading failure due to new gdk-pixbuf

* Mon Apr 22 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-25.hg2084299dffb6
- Handle GdkPixbuf.Pixbuf.new error

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-24.hg2084299dffb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-23.hg2084299dffb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 06 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-22.hg2084299dffb6
- SPDX migration

* Mon Jul 24 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-21.hg2084299dffb6
- Fix for python 3.12 rejecting non-integer arguments to randrange

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-20.hg2084299dffb6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 05 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-19.hg2084299dffb6
- Rebuild for python 3.12
- Port to setuptools: PEP632

* Sun May 07 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-18.hg2084299dffb6
- Use webkit2gtk-4.1 for F-39+
  https://fedoraproject.org/wiki/Changes/Remove_webkit2gtk-4.0_API_Version

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-17.hg2084299dffb6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug  3 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-17.hg2084299dffb6
- Use HTTPDownloader or so in python-twisted 21.7 (removed on 22.1) to
  workaround

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-16.hg2084299dffb6.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.2-16.hg2084299dffb6.2
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-16.hg2084299dffb6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 23 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-16.hg2084299dffb6
- Don't use old compatibility dependency for webkitgtk4

* Fri Oct 15 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-15.hg2084299dffb6
- Rebuild with fixed xml2po (ref: bug 2014227)

* Wed Oct 13 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-14.hg2084299dffb6
- Don't try to open file with double click on window at startup, when
  no photo is loaded yet (faf report 61954)

* Thu Aug 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-13.hg2084299dffb6
- Requires: python OpenSSL module

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-12.hg2084299dffb6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.2-12.hg2084299dffb6.1
- Rebuilt for Python 3.10

* Tue Mar 30 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-12.hg2084299dffb6
- Another fix for python3 for plugins - mainly for configuration

* Sun Mar 28 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-11.hg2084299dffb6
- Move help documentation according to freedesktop specification

* Wed Mar 17 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-10.hg2084299dffb6
- py3: fix for urlget

* Tue Mar 16 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-9.hg2084299dffb6
- python3x: bunch of fixes, mainly for plugins
- Limit number of times for checking idle status when service is not available
  to shutdown warnings

* Sat Mar 13 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-8.hg2084299dffb6
- Make tumblr plugin work again
- set timestamp when applying patch

* Fri Mar 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-7.hg2084299dffb6
- Support feedparser 6

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6.hg2084299dffb6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6.hg2084299dffb6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-6.hg2084299dffb6
- Kill gss support on F-33+

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-5.hg2084299dffb6.3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5.hg2084299dffb6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-5.hg2084299dffb6.1
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 23 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-5.hg2084299dffb6
- Switch to python3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4.hg2084299dffb6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-4.hg2084299dffb6
- Explicitly use python2 on shebang

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3.hg2084299dffb6.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3.hg2084299dffb6.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3.hg2084299dffb6.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.2-3.hg2084299dffb6.3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.2-3.hg2084299dffb6.2
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3.hg2084299dffb6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 31 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-3.hg2084299dffb6
- F-26+: switch to WebKit2 (on Fedora: webkitgtk4)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2.hg2084299dffb6.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2.hg2084299dffb6.2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2.hg2084299dffb6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-2.hg2084299dffb6
- F-23+: disable libproxy support for now (bug 1296817)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-1.hg2084299dffb6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr  3 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.2-1.hg2084299dffb6
- 2.0.2

* Thu Jan  1 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.1-3.hg0eed26d75481
- A Happy New Year
- Adjust for gdk-pixbuf 2.31.2 API

* Fri Dec  5 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.1-2.hg0eed26d75481
- Add appdata

* Tue Dec  2 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.1-1.hg82fdb3350fbd
- 2.0.1

* Wed Nov 26 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.1-0.1.b1.hga78a9b1d0cee
- 2.0.1-b1

* Sun Nov  9 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0-1.hg4fb32b74a755
- 2.0 release, and hg 1 commit ahead

* Mon Jul 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0-0.6.a3
- Support python-twisted 13.x API

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.5.a3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0-0.5.a3
- Add missing glade file for tumblr authentification (bug 1078155)

* Wed Nov 13 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0-0.4.a3
- 2.0-a3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.3.a2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.3.a2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0-0.3.a2
- Fix yet another case on exif information with zero denominator
  (bug 885377)

* Mon Aug 19 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.0-0.2.a2
- Fix traceback when choosing photo source on setting gui
- Fix traceback when choosing folder plugin on setting gui
- Handle exif file with zero denominator on geometry information

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.1.a2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.0-0.1.a2
- 2.0-a2

* Thu Mar 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.1-2
- Fix scriptlet type name

* Mon Mar  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5.1-1
- 1.5.1

* Sun Jan 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5-1
- 1.5

* Sun Jan  8 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5-0.2.rc1
- 1.5 rc1

* Tue Dec 20 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.5-0.1.b1
- 1.5 b1

* Wed Nov 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4.1-1
- 1.4.1

* Fri Nov 25 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4.1-0.1.b1
- 1.4.1-b1

* Tue Jul  5 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4-1
- 1.4

* Thu Jun 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4-0.2.rc1
- 1.4 rc1

* Sun Jun 12 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4-0.1.b2
- 1.4 b2

* Sun Apr 17 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3-1
- 1.3

* Tue Apr 12 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3-0.3.rc2
- 1.3 rc2

* Sat Apr  2 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3-0.2.b2
- 1.3 b2

* Thu Mar 24 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3-0.1.b1
- Try 1.3 b1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2-1
- 1.2 formal

* Thu Jan 27 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2-0.3.rc1
- 1.2 rc1

* Tue Jan 18 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2-0.2.b6
- Update to 1.2b6

* Mon Dec 27 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2-0.1.b4
- Update to 1.2b4
- And pull patch from hg head to fix gnome-screensaver related dbus error

* Sat Oct 23 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.1-1
- Update to 1.1

* Tue Jul 27 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-14: rebuild against python 2.7

* Sun Jul 25 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-2
- Fix license tag
- Remove unneeded macro definition

* Sat Jul 24 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0-1
- Initial packaging

