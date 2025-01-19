%global mingw_build_ucrt64 1
%{?mingw_package_header}

Name:          mingw-objfw
Version:       1.2.3
Release:       2%{?dist}
Summary:       MinGW port of ObjFW

License:       LGPL-3.0-only
URL:           https://objfw.nil.im
Source0:       https://objfw.nil.im/downloads/objfw-%{version}.tar.gz
Source1:       https://objfw.nil.im/downloads/objfw-%{version}.tar.gz.sig
# gpg2 --export --export-options export-minimal DC43171B6BE93978D09AD8B2C601EE21773E7C8F >gpgkey-objfw.gpg
Source2:       gpgkey-objfw.gpg

BuildArch:     noarch

BuildRequires: clang
BuildRequires: gnupg2
BuildRequires: make

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-binutils
BuildRequires: mingw32-gcc
BuildRequires: mingw32-openssl

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-binutils
BuildRequires: mingw64-gcc
BuildRequires: mingw64-openssl

BuildRequires: ucrt64-filesystem >= 95
BuildRequires: ucrt64-binutils
BuildRequires: ucrt64-gcc
BuildRequires: ucrt64-openssl

%description
ObjFW is a portable, lightweight framework for the Objective-C language. It
enables you to write an application in Objective-C that will run on any
platform supported by ObjFW without having to worry about differences between
operating systems or various frameworks you would otherwise need if you want to
be portable.

It supports all modern Objective-C features when using Clang, but is also
compatible with GCC ≥ 4.6 to allow maximum portability.

ObjFW also comes with its own lightweight and extremely fast Objective-C
runtime, which in real world use cases was found to be significantly faster
than both GNU's and Apple's runtime.

%package -n mingw32-objfw
Summary:       MinGW port of ObjFW
Requires:      mingw32-openssl

%description -n mingw32-objfw
MinGW port of ObjFW for mingw32

%package -n mingw64-objfw
Summary:       MinGW port of ObjFW
Requires:      mingw64-openssl

%description -n mingw64-objfw
MinGW port of ObjFW for mingw64

%package -n ucrt64-objfw
Summary:       MinGW port of ObjFW
Requires:      ucrt64-openssl

%description -n ucrt64-objfw
MinGW port of ObjFW for ucrt64

%{?mingw_debug_package}

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p0 -n objfw-%{version}

mkdir ../mingw32
mv * ../mingw32
mv ../mingw32/COPYING ../mingw32/COPYING.LESSER .
mv ../mingw32 .
cp -Rp mingw32 mingw64
cp -Rp mingw32 ucrt64

%build
pushd mingw32
%mingw32_configure --with-tls=openssl                     \
                   --disable-silent-rules                 \
                   OBJC="clang -target %{mingw32_target}" \
                   OBJCFLAGS="$mingw32_cflags"            \
                   LDFLAGS="$mingw32_ldflags"
%make_build
popd

pushd mingw64
%mingw64_configure --with-tls=openssl                     \
                   --disable-silent-rules                 \
                   OBJC="clang -target %{mingw64_target}" \
                   OBJCFLAGS="$mingw64_cflags"            \
                   LDFLAGS="$mingw64_ldflags"
%make_build
popd

pushd ucrt64
%ucrt64_configure --with-tls=openssl                    \
                  --disable-silent-rules                \
                  OBJC="clang -target %{ucrt64_target}" \
                  OBJCFLAGS="$ucrt64_cflags"            \
                  LDFLAGS="$ucrt64_ldflags"
%make_build
popd

%install
mkdir -p %{buildroot}/%{_bindir}

pushd mingw32
%make_install
for i in objfw-config objfw-compile objfw-embed; do
        mv %{buildroot}/%{mingw32_bindir}/%{mingw32_target}-$i %{buildroot}/%{_bindir}/
done
for i in objfw-new ofarc ofdns ofhash ofhttp; do
        rm %{buildroot}/%{mingw32_bindir}/$i.exe
        rm -fr %{buildroot}/%{mingw32_datadir}/$i
