
# koffice version to Obsolete
%global koffice_ver 3:2.3.70

%global pstoedit 1
%global marble 1
%global visio 1
%global wpd 1
%if 0%{?fedora} > 25
%global okular 1
%endif

#global external_lilypond_fonts 1

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Name:    calligra 
Version: 3.2.1
Release: 21%{?dist}
Summary: An integrated office suite

License: GPLv2+ and LGPLv2+
URL:     http://www.calligra-suite.org/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/calligra/%{version}/calligra-%{version}.tar.xz

## upstream patches
Patch2: 0002-Make-show-hidden-row-s-work.patch
Patch3: 0003-Fix-Bug-423038-Annotation-shape-crashes-on-paste.patch
Patch8: 0008-Fix-comparison-between-QString-and-0.patch
Patch9: 0009-Sheets-Fix-Bug-423474-Selections-not-retained-when-s.patch
Patch10: 0010-ChartTool-KoFormulaTool-Guard-against-crash-if-activ.patch
Patch18: 0018-Fix-assert-with-invalid-.local-share-autocorrect-cus.patch
Patch19: 0019-Repair-KFileWidget-integration.patch
Patch20: 0020-Fix-inserting-a-large-JPEG-image-into-a-presentation.patch
Patch32: 0032-Remove-duplicated-actions-provided-by-parent-view.patch
Patch37: 0037-kundo2_aware_xgettext.sh-fix-a-gawk-warning.patch
Patch53: 0053-Partial-update-of-Commit-62f51070-to-make-it-compile.patch
# Needed for compiling with C++17
Patch54: 0001-Fix-some-more-warnings.patch
Patch55: calligra-poppler-22.08.0-1.patch
Patch56: calligra-poppler-22.08.0-2.patch

## upstreamable patches

## downstream patches
# FIXME/TODO: (re)enable gemini for propper packaging
Patch200: calligra-disable_products.patch

# Fix missing #includes for gcc-11
Patch201: calligra-gcc11.patch

# Switch to C++17 because poppler needs it
Patch202: calligra-c++17.patch

BuildRequires: boost-devel
BuildRequires: bzip2-devel bzip2
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: libappstream-glib
BuildRequires: pkgconfig(eigen3)
BuildRequires: pkgconfig(exiv2) 
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: freeglut-devel
BuildRequires: gettext-devel
BuildRequires: giflib-devel
BuildRequires: pkgconfig(glew)
BuildRequires: pkgconfig(GraphicsMagick)
BuildRequires: pkgconfig(gsl) 

BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(gl) pkgconfig(glu) 
%if 0%{?marble}
BuildRequires: marble-widget-qt5-devel
%endif
%if 0%{?wpd}
%if 0%{?visio}
BuildRequires: pkgconfig(libvisio-0.1)
%endif
BuildRequires: pkgconfig(libetonyek-0.1)
BuildRequires: pkgconfig(libodfgen-0.1)
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(libwpd-0.10)
BuildRequires: pkgconfig(libwpg-0.3)
BuildRequires: pkgconfig(libwps-0.4)
%endif
BuildRequires: cmake(OpenColorIO)
BuildRequires: pkgconfig(libpng)
BuildRequires: libicu-devel
BuildRequires: libspnav-devel
BuildRequires: libtiff-devel
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(glib-2.0)
# As of OpenEXR 3 upstream has significantly reorganized the libraries
# including splitting out imath as a standalone library (which this project may
# or may not need). Please see
# https://github.com/AcademySoftwareFoundation/Imath/blob/master/docs/PortingGuide2-3.md
# for porting details and encourage upstream to support it. For now a 2.x
# compat package is provided.
%if 0%{?fedora} > 33
BuildRequires: cmake(OpenEXR) < 3
%else
BuildRequires: pkgconfig(OpenEXR) < 3
%endif
BuildRequires: perl-interpreter
BuildRequires: pkgconfig(poppler-qt5)
BuildRequires: cmake(Qca-qt5)
BuildRequires: readline-devel
BuildRequires: pkgconfig(sqlite3)

# kf5
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5KHtml)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5JobWidgets)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Kross)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5NotifyConfig)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5ThreadWeaver)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)

# qt5
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5OpenGL)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5WebKit)
BuildRequires: cmake(Qt5WebKitWidgets)
BuildRequires: cmake(Qt5X11Extras)
## optional qtquick1 components, retired in fedora, so let's omit this
#BuildRequires: cmake(Qt5Declarative)

BuildRequires: cmake(Phonon4Qt5)

BuildRequires: cmake(KF5Contacts)
# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%ifarch %{qt5_qtwebengine_arches}
BuildRequires: cmake(KF5Akonadi)
%endif

BuildRequires: cmake(Qca-qt5)

BuildRequires: git-core
BuildRequires: libgit2-devel

BuildRequires: cmake(KChart) >= 2.7
BuildRequires: cmake(KGantt) >= 2.7

## not used anymore, but may be re-added when their API stabilizes
#BuildRequires: cmake(KReport)
#BuildRequires: cmake(KPropertyWidgets)


# * Git
# * Qca-qt5 (required version >= 2.1.0), Qt Cryptographic Architecture, <http:/download.kde.org/stable/qca-qt5>
#   Required for encrypted OpenDocument files and encrypted xls files support (available as a module in kdesupport)
# * Vc (required version >= 1.1.0), Portable, zero-overhead SIMD library for C++, <https://github.com/VcDevel/Vc>
#   Required by the pigment for vectorization
# * Libgit2
# * Libqgit2
# * Cauchy, Cauchy's M2MML, a Matlab/Octave to MathML compiler, <https://bitbucket.org/cyrille/cauchy>
#   Required for the matlab/octave formula tool
# * OOoSDK

Obsoletes: koffice < %{koffice_ver} 
Obsoletes: koffice-suite < %{koffice_ver}

Requires:  %{name}-words = %{version}-%{release} 
Requires:  %{name}-sheets = %{version}-%{release} 
Requires:  %{name}-stage = %{version}-%{release}
Requires:  %{name}-karbon = %{version}-%{release}
%if 0%{?okular}
Requires:  %{name}-okular-odpgenerator = %{version}-%{release}
Requires:  %{name}-okular-odtgenerator = %{version}-%{release}
%endif

%description
%{summary}.

%package core
Summary:  Core support files for %{name} 
Obsoletes: koffice-core < %{koffice_ver}
Obsoletes: koffice-filters < %{koffice_ver}
Obsoletes: calligra-filters < 2.3.86-3
Provides:  calligra-filters = %{version}-%{release} 
Obsoletes: %{name}-kformula < 2.4.0
Obsoletes: %{name}-kformula-libs < 2.4.0
Obsoletes: %{name}-author < 3.0
Obsoletes: %{name}-flow < 3.0.1-6
Obsoletes: %{name}-flow-libs < 3.0.1-6
Obsoletes: %{name}-map-shape < 3.0
Obsoletes: %{name}-qtquick < 3.0
Obsoletes: %{name}-semanticitems < 3.0
%if ! 0%{?okular}
Obsoletes: %{name}-okular-odpgenerator < %{version}-%{release}
Obsoletes: %{name}-okular-odtgenerator < %{version}-%{release}
%endif
Obsoletes: %{name}-reports-map-element < 3.0
Obsoletes: %{name}-kexi-map-form-widget < 3.0
Obsoletes: %{name}-braindump < 3.0.0
Obsoletes: %{name}-braindump-libs < 3.0.0
%if 0%{?external_lilypond_fonts}
Requires: lilypond-emmentaler-fonts
%endif
Requires: color-filesystem
# formulashape fonts
Requires: lyx-fonts
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description core
%{summary}.

