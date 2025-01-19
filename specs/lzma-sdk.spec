%global ver_maj 24
%global ver_min 09
%global ver_rel 0

Name:           lzma-sdk
Version:        %{ver_maj}.%{ver_min}
Release:        2%{?dist}
Summary:        SDK for lzma compression

License:        LGPL-2.1-or-later
URL:            https://www.7-zip.org/sdk.html
Source0:        https://downloads.sourceforge.net/project/sevenzip/LZMA%20SDK/lzma%{ver_maj}%{ver_min}.7z
Source1:        lzma-sdk-LICENSE.fedora
Patch0:         lzma-sdk-sharedlib.patch

BuildRequires:  dos2unix
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  p7zip

%description
LZMA SDK provides the documentation, samples, header files, libraries,
and tools you need to develop applications that use LZMA compression.

LZMA is default and general compression method of 7z format
in 7-Zip compression program (www.7-zip.org). LZMA provides high
compression ratio and very fast decompression.

LZMA is an improved version of famous LZ77 compression algorithm. 
It was improved in way of maximum increasing of compression ratio,
keeping high decompression speed and low memory requirements for
decompressing.

%package devel
Summary:        Development libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for %{name}.

%prep
%autosetup -p1 -c -n lzma-sdk
rm -rv bin

for f in .h .c .cpp .dsw .dsp .java .cs .txt makefile; do
   find . -iname "*$f" | xargs chmod -x
done

# correct end-of-line encoding
find . -type f -name '*.txt' | xargs dos2unix -k

for i in \
DOC/7zC.txt \
DOC/7zFormat.txt \
DOC/installer.txt \
DOC/lzma-history.txt \
DOC/lzma-sdk.txt \
DOC/lzma-specification.txt \
DOC/lzma.txt \
DOC/Methods.txt \
CS/7zip/Compress/LzmaAlone/LzmaAlone.sln \
CPP/7zip/Bundles/Alone7z/resource.rc \
CPP/7zip/Bundles/LzmaCon/makefile.gcc \
CPP/Build.mak \
C/Util/Lzma/makefile.gcc \
CPP/7zip/Bundles/Format7zR/resource.rc \
C/Util/7z/makefile.gcc \
CPP/7zip/Archive/Archive.def \
CPP/7zip/Bundles/Format7zExtractR/resource.rc \
C/Util/LzmaLib/resource.rc \
CPP/7zip/Archive/Archive2.def \
CPP/7zip/MyVersionInfo.rc \
DOC/Methods.txt \
C/Util/LzmaLib/LzmaLib.def; do
    iconv -f iso-8859-1 -t utf-8 $i > $i.utf8
    touch -r $i $i.utf8
    mv $i.utf8 $i
done

install -p -m 0644 %{SOURCE1} .

%build
pushd CPP/7zip/Bundles/LzmaCon
make -f makefile.gcc clean all CXXFLAGS_EXTRA="%{build_cxxflags}" CFLAGS_WARN="%{build_cflags}" LDFLAGS_STATIC_2="%{build_cxxflags}"
popd

%install
install -dm0755 %{buildroot}%{_libdir}
install -pm0755 CPP/7zip/Bundles/LzmaCon/liblzmasdk.so.%{ver_maj}.%{ver_min}.%{ver_rel} %{buildroot}%{_libdir}
pushd %{buildroot}%{_libdir}
ln -s liblzmasdk.so.%{ver_maj}.%{ver_min}.%{ver_rel} liblzmasdk.so.%{ver_maj}
ln -s liblzmasdk.so.%{ver_maj}.%{ver_min}.%{ver_rel} liblzmasdk.so
popd
install -dm0755 %{buildroot}/%{_includedir}/lzma
find -iname '*.h' | xargs -I {} install -m0644 -D {} %{buildroot}/%{_includedir}/lzma-sdk/{}
#contains only Windows related headers so for fedora useless
rm -rv %{buildroot}/usr/include/lzma-sdk/CPP/Windows

%files
%license lzma-sdk-LICENSE.fedora
%doc DOC/lzma.txt DOC/lzma-history.txt
%{_libdir}/liblzmasdk.so.%{ver_maj}{,.*}

%files devel
%doc DOC/7z*.txt DOC/Methods.txt DOC/installer.txt DOC/lzma-sdk.txt DOC/lzma-specification.txt
%{_includedir}/lzma-sdk/
%{_libdir}/liblzmasdk.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 04 2024 Dominik Mierzejewski <dominik@greysector.net> - 24.09-1
- Update to 24.09 (resolves rhbz#2329624)

* Thu Sep 05 2024 Zephyr Lykos <fedora@mochaa.ws> - 24.08-1
- new version

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Aug 08 2023 Dominik Mierzejewski <dominik@greysector.net> - 22.01-1
- Rebase to 22.01 (based on Gwyn Ciesla's spec), resolves: rhbz#1546091
- Use SPDX identifier in License: tag
- Modernize spec

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 14 2015 Adam Jackson <ajax@redhat.com> 4.6.5-16
- Pass ldflags to make so hardening works

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.6.5-14
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Jon Ciesla <limburgher@gmail.com> - 4.6.5-11
- Fix format-security FTBFS, BZ 1037188.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Jon Ciesla <limb@jcomserv.net> - 4.6.5-6
- Changed first gcc on make line to g++ to silence rpmlint.

* Tue Aug  9 2011 Tom Callaway <spot@fedoraproject.org> - 4.6.5-5
- rework package to be more normal

* Wed Apr 27 2011 Jon Ciesla <limb@jcomserv.net> - 4.6.5-4
- Additional provides macro.

* Mon Apr 11 2011 Jon Ciesla <limb@jcomserv.net> - 4.6.5-3
- Stripped perl(SevenZip) provides.

* Tue Apr 05 2011 Jon Ciesla <limb@jcomserv.net> - 4.6.5-2
- Licensing clarification.

* Wed May 26 2010 Jon Ciesla <limb@jcomserv.net> - 4.6.5-1
- Initial build
