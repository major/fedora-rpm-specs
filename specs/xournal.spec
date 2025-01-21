Name:		xournal
Version:	0.4.8.2016
Release:	18%{?dist}
Summary:	Notetaking, sketching, PDF annotation and general journal

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://xournal.sourceforge.net/
Source0:	http://downloads.sourceforge.net/xournal/%{name}-%{version}.tar.gz
Patch0:		xournal-c99-1.patch
Patch1:		xournal-c99-2.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	gtk2-devel >= 2.10.0
BuildRequires:	libgnomecanvas-devel >= 2.4.0
%if 0%{?fedora} > 9 || 0%{?rhel} > 5
BuildRequires:	poppler-glib-devel >= 0.5.4
%else
BuildRequires:	poppler-devel >= 0.5.4
%endif
BuildRequires:	autoconf, automake
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick
BuildRequires:	gettext

Requires:	poppler-utils
Requires:	ghostscript

%description
Xournal is an application for notetaking, sketching, keeping a journal and
annotating PDFs. Xournal aims to provide superior graphical quality (subpixel
resolution) and overall functionality.

%prep
%autosetup -p1

NOCONFIGURE=1 ./autogen.sh

%build
CFLAGS="%optflags -DPACKAGE_LOCALE_DIR=\\\"\"%{_datadir}/locale\"\\\" -DPACKAGE_DATA_DIR=\\\"\"%{_datadir}\"\\\"" %configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"

# xournal icons and mime icons
# create 16x16, 32x32, 64x64, 128x128 icons and copy the 48x48 icon
for s in 16 32 48 64 128 ; do
	%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/
	convert -scale ${s}x${s} \
		pixmaps/%{name}.png \
		$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
	%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/${s}x${s}/mimetypes
	pushd ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/${s}x${s}/mimetypes
	%{__ln_s} ../apps/xournal.png application-x-xoj.png
	%{__ln_s} application-x-xoj.png gnome-mime-application-x-xoj.png
	popd
done

# Desktop entry
%{__install} -p -m 0644 -D pixmaps/xournal.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/xournal.png
desktop-file-install \
	--dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
	xournal.desktop

# GNOME (shared-mime-info) MIME type registration
%{__install} -p -m 0644 -D xournal.xml ${RPM_BUILD_ROOT}%{_datadir}/mime/packages/xournal.xml

