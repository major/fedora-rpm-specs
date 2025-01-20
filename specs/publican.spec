# Track font name changes
%define RHEL6 %([[ %{?dist}x == .el6[a-z]* ]] && echo 1 || echo 0)
%define RHEL7 %([[ %{?dist}x == .el7[a-z]* ]] && echo 1 || echo 0)

# BUGBUG BZ #1144220 work around wrong entity string bug
%define DBPATH %(find /usr/share/sgml/docbook/xml-dtd-4.5*/dbcentx.mod)

%define OTHER 1
%if %{RHEL6}
%define OTHER 0
%endif
%if %{RHEL7}
%define OTHER 0
%endif

# required for desktop file install
%define my_vendor %(test %{OTHER} == 1 && echo "fedora" || echo "redhat")

%define TESTS 1
%define wwwdir /var/www/html/docs

Name:           publican
Version:        4.3.2
Release:        32%{?dist}
Summary:        Common files and scripts for publishing with DocBook XML
# For a breakdown of the licensing, refer to LICENSE
License:        (GPL-2.0-or-later OR Artistic-1.0-Perl) AND CC0-1.0
URL:            https://publican.fedorahosted.org
Source0:        https://fedorahosted.org/released/publican/Publican-v%{version}.tar.gz
Patch0:         file-spec-fix.patch
Patch1:		    xsl.patch

BuildArch:      noarch
Provides:       publican-common = %{version}
Provides:       publican-common-db5 = %{version}
Provides:       publican-API = 4.1

## work around arch -> noarch bug in yum
Obsoletes:      publican < 3

BuildRequires:  perl(Devel::Cover)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) => 1.14
BuildRequires:  perl(Test::Pod::Coverage) => 1.04
BuildRequires:  perl(Archive::Tar) => 1.84
BuildRequires:  perl(Archive::Zip)
# Not reall required, but sometimes koji pulls in a conflicting dep...
BuildRequires:  perl(Compress::Zlib) => 2.030
BuildRequires:  perl(Locale::Maketext::Gettext) >= 1.27
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::Simple)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::DateParse)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy::Recursive) => 0.38
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Inplace)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::FormatText)
BuildRequires:  perl(HTML::FormatText::WithLinks)
BuildRequires:  perl(HTML::FormatText::WithLinks::AndTables) >= 0.02
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTML::WikiConverter::Markdown) >= 0.06
BuildRequires:  perl(I18N::LangTags::List)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Locale::Language)
BuildRequires:  perl(Locale::PO) >= 0.24
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(String::Similarity)
BuildRequires:  perl(Syntax::Highlight::Engine::Kate) >= 0.09
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Constants)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Time::localtime)
BuildRequires:  perl(XML::LibXML) => 1.70
BuildRequires:  perl(XML::LibXSLT) => 1.70
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(XML::TreeBuilder) => 5.4
# BZ #1053609
BuildRequires:  perl-generators
BuildRequires:  perl-XML-TreeBuilder >= 5.4
BuildRequires:  docbook-style-xsl >= 1.77.1
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  docbook5-schemas
BuildRequires:  docbook5-style-xsl >= 1.78.1
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(Locale::Msgfmt)
BuildRequires:  perl(Locale::Maketext::Lexicon)
BuildRequires:  perl(Lingua::EN::Fathom)
BuildRequires:  rpm-build libicu-devel

# Most of these are handled automatically
Requires:       perl(Locale::Maketext::Gettext)  >= 1.27
Requires:       rpm-build
Requires:       docbook-style-xsl >= 1.77.1
Requires:       perl(XML::LibXML)  >=  1.70
Requires:       perl(XML::LibXSLT) >=  1.70
Requires:       perl(XML::TreeBuilder) >= 5.4
Requires:       perl(HTML::WikiConverter::Markdown) >= 0.06
# BZ #1053609
Requires:       perl-XML-TreeBuilder >= 5.4
Requires:       perl-Template-Toolkit
Requires:       perl(DBD::SQLite)
Requires:       perl(Text::CSV_XS)
Requires:       docbook5-schemas
Requires:       docbook5-style-xsl >= 1.78.1

