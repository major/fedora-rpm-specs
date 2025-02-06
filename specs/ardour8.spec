# the test scripts seem to be broken
%bcond tests 0

# whether to do a verbose build
%bcond verbose_build 1
%if %{with verbose_build}
%global _verbose -v
%else
%global _verbose %{nil}
%endif

# whether to use system libraries
%bcond system_libs 1

# whether or not to apply 64-bit patches
%if "%_lib" == "lib64"
%bcond apply_64bit_patches 1
%else
%bcond apply_64bit_patches 0
%endif

# Don't generate provides for internal shared objects and plugins
%global internal_libs_re (aaf|alsa_audiobackend|ardour.*|audiographer|canvas|dummy_audiobackend|evoral|gtkmm2ext|jack_audiobackend|midipp|pan[12]in2out|panbalance|panvbap|pbd|ptformat|pulseaudio_backend.so|qmdsp|temporal|timecode|waveview|widgets)
%global __provides_exclude_from ^%{_libdir}/(%{name}|lv2)/.*$
%global __requires_exclude ^lib%{internal_libs_re}\.so.*$

# This package is named ardour8 to allow parallel installation with older versions of Ardour.
Name:       ardour8
Version:    8.11.0

Release:    %autorelease
Summary:    Digital Audio Workstation

License:    GPL-3.0-only
URL:        https://ardour.org
# Not available via direct download. Download via
# https://ardour.org/download.html
Source0:    Ardour-%{version}.tar.bz2
# BSD 2/3-clause, ISC licenses and GPLv3+ license terms used in some code files
Source1:    LICENSING
Source2:    gpl-3.0.txt

# Fedora-specific: Ignore custom gtkrc files, mainly to prevent that Ardour
# hangs when being started with the Breeze theme under KDE Plasma.
# https://bugzilla.redhat.com/show_bug.cgi?id=1837342
Patch0:     ardour8-8.4.0-ignore-custom-gtkrc.patch

# Search VST plugins in lib64 paths on 64-bit platforms. This isn't according
# to the VST standard, but enough packaged plugins use these paths to make it
# worthwhile. Patch number >= 100 applies this only on 64-bit systems.
Patch100:   %{name}-vst-lib64.patch

BuildRequires:  boost-devel >= 1.68
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  fontconfig
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  graphviz
BuildRequires:  itstool >= 2.0.0
BuildRequires:  kernel-headers
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(aubio) >= 0.3.2
BuildRequires:  pkgconfig(cairo) >= 1.12.0
BuildRequires:  pkgconfig(cairomm-1.0) >= 1.8.4
BuildRequires:  pkgconfig(cppunit) >= 1.12.0
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(flac) >= 1.2.1
BuildRequires:  pkgconfig(fluidsynth) >= 2.0.1
BuildRequires:  pkgconfig(giomm-2.4) >= 2.2
BuildRequires:  pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.32.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.2
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.18
BuildRequires:  pkgconfig(gtkmm-2.4) >= 2.18
BuildRequires:  pkgconfig(hidapi-hidraw)
BuildRequires:  pkgconfig(jack) >= 1.9.10
BuildRequires:  pkgconfig(libarchive) >= 3.0.0
BuildRequires:  pkgconfig(libcurl) >= 7.0.0
BuildRequires:  pkgconfig(liblo) >= 0.26
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libwebsockets) >= 2.0.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lilv-0) >= 0.24.2
BuildRequires:  pkgconfig(lrdf) >= 0.4.0
BuildRequires:  pkgconfig(ltc) >= 1.1.1
BuildRequires:  pkgconfig(lv2) >= 1.0.0
BuildRequires:  pkgconfig(ogg) >= 1.1.2
BuildRequires:  pkgconfig(pangoft2) >= 1.36.8
BuildRequires:  pkgconfig(pangomm-1.4) >= 1.4
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(rubberband) >= 3.0.0
BuildRequires:  pkgconfig(samplerate) >= 0.1.7
BuildRequires:  pkgconfig(serd-0) >= 0.14.0
BuildRequires:  pkgconfig(sigc++-2.0) >= 2.0
BuildRequires:  pkgconfig(sndfile) >= 1.0.18
BuildRequires:  pkgconfig(sord-0) >= 0.8.0
BuildRequires:  pkgconfig(soundtouch-1.0)
BuildRequires:  pkgconfig(sratom-0) >= 0.2.0
BuildRequires:  pkgconfig(suil-0) >= 0.6.0
BuildRequires:  pkgconfig(taglib) >= 1.9
BuildRequires:  pkgconfig(vamp-hostsdk) >= 2.1
BuildRequires:  pkgconfig(vamp-sdk) >= 2.1
BuildRequires:  pkgconfig(x11) >= 1.1
BuildRequires:  python3
BuildRequires:  python-unversioned-command
BuildRequires:  kiss-fft-static
BuildRequires:  qm-dsp-static
BuildRequires:  symlinks

Requires:       google-droid-sans-mono-fonts
Requires:       google-noto-sans-fonts

# custom variant of the clearlooks engine used by ardour
# version guessed (conservatively) by copyright of 2007
Provides:       bundled(gtk-theme-engine-clearlooks) = 2.9.0
# stripped down variant of libsmf, the complete version can be found at
# https://sourceforge.net/projects/libsmf/
Provides:       bundled(libsmf) = 1.2
# lua 5.3.5 with custom C++ wrapper
Provides:       bundled(lua) = 5.3.5
# copylib: only a header
# https://github.com/vinniefalco/LuaBridge -- 1.0.2-111-g04b47d7
Provides:       bundled(LuaBridge) = 1.0.2
# libmidi++ and libpbd are internal to ardour, written by the main author
Provides:       bundled(midi++) = 4.1.0
Provides:       bundled(pbd) = 4.1.0

