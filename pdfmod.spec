%global debug_package %{nil}
Name:		pdfmod
Version:	0.9.1
Release:	28%{?dist}
Summary:	A simple application for modifying PDF documents
Summary(es):	Una simple aplicación para modificar documentos PDF
License:	GPLv2+
URL:		https://wiki.gnome.org/Attic/PdfMod
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.9/%{name}-%{version}.tar.gz
#patch for mono 2.10
#https://build.opensuse.org/package/view_file?file=pdfmod-mono-2.10.patch&package=pdfmod&project=GNOME%3AApps&srcmd5=73b47920f485d87e789da3aa86216285
Patch0:		pdfmod-mono-2.10-1.patch

ExclusiveArch: %mono_arches

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	gnome-doc-utils
BuildRequires:	desktop-file-utils
BuildRequires:	gnome-sharp-devel
BuildRequires:	gtk-sharp2-devel
BuildRequires:	mono-devel
BuildRequires:	hyena-devel
BuildRequires:	poppler-sharp-devel

Requires:	mono-core
Requires:	hyena
Requires:	poppler-sharp
Requires:	poppler-glib
Requires:	gnome-sharp

%description
You can reorder, rotate, and remove pages, export images from a document,
edit the title, subject, author, and keywords, and combine documents via
drag and drop.

%description -l es
Permite ordenar, rotar y mover páginas, exportar imágenes del documento,
editar el titulo, asunto, autor, y palabras claves, y combinar documentos
mediante arrastrar y soltar.

%prep
%setup -q
%patch0 -p1
# upstream uses 0.4 vs Fedora current 0.8
sed -i 's/libpoppler-glib\.so\.4/libpoppler-glib\.so.8/g' lib/poppler-sharp/poppler-sharp/poppler-sharp.dll.config
sed -i "s#gmcs#mcs#g" configure.ac
sed -i "s#gmcs#mcs#g" configure

%build
%configure --enable-external-poppler-sharp
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
chmod a-x %{buildroot}%{_libdir}/%{name}/poppler-sharp.dll.config
%find_lang %{name}

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://bugzilla.gnome.org/show_bug.cgi?id=736860
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">pdfmod.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Split, merge and delete pages in a PDF</summary>
  <description>
    <p>
      PDFMod is a graphical utility that allows you to split, merge and delete pages of a PDF document. You simply open a document up in PDFMod, and each page is shown in the interface, then you can delete individual pages, move the pages around (i.e. reorder them), import additional PDF documents, even rotate individual pages in your PDF.
    </p>
  </description>
  <url type="homepage">http://live.gnome.org/Apps/PdfMod</url>
  <screenshots>
    <screenshot type="default">https://wiki.gnome.org/Apps/PdfMod?action=AttachFile&amp;do=get&amp;target=pdfmod-0.9.1.png</screenshot>
  </screenshots>
</application>
EOF

%files -f %{name}.lang
%doc AUTHORS COPYING HACKING NEWS README
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome/help/%{name}
%{_datadir}/icons/hicolor/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Ismael Olea <ismael@olea.org> - 0.9.1-22
- Adding explicit gnome-sharp install dependency #1778960
- URL moved to GNOME Wiki Attic
- making lint happier

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 9 2017 Ismael Olea <ismael@olea.org> - 0.9.1-14
- Corrected URL to //wiki.gnome.org/Apps/PdfMod

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-13
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.1-10
- Rebuild (mono4)

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.9.1-9
- Add an AppData file for the software center

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 19 2013 Ismael Olea <ismael@olea.org> 0.9.1-7
- fixing a wrong date in spec
- fixing typo causing #992443

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 <ismael@olea.org> 0.9.1-4
- making rpmlint happier https://bugzilla.redhat.com/show_bug.cgi?id=834552#c2
- minor cleaning
 
* Thu Jun 21 2012 <ismael@olea.org> 0.9.1-3
- cleaning spec

* Thu Nov 10 2011 Ismael Olea <ismael@olea.org> 0.9.1-2
- Added pdfmod-mono-2.10-1.patch 
- minor building love

* Mon Mar 21 2011 Claudio Rodrigo Pereyra Diaz <claudiorodrigo@pereyradiaz.com.ar> 0.9.1-1
- Update to upstream release
- Translate spec summary and description to spanish

* Sun Oct 03 2010 Claudio Rodrigo Pereyra Diaz <claudiorodrigo@pereyradiaz.com.ar> 0.9.0-1
- Update to upstream release

* Wed Jun 09 2010 Claudio Rodrigo Pereyra Diaz <claudiorodrigo@pereyradiaz.com.ar> 0.8.3-2
- Unbundle poppler-sharp

* Wed Jun 09 2010 Claudio Rodrigo Pereyra Diaz <claudiorodrigo@pereyradiaz.com.ar> 0.8.3-1
- New upstream release

* Fri Apr 02 2010 Sebastian Dziallas <sebastian@when.com> - 0.8.1-1
- new upstream release
- don't remove libs for now
- remove gnome-sharp dependency
- add build requirements as noted in review

* Sun Feb 07 2010 Sebastian Dziallas <sebastian@when.com> - 0.8-2
- remove bundled libs
- build in release mode
- enable maintainer mode

* Sun Nov 15 2009 Sebastian Dziallas <sebastian@when.com> - 0.8-1
- initial packaging
