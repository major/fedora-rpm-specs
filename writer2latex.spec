# rhbz#1025499 the package is technically noarch (java), but libreoffice
# does not have any arch-independent extension location
%global debug_package %{nil}

Name:          writer2latex
Version:       1.0.2
Release:       39%{?dist}
Summary:       Document Converter from ODT to LaTeX
License:       LGPLv2
Url:           http://writer2latex.sourceforge.net/
Source0:       http://writer2latex.svn.sourceforge.net/viewvc/writer2latex/tags/%{version}.tar.gz
Source1:       writer2latex.metainfo.xml
Source2:       writer2xhtml.metainfo.xml
Patch0:        writer2latex05.rh.patch
Patch1:        XDocumentPropertiesSupplier.patch
Patch2:        XDocumentPropertiesSupplier-writer2xhtml.patch
    # Path1--2 upstreamed as <https://sourceforge.net/tracker/?func=detail&
    # aid=3605657&group_id=253780&atid=1313919> "LibreOffice 4 doesn't show
    # LaTeX Options dialog upon export"
Patch3:        writer2latex-java11.patch
ExclusiveArch: %{java_arches}
BuildRequires: ant
BuildRequires: java-devel
BuildRequires: libreoffice-core
BuildRequires: osgi(javax.xml)

%global baseinstdir %{_libdir}/libreoffice

%description
Writer2LaTeX is a utility written in java. It converts LibreOffice documents
– in particular documents containing formulas – into other formats. It is
actually a collection of four converters, i.e.:
1) Writer2LaTeX converts documents into LaTeX 2e format for high quality
   typesetting.
2) Writer2BibTeX extracts bibliographic data from a document and stores it in
   BibTeX format (works together with Writer2LaTeX).
3) Writer2xhtml converts documents into XHTML 1.0 or XHTML 1.1+MathML 2.0 with
   CSS2.
4) Calc2xhtml is a companion to Writer2xhtml that converts OOo Calc documents
   to XHTML 1.0 with CSS2 to display your spreadsheets on the web.

%package java
Summary:       Java library for %{name}
BuildArch:     noarch
Requires:      osgi(javax.xml)
Suggests:      %{name}-doc
Obsoletes:     %{name} < 1.0.2-18
Provides:      %{name} = %{version}-%{release}

%description java
A java library for document conversion from ODT to LaTeX, BibTeX, XHTML,
HTML5 and EPUB.

%package doc
Summary:       User manual for %{name}
BuildArch:     noarch

%description doc
User manual for %{name}.

%package javadoc
Summary:     Javadoc for %{name}
BuildArch:   noarch

%description javadoc
Javadoc for %{name}.

%package -n libreoffice-writer2latex
Summary:   LibreOffice Writer To LateX Converter
Requires:  libreoffice-core%{?_isa}
Requires:  osgi(javax.xml)
Suggests:  %{name}-doc
Obsoletes: openoffice.org-writer2latex < 1.0.2-4

%package -n libreoffice-writer2xhtml
Summary:   LibreOffice Writer to xhtml Converter
Requires:  libreoffice-core%{?_isa}
Requires:  osgi(javax.xml)
Suggests:  %{name}-doc
Obsoletes: openoffice.org-writer2xhtml < 1.0.2-4

%description -n libreoffice-writer2latex
Document Converter Extension for LibreOffice to provide 
LaTeX and BibTeX export filters.

%description -n libreoffice-writer2xhtml
Document Converter Extension for LibreOffice to provide 
XHTML export filters.

%prep
%autosetup -n %{version} -p1
sed -i -e 's#name="OFFICE_CLASSES" location="/usr/share/java/openoffice"#name="OFFICE_CLASSES" location="%{_libdir}/libreoffice/program/classes"#' build.xml
sed -i -e 's#name="URE_CLASSES" location="/usr/share/java/openoffice"#name="URE_CLASSES" location="%{_libdir}/libreoffice/program/classes"#' build.xml

%build
ant jar javadoc oxt

%install
# jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 target/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -p -r target/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
pushd $RPM_BUILD_ROOT%{_javadocdir}
ln -s %{name}-%{version} %{name}
popd
# LibreOffice extensions
install -d -m 755 $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/writer2latex.oxt
unzip target/lib/writer2latex.oxt -d $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/writer2latex.oxt
install -d -m 755 $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/writer2xhtml.oxt
unzip target/lib/writer2xhtml.oxt -d $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/writer2xhtml.oxt
# AppData metadata
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/appdata
install -p -m 644 %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/appdata

