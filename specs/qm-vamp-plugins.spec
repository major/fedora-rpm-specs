%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

Name:           qm-vamp-plugins
Version:        1.7.1
Release:        24%{?dist}
Summary:        Vamp audio feature extraction plugin

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
# original homepage: http://isophonics.net/QMVampPlugins
URL:            http://vamp-plugins.org/plugin-doc/qm-vamp-plugins.html
Source0:        https://code.soundsoftware.ac.uk/attachments/download/1604/qm-vamp-plugins-1.7.1.tar.gz
# build flags cleanup
# (part of it not intended for upstream)
# http://vamp-plugins.org/forum/index.php/topic,270.0.html
Patch0:         qm-vamp-plugins-build.patch
# unbundle qm-dsp
# (not intended for upstream)
Patch1:         qm-vamp-plugins-unbundle.patch

BuildRequires: make
BuildRequires:  %{blaslib}-devel
BuildRequires:  gcc-c++
BuildRequires:  kiss-fft-static
BuildRequires:  qm-dsp-static
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
%patch -P0 -p1
%patch -P1 -p1


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
%doc README.txt
%{_libdir}/vamp/qm-vamp-plugins.cat
%{_libdir}/vamp/qm-vamp-plugins.n3
%{_libdir}/vamp/qm-vamp-plugins.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.1-23
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 16 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1.7.1-13
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 František Dvořák <valtri@civ.zcu.cz> - 1.7.1-8
- Add gcc-c++ BR

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 15 2016 František Dvořák <valtri@civ.zcu.cz> - 1.7.1-1
- Update to 1.7.1 (#1261681)
- New homepage
- Unbundled qm-dsp and kiss-fft libraries
- Rebased build patch
- New packaging guidelines (license tag)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Nov 05 2014 František Dvořák <valtri@civ.zcu.cz> - 1.7-2
- Replace qm-dsp-devel for qm-dsp-static BR
- Part of the build flags patch sent upstream

* Sat Feb 1 2014 František Dvořák <valtri@civ.zcu.cz> - 1.7-1
- Initial package
