%global commit e4292c8f1bd2580a44d3cbf3570a4505bd3a74b6

Summary:        GCJ-free toolkit for manipulating PDF documents
Name:           pdftk-java
Version:        3.3.3
Release:        8%{?dist}
# pdftk-java itself is GPL-2.0-or-later but uses other source codes, breakdown:
# LGPL-2.0-or-later: java/com/gitlab/pdftk_java/com/lowagie/
# APAFML: java/com/gitlab/pdftk_java/com/lowagie/text/pdf/fonts/*.{afm,txt}
# Apache-2.0: java/com/gitlab/pdftk_java/com/lowagie/text/pdf/{IntHashtable,TIFFLZWDecoder}.java
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND APAFML AND Apache-2.0
URL:            https://gitlab.com/pdftk-java/pdftk
Source0:        https://gitlab.com/pdftk-java/pdftk/-/archive/v%{version}/pdftk-%{version}.tar.gz
Patch0:         pdftk-java-3.3.1-classpath.patch
Patch1:         pdftk-java-3.3.3-bcprov-1.7x.patch
Patch2:         pdftk-java-3.3.2-bcprov-1.5x.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
BuildRequires:  ant
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  bouncycastle >= 1.70
%else
BuildRequires:  bouncycastle < 1.70
%endif
BuildRequires:  apache-commons-lang3 >= 3.3
BuildRequires:  javapackages-local
Requires:       java-headless
Requires:       bouncycastle
Requires:       apache-commons-lang3
# /usr/bin/pdftk wrapper uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
# https://gitlab.com/pdftk-java/pdftk/-/issues/109#note_668500267
Provides:       bundled(itext) = 2.1.7-4.2.0.modified_by_pdftk
Provides:       pdftk = %{version}-%{release}
Obsoletes:      pdftk < 2.03-1

%description
If PDF is electronic paper, then pdftk-java is an electronic staple-remover,
hole-punch, binder, secret-decoder-ring, and X-Ray-glasses. PDFtk is a simple
tool for doing everyday things with PDF documents: Merge PDF documents, split
PDF pages into a new document, decrypt input as necessary (password required),
encrypt output as desired, burst a PDF document into single pages, report on
PDF metrics, including metadata and bookmarks, uncompress and re-compress page
streams, and repair corrupted PDF (where possible).

Pdftk-java is a port of the original GCJ-based PDFtk to Java. The GNU Compiler
for Java (GCJ) is a portable, optimizing, ahead-of-time compiler for the Java
programming language, which had no new developments since 2009 and was finally
removed in 2016 from the GCC development tree before the release of GCC 7.

%prep
%setup -q -n pdftk-v%{version}-%{commit}
%patch -P0 -p1 -b .classpath
%if 0%{?fedora} || 0%{?rhel} >= 9
%patch -P1 -p1 -b .bcprov-1.7x
%else
%patch -P2 -p1 -b .bcprov-1.5x
%endif

%build
ant -Dant.build.javac.target=1.8 -Dant.build.javac.source=1.8 jar

%install
install -D -p -m 0644 build/jar/pdftk.jar $RPM_BUILD_ROOT%{_javadir}/pdftk.jar
install -D -p -m 0644 pdftk.1 $RPM_BUILD_ROOT%{_mandir}/man1/pdftk.1

%jpackage_script com.gitlab.pdftk_java.pdftk "" "" bcprov:commons-lang3:pdftk pdftk true

%check
# Prepare jpackage script for some tests
sed -e 's| pdftk"|"|' $RPM_BUILD_ROOT%{_bindir}/pdftk > pdftk
chmod 755 pdftk
export CLASSPATH="$RPM_BUILD_ROOT%{_javadir}/pdftk.jar"
set -euo pipefail

# Assemble (catenate) two PDF files into one
./pdftk test/files/duck.pdf test/files/duck.pdf output two-ducks.pdf
./pdftk two-ducks.pdf dump_data | grep -q "NumberOfPages: 2"

# Rotate a PDF file by 90 degrees clockwise
./pdftk test/files/duck.pdf rotate 1east output rotated-duck.pdf
./pdftk rotated-duck.pdf dump_data | grep -q "PageMediaRotation: 90"

%files
%license LICENSE license_gpl_pdftk/reference/{apache,gnu_lgpl}_license_2.txt
%license java/com/gitlab/pdftk_java/com/lowagie/text/pdf/fonts/License-Adobe.txt
%doc CHANGELOG.md README.md
%{_bindir}/pdftk
%{_javadir}/pdftk.jar
%{_mandir}/man1/pdftk.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 3.3.3-6
- Rebuilt for java-21-openjdk as system jdk

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 23 2022 Robert Scheck <robert@fedoraproject.org> 3.3.3-1
- Upgrade to 3.3.3 (#2129183)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 3.3.2-4
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.3.2-3
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Robert Scheck <robert@fedoraproject.org> 3.3.2-1
- Upgrade to 3.3.2 (#2034326)

* Fri Sep 03 2021 Robert Scheck <robert@fedoraproject.org> 3.3.1-1
- Upgrade to 3.3.1 (#2000976)
- Initial spec file for Fedora and Red Hat Enterprise Linux