%package libs
Summary: Runtime libraries for %{name} 
Obsoletes: koffice-libs < %{koffice_ver}
Obsoletes: calligra-devel < 3.0
Obsoletes: calligra-kdchart < 3.0
Obsoletes: calligra-kdchart-devel < 3.0
Obsoletes: koffice-devel < 3:2.3.70
%description libs
%{summary}.

%package l10n
Summary: Language files for calligra
Obsoletes: calligra-l10n-bs < 3.0
Obsoletes: calligra-l10n-ca < 3.0
Obsoletes: calligra-l10n-cs < 3.0
Obsoletes: calligra-l10n-da < 3.0
Obsoletes: calligra-l10n-de < 3.0
Obsoletes: calligra-l10n-el < 3.0
Obsoletes: calligra-l10n-en_GB < 3.0
Obsoletes: calligra-l10n-es < 3.0
Obsoletes: calligra-l10n-et < 3.0
Obsoletes: calligra-l10n-fi < 3.0
Obsoletes: calligra-l10n-fr < 3.0
Obsoletes: calligra-l10n-gl < 3.0
Obsoletes: calligra-l10n-hu < 3.0
Obsoletes: calligra-l10n-it < 3.0
Obsoletes: calligra-l10n-ja < 3.0
Obsoletes: calligra-l10n-kk < 3.0
Obsoletes: calligra-l10n-nb < 3.0
Obsoletes: calligra-l10n-nl < 3.0
Obsoletes: calligra-l10n-pl < 3.0
Obsoletes: calligra-l10n-pt < 3.0
Obsoletes: calligra-l10n-pt_BR < 3.0
Obsoletes: calligra-l10n-ru < 3.0
Obsoletes: calligra-l10n-sk < 3.0
Obsoletes: calligra-l10n-sv < 3.0
Obsoletes: calligra-l10n-tr < 3.0
Obsoletes: calligra-l10n-uk < 3.0
Obsoletes: calligra-l10n-zh_CN < 3.0
Obsoletes: calligra-l10n-zh_TW < 3.0
Provides: calligra-l10n-bs = %{version}-%{release}
Provides: calligra-l10n-ca = %{version}-%{release}
Provides: calligra-l10n-cs = %{version}-%{release}
Provides: calligra-l10n-da = %{version}-%{release}
Provides: calligra-l10n-de = %{version}-%{release}
Provides: calligra-l10n-el = %{version}-%{release}
Provides: calligra-l10n-en_GB = %{version}-%{release}
Provides: calligra-l10n-es = %{version}-%{release}
Provides: calligra-l10n-et = %{version}-%{release}
Provides: calligra-l10n-fi = %{version}-%{release}
Provides: calligra-l10n-fr = %{version}-%{release}
Provides: calligra-l10n-gl = %{version}-%{release}
Provides: calligra-l10n-hu = %{version}-%{release}
Provides: calligra-l10n-it = %{version}-%{release}
Provides: calligra-l10n-ja = %{version}-%{release}
Provides: calligra-l10n-kk = %{version}-%{release}
Provides: calligra-l10n-nb = %{version}-%{release}
Provides: calligra-l10n-nl = %{version}-%{release}
Provides: calligra-l10n-pl = %{version}-%{release}
Provides: calligra-l10n-pt = %{version}-%{release}
Provides: calligra-l10n-pt_BR = %{version}-%{release}
Provides: calligra-l10n-ru = %{version}-%{release}
Provides: calligra-l10n-sk = %{version}-%{release}
Provides: calligra-l10n-sv = %{version}-%{release}
Provides: calligra-l10n-tr = %{version}-%{release}
Provides: calligra-l10n-uk = %{version}-%{release}
Provides: calligra-l10n-zh_CN = %{version}-%{release}
Provides: calligra-l10n-zh_TW = %{version}-%{release}
# not *strictly* required, but helps ensure -l10n,-core, and other pkg versions match
Requires: %{name}-core = %{version}-%{release}
BuildArch: noarch
%description l10n
%{summary}.

%package  words
Summary:  An intuitive word processor application with desktop publishing features
Obsoletes: koffice-kword < %{koffice_ver}
Obsoletes: koffice-kword-libs < %{koffice_ver}
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-words-libs%{?_isa} = %{version}-%{release}
%{?kf5_kinit_requires}
%description words
KWord is an intuitive word processor and desktop publisher application.
With it, you can create informative and attractive documents with
pleasure and ease.

%package  words-libs
Summary:  Runtime libraries for %{name}-words
Requires: %{name}-words = %{version}-%{release}
%description words-libs
%{summary}.

%package  sheets 
Summary:  A fully-featured spreadsheet application
Obsoletes: koffice-kspread < %{koffice_ver}
Obsoletes: koffice-kspread-libs < %{koffice_ver}
Obsoletes: calligra-tables < 2.3.92
Provides:  calligra-tables = %{version}-%{release}
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-sheets-libs%{?_isa} = %{version}-%{release}
%{?kf5_kinit_requires}
%description sheets 
Tables is a fully-featured calculation and spreadsheet tool.  Use it to
quickly create and calculate various business-related spreadsheets, such
as income and expenditure, employee working hours…

%package  sheets-libs
Summary:  Runtime libraries for %{name}-sheets
Obsoletes: calligra-tables-libs < 2.3.92
Requires: %{name}-sheets = %{version}-%{release}
%description sheets-libs
%{summary}.

%package  stage 
Summary:  A full-featured presentation program
Obsoletes: koffice-kpresenter < %{koffice_ver}
Obsoletes: koffice-kpresenter-libs < %{koffice_ver}
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-stage-libs%{?_isa} = %{version}-%{release}
# when -libs was introduced
%description stage 
Stage is a powerful and easy to use presentation application. You
can dazzle your audience with stunning slides containing images, videos,
animation and more.

%package  stage-libs
Summary:  Runtime libraries for %{name}-stage
Requires: %{name}-stage = %{version}-%{release}
%description stage-libs
%{summary}.

%package  karbon
Summary:  A vector drawing application
Obsoletes: koffice-karbon < %{koffice_ver}
Obsoletes: koffice-karbon-libs < %{koffice_ver}
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-karbon-libs%{?_isa} = %{version}-%{release}
%if 0%{?pstoedit}
# for karbon eps import filter
BuildRequires: pstoedit
Requires: pstoedit
%endif
%{?kf5_kinit_requires}
%description karbon
Karbon is a vector drawing application with an user interface that is
easy to use, highly customizable and extensible. That makes Karbon a
great application for users starting to explore the world of vector
graphics as well as for artists wanting to create breathtaking vector
art.

