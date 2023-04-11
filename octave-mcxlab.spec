%global octpkg mcxlab
%global project mcxcl

Name:           octave-%{octpkg}
Version:        0.9.5
Release:        10%{?dist}
Summary:        MCXLAB - A GPU Monte Carlo 3-D photon transport simulator for MATLAB/Octave
License:        GPLv3+
URL:            http://mcx.space
Source0:        https://github.com/fangq/%{project}/archive/v%{version}/%{project}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  octave-devel gcc-c++  vim-common opencl-headers ocl-icd-devel

Requires:       octave opencl-filesystem
Requires(post): octave
Requires(postun): octave

%description
Monte Carlo eXtreme OpenCL (MCX-CL) is a fast photon transport simulation 
software for 3D heterogeneous turbid media, accelerated by GPUs.
MCXLAB-CL is the native MEX version of MCX-CL for Matlab and GNU Octave. 
It contains the entire MCX-CL code into a MEX function which can be called 
directly inside Matlab or Octave. The input and output files in MCX are 
replaced by convenient in-memory struct variables in MCXLAB-CL, thus, 
making it much easier to use and interact. Matlab/Octave also provides 
convenient plotting and data analysis functions. With MCXLAB-CL, your 
analysis can be streamlined and speed-up without involving disk files.

%prep
%autosetup -n %{project}-%{version}
rm -rf .git_filters deploy setup example
cp utils/*.m mcxlabcl

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangqq@gmail.com>
Maintainer: Qianqian Fang <fangqq@gmail.com>
Description: Monte Carlo eXtreme OpenCL (MCX-CL) is a fast photon transport simulation 
 software for 3D heterogeneous turbid media, accelerated by GPUs.
 MCXLAB-CL is the native MEX version of MCX-CL for Matlab and GNU Octave. 
 It contains the entire MCX-CL code into a MEX function which can be called 
 directly inside Matlab or Octave. The input and output files in MCX are 
 replaced by convenient in-memory struct variables in MCXLAB-CL, thus, 
 making it much easier to use and interact. Matlab/Octave also provides 
 convenient plotting and data analysis functions. With MCXLAB-CL, your 
 analysis can be streamlined and speed-up without involving disk files.
EOF

cp LICENSE.txt COPYING

cat > INDEX << EOF
mcxlabcl >> MCXLABCL
MCXLABCL
 cwdiffusion
 getdistance
 hobbysplines
 image3i
 islicer
 loadmc2
 loadmch
 json2mcx
 mcx2json
 mcxdcsg1
 mcxdetphoton
 mcxdettime
 mcxdettpsf
 mcxdetweight
 mcxfluence2energy
 mcxlabcl
 mcxloadfile
 mcxloadnii
 mcxmeanpath
 mcxmeanscat
 mcxplotphotons
 mcxplotvol
 normalizemcx
 serialcorr
 slice3i
 stacked_bar3
 tddiffusion
EOF

%build
cd src
make oct LIBOPENCLDIR=`octave-config -p OCTLIBDIR`
cd ../
rm README.txt
mv mcxlabcl/README.txt .
rm mcxlabcl/*.txt
mv mcxlabcl/examples .
mv mcxlabcl inst
rm -rf src
rm -rf doc
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
%doc examples README.txt AUTHORS.txt
%dir %{octpkgdir}
%{octpkgdir}/*.m
%{octpkgdir}/*.mex
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%changelog
* Sun Apr 09 2023 Orion Poplawski <orion@nwra.com> - 0.9.5-10
- Rebuild for octave 8.1.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 0.9.5-7
- Rebuild for octave 7.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 02 2019 Qianqian Fang <fangqq@gmail.com> - 0.9.5-1
- Initial package
