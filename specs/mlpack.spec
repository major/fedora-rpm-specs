Name:           mlpack
Version:        4.5.1
Release:        1%{?dist}
Summary:        Fast, header-only C++ machine learning library

# The source in src/mlpack/core/std_backport/ is available under 
# Apache-2.0 license
# All other code is under BSD-3-Clause
# The stb_image and stb_image_write libraries are (MIT OR Unlicense); since
# header-only libraries are treated as static libraries, they also contribute
# to the license of the binary RPMs.
License:        BSD-3-Clause AND Apache-2.0 AND (MIT OR Unlicense)
URL:            http://www.mlpack.org
Source0:        http://www.mlpack.org/files/%{name}-%{version}.tar.gz

# Drop support for i686
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc-c++
# Use cmake28 package on RHEL.
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  cmake28 >= 2.8.5
%else
BuildRequires:  cmake >= 2.8.5
%endif

BuildRequires:  armadillo-devel >= 10.8.2
BuildRequires:  ensmallen-devel >= 2.10.0
BuildRequires:  cli11-devel
BuildRequires:  cereal-devel
BuildRequires:  pkg-config

# Header-only libraries (-static is for tracking per guidelines)
# Enforce the the minimum EVR to contain fixes for all of:
# CVE-2021-28021
# CVE-2021-42715
# CVE-2021-42716
# CVE-2022-28041
# CVE-2023-43898
# CVE-2023-45661
# CVE-2023-45662
# CVE-2023-45663
# CVE-2023-45664
# CVE-2023-45666
# CVE-2023-45667
%if 0%{?el7} || 0%{?el8}
%global min_stb_image 2.28-0.39.20231011gitbeebb24
%else
%global min_stb_image 2.28^20231011gitbeebb24-12
%endif
BuildRequires:  stb_image-devel >= %{min_stb_image}
BuildRequires:  stb_image-static
BuildRequires:  stb_image_write-devel
BuildRequires:  stb_image_write-static

# For generating man pages (CMake configuration takes care of this assuming
# txt2man is installed).  It is possible that we could just add all the man
# pages, generated offline, as a patch to this SRPM, but txt2man seems to exist
# in repos.
BuildRequires:  txt2man

# Required for building Python bindings.
BuildRequires: 	python3-devel, python3-Cython, python3-setuptools, python3-numpy
BuildRequires:	python3-pandas, python3-pytest-runner, python3-wheel

# something doesn't like size_t being unsigned long on s390
ExcludeArch:    s390
# The s390x builders don't currently have enough RAM to build mlpack.
# (Check again for mlpack 4.0, which should require much less RAM.)
#ExcludeArch:	s390x

%description
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use. Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users. mlpack outperforms competing machine learning libraries by large
margins.

# Licenses and information files
%package licenses
Summary:        Licenses and information files for mlpack (machine learning library)

%description licenses
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use. Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users. mlpack outperforms competing machine learning libraries by large
margins.  This package provides the command-line executables which run mlpack
methods and related documentation.

# Executables.
%package bin
Summary:        Command-line executables for mlpack (machine learning library)
Requires:       %{name}-licenses
Requires:       armadillo

%description bin
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use. Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users. mlpack outperforms competing machine learning libraries by large
margins.  This package provides the command-line executables which run mlpack
methods and related documentation.

# Development headers.
%package devel
Summary:   Development headers for mlpack (C++ machine learning library)
Requires:  %{name}-licenses
Requires:  armadillo-devel >= 9.800.0
Requires:  ensmallen-devel >= 2.10.0
Requires:  cereal-devel
Requires:  lapack-devel
Requires:  pkg-config
Requires:  stb_image-devel%{?_isa} >= %{min_stb_image}
Requires:  stb_image_write-devel%{?_isa}
Provides:  %{name}-static = %{version}-%{release}

%description devel
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use. Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users. mlpack outperforms competing machine learning libraries by large
margins.  This package provides the headers to compile applications against
mlpack.



