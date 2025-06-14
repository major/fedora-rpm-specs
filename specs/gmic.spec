%global gimpplugindir %(%___build_pre; gimptool --gimpplugindir)/plug-ins/gmic_gimp_qt

%global use_system_cimg 1

# As generated by new-snapshot.sh script
%global zart_version 20231127gitd014169
%global gmic_qt_version 20250520gitb55b8ca
%global gmic_community_version 20250608git8bbd3d4a


Summary: GREYC's Magic for Image Computing
Name:    gmic
Version: 3.5.5
%global shortver %(foo=%{version}; echo ${foo//./})
Release: %autorelease
Source0: https://gmic.eu/files/source/%{name}_%{version}.tar.gz
# GIT archive snapshot of https://github.com/c-koi/zart
Source1: zart-%{zart_version}.tar.gz
# GIT archive snapshot of https://github.com/c-koi/gmic-qt
Source2: gmic-qt-%{gmic_qt_version}.tar.gz
# GIT archive snapshot of https://github.com/dtschump/gmic-community
Source3: gmic-community-%{gmic_community_version}.tar.gz

License: ( CECILL-2.1 OR CECILL-C ) AND GPL-3.0-or-later
Url: http://gmic.eu/
%if %{use_system_cimg}
BuildRequires: CImg-devel == 1:%{version}
%endif
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libtiff-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: fftw-devel
%if 0%{?fedora} > 34
BuildRequires: openexr-devel
BuildRequires: imath-devel
%else
BuildRequires: OpenEXR-devel
BuildRequires: ilmbase-devel
%endif
BuildRequires: zlib-devel
BuildRequires: gimp-devel-tools
BuildRequires: hdf5-devel
BuildRequires: opencv-devel
BuildRequires: GraphicsMagick-c++-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: libcurl-devel
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: make
BuildRequires: chrpath

Provides: bundled(zart) = %{zart_version}
Provides: bundled(gmic-qt) = %{gmic_qt_version}
Provides: bundled(gmic-community) = %{gmic_community_version}

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

# The C library binding was mistakenly put in a -static
# package despite being a shared library
Obsoletes:     gmic-static <= 2.1.8
# we no longer have gimp-devel-tools on s390x
ExcludeArch:    s390x

%description
G'MIC is an open and full-featured framework for image processing, providing
several different user interfaces to convert/manipulate/filter/visualize
generic image datasets, from 1d scalar signals to 3d+t sequences of
multi-spectral volumetric images.

%package devel
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Summary: Development files for G'MIC

%package gimp
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: G'MIC plugin for GIMP

%package libs
Summary: G'MIC shared libraries

%description devel
G'MIC is an open and full-featured framework for image processing, providing
several different user interfaces to convert/manipulate/filter/visualize
generic image datasets, from 1d scalar signals to 3d+t sequences of
multi-spectral volumetric images.

Provides files for building applications against the G'MIC API

%description gimp
G'MIC is an open and full-featured framework for image processing, providing
several different user interfaces to convert/manipulate/filter/visualize
generic image datasets, from 1d scalar signals to 3d+t sequences of
multi-spectral volumetric images.

Provides a plugin for using G'MIC from GIMP

%description libs
G'MIC is an open and full-featured framework for image processing, providing
several different user interfaces to convert/manipulate/filter/visualize
generic image datasets, from 1d scalar signals to 3d+t sequences of
multi-spectral volumetric images.

Provides G'MIC shared libraries

%prep
%setup -q -a 1 -a 3

# gmic bundles 'qt', but we don't assume they have the latest
# version, so remove it and provide our own
rm -rf gmic-qt
tar zxvf %{SOURCE2}

cd gmic-qt
# no longer needed
#%%patch 1 -p1
#%%patch 2 -p1
#%%patch 3 -p1

# remove stash-file (thanks Wolfgang Lieff <Wolfgang.Lieff@airborneresearch.org.au>)
rm -f zart/.qmake.stash

%build
# ccache can be used only in local builds, koji and copr don't use it
#export CCACHE_DISABLE=1
cd src

ln -fs ../gmic-community/libcgmic/gmic_libc.cpp .
ln -fs ../gmic-community/libcgmic/gmic_libc.h .
ln -fs ../gmic-community/libcgmic/use_libcgmic.c .

%if %{use_system_cimg}
# We want to build against the system installed CImg package.
# G'MIC provides no way todo this, so we just copy the file
# over what's there already
mv CImg.h CImg.h.bak
cp /usr/include/CImg.h CImg.h
%endif

make OPT_CFLAGS="%{optflags} -g" NOSTRIP=1 PREFIX=%{_prefix} LIB=%{_lib} cli lib libc

cd ../gmic-qt
%{qmake_qt5} CONFIG+=release GMIC_PATH=../src HOST=gimp gmic_qt.pro && %{make_build}
%{qmake_qt5} CONFIG+=release GMIC_PATH=../src HOST=none gmic_qt.pro && %{make_build}

cd ../zart
%{qmake_qt5} CONFIG+=release GMIC_PATH=../src zart.pro && %{make_build}

%install
mv gmic-qt/COPYING COPYING-gmic-qt
mv gmic-community/libcgmic/COPYING COPYING-libcgmic


iconv -f iso8859-1 -t utf-8 COPYING > COPYING.conv && mv -f COPYING.conv COPYING
iconv -f iso8859-1 -t utf-8 COPYING-libcgmic > COPYING-libcgmic.conv && mv -f COPYING-libcgmic.conv COPYING-libcgmic

cd src
# Makefile hardcodes gimptool-2.0 for setting PLUGIN var, so
# override for gimp-3 compat until upstream fixes its rules
make DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} LIB=%{_lib} PLUGIN=%{gimpplugindir} install

desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/gmic_qt.desktop
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/zart.desktop

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
mv $RPM_BUILD_ROOT/%{_datadir}/bash-completion/completions/gmic $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d/gmic
rm -rf $RPM_BUILD_ROOT/%{_datadir}/bash-completion/completions/

# Sourced files shouldn't be executable
chmod -x $RPM_BUILD_ROOT/%{_sysconfdir}/bash_completion.d/gmic

# remove rpaths
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/gmic
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libcgmic.so.%{shortver}
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libgmic.so.%{shortver}

%ldconfig_scriptlets libs

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

# Handle upgrades across the Gimp 3 transition, which required
# moving the plugin into a sub-directory.
#
# cpio can't handle file -> dir replacements, so must manually
# purge the old file path.
#
# Workaround could be removed in Fedora >= 45 timeframe at which
# point we shouldn't see any legacy files around in a normal
# upgrade scenario.
%pretrans -p <lua> gimp
path = "%{gimpplugindir}"
st = posix.stat(path)
if st and st.type == "regular" then
  os.remove(path)
end

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc README
%license COPYING COPYING-gmic-qt COPYING-libcgmic
%{_bindir}/gmic
%{_bindir}/gmic_qt
%{_bindir}/zart
%{_sysconfdir}/bash_completion.d/gmic
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/fr/man1/%{name}.1.gz
%{_datadir}/applications/gmic_qt.desktop
%{_datadir}/applications/zart.desktop
%{_datadir}/icons/hicolor/48x48/apps/gmic_qt.png
%{_datadir}/icons/hicolor/48x48/apps/zart.png
%{_datadir}/icons/hicolor/scalable/apps/gmic_qt.svg
%{_datadir}/icons/hicolor/scalable/apps/zart.svg

%files devel
%{_prefix}/include/gmic.h
%{_prefix}/include/gmic_libc.h
%{_libdir}/libgmic.so
%{_libdir}/libcgmic.so

%files gimp
%dir %{gimpplugindir}
%{gimpplugindir}/gmic_gimp_qt
%dir %{_datadir}/gmic
%{_datadir}/gmic/gmic_cluts.gmz
%{_datadir}/gmic/gmic_denoise_cnn.gmz
%{_datadir}/gmic/gmic_fonts.gmz
%{_datadir}/gmic/gmic_lightleaks.gmz
%{_datadir}/gmic/gmic_scale2x_cnn.gmz

%files libs
%license COPYING COPYING-libcgmic
%{_libdir}/libgmic.so.3*
%{_libdir}/libcgmic.so.3*

%changelog
%autochangelog
