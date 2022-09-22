%global __provides_exclude_from ^%{_libdir}/calibre/calibre/plugins/.*\.so$

%global _python_bytecompile_extra 0

Name:           calibre
Version:        5.43.0
Release:        %autorelease
Summary:        E-book converter and library manager
License:        GPLv3
URL:            https://calibre-ebook.com/

Source0:        https://download.calibre-ebook.com/%{version}/%{name}-%{version}.tar.xz

# Disable auto update from inside the app
Patch1:         calibre-no-update.patch

# Do not display multiple apps in desktop files, only the main app
# This is so gnome-software only 'sees' calibre once.
Patch3:         calibre-nodisplay.patch

# Switch from cchardet to uchardet
# cchardet is not maintained anymore:
#   https://github.com/PyYoshi/cChardet/issues/77
#   https://bugzilla.redhat.com/show_bug.cgi?id=2021804
# Backported from upstream:
#   https://github.com/kovidgoyal/calibre/commit/5c3385476f
Patch4:         calibre-replace-cchcardet-with-uchardet.patch

ExclusiveArch:  %{qt5_qtwebengine_arches}

# https://fedoraproject.org/wiki/Changes/RetireARMv7
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-qt5
BuildRequires:  podofo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  xdg-utils
BuildRequires:  chmlib-devel
BuildRequires:  sqlite-devel
BuildRequires:  libicu-devel
BuildRequires:  libpng-devel
BuildRequires:  libmtp-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  web-assets-devel
BuildRequires:  qt5-qtbase-static
BuildRequires:  libXrender-devel
BuildRequires:  openssl-devel
# calibre installer is so smart that it check for the presence of the
# directory (and then installs in the wrong place)
BuildRequires:  bash-completion
BuildRequires:  glib2-devel
BuildRequires:  fontconfig-devel
BuildRequires:  libinput-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libappstream-glib
BuildRequires:  optipng
BuildRequires:  python3dist(apsw)
BuildRequires:  python3dist(mechanize)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(css-parser)
BuildRequires:  python3dist(feedparser)
BuildRequires:  python3dist(netifaces)
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(soupsieve)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(regex)
BuildRequires:  python3dist(html5-parser) >= 0.4.8
BuildRequires:  python3dist(html2text)
BuildRequires:  python3dist(zeroconf)
BuildRequires:  python3dist(markdown) >= 3.0
BuildRequires:  python3dist(sip) >= 5.5
BuildRequires:  python3dist(pyqt-builder)
BuildRequires:  python3dist(pychm)
BuildRequires:  python3dist(pycrypto)
BuildRequires:  python3dist(sgmllib3k)
BuildRequires:  python3-speechd
BuildRequires:  python3-jeepney
BuildRequires:  hunspell-devel
BuildRequires:  qt5-qtwebengine-devel
BuildRequires:  python-qt5-webengine
BuildRequires:  hyphen-devel
BuildRequires:  qt5-qtimageformats
BuildRequires:  libstemmer-devel
BuildRequires:  uchardet-devel
# using the bundled mathjax until Fedora updates to 3.0.0
#BuildRequires:  mathjax
# Those are only used for tests. Do not add to runtime deps.
BuildRequires:  /usr/bin/jpegtran
BuildRequires:  /usr/bin/JxrDecApp

%{?pyqt5_requires}
# once ^^ %%pyqt5_requires is everywhere, can drop python-qt5 dep below -- rex

# Add hard dep to specific qtbase pkg, see build message below -- rex
# Project MESSAGE: This project is using private headers and will therefore be tied to this specific Qt module build version.
# Project MESSAGE: Running this project against other versions of the Qt modules may crash at any arbitrary point.
# Project MESSAGE: This is not a bug, but a result of using Qt internals. You have been warned!
BuildRequires:  qt5-qtbase-private-devel


Requires:       python3-qt5
Requires:       python-qt5-webengine
Requires:       qt5-qtwebengine
Requires:       qt5-qtsvg
Requires:       qt5-qtsensors
Requires:       qt5-qtimageformats
Requires:       poppler-utils
Requires:       liberation-sans-fonts
Requires:       liberation-serif-fonts
Requires:       liberation-mono-fonts
# using the bundled mathjax until Fedora updates to 3.0.0
#Requires:       mathjax
Requires:       optipng
Requires:       python3dist(odfpy)
Requires:       python3dist(lxml)
Requires:       python3dist(pillow)
Requires:       python3dist(mechanize)
Requires:       python3dist(python-dateutil)
Requires:       python3dist(beautifulsoup4)
Requires:       python3dist(soupsieve)
Requires:       python3dist(css-parser)
Requires:       python3dist(feedparser)
Requires:       python3dist(netifaces)
Requires:       python3dist(dnspython)
Requires:       python3dist(apsw)
Requires:       python3dist(psutil)
Requires:       python3dist(pygments)
Requires:       python3dist(msgpack)
Requires:       python3dist(regex)
Requires:       python3dist(html5-parser) >= 0.4.8
Requires:       python3dist(html2text)
Requires:       python3dist(markdown) >= 3.0
Requires:       python3dist(pychm)
Requires:       python3dist(pyqt5-sip) >= 12.8, python3dist(pyqt5-sip) < 13
Requires:       udisks2
Requires:       /usr/bin/jpegtran
Requires:       /usr/bin/JxrDecApp
Requires:       python3-jeepney
Recommends:     python3dist(zeroconf)