%files java
%license source/distro/COPYING.TXT
%{_javadir}/*

%files doc
%doc source/distro/History.txt source/distro/Readme.txt source/distro/doc/user-manual.odt
%license source/distro/COPYING.TXT

%files javadoc
%license source/distro/COPYING.TXT
%{_javadocdir}/%{name}
%{_javadocdir}/%{name}-%{version}

%files -n libreoffice-writer2latex
%license source/distro/COPYING.TXT
%{baseinstdir}/share/extensions/writer2latex.oxt
%{_datadir}/appdata/writer2latex.metainfo.xml

%files -n libreoffice-writer2xhtml
%license source/distro/COPYING.TXT
%{baseinstdir}/share/extensions/writer2xhtml.oxt
%{_datadir}/appdata/writer2xhtml.metainfo.xml

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Caolán McNamara <caolanm@redhat.com> - 1.0.2-37
- Resolves: rhbz#2104111 i686 java-openjdk packages to be removed

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.2-36
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 02 2021 Caolán McNamara <caolanm@redhat.com> - 1.0.2-34
- prep for f36 mass rebuild for java-17-openjdk

* Wed Aug 04 2021 Caolán McNamara <caolanm@redhat.com> - 1.0.2-33
- Resolves: rhbz#1988047 rebuild for FTBFS

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.0.2-29
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue May 05 2020 Caolán McNamara <caolanm@redhat.com> - 1.0.2-28
- allow rebuild with java 11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 David Tardon <dtardon@redhat.com> - 1.0.2-18
- add AppData Addon metadata
- move writer2latex.jar into a noarch subpackage
- split user manual into a separate noarch subpackage

* Tue Jul 07 2015 Caolán McNamara <caolanm@redhat.com> - 1.0.2-17
- Resolves: rhbz#1240059 FTBFS with merged ure dirs

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 31 2013 David Tardon <dtardon@redhat.com> - 1.0.2-13
- Resolves: rhbz#1025499 there is no debuginfo here

* Wed Oct 23 2013 Caolán McNamara <caolanm@redhat.com> - 1.0.2-12
- Resolves: rhbz#1022169 remove versioned jars

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Stephan Bergmann <sbergman@redhat.com> - 1.0.2-10
- Resolves: rhbz#914578 FTBFS (incl. adaption to LibreOffice 4.0 API changes)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 Caolán McNamara <caolanm@redhat.com> 1.0.2-6
- Resolves: rhbz#715890 FTBFS, just use basis-link from now on

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 23 2010 Caolán McNamara <caolanm@redhat.com> 1.0.2-4
- Resolves: rhbz#645906 rebuild for LibreOffice 

* Wed Jul 14 2010 Caolán McNamara <caolanm@redhat.com> 1.0.2-3
- rebuild for OpenOffice.org 3.3

* Thu Jul 08 2010 Caolán McNamara <caolanm@redhat.com> 1.0.2-2
- add COPYING to all subpackages

* Sat Jun 05 2010 Caolán McNamara <caolanm@redhat.com> 1.0.2-1
- latest version

* Tue Mar 09 2010 Caolán McNamara <caolanm@redhat.com> 1.0.1-1
- latest version

* Mon Dec 21 2009 Caolán McNamara <caolanm@redhat.com> 1.0-3
- Preserve time stamps

* Thu Nov 19 2009 Caolán McNamara <caolanm@redhat.com> 1.0-2
- Resolves: rhbz#539035 update for OOo 3.2

* Mon Sep 21 2009 Caolán McNamara <caolanm@redhat.com> 1.0-1
- latest version

* Fri Jul 24 2009 Caolán McNamara <caolanm@redhat.com> 0.5.0.2-7
- make javadoc no-arch when building as arch-dependant aot

* Thu Feb 26 2009 Caol@n McNamara <caolanm@redhat.com> 0.5.0.2-6
- update for 3.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Caolán McNamara <caolanm@redhat.com> 0.5.0.2-4
- tweak summary

* Thu Nov 20 2008 Caolán McNamara <caolanm@redhat.com> 0.5.0.2-3
- upstream repacked tarballs to replace 0.5.0.1 with 0.5.0.2

* Mon Oct 06 2008 Caolán McNamara <caolanm@redhat.com> 0.5.0.2-2
- update for guidelines

* Wed Sep 03 2008 Caolán McNamara <caolanm@redhat.com> 0.5.0.2-1
- latest version

* Sat Aug 09 2008 Caolán McNamara <caolanm@redhat.com> 0.5-4
- use generic requires

* Mon Mar 31 2008 Caolán McNamara <caolanm@redhat.com> 0.5-3
- tweak for guidelines
- and adjust for OOo3 3 layer packaging

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.5-2
- Autorebuild for GCC 4.3

* Sat Dec 1 2007 Caolán McNamara <caolanm@redhat.com> 0.5-1
- initial version