Whether you want to create clipart, logos, illustrations or photorealistic
vector images – look no further, Karbon is the tool for you!

%package  karbon-libs
Summary:  Runtime libraries for %{name}-karbon
Requires: %{name}-karbon = %{version}-%{release}
%description karbon-libs
%{summary}.

%package  plan 
Summary:  A project planner
Obsoletes: koffice-kplato < %{koffice_ver}
Obsoletes: koffice-kplato-libs < %{koffice_ver}
Requires: %{name}-core = %{version}-%{release}
Requires: %{name}-plan-libs%{?_isa} = %{version}-%{release}
%if 0%{?mpxj}
BuildRequires: java-devel
Requires: apache-poi
#Requires: apache-mpxj
%endif
%description plan 
Plan is a project management application. It is intended for managing
moderately large projects with multiple resources.

%package  plan-libs
Summary:  Runtime libraries for %{name}-plan
Requires: %{name}-plan = %{version}-%{release}
%description plan-libs
%{summary}.

%if 0%{?okular}
%package  okular-odpgenerator
Summary:  OpenDocument presenter support for okular
Obsoletes: koffice-okular-odpgenerator < %{koffice_ver}
BuildRequires: okular5-devel
# README.PACKAGER claims this, but I don't think it's true anymore
Requires: %{name}-stage = %{version}-%{release}
Requires: okular5-part
%description okular-odpgenerator
%{summary}.

%package  okular-odtgenerator
Summary:  OpenDocument text support for okular
BuildRequires: okular5-devel
Requires: %{name}-words = %{version}-%{release}
Requires: okular5-part
%description okular-odtgenerator
%{summary}.
%endif


%prep
%autosetup -p1


%build
%cmake_kf5 \
  -Wno-dev

%cmake_build


%install
%cmake_install

## unpackaged files
rm -fv %{buildroot}%{_datadir}/mime/packages/{krita_ora,x-iwork-keynote-sffkey}.xml
%if 0%{?external_lilypond_fonts}
rm -fv %{buildroot}%{_kf5_datadir}/calligra_shape_music/fonts/Emmentaler-14.ttf
%endif
rm -frv %{buildroot}%{_kf5_datadir}/locale/x-test/

%find_lang %{name} --all-name --with-html


