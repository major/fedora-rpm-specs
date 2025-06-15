Name:           Pencil2D
Version:        0.7.0
Release:        %autorelease
Summary:        Create traditional hand-drawn animation (cartoon)
# For translations, check translations/*.ts.
# Our Summary is based on the upstream description. Since it must be edited to
# make a concise description, localized/translated summaries can be added only
# with sufficient knowledge of the languages in question. We can still have a
# full set of localized/translated descriptions. PR’s to add translated summary
# text are welcome.
# Summary(ar):    <?>
# Summary(bg):    (no upstream translation)
Summary(ca):    Crear animacions tradicionals fetes a mà (dibuixos animats)
# Summary(cs):    <?>
# Summary(da):    <?>
# Summary(de):    <?>
# Summary(el):    <?>
Summary(en):    Create traditional hand-drawn animation (cartoon)
Summary(es):    Crear animaciones (cartoons) de manera tradicional
# Summary(et):    (no upstream translation)
# Summary(fa):    (no upstream translation)
Summary(fr):    Créer une animation traditionnelle (dessin animé) à la main
# Summary(he):    <?>
# Summary(hu_HU): <?>
# Summary(id):    <?>
Summary(it):    Creare animazioni tradizionali disegnate a mano (cartoni animati)
# Summary(ja):    <?>
# Summary(kab):   <?>
# Summary(ko):    <?>
# Summary(nb):    (no upstream translation)
# Summary(nl_NL): (no upstream translation)
# Summary(pl):    <?>
Summary(pt_BR): Criar animações tradicionais feitas a mão (desenhos animados)
Summary(pt):    Criar animações tradicionais feitas a mão (desenhos animados)
# Summary(ru):    <?>
# Summary(sl):    <?>
# Summary(sv):    <?>
# Summary(tr):    <?>
# Summary(vi):    (no upstream translation)
# Summary(yue):   <?>
# Summary(zh_CN): <?>
# Summary(zh_TW): <?>

# The entire source is GPL-2.0-only, except:
#
# -----
#
# In LICENSE.QT.TXT, upstream reports:
#
#   The following source files are part of the examples of the Qt Toolkit:
#
#     core_lib/src/interface/flowlayout.cpp
#     core_lib/src/interface/flowlayout.h
#
#   The following source files are part of the QtCore module of the Qt Toolkit:
#
#     app/src/elidedlabel.cpp
#     app/src/elidedlabel.h
#
# All four files are BSD-3-Clause.
#
# The version of Qt from which these are taken is unknown, although based on
# the copyright date of 2016 and some comparison of sources, it seems to have
# been a Qt5 release. See:
#
#   https://github.com/qt/qtbase/blob/5.15/examples/widgets/layouts/flowlayout/flowlayout.h
#   https://github.com/qt/qtbase/blob/5.15/examples/widgets/layouts/flowlayout/flowlayout.cpp
#
# It looks like, despite upstream’s description, the elidedlabel souces are
# also from an example shipped with qtbase (which contains QtCore) rather than
# from the QtCore library itself:
#
#   https://github.com/qt/qtbase/blob/5.15/examples/widgets/widgets/elidedlabel/elidedlabel.h
#   https://github.com/qt/qtbase/blob/5.15/examples/widgets/widgets/elidedlabel/elidedlabel.cpp
#
# Since all four files are from Qt examples rather than from library code, we
# do not treat these as a case of bundling.
#
# -----
#
# The following sources are “heavily influenced by” QAquarelle, which is
# GPL-2.0-or-later, and bear its copyright/license notice.
#   - core_lib/src/tool/strokeinterpolator.cpp
License:        GPL-2.0-only AND BSD-3-Clause AND GPL-2.0-or-later
# Additionally, the following are under other allowed licenses but, for one
# reason or another, do not contribute to the licenses of the binary RPMs.
#
# The following sources belong to a bundled copy of the miniz library
# (MZ_VERSION 10.1.0, corresponding to release 2.1.0, as of this writing);
# they are removed in %%prep in order to use the system miniz library, and
# their licenses do not contribute to the licenses of
# the binary RPMs.
#   - core_lib/src/miniz.cpp is MIT
#   - core_lib/src/miniz.h appears to be Unlicense
#
# The following source belongs to a bundled copy of Catch (catch2) (version
# 2.13.9 as of this writing); it is removed in %%prep in order to use the system
# Catch library. Because version 2.x (catch2) is header-only, it is treated as
# a static library and would contribute to the licenses of the binary RPMs,
# except that it is used only for test executables that are not installed.
#   - tests/src/catch.hpp is BSL-1.0
#
# The following source is part of support for Windows Installer, which is not
# used in this package; furthermore, it is OK to distribute in the source RPM
# because it is content (for which CC0-1.0 is allowed) rather than code (for
# which it is not-allowed).
#   - util/installer/cog.svg
SourceLicense:  %{shrink:
                %{license} AND
                BSL-1.0 AND
                CC0-1.0 AND
                MIT AND
                Unlicense
                }
