%global octpkg jnifti

Name:           octave-%{octpkg}
Version:        0.5
Release:        16%{?dist}
Summary:        Fast NIfTI-1/2 reader and NIfTI-to-JNIfTI converter for MATLAB/Octave
# Automatically converted from old format: GPLv3+ or ASL 2.0 - review is highly recommended.
License:        GPL-3.0-or-later OR Apache-2.0
URL:            https://github.com/fangq/jnifti
Source0:        https://github.com/fangq/%{octpkg}/archive/v%{version}/%{octpkg}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  octave-devel

Requires:       octave
Requires(post): octave
Requires(postun): octave
Recommends:     octave-jsonlab

%description
JNIfTI Toolbox is a fully functional NIfTI-1/2 reader/writer that supports both
MATLAB and GNU Octave, and is capable of reading/writing both non-compressed
and compressed NIfTI files (.nii, .nii.gz) as well as two-part Analyze7.5/NIfTI
files (.hdr/.img and .hdr.gz/.img.gz).  More importantly, this is a toolbox 
that converts NIfTI data to its JSON-based replacement, JNIfTI (.jnii for 
text-based and .bnii for binary-based), defined by the JNIfTI specification 
(http://github.com/fangq/jnifti). JNIfTI is a much more flexible, human-readable 
and extensible file format compared to the more rigid and opaque NIfTI format, 
making the data much easier to manipulate and share.


%package -n %{octpkg}-demos
Summary:        Example datasets and scripts for the JNIfTI toolbox
BuildArch:      noarch
Requires:       octave octave-%{octpkg}

%description -n %{octpkg}-demos
This package contains the demo script and sample datasets for octave-%{octpkg}. 

%prep
%autosetup -n %{octpkg}-%{version}
rm -rf *.md *.txt
cp lib/matlab/* .
cp lib/octave/* .
rm -rf lib

cp LICENSE_GPLv3.txt COPYING

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangqq@gmail.com>
Maintainer: Qianqian Fang <fangqq@gmail.com>
Description: JNIfTI Toolbox is a fully functional NIfTI-1/2 reader/writer that supports both
 MATLAB and GNU Octave, and is capable of reading/writing both non-compressed
 and compressed NIfTI files (.nii, .nii.gz) as well as two-part Analyze7.5/NIfTI
 files (.hdr/.img and .hdr.gz/.img.gz). 
 More importantly, this is a toolbox that converts NIfTI data to its JSON-based
 replacement, JNIfTI (.jnii for text-based and .bnii for binary-based), defined
 by the JNIfTI specification (http://github.com/fangq/jnifti). JNIfTI is a
 much more flexible, human-readable and extensible file format compared to the
 more rigid and opaque NIfTI format, making the data much easier to manipulate
 and share.
EOF

cat > INDEX << EOF
jnifti >> JNIfTI
JNIfTI
 jnifticreate
 loadjnifti
 loadnifti
 memmapstream
 nifticreate
 niftiread
 niftiinfo
 niftiwrite
 nii2jnii
 niicodemap
 niiformat
 savebnii
 savejnifti
 savejnii
 savenifti
EOF

mkdir -p inst/
mv *.m inst/

%build
%octave_pkg_build

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%license LICENSE_GPLv3.txt LICENSE_Apache-2.0.txt
%doc README.md
%dir %{octpkgdir}
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%files -n %{octpkg}-demos
%license LICENSE_GPLv3.txt LICENSE_Apache-2.0.txt
%doc samples

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 09 2023 Orion Poplawski <orion@nwra.com> - 0.5-10
- Rebuild for octave 8.1.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 0.5-7
- Rebuild for octave 7.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 02 2019 Qianqian Fang <fangqq@gmail.com> - 0.5-1
- Initial package