%check
for appdata_file in %{buildroot}%{_kf5_metainfodir}/*.appdata.xml ; do
appstream-util validate-relax --nonet ${appdata_file} ||:
done
for desktop_file in %{buildroot}%{_datadir}/applications/*.desktop ; do
desktop-file-validate ${desktop_file}  ||:
done


%files 
## devtools fun
#{_kf5_bindir}/cstester
#{_kf5_bindir}/cstrunner
#{_kf5_bindir}/visualimagecompare

%files core
%doc AUTHORS README
%license COPYING*
%{_kf5_bindir}/calligra
%{_kf5_bindir}/calligraconverter
%{_datadir}/color/icc/calligra/
%{_kf5_datadir}/calligra/
#{_datadir}/mime/packages/msooxml-all.xml
%{_datadir}/mime/packages/calligra_svm.xml
%if 0%{?krita}
%{_datadir}/mime/packages/krita*.xml
%endif
%{_datadir}/mime/packages/wiki-format.xml
%{_kf5_datadir}/icons/hicolor/*/*/*
%if ! 0%{?external_lilypond_fonts}
%{_kf5_datadir}/calligra_shape_music/fonts/Emmentaler-14.ttf
%endif
%{_kf5_sysconfdir}/xdg/calligra_stencils.knsrc
%{_kf5_datadir}/kservices5/calligra_odg_thumbnail.desktop
%{_kf5_datadir}/kservices5/calligradocinfopropspage.desktop
%{_kf5_datadir}/kservices5/flow_vsdx_thumbnail.desktop
%{_kf5_datadir}/kservices5/flow_wpg_thumbnail.desktop
# PART_COMPONENTS, used by gemini
# links all of  calligrasheetscommon,calligrastageprivate,wordsprivate
#{_kf5_libdir}/qt5/qml/org/kde/calligra/

%ldconfig_scriptlets libs

%files libs
%{_kf5_libdir}/libbasicflakes.so*
%{_kf5_libdir}/libflake.so*
%{_kf5_libdir}/libkoformula.so*
%{_kf5_libdir}/libkomain.so*
%{_kf5_libdir}/libkoodf.so*
%{_kf5_libdir}/libkoodf2.so*
%{_kf5_libdir}/libkoodfreader.so*
%{_kf5_libdir}/libkopageapp.so*
%{_kf5_libdir}/libkoplugin.so*
%{_kf5_libdir}/libkostore.so*
%{_kf5_libdir}/libkotext.so*
%{_kf5_libdir}/libkowidgets.so*
%{_kf5_libdir}/libkowidgetutils.so*
%{_kf5_libdir}/libkowv2.so*
%{_kf5_libdir}/libkundo2.so*
%{_kf5_libdir}/libkomsooxml.so*
%{_kf5_libdir}/libpigmentcms.so*
%{_kf5_libdir}/libRtfReader.so*
%{_kf5_libdir}/libkotextlayout.so*
%{_kf5_libdir}/libkovectorimage.so*
%{_kf5_libdir}/libkoversion.so*
# core-libs ?
%{_kf5_qtplugindir}/calligra/colorspaces/kolcmsengine.so
%{_kf5_qtplugindir}/calligra/devices/calligra_device_spacenavigator.so
%{_kf5_qtplugindir}/calligra/dockers/calligra_docker_defaults.so
%{_kf5_qtplugindir}/calligra/dockers/calligra_docker_stencils.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_eps2svgai.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_key2odp.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_kpr2odp.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_pdf2odg.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_pdf2svg.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_vsdx2odg.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_wmf2svg.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_xfig2odg.so
%{_kf5_qtplugindir}/calligra/pageapptools/kopabackgroundtool.so
%{_kf5_qtplugindir}/calligra/shapefiltereffects/calligra_filtereffects.so
%{_kf5_qtplugindir}/calligra/shapes/calligra_shape_artistictext.so
%{_kf5_qtplugindir}/calligra/shapes/calligra_shape_chart.so
%{_kf5_qtplugindir}/calligra/shapes/calligra_shape_formula.so
%{_kf5_qtplugindir}/calligra/shapes/calligra_shape_music.so
%{_kf5_qtplugindir}/calligra/shapes/calligra_shape_paths.so
%{_kf5_qtplugindir}/calligra/shapes/calligra_shape_picture.so
%{_kf5_qtplugindir}/calligra/shapes/calligra_shape_plugin.so
%{_kf5_qtplugindir}/calligra/shapes/calligra_shape_text.so
%{_kf5_qtplugindir}/calligra/shapes/calligra_shape_vector.so
%{_kf5_qtplugindir}/calligra/shapes/calligra_shape_video.so
%{_kf5_qtplugindir}/calligra/textediting/calligra_textediting_autocorrect.so
%{_kf5_qtplugindir}/calligra/textediting/calligra_textediting_changecase.so
%{_kf5_qtplugindir}/calligra/textediting/calligra_textediting_spellcheck.so
%{_kf5_qtplugindir}/calligra/textediting/calligra_textediting_thesaurus.so
%{_kf5_qtplugindir}/calligra/textinlineobjects/calligra_textinlineobject_variables.so
%{_kf5_qtplugindir}/calligra/tools/calligra_tool_basicflakes.so
%{_kf5_qtplugindir}/calligra/tools/calligra_tool_defaults.so
%{_kf5_qtplugindir}/calligradocinfopropspage.so
%{_kf5_qtplugindir}/calligraimagethumbnail.so
%{_kf5_qtplugindir}/calligrathumbnail.so
#{_kf5_qtplugindir}/kreport/planreport_textplugin.so

%files l10n -f %{name}.lang
# includes en/ docs, rename to -doc instead? -- rdieter
%{_kf5_datadir}/applications/calligra.desktop

%files sheets 
%{_kf5_bindir}/calligrasheets
%{_kf5_libdir}/libkdeinit5_calligrasheets.so
%{_kf5_datadir}/calligrasheets/
%{_kf5_sysconfdir}/xdg/calligrasheetsrc
%{_kf5_datadir}/applications/org.kde.calligrasheets.desktop
%{_kf5_metainfodir}/org.kde.calligrasheets.appdata.xml
%{_kf5_datadir}/kxmlgui5/calligrasheets
%{_kf5_datadir}/config.kcfg/calligrasheets.kcfg
%{_kf5_datadir}/kservices5/ServiceMenus/calligra/sheets_print.desktop
%{_kf5_datadir}/kservices5/sheets_excel_thumbnail.desktop
%{_kf5_datadir}/kservices5/sheets_ods_thumbnail.desktop
%{_kf5_datadir}/kservices5/sheets_xlsx_thumbnail.desktop
%{_kf5_datadir}/templates/SpreadSheet.desktop
%{_kf5_datadir}/templates/.source/SpreadSheet.ods

%ldconfig_scriptlets sheets-libs

%files sheets-libs
%{_libdir}/libcalligrasheetscommon.so*
%{_libdir}/libcalligrasheetsodf.so*
%{_kf5_qtplugindir}/calligrasheets/
%{_kf5_qtplugindir}/calligra/parts/calligrasheetspart.so
#
#{_kf5_qtplugindir}/calligra/shapes/calligra_shape_spreadsheet.so
#{_kf5_qtplugindir}/calligra/deferred/calligra_shape_spreadsheet-deferred.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_applixspread2kspread.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_dbase2kspread.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_csv2sheets.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_gnumeric2sheets.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_kspread2tex.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_opencalc2sheets.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_qpro2sheets.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_sheets2csv.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_sheets2gnumeric.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_sheets2html.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_sheets2opencalc.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_xls2ods.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_xlsx2ods.so

%files stage 
#doc stage/AUTHORS stage/CHANGES
%{_bindir}/calligrastage
%{_libdir}/libkdeinit5_calligrastage.so
%{_kf5_datadir}/applications/org.kde.calligrastage.desktop
%{_kf5_metainfodir}/org.kde.calligrastage.appdata.xml
%{_kf5_datadir}/kservices5/ServiceMenus/calligra/stage_print.desktop
%{_kf5_datadir}/calligrastage
%{_kf5_sysconfdir}/xdg/calligrastagerc
%{_kf5_datadir}/kxmlgui5/calligrastage
%{_kf5_datadir}/kservices5/stage_key_thumbnail.desktop
%{_kf5_datadir}/kservices5/stage_kpr_thumbnail.desktop
%{_kf5_datadir}/kservices5/stage_odp_thumbnail.desktop
%{_kf5_datadir}/kservices5/stage_powerpoint_thumbnail.desktop
%{_kf5_datadir}/kservices5/stage_pptx_thumbnail.desktop
%{_kf5_datadir}/templates/.source/Presentation.odp
%{_kf5_datadir}/templates/Presentation.desktop

%ldconfig_scriptlets stage-libs

%files stage-libs
%{_kf5_libdir}/libcalligrastageprivate.so*
%{_kf5_qtplugindir}/calligra/parts/calligrastagepart.so
#
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_ppt2odp.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_pptx2odp.so
%{_kf5_qtplugindir}/calligra/presentationeventactions/calligrastageeventactions.so
%{_kf5_qtplugindir}/calligra/textinlineobjects/kprvariables.so
%{_kf5_qtplugindir}/calligrastage/pageeffects/kpr_pageeffect_barwipe.so
%{_kf5_qtplugindir}/calligrastage/pageeffects/kpr_pageeffect_clockwipe.so
%{_kf5_qtplugindir}/calligrastage/pageeffects/kpr_pageeffect_edgewipe.so
%{_kf5_qtplugindir}/calligrastage/pageeffects/kpr_pageeffect_fade.so
%{_kf5_qtplugindir}/calligrastage/pageeffects/kpr_pageeffect_iriswipe.so
%{_kf5_qtplugindir}/calligrastage/pageeffects/kpr_pageeffect_matrixwipe.so
%{_kf5_qtplugindir}/calligrastage/pageeffects/kpr_pageeffect_slidewipe.so
%{_kf5_qtplugindir}/calligrastage/pageeffects/kpr_pageeffect_spacerotation.so
%{_kf5_qtplugindir}/calligrastage/pageeffects/kpr_pageeffect_swapeffect.so
%{_kf5_qtplugindir}/calligrastage/shapeanimations/kpr_shapeanimation_example.so
%{_kf5_qtplugindir}/calligrastage/tools/calligrastagetoolanimation.so

%posttrans karbon
update-desktop-database -q &> /dev/null ||:

%postun karbon
if [ $1 -eq 0 ] ; then
update-desktop-database -q &> /dev/null ||:
fi

%files karbon
%{_kf5_sysconfdir}/xdg/karbonrc
%{_kf5_datadir}/applications/org.kde.karbon.desktop
%{_kf5_metainfodir}/org.kde.karbon.appdata.xml
%{_kf5_bindir}/karbon
%{_kf5_libdir}/libkdeinit5_karbon.so
%{_kf5_datadir}/karbon/
%{_kf5_datadir}/kservices5/ServiceMenus/calligra/karbon_print.desktop
%{_kf5_datadir}/kservices5/karbon_karbon1x_thumbnail.desktop
%{_kf5_datadir}/kservices5/karbon_wmf_thumbnail.desktop
%{_kf5_datadir}/kservices5/karbon_wpg_thumbnail.desktop
%{_kf5_datadir}/kservices5/karbon_xfig_thumbnail.desktop
%{_kf5_datadir}/kxmlgui5/karbon/
%{_kf5_datadir}/templates/.source/Illustration.odg
%{_kf5_datadir}/templates/Illustration.desktop

%ldconfig_scriptlets karbon-libs

%files karbon-libs
%{_kf5_libdir}/libkarboncommon.so*
%{_kf5_libdir}/libkarbonui.so*
%{_kf5_qtplugindir}/calligra/parts/karbonpart.so
#
%{_kf5_qtplugindir}/calligra/tools/karbon_tools.so
%{_kf5_qtplugindir}/karbon/extensions/karbon_flattenpath.so
%{_kf5_qtplugindir}/karbon/extensions/karbon_refinepath.so
%{_kf5_qtplugindir}/karbon/extensions/karbon_roundcorners.so
%{_kf5_qtplugindir}/karbon/extensions/karbon_whirlpinch.so
#
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_karbon1x2karbon.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_karbon2image.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_karbon2svg.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_karbon2wmf.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_svg2karbon.so

%posttrans words
update-desktop-database -q &> /dev/null ||:

%postun words
if [ $1 -eq 0 ] ; then
update-desktop-database -q &> /dev/null ||:
fi

%files words
%{_kf5_bindir}/calligrawords
%{_kf5_libdir}/libkdeinit5_calligrawords.so
%{_kf5_sysconfdir}/xdg/calligrawordsrc
%{_kf5_datadir}/applications/org.kde.calligrawords.desktop
%{_kf5_datadir}/applications/org.kde.calligrawords_ascii.desktop
%{_kf5_metainfodir}/org.kde.calligrawords.appdata.xml
%{_kf5_datadir}/calligrawords/
%{_kf5_datadir}/templates/TextDocument.desktop
%{_kf5_datadir}/templates/.source/TextDocument.odt
%{_kf5_datadir}/kxmlgui5/calligrawords/
#{_kf5_datadir}/applications/calligra_filter_odt2docx.desktop
%{_kf5_datadir}/kservices5/ServiceMenus/calligra/words_print.desktop
%{_kf5_datadir}/kservices5/words_docx_thumbnail.desktop
%{_kf5_datadir}/kservices5/words_msword_thumbnail.desktop
%{_kf5_datadir}/kservices5/words_odt_thumbnail.desktop
%{_kf5_datadir}/kservices5/words_rtf_thumbnail.desktop
%{_kf5_datadir}/kservices5/words_wpd_thumbnail.desktop
%{_kf5_datadir}/kservices5/words_wps_thumbnail.desktop

%ldconfig_scriptlets words-libs

%files words-libs
%{_kf5_libdir}/libwordsprivate.so*
%{_kf5_qtplugindir}/calligra/parts/calligrawordspart.so
#
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_applixword2odt.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_ascii2words.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_doc2odt.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_docx2odt.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_html2ods.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_odt2ascii.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_odt2docx.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_odt2epub2.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_odt2html.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_odt2mobi.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_odt2wiki.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_rtf2odt.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_wpd2odt.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_wpg2odg.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_wpg2svg.so
%{_kf5_qtplugindir}/calligra/formatfilters/calligra_filter_wps2odt.so

%if 0%{?okular}
%files okular-odpgenerator
%{_kf5_libdir}/libkookularGenerator_odp.so*
%{_kf5_qtplugindir}/okular/generators/okularGenerator_odp_calligra.so
%{_kf5_qtplugindir}/okular/generators/okularGenerator_powerpoint_calligra.so
%{_kf5_qtplugindir}/okular/generators/okularGenerator_pptx_calligra.so
%{_kf5_datadir}/applications/okularApplication_odp_calligra.desktop
%{_kf5_datadir}/applications/okularApplication_powerpoint_calligra.desktop
%{_kf5_datadir}/applications/okularApplication_pptx_calligra.desktop
%{_kf5_datadir}/kservices5/okularOdp_calligra.desktop
%{_kf5_datadir}/kservices5/okularPowerpoint_calligra.desktop
%{_kf5_datadir}/kservices5/okularPptx_calligra.desktop

%files okular-odtgenerator
%{_kf5_libdir}/libkookularGenerator_odt.so*
%{_kf5_qtplugindir}/okular/generators/okularGenerator_doc_calligra.so
%{_kf5_qtplugindir}/okular/generators/okularGenerator_docx_calligra.so
%{_kf5_qtplugindir}/okular/generators/okularGenerator_odt_calligra.so
%{_kf5_qtplugindir}/okular/generators/okularGenerator_powerpoint_calligra.so
%{_kf5_qtplugindir}/okular/generators/okularGenerator_rtf_calligra.so
%{_kf5_qtplugindir}/okular/generators/okularGenerator_wpd_calligra.so
%{_kf5_datadir}/applications/okularApplication_doc_calligra.desktop
%{_kf5_datadir}/applications/okularApplication_docx_calligra.desktop
%{_kf5_datadir}/applications/okularApplication_odt_calligra.desktop
%{_kf5_datadir}/applications/okularApplication_rtf_calligra.desktop
%{_kf5_datadir}/applications/okularApplication_wpd_calligra.desktop
%{_kf5_datadir}/kservices5/okularDoc_calligra.desktop
%{_kf5_datadir}/kservices5/okularDocx_calligra.desktop
%{_kf5_datadir}/kservices5/okularOdt_calligra.desktop
%{_kf5_datadir}/kservices5/okularRtf_calligra.desktop
%{_kf5_datadir}/kservices5/okularWpd_calligra.desktop
%endif


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.1-20
- Rebuild for gsl-2.7.1

* Mon Aug 08 2022 Marek Kasik <mkasik@redhat.com> - 3.2.1-19
- Rebuild for poppler-22.08.0
- Backport necessary changes from upstream

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 24 2022 Rex Dieter <rdieter@fedoraproject.org> - 3.2.1-17
- rebuild (poppler)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Marek Kasik <mkasik@redhat.com> - 3.2.1-15
- Rebuild for poppler-22.01.0
- Switch to C++17 because it is needed by poppler now

* Sun Nov 28 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.2.1-14
- Rebuild for libgit2 1.3.x

* Thu Aug 05 2021 Marek Kasik <mkasik@redhat.com> - 3.2.1-13
- Rebuild for poppler-21.08.0

* Sun Aug 01 2021 Rex Dieter <rdieter@fedoraproject.org> - 3.2.1-12
- pull in upstream 3.2 branch fixes

* Sun Aug 01 2021 Richard Shaw <hobbes1069@gmail.com> - 3.2.1-11
- Move to openexr2 compat package.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Marek Kasik <mkasik@redhat.com> - 3.2.1-8
- Rebuild for poppler-21.01.0

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 3.2.1-7
- Rebuild for OpenEXR 2.5.3.

* Mon Dec 28 19:00:18 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.2.1-6
- Rebuild for libgit2 1.1.x

* Wed Oct 14 2020 Jeff Law <law@redhat.com> - 3.2.1-5
- Add missing #includes for gcc-11

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.2.1-2
- rebuild (poppler)

* Fri May 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.2.1-1
- 3.2.1

* Fri Apr 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Wed Apr 08 2020 Rex Dieter <rdieter@fedoraproject.org> - 3.1.90-1
- 3.1.90 (3.2 beta1)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 3.1.0-18
- Rebuild for poppler-0.84.0

* Fri Aug 23 2019 Adam Williamson <awilliam@redhat.com> - 3.1.0-17
- Backport upstream fix for compile with Qt 5.13

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.1.0-16
- Rebuilt for GSL 2.6.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Richard Shaw <hobbes1069@gmail.com> - 3.1.0-14
- Rebuild for OpenEXR 2.3.0.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Marek Kasik <mkasik@redhat.com> - 3.1.0-12
- Rebuild for poppler-0.73.0

* Wed Dec 05 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-11
- (re)enable stage (#1518400)

* Tue Aug 14 2018 Marek Kasik <mkasik@redhat.com> - 3.1.0-10
- Rebuild for poppler-0.67.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-8
- Upstream Qt-5.11 fixes

* Sun Apr 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-7
- rebuild (okular)

* Fri Apr 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-6
- calligra-sheets package doesn't depend on calligra-sheets-libs (#1563177)
- use %%make_build %%ldconfig_scriptlets

* Fri Mar 23 2018 Marek Kasik <mkasik@redhat.com> - 3.1.0-5
- Rebuild for poppler-0.63.0

* Fri Mar 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-4
- rebuild

* Wed Feb 14 2018 David Tardon <dtardon@redhat.com> - 3.1.0-3
- rebuild for poppler 0.62.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.1.0-1
- calligra-3.1.0 (#1539266)

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.90-3
- Remove obsolete scriptlets

* Sun Jan 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.0.90-2
- fix -core/-libs to avoid dep on -stage

* Thu Jan 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.0.90-1
- calligra-3.0.90
- drop calligra-plan (packaged separately)
- +kf5+kinit_requires as needed

* Fri Dec 29 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-15
- rebuild (okular)

* Wed Dec 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-14
- omit incompatible KF5AkonadiContacts/KF5CalendarCore components (for now)

* Fri Nov 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-13
- use %%_kf5_metainfodir macro

* Wed Nov 08 2017 David Tardon <dtardon@redhat.com> - 3.0.1-13
- rebuild for poppler 0.61.0

* Fri Oct 06 2017 David Tardon <dtardon@redhat.com> - 3.0.1-12
- rebuild for poppler 0.60.1

* Wed Sep 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-11
- rebuild (marble)

* Fri Sep 08 2017 David Tardon <dtardon@redhat.com> - 3.0.1-10
- rebuild for poppler 0.59.0

* Thu Aug 03 2017 David Tardon <dtardon@redhat.com> - 3.0.1-9
- rebuild for poppler 0.57.0

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 3.0.1-8
- Rebuild with binutils fix for ppc64le (#1475636)

* Tue Jul 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-7
- rebuild (gsl)

* Wed Jul 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-6
- drop empty -flow subpkg (#1470345)

* Mon Jun 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-5
- -l10n subpkg

* Tue Jun 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-4
- fix/move plugins to make apps independantly installable

* Tue Jun 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-3
- main: drop Requires: -author
- Obsoletes: -braindump-libs

* Mon Jun 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.1-2
- more Obsoletes: -author -reports-map-element -kexi-map-form-widget

* Tue Mar 28 2017 David Tardon <dtardon@redhat.com> - 2.9.11-20
- rebuild for poppler 0.53.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.9.11-18
- drop okular support on f26+

* Wed Jan 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.9.11-17
- -okular-*: (Build)Requires: s/okular/okular4/

* Wed Dec 28 2016 Rich Mattes <richmattes@gmail.com> - 2.9.11-16
- Rebuild for eigen3-3.3.1

* Sun Dec 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.9.11-15
- Backport upstream plan-related fixes (#1382445,kde#359537)

* Sun Dec 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.9.11-14
- filters/karbon/pdf: drop libjpeg/openjpeg overlinking
- make openjpeg build dep krita-only

* Fri Dec 16 2016 David Tardon <dtardon@redhat.com> - 2.9.11-13
- rebuild for poppler 0.50.0

* Thu Nov 24 2016 Orion Poplawski <orion@cora.nwra.com> - 2.9.11-12
- Rebuild for poppler 0.49.0

* Fri Oct 21 2016 Marek Kasik <mkasik@redhat.com> - 2.9.11-11
- Rebuild for poppler-0.48.0

* Sun Oct 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.9.11-10
- omit krita on f25+, now packaged separately (#1376994)

* Thu Aug 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.9.11-9
- fix typo in -kexi-driver-mysql (#1370037)

* Mon Jul 18 2016 Marek Kasik <mkasik@redhat.com> - 2.9.11-8
- Rebuild for poppler-0.45.0

* Tue May 31 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.9.11-7
- calligra: allow >= krita versions, as future krita's will be released separately

* Tue May  3 2016 Marek Kasik <mkasik@redhat.com> - 2.9.11-6
- Rebuild for poppler-0.43.0

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 2.9.11-5
- rebuild for ICU 57.1

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.9.11-4
- Rebuild for gsl 2.1

* Tue Feb 09 2016 Rex Dieter <rdieter@fedoraproject.org> 2.9.11-3
- rebuild (okular)

* Tue Feb 09 2016 Rex Dieter <rdieter@fedoraproject.org> 2.9.11-2
- support kf5 ServiceMenus

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> 2.9.11-1
- 2.9.11
- disable FTBFS krita gmic plugin on fc24+ (gcc6 internal compiler error)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Rex Dieter <rdieter@fedoraproject.org> 2.9.10-4
- rebuild (boost)

* Fri Jan 22 2016 Marek Kasik <mkasik@redhat.com> - 2.9.10-3
- Rebuild for poppler-0.40.0

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 2.9.10-2
- Rebuild for glew 1.13

* Wed Dec 09 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.10-1
- 2.9.10

* Fri Nov 06 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.9-1
- 2.9.9

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 2.9.8-3
- rebuild for ICU 56.1

* Fri Oct 16 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.8-2
- kexi-map-form-widget: drop hard-coded marble dep

* Tue Oct 13 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.8-1
- 2.9.8

* Sun Sep 20 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.7-2
- rebuild (marble)

* Thu Sep 03 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.7-1
- 2.9.7 (#1241726)

* Tue Sep 01 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.6-9
- rebuild (marble)

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.9.6-8
- Rebuilt for Boost 1.59

* Mon Aug 10 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.6-7
- (re)enable pstoedit support, bug #1183335 fixed

* Tue Aug 04 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.6-6
- kexi: Requires: kate-part (epel7)

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Tue Jul 28 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.6-4
- pull in minor/cosmetic upstream commits (version, .desktop validation)

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.9.6-3
- rebuild for Boost 1.58

* Wed Jul 22 2015 Marek Kasik <mkasik@redhat.com> 2.9.6-2
- Rebuild (poppler-0.34.0)

* Tue Jul 14 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.6-1
- 2.9.6 (#1241726)

* Wed Jun 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.9.5-3
- rebuild (exiv2)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.5-1
- 2.9.5 (#1228439), libwps-0.4 support f23+ only

* Sat Jun 06 2015 David Tardon <dtardon@redhat.com> - 2.9.4-5
- enable Apple Keynote import
- adapt to libwps 0.4

* Fri Jun  5 2015 Marek Kasik <mkasik@redhat.com> 2.9.4-4
- Rebuild (poppler-0.33.0)

* Fri May 22 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.4-3
- rebuild (libwps)

* Thu May 07 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.4-2
- -qtquick subpkg, -kexi: move kexirelationdesignshape here

* Thu May 07 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.4-1
- 2.9.4, BR: s/marble-devel/marble-widget-devel/

* Mon Apr 20 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.2-4
- kexi-libs: Requires: kate4-part (#1213229, kde#346373)

* Sun Apr 19 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.2-3
- rebuild (marble)

* Mon Apr 06 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.2-2
- backport "fix csv import" (kde#344718)

* Fri Apr 03 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.2-1
- 2.9.2

* Sun Mar 15 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.1-1
- calligra-2.9.1 (#1202153)

* Fri Mar 13 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.0-4
- -core: move kexirelationdesignshape plugin here (to match the .desktop file)

* Mon Mar 09 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.0-3
- rebuild (GraphicsMagick)

* Sun Mar 01 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.0-2
- rebuild

* Thu Feb 26 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.0-1
- 2.9.0

* Thu Feb 26 2015 Rex Dieter <rdieter@fedoraproject.org> 2.8.7-10
- rebuild (gcc5)

* Wed Feb 04 2015 Petr Machata <pmachata@redhat.com> - 2.8.7-9
- Bump for rebuild.

* Sun Feb 01 2015 Rex Dieter <rdieter@fedoraproject.org> 2.8.7-8
- don't own %%_datadir/appdata (#1188049)

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2.8.7-7
- Rebuild for boost 1.57.0

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2.8.7-6
- Rebuild for boost 1.57.0

* Fri Jan 23 2015 Marek Kasik <mkasik@redhat.com> 2.8.7-5
- Rebuild (poppler-0.30.0)

* Sun Jan 18 2015 Rex Dieter <rdieter@fedoraproject.org> 2.8.7-4
- kde-applications fixes
- disable pstoedit support on f22+ (#1183335)

* Sun Dec 21 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.7-3
- move libcalligradb to -libs, libkoreport now depends on it (#1176398)

* Wed Dec 10 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.7-2
- rebuild (marble)

* Fri Dec 05 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.7-1
- 2.8.7
- -core: +Requires: calligra-l10n

* Thu Nov 27 2014 Marek Kasik <mkasik@redhat.com> 2.8.6-3
- Rebuild (poppler-0.28.1)

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.6-2
- rebuild (openexr)

* Mon Sep 22 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.6-1
- 2.8.6

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 2.8.5-6
- rebuild for ICU 53.1

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.5-4
- rebuild (okular)

* Wed Aug 06 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.5-3
- rebuild (kde-4.13.97)

* Mon Jul 14 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.5-2
- rebuild (marble)

* Sun Jul 06 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.5-1
- 2.8.5

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.4-2
- optimize mimeinfo scriptlet

* Tue Jun 24 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.4-1
- 2.8.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 David Tardon <dtardon@redhat.com> - 2.8.3-3
- switch to librevenge-based import libs

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 2.8.3-2
- Rebuild for boost 1.55.0

* Thu May 15 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.3-1
- 2.8.3

* Tue May 13 2014 Marek Kasik <mkasik@redhat.com> 2.8.2-4
- Rebuild (poppler-0.26.0)

* Fri May 09 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.2-3
- fix dep on marble-part (no epoch)

* Wed May 07 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.2-2
- okular-odpgenerator: Requires: okular-part
- reports-map-element: Requires: marble-part

* Wed Apr 16 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.2-1
- 2.8.2

* Fri Apr 04 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.1-3
- rebuild (okular)

* Sat Mar 29 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.1-2
- respin tarball (omitting typo)

* Tue Mar 25 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.1-1
- 2.8.1

* Thu Mar 20 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-2
- rebuild (kde-4.13)

* Sun Mar 02 2014 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-1
- 2.8.0

* Wed Feb 12 2014 Rex Dieter <rdieter@fedoraproject.org> 2.7.92-2
- rebuild (libicu)

* Sun Feb 09 2014 Rex Dieter <rdieter@fedoraproject.org> 2.7.92-1
- 2.7.92

* Mon Jan 13 2014 Rex Dieter <rdieter@fedoraproject.org> 2.7.91-1
- 2.7.91
- BR: +libodfgen-devel -OpenGTL-devel

* Mon Dec 16 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.90-3
- krita: fix handling of unversioned libkritasketchlib.so

* Sun Dec 15 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.90-2
- enable use of libpqxx-4.x

* Fri Dec 13 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.90-1
- 2.7.90

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.7.5-2
- rebuild (exiv2)

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.5-1
- calligra-2.7.5

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 2.7.4-3
- rebuilt for GLEW 1.10

* Sat Nov 16 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.4-2
- rebuild (kde-4.12)

* Sat Oct 12 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.4-1
- calligra-2.7.4

* Fri Sep 20 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.3-1
- calligra-2.7.3 (#951003)

* Sun Sep 08 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.2-3
- rebuild (openexr)

* Thu Sep 05 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.2-2
- rebuild (for libkdcraw-4.11.x)

* Fri Aug 23 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.2-1
- calligra-2.7.2 (#951003)

* Mon Aug 19 2013 Marek Kasik <mkasik@redhat.com> 2.7.1-2
- Rebuild (poppler-0.24.0)

* Wed Jul 31 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.1-1
- 2.7.1

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 2.7.0-3
- Rebuild for boost 1.54.0

* Sat Jul 20 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.0-2
- fix arm FTBFS (qreal_double.patch courtesy of kubuntu)

* Fri Jul 19 2013 Rex Dieter <rdieter@fedoraproject.org> 2.7.0-1
- 2.7.0

* Sat Jun 29 2013 Rex Dieter <rdieter@fedoraproject.org> 2.6.92-1
- 2.6.92

* Mon Jun 24 2013 Marek Kasik <mkasik@redhat.com> 2.6.4-2
- Rebuild (poppler-0.22.5)

* Thu May 30 2013 Rex Dieter <rdieter@fedoraproject.org> 2.6.4-1
- 2.6.4 (#951003)

* Thu Apr 11 2013 Rex Dieter <rdieter@fedoraproject.org> 2.6.3-1
- 2.6.3

* Tue Mar 26 2013 Rex Dieter <rdieter@fedoraproject.org> 2.6.2-4
- explicitly omit bundled Arev fonts

* Sat Mar 23 2013 Rex Dieter <rdieter@fedoraproject.org> 2.6.2-3
- cannot display formulas (kde#317195)

* Mon Mar 18 2013 Rex Dieter <rdieter@fedoraproject.org> 2.6.2-2
- rebuild (OpenGTL)

* Mon Mar 11 2013 Rex Dieter <rdieter@fedoraproject.org> 2.6.2-1
- 2.6.2

* Sun Mar 10 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.6.1-3
- rebuild (OpenEXR)

* Mon Mar 04 2013 Rex Dieter <rdieter@fedoraproject.org> 2.6.1-2.1
- rebuild (f18/marble)

* Tue Feb 19 2013 Rex Dieter <rdieter@fedoraproject.org> 2.6.1-2
- rebuild (OpenGTL/llvm)

* Mon Feb 18 2013 Rex Dieter <rdieter@fedoraproject.org> 2.6.1-1
- 2.6.1

* Mon Feb 04 2013 Rex Dieter <rdieter@fedoraproject.org> 2.6.0-1
- 2.6.0

* Sat Jan 26 2013 Rex Dieter <rdieter@fedoraproject.org> 2.5.93-4
- rebuild (icu)

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2.5.93-3
- rebuild due to "jpeg8-ABI" feature drop

* Fri Jan 18 2013 Marek Kasik <mkasik@redhat.com> 2.5.93-2
- Rebuild (poppler-0.22.0)

* Sat Jan 05 2013 Rex Dieter <rdieter@fedoraproject.org> 2.5.93-1
- 2.5.93

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 2.5.92-3
- Rebuild for glew 1.9.0

* Tue Dec 04 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.92-2
- rebuild (marble)

* Wed Nov 28 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.92-1
- 2.5.92

* Wed Oct 24 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.91-1
- 2.5.91

* Mon Oct 08 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.3-1
- 2.5.3

* Sat Sep 08 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.2-1
- 2.5.2

* Wed Aug 29 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.1-1
- 2.5.1

* Sun Aug 26 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.0-3
- calligra is FTBFS on ARM, qreal = float (bug #851851)

* Tue Aug 07 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.0-2
- respin

* Sat Aug 04 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.0-1
- 2.5.0

* Fri Jul 27 2012 Rex Dieter <rdieter@fedoraproject.org> 2.4.92-4
- rebuild (glew)

* Thu Jul 19 2012 Dan Horák <dan[at]danny.cz> 2.4.92-3
- OpenGTL is missing on s390(x)

* Wed Jul 18 2012 Rex Dieter <rdieter@fedoraproject.org> 2.4.92-2
- BR: libvisio-devel

* Sat Jul 14 2012 Rex Dieter <rdieter@fedoraproject.org> 2.4.92-1
- calligra-2.4.92

* Mon Jul  2 2012 Marek Kasik <mkasik@redhat.com> - 2.4.91-3
- Rebuild (poppler-0.20.1)

* Sun Jun 17 2012 Rex Dieter <rdieter@fedoraproject.org> 2.4.91-2
- tarball respin

* Fri Jun 15 2012 Rex Dieter <rdieter@fedoraproject.org> 2.4.91-1
- calligra-2.4.91

* Wed Jun 06 2012 Rex Dieter <rdieter@fedoraproject.org> 2.4.90-2
- fix kexi-map-form-widget Requires/Obsoletes logic

* Tue May 29 2012 Jaroslav Reznik <jreznik@redhat.com> 2.4.90-1
- calligra-2.4.90

* Sat May 26 2012 Rex Dieter <rdieter@fedoraproject.org> 2.4.2-1
- calligra-2.4.2

* Wed May 16 2012 Marek Kasik <mkasik@redhat.com> - 2.4.1-4
- Rebuild (poppler-0.20.0)

* Mon May 07 2012 Rex Dieter <rdieter@fedoraproject.org> 2.4.1-3
- segfault when opening a new doc / new from template (#819371)

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 2.4.1-2
- rebuild (exiv2)

* Sat Apr 21 2012 Rex Dieter <rdieter@fedoraproject.org> 2.4.1-1
- 2.4.1

* Fri Apr 20 2012 Rex Dieter <rdieter@fedoraproject.org> 2.4.0-4
- manifest file corrupted (#814643, kde#298134)

* Mon Apr 16 2012 Rex Dieter <rdieter@fedoraproject.org> 2.4.0-3
- -sheets: Provides: -tables

* Sun Apr 08 2012 Rex Dieter <rdieter@fedoraproject.org> 2.4.0-2
- -core/-libs: tighten subpkg deps

* Sat Apr 07 2012 Rex Dieter <rdieter@fedoraproject.org> 2.4.0-1
- 2.4.0
- Obsoletes: -map-shape (dropped since rc2)

* Sat Mar 17 2012 Rex Dieter <rdieter@fedoraproject.org> 2.3.92-1
- 2.3.92 (2.4rc2)
- rename -tables => -sheets

* Sat Mar 03 2012 Rex Dieter <rdieter@fedoraproject.org> 2.3.91-1
- 2.3.91 (2.4rc1)

* Sat Feb 11 2012 Rex Dieter <rdieter@fedoraproject.org> 2.3.87-4
- upstream krita_fitscreen patch (#788327)

* Wed Feb 08 2012 Rex Dieter <rdieter@fedoraproject.org> 2.3.87-3
- -braindump: move stateshape here

* Tue Jan 31 2012 Rex Dieter <rdieter@fedoraproject.org> 2.3.87-2
- -kexi: fix error in %%postun scriptlet

* Sat Jan 28 2012 Rex Dieter <rdieter@fedoraproject.org> 2.3.87-1
- 2.3.87

* Thu Jan 12 2012 Rex Dieter <rdieter@fedoraproject.org> 2.3.86-3
- %%build: -DBUILD_cstester:BOOL=OFF
- drop -filters

* Thu Jan 12 2012 Rex Dieter <rdieter@fedoraproject.org> 2.3.86-2
- rename kexi-driver-pgsql -> kexi-driver-postgresql
- kexi-driver-sybase subpkg
- kexi-map-form-widget, map-shape, reports-map-elemement subpkgs (with marble deps)

* Tue Jan 10 2012 Rex Dieter <rdieter@fedoraproject.org> 2.3.86-1
- 2.3.86
- License: +LGPLv2+
- drop Obsoletes: koffice-kivio

* Thu Aug 18 2011 Rex Dieter <rdieter@fedoraproject.org> 2.3.74-2
- fix Obsoletes: -kformula

* Mon Aug 15 2011 Rex Dieter <rdieter@fedoraproject.org> 2.3.74-1
- 2.3.74
- kformula dropped (upstream)

* Fri Jun 17 2011 Rex Dieter <rdieter@fedoraproject.org> 2.3.72-2
- fix URL
- Obsoletes: koffice < 3:2.3.70

* Thu Jun 16 2011 Rex Dieter <rdieter@fedoraproject.org> 2.3.72-1
- 2.3.72 (first try)