%package python3
Summary:   Python 3 bindings for mlpack (C++ machine learning library)
Requires:  %{name}-licenses
Requires:  python3
Requires:  python3-numpy
Requires:  python3-pandas
Requires:  python3-Cython

%description python3
mlpack is a C++ machine learning library with emphasis on scalability, speed,
and ease-of-use.  Its aim is to make machine learning possible for novice users
by means of a simple, consistent API, while simultaneously exploiting C++
language features to provide maximum performance and maximum flexibility for
expert users.  mlpack outperforms competing machine learning libraries by large
margins.  This package provides the Python bindings for mlpack.


# For the F20 unversioned documentation change.  This evaluates to
# %%{_pkgdocdir} if on F20 and %%{_docdir}/%%{name}-%%{version} otherwise.
%global our_docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

# Disable LTO: it takes too much memory.
%define _lto_cflags %{nil}

%prep
%autosetup -p1

%build
# Make sure pip is available.
%{python3} -m ensurepip --upgrade

%if 0%{?rhel} && 0%{?rhel} <= 7
# On RHEL6, the Boost CMake scripts fail for some reason.  I don't have the
# time (or patience) to investigate, but if we force CMake to find Boost "the
# hard way" by specifying Boost_NO_BOOST_CMAKE=1, it works.
%{cmake28} -D CMAKE_INSTALL_LIBDIR=%{_libdir} -D DEBUG=OFF -D PROFILE=OFF -D BUILD_TESTS=OFF -D BUILD_PYTHON_BINDINGS=ON -D PYTHON_EXECUTABLE=%{python3} -D BUILD_GO_BINDINGS=OFF -D BUILD_JULIA_BINDINGS=OFF -D STB_IMAGE_INCLUDE_DIR=%{_includedir}
%else
%{cmake} -D CMAKE_INSTALL_LIBDIR=%{_libdir} -D DEBUG=OFF -D PROFILE=OFF -D BUILD_TESTS=OFF -D BUILD_PYTHON_BINDINGS=ON -D PYTHON_EXECUTABLE=%{python3} -D BUILD_GO_BINDINGS=OFF -D BUILD_JULIA_BINDINGS=OFF -D STB_IMAGE_INCLUDE_DIR=%{_includedir}
%endif

# Try and reduce RAM usage.
%ifarch armv7hl
cmake -B %{__cmake_builddir} \
      -D CMAKE_C_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" -D CMAKE_CXX_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" .
%endif

%ifarch i686
cmake -B %{__cmake_builddir} \
      -D CMAKE_C_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" -D CMAKE_CXX_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" .
%endif

%ifarch ppc64le
cmake -B %{__cmake_builddir} \
      -D CMAKE_C_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" -D CMAKE_CXX_FLAGS="`echo %{optflags} | sed 's/-pipe//g' | sed 's/$/ --param ggc-min-heapsize=32768 --param ggc-min-expand=1/'`" .
%endif

# Don't use %make because it could use too much RAM with multiple cores on Koji...
%{cmake_build}

%install
%{cmake_install}

%ldconfig_scriptlets

%files licenses
%license LICENSE.txt
%license COPYRIGHT.txt
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc HISTORY.md
%doc GOVERNANCE.md
%doc README.md
%doc UPDATING.txt

