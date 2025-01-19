# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%if 0%{?fedora} >= 38
# openmpi segmentation fault on i686 bug #2142304
ExcludeArch: %{ix86} s390x
%else
# ga/nwchem most likely does not support s390x
# https://github.com/edoapra/fedpkg/issues/10
ExcludeArch: s390x
%endif

%if 0%{?el6} || 0%{?el7}
need libxc version > 3
%quit
%endif

%global upstream_name nwchem

%{?!major_version: %global major_version 7.2.3}
%{?!git_hash: %global git_hash 8701f25ad941a4237cdd5a843b6d569f5b3fff1d}
%{?!ga_version: %global ga_version 5.8.2-1}


%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

%ifarch %ix86 %arm
%global make64_to_32 0
%global NWCHEM_TARGET LINUX
%else
%global make64_to_32 1
# arch is x86_64
%global NWCHEM_TARGET LINUX64
%endif
# build with python support
%{?!PYTHON_SUPPORT: %global PYTHON_SUPPORT 1}

# static (a) or shared (so) libpython.*
%global BLASOPT -L%{_libdir} -l%{blaslib}
# from https://nwchemgit.github.io/ forum:
# BLAS_SIZE=4 is needed when the Blas library you are using have
# 32-bit integer arguments (de facto default)
%global BLAS_SIZE 4
%global LAPACK_LIB -L%{_libdir} -l%{blaslib}

Name:			nwchem
Version:		%{major_version}
Release:		3%{?dist}
Summary:		Delivering High-Performance Computational Chemistry to Science

# Automatically converted from old format: ECL 2.0 - review is highly recommended.
License:		ECL-2.0
URL:			https://nwchemgit.github.io/
# Nwchem changes naming convention of tarballs very often!
Source0:		https://github.com/nwchemgit/nwchem/archive/%{git_hash}.tar.gz
# Patch for implicit declaration of function ‘Py_SetProgramName' in Python 3.13 https://github.com/nwchemgit/nwchem/issues/950

# https://fedoraproject.org/wiki/Packaging:Guidelines#Compiler_flags
# One needs to patch gfortran/gcc makefiles in order to use
# $RPM_OPT_FLAGS (= %%optflags), but an attempt resulted in broken
# executables http://koji.fedoraproject.org/koji/taskinfo?taskID=6429073
# even after removing the -Werror=format-security flag
# https://bugzilla.redhat.com/show_bug.cgi?id=1037075


%global PKG_TOP ${RPM_BUILD_DIR}/%{name}-%{git_hash}

BuildRequires: make
BuildRequires:		patch
BuildRequires:		time

%if 0%{?fedora} >= 29 || 0%{?rhel} >= 9
BuildRequires:		python3-devel
%else
BuildRequires:		python2-devel
%endif

BuildRequires:		gcc-gfortran

BuildRequires:		%{blaslib}-devel
# https://pagure.io/releng/issue/12359
BuildRequires:		environment-modules
# Use openblas-serial instead of openblas-openmp, but it's unavailable on centos stream
# due to https://bugzilla.redhat.com/show_bug.cgi?id=2182460, so use a workaround of export OMP_NUM_THREADS=1
# See https://github.com/edoapra/fedpkg/issues/10#issuecomment-731855285
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
BuildRequires:		flexiblas-openblas-openmp
Requires:		flexiblas-openblas-openmp
%endif
BuildRequires:		libxc-devel

%if 0%{?rhel} == 6
BuildRequires:		net-tools
%else
BuildRequires:		hostname
%endif

%if 0%{?fedora}
BuildRequires:		perl-interpreter
%else
BuildRequires:		perl
%endif
%if 0%{?fedora} >= 33
BuildRequires:		perl-File-Basename
%endif

BuildRequires:		openssh-clients

Requires:		openssh-clients
Requires:		%{name}-common = %{version}-%{release}


%global nwchem_desc_base \
NWChem aims to provide its users with computational chemistry tools that are\
scalable both in their ability to treat large scientific computational\
chemistry problems efficiently, and in their use of available parallel\
computing resources from high-performance parallel supercomputers to\
conventional workstation clusters.

%global nwchem_desc_cite \
Please cite the following reference when\
publishing results obtained with NWChem:\
M. Valiev, E.J. Bylaska, N. Govind, K. Kowalski, T.P. Straatsma,\
H.J.J. van Dam, D. Wang, J. Nieplocha, E. Apra, T.L. Windus, W.A. de Jong,\
"NWChem: a comprehensive and scalable open-source solution for\
large scale molecular simulations" Comput. Phys. Commun. 181, 1477 (2010)


