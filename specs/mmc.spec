%global octpkg mmclab

Name:           mmc
Version:        1.7.9
Release:        14%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://mcx.space/mmc
Source0:        https://github.com/fangq/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Summary:        A GPU-based mesh-based Monte Carlo (MMC) photon simulator
BuildRequires: make
BuildRequires:  octave-devel gcc-c++ vim-common opencl-headers ocl-icd-devel
Requires:       octave opencl-filesystem octave-iso2mesh
Requires(post): octave
Requires(postun): octave
Provides:       bundled(ssemath) = 0.0
Provides:       bundled(cjson) = 0.0

%description
Mesh-based Monte Carlo (MMC) is a 3D Monte Carlo (MC) simulation software
for photon transport in complex turbid media. MMC combines the strengths
of the MC-based technique and the finite-element (FE) method: on the
one hand, it can handle general media, including low-scattering ones,
as in the MC method; on the other hand, it can use an FE-like tetrahedral
mesh to represent curved boundaries and complex structures, making it
even more accurate, flexible, and memory efficient. MMC uses the
state-of-the-art ray-tracing techniques to simulate photon propagation in
a mesh space. It has been extensively optimized for excellent computational
efficiency and portability. MMC currently supports both multi-threaded
parallel computing and GPU to maximize performance on modern processors.

%package -n octave-%{octpkg}
Summary:        A GPU mesh-based Monte Carlo photon simulator for MATLAB/Octave
Requires:       octave opencl-filesystem octave-iso2mesh
Recommends:     %{octpkg}-demos

%description -n octave-%{octpkg}
MMCLAB is the native MEX version of MMC - Mesh-based Monte Carlo - for
MATLAB and GNU Octave. By converting the input and output files into
convenient in-memory variables, MMCLAB is very intuitive to use and
straightforward to be integrated with mesh generation and post-simulation
analyses. Because MMCLAB contains the same computational codes for
OpenCL-based photon simulation as in a MMC binary, running MMCLAB
inside MATLAB is expected to give similar speed as running a standalone
MMC binary using either a CPU or a GPU.

%package -n %{octpkg}-demos
Summary:        Example datasets and scripts for MMCLAB toolbox
BuildArch:      noarch
Requires:       octave octave-%{octpkg} octave-iso2mesh

%description -n %{octpkg}-demos
This package contains the demo script and sample datasets for octave-%{octpkg}.


%package demos
Summary:        Example datasets and scripts for Mesh-based Monte Carlo - MMC
BuildArch:      noarch
Requires:       octave octave-iso2mesh

%description demos
This package contains the demo script and sample datasets for MMC. 


%prep
%autosetup -n %{name}-%{version}
rm -rf .git_filters .gitattributes deploy webmmc
cp matlab/*.m mmclab

cp LICENSE.txt COPYING

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangqq@gmail.com>
Maintainer: Qianqian Fang <fangqq@gmail.com>
Description: Mesh-based Monte Carlo (MMC) is a 3D Monte Carlo (MC) simulation software
 for photon transport in complex turbid media. MMC combines the strengths
 of the MC-based technique and the finite-element (FE) method: on the
 one hand, it can handle general media, including low-scattering ones,
 as in the MC method; on the other hand, it can use an FE-like tetrahedral
 mesh to represent curved boundaries and complex structures, making it
 even more accurate, flexible, and memory efficient. MMC uses the
 state-of-the-art ray-tracing techniques to simulate photon propagation in 
 a mesh space. It has been extensively optimized for excellent computational
 efficiency and portability. MMC currently supports both multi-threaded
 parallel computing and GPU to maximize performance on a multi-core processor.
URL: %{url}
Depends: iso2mesh
EOF

cat > INDEX << EOF
mmclab >> MMCLAB
MMCLAB
 generate_g1
 genT5mesh
 genT6mesh
 loadmch
 load_mc_prop
 mmc2json
 mmcadddet
 mmcaddsrc
 mmcdettime
 mmcdettpsf
 mmcdetweight
 mmcjacobian
 mmcjmua
 mmcjmus
 mmclab
 mmcmeanpath
 mmcmeanscat
 mmcraytrace
 mmcsrcdomain
 readmmcelem
 readmmcface
 readmmcmesh
 readmmcnode
 savemmcmesh
SphDiffusion Toolbox
 besselhprime
 besseljprime
 besselyprime
 cart2sphorigin
 spbesselh
 spbesselhprime
 spbesselj
 spbesseljprime
 spbessely
 spbesselyprime
 spharmonic
 sphdiffAcoeff
 sphdiffBcoeff
 sphdiffCcoeff
 sphdiffexterior
 sphdiffincident
 sphdiffinterior
 sphdiffscatter
 sphdiffusioninfinite
 sphdiffusion
 sphdiffusionscatteronly
 sphdiffusionsemi
 sphdiffusionslab
EOF

%build
%set_build_flags
rm -rf src/SFMT
# Build octave bits
%ifarch %ix86 x86_64
    %make_build -C src oct LFLAGS="-L`octave-config -p OCTLIBDIR` -lOpenCL" USERCCFLAGS="%{optflags} -DUSE_OS_TIMER -DUSE_OPENCL"
%else
    %make_build -C src octomp LFLAGS="-L`octave-config -p OCTLIBDIR` -lOpenCL" USERCCFLAGS="%{optflags} -DUSE_OS_TIMER -DUSE_OPENCL"
%endif

rm %{octpkg}/*.txt
mv %{octpkg}/example .
mv %{octpkg} inst
mv src/Makefile .
%octave_pkg_build

# Build non octave bits
mv Makefile src
pushd src
%make_build clean

%ifarch %ix86 x86_64
  %make_build USERCCFLAGS="%{optflags} -DUSE_OS_TIMER -DUSE_OPENCL"
%else
  %make_build omp USERCCFLAGS="%{optflags} -DUSE_OS_TIMER -DUSE_OPENCL"
%endif

mkdir -p ../bin
cp bin/%{name} ../bin/%{name}
popd

%if 0%{?fedora} <=30
   %global octave_tar_suffix any-none
%endif

%install
%octave_pkg_install

install -m 0755 -pd %{buildroot}%{_bindir}
install -m 0755 -pt %{buildroot}%{_bindir} bin/%{name}

# Move mex to arch specific directory
mkdir -p -m 0755 %{buildroot}/%{octpkglibdir}/%{octave_host}-%{octave_api}
mv %{buildroot}/%{octpkgdir}/*.mex %{buildroot}/%{octpkglibdir}/%{octave_host}-%{octave_api} -v

%post -n octave-%{octpkg}
%octave_cmd pkg rebuild

%preun -n octave-%{octpkg}
%octave_pkg_preun

%postun -n octave-%{octpkg}
%octave_cmd pkg rebuild

%files
%license LICENSE.txt
%doc README.txt AUTHORS.txt
%{_bindir}/%{name}

%files demos
%license LICENSE.txt
%doc README.txt AUTHORS.txt
%doc examples

%files -n octave-%{octpkg}
%license LICENSE.txt
%doc README.txt AUTHORS.txt
%doc %{octpkgdir}/doc-cache
%{octpkglibdir}
%{octpkgdir}
%{octpkgdir}/packinfo

%files -n %{octpkg}-demos
%license LICENSE.txt
%doc README.txt AUTHORS.txt
%doc example


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.9-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Oct 04 2019 Qianqian Fang <fangqq@gmail.com> - 1.7.9-1
- Initial package