%files bin
%{_bindir}/mlpack_adaboost
%{_bindir}/mlpack_approx_kfn
%{_bindir}/mlpack_bayesian_linear_regression
%{_bindir}/mlpack_cf
%{_bindir}/mlpack_dbscan
%{_bindir}/mlpack_decision_tree
%{_bindir}/mlpack_det
%{_bindir}/mlpack_emst
%{_bindir}/mlpack_fastmks
%{_bindir}/mlpack_gmm_generate
%{_bindir}/mlpack_gmm_probability
%{_bindir}/mlpack_gmm_train
%{_bindir}/mlpack_hmm_generate
%{_bindir}/mlpack_hmm_loglik
%{_bindir}/mlpack_hmm_train
%{_bindir}/mlpack_hmm_viterbi
%{_bindir}/mlpack_hoeffding_tree
%{_bindir}/mlpack_image_converter
%{_bindir}/mlpack_kde
%{_bindir}/mlpack_kernel_pca
%{_bindir}/mlpack_kfn
%{_bindir}/mlpack_kmeans
%{_bindir}/mlpack_knn
%{_bindir}/mlpack_krann
%{_bindir}/mlpack_lars
%{_bindir}/mlpack_linear_regression
%{_bindir}/mlpack_linear_svm
%{_bindir}/mlpack_lmnn
%{_bindir}/mlpack_local_coordinate_coding
%{_bindir}/mlpack_logistic_regression
%{_bindir}/mlpack_lsh
%{_bindir}/mlpack_mean_shift
%{_bindir}/mlpack_nbc
%{_bindir}/mlpack_nca
%{_bindir}/mlpack_nmf
%{_bindir}/mlpack_pca
%{_bindir}/mlpack_perceptron
%{_bindir}/mlpack_preprocess_binarize
%{_bindir}/mlpack_preprocess_describe
%{_bindir}/mlpack_preprocess_imputer
%{_bindir}/mlpack_preprocess_one_hot_encoding
%{_bindir}/mlpack_preprocess_scale
%{_bindir}/mlpack_preprocess_split
%{_bindir}/mlpack_radical
%{_bindir}/mlpack_random_forest
%{_bindir}/mlpack_range_search
%{_bindir}/mlpack_softmax_regression
%{_bindir}/mlpack_sparse_coding
%{_mandir}/mlpack_adaboost.1*
%{_mandir}/mlpack_approx_kfn.1*
%{_mandir}/mlpack_bayesian_linear_regression.1*
%{_mandir}/mlpack_cf.1*
%{_mandir}/mlpack_dbscan.1*
%{_mandir}/mlpack_decision_tree.1*
%{_mandir}/mlpack_det.1*
%{_mandir}/mlpack_emst.1*
%{_mandir}/mlpack_fastmks.1*
%{_mandir}/mlpack_gmm_generate.1*
%{_mandir}/mlpack_gmm_probability.1*
%{_mandir}/mlpack_gmm_train.1*
%{_mandir}/mlpack_hmm_generate.1*
%{_mandir}/mlpack_hmm_loglik.1*
%{_mandir}/mlpack_hmm_train.1*
%{_mandir}/mlpack_hmm_viterbi.1*
%{_mandir}/mlpack_hoeffding_tree.1*
%{_mandir}/mlpack_image_converter.1*
%{_mandir}/mlpack_kde.1*
%{_mandir}/mlpack_kernel_pca.1*
%{_mandir}/mlpack_kfn.1*
%{_mandir}/mlpack_kmeans.1*
%{_mandir}/mlpack_knn.1*
%{_mandir}/mlpack_krann.1*
%{_mandir}/mlpack_lars.1*
%{_mandir}/mlpack_linear_regression.1*
%{_mandir}/mlpack_linear_svm.1*
%{_mandir}/mlpack_lmnn.1*
%{_mandir}/mlpack_local_coordinate_coding.1*
%{_mandir}/mlpack_logistic_regression.1*
%{_mandir}/mlpack_lsh.1*
%{_mandir}/mlpack_mean_shift.1*
%{_mandir}/mlpack_nbc.1*
%{_mandir}/mlpack_nca.1*
%{_mandir}/mlpack_nmf.1*
%{_mandir}/mlpack_pca.1*
%{_mandir}/mlpack_perceptron.1*
%{_mandir}/mlpack_preprocess_binarize.1*
%{_mandir}/mlpack_preprocess_describe.1*
%{_mandir}/mlpack_preprocess_imputer.1*
%{_mandir}/mlpack_preprocess_one_hot_encoding.1*
%{_mandir}/mlpack_preprocess_scale.1*
%{_mandir}/mlpack_preprocess_split.1*
%{_mandir}/mlpack_radical.1*
%{_mandir}/mlpack_random_forest.1*
%{_mandir}/mlpack_range_search.1*
%{_mandir}/mlpack_softmax_regression.1*
%{_mandir}/mlpack_sparse_coding.1*