# KDE (legacy) MIME type registration
%{__install} -p -m 0644 -D x-xoj.desktop ${RPM_BUILD_ROOT}%{_datadir}/mimelnk/application/x-xoj.desktop

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/xournal
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/icons/hicolor/*x*/mimetypes/application-x-xoj.png
%{_datadir}/icons/hicolor/*x*/mimetypes/gnome-mime-application-x-xoj.png
%{_datadir}/pixmaps/xournal.png
%{_datadir}/applications/xournal.desktop
%{_datadir}/mime/packages/xournal.xml
%{_datadir}/mimelnk/application/x-xoj.desktop
%{_datadir}/xournal/
%doc AUTHORS ChangeLog COPYING


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8.2016-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.8.2016-17
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8.2016-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8.2016-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8.2016-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8.2016-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec  6 2022 Florian Weimer <fweimer@redhat.com> - 0.4.8.2016-12
- Port to C99

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8.2016-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8.2016-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8.2016-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8.2016-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8.2016-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8.2016-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8.2016-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 0.4.8.2016-4
- Rebuild for poppler-0.84.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8.2016-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8.2016-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.4.8.2016-1
- Update to 0.4.8.2016.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Nathanael Noblet <nathanael@gnat.ca> - 0.4.8-11
- Fix build error by adding automake/autoconf as a BuildRequirement

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Jaromir Capik <jcapik@redhat.com> - 0.4.8-5
- Remove libgnomeprintui22-devel from BR (#1288599)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 0.4.8-3
- update desktop/icon/mime scriptlets, move autogen to %%prep

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 02 2014 Jaromir Capik <jcapik@redhat.com> - 0.4.8-1
- Upgrading to 0.4.8

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.4.7-2
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Thu Aug 16 2012 Jaromir Capik <jcapik@redhat.com> - 0.4.7-1
- Update to 0.4.7

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Jaromir Capik <jcapik@redhat.com> - 0.4.5-19
- #827922 - image insertion patch

* Wed May 16 2012 Marek Kasik <mkasik@redhat.com> - 0.4.5-18
- Rebuild (poppler-0.20.0)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.4.5-16
- rebuild(poppler)

* Fri Sep 30 2011 Marek Kasik <mkasik@redhat.com> - 0.4.5-15
- Rebuild (poppler-0.18.0)

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 0.4.5-14
- Rebuild (poppler-0.17.3)

* Tue Jul 19 2011 Nathanael Noblet <nathanael@gnat.ca> 0.4.5-13
- Add patch for depreciated poppler_page_render_to_pixbuf function removed in 0.17
 
* Sun Mar 13 2011 Marek Kasik <mkasik@redhat.com> - 0.4.5-12
- Rebuild (poppler-0.16.3)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.4.5-10
- rebuild (poppler)

* Wed Dec 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.4.5-9
- rebuild (poppler)

* Sat Nov 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.4.5-8
- rebuilt (poppler)

* Tue Oct  5 2010 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.4.5-7
- rebuild (poppler)

* Thu Aug 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.4.5-6
- rebuild (poppler)

* Tue Jun 22 2010 Matthias Clasen <mclasen@redhat.com> - 0.4.5-5
- Rebuild against new poppler

* Tue Jun 01 2010 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.4.5-4
- Add EPEL defines

* Tue Feb 16 2010 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.4.5-3
- Remove freetype patch and add general configure.in patch to
  fix implicit DSO linking

* Wed Jan 06 2010 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.4.5-2
- Added xournal-0.4.5-xoprint-len.patch to fix 64 bit systems

* Mon Oct 05 2009 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.4.5-1
- New upstream release
- Removed xournal.xml, xournal.desktop and x-xoj.desktop sources as they are now in upstream source
- Updated gtk2 devel requirements to 2.10
- Added poppler-glib-devel to BR
- Added gettext BR
- Updated summary

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.4.2.1-2
- Fix Patch0:/patch mismatch (#463069)

* Mon Apr  7 2008 Jeremy Katz <katzj@redhat.com> - 0.4.2.1-1
- Update to 0.4.2.1 to fix problems with newer xorg

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.1-4
- Autorebuild for GCC 4.3

* Wed Oct 10 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.4.1-3
- Changed permission on xournal.png from 0755 to 0644

* Fri Sep 21 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.4.1-2
- Added freetype to build requires
- Created patch to add freetype to configure.in pkgconfig

* Thu Sep 20 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.4.1-1
- New upstream release
- Changed source to use name and version variables
- Updated xournal.desktop to reflect upstream changes
- Updated x-xoj.desktop to reflect upstream changes
- Updated license to reflect specific GPL version

* Mon Jun 11 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.3.3-5
- Added Requires for poppler-utils (#243750)
- Added Requires for ghostscript

* Wed May 30 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.3.3-4
- Added optflags and PACKAGE_DATA_DIR to CFLAGS

* Tue May 29 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.3.3-3
- Changed all commands to macros
- Removed icon sources and create icons in spec from xournal icon
- Added 64x64 and 128x128 icons
- Consolidated icon directories with wildcards
- Added timestamp preservation to install
- Removed desktop categories Application and X-Fedora
- Added NOCONFIGURE to autogen.sh to stop auto-conf from running twice
- Removed desktop-file-utils post and postun requires
- Removed manual from doc section; it is already installed by the package
- Changed xournal.desktop, xournal.xml and x-xoj.desktop from here documents to files
- Add ImageMagick buildrequires for convert command
- Separated BuildRequires into one per line for easier reading
- Added PACKAGE_LOCALE_DIR CFLAG to configure

* Fri May 18 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.3.3-2
- Added mimetype support for gnome and kde
- Made xournal.desktop a here document

* Sat May 12 2007 Rick L Vinyard Jr <rvinyard@cs.nmsu.edu> 0.3.3-1
- Initial version

