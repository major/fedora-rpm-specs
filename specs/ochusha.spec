%define		__default_patch_fuzz	2

# To create CVS based tarball, do
# cvs -z3 -d:pserver:anonymous@cvs.sourceforge.jp:/cvsroot/ochusha \
#	co \
#	-D "%%{codate} %%{cotime_JST}" \
#	ochusha
# ln -sf ochusha %%{name}-%%{main_ver}-%%{strtag}
# tar cjf %%{name}-%%{main_ver}-%%{strtag}.tar.bz2 \
#	%%{name}-%%{main_ver}-%%{strtag}/./


%define		with_system_ca_cert_file	1
%define		with_external_onig		1
%if 0%{?fedora} >= 42
%define		system_ca_cert_file		%{_sysconfdir}/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
%else
%define		system_ca_cert_file		%{_sysconfdir}/pki/tls/cert.pem
%endif
%define		help_url			file://%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}/doc/index.html

%define		main_ver	0.6.0.1
%define		codate		20100817
%define		cotime_JST	0000
%define		strtag		cvs%{codate}T%{cotime_JST}
%define		repoid		36733

%define		baserelease	20
%define		pre_release	1

%if %{pre_release}
%define		rel		0.%{baserelease}.%{strtag}%{?dist}
%else
%define		rel		%{baserelease}%{?dist}
%endif

Summary:	A GTK+ 2ch.net BBS Browser
Name:		ochusha
Version:	%{main_ver}
Release:	%{rel}
URL:		http://ochusha.sourceforge.jp/
%if %{pre_release}
Source:		%{name}-%{main_ver}-%{strtag}.tar.bz2
%else
Source:		http://downloads.sourceforge.jp/ochusha/%{repoid}/%{name}-%{version}.tar.bz2
%endif
Source10:	ochusha-prefs-gtkrc
Source11:	ochusha.sh
Patch0:		ochusha-D20100214-gtk-deprecated.patch
Patch1:		ochusha-D20100817-format-string.patch
# COPYING	BSD-2-Clause
# intl/	LGPL-2.1-or-later (unused)
# libochusha/sigslot.h	public domain (need review)
# libochushagtk_lgpl/	LGPL-2.1-or-later

# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD

Requires:	mona-fonts-VLGothic
%if 0%{?fedora} < 41
Requires:	%{system_ca_cert_file}
%endif
Requires:	xdg-utils

BuildRequires: make
BuildRequires:	gcc-c++
BuildRequires:	libtool
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libSM-devel
BuildRequires:	libXt-devel
BuildRequires:	libxml2-devel
BuildRequires:	gtk2-devel
BuildRequires:	oniguruma-devel
BuildRequires:	openssl-devel
BuildRequires:	sqlite-devel