%files devel
%{_includedir}/mlpack.hpp
%{_includedir}/mlpack/
%{_libdir}/pkgconfig/mlpack.pc

%files python3
%{python3_sitearch}/mlpack/
%{python3_sitearch}/mlpack-*.dist-info

%changelog
* Tue Dec 24 2024 Ryan Curtin <ryan@ratml.org> - 4.5.1-1
- Update to latest stable version.

* Mon Dec 23 2024 Orion Poplawski <orion@nwra.com> - 4.5.0-2
- Rebuild with numpy 2.x (rhbz#2333778)

* Fri Sep 20 2024 Ryan Curtin <ryan@ratml.org> - 4.5.0-1
- Update to latest stable version.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 4.4.0-2
- Rebuilt for Python 3.13

* Fri May 31 2024 Ryan Curtin <ryan@ratml.org>  - 4.4.0-1
- Update to latest stable version.

* Sun May 12 2024 Sandro <devel@penguinpee.nl> - 4.3.0-4
- Drop i686 support

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 19 2023 Ryan Curtin <ryan@ratml.org> - 4.3.0-1
- Update to latest stable version.
- Rebuild against new Armadillo major version (12).

* Mon Oct 30 2023 Benson Muite <benson_muite@emailplus.org> - 4.2.1-5
- Use RPM macros for python and cmake build directory

* Fri Oct 27 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 4.2.1-4
- Ensure stb_image contains the latest CVE patches

* Wed Oct 25 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 4.2.1-3
- Ensure stb_image contains the latest CVE patches

* Mon Oct 16 2023 Ryan Curtin <ryan@ratml.org> - 4.2.1-2
- Attempt to reduce RAM usage on ppc64le.

* Mon Sep 11 2023 Ryan Curtin <ryan@ratml.org> - 4.2.1-1
- Update to latest stable version.

* Thu Jul 27 2023 Ryan Curtin <ryan@ratml.org> - 4.2.0-4
- Bugfix: ensure Cython finds pxds for a successful build.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 4.2.0-2
- Rebuilt for Python 3.12

* Thu Jun 22 2023 Ryan Curtin <ryan@ratml.org> - 4.2.0-1
- Update to latest stable version.

* Thu Apr 27 2023 Benson Muite <benson_muite@emailplus.org> - 4.1.0-1
- Update to new version

* Sat Feb 25 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 4.0.1-4
- Update min. stb_image versions for nullptr deref. bug
- Add stb license to the License field

* Mon Feb 13 2023 Benson Muite <benson_muite@emailplus.org> - 4.0.1-3
- Use SPDX identifiers
- Update license information to include Apache-2.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Ryan Curtin <ryan@ratml.org> - 4.0.1-1
- Update to latest stable version.

* Mon Nov 21 2022 Ryan Curtin <ryan@ratml.org> - 4.0.0-7
- Fix incorrect Requires again (oops) :).

* Thu Nov 17 2022 Benson Muite <benson_muite@emailplus.org> - 4.0.0-6
- Use license package

* Tue Nov 15 2022 Benson Muite <benson_muite@emailplus.org> - 4.0.0-5
- Use just bin and devel directories

* Mon Nov 14 2022 Benson Muite <benson_muite@emailplus.org> - 4.0.0-4
- Include README and other documentation files

* Sun Nov 13 2022 Benson Muite <benson_muite@emailplus.org> - 4.0.0-3
- Put license in base package
- Add static label to header only library

* Mon Oct 31 2022 Ryan Curtin <ryan@ratml.org> - 4.0.0-2
- Fix incorrect Requires.