%description
Calibre is meant to be a complete e-library solution. It includes library
management, format conversion, news feeds to ebook conversion as well as
e-book reader sync features.

Calibre is primarily a ebook cataloging program. It manages your ebook
collection for you. It is designed around the concept of the logical book,
i.e. a single entry in the database that may correspond to ebooks in several
formats. It also supports conversion to and from a dozen different ebook
formats.

Supported input formats are: MOBI, LIT, PRC, EPUB, CHM, ODT, HTML, CBR, CBZ,
RTF, TXT, PDF and LRS.

%prep
%autosetup -n calibre-%{version} -p1

# remove shebangs
sed -i -e '/^#!\//, 1d' src/calibre/*/*/*/*/*.py
sed -i -e '/^#!\//, 1d' src/calibre/*/*/*/*.py
sed -i -e '/^#!\//, 1d' src/calibre/*/*/*.py
sed -i -e '/^#![ ]*\//, 1d' src/calibre/*/*.py
sed -i -e '/^#!\//, 1d' src/calibre/*.py
sed -i -e '/^#!\//, 1d' src/css_selectors/*.py
sed -i -e '/^#!\//, 1d' src/polyglot/*.py
sed -i -e '/^#!\//, 1d' src/templite/*.py
sed -i -e '/^#!\//, 1d' src/tinycss/*/*.py
sed -i -e '/^#!\//, 1d' src/tinycss/*.py
sed -i -e '/^#!\//, 1d' resources/default_tweaks.py

chmod -x src/calibre/*/*/*/*.py \
    src/calibre/*/*/*.py \
    src/calibre/*/*.py \
    src/calibre/*.py

# Using bundled mathjax until fedora goes to 3.0.0
# remove bundled MathJax
#rm -rvf resources/mathjax

%build
# unbundle MathJax
# using the bundled mathjax until Fedora updates to 3.0.0
#CALIBRE_PY3_PORT=1 \
#%%__python3 setup.py mathjax \
#    --system-mathjax \
#    --path-to-mathjax %%{_jsdir}/mathjax/

OVERRIDE_CFLAGS="%{optflags}" \
CALIBRE_PY3_PORT=1 \
%__python3 setup.py build

%install
mkdir -p %{buildroot}%{_datadir}

# create directory for calibre environment module
# the install script assumes it's there.
mkdir -p %{buildroot}%{python3_sitearch}

# create directory for completion files, so calibre knows where
# to install them
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions

LIBPATH="%{_libdir}" \
CALIBRE_PY3_PORT=1 \
%__python3 setup.py install --root=%{buildroot}%{_prefix} \
                            --prefix=%{_prefix} \
                            --libdir=%{_libdir} \
                            --staging-root=%{buildroot}%{_prefix} \
                            --staging-libdir=%{buildroot}%{_libdir} \
                            --staging-sharedir=%{buildroot}%{_datadir}

# remove shebang from init_calibre.py here because
# it just got spawned by the install script
sed -i -e '/^#!\//, 1d' %{buildroot}%{python3_sitearch}/init_calibre.py

# there are some python files there, do byte-compilation on them
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/calibre

# icons
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp -p resources/images/library.png                \
   %{buildroot}%{_datadir}/pixmaps/calibre-gui.png
cp -p resources/images/viewer.png                 \
   %{buildroot}%{_datadir}/pixmaps/calibre-viewer.png
cp -p resources/images/tweak.png                 \
   %{buildroot}%{_datadir}/pixmaps/calibre-ebook-edit.png

# packages aren't allowed to register mimetypes like this
rm -f %{buildroot}%{_datadir}/applications/defaults.list
rm -f %{buildroot}%{_datadir}/applications/mimeinfo.cache
rm -f %{buildroot}%{_datadir}/mime/application/*.xml
rm -f %{buildroot}%{_datadir}/mime/text/*.xml

# check .desktop files
desktop-file-validate \
    %{buildroot}%{_datadir}/applications/calibre-ebook-edit.desktop \
    %{buildroot}%{_datadir}/applications/calibre-ebook-viewer.desktop \
    %{buildroot}%{_datadir}/applications/calibre-gui.desktop \
    %{buildroot}%{_datadir}/applications/calibre-lrfviewer.desktop

# mimetype icon for lrf
rm -rf %{buildroot}%{_datadir}/icons/hicolor/128x128
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
cp -p resources/images/mimetypes/lrf.png \
      %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-sony-bbeb.png
cp -p resources/images/viewer.png \
      %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/calibre-viewer.png

# these are provided as separate packages
rm -rf %{buildroot}%{_libdir}/calibre/odf

# unbundle Liberation fonts
rm -f %{buildroot}%{_datadir}/calibre/fonts/liberation/*
ln --symbolic --relative \
    %{buildroot}%{_datadir}/fonts/liberation-mono/LiberationMono-BoldItalic.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationMono-BoldItalic.ttf
ln --symbolic --relative \
    %{buildroot}%{_datadir}/fonts/liberation-mono/LiberationMono-Bold.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationMono-Bold.ttf
ln --symbolic --relative \
    %{buildroot}%{_datadir}/fonts/liberation-mono/LiberationMono-Italic.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationMono-Italic.ttf
ln --symbolic --relative \
    %{buildroot}%{_datadir}/fonts/liberation-mono/LiberationMono-Regular.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationMono-Regular.ttf
ln --symbolic --relative \
    %{buildroot}%{_datadir}/fonts/liberation-sans/LiberationSans-BoldItalic.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationSans-BoldItalic.ttf
ln --symbolic --relative \
    %{buildroot}%{_datadir}/fonts/liberation-sans/LiberationSans-Bold.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationSans-Bold.ttf
ln --symbolic --relative \
    %{buildroot}%{_datadir}/fonts/liberation-sans/LiberationSans-Italic.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationSans-Italic.ttf
ln --symbolic --relative \
    %{buildroot}%{_datadir}/fonts/liberation-sans/LiberationSans-Regular.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationSans-Regular.ttf
ln --symbolic --relative \
    %{buildroot}%{_datadir}/fonts/liberation-serif/LiberationSerif-BoldItalic.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationSerif-BoldItalic.ttf
ln --symbolic --relative \
    %{buildroot}%{_datadir}/fonts/liberation-serif/LiberationSerif-Bold.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationSerif-Bold.ttf
ln --symbolic --relative \
    %{buildroot}%{_datadir}/fonts/liberation-serif/LiberationSerif-Italic.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationSerif-Italic.ttf
ln --symbolic --relative \
    %{buildroot}%{_datadir}/fonts/liberation-serif/LiberationSerif-Regular.ttf \
    %{buildroot}%{_datadir}/calibre/fonts/liberation/LiberationSerif-Regular.ttf

# Remove these 2 appdata files, we can only include one
rm -f %{buildroot}/%{_datadir}/metainfo/calibre-ebook-edit.appdata.xml
rm -f %{buildroot}/%{_datadir}/metainfo/calibre-ebook-viewer.appdata.xml
 
# rename MathJax folder to allow upgrade from 4.8.0-1 and earlier, which
# relied on a symlink handled by the %%preun and %%posttrans scriptlets
#mv %%{buildroot}%%{_datadir}/calibre/mathjax %%{buildroot}%%{_datadir}/calibre/mathjax-fedora

%check
TEST_ARGS=(
    # skip failing tests:
    --exclude-test-name unrar              # missing dependencies
    --exclude-test-name bonjour            # problems in mock
    --exclude-test-name 7z                 # missing dependencies
    --exclude-test-name test_searching     # python3 porting issue?
%ifarch %{ix86} armv7hl
    --exclude-test-name qt                 # fails on 32-bit architectures only
    --exclude-test-name test_dom_load
%endif
)

CALIBRE_PY3_PORT=1 \
%python3 setup.py test "${TEST_ARGS[@]}"

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/calibre-gui.metainfo.xml

%preun
if [ -L %{_datadir}/calibre/mathjax ]; then
    rm -f %{_datadir}/calibre/mathjax
fi

#posttrans
#ln -s -r %{_datadir}/calibre/mathjax-fedora %{_datadir}/calibre/mathjax

%files
%license LICENSE
%doc Changelog.txt COPYRIGHT README.md
%{_bindir}/calibre
%{_bindir}/calibre-complete
%{_bindir}/calibre-customize
%{_bindir}/calibre-debug
%{_bindir}/calibre-parallel
%{_bindir}/calibre-server
%{_bindir}/calibre-smtp
%{_bindir}/calibredb
%{_bindir}/ebook-convert
%{_bindir}/ebook-device
%{_bindir}/ebook-edit
%{_bindir}/ebook-meta
%{_bindir}/ebook-polish
%{_bindir}/ebook-viewer
%{_bindir}/fetch-ebook-metadata
%{_bindir}/lrf2lrs
%{_bindir}/lrfviewer
%{_bindir}/lrs2lrf
%{_bindir}/markdown-calibre
%{_bindir}/web2disk
%{_libdir}/calibre/
%{_datadir}/calibre/
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/icons/hicolor/*/apps/*
%{python3_sitearch}/init_calibre.py
%{python3_sitearch}/__pycache__/init_calibre.*.py*
%{_datadir}/bash-completion/completions
%{_datadir}/zsh/site-functions/_calibre
%{_datadir}/metainfo/*.metainfo.xml

%changelog
%autochangelog
