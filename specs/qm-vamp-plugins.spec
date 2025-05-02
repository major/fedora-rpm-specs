%global blaslib openblas

Name:           qm-vamp-plugins
Version:        1.8.0
Release:        %autorelease
Summary:        Vamp audio feature extraction plugin

License:        GPL-2.0-or-later
# original homepage: http://isophonics.net/QMVampPlugins
URL:            https://code.soundsoftware.ac.uk/projects/qm-vamp-plugins
Source0:        https://code.soundsoftware.ac.uk/attachments/download/2624/qm-vamp-plugins-1.8.0.tar.gz
# build flags cleanup
# (part of it not intended for upstream)
# http://vamp-plugins.org/forum/index.php/topic,270.0.html
Patch0:         qm-vamp-plugins-build.patch
# unbundle qm-dsp
# (not intended for upstream)
Patch1:         qm-vamp-plugins-1.8.0-unbundle.patch

BuildRequires:  make
BuildRequires:  %{blaslib}-devel
BuildRequires:  gcc-c++
BuildRequires:  kiss-fft-static
BuildRequires:  qm-dsp-static >= 1.8.0
BuildRequires:  vamp-plugin-sdk-devel

%description
qm-vamp-plugins are vamp audio feature extraction plugins from the Centre for
Digital Music at Queen Mary, University of London,
http://www.elec.qmul.ac.uk/digitalmusic/.

This plugin set includes note onset detector, beat and barline tracker, tempo
estimator, key estimator, tonal change detector, structural segmenter, timbral
and rhythmic similarity, wavelet scaleogram, adaptive spectrogram, note
transcription, chromagram, constant-Q spectrogram, and MFCC plugins.

For more information see
http://vamp-plugins.org/plugin-doc/qm-vamp-plugins.html.


%prep
%setup -q
# remove atlas binaries
rm -rf build/linux/amd64 build/linux/i686
cp -p build/linux/Makefile.linux32 Makefile
# remove bundled qm-dsp, also with bundled kiss-fft
rm -rf qm-dsp
%patch -P0 -p1 -b .build
%patch -P1 -p1 -b .unbundle


%build
# extra cflags used in upstream
%ifarch %{ix86}
EXTRA_CFLAGS="-msse -mfpmath=sse"
%endif
%ifarch x86_64
EXTRA_CFLAGS="-msse -msse2 -mfpmath=sse"
%endif

CFLAGS="-I%{_includedir}/qm-dsp $EXTRA_CFLAGS %{?optflags}" \
LDFLAGS="%{?__global_ldflags}" \
BLAS_LIBS="-l%{blaslib}" \
make %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_libdir}/vamp
install -p -m 0644 qm-vamp-plugins.cat %{buildroot}%{_libdir}/vamp/
install -p -m 0644 qm-vamp-plugins.n3 %{buildroot}%{_libdir}/vamp/
install -p -m 0755 qm-vamp-plugins.so %{buildroot}%{_libdir}/vamp/


%files
%license COPYING
%doc README.md
%{_libdir}/vamp/qm-vamp-plugins.cat
%{_libdir}/vamp/qm-vamp-plugins.n3
%{_libdir}/vamp/qm-vamp-plugins.so


%changelog
%autochangelog