# Not really required, but sometimes koji pulls in a conflicting dep...
Requires:       perl(Compress::Zlib) => 2.030

# Lets validate some basics
Requires:       rpmlint

# Pull in the fonts for all languages, else you can't build translated PDF in brew/koji
%if %{RHEL6}
Requires:       liberation-mono-fonts liberation-sans-fonts liberation-serif-fonts
Requires:       cjkuni-uming-fonts ipa-gothic-fonts ipa-pgothic-fonts
Requires:       lklug-fonts baekmuk-ttf-batang-fonts
Requires:       lohit-assamese-fonts lohit-bengali-fonts lohit-devanagari-fonts
Requires:       lohit-gujarati-fonts lohit-hindi-fonts lohit-kannada-fonts
Requires:       lohit-kashmiri-fonts lohit-konkani-fonts lohit-maithili-fonts
Requires:       lohit-malayalam-fonts lohit-marathi-fonts lohit-nepali-fonts
Requires:       lohit-oriya-fonts lohit-punjabi-fonts lohit-sindhi-fonts
Requires:       lohit-tamil-fonts lohit-telugu-fonts dejavu-lgc-sans-mono-fonts
Requires:       dejavu-fonts-common dejavu-serif-fonts dejavu-sans-fonts
Requires:       dejavu-sans-mono-fonts overpass-fonts
Requires:       wqy-zenhei-fonts
Requires:       wkhtmltopdf >= 0.12.1.devlopment
BuildRequires:  wkhtmltopdf >= 0.12.1.development
BuildRequires:  liberation-mono-fonts liberation-sans-fonts liberation-serif-fonts
BuildRequires:  cjkuni-uming-fonts ipa-gothic-fonts ipa-pgothic-fonts
BuildRequires:  lklug-fonts baekmuk-ttf-batang-fonts
BuildRequires:  dejavu-fonts-common dejavu-serif-fonts dejavu-sans-fonts
BuildRequires:  dejavu-sans-mono-fonts overpass-fonts dejavu-lgc-sans-mono-fonts
%endif
%if %{RHEL7}
Requires:       liberation-mono-fonts liberation-sans-fonts liberation-serif-fonts
Requires:       cjkuni-uming-fonts ipa-gothic-fonts ipa-pgothic-fonts
Requires:       lklug-fonts baekmuk-ttf-batang-fonts overpass-fonts
Requires:       wkhtmltopdf >= 0.12.1.devlopment
BuildRequires:  wkhtmltopdf >= 0.12.1.development
BuildRequires:  liberation-mono-fonts liberation-sans-fonts liberation-serif-fonts
BuildRequires:  cjkuni-uming-fonts ipa-gothic-fonts ipa-pgothic-fonts
BuildRequires:  lklug-fonts baekmuk-ttf-batang-fonts
%endif
%if %{OTHER}
Requires:       liberation-mono-fonts liberation-sans-fonts liberation-serif-fonts
Requires:       cjkuni-uming-fonts ipa-gothic-fonts ipa-pgothic-fonts
Requires:       baekmuk-ttf-batang-fonts overpass-fonts
Requires:       fop
BuildRequires:  fop
BuildRequires:  liberation-mono-fonts liberation-sans-fonts liberation-serif-fonts
BuildRequires:  cjkuni-uming-fonts ipa-gothic-fonts ipa-pgothic-fonts
BuildRequires:  baekmuk-ttf-batang-fonts
%endif

%description
Publican is a DocBook publication system, not just a DocBook processing tool.
As well as ensuring your DocBook XML is valid, publican works to ensure
your XML is up to publishable standard.

%package doc
Summary:        Documentation for the Publican package
Requires:       xdg-utils
Obsoletes:      publican-doc < 3

%description doc
Publican is a tool for publishing material authored in DocBook XML.
This guide explains how to  to create and build books and articles
using publican. It is not a DocBook XML tutorial and concentrates
solely on using the publican tools.

%package releasenotes
Summary:        Release notes for the Publican package
Requires:       xdg-utils

%description releasenotes
Release notes for Publican %{version}.

%package common-web
Summary:        Website style for common brand
Requires:       publican

