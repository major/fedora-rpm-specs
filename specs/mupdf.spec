Name:		mupdf
%global libname libmupdf
Version:	1.25.4
%global pypiname mupdf
# upstream prerelease versions tags need to be translated to Fedorian
%global upversion %{version}
%global soname 25.4
Release:	%autorelease
Summary:	A lightweight PDF viewer and toolkit
License:	AGPL-3.0-or-later
URL:		http://mupdf.com/
Source0:	http://mupdf.com/downloads/archive/%{name}-%{upversion}-source.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}-gl.desktop
# Fedora specific patches:
# Do not bug me if Artifex relies on local fork
Patch:		0001-Do-not-complain-to-your-friendly-local-distribution-.patch
# Do not generate wrong form of dependencies
Patch:		0001-setup.py-do-not-require-libclang-and-swig.patch
# Do install shared libraries in the python tree
Patch:		0001-setup.py-do-not-bundle-c-and-c-libs-in-wheel.patch
# Avoid core dump of python bindings with gcc15
Patch:		0001-pdf_choice_widget_options2-avoid-core-dump-with-_GLI.patch
# Do not apply CXXFLAGS to swig
Patch:		0001-do-not-use-CXXFLAGS-with-swig.patch
BuildRequires:	gcc gcc-c++ make binutils desktop-file-utils coreutils pkgconfig
BuildRequires:	openjpeg2-devel desktop-file-utils
BuildRequires:	libjpeg-devel freetype-devel libXext-devel curl-devel
BuildRequires:	harfbuzz-devel openssl-devel mesa-libEGL-devel
BuildRequires:	mesa-libGL-devel mesa-libGLU-devel libXi-devel libXrandr-devel
BuildRequires:	gumbo-parser-devel leptonica-devel tesseract-devel
BuildRequires:	freeglut-devel
BuildRequires:	jbig2dec-devel
BuildRequires:	swig python3-clang python3-devel
# We need to build against the Artifex fork of lcms2 so that we are thread safe
# (see bug #1553915). Artifex make sure to rebase against upstream, who refuse
# to integrate Artifex's changes. 
Provides:	bundled(lcms2-devel) = 2.14~rc1^60.gab4547b
# muPDF needs the muJS sources for the build even if we build against the system
# version so bundling them is the safer choice.
Provides:	bundled(mujs-devel) = 1.3.5
# muPDF builds only against in-tree extract which is versioned along with ghostpdl.
Provides:	bundled(extract) = 10.03.0

%description
MuPDF is a lightweight PDF viewer and toolkit written in portable C.
The renderer in MuPDF is tailored for high quality anti-aliased
graphics. MuPDF renders text with metrics and spacing accurate to
within fractions of a pixel for the highest fidelity in reproducing
the look of a printed page on screen.
MuPDF has a small footprint. A binary that includes the standard
Roman fonts is only one megabyte. A build with full CJK support
(including an Asian font) is approximately seven megabytes.
MuPDF has support for all non-interactive PDF 1.7 features, and the
toolkit provides a simple API for accessing the internal structures of
the PDF document. Example code for navigating interactive links and
bookmarks, encrypting PDF files, extracting fonts, images, and
searchable text, and rendering pages to image files is provided.

%package devel
Summary:	C Development files for %{name}
Requires:	%{name}-libs%{_isa} = %{version}-%{release}

%description devel
The mupdf-devel package contains library and header files for developing
C applications that use the mupdf library.

%package libs
Summary:	C Library files for %{name}

%description libs
The mupdf-libs package contains the mupdf C library files.

%package cpp-devel
Summary:	C++ Development files for %{name}
Requires:	%{name}-cpp-libs%{_isa} = %{version}-%{release}

%description cpp-devel
The mupdf-cpp-devel package contains library and header files for developing
C++ applications that use the mupdf library.

%package cpp-libs
Summary:	C++ Library files for %{name}

%description cpp-libs
The mupdf-cpp-libs package contains the mupdf C++ library files.

%package -n python3-%{pypiname}
Summary:	Python bindings for %{name}

%description -n python3-%{pypiname}
The python3-%{pypiname} package contains low level mupdf python bindings.

%prep
%autosetup -p1 -n %{name}-%{upversion}-source
for d in $(ls thirdparty | grep -v -e extract -e lcms2 -e mujs)
do
	rm -rf thirdparty/$d
done

echo > user.make "\
	USE_SYSTEM_LIBS := yes
	USE_SYSTEM_MUJS := no # build needs source anyways
	USE_TESSERACT := yes
	VENV_FLAG :=
	build := release
	shared := yes
	verbose := yes
"

# c++ and python install targets rebuild unconditionally. Avoid multiple rebuilds:
sed -i -e '/^install-shared-c++:/s/ c++//' Makefile
sed -i -e '/^install-shared-python:/s/ python//' Makefile

%generate_buildrequires
%pyproject_buildrequires -R

%build
export XCFLAGS="%{build_cflags} -fPIC -DJBIG_NO_MEMENTO -DTOFU -DTOFU_CJK_EXT"
export XCXXFLAGS="%{build_cxxflags} -fPIC -DJBIG_NO_MEMENTO -DTOFU -DTOFU_CJK_EXT"
make %{?_smp_mflags} shared c++
# Use the same build directory which make uses:
export MUPDF_SETUP_BUILD_DIR=build/shared-release
# Use stable python directories:
export MUPDF_SETUP_VERSION=%{version}
%pyproject_wheel

%install
make DESTDIR=%{buildroot} install install-shared-c install-shared-c++ prefix=%{_prefix} libdir=%{_libdir} pydir=%{python3_sitearch} SO_INSTALL_MODE=755
%pyproject_install
%pyproject_save_files -L %{pypiname}
# handle docs on our own
rm -rf %{buildroot}/%{_docdir}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m644 docs/logo/mupdf-logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/mupdf.svg
install -p -m644 docs/logo/mupdf-logo.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/mupdf-gl.svg
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
%{_libdir}/%{libname}.so

%files libs
%license COPYING
%{_libdir}/%{libname}.so.%{soname}

%files cpp-devel
%{_includedir}/%{name}
%{_libdir}/%{libname}cpp.so

%files cpp-libs
%license COPYING
%{_libdir}/%{libname}cpp.so.%{soname}

%files -n python3-%{pypiname} -f %{pyproject_files}
%license COPYING
%{python3_sitearch}/_%{pypiname}.so

%changelog
%autochangelog