URL:            https://www.pencil2d.org
%global forgeurl https://github.com/pencil2d/pencil
Source:         %{forgeurl}/archive/v%{version}/pencil-%{version}.tar.gz

# Ensure QDebug is included for all qDebug uses
# https://github.com/pencil2d/pencil/pull/1912
Patch:          0001-Ensure-QDebug-is-included-for-all-qDebug-uses.patch
# Use the latest GPLv2 license text
# https://github.com/pencil2d/pencil/pull/1914
# OK to patch license text downstream since the PR was merged upstream.
Patch:          %{forgeurl}/pull/1914.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  pkgconfig(Qt6)
# app/app.pro:
# QT += core widgets gui xml multimedia svg network
# core_lib/core_lib.pro:
# QT += core widgets gui xml multimedia svg
# tests/tests.pro:
# QT += core widgets gui xml multimedia svg
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)

# app/app.pro:
# CONFIG += precompile_header lrelease embed_translations
BuildRequires:  qt6-linguist

BuildRequires:  miniz-devel
# Header-only:
BuildRequires:  catch2-static

BuildRequires:  desktop-file-utils
# Required by guidelines (https://pagure.io/packaging-committee/issue/1053):
BuildRequires:  libappstream-glib
# Matches what gnome-software and others use:
BuildRequires:  appstream

BuildRequires:  help2man

# Required to import and export videos. This is essential functionality for an
# animation tool, so we make it a hard dependency.
BuildRequires:  /usr/bin/ffmpeg
Requires:       /usr/bin/ffmpeg

# Provides plugins required for loading SVG icons
# https://github.com/pencil2d/pencil/pull/1796#issuecomment-1805940297
Requires:       qt6-qtsvg

# For %%{_datadir}/icons/hicolor
Requires:       hicolor-icon-theme

%global app_id org.pencil2d.Pencil2D

# For translations, check translations/*.ts.
%description
Pencil2D is an animation/drawing software for Mac OS X, Windows, and Linux. It
lets you create traditional hand-drawn animation (cartoon) using both bitmap
and vector graphics.

%description -l ar
بنسل2دي هو برنامج رسوم متحركة متوفر لـ ماك أو أس أكس و ويندوز و لينكس. يسمح لك
بعمل رسوم متحركة متحركة مرسومة باليد برسوم نقطية أو متجهة.

# %%description -l bg
# (no upstream translation)

%description -l ca
Pencil2D es un software d’animació/dibuix per a Mac OS X, Windows i Linux.
Permet crear animacions tradicionals fetes a mà (dibuixos animats) utilitzant
gràfics rasteritzats i/o vectorials.

%description -l cs
Pencil2D je animační/kreslicí program pro operační systémy Mac OS X, Windows a
Linux. Dovolí vám tvořit tradiční ručně kreslenou animaci pomocí bitmapové i
vektorové grafiky

%description -l da
Pencil2D er et animations/tegne software for Mac OS X, Windows og Linux. Det
lader dig skabe traditionel håndtegnet animation (tegnefilm) med både bitmap og
vektor grafik.