%description common-web
Website style for common brand.

%package common-db5-web
Summary:        Website style for common brand for DocBook5 content
Requires:       publican

%description common-db5-web
Website style for common brand for DocBook5 content

%prep
%setup -q -n Publican-v%{version}
%autopatch -p1

%build
sed -i -e 's,PATH,%{DBPATH},g' catalog
XML_CATALOG_FILES=$dir/catalog %{__perl} Build.PL installdirs=vendor --nocolours=1

XML_CATALOG_FILES=$dir/catalog ./Build --nocolours=1
dir=`pwd`

cd Users_Guide && XML_CATALOG_FILES=$dir/catalog  %{__perl} -CDAS -I $dir/blib/lib $dir/blib/script/publican build \
    --formats=html-desktop --publish --langs=en-US \
    --common_config="$dir/blib/datadir" \
    --common_content="$dir/blib/datadir/Common_Content" --nocolours

cd $dir

cd Release_Notes && XML_CATALOG_FILES=$dir/catalog %{__perl} -CDAS -I $dir/blib/lib $dir/blib/script/publican build \
    --formats=html-desktop --publish --langs=en-US \
    --common_config="$dir/blib/datadir" \
    --common_content="$dir/blib/datadir/Common_Content" --nocolours

%install
rm -rf $RPM_BUILD_ROOT
dir=`pwd`

XML_CATALOG_FILES=$dir/catalog ./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

sed -i -e 's|@@FILE@@|%{_docdir}/%{name}-doc%{!?_docdir_fmt:-%{version}}/en-US/index.html|' %{name}.desktop
sed -i -e 's|@@ICON@@|%{_docdir}/%{name}-doc%{!?_docdir_fmt:-%{version}}/en-US/images/icon.svg|' %{name}.desktop
sed -i -e 's|@@FILE@@|%{_docdir}/%{name}-releasenotes%{!?_docdir_fmt:-%{version}}/en-US/index.html|' %{name}-releasenotes.desktop
sed -i -e 's|@@ICON@@|%{_docdir}/%{name}-releasenotes%{!?_docdir_fmt:-%{version}}/en-US/images/icon.svg|' %{name}-releasenotes.desktop

desktop-file-install --vendor="%{my_vendor}" --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop
desktop-file-install --vendor="%{my_vendor}" --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{name}-releasenotes.desktop

%find_lang %{name} --with-man

# Package web common files
mkdir -p -m755 $RPM_BUILD_ROOT/%{wwwdir}/common
dir=`pwd`
cd datadir/Common_Content/common
XML_CATALOG_FILES=$dir/catalog %{__perl} -CDAS -I $dir/blib/lib $dir/blib/script/publican install_brand --web --path=$RPM_BUILD_ROOT/%{wwwdir}/common
cd -
mkdir -p -m755 $RPM_BUILD_ROOT/%{wwwdir}/common-db5
cd datadir/Common_Content/common-db5
XML_CATALOG_FILES=$dir/catalog %{__perl} -CDAS -I $dir/blib/lib $dir/blib/script/publican install_brand --web --path=$RPM_BUILD_ROOT/%{wwwdir}/common-db5
cd -

%check
%if %{TESTS}
dir=`pwd`
XML_CATALOG_FILES=$dir/catalog ./Build --nocolours=1 test
%endif

%post
# hack to allow branch directory BZ #800252
CATALOG=%{_sysconfdir}/xml/catalog
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
"https://fedorahosted.org/released/publican/xsl/docbook4/" \
"file://%{_datadir}/publican/xsl/"  $CATALOG

CATALOG=%{_sysconfdir}/xml/catalog
%{_bindir}/xmlcatalog --noout --add "public" \
"-//OASIS//ENTITIES DocBook Character Entities V4.5//EN" \
"file://%{DBPATH}"  $CATALOG

%postun
if [ "$1" = 0 ]; then
  CATALOG=%{_sysconfdir}/xml/catalog
  %{_bindir}/xmlcatalog --noout --del \
  "https://fedorahosted.org/released/publican/xsl/docbook4/" $CATALOG

  CATALOG=%{_sysconfdir}/xml/catalog
  %{_bindir}/xmlcatalog --noout --del \
  "-//OASIS//ENTITIES DocBook Character Entities V4.5//EN" $CATALOG
