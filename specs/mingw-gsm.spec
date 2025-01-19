%{?mingw_package_header}

# Breaks build as native ldflags end up in the cross command line
%undefine _auto_set_build_flags

Name:           mingw-gsm
Version:        1.0.16
Release:        20%{?dist}
Summary:        Shared libraries for GSM speech compressor

License:        MIT
URL:            http://www.quut.com/gsm/
Source:         http://www.quut.com/gsm/gsm-%{version}.tar.gz
# patches from gsm package
Patch1:         gsm-warnings.patch
Patch2:         gsm-64bit.patch
# patch for MinGW (build dll, .exe suffix)
# (stdin/out in tools not supported for now)
Patch3:         gsm-mingw.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc

%global srcver 1.0-pl16

%description
Contains runtime shared libraries for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

GSM 06.10 compresses frames of 162 13-bit samples (8 kHz sampling
rate, i.e. a frame rate of 50 Hz) into 260 bits; for compatibility
with typical UNIX applications, our implementation turns frames of 160
16-bit linear samples into 33-byte frames (1650 Bytes/s).
The quality of the algorithm is good enough for reliable speaker
recognition; even music often survives transcoding in recognizable
form (given the bandwidth limitations of 8 kHz sampling rate).

The interfaces offered are a front end modelled after compress(1), and
a library API.  Compression and decompression run faster than realtime
on most SPARCstations.  The implementation has been verified against the
ETSI standard test patterns.


%package -n mingw32-gsm
Summary:        %{summary}

%description -n mingw32-gsm
Contains runtime shared libraries, header files, and development libraries for
libgsm, an implementation of the European GSM 06.10 provisional standard for
full-rate speech transcoding, prI-ETS 300 036, which uses RPE/LTP (residual
pulse excitation/long term prediction) coding at 13 kbit/s.

GSM 06.10 compresses frames of 162 13-bit samples (8 kHz sampling
rate, i.e. a frame rate of 50 Hz) into 260 bits; for compatibility
with typical UNIX applications, our implementation turns frames of 160
16-bit linear samples into 33-byte frames (1650 Bytes/s).
The quality of the algorithm is good enough for reliable speaker
recognition; even music often survives transcoding in recognizable
form (given the bandwidth limitations of 8 kHz sampling rate).

The interfaces offered are a front end modelled after compress(1), and
a library API.  Compression and decompression run faster than realtime
on most SPARCstations.  The implementation has been verified against the
ETSI standard test patterns.

This package is MinGW compiled gsm library for the Win32 target.


%package -n mingw32-gsm-tools
Summary:        GSM speech compressor tools
Requires:       mingw32-gsm = %{version}-%{release}

%description -n mingw32-gsm-tools
Contains command line utilities for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

This package are MinGW compiled gsm tools for the Win32 target.


%package -n mingw64-gsm
Summary:        %{summary}

%description -n mingw64-gsm
Contains runtime shared libraries for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

GSM 06.10 compresses frames of 162 13-bit samples (8 kHz sampling
rate, i.e. a frame rate of 50 Hz) into 260 bits; for compatibility
with typical UNIX applications, our implementation turns frames of 160
16-bit linear samples into 33-byte frames (1650 Bytes/s).
The quality of the algorithm is good enough for reliable speaker
recognition; even music often survives transcoding in recognizable
form (given the bandwidth limitations of 8 kHz sampling rate).

The interfaces offered are a front end modelled after compress(1), and
a library API.  Compression and decompression run faster than realtime
on most SPARCstations.  The implementation has been verified against the
ETSI standard test patterns.

This package is MinGW compiled gsm library for the Win64 target.


%package -n mingw64-gsm-tools
Summary:        Tools for Free Lossless Audio Codec
Requires:       mingw64-gsm = %{version}-%{release}

%description -n mingw64-gsm-tools
Contains command line utilities for libgsm, an implementation of
the European GSM 06.10 provisional standard for full-rate speech
transcoding, prI-ETS 300 036, which uses RPE/LTP (residual pulse
excitation/long term prediction) coding at 13 kbit/s.

This package are MinGW compiled gsm tools for the Win64 target.


%{?mingw_debug_package}


%prep
%setup -qc
pushd gsm-%{srcver}
%patch -P1 -p1 -b .warn
%patch -P2 -p1 -b .64bit
%patch -P3 -p1
popd


%build
cp -a gsm-%{srcver} build_win32
cp -a gsm-%{srcver} build_win64

