%{?mingw_package_header}

%global _basename opusfile

Name:          mingw-%{_basename}
Version:       0.12
Release:       15%{?dist}
Summary:       A high-level API for decoding and seeking within .opus files

License:       BSD-3-Clause
URL:           https://www.opus-codec.org/
Source0:       https://downloads.xiph.org/releases/opus/%{_basename}-%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=1675383
Patch0:        opusfile-0.11-disable-cert-store-integration.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2163898
Patch1:        mingw-opusfile-0.12-CVE-2022-47021.patch

BuildArch:     noarch

BuildRequires: make
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-libogg
BuildRequires: mingw32-openssl
BuildRequires: mingw32-opus

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-libogg
BuildRequires: mingw64-openssl
BuildRequires: mingw64-opus

%description
libopusfile provides a high-level API for decoding and seeking
within .opus files. It includes:
* Support for all files with at least one Opus stream (including
multichannel files or Ogg files where Opus is muxed with something else).
* Full support, including seeking, for chained files.
* A simple stereo downmixing API (allowing chained files to be
decoded with a single output format, even if the channel count changes).
* Support for reading from a file, memory buffer, or over HTTP(S)
(including seeking).
* Support for both random access and streaming data sources.

%package -n mingw32-%{_basename}
Summary: A high-level API for decoding and seeking within .opus files

%description -n mingw32-%{_basename}
libopusfile provides a high-level API for decoding and seeking
within .opus files. It includes:
* Support for all files with at least one Opus stream (including
multichannel files or Ogg files where Opus is muxed with something else).
* Full support, including seeking, for chained files.
* A simple stereo downmixing API (allowing chained files to be
decoded with a single output format, even if the channel count changes).
* Support for reading from a file, memory buffer, or over HTTP(S)
(including seeking).
* Support for both random access and streaming data sources.
This is the MinGW version, built for the win32 target.

%package -n mingw64-%{_basename}
Summary: A high-level API for decoding and seeking within .opus files

%description -n mingw64-%{_basename}
libopusfile provides a high-level API for decoding and seeking
within .opus files. It includes:
* Support for all files with at least one Opus stream (including
multichannel files or Ogg files where Opus is muxed with something else).
* Full support, including seeking, for chained files.
* A simple stereo downmixing API (allowing chained files to be
decoded with a single output format, even if the channel count changes).
* Support for reading from a file, memory buffer, or over HTTP(S)
(including seeking).
* Support for both random access and streaming data sources.
This is the MinGW version, built for the win64 target.

%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{_basename}-%{version}


%build
%{mingw_configure} --disable-static

%{mingw_make} %{?_smp_mflags} V=1


%install
# Unset dist_doc_DATA to prevent installing docs. Use files sections instead.
%{mingw_make} DESTDIR=%{buildroot} INSTALL='install -p' dist_doc_DATA= install 

# Remove libtool archives.
find %{buildroot} -name '*.la' -delete


%files -n mingw32-%{_basename}
%doc AUTHORS README.md
%license COPYING
%{mingw32_bindir}/libopusfile-0.dll
%{mingw32_bindir}/libopusurl-0.dll
%{mingw32_libdir}/libopusfile.dll.a
%{mingw32_libdir}/libopusurl.dll.a
%{mingw32_libdir}/pkgconfig/opusfile.pc
%{mingw32_libdir}/pkgconfig/opusurl.pc
%{mingw32_includedir}/opus/opus*

%files -n mingw64-%{_basename}
%doc AUTHORS README.md
%license COPYING
%{mingw64_bindir}/libopusfile-0.dll
%{mingw64_bindir}/libopusurl-0.dll
%{mingw64_libdir}/libopusfile.dll.a
%{mingw64_libdir}/libopusurl.dll.a
%{mingw64_libdir}/pkgconfig/opusfile.pc
%{mingw64_libdir}/pkgconfig/opusurl.pc
%{mingw64_includedir}/opus/opus*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 David King <amigadave@amigadave.com> - 0.12-10
- Fix CVE-2022-47021 (#2163898)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.12-7
- Rebuild with mingw-gcc-12

* Thu Feb 17 2022 Sandro Mani <manisandro@gmail.com> - 0.12-6
- Rebuild (openssl)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 David King <amigadave@amigadave.com> - 0.12-1
- Update to 0.12

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.11-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 David King <amigadave@amigadave.com> - 0.11-1
- Update to 0.11 (#1675383)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 24 2018 Richard W.M. Jones <rjones@redhat.com> - 0.8-6
- Rebuild for new mingw-openssl.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 04 2016 David King <amigadave@amigadave.com> - 0.8-1
- Update to 0.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 David King <amigadave@amigadave.com> - 0.7-1
- Update to 0.7

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 14 2014 David King <amigadave@amigadave.com> 0.6-1
- Update to 0.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 David King <amigadave@amigadave.com> 0.5-1
- Ported Fedora package to MinGW (#1085352)