* Wed Oct 26 2022 Ryan Curtin <ryan@ratml.org> - 4.0.0-1
- Update to latest stable version.
- doc subpackage is no longer produced (mlpack 4.0.0 has no Doxygen support anymore).
- Remove boost dependency, replace with cereal.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Lumír Balhar <lbalhar@redhat.com> - 3.4.2-17
- Fix build by BR python3-devel
- Fix compatibility with latest setuptools

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 3.4.2-16
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 3.4.2-15
- Rebuilt for Boost 1.78

* Sat Apr 23 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 3.4.2-14
- Security fix for CVE-2022-28041

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 22 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.4.2-12
- Fix CVE-2021-42715 and CVE-2021-42716 in stb_image

* Mon Aug 23 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.4.2-11
- Simplify stb unbundling

* Mon Aug 23 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 3.4.2-10
- Unbundle stb_image.h/stb_image_write.h

* Fri Aug 13 2021 Ryan Curtin <ryan@ratml.org> - 3.4.2-9
- Rebuilt for CLI 2.0.0.

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 3.4.2-8
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.4.2-6
- Rebuilt for Python 3.10

* Mon Feb 15 2021 Ryan Curtin <ryan@ratml.org> - 3.4.2-5
- Disable s390x build due to memory usage concerns.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 3.4.2-3
- Rebuilt for Boost 1.75

* Tue Jan  5 19:43:14 WET 2021 José Matos <jamatos@fedoraproject.org> - 3.4.2-2
- rebuild for armadillo 10

* Wed Oct 28 2020 Ryan Curtin <ryan@ratml.org> - 3.4.2-1
- Update to latest stable version.

* Wed Sep 09 2020 Ryan Curtin <ryan@ratml.org> - 3.4.1-1
- Update to latest stable version.

* Tue Aug 04 2020 Ryan Curtin <ryan@ratml.org> - 3.3.2-4
- Update for CMake out-of-source build fixes.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Ryan Curtin <ryan@ratml.org> - 3.3.2-1
- Update to latest stable version.

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 3.3.0-3
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3.0-2
- Rebuilt for Python 3.9

* Wed Apr 08 2020 Ryan Curtin <ryan@ratml.org> - 3.3.0-1
- Update to latest stable version.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 27 2019 Ryan Curtin <ryan@ratml.org> - 3.2.2-1
- Update to latest stable version.

* Tue Nov 05 2019 Ryan Curtin <ryan@ratml.org> - 3.2.1-1
- Update to latest stable version.

* Thu Sep 26 2019 Ryan Curtin <ryan@ratml.org> - 3.2.0-1
- Update to latest stable version.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-2
- Rebuilt for Python 3.8

* Fri Aug 02 2019 Ryan Curtin <ryan@ratml.org> - 3.1.1-1
- Update to latest stable version.

* Thu Jul 25 2019 Ryan Curtin <ryan@ratml.org> - 3.1.0-3
- Add ensmallen dependency correctly.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Ryan Curtin <ryan@ratml.org> - 3.1.0-1
- Update to latest stable version.

* Sun Mar 10 2019 Ryan Curtin <ryan@ratml.org> - 3.0.4-3
- Remove Python2 packages.

* Thu Feb 07 2019 Ryan Curtin <ryan@ratml.org> - 3.0.4-2
- Add Python packages.
- A few simple fixes.

* Thu Feb 07 2019 Tomas Popela <tpopela@redhat.com> - 3.0.4-1
- Update to 3.0.4

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 2.2.5-9
- Rebuilt for Boost 1.69

* Fri Aug 17 2018 José Abílio Matos <jamatos@fc.up.pt> - 2.2.5-8
- rebuild for armadillo soname bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.2.5-6
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.5-5
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 2.2.5-3
- Rebuilt for Boost 1.66

* Fri Dec 01 2017 Ryan Curtin <ryan@ratml.org> - 2.2.5-2
- Rebuild for Armadillo soname bump.