pushd build_win32
make %{?_smp_mflags} all \
  CC=%mingw32_cc \
  AR=%mingw32_ar \
  RANLIB=%mingw32_ranlib \
  RPM_CFLAGS="%{mingw32_cflags}" \
  RPM_LDFLAGS="%{mingw32_ldflags}"
popd

pushd build_win64
make %{?_smp_mflags} all \
  CC=%mingw64_cc \
  AR=%mingw64_ar \
  RANLIB=%mingw64_ranlib \
  RPM_CFLAGS="%{mingw64_cflags}" \
  RPM_LDFLAGS="%{mingw64_ldflags}"
popd


%install
pushd build_win32
mkdir -p \
  %{buildroot}%{mingw32_bindir} \
  %{buildroot}%{mingw32_mandir}/man1 \
  %{buildroot}%{mingw32_mandir}/man3 \
  %{buildroot}%{mingw32_includedir}/gsm \
  %{buildroot}%{mingw32_libdir}

make install \
  CC=%mingw32_cc \
  AR=%mingw32_ar \
  RANLIB=%mingw32_ranlib \
  INSTALL_ROOT=%{buildroot}%{mingw32_prefix} \
  GSM_INSTALL_BIN=%{buildroot}%{mingw32_bindir} \
  GSM_INSTALL_INC=%{buildroot}%{mingw32_includedir}/gsm \
  GSM_INSTALL_LIB=%{buildroot}%{mingw32_libdir} \
  GSM_INSTALL_MAN=%{buildroot}%{mingw32_mandir}/man3 \
  TOAST_INSTALL_BIN=%{buildroot}%{mingw32_bindir} \
  TOAST_INSTALL_MAN=%{buildroot}%{mingw32_mandir}/man1

# some apps look for this in /usr/include
ln -s gsm/gsm.h %{buildroot}%{mingw32_includedir}
popd

pushd build_win64
mkdir -p \
  %{buildroot}%{mingw64_bindir} \
  %{buildroot}%{mingw64_mandir}/man1 \
  %{buildroot}%{mingw64_mandir}/man3 \
  %{buildroot}%{mingw64_includedir}/gsm \
  %{buildroot}%{mingw64_libdir}

make install \
  CC=%mingw64_cc \
  AR=%mingw64_ar \
  RANLIB=%mingw64_ranlib \
  INSTALL_ROOT=%{buildroot}%{mingw64_prefix} \
  GSM_INSTALL_BIN=%{buildroot}%{mingw64_bindir} \
  GSM_INSTALL_INC=%{buildroot}%{mingw64_includedir}/gsm \
  GSM_INSTALL_LIB=%{buildroot}%{mingw64_libdir} \
  GSM_INSTALL_MAN=%{buildroot}%{mingw64_mandir}/man3 \
  TOAST_INSTALL_BIN=%{buildroot}%{mingw64_bindir} \
  TOAST_INSTALL_MAN=%{buildroot}%{mingw64_mandir}/man1

# some apps look for this in /usr/include
ln -s gsm/gsm.h %{buildroot}%{mingw64_includedir}
popd


%files -n mingw32-gsm
%license gsm-%{srcver}/COPYRIGHT
%doc gsm-%{srcver}/ChangeLog
%doc gsm-%{srcver}/README
%dir %{mingw32_includedir}/gsm
%exclude %{mingw32_mandir}
%exclude %{mingw32_libdir}/libgsm.a
%{mingw32_bindir}/libgsm-1.dll
%{mingw32_libdir}/libgsm.dll.a
%{mingw32_includedir}/gsm.h
%{mingw32_includedir}/gsm/gsm.h

%files -n mingw32-gsm-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-gsm
%license gsm-%{srcver}/COPYRIGHT
%doc gsm-%{srcver}/ChangeLog
%doc gsm-%{srcver}/README
%dir %{mingw64_includedir}/gsm
%exclude %{mingw64_mandir}
%exclude %{mingw64_libdir}/libgsm.a
%{mingw64_bindir}/libgsm-1.dll
%{mingw64_libdir}/libgsm.dll.a
%{mingw64_includedir}/gsm.h
%{mingw64_includedir}/gsm/gsm.h

%files -n mingw64-gsm-tools
%{mingw64_bindir}/*.exe


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.0.16-13
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 František Dvořák <valtri@civ.zcu.cz> - 1.0.16-1
- Update to 1.0.16

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 16 2014 František Dvořák <valtri@civ.zcu.cz> - 1.0.13-1
- Initial package