%description -l de
Pencil2D ist eine Animations-/Zeichensoftware für Mac OS X, Windows und Linux.
Sie eignet sich zum Schaffen von traditioneller handgezeichneter Animation
(Zeichentrick) sowohl mit Raster- als auch mit Vektorgrafik.

%description -l el
Pencil2D είναι ένα λογισμικό κινουμένων σχεδίων/ζωγραφικής για Mac OS X,
Windows, και Linux. Δίνει τη δυνατότητα δημιουργίας παραδοσιακών, ζωγραφισμένων
στο χέρι κινούμενων σχεδίων (καρτούν) χρησιμοποιώντας bitmap και διανυσματική
γραφιστική.

%description -l en
Pencil2D is an animation/drawing software for Mac OS X, Windows, and Linux. It
lets you create traditional hand-drawn animation (cartoon) using both bitmap
and vector graphics.

%description -l es
Pencil2D es un programa de animación/dibujo para Mac OS X, Windows y Linux. Te
permite crear animaciones (cartoons) de manera tradicional y cuenta con mapa de
bits y gráficos vectoriales.

# %%description -l et
# (no upstream translation)

# %%description -l fa
# (no upstream translation)

%description -l fr
Pencil2D est un logiciel d’animation/dessin pour Mac OS X, Windows et Linux. Il
vous permet de créer une animation traditionnelle (dessin animé) à la main en
utilisant à la fois des images matricielles et des graphiques vectoriels.

%description -l he
Pencil2D היא תוכנת ציור והנפשה עבור Mac OS X, Windows ו-Linux. היא מאפשרת לך
ליצור הנפשות בסגנון מסורתי מצוייר ביד (cartoon) תוך שימוש בכלי מפת ביטים וכלים
וקטוריים.

%description -l hu_HU
A Pencil2D egy animáció készítő/rajzoló szoftver Mac OS X, Windows és Linux
rendszerekre. Hagyományos, kézzel rajzolt animációk készítésére alkalmas
bitképek és vektorgrafika használatával.

# %%description -l id
# (no upstream translation)

%description -l it
Pencil2D è un software di animazione/disegno per Mac OS X, Windows e Linux. Ti
consente di creare animazioni tradizionali disegnate a mano (cartoni animati)
utilizzando sia grafica bitmap che vettoriale.

%description -l ja
Pencil2DはMac OS X, Windows, and Linuxに対応したアニメーション及びドローイング
ソフトです。本ソフトウェアのベクター・ビットマップ両方の描画機能を使用して、一
般的なコマ送りアニメーションを作成できます。

%description -l kab
Pencil2D d aseɣẓan n usmussu akked usuneɣ i Mac OS X, Windows, akked Linux. Ad
k-yeǧǧ ad d-tesnulfuḍ unuɣen yettemwwiwilen ara tsunɣeḍ s ufus s useqdec n
wudlifen n bitmap akked wudlifen imawayen.

%description -l ko
Pencil2D는 맥 OS X, 윈도우, 리눅스에서 지원되는 애니메이션/그림그리기
소프트웨어입니다. 비트맵과 벡터 모두를 사용하여 손 그림 애니메이션(만화)를 만들
수 있게 해줍니다.

# %%description -l nb
# (no upstream translation)

# %%description -l nl_NL
# (no upstream translation)

%description -l pl
Pencil2D to program do animacji/rysowania dla Mac OS X, Windows, i Linux. Ono
pozwala ci tworzyć tradycyjne ręcznie rysowane animacje (kreskówki) używając
bitmap i grafiki wektorowej.

%description -l pt_BR
Pencil2D é um programa de animação/desenho para Mac OS X, Windows e Linux.
Permite criar animações tradicionais feitas a mão (desenhos animados)
utilizando gráficos bitmaps e vetoriais.

%description -l pt
Pencil2D é um programa de animação/desenho para Mac OS X, Windows e Linux.
Permite criar animações tradicionais feitas a mão (desenhos animados)
utilizando gráficos bitmaps e vetoriais.