%description
%{nwchem_desc_base}
%{nwchem_desc_cite}

There is currently no serial version built.


%package openmpi
Summary:		%{upstream_name} - openmpi version
BuildRequires:		openmpi-devel
BuildRequires:		ga-openmpi-devel >= %{ga_version}
Requires:		%{name} = %{version}-%{release}
Requires:		openmpi
%if 0%{?el7} 
Requires:		ga-openmpi
%endif

%description openmpi
%{nwchem_desc_base}
%{nwchem_desc_cite}

This package contains the openmpi version.


%package mpich
Summary:		%{upstream_name} - mpich version
BuildRequires:		mpich-devel
BuildRequires:		ga-mpich-devel >= %{ga_version}
Requires:		%{name} = %{version}-%{release}
Requires:		mpich
%if 0%{?el7} 
Requires:		ga-mpich
%endif

%description mpich
%{nwchem_desc_base}
%{nwchem_desc_cite}

This package contains the mpich version.


%package common
Summary:		%{upstream_name} - common files
BuildArch:		noarch

%description common
%{nwchem_desc_base}
%{nwchem_desc_cite}

This package contains the data files.

%prep
%setup -q -n %{name}-%{git_hash}

# See bundling discussion at https://github.com/nwchemgit/nwchem/discussions/905
# remove the whole src/libext
mv src/libext/GNUmakefile /tmp/GNUmakefile.libext
rm -rf src/libext/*
mv /tmp/GNUmakefile.libext src/libext/GNUmakefile

# remove bundling of BLAS/LAPACK
mv src/blas/GNUmakefile /tmp/GNUmakefile.blas
mv src/lapack/GNUmakefile /tmp/GNUmakefile.lapack
rm -rf src/blas/* src/lapack/*
mv /tmp/GNUmakefile.blas src/blas/GNUmakefile
mv /tmp/GNUmakefile.lapack src/lapack/GNUmakefile
sed -e 's|CORE_SUBDIRS_EXTRA +=.*|CORE_SUBDIRS_EXTRA +=|g' -i src/config/makefile.h
sed -e 's|CORE_SUBDIRS_EXTRA =.*|CORE_SUBDIRS_EXTRA =|g' -i src/config/makefile.h
sed -e 's|-llapack||g' -i src/config/makefile.h
sed -e 's|-lblas||g' -i src/config/makefile.h
sed -e 's|-lnwclapack||g' -i src/config/makefile.h
sed -e 's|-lnwcblas||g' -i src/config/makefile.h

# remove references to tcsh
rm -f QA/doqm.bat
rm -f src/config/sngl_to_dbl
rm -f src/config/*depend
rm -f src/config/*blas
rm -f src/config/dbl_to_sngl
rm -rf src/tools/ga-*

# remove compiler native arch optimizations, see
# https://bugzilla.redhat.com/show_bug.cgi?id=1347788
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=767481
sed -i 's|-march=native||' src/config/makefile.h
sed -i 's|-mtune=native|-mtune=generic|' src/config/makefile.h
sed -i 's|-mfpmath=sse||' src/config/makefile.h
sed -i 's|-msse3||' src/config/makefile.h

# remove slow tests
# https://github.com/nwchemgit/nwchem/issues/895
sed -i '/libxc_waterdimer_bmk/d' QA/dolibxctests.mpi

%build
# base settings
echo "# see https://nwchemgit.github.io/Compiling-NWChem.html" > settings.sh
echo export NWCHEM_TARGET=%{NWCHEM_TARGET} >> settings.sh
#
echo export CC=gcc >> settings.sh
echo export FC=gfortran >> settings.sh
# https://nwchemgit.github.io/Special_AWCforum/st/id1590/Nwchem-dev.revision26704-src.201....html
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 9
echo export USE_ARUR=TRUE >> settings.sh
%endif
%if 0%{?rhel} >= 7
echo export USE_ARUR=TRUE >> settings.sh
%endif
#
echo export USE_NOFSCHECK=TRUE >> settings.sh
# https://github.com/nwchemgit/nwchem/issues/272
echo export USE_NOIO=TRUE >> settings.sh
echo export NWCHEM_FSCHECK=N >> settings.sh
echo export LARGE_FILES=TRUE >> settings.sh
echo export MRCC_THEORY=Y >> settings.sh
echo export EACCSD=Y >> settings.sh
echo export IPCCSD=Y >> settings.sh
echo export CCSDTQ=Y >> settings.sh
echo export CCSDTLR=Y >> settings.sh
echo export NWCHEM_LONG_PATHS=Y >> settings.sh
# https://github.com/nwchemgit/nwchem/issues/723
echo unset USE_LIBXC >> settings.sh
echo export LIBXC_LIB="'%{_libdir}'" >> settings.sh
echo export LIBXC_INCLUDE="'%{_includedir}'" >> settings.sh
echo export LIBXC_MODDIR="'%{_libdir}/gfortran/modules'" >> settings.sh
echo export NO_NWPWXC_VDW3A=1 >> settings.sh
#
echo export HAS_BLAS=yes >> settings.sh
echo export BLASOPT="'%{BLASOPT}'" >> settings.sh
echo export BLAS_SIZE="'%{BLAS_SIZE}'" >> settings.sh
echo export LAPACK_LIB="'%{LAPACK_LIB}'" >> settings.sh
echo export MAKE='%{__make}' >> settings.sh
%if 0%{?PYTHON_SUPPORT}
echo '$MAKE nwchem_config NWCHEM_MODULES="all python" 2>&1 | tee ../make_nwchem_config.log' > make.sh
%else
echo '$MAKE nwchem_config NWCHEM_MODULES="all" 2>&1 | tee ../make_nwchem_config.log' > make.sh
%endif
%if 0%{?make64_to_32}
echo '$MAKE 64_to_32 2>&1 | tee ../make_64_to_32.log' >> make.sh
echo 'export MAKEOPTS="USE_64TO32=y"' >> make.sh
%else
echo 'export MAKEOPTS=""' >> make.sh
%endif
# final make (log of ~200MB, don't write it)
echo '$MAKE ${MAKEOPTS} 2>&1' >> make.sh # | tee ../make.log' >> make.sh

# Have to do off-root builds to be able to build many versions at once
mv src src.orig

# To avoid replicated code define a macro
%global dobuild() \
cd src&& \
cp -p ../settings.sh ../compile$MPI_SUFFIX.sh&& \
echo export USE_MPI=y >> ../compile$MPI_SUFFIX.sh&& \
echo export USE_MPIF=y >> ../compile$MPI_SUFFIX.sh&& \
echo export USE_MPIF4=y >> ../compile$MPI_SUFFIX.sh&& \
echo export MPIEXEC=$MPI_BIN/mpiexec >> ../compile$MPI_SUFFIX.sh&& \
echo export LD_LIBRARY_PATH=$MPI_LIB >> ../compile$MPI_SUFFIX.sh&& \
echo export EXTERNAL_GA_PATH=$MPI_HOME >> ../compile$MPI_SUFFIX.sh&& \
cat ../make.sh >> ../compile$MPI_SUFFIX.sh&& \
%{__sed} -i "s|.log|$MPI_SUFFIX.log|g" ../compile$MPI_SUFFIX.sh&& \
cat ../compile$MPI_SUFFIX.sh&& \
sh ../compile$MPI_SUFFIX.sh&& \
mv ../bin/%{NWCHEM_TARGET}/%{name} ../bin/%{NWCHEM_TARGET}/%{name}_binary$MPI_SUFFIX&& \
echo '#!/bin/bash' >  ../bin/%{NWCHEM_TARGET}/%{name}$MPI_SUFFIX&& \
echo 'export FLEXIBLAS=openblas-openmp' >>  ../bin/%{NWCHEM_TARGET}/%{name}$MPI_SUFFIX&& \
echo -n "%{name}_binary$MPI_SUFFIX " >>  ../bin/%{NWCHEM_TARGET}/%{name}$MPI_SUFFIX&& \
echo '"$@"' >>  ../bin/%{NWCHEM_TARGET}/%{name}$MPI_SUFFIX&& \
chmod 755  ../bin/%{NWCHEM_TARGET}/%{name}$MPI_SUFFIX&& \
cat ../bin/%{NWCHEM_TARGET}/%{name}$MPI_SUFFIX&& \
NWCHEM_TARGET=%{NWCHEM_TARGET} %{__make} BLAS_SIZE=%{BLAS_SIZE} USE_INTERNALBLAS=1 USE_MPI=y clean&& \
cd ..

# build openmpi version
cp -rp src.orig src
%{_openmpi_load}
%dobuild
%{_openmpi_unload}

rm -rf src

cp -rp src.orig src
# build mpich version
%{_mpich_load}
%dobuild
%{_mpich_unload}

# leave last src build for debuginfo

rm -f make.sh settings.sh

cat <<EOF > %{PKG_TOP}/%{name}.sh
# NOTE: This is an automatically-generated file!  (generated by the
# %%{name} RPM).  Any changes made here will be lost if the RPM is
# uninstalled or upgraded.

# must end with slash!
PA=%{_datadir}/%{name}/libraries/

case \$NWCHEM_BASIS_LIBRARY in
*\${PA}*);;
*) NWCHEM_BASIS_LIBRARY=\${PA};;
esac
export NWCHEM_BASIS_LIBRARY

# must end with slash!
PA=%{_datadir}/%{name}/libraryps/

case \$NWCHEM_NWPW_LIBRARY in
*\${PA}*);;
*) NWCHEM_NWPW_LIBRARY=\${PA};;
esac
export NWCHEM_NWPW_LIBRARY

EOF

cat <<EOF > %{PKG_TOP}/%{name}.csh
# NOTE: This is an automatically-generated file!  (generated by the
# %%{name} RPM).  Any changes made here will be lost if the RPM is
# uninstalled or upgraded.

# must end with slash!
set PA=%{_datadir}/%{name}/libraries/

if (\$?NWCHEM_BASIS_LIBRARY) then
if ("\$NWCHEM_BASIS_LIBRARY" !~ *\${PA}*) then
	setenv NWCHEM_BASIS_LIBRARY \${PA}
endif
else
setenv NWCHEM_BASIS_LIBRARY \${PA}
endif

unset PA

# must end with slash!
set PA=%{_datadir}/%{name}/libraryps/

if (\$?NWCHEM_NWPW_LIBRARY) then
if ("\$NWCHEM_NWPW_LIBRARY" !~ *\${PA}*) then
	setenv NWCHEM_NWPW_LIBRARY \${PA}
endif
else
setenv NWCHEM_NWPW_LIBRARY \${PA}
endif

unset PA

EOF

# create /etc/nwchemrc
cat <<EOF > %{PKG_TOP}/nwchemrc
# NOTE: This is an automatically-generated file!  (generated by the
# %%{name} RPM).  Any changes made here will be lost if the RPM is
# uninstalled or upgraded.

# data directory names must end with slash!
nwchem_basis_library %{_datadir}/%{name}/libraries/
nwchem_nwpw_library %{_datadir}/%{name}/libraryps/
ffield amber
amber_1 %{_datadir}/%{name}/amber_s/
amber_2 %{_datadir}/%{name}/amber_q/
amber_3 %{_datadir}/%{name}/amber_x/
amber_4 %{_datadir}/%{name}/amber_u/
spce %{_datadir}/%{name}/solvents/spce.rst
charmm_s %{_datadir}/%{name}/charmm_s/
charmm_x %{_datadir}/%{name}/charmm_x/
EOF


%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}

# *.bak files not allowed by rpmlint
for file in `find %{PKG_TOP} -name "*.bak"`; do
rm -f ${file}
done

# To avoid replicated code define a macro
%global doinstall() \
mkdir -p $RPM_BUILD_ROOT/$MPI_BIN&& \
install -p -m 755 %{PKG_TOP}/bin/%{NWCHEM_TARGET}/%{name}_binary$MPI_SUFFIX $RPM_BUILD_ROOT/$MPI_BIN&& \
install -p -m 755 %{PKG_TOP}/bin/%{NWCHEM_TARGET}/%{name}$MPI_SUFFIX $RPM_BUILD_ROOT/$MPI_BIN

# install openmpi version
%{_openmpi_load}
%doinstall
%{_openmpi_unload}

# install mpich version
%{_mpich_load}
%doinstall
%{_mpich_unload}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -rp %{PKG_TOP}/src/data/* $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rp %{PKG_TOP}/src/basis/libraries $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rp %{PKG_TOP}/src/nwpw/libraryps $RPM_BUILD_ROOT%{_datadir}/%{name}
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/libraryps/{*MakeFile,*.fh,*.F,dependencies,include_stamp}

# env scripts
install -p -m 444 %{PKG_TOP}/*.*sh $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 444 %{PKG_TOP}/nwchemrc $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 444 %{PKG_TOP}/nwchemrc $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -p -m 444 %{PKG_TOP}/%{name}*.*sh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d

# To avoid: "Found '/tmp/rpmbuild/build/' in installed files; aborting"
for file in `find %{PKG_TOP} -name "*.log"`; do
%{__sed} -i "s|$RPM_BUILD_ROOT||g" ${file}
done
for file in `find %{PKG_TOP} -name "*.sh"`; do
%{__sed} -i "s|$RPM_BUILD_ROOT||g" ${file}
done


%check
export NWCHEM_TARGET=%{NWCHEM_TARGET}
# data directory names must end with slash!
export NWCHEM_BASIS_LIBRARY=$RPM_BUILD_ROOT%{_datadir}/%{name}/libraries/
export NWCHEM_NWPW_LIBRARY=$RPM_BUILD_ROOT%{_datadir}/%{name}/libraryps/

mv QA QA.orig.orig
cp -rp QA.orig.orig QA.orig

export NPROC=2 # test on 2 cores
export FLEXIBLAS=openblas-openmp

%if 0%{?el6}
export TIMEOUT_OPTS='3600'
%else
export TIMEOUT_OPTS='--preserve-status --kill-after 10 2700'
%endif

# To avoid replicated code define a macro
%global docheck() \
cp -rp QA.orig QA&& \
cd QA&& \
export LD_LIBRARY_PATH=${MPI_LIB}&& \
export PATH=%{PKG_TOP}/bin/$NWCHEM_TARGET:${MPI_BIN}:${PATH}&& \
export MPIRUN_PATH=${MPI_BIN}/mpiexec&& \
export MPIRUN_NPOPT="-np" && \
export USE_LIBXC=True && \
export NWCHEM_EXECUTABLE=%{PKG_TOP}/bin/$NWCHEM_TARGET/nwchem$MPI_SUFFIX&& \
time timeout ${TIMEOUT_OPTS} ./doafewqmtests.mpi ${NPROC} 2>&1 < /dev/null | tee ../doafewqmtests.mpi.${NPROC}$MPI_SUFFIX.log&& \
mv testoutputs ../testoutputs.doafewqmtests.mpi.${NPROC}$MPI_SUFFIX.log&& \
time timeout ${TIMEOUT_OPTS} ./dolibxctests.mpi ${NPROC} 2>&1 < /dev/null | tee ../dolibxctests.mpi.${NPROC}$MPI_SUFFIX.log&& \
mv testoutputs ../testoutputs.dolibxctests.mpi.${NPROC}$MPI_SUFFIX.log&& \
BUILD_LOG=../doafewqmtests.mpi.${NPROC}$MPI_SUFFIX.log&& \
TESTOUTPUTS=../testoutputs.doafewqmtests.mpi.${NPROC}$MPI_SUFFIX.log&& \
ls -al ${TESTOUTPUTS}&& \
for f in $(diff <(grep "Running tests/" ${BUILD_LOG}) <(grep -E "Running tests/|verifying output ... OK" ${BUILD_LOG} | grep "verifying output" -B 1 | grep Running) | grep Running | cut -d' ' -f 4); do printf '#%.0s' {1..80} && echo && NAME=$(basename ${f}) && echo ${TESTOUTPUTS}/${NAME}.out && printf '#%.0s' {1..80} && echo && cat ${TESTOUTPUTS}/${NAME}.out && printf '#%.0s' {1..80} && echo && if test -r ${TESTOUTPUTS}/${NAME}.out.nwparse; then cat ${TESTOUTPUTS}/${NAME}.out.nwparse; else cat ${TESTOUTPUTS}/${NAME}.err; fi; done&& \
BUILD_LOG=../dolibxctests.mpi.${NPROC}$MPI_SUFFIX.log&& \
TESTOUTPUTS=../testoutputs.dolibxctests.mpi.${NPROC}$MPI_SUFFIX.log&& \
ls -al ${TESTOUTPUTS}&& \
for f in $(diff <(grep "Running tests/" ${BUILD_LOG}) <(grep -E "Running tests/|verifying output ... OK" ${BUILD_LOG} | grep "verifying output" -B 1 | grep Running) | grep Running | cut -d' ' -f 4); do printf '#%.0s' {1..80} && echo && NAME=$(basename ${f}) && echo ${TESTOUTPUTS}/${NAME}.out && printf '#%.0s' {1..80} && echo && cat ${TESTOUTPUTS}/${NAME}.out && printf '#%.0s' {1..80} && echo && if test -r ${TESTOUTPUTS}/${NAME}.out.nwparse; then cat ${TESTOUTPUTS}/${NAME}.out.nwparse; else cat ${TESTOUTPUTS}/${NAME}.err; fi; done&& \
cd ..&& \
rm -rf QA

# check openmpi version
%{_openmpi_load}
export OMPI_MCA_btl=^uct
export OMPI_MCA_btl_base_warn_component_unused=0
%docheck
%{_openmpi_unload}

%{_mpich_load}
%docheck
%{_mpich_unload}


# restore QA
mv QA.orig QA


%files


%files common
%doc LICENSE*
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/profile.d/%{name}*.*sh
%config(noreplace) %{_sysconfdir}/nwchemrc


%files openmpi
%{_libdir}/openmpi%{?_opt_cc_suffix}/bin/%{name}_binary_openmpi
%{_libdir}/openmpi%{?_opt_cc_suffix}/bin/%{name}_openmpi


%files mpich
%{_libdir}/mpich%{?_opt_cc_suffix}/bin/%{name}_binary_mpich
%{_libdir}/mpich%{?_opt_cc_suffix}/bin/%{name}_mpich


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Oct 12 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 7.2.3-2
- Rebuild against libxc 7.0.0 in rawhide.

* Tue Sep 24 2024 Marcin Dulak <marcindulak@fedoraproject.org> - 7.2.3-1
- New upstream release

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 7.2.2-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 7.2.2-6
- Rebuilt for Python 3.13

* Fri Feb 16 2024 Marcin Dulak <marcindulak@fedoraproject.org> - 7.2.2-5
- Patch for implicit declaration of function ‘Py_SetProgramName' https://github.com/nwchemgit/nwchem/issues/950

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 10 2023 Marcin Dulak <marcindulak@fedoraproject.org> - 7.2.2-2
- Fix verbose mpich output truncation https://github.com/nwchemgit/nwchem/issues/895

* Mon Nov 06 2023 Marcin Dulak <marcindulak@fedoraproject.org> - 7.2.2-1
- New upstream release
- Print outputs of failed tests https://github.com/nwchemgit/nwchem/issues/895

* Fri Oct 20 2023 Marcin Dulak <marcindulak@fedoraproject.org> - 7.2.1-1
- New upstream release

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 7.2.0-3
- Rebuilt for Python 3.12

* Fri Jun 09 2023 Marcin Dulak <marcindulak@fedoraproject.org> - 7.2.0-2
- Switch to flexiblas-openblas-openmp due to bug #2182460

* Tue Mar 28 2023 Marcin Dulak <marcindulak@fedoraproject.org> - 7.2.0-1
- New upstream release
- Build with libxc support bug #2081873
- Remove %%{ix86} support due to openmpi bug #2142304

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 7.0.2-10
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 7.0.2-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Marcin Dulak <marcindulak@fedoraproject.org> - 7.0.2-6
- Requires %{name} instead of %{name-common} to handle install dependencies
- export FLEXIBLAS=openblas-serial using a wrapper https://bugzilla.redhat.com/show_bug.cgi?id=1920009

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 7.0.2-4
- Patch for Python 3.10
- Compile with USE_NOIO=TRUE https://github.com/nwchemgit/nwchem/issues/272

* Sat Nov 21 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 7.0.2-3
- Replace OMP_NUM_THREADS=1 with FLEXIBLAS=openblas-serial to restore https://src.fedoraproject.org/rpms/flexiblas/c/4286c061697330a8d30d2cd3a1d20f018da81258
- Replace mentions of the old website with nwchemgit.github.io

* Mon Oct 19 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 7.0.2-2
- Set OMP_NUM_THREADS=1 https://github.com/edoapra/fedpkg/issues/10#issuecomment-699276160
- Fix hostname br for el6

* Thu Oct 15 2020 Edoardo Aprà <edoardo.apra@gmail.com> - 7.0.2-1
- new 7.0.2 release

* Fri Aug 28 2020 Iñaki Úcar <iucar@fedoraproject.org> - 7.0.0-11
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.0.0-9
- Rebuilt for Python 3.9

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 7.0.0-8
- Fix string quoting for rpm >= 4.16

* Sat Mar 28 2020 Edoardo Aprà <edoardo.apra@gmail.com> - 7.0.0-7
- nproc=1 for mpich/ppc64le

* Sun Mar 22 2020 Edoardo Aprà <edoardo.apra@gmail.com> - 7.0.0-6
- fix to get rid of HYDRA_DEBUG on mpich
- drop rhel6 support

* Wed Mar 18 2020 Edoardo Aprà <edoardo.apra@gmail.com> - 7.0.0-5
- switch to ga 5.7-2.3
- enabled arm, aarch64 and ppc64le architectures
- removed libibverbs-devel, ncurses-devel, zlib-devel and readline-devel
- perl-File-Basename rpm needed on fedora 33
- 32bit build needed for arm
- added patch to fix solvation failures on ppc64le

* Fri Mar 06 2020 Edoardo Aprà <edoardo.apra@gmail.com> - 7.0.0-4
- work-around for openmpi 4.0.1 segfault
- skip tests for rhel6 mpich
- fix for pspw when peigs is not available and scalapack is
- fix for mcscf when peigs is not available and scalapack is
- Using tarball from 7.0.0 official release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Marcin Dulak <marcindulak@fedoraproject.org> - 7.0.0-2
- new upstream snapshot release

* Fri Oct 04 2019 Marcin Dulak <marcindulak@fedoraproject.org> - 7.0.0-1
- new upstream snapshot release

* Fri Aug 30 2019 Marcin Dulak <marcindulak@fedoraproject.org> - 6.8.2-1
- new upstream snapshot release
- switch to python3 br on fedora >= 30 bug #1738065

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Marcin Dulak <marcindulak@fedoraproject.org> - 6.8.1-10
- removal of tcsh br requires a patch https://github.com/nwchemgit/nwchem/issues/120

* Mon Jun 03 2019 Marcin Dulak <marcindulak@fedoraproject.org> - 6.8.1-9
- remove br tcsh since it's orphaned in Fedora 30

* Fri May 17 2019 Marcin Dulak <marcindulak@fedoraproject.org> - 6.8.1-8
- explicit mpi related requires on epel7/epel6

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 6.8.1-7
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Marcin Dulak <marcindulak@fedoraproject.org> - 6.8.1-6
- protect yourself from Fedora changing rpm macros: no python_version available in f29

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Edoardo Apra <edoardo.apra@gmail.com> - 6.8.1-4
- requires ga rpm version >= 5.6.5-1

* Fri Jun 15 2018 Marcin Dulak <marcindulak@fedoraproject.org> - 6.8.1-3
- minor cleanup
- br libibverbs-devel

* Thu Jun 14 2018 Edoardo Apra <edoardo.apra@gmail.com> - 6.8.1-2
- 6.8.1 release tarball

* Thu Jun 14 2018 Marcin Dulak <marcindulak@fedoraproject.org> - 6.8.1-1
- upstream update, sources are at github now
- drop el6 support

* Fri Jun 08 2018 Marcin Dulak <marcindulak@fedoraproject.org> - 6.6.27746-34
- patch https://github.com/nwchemgit/nwchem/issues/41

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.27746-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.27746-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.27746-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Marcin Dulak <marcindulak@fedoraproject.org> - 6.6.27746-30
- restore nwchemrc

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.27746-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 6.6.27746-28
- Rebuild for openmpi 2.0

* Tue Jul 19 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 6.6.27746-27
- apply upstream patches for gcc version 6 (see bug# 1356735)
- set NWCHEM env variables instead of prepending (bug #1347788)

* Sat Jul 16 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 6.6.27746-26
- remove compiler native arch optimizations (see bug# 1347788)

* Sat Jul 16 2016 Marcin Dulak <marcindulak@fedoraproject.org> - 6.6.27746-25
- kill hanging %%check after 30min timeout (see bug #1356735)
- remove defattr
- prevent macros from continuing after an intermediate command error
- handle mpi Requires explicitly due to el6 (see bug #1357018)
- get rid of %%{mpich} variables

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.27746-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Rafael Fonseca <rdossant@redhat.com> - 6.5.26243-23
- Make nwchem x86 exclusive because of its BuildRequires (#1278066)

* Sat Nov  7 2015 Marcin Dulak <marcindulak@fedoraproject.org> - 6.6.27746-22
- upstream update
- files-attr

* Fri Oct 23 2015 Susi Lehtola <jussilehtola@fedoraproject.org> - 6.5.26243-21
- Enable CCSDTQ and CCSDTLR.

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 6.5.26243-20
- Rebuild for openmpi 1.10.0

* Fri Aug 28 2015 Marcin Dulak <marcindulak@fedoraproject.org> - 6.5.26243-19
- hostname is in net-tools only on el6

* Thu Aug 27 2015 Marcin Dulak <marcindulak@fedoraproject.org> - 6.5.26243-18
- BuildRequires net-tools (hostname) needed

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> - 6.5.26243-17
- Rebuild for RPM MPI Requires Provides Change

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.26243-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Marcin Dulak <marcindulak@fedoraproject.org> - 6.5.26243-15
- fix linking of mpich/openmpi

* Mon Mar 30 2015 Marcin Dulak <marcindulak@fedoraproject.org> - 6.5.26243-15
- EACCSD, IPCCSD enabled
- fix Fedora 23 linking of mpich/openmpi

* Mon Mar 2 2015 Marcin Dulak <marcindulak@fedoraproject.org> - 6.5.26243-14
- fix bug #1196616
- allow SRPM build on noarch

* Sat Nov 15 2014 Marcin Dulak <marcindulak@fedoraproject.org> - 6.5.26243-13
- upstream update
- MRCC_THEORY and NWCHEM_LONG_PATHS enabled
- exclude aarch64
- mpich3 on el6

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Marcin Dulak <marcindulak@fedoraproject.org> - 6.3.2-11
- explicit Requires needed bug #1105509
- excluding tests (hang on Fedora 21 i686)
- added arm to ifarch (koji does: rpmbuild -bs --target arm --nodeps)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 8 2014 Marcin Dulak <marcindulak@fedoraproject.org> 6.3.2-9
- removed bundling of BLAS, LAPACK, GA

* Tue Mar 18 2014 Björn Esser <bjoern.esser@gmail.com> - 6.3.2-8
- rebuilt for mpich-3.1

* Fri Feb 7 2014 Marcin Dulak <marcindulak@fedoraproject.org> 6.3.2-7
- exclude ppc64 on el6

* Fri Feb 7 2014 Marcin Dulak <marcindulak@fedoraproject.org> 6.3.2-6
- common is noarch
- LICENSE* in common
- %%config(noreplace) %%{_sysconfdir}/profile.d/* + more explicit glob
- shorten %%description and %%summary
- use serial atlas (-lsatlas)
- export BLAS_SIZE=4
- fdupes removed: runs twice (for i686 and x86_64) and exchanges links on
  these two platforms, giving: BuildError: mismatch when analyzing ...

* Sat Jan 25 2014 Marcin Dulak <marcindulak@fedoraproject.org> 6.3.2-5
- ExcludeArch: %%arm

* Fri Jan 24 2014 Marcin Dulak <marcindulak@fedoraproject.org> 6.3.2-4
- the idea of %%optflags dropped, resulting executables were broken

* Tue Jan 14 2014 Marcin Dulak <marcindulak@fedoraproject.org> 6.3.2-3
- https://bugzilla.redhat.com/show_bug.cgi?id=984605#c12: timestamps

* Wed Nov 6 2013 Marcin Dulak <marcindulak@fedoraproject.org> 6.3.2-2
- update version
- explicitly set ARMCI_NETWORK=SOCKETS for serial build
- dependency on openssh-clients for serial build
- use tatlas on Fedora >= 21
- basis are now under src/basis/libraries

* Wed Jul 10 2013 Marcin Dulak <marcindulak@fedoraproject.org> 6.3.1-2
- conform to http://fedoraproject.org/wiki/Packaging:MPI#Packaging_of_MPI_software

* Wed Jul 10 2013 Marcin Dulak <marcindulak@fedoraproject.org> 6.3.1-1
- adopted for Fedora and EPEL
- split into the main and data package

* Mon Aug 13 2012 Marcin Dulak <Marcin.Dulak@fysik.dtu.dk> 6.1.1-1
- restructured for build.opensuse.org and Fedora based on nwchem.spec

* Sat Feb 4 2012 Marcin Dulak <marcindulak@fedoraproject.org> 6.1-1
- USE_NOFSCHECK set to True
- src/data/* installed under %%{prefix}/share/%%{prgname}/data
- contrib/python/Gnuplot.py excluded
- scalapack build on Fedora (for some reason libscalapack.a not found on build.opensuse.org)
- {doc,web} directories not in source anymore

* Wed Dec 21 2011 Marcin Dulak <marcindulak@fedoraproject.org> 6.1.pre6-1
- allow pre releases to be built
- fixed ga-5-0 configure problems on EL5 and openSUSE 11.3-12.1

* Mon Oct 31 2011 Marcin Dulak <marcindulak@fedoraproject.org> 6.0-1
- initial version