%description
The ochusha is BBS, especially 2ch.net, browser with GUI.
It uses the GTK+ toolkit for all of its interface needs.
The ochusha offers a sort of features such as multi-level
popup view of `response's, embeded and popup view of
images that helps users to interact with BBSs.

%prep
%if %{pre_release}
%setup -q -n %{name}-%{main_ver}-%{strtag}
%else
%setup -q
%endif
#%%patch0 -p0 -b .gtk
%patch -P1 -p1 -b .format

# Icon path fix
%{__sed} -i -e 's|Icon.*$|Icon=ochusha48|' ochusha/ochusha.desktop.in

# set xdg-open as a default browser
%{__sed} -i -e 's|firefox|xdg-open|' ochusha/ui_constants.h

# Umm...
%{__sed} -i.depre -e 's|GTK_EXTRA_CFLAGS=.*|GTK_EXTRA_CFLAGS=""|' configure.ac
%{__sed} -i.depre \
	-e 's|-D[^ ][^ ]*DEPRECATED||g' \
	libochushagtk_lgpl/Makefile.am

# Support autoconf 2.7x
%if %{pre_release}
%{__sed} -i.autoconf \
	-e 's@2.6\[0-9\]@2.[67][0-9]@' \
	autogen.sh
%endif

%if %{pre_release}
sh autogen.sh
%endif

%build
export LDFLAGS="-Wl,--rpath,%{_libdir}/%{name}"
%configure \
%if %{with_external_onig}
	--with-external-oniguruma \
%endif
%if %{with_system_ca_cert_file}
	--with-ca-cert-file=%{system_ca_cert_file} \
%endif
	--with-help-url=%{help_url} \
	--bindir=%{_libexecdir} \
	--libdir=%{_libdir}/%{name}

%{__make} %{?_smp_flags} -k

%install
%{__rm} -rf %{buildroot}
%{__rm} -rf DOCs/

%{__make} \
	DESTDIR=%{buildroot} \
	INSTALL="%{__install} -p" \
	install

# find lang
%find_lang %{name}
%find_lang %{name}-properties

%{__cat} %{name}.lang %{name}-properties.lang > all.lang

# Licenses.
%{__mkdir} DOCs/
%if ! %{with_external_onig}
%{__mkdir_p} DOCs/oniguruma
%{__cp} -p DOCs/oniguruma/COPYING DOCs/oniguruma/
%endif
%{__mkdir_p} DOCs/libochushagtk_lgpl
%{__cp} -p libochushagtk_lgpl/COPYING DOCs/libochushagtk_lgpl/

# remove unneeded files
%{__rm} -f %{buildroot}/%{_libdir}/%{name}/*.{a,la,so}
%if %{with_system_ca_cert_file}
%{__rm} -f %{buildroot}/%{_datadir}/%{name}/ca-bundle.crt
%endif
pushd %{buildroot}/%{_datadir}/%{name}
rm -f *.{gif,html} \
	ochusha-* \
	ochusha.png \
	[a-np-z]*.png
popd

# Install wrapper script, default setting
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -cpm 0755 %{SOURCE11} \
	%{buildroot}%{_bindir}/%{name}
%{__install} -cpm 0644 %{SOURCE10} \
	%{buildroot}%{_datadir}/%{name}/ochusha-prefs-gtkrc

# install desktop file and delete original
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
	--delete-original \
%if 0%{?fedora} < 19
	--vendor fedora \
%endif
	--remove-category Application \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/ochusha/%{name}.desktop

# link icon to icondir according to Icon Theme Specification.
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
%{__ln_s} -f ../../../../ochusha/ochusha48.png \
	%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/

# change documents' encoding to UTF-8.
change_encoding(){

CODE=$1
shift
for f in $*
do
	%{__mv} ${f} ${f}.tmp
	iconv -f $CODE -t UTF-8 ${f}.tmp > ${f} && 
		( touch -r ${f}.tmp $f ; %{__rm} -f ${f}.tmp ) || \
		%{__mv} ${f}.tmp ${f}
done

}

change_encoding \
	EUCJP \
	BUGS ChangeLog NEWS README TODO \
	ochusha/ochusha-gtkrc.gray

# Another documents
%{__mkdir_p} DOCs/ochusha

%{__cp} -a doc/ DOCs/
%{__rm} -rf DOCs/doc/Makefile* DOCs/doc/*.in DOCs/doc/CVS/
%{__cp} -p ochusha/ochusha-* DOCs/ochusha/
%{__rm} -f DOCs/ochusha/ochusha-*.h

%files -f all.lang
%doc	ACKNOWLEDGEMENT AUTHORS 
%doc	BUGS 
%doc	COPYING ChangeLog 
%doc	NEWS 
%doc	README 
%doc	TODO
%doc	DOCs/*

%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/%{name}/
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}.1*

%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/*.png

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.20.cvs20100817T0000
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 24 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.0.1-0.19.cvs20100817T0000
- Update system ca cert file for F42
- Remove explicit file Requires per new package guidelines

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.0.1-0.18.cvs20100817T0000
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.17.cvs20100817T0000
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 31 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.0.1-0.16.cvs20100817T0000
- Rebuild for %%patch macro usage update

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.15.cvs20100817T0000.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.15.cvs20100817T0000.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.15.cvs20100817T0000.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.15.cvs20100817T0000.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.15.cvs20100817T0000.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.15.cvs20100817T0000.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.15.cvs20100817T0000.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 25 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.0.1-0.15.cvs20100817T0000
- Support autoconf 2.7x

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.11
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 30 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.6
- Rebuild for oniguruma 6.1.1

* Mon Jul 18 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.5
- Rebuild for oniguruma 6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.0.1-0.14.cvs20100817T0000.1.2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.0.1-0.14.cvs20100817T0000
- Support -Werror=format-security

* Fri Jul 26 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.6.0.1-0.13.cvs20100817T0000
- Point help URL to %%{_pkgdocdir} where available.
- Fix bogus dates in %%changelog.

* Sat Feb  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.6.0.1-0.12.cvs20100817T0000
- F-19: kill vendorization of desktop file (fpc#247)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.1-0.11.cvs20100817T0000.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.1-0.11.cvs20100817T0000.1
- Rebuilt for c++ ABI breakage

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.6.0.1-0.11.cvs20100817T0000
- F-17: rebuild against gcc47

* Wed Nov  9 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.6.0.1-0.10.cvs20100817T0000
- Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.1-0.9.cvs20100817T0000.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.0.1-0.9.cvs20100817T0000
- Update to CVS 2010-Aug-17

* Fri Jun  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.0.1-0.8.cvs20090728T0130
- Umm... just a workaround for GTK deprecated functions issue...

* Sun Feb 14 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.0.1-0.7.cvs20090728T0130
- Patch to compile with GTK 2.19.3+

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.6.0.1-0.6.cvs20090728T0130.1
- rebuilt with new openssl

* Tue Jul 28 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Update to the latest trunk

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-12: Mass rebuild

* Mon Apr 13 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Update to the latest CVS

* Mon Feb 23 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- GTK icon cache updating script update

* Mon Feb 23 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Update to the latest CVS

* Sat Feb 21 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.0.1-0.4.cvs20090221T0000
- Update to the latest CVS
- And another patch to compile with g++44

* Thu Feb  5 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.0.1-0.3.cvs20090106T1430
- Patch to compile with g++44

* Thu Jan 15 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- F-11: rebuild against new openssl

* Tue Jan  6 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Use latest CVS

* Thu Jan  1 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- A Happy New Year

* Fri Dec 26 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.0.1-0.2.cvs20081226T1200
- 2008-12-26 12:00
- Hopely fix the issue on /linux/1148809116/612
- Fix the permission of ochusha-prefs-gtkrc

* Wed Dec 24 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6-3
- 0.6
- Fix default document HTML place

* Tue Oct 28 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.99.67.1-0.4.cvs20081023T0304
- Install ochusha-prefs-gtkrc to set default font
- ... and use wrapper script

* Mon Oct 20 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.99.67.1-0.2.cvs20081020_1
- Upstream development restarted, try latest
- Use system-wide oniguruma
- Drop 2 patches (upstreamed)
- Also try to disable disable-lock-check.patch for trial
- Spec file clean up
- Move all libraries to %%_libdir/%%name, no need to make them system-wide,
  set rpath

* Sun Sep 21 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.99.66-0.6.cvs070110
- Patch to deal with occational cookie change

* Mon Jul 28 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.99.66-0.5.cvs070110
- Change Japanese fonts Requires (F-10+)

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43

* Sun Jan  6 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.5.99.66-0.4.cvs070110
- Misc fixes for g++43.

* Wed Dec  5 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.5.99.66-0.3.cvs070110
- Fix icon path in desktop file for desktop-file-utils 0.14+

* Tue Dec  4 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.5.99.66-0.2.cvs070110.dist.3
- Rebuild for new openssl (on rawhide)

* Tue Aug 21 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.5.99.66-0.2.cvs070110.dist.2
- Mass rebuild (buildID or binutils issue)

* Tue Apr 17 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.5.99.66-0.2.cvs070110
- Disable lock checking for now.

* Wed Jan 10 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.5.99.66-0.1.cvs070110
- cvs 070110 (19:20 JST)

* Sat Nov 18 2006 <fuyu@users.sourceforge.jp>
- COPYING files of oniguruma and libochushagtk_lgpl will be installed
  as COPYING.oniguruma and COPYING.libochushagtk_lgpl.

* Fri Nov 03 2006 <fuyu@users.sourceforge.jp> 0.5.99.62-1
- Version down.
- Specify the CA certificate file bundled within openssl package.

* Tue Sep 19 2006 <fuyu@users.sourceforge.jp> 0.6-1
- Version up.
- Change request fields for gtk+-2.6 and libxml2-2.6.

* Sat Aug 26 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.5.8.2-3
- Install (link) icon to the usual directory and use 
  cache updating method.

* Sat Aug 26 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.5.8.2-2
- Explicitly require Japanese fonts.

* Wed Aug 23 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 0.5.8.2-1
- Import to Fedora Extras.
- Add two patch (from 2ch BBS ochusha thread).
- Remove unnecessary .so files and desktop file installed on wrong
  location.
- Use desktop-file-install, update-desktop-database
- Add some missing BR.
- Change documents' encoding.

* Wed Dec 29 2004 <fuyu@users.sourceforge.jp> 0.5.7.1-1
- Version up.
- The ochusha.spec file is polished according to anonymous people's voice.

* Thu Nov 25 2004 <fuyu@users.sourceforge.jp> 0.5.7-1
- Version up.
- The ochusha.spec file is polished according to Matchy's advise.

* Sat Nov 13 2004 <fuyu@users.sourceforge.jp> 0.5.6-1
- Version up.
- The ochusha.spec file is now generated automatically.
- Some hardcoded build/install rules are replaced with common macros.
- Post install/uninstall rules are modified to link/unlink the
  ochusha.desktop file for menu.

* Sat Jul 03 2004 <yuhei@users.sourceforge.jp> 0.5.5-1
- Version up.

* Sun Jun 20 2004 <yuhei@users.sourceforge.jp> 0.5.4.10-1
- Version up.

* Wed Jun 16 2004 <yuhei@users.sourceforge.jp> 0.5.4.9-1
- Version up.

* Tue Jun 15 2004 <yuhei@users.sourceforge.jp> 0.5.4.8-1
- Version up.

* Mon Jun 14 2004 <yuhei@users.sourceforge.jp> 0.5.4.7-1
- Version up.

* Sun Jun 13 2004 <yuhei@users.sourceforge.jp> 0.5.4.5-1
- Version up.

* Sat Jun 12 2004 <yuhei@users.sourceforge.jp> 0.5.4.4-1
- Version up.

* Sun Jun 06 2004 <yuhei@users.sourceforge.jp> 0.5.4.3-1
- Version up.

* Mon May 24 2004 <yuhei@users.sourceforge.jp> 0.5.4.2-1
- Version up.

* Mon May 17 2004 <yuhei@users.sourceforge.jp> 0.5.4.1-1
- Version up.

* Sun May 02 2004 <yuhei@users.sourceforge.jp> 0.5.2-1
- Version up.

* Sat Apr 10 2004 <yuhei@users.sourceforge.jp> 0.5.1-1
- Version up.
- Added manfile to filelist.
- Added mandir option to configure script.

* Mon Mar 01 2004 <yuhei@users.sourceforge.jp> 0.5-1
- Version up.
- Changed filelist.

* Wed Jan 28 2004 <yuhei@users.sourceforge.jp> 0.4.10.3-1
- Version up.

* Fri Jan 23 2004 <yuhei@users.sourceforge.jp> 0.4.10.1-1
- Version up.

* Wed Jan 21 2004 <yuhei@users.sourceforge.jp> 0.4.10-1
- Version up.

* Sun Jan 18 2004 <yuhei@users.sourceforge.jp> 0.4.9.7-1
- Version up.

* Sat Jan 17 2004 <yuhei@users.sourceforge.jp> 0.4.9.6-1
- Version up.

* Fri Jan 16 2004 <yuhei@users.sourceforge.jp> 0.4.9.5-1
- Version up.

* Wed Jan 14 2004 <yuhei@users.sourceforge.jp> 0.4.9.4-1
- Version up.

* Wed Jan 14 2004 <yuhei@users.sourceforge.jp> 0.4.9.3-1
- Version up.

* Tue Jan 13 2004 <yuhei@users.sourceforge.jp> 0.4.9.2-1
- Version up.

* Mon Jan 12 2004 <yuhei@users.sourceforge.jp> 0.4.9.1-1
- Version up.

* Thu Jan 01 2004 <yuhei@users.sourceforge.jp> 0.4.8.2-1
- Version up.

* Wed Dec 31 2003 <yuhei@users.sourceforge.jp> 0.4.8.1-1
- Version up.

* Tue Dec 30 2003 <yuhei@users.sourceforge.jp> 0.4.8-1
- Version up.
- Added files about libtsengine.
- Added ochusha-init.scm file.
- Added to run ldconfig when (un)installing. 

* Mon Dec 29 2003 <yuhei@users.sourceforge.jp> 0.4.7.1-1
- Version up.

* Wed Dec 24 2003 <yuhei@users.sourceforge.jp> 0.4.7-1
- Version up.

* Mon Dec 22 2003 <yuhei@users.sourceforge.jp> 0.4.6-1
- Version up.

* Sun Dec 21 2003 <yuhei@users.sourceforge.jp> 0.4.5.10-1
- Version up.

* Fri Dec 19 2003 <yuhei@users.sourceforge.jp> 0.4.5.7-1
- Version up.

* Tue Dec 16 2003 <yuhei@users.sourceforge.jp> 0.4.5.6-1
- Version up.

* Tue Dec 16 2003 <yuhei@users.sourceforge.jp> 0.4.5.5-1
- Version up.

* Sun Dec 14 2003 <yuhei@users.sourceforge.jp> 0.4.5.4-1
- Version up.

* Sat Dec 13 2003 <yuhei@users.sourceforge.jp> 0.4.5.3-1
- Version up.

* Tue Dec 09 2003 <yuhei@users.sourceforge.jp> 0.4.5.1-1
- Version up.

* Sat Dec 06 2003 <yuhei@users.sourceforge.jp> 0.4.5-1
- Version up.
- Added png icon file. 
- Added gtkrc file.

* Thu Nov 27 2003 <yuhei@users.sourceforge.jp> 0.4.4.8-1
- Added xpm icon file.
- Version up.

* Fri Nov 21 2003 <yuhei@users.sourceforge.jp> 0.4.4.3-1
- Version up.

* Fri Nov 14 2003 <yuhei@users.sourceforge.jp> 0.4.4.2-1
- Version up.
- Added some libraries. 

* Mon Jun 23 2003 <yuhei@users.sourceforge.jp> 0.4.3.6-1
- Version up.

* Wed Jun 11 2003 <yuhei@users.sourceforge.jp> 0.4.3.4-1
- Version up.
- changed prefix enviromental valuable.
- changed URL.

* Mon May 19 2003 <yuhei@users.sourceforge.jp> 0.4.3.3-1
- Version up.

* Mon May 12 2003 <yuhei@users.sourceforge.jp> 0.4.3.2-1
- Version up.
- Fixed Group.

* Mon May 12 2003 <yuhei@users.sourceforge.jp> 0.4.2.1-1
- Initial build.
