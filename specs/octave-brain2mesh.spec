%global octpkg brain2mesh

Name:           octave-%{octpkg}
Version:        0.5
Release:        16%{?dist}
Summary:        A fully automated high-quality brain tetrahedral mesh generation toolbox
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://mcx.space/brain2mesh
Source0:        https://github.com/fangq/%{octpkg}/archive/v%{version}/%{octpkg}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  octave-devel

Requires:       octave octave-image octave-iso2mesh octave-jsonlab octave-zmat octave-jnifti
Requires(post): octave
Requires(postun): octave

%description
The Brain2Mesh toolbox provides a streamlined matlab function to convert
a segmented brain volumes and surfaces into a high-quality multi-layered
tetrahedral brain/full head mesh. Typical inputs include segmentation
outputs from SPM, FreeSurfer, FSL etc. This tool does not handle the
segmentation of MRI scans, but examples of how commonly encountered
segmented datasets can be used to create meshes can be found in the 
package named %{octpkg}-demos.


%package -n %{octpkg}-demos
Summary:        Example datasets and scripts for the brain2mesh toolbox
BuildArch:      noarch
Requires:       octave octave-%{octpkg}

%description -n %{octpkg}-demos
This package contains the demo script and sample datasets for octave-%{octpkg}. 

%prep
%autosetup -n %{octpkg}-%{version}

cp LICENSE.txt COPYING

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangqq@gmail.com> and Anh Phong Tran <tran.anh@husky.neu.edu>
Maintainer: Qianqian Fang <fangqq@gmail.com>
Description:  The Brain2Mesh toolbox provides a streamlined matlab function to convert
 a segmented brain volumes and surfaces into a high-quality multi-layered
 tetrahedral brain/full head mesh. Typical inputs include segmentation
 outputs from SPM, FreeSurfer, FSL etc. This tool does not handle the
 segmentation of MRI scans, but examples of how commonly encountered
 segmented datasets can be used to create meshes can be found in the 
 package named %{octpkg}-demos.
URL: %{url}
Depends: image, iso2mesh, jsonlab, jnifti, zmat
EOF

cat > INDEX << EOF
brain2mesh >> Brain2Mesh
 brain2mesh
 intriangulation
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
%license LICENSE.txt
%doc README.md
%dir %{octpkgdir}
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%files -n %{octpkg}-demos
%license LICENSE.txt
%doc examples

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5-15
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

* Fri Oct 11 2019 Qianqian Fang <fangqq@gmail.com> - 0.5-1
- Initial package