done
rm %{buildroot}/%{mingw32_mandir}/man1/*.1
popd

pushd mingw64
%make_install
for i in objfw-config objfw-compile objfw-embed; do
        mv %{buildroot}/%{mingw64_bindir}/%{mingw64_target}-$i %{buildroot}/%{_bindir}/
done
for i in objfw-new ofarc ofdns ofhash ofhttp; do
        rm %{buildroot}/%{mingw64_bindir}/$i.exe
        rm -fr %{buildroot}/%{mingw64_datadir}/$i
done
rm %{buildroot}/%{mingw64_mandir}/man1/*.1
popd

pushd ucrt64
%make_install
for i in objfw-config objfw-compile objfw-embed; do
        mv %{buildroot}/%{ucrt64_bindir}/%{ucrt64_target}-$i %{buildroot}/%{_bindir}/
done
for i in objfw-new ofarc ofdns ofhash ofhttp; do
        rm %{buildroot}/%{ucrt64_bindir}/$i.exe
        rm -fr %{buildroot}/%{ucrt64_datadir}/$i
done
rm %{buildroot}/%{ucrt64_mandir}/man1/*.1
popd

%files -n mingw32-objfw
%license COPYING
%license COPYING.LESSER
%{_bindir}/%{mingw32_target}-objfw-compile
%{_bindir}/%{mingw32_target}-objfw-config
%{_bindir}/%{mingw32_target}-objfw-embed
%{mingw32_bindir}/objfw1.dll
%{mingw32_bindir}/objfwhid1.dll
%{mingw32_bindir}/objfwrt1.dll
%{mingw32_bindir}/objfwtls1.dll
%{mingw32_includedir}/ObjFW
%{mingw32_includedir}/ObjFWHID
%{mingw32_includedir}/ObjFWRT
%{mingw32_includedir}/ObjFWTLS
%{mingw32_includedir}/ObjFWTest
%{mingw32_libdir}/libobjfw.dll.a
%{mingw32_libdir}/libobjfwhid.dll.a
%{mingw32_libdir}/libobjfwrt.dll.a
%{mingw32_libdir}/libobjfwtest.a
%{mingw32_libdir}/libobjfwtls.dll.a
%{mingw32_libdir}/objfw-config

%files -n mingw64-objfw
%license COPYING
%license COPYING.LESSER
%{_bindir}/%{mingw64_target}-objfw-compile
%{_bindir}/%{mingw64_target}-objfw-config
%{_bindir}/%{mingw64_target}-objfw-embed
%{mingw64_bindir}/objfw1.dll
%{mingw64_bindir}/objfwhid1.dll
%{mingw64_bindir}/objfwrt1.dll
%{mingw64_bindir}/objfwtls1.dll
%{mingw64_includedir}/ObjFW
%{mingw64_includedir}/ObjFWHID
%{mingw64_includedir}/ObjFWRT
%{mingw64_includedir}/ObjFWTLS
%{mingw64_includedir}/ObjFWTest
%{mingw64_libdir}/libobjfw.dll.a
%{mingw64_libdir}/libobjfwhid.dll.a
%{mingw64_libdir}/libobjfwrt.dll.a
%{mingw64_libdir}/libobjfwtest.a
%{mingw64_libdir}/libobjfwtls.dll.a
%{mingw64_libdir}/objfw-config

%files -n ucrt64-objfw
%license COPYING
%license COPYING.LESSER
%{_bindir}/%{ucrt64_target}-objfw-compile
%{_bindir}/%{ucrt64_target}-objfw-config
%{_bindir}/%{ucrt64_target}-objfw-embed
%{ucrt64_bindir}/objfw1.dll
%{ucrt64_bindir}/objfwhid1.dll
%{ucrt64_bindir}/objfwrt1.dll
%{ucrt64_bindir}/objfwtls1.dll
%{ucrt64_includedir}/ObjFW
%{ucrt64_includedir}/ObjFWHID
%{ucrt64_includedir}/ObjFWRT
%{ucrt64_includedir}/ObjFWTLS
%{ucrt64_includedir}/ObjFWTest
%{ucrt64_libdir}/libobjfw.dll.a
%{ucrt64_libdir}/libobjfwhid.dll.a
%{ucrt64_libdir}/libobjfwrt.dll.a
%{ucrt64_libdir}/libobjfwtest.a
%{ucrt64_libdir}/libobjfwtls.dll.a
%{ucrt64_libdir}/objfw-config

%autochangelog