fi

%files -f %{name}.lang
%doc Changes README COPYING Artistic pod1/publican
%{perl_vendorlib}/Publican.pm
%{perl_vendorlib}/Publican
%{_mandir}/man3/Publican*
%{_mandir}/man1/*
%{_bindir}/publican
%{_bindir}/db5-valid
%{_bindir}/db4-2-db5
%{_datadir}/publican
%config(noreplace) %{_datadir}/publican/default.db
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/publican-website.cfg
%config(noreplace) %{_sysconfdir}/bash_completion.d/_publican

%files doc
%doc Users_Guide/publish/desktop/*
%{_datadir}/applications/%{my_vendor}-%{name}.desktop
%doc fdl.txt

%files releasenotes
%doc Release_Notes/publish/desktop/*
%{_datadir}/applications/%{my_vendor}-%{name}-releasenotes.desktop
%doc fdl.txt

%files common-web
%{wwwdir}/common

%files common-db5-web
%{wwwdir}/common-db5

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 21 2024 Jeff Fearn <jfearn@redhat.com> - 4.3.2-31
- Patch broken html simple build
- Patch File::Spec warning

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Michal Josef Špaček <mspacek@redhat.com> - 4.3.2-26
- Remove lklug-fonts require, not present in Fedora

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.3.2-21
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Jeff Fearn <jfearn@redhat.com> 4.3.2-18
- Bug 1856259 Re-add FOP.

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.3.2-17
- Perl 5.32 rebuild

* Fri May 22 2020 Jeff Fearn <jfearn@redhat.com> 4.3.2-16
- Bug 1799903 remove FOP dependency.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.3.2-13
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.3.2-10
- Perl 5.28 rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.3.2-9
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.3.2-6
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 25 2016 Jeff Fearn <jfearn@redhat.com> - 4.3.2-4
- Reenable tests. BZ #1197699

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.3.2-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Peter Robinson <pbrobinson@fedoraproject.org> 4.3.2-1
- Fix versions in git
- Disable tests to fix FTBFS (1265063)

* Tue Jul 28 2015 Lee Newson <lnewson@redhat.com> 4.3.2-0
- Do not replace non-breaking spaces by spaces in msgid of POT files. BZ #1233202
- Fixed Unwanted line breaks around <inlinemediaobject> images. BZ #1222067
- Fixed EPUB output of db5 brands can't be viewed. BZ #1241348

* Thu Jun 18 2015 Lee Newson <lnewson@redhat.com> 4.3.1-0
- Fixed a regression in 4.3.0 that caused TOC's not to be included in wkhtmltopdf PDF's. BZ #1230023
- Fixed callout image urls being broken. BZ #1222716

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 5 2015 Jeff Fearn <jfearn@redhat.com> 4.3.0-0
- Fix web site templates to be more flexable.
- Tweak default website styles.
- Remove all FOP customisations. BZ #1168765
- Use FontAwesome for aswesomeness.
- Switch DocBook-5 HTML to highlight.js.
- Change splash page group publish directory structure so it can be used directly. BZ #1186990
- Fix duplicate link in Website docs. BZ #1188384
- Fix PDF builds ignoring overrides.css and lang.css. BZ #1165005
- Pulled in new/updated translations. BZ #1169605
- Removed duplicate IDs from PUG. BZ #1197523
- Removed the titlepage.xsl import from html-single due to breaking the xsl precedence. BZ #1187728
- Fix Publican doesn't fallback to base_brand xsl files. BZ #1185127
- Fix <section> elements being stripped in drupal-book builds. BZ #1158747
- Fix malformed HTML/Drupal XML Feed for DocBook 5 content. BZ #1158740
- Fix incorrect missing image warnings for drupal builds. BZ #1158725
- Fix articles not building when using the drupal-book format. BZ #1164640
- Fix initial title page content being skipped when a user defines a custom bookinfo id. BZ #1165482
- Fix invalid XML being generated for drupal-book, when titles contain reserved chars. BZ #1165438
- Changed the drupal feed <parent> field to use the url value instead of the title. BZ #1165724
- Fix publican.cfg values are used in the feed page <title> tag. BZ #1172402
- Fix drupal content is dropped, if the element that is chunked has no id. BZ #1173421
- Adjusted the XML output so anchors to something in the same page doesn't include the page url.
- Make legalnotice chunk in a similar way as chapters for drupal builds, so it's included in the feed.
- Enable section.label.includes.component.label for common-db5. BZ #1205952
- Fix formalpara ids being dropped for DocBook 4.5. BZ #1209344
- Add --no_clean option to allow custom entity files. BZ #1208069

* Tue Feb 24 2015 Petr Pisar <ppisar@redhat.com> - 4.2.6-1
- Fix versions in Perl module dependencies again

* Tue Oct 21 2014 Jeff Fearn <jfearn@redhat.com> 4.2.6-0
- Fix External_Links translation not merging. BZ #1153911

* Wed Oct 15 2014 Jeff Fearn <jfearn@redhat.com> 4.2.5-0
- Fix DocBook4 epub failing for ja-JP. BZ #1152780

* Tue Oct 14 2014 Jeff Fearn <jfearn@redhat.com> 4.2.4-0
- Allow External_Links.xml to be translated. BZ #1150386
- Change ja-JP person-name style. BZ #1150866

* Tue Oct 7 2014 Jeff Fearn <jfearn@redhat.com> 4.2.3-0
- Fix DocBook4 entity text, BZ #1143060
- Remove extra white space from non-verbatim msgid's. BZ #1143792
- Fix PDF build using FOP fails with "No numberLines function available." BZ #1143852
- Add allow_network option. Defaults OFF. BZ #1144949
- Add hacks to work around BZ #1144220

* Wed Sep 17 2014 Jeff Fearn <jfearn@redhat.com> 4.2.2-2
- Fix duplicate messages in POT files. BZ #1136133
- Remove top level directory from drupal tar file. BZ #1139070
- Fix PDF font selection. BZ #1139899

* Mon Sep 01 2014 Jeff Fearn <jfearn@redhat.com> 4.2.1-0
- Remove empty msgids from POT files. BZ #1135143
- Fix highlight in callout with areaspec. BZ #1135827

* Thu Aug 28 2014 Jeff Fearn <jfearn@redhat.com> 4.2.0-0
- Add iframe video support to DocBook5 HTML5. BZ #752021
- Stop calculating column width if no width is set. BZ #1084860
- Simply styling of code, and admonitions in HTML5. BZ #1093498
- Added tip formatting. BZ #1033830
- Remove incorrect prompt. BZ #1096544
- Add "popper" to hide program listing after 4 lines. BZ #1088051
- Fix white space being removed from msgids when merging. BZ #1097090
- Add code language switching. BZ #1092351
- Fix CDATA support, bump XML::TreeBuilder dep to 5.3. BZ #1101050
- Add --showfuzzy to build options.
- Move PO manipulation to Locale::PO.
- Fix inline"\n" not working in verbatim. BZ #1097091 (TODO bump Locale::PO version when released)
- Fix images for DB4 website callouts. BZ #1112899
- Remove newline after cdata. BZ #1110611
- Add Markdown output. BZ #1120455
- Bump Syntax::Highlight::Engine::Kate dep to 0.09.
- Add external link support. BZ #1123193
- Add 'th' to translation block list. BZ #1127462

* Mon Aug 04 2014 Jeff Fearn <jfearn@redhat.com> 4.1.7-0
- Another shot at fixing PDF index out of range error.

* Tue Jul 29 2014 Jeff Fearn <jfearn@redhat.com> 4.1.6-0
- Another shot at fixing PDF index out of range error.

* Wed Jul 09 2014 Jeff Fearn <jfearn@redhat.com> 4.1.5-0
- Add some web UI tranlstaion strings & sort formats. BZ #1117081
- Fix formal para title CSS. BZ #1110076

* Thu Jul 03 2014 Jeff Fearn <jfearn@redhat.com> 4.1.4-1
- Expose sort functions to version index page.

* Wed May 21 2014 Jeff Fearn <jfearn@redhat.com> 4.1.4-0
- Fix headers and footers triggering index out of range in PDF Build.

* Wed May 21 2014 Jeff Fearn <jfearn@redhat.com> 4.1.3-0
- Fix extra space breaking spec files with sort_order. BZ #1099262
- Make div.title bold in db4.css. BZ #1049661

* Wed May 14 2014 Jeff Fearn <jfearn@redhat.com> 4.1.2-0.1
- Fix Fedora and RHEL7  requires

* Wed May 14 2014 Jeff Fearn <jfearn@redhat.com> 4.1.2-0
- Fix broken DocBook5 validation stopping package builds. BZ #1097495

* Thu May 8 2014 Jeff Fearn <jfearn@redhat.com> 4.1.1-0
- Fix long tables and pre's breaking PDF build. BZ #1095574

* Mon May 5 2014 Jeff Fearn <jfearn@redhat.com> 4.1.0-0
- Add abstract to release notes so PDF builds
- Fix RPM upgrade not pulling in required XML::TreeBuilder version. BZ #1053609
- Allow PDF to build without any authors. BZ #1050975
- Increase XML::LibXSLT::max_depth to 10K. BZ #1035525
- Include entrytbl in cols count. BZ #1069405
- Add 'td' to translatable blocks list. BZ #1059938
- Treat entry like para for mixedmode tags. BZ #1039382
- Add blank page after cover page in PDF. BZ #1050770
- Fix replaceable override in DB 4.5 XSL. BZ #1054462
- Store processing instructions. BZ #1045463
- Add releaseinfo support. BZ #1050789
- Add suppor5t for wkhtmltopdf 0.12.0
- Add non-minified JS files. BZ #1062109
- Use term as ID node for varlistentry. BZ #1050836
- Fix acroread search and image issues. BZ #1038393 #1065810
- Add line numbering to DB5 html output. BZ #1074709
- Remove glossdiv and indexdiv headings from PDF TOC. BZ #1058545
- Add basic handling & style for revisionflag.
- Fix admonition style for wkhtmnltopdf 0.12.
- Pass chunk_section_depth to wkhtmltopdf. BZ #1044848
- Do not die on empty brand conf files. BZ #1037037
- Fix font embedding
- Enforce RPM API requirements. BZ #1029293
- Fix desktop SPEC file creation. BZ #1081087
- Pass previous option to msgmerge. BZ #1081363
- Load splash pages in templates instead of using javascript. BZ #1081300
- Sync list layout across web and desktop styles. BZ #1080236
- Add dt_format parameter. BZ #1081808
- Provide gettext version of package name. BZ #1083102
- Fix step style. BZ #1080156
- Fix DD layout. BZ #1084242
- Fix tables breaking out. BZ #1082444
- Add zt_push and zt_pull for Zanata.

* Wed Dec 18 2013 Rüdiger Landmann <rlandmann@redhat.com> 4.0.0-0
- Support DocBook 5 as input format. BZ #1005042
- Fix duplicate first author in PDF. BZ #996351
- Include DocBook 5-compatible templates. BZ #697366
- Fix UTF8 issue in ~/.publican.cfg. BZ #987325
- Replace abstract and subtitle xsl. BZ #953675
- Change Cover page font. BZ #1006134
- Fix TOC leader in PDF. BZ #1006056
- Fix PDF Legal Notice trademarks & formatting. BZ #970851
- Fix keyword lable showing in PDF when there are no keywords. BZ #1007146
- Indicate whether a translation is older in the web GUI. BZ #889031
- Include time in update_date. BZ #979846 
- Support web site navigation for books without HTML. BZ #885916
- Support ascending Revision History. BZ #999578
- Add ability to compy installed brand web content to another site. BZ #967664
- Fix PDF example.properties template. BZ #999586
- Fix PUG PDF format for OpenSuse. BZ #999581
- Simplify highlight error message. BZ #987059
- Add css styles for table sizes. BZ #1005640
- Tidy up Build.PL for better CPAN support. BZ #999259
- Fix image path for icon.svg. BZ #1011222
- Fix print_unused not handling include from higher directories. BZ #1004955
- Fix SVG fallback to PNG. BZ #990823
- Fix subtitle font size. BZ #987431
- Support grouping of books within a version. BZ #901560
- Remove bold from titles in Indic scripts. BZ #1006135
- Overhaul EPUB, basic CSS, harcode chunking, fix errors. BZ #883159
- Fix duplicate file listing in EPUB. BZ #875119
- Fix objects in EPUB not in catalog. BZ #875125
- Fix duplicate ID's in EPUBs. BZ #875116
- Fix ConfigData not being reset after testing on all platforms. BZ #999427
- Fix links to step not functioning. BZ #1009015
- Support GIT for distributed sets. BZ #864226
- Fix Build.PL not handling .mo files. BZ #1016421
- Bold and Center titlepage edition. BZ #1017548
- Fix broken use of pushd in Build.PL. BZ #1018608
- Remove XML from spec file abstract. BZ #1018796
- Fix UTF8 in publican.cfg not being handled. BZ #1020059
- Fix Indic PDF build on F19. BZ #1018024
- Fix UTF8 encoding for title in Revision_History.xml BZ #1020570
- Fix browser not detecting UTF8 on HTML5 files with .html extension. BZ #1018659
- Fix styling of DB4 example, package, & option. Remove html.longdesc.embed xsl. BZ #1023248
- Fix UTF8 in Groups.xml. BZ #1022575
- Add translations for "Edition" BZ# 1007141
- Add translations for "English is newer"  BZ #889031
- Fix broken or-IN translation.
- Update DB4 CSS steps, stepalts, OLs, term. BZ #1026173
- Remove chunk override from html.xsl. BZ #1026563
- Fix path to POD. BZ #1026563
- Update CLI translations
- Various fixes to Common Content + update Common Content translation. BZ #1027248
- Update and correct Debian installation instructions. BZ #1013934
- Correct OpenSUSE installation instructions. BZ #1000534
- Add Docker installation instructions. BZ #1015943
- Clarify where relative paths are used in brand instructions  - BZ #1028815
- Update and clarify translation instructions BZ #1021287 
- Expose glossterm in PO files to support sortas attribute. BZ #1030591
- Add report action to print readability statistics. BZ #1031364
- Change comment in syntax highlight to light grey. BZ #1030718
- Document use of "sortas" for indexes and glossaries in PUG
- Fix newline in translation affecting output. BZ #1036150

* Fri Oct 4  2013 Jeff Fearn <jfearn@redhat.com> 3.9.9-0
- Publican 4.0 RC1

* Wed Sep 04 2013 Jeff Fearn <jfearn@redhat.com> 3.2.1-0
- Fix empty images dir causing packaging fail. BZ #996349
- Fix draft background being in front. BZ #996361
- Fix Titles that are ulinks are incorrectly positioned. BZ #995095
- Fix Syntax Highlighting not working when Language and Module names differ. BZ #995932
- Fix missing '/' on callout image url. BZ #998736
- Add string for brand customistaion BZ #1002388

* Thu Aug 8 2013 Jeff Fearn <jfearn@redhat.com> 3.2.0-0
- Add spaces to web-spec.xsl to work around newer libxml2 eating white space in spec files  BZ #982424
- Fix typos in common content BZ #952490 #974918
- Stop menu bouncing. BZ #953716
- Fix ID missing from admonitions. BZ #966494
- Support corpauthor for PDF. BZ #908666
- Fix nested block tags breaking translation flow. BZ #909728
- Fix multiple calls to update_po breaking packaging. BZ #891167
- Add website labels and translations. BZ #979885
- Add orgname to block/inline code. BZ #872955
- Fix get_keywords not using correct info file. BZ #957956
- Improve web print CSS. BZ #927513
- Fix pre border in PDF. BZ #905752
- Fix epub DOCTYPE. BZ #875129
- Fix step first child style. BZ #971221
- Fix long link word wrap in PDF. BZ #923481
- Support case-insensitive "language" attribute. BZ #919474
- Apply title style patch from Jaromir Hradilek. BZ #924518
- Expose %%book_ver_list to products/versions_index.tmpl. BZ #962643
- Allow brands to ship web templates. Add site config toc_js. BZ #956935
- Add pdftool option to build for pdf tool control. BZ #953728
- Add default mapping for language to locale. BZ #844202
- Fix ID missing from translated Revision History. BZ #911462
- Add pub_dir option to override publish directory. BZ #830062
- Removed show_unknown parameter and associated code. BZ #915428
- Add img_dir parameter to override images directory. BZ #919481
- Support all DocBook conditionals. BZ #919486
- Flag spaces in product number as invalid. BZ #973895
- Standardized prompts in commands. BZ #880456
- Updated web_formats publican.cfg info BZ #839141
- Replaced 'home page' with 'product or version page' BZ #921803
- Replaced a broken link to CPAN with a working link BZ# 973461
- Remove duplicate brand files from base install. BZ #966143
- Add extras_dir parameter to override extras directory. BZ #953998
- Fix PDF ignoring cover logo. BZ #974353
- Add trans_drop action to freeze source language for translation. BZ #887707
- Fix empty pot files not being deleted. BZ #961413
- Fix long title layout on cover page in PDF. BZ #956934
- Add Mac OS X Lion installation instructions. BZ# 979229
- Add file handle limit workaround to FAQ BZ #952476
- Support CDATA tags. BZ #958343
- Fix UTF8 image names getting mangled in publish. BZ #953618
- Add wkhtmltopdf_opts parameter to pass options to wkhtmltopdf. BZ #951290
- Fix edition missing on PDF cover pages. BZ #956940
- Support XML in add_revision member. BZ #862465
- Fix duplicate footnotes in bibliography. BZ #653447
- Fix Link from footlink to footlink-ref not working in PDF. BZ #909786
- Fix TOC draft watermark in PDF. BZ #905271
- Add common-db5 sub package. BZ #958495
- Support decimals in colwidth & convert exact measures to pixels. BZ #913775
- Tweak equation formatting. BZ #804531
- Fix POT-Creation-Date format. BZ #985836
- Fix site stats report swapping languages and products.
- Fix web_dir not used for home page packages. BZ #988191
- Updated web site instructions - BZ#979224

* Mon Mar 18 2013 Jeff Fearn <jfearn@redhat.com> 3.1.5-0
- Fix translated PDF encode issue when build from packaged books. BZ #922618

* Tue Mar 12 2013 Jeff Fearn <jfearn@redhat.com> 3.1.4-0
- Fix entities in Book_Info braking build. BZ #917898
- add translations of "Revision History". BZ #918365
- Fix TOC title not translated in PDF. BZ #918365
- Fix translated strings with parameters. BZ #891166
- update translations
- add it-IT translation of PUG via <fedora@marionline.it> BZ #797515

* Fri Feb 22 2013 Jeff Fearn <jfearn@redhat.com> 3.1.3-1
- Fix add_revision breaking XML parser. BZ #912985
- Stronger fix for cover pages causing page number overrun. BZ #912967
- Fix CSS for article front page subtile. BZ #913016

* Mon Feb 18 2013 Jeff Fearn <jfearn@redhat.com> 3.1.2-0
- Fix tests failing when publican not installed. BZ #908956
- Fix broken mr-IN/Conventions.po. BZ #908956
- Fix footnote link unclickable. BZ #909006
- Fix missing translations for common files. BZ #908976
- Fix using edition for version on cover pages. BZ #912180
- Fix nested entities causing XML::TreeBuilder to fail. BZ #912187

* Thu Feb 7 2013 Jeff Fearn <jfearn@redhat.com> 3.1.1-0
-  Fix web site CSS for admonitions. BZ #908539

* Mon Feb 4 2013 Jeff Fearn <jfearn@redhat.com> 3.1.0-2
- Fix translated text

* Mon Feb 4 2013 Jeff Fearn <jfearn@redhat.com> 3.1.0-1
- Warn of failure to chmod/chown.

* Fri Jan 25 2013 Jeff Fearn <jfearn@redhat.com> 3.1.0-0
- new upstream package.

* Wed Oct 31 2012 Jeff Fearn <jfearn@redhat.com> 3.0.0-0
- new upstream package.

