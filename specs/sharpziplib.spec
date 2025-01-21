%global libname SharpZipLib

# mono is without any packagable debuginfo
%global debug_package %{nil}

%bcond_with brokentests

Name:           sharpziplib
Version:        1.3.3
Release:        8%{?dist}
Summary:        Zip, GZip, Tar and BZip2 library

# - as stated on the homepage, license is aka GNU Classpath exception:
# As a special exception, the copyright holders of this library give you permission
# to link this library with independent modules to produce an executable, regardless
# of the license terms of these independent modules, and to copy and distribute the
# resulting executable under terms of your choice, provided that you also meet, for
# each linked independent module, the terms and conditions of the license of that module. 
# - some files are licensed explicitly with BSD:
# + samples/cs/CreateZipFile/Main.cs
# + samples/cs/FastZip/Main.cs
# + samples/cs/minibzip2/Main.cs
# + samples/cs/minigzip/Main.cs
# + samples/cs/sz/sz.cs
# + samples/cs/tar/Main.cs
# + samples/cs/unzipfile/UnZipFile.cs
# + samples/cs/zipfiletest/ZipFileTest.cs
# + samples/vb/CreateZipFile/MainForm.vb
# + samples/vb/minibzip2/Main.vb
# + samples/vb/viewzipfile/Main.vb
# - samples/HttpCompressionModule is licensed as zlib/libpng (=zlib)
# Automatically converted from old format: GPLv2+ with exceptions and BSD and zlib - review is highly recommended.
License:        LicenseRef-Callaway-GPLv2+-with-exceptions AND LicenseRef-Callaway-BSD AND Zlib
URL:            http://icsharpcode.github.io/%{libname}
Source0:        https://github.com/icsharpcode/%{name}/archive/v%{version}.tar.gz#/%{libname}-%{version}.tar.gz

ExclusiveArch:  %{mono_arches}
BuildRequires:  mono-devel

# fix ownership of mono folders
Requires:       mono-core

%description
SharpZipLib, formerly NZipLib is a Zip, GZip, Tar and BZip2 library
written entirely in C# . It is implemented as an assembly (installable
in the GAC), and thus can easily be incorporated into other projects.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup -qn%{libname}-%{version}

%build

mkdir bin
cd src/ICSharpCode.SharpZipLib/

cat > AssemblyInfo.cs << FINISH
using System.Reflection;

// General Information about an assembly is controlled through the following 
// set of attributes. Change these attribute values to modify the information
// associated with an assembly.
[assembly: AssemblyTitle("SharpZipLib")]
[assembly: AssemblyVersion("%{version}")]
[assembly: AssemblyDescription("C# Zip, GZip, Tar and BZip2 library for .NET")]
[assembly: AssemblyCulture("")]
FINISH

