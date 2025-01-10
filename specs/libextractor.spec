%global plugindir   %{_libdir}/%{name}
%global gtkver      3

Name:           libextractor
Version:        1.13
Release:        %autorelease
Summary:        Simple library for keyword extraction

# GPL-3.0-or-later: main library
# GPL-2.0-or-later:
# - libextractor-1.10/src/include/platform.h
# - libextractor-1.10/src/intlemu/intlemu.c
# - libextractor-1.10/src/intlemu/libintlemu.h
# - libextractor-1.10/src/main/extractor_metatypes.c
# - libextractor-1.10/src/main/extractor_print.c
# - libextractor-1.10/src/main/getopt.c
# - libextractor-1.10/src/main/getopt.h
# - libextractor-1.10/src/main/getopt1.c
# - libextractor-1.10/src/main/iconv.c
# - libextractor-1.10/src/plugins/html_extractor.c
# GFDL-1.3-or-later:
# - libextractor-1.10/doc/libextractor.info
# - libextractor-1.10/doc/libextractor.texi
# GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain:
# - libextractor-1.10/src/plugins/wav_extractor.c
# LGPL-2.0-or-later:
# - libextractor-1.10/src/include/gettext.h
# LGPL-2.1-or-later:
# - libextractor-1.10/src/include/plibc.h
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND GFDL-1.3-or-later AND (GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain) AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.gnu.org/software/libextractor
Source:         https://ftp.gnu.org/gnu/libextractor/%{name}-%{version}.tar.gz
Source:         https://ftp.gnu.org/gnu/libextractor/%{name}-%{version}.tar.gz.sig
Source:         https://ftp.gnu.org/gnu/gnu-keyring.gpg
Source:         README.fedora
# Patch to fix the exiv2 tests for exiv >= 0.28.0
Patch:          0001-Fix-test_exiv2.c-for-exiv2-0.28.0.patch

BuildRequires:  gcc
## exiv2 config check uses g++
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gnupg2
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  zzuf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
libextractor is a simple library for keyword extraction.  libextractor
does not support all formats but supports a simple plugging mechanism
such that you can quickly add extractors for additional formats, even
without recompiling libextractor.  libextractor typically ships with a
dozen helper-libraries that can be used to obtain keywords from common
file-types.

libextractor is a part of the GNU project (http://www.gnu.org/).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        plugins
Summary:        Plugins for libextractor
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugins-base
Requires:       %{name}-plugins-exiv2
Requires:       %{name}-plugins-ogg
Requires:       %{name}-plugins-ole2
Requires:       %{name}-plugins-thumbnailgtk
Requires:       %{name}-plugins-rpm
Requires:       %{name}-plugins-tiff
Requires:       %{name}-plugins-gif
Requires:       %{name}-plugins-mime
Requires:       %{name}-plugins-flac
Obsoletes:      %{name}-plugins-pdf < %{version}
Obsoletes:      %{name}-plugins-thumbnailqt < %{version}

%description    plugins
libextractor is a simple library for keyword extraction.  libextractor
does not support all formats but supports a simple plugging mechanism
such that you can quickly add extractors for additional formats, even
without recompiling libextractor.

This is a metapackage which requires all supported plugins for
libextractor.

%global pluginpkg(B:R:P:u)                                                          \
%package        plugins-%1                                                          \
Summary:        The '%1' libextractor plugin                                        \
                                                                                    \
Provides:       plugin(%{name}) = %1 %%{-P*}                                        \
%%{-u:Requires(post):   /usr/sbin/update-alternatives}                              \
%%{-u:Requires(preun):  /usr/sbin/update-alternatives}                              \
%%{-B:BuildRequires:    %%{-B*}}                                                    \
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release} %%{-R*}   \
                                                                                    \
%description    plugins-%1                                                          \
libextractor is a simple library for keyword extraction.  libextractor              \
does not support all formats but supports a simple plugging mechanism               \
such that you can quickly add extractors for additional formats, even               \
without recompiling libextractor.                                                   \
                                                                                    \
This package ships the '%1' plugin.                                                 \
                                                                                    \
%files plugins-%1                                                                   \
%{plugindir}/libextractor_%1.so*                                                    \
%nil