%description
Ardour is a multi-channel digital audio workstation, allowing users to record,
edit, mix and master audio and MIDI projects. It is targeted at audio
engineers, musicians, soundtrack editors and composers.

%prep
%autosetup -S gendiff -N -n Ardour-%{version}
%autopatch -p1 %{!?with_apply_64bit_patches:-M 99}

%if %{with system_libs}
# remove bundled library sources
for i in fluidsynth hidapi libltc qm-dsp; do
    find "libs/$i" \( -name \*.\[ch\] -o -name \*.cc -o -name \*.\[ch\]pp \) -delete
done
%endif

# use versionized name for man page
cp -p ardour.1 %{name}.1

cp %{SOURCE1} %{SOURCE2} .

%build
export LC_ALL=C.UTF-8
%set_build_flags
./waf configure \
%if %{with tests}
    --test \
%endif
    --prefix="%_prefix" \
    --bindir="%_bindir" \
    --configdir="%_sysconfdir" \
    --datadir="%_datadir" \
    --includedir="%_includedir" \
    --libdir="%_libdir" \
    --mandir="%_mandir" \
    --docdir="%_docdir" \
    --docs \
    --noconfirm \
    --no-phone-home \
    --optimize \
%ifarch %ix86 x86_64
    --arch="%optflags -msse -mfpmath=sse -DUSE_XMMINTRIN" \
%else
    --arch="%optflags" \
%endif
%if %{with system_libs}
    --use-external-libs \
%endif
    --cxx11 \
    --freedesktop \
    --no-ytk \
    --with-backends=dummy,alsa,jack,pulseaudio

./waf build %{_verbose} %{?_smp_mflags}
./waf i18n %{_verbose} %{?_smp_mflags}

%install
./waf --destdir=%{buildroot} install %{_verbose}

# ArdourMono.ttf is really Droid Sans Mono
%if ! 0%{?fedora}%{?rhel} || 0%{?fedora} >= 32 || 0%{?rhel} >= 9
ln -snf ../fonts/google-droid-sans-mono-fonts/DroidSansMono.ttf \
    %{buildroot}%{_datadir}/%{name}/ArdourMono.ttf
%else
ln -snf ../fonts/google-droid/DroidSansMono.ttf %{buildroot}%{_datadir}/%{name}/ArdourMono.ttf
%endif

# ArdourSans.ttf is originally Noto Sans Regular
ln -snf ../fonts/google-noto/NotoSans-Regular.ttf %{buildroot}%{_datadir}/%{name}/ArdourSans.ttf

# install man page
install -d -m755 %{buildroot}%{_mandir}/man1
install -p -m644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# tweak and install desktop file
mkdir -p %{buildroot}%{_datadir}/applications/
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
    --set-key=Name --set-value="Ardour %{version}" \
    --set-generic-name="Digital Audio Workstation" \
    --set-key=X-GNOME-FullName \
    --set-value="Ardour v%{version} (Digital Audio Workstation)" \
    --set-comment="Record, mix and master audio" \
    --remove-category=AudioEditing \
    --add-category=X-AudioEditing \
    build/gtk2_ardour/%{name}.desktop

# Delete zero length file (probably needed to keep empty dir in GIT)
rm %{buildroot}%{_datadir}/%{name}/templates/.stub

%find_lang %{name}
%find_lang gtk2_%{name}
%find_lang gtkmm2ext3

# Collect non-locale data files and (all) directories
find %{buildroot}%{_datadir}/%{name} | \
    sed 's|^%{buildroot}||g' | \
    while read f; do
        # *sigh*
        if [ "$f" = "${f/ /}" ]; then
            _f="$f"
        else
            _f="\"${f}\""
        fi

        if [ -d "%{buildroot}${f}" ]; then
            echo "%%dir ${_f}"
        else
            if [ "${f}" = "${f#%{_datadir}/%{name}/locale}" ]; then
                echo "${_f}"
            fi
        fi
    done > %{name}-datafiles.list

# Convert dangling absolute symlinks to resolvable ones
find %{buildroot} -type l | while read src; do
    tgt="$(readlink "$src")"
    if [ "${tgt#/}" != "$tgt" -a "${tgt#%{buildroot}/}" = "$tgt" ]; then
        ln -snf "%{buildroot}${tgt}" "$src"
    fi
done

# Convert absolute to relative symlinks
symlinks -r -c %{buildroot}

%check
%if %{with tests}
WAFTPATH="$PWD/doc/waft"
pushd libs/ardour
sh "$WAFTPATH" --targets=libardour-tests && LV2_PATH= ./run-tests.sh
popd
%endif

# check appdata file
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

rm -f %{buildroot}%{_bindir}/run-tests

%files -f %{name}.lang -f gtk2_%{name}.lang -f gtkmm2ext3.lang -f %{name}-datafiles.list
%license COPYING gpl-3.0.txt LICENSING
%{_bindir}/%{name}
%{_bindir}/%{name}-copy-mixer
%{_bindir}/%{name}-export
%{_bindir}/%{name}-lua
%{_bindir}/%{name}-new_empty_session
%{_bindir}/%{name}-new_session
%config(noreplace) %{_sysconfdir}/%{name}
%{_libdir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
# intentionally unversioned
%{_datadir}/mime/packages/ardour.xml
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
