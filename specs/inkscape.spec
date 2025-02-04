# Reduce debuginfo verbosity
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')

%bcond_with check
%bcond_with toolchain_clang

%if %{with toolchain_clang}
%global toolchain clang
%endif

%if %{undefined flatpak} && %{undefined rhel}
%if 0%{?fedora} >= 38
%bcond_without graphicsmagick
%else
%bcond_without imagemagick
%endif
%endif

%global inkscape_date 2023-11-16
%global date %(d=%{inkscape_date}; echo ${d//-/})
%global commit 91b66b078370477bd794fe0e1db149c34333dae8
%global shortcommit %(c=%{commit}; echo ${c:0:10})

Name:           inkscape
Version:        1.4
Release:        %autorelease
Summary:        Vector-based drawing program using SVG

License:        GPL-2.0-or-later AND CC-BY-3.0
URL:            https://inkscape.org/
Source0:        https://media.inkscape.org/dl/resources/file/inkscape-%{version}.tar.xz

# The signatures were uploaded by the responsible release manager, and includes release date and commit, not using macros because it's inconsistent.
Source1:        https://media.inkscape.org/media/resources/sigs/inkscape-1.4_2024-10-09_e7c3feb100.tar.xz.sig

# Keyring(s)
Source10:       https://inkscape.org/~MarcJeanmougin/gpg/#/MarcJeanmougin.gpg


# Should we split this package and mark it as a Enhance,
# to clarify the upstream license for this package? -- mochaa, 2023-10-23
# Fedora Color Palette, GIMP format, CC-BY 3.0
Source100:      Fedora-Color-Palette.gpl

# Fix member name - fixes FTBFS https://bugzilla.redhat.com/show_bug.cgi?id=2340648
Patch0:         https://gitlab.com/inkscape/inkscape/-/merge_requests/6755.patch

# Don't drop i686 until at least texlive no longer needs it -GC, 2023-08-10
#%%if 0%%{?fedora} >= 39
#ExcludeArch:    %%{ix86}
#%%endif

Provides: bundled(libcroco) = 0.6.99~gitb9e4b47
Provides: bundled(autotrace) = 0.40.0~git0de6201
Provides: bundled(libdepixelize) = 0~git19b7601
Provides: bundled(libuemf) = 0.2.8
Provides: bundled(adaptagrams) = 0~gitc8e3196

%if %{with toolchain_clang}
BuildRequires:  clang
%else
BuildRequires:  gcc-c++
%endif

BuildRequires:  cmake

BuildRequires:  gnupg2
BuildRequires:  dos2unix
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-rpm-macros

%if %{with check}
BuildRequires:  %{_bindir}/bc
BuildRequires:  %{_bindir}/convert
%endif

BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(gtest)

%global gtk3_version 3.24

BuildRequires:  pkgconfig(gtkmm-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gdkmm-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gdk-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(gspell-1)

BuildRequires:  cmake(double-conversion)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(pangocairo) >= 1.44
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.42
BuildRequires:  pkgconfig(bdw-gc)
BuildRequires:  pkgconfig(lcms2)
%if 0%{?fedora} >= 39
BuildRequires:  pkgconfig(2geom) >= 1.3.0
%endif
BuildRequires:  pkgconfig(poppler) >= 0.20.0
BuildRequires:  pkgconfig(poppler-glib) >= 0.20.0
BuildRequires:  pkgconfig(cairo-svg)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(libwpg-0.3)
BuildRequires:  pkgconfig(libvisio-0.1)
BuildRequires:  pkgconfig(libcdr-0.1)

%if %{with imagemagick}
BuildRequires:  pkgconfig(ImageMagick++) < 7
%endif
%if %{with graphicsmagick}
BuildRequires:  pkgconfig(GraphicsMagick++)
%endif

BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng) >= 1.2

BuildRequires:  pkgconfig(libxslt) >= 1.0.15
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.11

BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(epoxy)

BuildRequires:  boost-devel >= 1.19.0
%if %{with toolchain_clang}
BuildRequires:  libomp-devel
%endif
BuildRequires:  potrace-devel

Requires:       python%{python3_pkgversion}-libs >= 3.7
Requires:       %{py3_dist inkex}
Requires:       python%{python3_pkgversion}-appdirs

# Weak dependencies for the LaTeX plugin
Suggests:       pstoedit
Suggests:       tex(latex)
Suggests:       tex(dvips)
Suggests:       texlive-amsmath
Suggests:       texlive-amsfonts
Suggests:       texlive-standalone

%description
Inkscape is a vector graphics editor, with capabilities similar to
Illustrator, CorelDraw, or Xara X, using the W3C standard Scalable Vector
Graphics (SVG) file format.  It is therefore a very useful tool for web
designers and as an interchange format for desktop publishing.

Inkscape supports many advanced SVG features (markers, clones, alpha
blending, etc.) and great care is taken in designing a streamlined
interface. It is very easy to edit nodes, perform complex path operations,
trace bitmaps and much more.

%package libs
Summary:        Shared libraries for Inkscape

%description libs
This package provides base libraries to share between Inkscape and Inkview.


%package view
Summary:        Viewing program for SVG files

%description view
Viewer for files in W3C standard Scalable Vector Graphics (SVG) file
format.


%package docs
Summary:        Documentation for Inkscape

%description docs
Tutorial and examples for Inkscape, a graphics editor for vector
graphics in W3C standard Scalable Vector Graphics (SVG) file format.


%prep
%{gpgverify} --keyring='%{SOURCE10}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -n inkscape-1.4_2024-10-09_e7c3feb100 -p1
%py3_shebang_fix .

# https://bugs.launchpad.net/inkscape/+bug/314381
# A couple of files have executable bits set,
# despite not being executable
find . -name '*.cpp' -print0 | xargs -0 chmod -x
find . -name '*.h' -print0 | xargs -0 chmod -x

%build
%cmake \
        -DWITH_GRAPHICS_MAGICK=%{?with_graphicsmagick:ON}%{!?with_graphicsmagick:OFF} \
        -DWITH_IMAGE_MAGICK=%{?with_imagemagick:ON}%{!?with_imagemagick:OFF} \
        -DBUILD_TESTING:BOOL=%{?with_check:ON}%{!?with_check:OFF}
%cmake_build


%install
%cmake_install

# Install Fedora Color Pallette
install -pm 644 %{SOURCE100} %{buildroot}%{_datadir}/inkscape/palettes/

%find_lang %{name} --with-man

rm -rf %{buildroot}%{_datadir}/inkscape/doc
rm -f %{buildroot}%{_datadir}/doc/inkscape/copyright

# Use system inkex
rm -rf %{buildroot}%{_datadir}/inkscape/extensions/inkex
ln -s %{python3_sitelib}/inkex %{buildroot}%{_datadir}/inkscape/extensions/inkex

%check
%if %{with check}
%ctest
%endif

# Validate appdata file
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

# Validate desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%pretrans -p <lua>
-- Remove directories that will become symlinks
dirs = {"%{_datadir}/inkscape/extensions/inkex"}
for i, path in ipairs(dirs) do
  st = posix.stat(path)
  if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if not status then
      suffix = 0
      while not status do
        suffix = suffix + 1
        status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
      end
      os.rename(path, path .. ".rpmmoved")
    end
  end
end


%files -f %{name}.lang
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS NEWS.md README.md
%{_bindir}/inkscape
%dir %{_datadir}/inkscape
%{_datadir}/inkscape/attributes
%{_datadir}/inkscape/branding
%{_datadir}/inkscape/extensions
%{_datadir}/inkscape/filters
%{_datadir}/inkscape/icons
%{_datadir}/inkscape/keys
%{_datadir}/inkscape/markers
%{_datadir}/inkscape/palettes
%{_datadir}/inkscape/paint
%{_datadir}/inkscape/screens
%{_datadir}/inkscape/symbols
%{_datadir}/inkscape/templates
%{_datadir}/inkscape/ui
%{_datadir}/metainfo/org.inkscape.Inkscape.appdata.xml
%{_datadir}/applications/org.inkscape.Inkscape.desktop
%{_mandir}/man1/*.1*
%exclude %{_mandir}/man1/inkview.1*
%{_datadir}/inkscape/tutorials
%{_datadir}/inkscape/themes
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/bash-completion/completions/inkscape
%ghost %{_datadir}/inkscape/extensions/inkex.removed


%files libs
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_libdir}/inkscape/libinkscape_base.so*
%dir %{_libdir}/inkscape/
%ghost %{_datadir}/inkscape/extensions/inkex.rpmmoved*

%files view
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS NEWS.md README.md
%{_bindir}/inkview
%{_mandir}/man1/inkview.1*
%{_mandir}/*/man1/inkview.1*


%files docs
%license COPYING
%dir %{_datadir}/inkscape
%{_datadir}/inkscape/examples


%changelog
%autochangelog