%package        plugins-base
Summary:        Base plugins for libextractor
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description    plugins-base
libextractor is a simple library for keyword extraction.  libextractor
does not support all formats but supports a simple plugging mechanism
such that you can quickly add extractors for additional formats, even
without recompiling libextractor.

This package contains all plugins for libextractor which do not
introduce additional dependencies.

%pluginpkg      flac -B flac-devel
%pluginpkg      exiv2 -B exiv2-devel
%pluginpkg      ogg -B libvorbis-devel
%pluginpkg      ole2 -B libgsf-devel,glib2-devel
%pluginpkg      rpm  -B rpm-devel
%pluginpkg      tiff -B libtiff-devel
%pluginpkg      gif  -B giflib-devel
%pluginpkg      mime -B file-devel
%pluginpkg      thumbnailgtk -B gtk%{gtkver}-devel,gtk2-devel,file-devel

## does not work with libjpeg-turbo
#pluginpkg      jpeg -B libjpeg-devel

## is not detected...
## TODO: check whether supported in future versions
#pluginpkg      gstreamer  -B gstreamer-devel,libgsf-gnome-devel,libgsf-devel,gtk

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
cp -aR %{SOURCE3} .
rm -rfv README.debian
sed -i 's!\(-L\(/usr\|\$with_qt\)/lib\|-I/usr/include\) !!g' configure

%build
autoreconf -fi
export ac_cv_lib_mpeg2_mpeg2_init=no
export lt_cv_sys_dlsearch_path='/%{_lib}:%{_prefix}/%{_lib}:%{plugindir}'
%configure --disable-static    \
           --disable-rpath     \
           --disable-xpdf        \
           CPPFLAGS='-DLIBDIR=\"%{_libdir}\"'    \
           LDFLAGS='-Wl,--as-needed'
cat config.log

# build with --as-needed and disable rpath
sed -i                                                                                                  \
    -e 's! -shared ! -Wl,--as-needed\0!g'                                                               \
    -e '\!sys_lib_dlsearch_path_spec=\"/lib /usr/lib !s!\"/lib /usr/lib !\"/%{_lib} /usr/{%_lib} !g'    \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g'                                         \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g'                                 \
    libtool

# not SMP safe
make # %{?_smp_mflags}

%install
%{make_install}
find %{buildroot} -name '*.la' -exec rm -rfv {} ';'
rm -rfv %{buildroot}%{plugindir}/libextractor_thumbnail.so

for i in %{buildroot}%{plugindir}/*.so; do
    readelf -a "$i" | \
    sed '/(NEEDED)/s!.*\[\(.*\)\].*!\1!p;d' | {
        target=base
        fname=${i##%{buildroot}}
        while read lib; do
            lib=${lib%%.so*}
            case $lib in
                (libgcc_s|ld-linux*)            ;;
                (libz|libdl)                ;;
                (libextractor|libextractor_common)    ;;
                (libc|libm|libpthread)    ;;
                (libstdc++) ;;
                (*)
                    target=other
                    echo "$fname -> $lib"
                    ;;
            esac
        done

        case $target in
            (base)    echo "$fname" >> filelists.base;;
        esac
    }
done
rm -rfv %{buildroot}%{_infodir}/dir

mv %{buildroot}%{_bindir}/{,libextractor-}extract
mv %{buildroot}%{_mandir}/man1/{,libextractor-}extract.1

%find_lang libextractor


%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
export LIBEXTRACTOR_PREFIX=%{buildroot}%{_libdir}/libextractor

%ifnarch s390x
# test_elf fails on s390x
make check
%endif

%files -f libextractor.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README* TODO
%{_bindir}/libextractor-extract
%{_libdir}/libextractor.so.3*
%{_libdir}/libextractor_common.so.1*
%{_infodir}/libextractor.info*
%{_mandir}/man1/libextractor-extract.1*
%dir %{plugindir}

%files plugins
%files plugins-base -f filelists.base

%files devel
%{_includedir}/extractor.h
%{_libdir}/libextractor*.so
%{_libdir}/libextractor
%{_mandir}/man3/*
%{_libdir}/pkgconfig/libextractor.pc

%changelog
%autochangelog
