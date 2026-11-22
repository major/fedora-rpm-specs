%global ver_maj 26
%global ver_min 01
%global ver_rel 0

Name:           lzma-sdk
Version:        %{ver_maj}.%{ver_min}
Release:        %autorelease
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
%autochangelog