%description -l ru
Pencil2D — программа для рисования и анимации, которая работает в Mac OS X,
Windows и Linux. С помощью неё можно создавать традиционную рисованную анимацию
(мультфильмы) на основе как растровой, так и векторной графики.

%description -l sl
Svinčnik2D je program za animacijo/risanje v Mac OS X, Windows in Linux-u. Z
njim lahko ustvarite tradicionalno ročno risano animacijo (risanko) s pomočjo
bitne in vektorske grafike

%description -l sv
Pencil2D är ett animations- / ritprogram för Mac OSX, Windows och Linux. Det
låter dig skapa traditionellt handritad animering (tecknat) med både bitmapp
och vektorgrafik.

%description -l tr
Pencil2D, Mac OS X, Windows ve Linux için bir animasyon/çizim yazılımıdır. Hem
bitmap hem de vektör grafikleri kullanarak geleneksel elle çizilmiş animasyon
(çizgi film) oluşturmanıza olanak tanır.

# %%description -l vi
# (no upstream translation)

%description -l yue
Pencil2D là một phần mềm hoạt hình / vẽ cho Mac OS X, Windows và Linux. Nó cho
phép bạn tạo hoạt ảnh vẽ tay truyền thống (phim hoạt hình) bằng cách sử dụng cả
đồ họa bitmap và đồ họa vector.

%description -l zh_CN
Pencil2D是适用于Mac OS X，Windows和Linux的动画/绘图软件。它允许您使用位图和矢量
图形创建传统的手绘动画（卡通）。

%description -l zh_TW
Pencil2D是适用于Mac OS X，Windows和Linux的动画/绘图软件。它允许您使用位图和矢量
图形创建传统的手绘动画（卡通）。


%prep
%autosetup -n pencil-%{version} -p1

# Unbundle miniz
rm -v core_lib/src/miniz.h core_lib/src/miniz.cpp
sed -r -i '/\bminiz\.(h|cpp)/d' core_lib/core_lib.pro
echo 'LIBS_PRIVATE += -lminiz' | tee -a */*.pro >/dev/null

# Unbundle catch2
rm -v tests/src/catch.hpp
sed -r -i '/\bcatch\.hpp/d' tests/tests.pro
echo 'INCLUDEPATH += "%{_includedir}/catch2"' >> tests/tests.pro


%conf
# We want the compiled-in version information to describe this as a release
# build to the user. We could set DEFINES+=PENCIL2D_RELEASE, but that would set
# QT_NO_DEBUG_OUTPUT; we would rather preserve that to help with debugging, as
# it does no harm except for a slight impact on performance. Instead, we define
# PENCIL2D_RELEASE_BUILD directly. See common.pri for details.
%{qmake_qt6} \
    PREFIX='%{_prefix}' \
    DEFINES+=PENCIL2D_RELEASE_BUILD \
    VERSION='%{version}'


%build
%make_build

# Sometimes the formatting in help2man-generated man pages is of poor to
# marginal quality; in this case, it is good enough that it is not worth
# furnishing a hand-written man page. We need QT_QPA_PLATFORM=offscreen to run
# the application in headless mode for long enough to print its --help output.
QT_QPA_PLATFORM=offscreen help2man --no-info --output=pencil2d.1 ./app/pencil2d


%install
%make_install INSTALL_ROOT='%{buildroot}'

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 pencil2d.1


%check
desktop-file-validate '%{buildroot}%{_datadir}/applications/%{app_id}.desktop'
appstream-util validate-relax --nonet \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'
appstreamcli validate --no-net --explain \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'

# Run catch tests; QT_QPA_PLATFORM=offscreen keeps us from needing xvfb-run.
QT_QPA_PLATFORM=offscreen ./tests/tests


%files
%license LICENSE.TXT LICENSE.QT.TXT

%doc README.md
%doc ChangeLog.md

%{_bindir}/pencil2d
%{_mandir}/man1/pencil2d.1*

%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/*/apps/%{app_id}.png
%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/mime/packages/%{app_id}.xml

%{_datadir}/bash-completion/completions/pencil2d
%{_datadir}/zsh/site-functions/_pencil2d


%changelog
%autochangelog
