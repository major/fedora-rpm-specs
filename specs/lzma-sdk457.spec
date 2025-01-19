Name:		lzma-sdk457
Version:	4.57
Release:	32%{?dist}
Summary:	SDK for lzma compression
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://sourceforge.net/projects/sevenzip/
Source0:	http://downloads.sourceforge.net/sevenzip/lzma457.tar.bz2
Source1:	http://www.gnu.org/licenses/lgpl-2.1.txt
Patch0:		lzma-sdk-4.5.7-sharedlib.patch
Patch1:		lzma-sdk-4.5.7-format-security-fix.patch

BuildRequires: make
BuildRequires:  gcc-c++
%description
LZMA SDK provides the documentation, samples, header files, libraries,
and tools you need to develop applications that use LZMA compression.

LZMA is default and general compression method of 7z format
in 7-Zip compression program (7-zip.org). LZMA provides high
compression ratio and very fast decompression.

LZMA is an improved version of famous LZ77 compression algorithm. 
It was improved in way of maximum increasing of compression ratio,
keeping high decompression speed and low memory requirements for
decompressing.

%package devel
Summary:	Development libraries and headers for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for %{name}.

%prep
%setup -q -c -n lzma457
%patch -P0 -p1 -b .shared
%patch -P1 -p1 -b .format-security
# Fix FSF mailing address
rm LGPL.txt
cp %{SOURCE1} LGPL.txt
rm lzma.exe

for f in .h .c .cpp .dsw .dsp .java .cs .txt makefile; do
	find . -iname "*$f" | xargs chmod -x
done

# correct end-of-line encoding
sed -i 's/\r//' *.txt 

for i in \
7zFormat.txt \
CS/7zip/Compress/LzmaAlone/LzmaAlone.sln \
7zC.txt \
CS/7zip/Compress/LzmaAlone/LzmaAlone.csproj \
CPP/7zip/Bundles/Alone7z/resource.rc \
history.txt \
lzma.txt \
CPP/7zip/Compress/LZMA_Alone/makefile.gcc \
CPP/Build.mak \
CPP/7zip/Bundles/Format7zR/resource.rc \
C/Archive/7z/makefile.gcc \
CPP/7zip/Archive/Archive.def \
CPP/7zip/Bundles/Format7zExtractR/resource.rc \
CPP/7zip/Archive/Archive2.def \
CPP/7zip/MyVersionInfo.rc \
Methods.txt; do
	iconv -f iso-8859-1 -t utf-8 $i > $i.utf8
	touch -r $i $i.utf8
	mv $i.utf8 $i
done

%build
cd CPP/7zip/Compress/LZMA_Alone
make -f makefile.gcc clean all CXX="g++ %{optflags} -fPIC" CXX_C="gcc %{optflags} -fPIC" LDFLAGS="%{?__global_ldflags}"

%install
mkdir -p %{buildroot}%{_libdir}
install -m0755 CPP/7zip/Compress/LZMA_Alone/liblzmasdk457.so.4.5.7 %{buildroot}%{_libdir}
pushd %{buildroot}%{_libdir}
ln -s liblzmasdk457.so.4.5.7 liblzmasdk457.so.4
ln -s liblzmasdk457.so.4.5.7 liblzmasdk457.so
popd
mkdir -p %{buildroot}/%{_includedir}/lzma457/
find -iname '*.h' | xargs -I {} install -m0644 -D {} %{buildroot}/%{_includedir}/lzma457/{}

%ldconfig_scriptlets

%files
%doc lzma.txt history.txt LGPL.txt
%{_libdir}/liblzmasdk457.so.*

%files devel
%doc 7z*.txt Methods.txt
%{_includedir}/lzma457/
%{_libdir}/liblzmasdk457.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 4.57-31
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.57-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 14 2015 Adam Jackson <ajax@redhat.com> 4.57-11
- Pass ldflags to make so hardening works

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.57-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.57-9
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.57-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.57-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Tom Callaway <spot@fedoraproject.org> - 4.57-6
- fix compile with -Werror=format-security

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.57-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.57-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.57-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Tom Callaway <spot@fedoraproject.org> - 4.57-1
- make 4.57 package for physfs/physfs2