mcs ./Lzw/LzwException.cs ./Lzw/LzwInputStream.cs ./Lzw/LzwConstants.cs ./Core/Exceptions/StreamDecodingException.cs \
    ./Core/Exceptions/SharpZipBaseException.cs ./Core/Exceptions/ValueOutOfRangeException.cs \
    ./Core/Exceptions/StreamUnsupportedException.cs ./Core/Exceptions/UnexpectedEndOfStreamException.cs \
    ./Core/EmptyRefs.cs \
    ./Core/InvalidNameException.cs ./Core/FileSystemScanner.cs ./Core/INameTransform.cs ./Core/PathFilter.cs \
    ./Core/PathUtils.cs ./Core/StreamUtils.cs ./Core/IScanFilter.cs ./Core/NameFilter.cs \
    ./BZip2/BZip2.cs ./BZip2/BZip2Exception.cs ./BZip2/BZip2InputStream.cs ./BZip2/BZip2OutputStream.cs ./BZip2/BZip2Constants.cs \
    ./Zip/ZipHelperStream.cs ./Zip/FastZip.cs ./Zip/IEntryFactory.cs ./Zip/Compression/InflaterHuffmanTree.cs \
    ./Zip/Compression/InflaterDynHeader.cs ./Zip/Compression/Deflater.cs ./Zip/Compression/DeflaterEngine.cs \
    ./Zip/Compression/DeflaterHuffman.cs ./Zip/Compression/DeflaterConstants.cs ./Zip/Compression/PendingBuffer.cs \
    ./Zip/Compression/Streams/InflaterInputStream.cs ./Zip/Compression/Streams/StreamManipulator.cs \
    ./Zip/Compression/Streams/DeflaterOutputStream.cs ./Zip/Compression/Streams/OutputWindow.cs ./Zip/Compression/Inflater.cs \
    ./Zip/Compression/DeflaterPending.cs ./Zip/ZipException.cs ./Zip/ZipEntryFactory.cs ./Zip/ZipFile.cs ./Zip/ZipExtraData.cs \
    ./Zip/ZipEntryExtensions.cs \
    ./Zip/ZipEntry.cs ./Zip/ZipNameTransform.cs ./Zip/ZipInputStream.cs ./Zip/ZipOutputStream.cs ./Zip/ZipConstants.cs \
    ./Zip/ZipStrings.cs ./Zip/WindowsNameTransform.cs \
    ./Zip/ZipEncryptionMethod.cs \
    ./Tar/TarInputStream.cs ./Tar/InvalidHeaderException.cs ./Tar/TarException.cs ./Tar/TarArchive.cs ./Tar/TarBuffer.cs \
    ./Tar/TarHeader.cs ./Tar/TarEntry.cs ./Tar/TarExtendedHeaderReader.cs ./Tar/TarOutputStream.cs \
    ./GZip/GzipInputStream.cs ./GZip/GZip.cs ./GZip/GZipException.cs ./GZip/GZipConstants.cs ./GZip/GzipOutputStream.cs \
    ./Encryption/ZipAESTransform.cs ./Encryption/ZipAESStream.cs ./Encryption/PkzipClassic.cs \
    ./Checksum/BZip2Crc.cs ./Checksum/Adler32.cs ./Checksum/IChecksum.cs ./Checksum/Crc32.cs \
    ./Checksum/CrcUtilities.cs \
    ./AssemblyInfo.cs \
    -define:NETFRAMEWORK -define:NET45 \
    -keyfile:../../assets/ICSharpCode.SharpZipLib.snk \
    -target:library -out:../../bin/ICSharpCode.SharpZipLib.dll
cd -

%install
mkdir -p %{buildroot}/%{_monogacdir} %{buildroot}/%{_libdir}/pkgconfig
gacutil -i bin/*.dll -f -package %{name} -root %{buildroot}/usr/lib

cat > %{buildroot}/%{_libdir}/pkgconfig/%{name}.pc <<FINISH
prefix=/usr
exec_prefix=\${prefix}
libdir=\${exec_prefix}/lib

Name: sharpziplib
Description: C# Zip, GZip, Tar and BZip2 library for .NET
Version: %{version}
Libs: -r:\${libdir}/mono/sharpziplib/ICSharpCode.SharpZipLib.dll
FINISH

%check

%files
%license LICENSE.txt
%doc README.md
# usage of wildcards cause of weird dll name
%{_monogacdir}/*%{libname}
%{_monodir}/%{name}/*%{libname}.dll
%dir %{_monodir}/%{name}

%files devel
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.3-7
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 20 2021 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.3.3-0
- Upgrade to v1.3.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 10 2021 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.3.2-0
- Upgrade to v1.3.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 22 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.3.1-0
- Upgrade to v1.3.1

* Sat Oct 10 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.3.0-0
- Upgrade to v1.3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.2.0-1
- new build so that the provides work (fixed mono scripts)

* Tue Aug 20 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.2.0-0
- Upgrade to v1.2.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.1.0-0
* Upgrade to v1.1.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.86.0.518-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.86.0.518-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.86.0.518-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.86.0.518-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.86.0.518-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.86.0.518-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.86.0.518-3
- mono rebuild for aarch64 support

* Wed Aug 31 2016 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.86.0.518-2
- build with nunit2

* Thu Apr 21 2016 Raphael Groner <projects.rg@smart.ms> - 0.86.0.518-1
- adjust version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.86.0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 17 2015 Raphael Groner <projects.rg@smart.ms> - 0.86.0-0.5
- split devel subpackage

* Fri Nov 13 2015 Raphael Groner <projects.rg@smart.ms> - 0.86.0-0.4
- improve licence breakdown

* Thu Nov 12 2015 Raphael Groner <projects.rg@smart.ms> - 0.86.0-0.3
- revert usage of gone nunit-runner
- fix folders ownership

* Mon Nov 09 2015 Raphael Groner <projects.rg@smart.ms> - 0.86.0-0.2
- improve License tag
- fix directory ownership

* Sun Nov 08 2015 Raphael Groner <projects.rg@smart.ms> - 0.86.0-0.1
- add Suggests to doc subpackage
- adjust Version tag
- shorten Summary text
- use nunit-runner cause now a separate package

* Thu Oct 08 2015 Raphael Groner <projects.rg@smart.ms> - 0.85.5-0.1
- initial
