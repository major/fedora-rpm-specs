%global octpkg zmat

Name:           octave-%{octpkg}
Version:        0.9.8
Release:        16%{?dist}
Summary:        A portable data compression/decompression toolbox for MATLAB/Octave
# Automatically converted from old format: GPLv3+ or BSD - review is highly recommended.
License:        GPL-3.0-or-later OR LicenseRef-Callaway-BSD
URL:            https://github.com/fangq/zmat
Source0:        https://github.com/fangq/zmat/archive/v%{version}/%{octpkg}-%{version}.tar.gz
Patch0:         zmat-0.9.8-Octave7.patch
BuildRequires:  make
BuildRequires:  octave-devel zlib gcc-c++

Requires:       octave zlib
Requires(post): octave
Requires(postun): octave

%description
ZMat is a portable mex function to enable zlib/gzip/lzma/lzip/lz4/lz4hc 
based data compression/decompression and base64 encoding/decoding support 
in MATLAB and GNU Octave. It is fast and compact, can process a large 
array within a fraction of a second. Among the 6 supported compression 
methods, lz4 is the fastest for compression/decompression; lzma is the 
slowest but has the highest compression ratio; zlib/gzip have the best 
balance between speed and compression time.

%prep
%autosetup -n %{octpkg}-%{version} -S patch -p1

cp LICENSE.txt COPYING

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangqq@gmail.com>
Maintainer: Qianqian Fang <fangqq@gmail.com>
Description: ZMat is a portable mex function to enable zlib/gzip/lzma/lzip/lz4/lz4hc 
 based data compression/decompression and base64 encoding/decoding support 
 in MATLAB and GNU Octave. It is fast and compact, can process a large 
 array within a fraction of a second. Among the 6 supported compression 
 methods, lz4 is the fastest for compression/decompression; lzma is the 
 slowest but has the highest compression ratio; zlib/gzip have the best 
 balance between speed and compression time.

Categories: Zip
EOF

cat > INDEX << EOF
zmat >> ZMat
ZMat
 zmat
 zipmat
EOF


mkdir -p inst/
mv *.m inst/

%build
cd src
make clean
make oct CFLAGS="%{optflags}"
cd ../
mv *.mex inst/
rm -rf src
%octave_pkg_build

%if 0%{?fedora} <=30
   %global octave_tar_suffix any-none
%endif

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%license LICENSE.txt
%doc example
%doc README.rst
%doc AUTHORS.txt
%doc ChangeLog.txt
%dir %{octpkgdir}
%{octpkgdir}/*.m
%{octpkgdir}/*.mex
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.8-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 09 2023 Orion Poplawski <orion@nwra.com> - 0.9.8-10
- Rebuild for octave 8.1.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 Qianqian Fang <fangqq@gmail.com> - 0.9.8-8
- Avoid Octave 7 mkoctfile infinite loop, fix #2046780

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 0.9.8-6
- Rebuild for octave 7.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Qianqian Fang <fangqq@gmail.com> - 0.9.8-1
- Update to new upstream release v0.9.8

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Qianqian Fang <fangqq@gmail.com> - 0.9-1
- Initial package