* Wed Sep 13 2017 Ryan Curtin <ryan@ratml.org> - 2.2.5-1
- Update to latest stable version.
- Add pkg-config dependency.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 2.0.1-6
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 2.0.1-5
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 30 2016 José Matos <jamatos@fedoraproject.org> - 2.0.1-2
- Rebuild for armadillo 7.x and remove BR SuperLU as armadillo takes care of that

* Thu Feb 11 2016 Ryan Curtin <ryan@ratml.org> - 2.0.1-1
- Update to latest stable version.
- Add doxygen.patch for bug with newer Doxygen versions.

* Thu Feb 11 2016 José Matos <jamatos@fedoraproject.org> - 1.0.11-11
- rebuild for armadillo 6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.0.11-9
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.0.11-8
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.0.11-6
- rebuild for Boost 1.58

* Fri Jul  3 2015 José Matos <jamatos@fedoraproject.org> - 1.0.11-5
- Rebuild for armadillo 5(.xxx.y)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.11-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.0.11-2
- Rebuild for boost 1.57.0

* Thu Dec 11 2014 Ryan Curtin <ryan@ratml.org> - 1.0.11-1
- Update to latest stable release.

* Fri Aug 29 2014 Ryan Curtin <ryan@ratml.org> - 1.0.10-1
- Update to latest stable release.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Ryan Curtin <ryan@ratml.org> - 1.0.9-1
- Update to latest stable release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.0.8-3
- Rebuild for boost 1.55.0

* Wed Mar 19 2014 José Matos <jamatos@fedoraproject.org> - 1.0.8-2
- Rebuild for Armadillo 4.1 on Fedora 19, 20 and rawhide.

* Fri Jan 10 2014 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.8-1
- Update to latest stable release.
- Rebuild for Armadillo 4.0 on rawhide.

* Sun Nov 03 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.7-1
- Update to latest stable release.

* Tue Aug 06 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.6-6
- Add no_exclude_build.patch so that Koji builds don't exclude all the code from Doxygen.

* Tue Aug 06 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.6-5
- Require graphviz (dot) for generation of Doxygen graphs.

* Tue Aug 06 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.6-4
- Use %%{our_docdir} for F20 change to unversioned documentation directory names.
- Do not package HTML documentation in main package.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 1.0.6-2
- Rebuild for boost 1.54.0

* Thu Jun 13 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.6-1
- Update to latest stable release.

* Sat May 25 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.5-1
- Update to latest stable release.
- Add new executables that version 1.0.5 provides.

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.0.4-3
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.0.4-2
- Rebuild for Boost-1.53.0

* Fri Feb 08 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.4-1
- Update to latest stable release.
- Update dependencies to new minimum requirements.

* Wed Jan 02 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.3-4
- Use cmake28 in RHEL packages.

* Wed Jan 02 2013 Dan Horák <dan[at]danny.cz> - 1.0.3-3
- Exclude s390, something doesn't like size_t being unsigned long

* Tue Jan 01 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.3-2
- Add u64_s64.patch.
- Fix bogus dates in changelog.
- Add new executables and man pages to files list.

* Tue Jan 01 2013 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.3-1
- Update to version 1.0.3.
- Remove now-unnecessary packages.

* Wed Sep 26 2012 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.1-5
- Simplify LICENSE.txt installation.
- Install doxygen documentation.

* Sun Sep 16 2012 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.1-4
- Distribute LICENSE.txt.

* Sun Jul 29 2012 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.1-3
- Fix group names for packages.
- Comment patches more verbosely.
- Rename exectuables to mlpack_* to avoid possible naming conflicts.

* Sat Jul 21 2012 Sterling Lewis Peet <sterling.peet@gatech.edu> - 1.0.1-2
- Include GetKernelMatrix patch so that mlpack builds using fedora flags.

* Thu Mar 08 2012 Ryan Curtin <gth671b@mail.gatech.edu> - 1.0.1-1
- Initial packaging of mlpack.
