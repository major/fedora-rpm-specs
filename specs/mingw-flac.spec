%{?mingw_package_header}

Name:           mingw-flac
Version:        1.4.3
Release:        2%{?dist}
Summary:        Encoder/decoder for the Free Lossless Audio Codec

License:        BSD-3-Clause AND GPL-2.0-or-later AND GFDL-1.1-or-later
URL:            https://xiph.org/flac/
Source0:        https://downloads.xiph.org/releases/flac/flac-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-libogg
BuildRequires:  mingw32-win-iconv

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libogg
BuildRequires:  mingw64-win-iconv

BuildRequires:  automake autoconf libtool gettext-devel
BuildRequires:  nasm

%description
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.


%package -n mingw32-flac
Summary:        %{summary}

%description -n mingw32-flac
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package is MinGW compiled flac library for the Win32 target.


%package -n mingw32-flac-tools
Summary:        Tools for Free Lossless Audio Codec
Requires:       mingw32-flac = %{version}-%{release}

%description -n mingw32-flac-tools
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package is MinGW compiled flac tools for the Win32 target.


%package -n mingw64-flac
Summary:        %{summary}

%description -n mingw64-flac
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package is MinGW compiled flac library for the Win64 target.


%package -n mingw64-flac-tools
Summary:        Tools for Free Lossless Audio Codec
Requires:       mingw64-flac = %{version}-%{release}

%description -n mingw64-flac-tools
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package is MinGW compiled flac tools for the Win64 target.


%{?mingw_debug_package}


%prep
%setup -q -n flac-%{version}


%build
# use our libtool to avoid problems with RPATH
./autogen.sh -V

%mingw_configure \
    --disable-silent-rules \
    --disable-thorough-tests

%mingw_make %{?_smp_mflags}


%install
%mingw_make_install

# documentation in native package
rm -rf %{buildroot}%{mingw32_docdir}/flac*
rm -rf %{buildroot}%{mingw64_docdir}/flac*
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

rm %{buildroot}%{mingw32_libdir}/*.la
rm %{buildroot}%{mingw64_libdir}/*.la


%files -n mingw32-flac
%doc AUTHORS README.md CHANGELOG.md
%license COPYING*
%{mingw32_bindir}/libFLAC-12.dll
%{mingw32_bindir}/libFLAC++-10.dll
%{mingw32_includedir}/*
%{mingw32_libdir}/libFLAC.dll.a
%{mingw32_libdir}/libFLAC++.dll.a
%{mingw32_libdir}/pkgconfig/flac.pc
%{mingw32_libdir}/pkgconfig/flac++.pc
%{mingw32_datadir}/aclocal/libFLAC.m4
%{mingw32_datadir}/aclocal/libFLAC++.m4

%files -n mingw32-flac-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-flac
%doc AUTHORS README.md
%license COPYING*
%{mingw64_bindir}/libFLAC-12.dll
%{mingw64_bindir}/libFLAC++-10.dll
%{mingw64_includedir}/*
%{mingw64_libdir}/libFLAC.dll.a
%{mingw64_libdir}/libFLAC++.dll.a
%{mingw64_libdir}/pkgconfig/flac.pc
%{mingw64_libdir}/pkgconfig/flac++.pc
%{mingw64_datadir}/aclocal/libFLAC.m4
%{mingw64_datadir}/aclocal/libFLAC++.m4

%files -n mingw64-flac-tools
%{mingw64_bindir}/*.exe


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jul 30 2024 František Dvořák <valtri@civ.zcu.cz> - 1.4.3-1
- Update to 1.4.3
- Convert license tag to SPDX
- Installation macro

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.3.3-4
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 14 2021 František Dvořák <valtri@civ.zcu.cz> - 1.3.3-1
- Update to 1.3.3
- Fixes CVE-2017-6888 and CVE-2020-0499

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.3.2-8
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 David King <amigadave@amigadave.com> - 1.3.2-1
- Update to 1.3.2 (#1409574)
- Use license macro for COPYING

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 27 2014 David King <amigadave@amigadave.com> - 1.3.1-1
- Update to 1.3.1 (#1168768)
- Fixes CVE-2014-8962 and CVE-2014-9028

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 16 2014 František Dvořák <valtri@civ.zcu.cz> - 1.3.0-2
- Added tools subpackage
- Comment licensing breakdown

* Sat Jan 11 2014 František Dvořák <valtri@civ.zcu.cz> - 1.3.0-1
- Initial package, based on the native flac
