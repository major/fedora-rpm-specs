# Desired jbig2dec header files and library version
# Apparantly, jbig2dec complains even about newer versions.
# Please update if needed.
%global jbig2dec_version 0.19

Name:           mupdf
Version:        1.20.3
%global upversion 1.20.3
Release:        %autorelease
Summary:        A lightweight PDF viewer and toolkit
License:        AGPLv3+
URL:            http://mupdf.com/
Source0:        http://mupdf.com/downloads/archive/%{name}-%{upversion}-source.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}-gl.desktop
BuildRequires:  gcc gcc-c++ make binutils desktop-file-utils coreutils pkgconfig
BuildRequires:  openjpeg2-devel desktop-file-utils
BuildRequires:  libjpeg-devel freetype-devel libXext-devel curl-devel
BuildRequires:  harfbuzz-devel openssl-devel mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel mesa-libGLU-devel libXi-devel libXrandr-devel
BuildRequires:  gumbo-parser-devel leptonica-devel tesseract-devel
BuildRequires:  jbig2dec-devel = %{jbig2dec_version}
BuildRequires:  jbig2dec-libs = %{jbig2dec_version}
Requires:       jbig2dec-libs = %{jbig2dec_version}
# We need to build against the Artifex fork of lcms2 so that we are thread safe
# (see bug #1553915). Artifex make sure to rebase against upstream, who refuse
# to integrate Artifex's changes. 
Provides:       bundled(lcms2-devel) = 2.12^85.g558b336
# We need to build against the Artifex fork of freeglut so that we are unicode safe.
Provides:       bundled(freeglut-devel) = 3.0.0^11.g13ae6aa
# muPDF needs the muJS sources for the build even if we build against the system
# version so bundling them is the safer choice.
Provides:       bundled(mujs-devel) = 1.2.0
# muPDF builds only against in-tree extract which is versioned along with ghostpdl.
Provides:       bundled(extract) = 9.56.0^4.g10c442d

%description
MuPDF is a lightweight PDF viewer and toolkit written in portable C.
The renderer in MuPDF is tailored for high quality anti-aliased
graphics.  MuPDF renders text with metrics and spacing accurate to
within fractions of a pixel for the highest fidelity in reproducing
the look of a printed page on screen.
MuPDF has a small footprint.  A binary that includes the standard
Roman fonts is only one megabyte.  A build with full CJK support
(including an Asian font) is approximately seven megabytes.
MuPDF has support for all non-interactive PDF 1.7 features, and the
toolkit provides a simple API for accessing the internal structures of
the PDF document.  Example code for navigating interactive links and
bookmarks, encrypting PDF files, extracting fonts, images, and
searchable text, and rendering pages to image files is provided.

%package devel
Summary:        Development files for %{name}
Requires:         %{name} = %{version}-%{release}
Provides:         %{name}-static = %{version}-%{release}

%description devel
The mupdf-devel package contains header files for developing
applications that use mupdf and static libraries

%prep
%setup -q -n %{name}-%{upversion}-source
for d in $(ls thirdparty | grep -v -e extract -e freeglut -e lcms2 -e mujs)
do
  rm -rf thirdparty/$d
done

echo > user.make "\
  USE_SYSTEM_FREETYPE := yes
  USE_SYSTEM_HARFBUZZ := yes
  USE_SYSTEM_JBIG2DEC := yes
  USE_SYSTEM_JPEGXR := yes # not used without HAVE_JPEGXR
  USE_SYSTEM_LCMS2 := no # need lcms2-art fork
  USE_SYSTEM_LIBJPEG := yes
  USE_SYSTEM_MUJS := no # build needs source anyways
  USE_SYSTEM_OPENJPEG := yes
  USE_SYSTEM_ZLIB := yes
  USE_SYSTEM_GLUT := no # need freeglut2-art fork
  USE_SYSTEM_CURL := yes
  USE_SYSTEM_GUMBO := yes
  USE_TESSERACT := yes
  USE_SYSTEM_LEPTONICA := yes
  USE_SYSTEM_TESSERACT := yes
"

%build
export XCFLAGS="%{optflags} -fPIC -DJBIG_NO_MEMENTO -DTOFU -DTOFU_CJK_EXT"

make  %{?_smp_mflags}  build=debug verbose=yes
%install
make DESTDIR=%{buildroot} install prefix=%{_prefix} libdir=%{_libdir} build=debug verbose=yes
## handle docs on our own
rm -rf %{buildroot}/%{_docdir}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m644 docs/logo/mupdf-logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/mupdf.svg
install -p -m644 docs/logo/mupdf-logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/mupdf-gl.svg
## fix strange permissons
chmod 0644 %{buildroot}%{_libdir}/*.a
find %{buildroot}/%{_mandir} -type f -exec chmod 0644 {} \;
find %{buildroot}/%{_includedir} -type f -exec chmod 0644 {} \;
cd %{buildroot}/%{_bindir} && ln -s %{name}-x11 %{name}

%files
%license COPYING
%doc README CHANGES docs/*
%{_bindir}/*
%{_datadir}/applications/mupdf*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/*.1.gz

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}*.a

%changelog
%autochangelog
