#uncomment next line for a release candidate or a beta
#%%global relc rc1

# Simple way to disable tests
%if 0%{?flatpak} || 0%{?rhel} || 0%{?fedora}
%bcond_with tests
%else
%bcond_without tests
%endif

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%global blasvar %{nil}
%else
%global blaslib openblas
%global blasvar p
%endif

%global modname numpy

Name:           numpy
Version:        2.3.2
Release:        1%{?dist}
Epoch:          1
Summary:        A fast multidimensional array facility for Python

# Everything is BSD-3-Clause except...
# numpy/core/include/numpy/libdivide: Zlib OR BSL-1.0
# numpy/core/src/multiarray/dragon4.*: MIT
# numpy/random/src/mt19937/randomkit.h: MIT
# numpy/random/src/pcg64: MIT AND Apache-2.0
# numpy/random/src/sfc64: MIT
License:        BSD-3-Clause AND MIT AND Apache-2.0 AND (Zlib OR BSL-1.0)
URL:            http://www.numpy.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://numpy.org/doc/%(echo %{version} | cut -d. -f1-2)/numpy-html.zip

# https://github.com/numpy/numpy/pull/28748
#Patch:          Support-Python-3.14.patch

%description
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

There are also basic facilities for discrete fourier transform,
basic linear algebra and random number generation. Also included in
this package is a version of f2py that works properly with NumPy.


%package -n python3-numpy
Summary:        A fast multidimensional array facility for Python

%{?python_provide:%python_provide python3-numpy}
Provides:       libnpymath-static = %{epoch}:%{version}-%{release}
Provides:       libnpymath-static%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       numpy = %{epoch}:%{version}-%{release}
Provides:       numpy%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      numpy < 1:1.10.1-3

BuildRequires:  python3-devel
BuildRequires:  gcc-gfortran gcc gcc-c++
BuildRequires:  lapack-devel
%if 0%{?fedora}
BuildRequires:  libdivide-devel
%endif
BuildRequires:  ninja-build
%if %{with tests}
BuildRequires:  python3-hypothesis
BuildRequires:  python3-pytest
BuildRequires:  python3-test
BuildRequires:  python3-typing-extensions
%endif
BuildRequires: %{blaslib}-devel
BuildRequires: chrpath
# Upstream does not support splitting out f2py
#  https://github.com/numpy/numpy/issues/28016
#  https://bugzilla.redhat.com/show_bug.cgi?id=2332307
Requires:       python3-numpy-f2py%{?_isa} = %{epoch}:%{version}-%{release}

%if !0%{?fedora}
Provides:       bundled(libdivide) = 3.0
%endif

%description -n python3-numpy
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

There are also basic facilities for discrete fourier transform,
basic linear algebra and random number generation. Also included in
this package is a version of f2py that works properly with NumPy.

%package -n python3-numpy-f2py
Summary:        f2py for numpy
Requires:       python3-numpy%{?_isa} = %{epoch}:%{version}-%{release}
Suggests:       python3-devel
Provides:       python3-f2py = %{version}-%{release}
Obsoletes:      python3-f2py <= 2.45.241_1927
%{?python_provide:%python_provide python3-numpy-f2py}
Provides:       f2py = %{epoch}:%{version}-%{release}
Provides:       numpy-f2py = %{epoch}:%{version}-%{release}
Obsoletes:      numpy-f2py < 1:1.10.1-3

%description -n python3-numpy-f2py
This package includes a version of f2py that works properly with NumPy.

%package -n python3-numpy-doc
Summary:	Documentation for numpy
Requires:	python3-numpy = %{epoch}:%{version}-%{release}
BuildArch:	noarch

%description -n python3-numpy-doc
This package provides the complete documentation for NumPy.


%prep
%autosetup -n %{name}-%{version} -p1

# openblas is provided by flexiblas by default; otherwise,
# Use openblas pthreads as recommended by upstream (see comment in site.cfg.example)
cat >> site.cfg <<EOF
[openblas]
libraries = %{blaslib}%{blasvar}
library_dirs = %{_libdir}
EOF

%if 0%{?fedora}
# Unbundle libdivide
sed -i 's,"numpy/libdivide/libdivide.h",<libdivide.h>,' \
    numpy/_core/src/umath/loops.c.src
%endif

%generate_buildrequires
%pyproject_buildrequires -R -Csetup-args=-Dblas=flexiblas -Csetup-args=-Dlapack=lapack

%build
%set_build_flags
# Allow libdivide to use vector instructions where possible
%ifarch x86_64
%if 0%{?rhel} > 9
# x86_64-v3
sed -i '/libdivide\.h/i#define LIBDIVIDE_AVX2' numpy/_core/src/umath/loops.c.src
%else
# x86_64-v1 or x86_64-v2
sed -i '/libdivide\.h/i#define LIBDIVIDE_SSE2' numpy/_core/src/umath/loops.c.src
%endif
%elifarch aarch64
sed -i '/libdivide\.h/i#define LIBDIVIDE_NEON' numpy/_core/src/umath/loops.c.src
%endif

#fix flags for ELN ppc64le
%if 0%{?rhel} >= 10
%ifarch ppc64le
find . -type f -print0 | xargs -0 sed -i s/mcpu=power8/mcpu=power9/
%endif
%endif

%pyproject_wheel -Csetup-args=-Dblas=flexiblas -Csetup-args=-Dlapack=lapack -Ccompile-args=-v

%install
mkdir docs
pushd docs
unzip %{SOURCE1}
popd

%pyproject_install
pushd %{buildroot}%{_bindir} &> /dev/null
ln -s f2py f2py3
ln -s f2py f2py%{python3_version}
ln -s f2py3 f2py.numpy
popd &> /dev/null

#symlink for includes, BZ 185079
mkdir -p %{buildroot}%{_includedir}
ln -s %{python3_sitearch}/%{name}/_core/include/numpy/ %{buildroot}%{_includedir}/numpy

%if 0%{?fedora}
rm %{buildroot}%{python3_sitearch}/numpy/_core/include/numpy/random/libdivide.h
%endif

%check
%if %{with tests}
export PYTHONPATH=%{buildroot}%{python3_sitearch}
# test_ppc64_ibm_double_double128 is unnecessary now that ppc64le has switched long doubles to IEEE format.
# https://github.com/numpy/numpy/issues/21094
%ifarch %{ix86}
# Weird RuntimeWarnings on i686, similar to https://github.com/numpy/numpy/issues/13173
# Some tests also overflow on 32bit
%global ix86_k and not test_vector_matrix_values and not test_matrix_vector_values and not test_identityless_reduction_huge_array and not (TestKind and test_all)
%endif
%ifarch riscv64
# These two tests will always fail in RISC-V
# See https://github.com/numpy/numpy/pull/25246
# Patch from http://fedora.riscv.rocks:3000/rpms/numpy/commit/b34bc42e3455b5b070d96e041ef0a5303bdc8f6c
%global riscv64_k and not test_fpclass and not test_fp_noncontiguous and not (TestBoolCmp and test_float)
%endif
# test_deprecate_... fail on Python 3.13+ due to docstrings being dedented
# Upstream has removed the tests in git HEAD.
%if v"0%{python3_version}" >= v"3.13"
%global py313_k and not test_deprecate_help_indentation and not test_deprecate_preserve_whitespace
%endif
%ifnarch %{ix86}
python3 runtests.py --no-build -- -ra -k 'not test_ppc64_ibm_double_double128 %{?ix86_k} %{?riscv64_k} %{?py313_k}' \
                                  -W "ignore:pkg_resources is deprecated as an API::pkg_resources"
%endif

%endif


%files -n python3-numpy
%license LICENSE.txt
%doc THANKS.txt
%{python3_sitearch}/%{name}/__pycache__
%{_bindir}/numpy-config
%dir %{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}/*.py*
%{python3_sitearch}/%{name}/char
%{python3_sitearch}/%{name}/ctypeslib
%{python3_sitearch}/%{name}/core
%{python3_sitearch}/%{name}/doc
%{python3_sitearch}/%{name}/fft
%{python3_sitearch}/%{name}/lib
%{python3_sitearch}/%{name}/linalg
%{python3_sitearch}/%{name}/ma
%{python3_sitearch}/%{name}/random
%{python3_sitearch}/%{name}/rec
%{python3_sitearch}/%{name}/strings
%{python3_sitearch}/%{name}/testing
%{python3_sitearch}/%{name}/tests
%{python3_sitearch}/%{name}/matrixlib
%{python3_sitearch}/%{name}/polynomial
%{python3_sitearch}/%{name}-*.dist-info
%{_includedir}/numpy
%{python3_sitearch}/%{name}/__init__.pxd
%{python3_sitearch}/%{name}/__init__.cython-30.pxd
%{python3_sitearch}/%{name}/py.typed
%{python3_sitearch}/%{name}/typing/
%{python3_sitearch}/%{name}/_core/
%{python3_sitearch}/%{name}/_pyinstaller/
%{python3_sitearch}/%{name}/_typing/
%{python3_sitearch}/%{name}/_utils/

%files -n python3-numpy-f2py
%{_bindir}/f2py
%{_bindir}/f2py3
%{_bindir}/f2py.numpy
%{_bindir}/f2py%{python3_version}
%{python3_sitearch}/%{name}/f2py

%files -n python3-numpy-doc
%doc docs/*


%changelog
<<<<<<< HEAD
* Thu Jul 24 2025 Gwyn Ciesla <gwync@protonmail.com> - 1:2.3.2-1
- 2.3.2

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jun 20 2025 Gwyn Ciesla <gwync@protonmail.com> - 1:2.3.1-1
- 2.3.1

* Mon Jun 16 2025 Gwyn Ciesla <gwync@protonmail.com> - 1:2.3.0-2
- Bump EVR

* Sat Jun 07 2025 Gwyn Ciesla <gwync@protonmail.com> - 1:2.3.0-1
- 2.3.0

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1:2.2.6-2
- Rebuilt for Python 3.14

* Mon May 19 2025 Gwyn Ciesla <gwync@protonmail.com> - 1:2.2.6-1
- 2.2.6

* Sat Apr 19 2025 Gwyn Ciesla <gwync@protonmail.com> - 1:2.2.5-1
- 2.2.5

* Sun Mar 16 2025 Gwyn Ciesla <gwync@protonmail.com> - 1:2.2.4-1
- 2.2.4

* Wed Feb 12 2025 Gwyn Ciesla <gwync@protonmail.com> - 1:2.2.3-1
- 2.2.3

* Fri Jan 31 2025 Gwyn Ciesla <gwync@protonmail.com> - 1:2.2.2-2
- Relax python3-devel requirement for f2py.

* Sat Jan 18 2025 Gwyn Ciesla <gwync@protonmail.com> - 1:2.2.2-1
- 2.2.2

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 1:2.2.1-2
- Stop running RHEL code on Fedora (rhbz#2336127)

* Sat Dec 21 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:2.2.1-1
- 2.2.1

* Fri Dec 20 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:2.2.0-4
- Fix /usr/include/numpy symlink, 2333490

* Wed Dec 18 2024 Orion Poplawski <orion@nwra.com> - 1:2.2.0-3
- Make main package require f2py (rhbz#2332307)

* Tue Dec 17 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:2.2.0-2
- Tweak flags to fix build on ELN ppc64le.

* Sun Dec 08 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:2.2.0-1
- 2.2.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.26.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1:1.26.4-7
- Rebuilt for Python 3.13

* Wed Jun 05 2024 Lukáš Zaoral <lzaoral@redhat.com> - 1:1.26.4-6
- remove redundant patchelf dependency (RHEL-36334)

* Thu May 30 2024 Songsong Zhang <U2FsdGVkX1@gmail.com> - 1:1.26.4-5
- Skip failing tests in RISC-V

* Mon May 13 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:1.26.4-4
- Patch for 3.13

* Wed Apr 17 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 1:1.26.4-3
- Do not upper-bound the meson-python version

* Fri Mar 15 2024 Jerry James <loganjerry@gmail.com> - 1:1.26.4-2
- Unbundle libdivide in Fedora
- Let libdivide use vector instructions when possible

* Mon Feb 26 2024 Gwyn Ciesla <gwync@protonmail.com> - 1:1.26.4-1
- 1.26.4

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.26.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.26.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 15 2024 Miro Hrončok <mhroncok@redhat.com> - 1:1.26.2-2
- Add missing licenses to the License tag

* Tue Dec 26 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 1:1.26.2-1
- 1.26.2

* Mon Nov 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:1.26.0-2
- Fix FTBFS with Python 3.13.

* Tue Sep 19 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:1.26.0-1
- 1.26.0

* Mon Jul 31 2023 Miro Hrončok <mhroncok@redhat.com> - 1:1.24.4-2
- Backport support for Cython 3

* Tue Jul 18 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:1.24.4-1
- 1.24.4

* Wed Jul 05 2023 Scott Talbert <swt@techie.net> - 1:1.24.3-4
- Fix FTBFS with Python 3.12

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 1:1.24.3-3
- Rebuilt for Python 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1:1.24.3-2
- Bootstrap for Python 3.12

* Mon Apr 24 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:1.24.3-1
- 1.24.3

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:1.24.1-3
- migrated to SPDX license

* Fri Jan 27 2023 Pavel Simovec <psimovec@redhat.com> - 1:1.24.1-2
- Generalize documentation Source link
- Add forgotten documentation file

* Thu Jan 26 2023 Pavel Simovec <psimovec@redhat.com> - 1:1.24.1-1
- Update to 1.24.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.23.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Charalampos Stratakis <cstratak@redhat.com> - 1:1.23.5-1
- Update to 1.23.5

* Fri Oct 21 2022 Miro Hrončok <mhroncok@redhat.com> - 1:1.23.4-1
- Update to 1.23.4
- Use distutils from setuptools to build the package

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.22.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Miro Hrončok <mhroncok@redhat.com> - 1:1.22.0-6
- GenericAlias fixes for Python 3.11.0b4+

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1:1.22.0-5
- Rebuilt for Python 3.11

* Mon Mar 07 2022 Karolina Surma <ksurma@redhat.com> - 1:1.22.0-4
- Work around the test failures with setuptools >= 60.x by using the Python's
  standard library distutils
- Build numpy using Python's standard library distutils

* Sat Feb 19 2022 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1:1.22.0-3
- Re-enable tests

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:1.22.0-1
- 1.22.0

* Wed Dec 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 1:1.21.5-1
- 1.21.5

* Thu Aug 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 1:1.21.1-1
- 1.21.1, disabing tests as they depend on .coveragerc, not shipped.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.20.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 1:1.20.1-4
- Rebuilt for Python 3.10

* Fri May 07 2021 Gwyn Ciesla <gwync@protonmail.com> - 1:1.20.1-3
- Python 3.10 fix.
- Xfail TestCond.test_nan.

* Fri Feb 12 2021 Nikola Forró <nforro@redhat.com> - 1:1.20.1-2
- Fix build requirements, hypothesis is a test dependency

* Mon Feb 08 2021 Gwyn Ciesla <gwync@protonmail.com> 1:1.20.1-1
- 1.21.1

* Mon Feb 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 1:1.20.0-1
- 1.20.0 final.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.20.0-0.2.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Nikola Forró <nforro@redhat.com> - 1:1.20.0-0.1.rc2
- Generate the main dispatcher config header into the build dir

* Mon Dec 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.20.0-0.rc2
- 1.20.0 rc2

* Tue Nov 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.19.4-1
- 1.19.4

* Thu Oct 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.19.3-1
- 1.19.3

* Tue Oct 27 2020 Nikola Forró <nforro@redhat.com> - 1:1.19.2-2
- Make test suite work in FIPS (140-2) Mode

* Thu Sep 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.19.2-1
- 1.19.2

* Sun Aug 16 2020 Iñaki Úcar <iucar@fedoraproject.org> - 1:1.19.1-3
- https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.19.1-1
- 1.19.1

* Thu Jul 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.19.0-2
- Assume old-style numpy provides from python2-numpy

* Mon Jun 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.19.0-1
- 1.19.0 final.

* Mon Jun 01 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.19.0-0.rc2
- 1.19.0 rc2

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 1:1.18.4-3
- Rebuilt for Python 3.9

* Fri May 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.18.4-2
- Own __pycache__ dir, 1833392

* Sun May 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.18.4-1
- 1.18.4

* Mon Apr 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.18.3-1
- 1.18.3

* Wed Mar 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.18.2-1
- 1.18.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1:1.18.1-1
- 1.18.1

* Mon Dec 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 1:1.18.0-1
- 1.18.0

* Mon Nov 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1:1.17.4-2
- Backport patch for s390x failures
- Enable non-broken tests on ppc64le

* Mon Nov 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 1:1.17.4-1
- 1.17.4

* Fri Oct 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 1:1.17.3-1
- 1.17.3

* Sat Sep 07 2019 Gwyn Ciesla <gwync@protonmail.com> - 1:1.17.2-1
- 1.17.2

* Thu Aug 29 2019 Gwyn Ciesla <gwync@protonmail.com> - 1:1.17.1-1
- 1.17.1

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1:1.17.0-3
- Rebuilt for Python 3.8

* Thu Aug 01 2019 Miro Hrončok <mhroncok@redhat.com> - 1:1.17.0-2
- Reintroduce libnpymath.a (#1735674)

* Tue Jul 30 2019 Gwyn Ciesla <gwync@protonmail.com> 1:1.17.0-1
- 1.17.0, split out Python 2.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.16.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Kalev Lember <klember@redhat.com> - 1:1.16.4-2
- Avoid hardcoding /usr prefix

* Tue May 28 2019 Gwyn Ciesla <gwync@protonmail.com> - 1:1.16.4-1
- 1.16.4

* Thu May 16 2019 Orion Poplawski <orion@nwra.com> - 1:1.16.3-2
- Build only with openblasp (bugz#1709161)

* Mon Apr 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 1:1.16.3-1
- 1.16.3.

* Tue Feb 26 2019 Gwyn Ciesla <gwync@protonmail.com> - 1:1.16.2-1
- 1.16.2.

* Fri Feb 01 2019 Gwyn Ciesla <limburgher@gmail.com> - 1:1.16.1-1
- 1.16.1.

* Tue Jan 22 2019 Gwyn Ciesla <limburgher@gmail.com> - 1:1.16.0-1
- 1.16.0.

* Wed Aug 29 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1:1.15.1-2
- Switch to pytest for running tests during check
- Stop ignoring failures when running tests
- Set PATH in check so that f2py tests work
- Update docs to match release
- Remove outdated workaround from rhbz#849713

* Wed Aug 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1:1.15.1-1
- Update to latest version

* Sat Aug 11 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1:1.15.0-2
- Fix broken build on s390x
- Remove bytecode produced by pytest
- Re-enable tests on s390x

* Tue Jul 24 2018 Gwyn Ciesla <limburgher@gmail.com> - 1:1.15.0-1
- 1.15.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.14.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 1:1.14.5-2
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Gwyn Ciesla <limburgher@gmail.com> - 1:1.14.5-1
- 1.14.5

* Tue May 01 2018 Gwyn Ciesla <limburgher@gmail.com> - 1:1.14.3-1
- 1.14.3

* Mon Mar 12 2018 Gwyn Ciesla <limburgher@gmail.com> - 1:1.14.2-1
- 1.14.2

* Wed Feb 21 2018 Gwyn Ciesla <limburgher@gmail.com> - 1:1.14.1-1
- 1.14.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.14.0-0.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Gwyn Ciesla <limburgher@gmail.com> - 1:1.14.0-0.rc1
- 1.14.0 rc1

* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1:1.13.3-5
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Nov 16 2017 Gwyn Ciesla <limburgher@gmail.com> - 1:1.13.3-4
- Split out doc subpackage.

* Mon Nov 06 2017 Merlin Mathesius <mmathesi@redhat.com> - 1:1.13.3-3
- Cleanup spec file conditionals

* Tue Oct 31 2017 Christian Dersch <lupinix@mailbox.org> - 1:1.13.3-2
- set proper environment variables for openblas

* Wed Oct 04 2017 Gwyn Ciesla <limburgher@gmail.com> - 1:1.13.3-1
- 1.13.3

* Thu Sep 28 2017 Gwyn Ciesla <limburgher@gmail.com> - 1:1.13.2-1
- 1.13.2

* Tue Aug 08 2017 Gwyn Ciesla <limburgher@gmail.com> - 1:1.13.1-4
- Use openblas where available, BZ 1472318.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Gwyn Ciesla <limburgher@gmail.com> - 1:1.13.1-1
- 1.13.1 final

* Fri Jun 09 2017 Gwyn Ciesla <limburgher@gmail.com> - 1:1.13.0-1
- 1.13.0 final

* Fri May 19 2017 Gwyn Ciesla <limburgher@gmail.com> - 1:1.13.0-0.rc2
- 1.13.0 rc2

* Thu May 11 2017 Gwyn Ciesla <limburgher@gmail.com> - 1:1.13.0-0.rc1
- 1.13.0 rc1

* Wed Mar 29 2017 Gwyn Ciesla <limburgher@gmail.com> - 1:1.12.1-1
- 1.12.1

* Tue Jan 31 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.0-1
- Update to 1.12.0, build with gcc 7.0.

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 1:1.11.2-2
- Rebuild for Python 3.6

* Mon Oct 3 2016 Orion Poplawski <orion@cora.nwra.com> - 1:1.11.2-1
- Update to 1.11.2 final

* Thu Sep 15 2016 Jon Ciesla <limburgher@gmail.com> - 1:1.11.2-0.rc1
- Update to 1.11.2rc1, BZ 1340440.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.11.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Orion Poplawski <orion@cora.nwra.com> - 1:1.11.1-1
- Update to 1.11.1 final

* Tue Jun 07 2016 Jon Ciesla <limburgher@gmail.com> - 1:1.11.1-0.rc1
- Update to 1.11.1rc1, BZ 1340440.

* Mon Mar 28 2016 Orion Poplawski <orion@cora.nwra.com> - 1:1.11.0-4
- Update to 1.11.0 final

* Wed Mar 23 2016 Orion Poplawski <orion@cora.nwra.com> - 1:1.11.0-3.rc2
- Update to 1.11.0rc2

* Sun Mar  6 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1:1.11.0-2.b3
- Bump Release. 1b2 is higher than 0b3

* Wed Feb 10 2016 Jon Ciesla <limburgher@gmail.com> - 1:1.11.0-0.b3
- Update to 1.11.0b2, BZ 1306249.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.11.0-1b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Jon Ciesla <limburgher@gmail.com> - 1:1.11.0-0.b2
- Update to 1.11.0b2, BZ 1303387.

* Tue Jan 26 2016 Jon Ciesla <limburgher@gmail.com> - 1:1.11.0-020161016.cc2b04git
- Update to git snapshot (due to build issue) after 1.11.0b1, BZ 1301943.

* Thu Jan 07 2016 Jon Ciesla <limburgher@gmail.com> - 1:1.10.4-1
- Update to 1.10.4, BZ 1296509.

* Tue Dec 15 2015 Jon Ciesla <limburgher@gmail.com> - 1:1.10.2-1
- Update to 1.10.2, BZ 1291674.

* Tue Dec 08 2015 Jon Ciesla <limburgher@gmail.com> - 1:1.10.2-0.2.rc2
- Update to 1.10.2rc1, BZ 1289550.

* Fri Nov 13 2015 Orion Poplawski <orion@cora.nwra.com> - 1:1.10.2-0.1.rc1
- Update to 1.10.2rc1
- Drop opt-flags patch applied upstream

* Fri Nov 13 2015 Kalev Lember <klember@redhat.com> - 1:1.10.1-6
- Add provides to satisfy numpy%%{_isa} requires in other packages

* Thu Nov 12 2015 Orion Poplawski <orion@nwra.com> - 1:1.10.1-5
- Re-add provides f2py

* Thu Nov 12 2015 Kalev Lember <klember@redhat.com> - 1:1.10.1-4
- Fix obsoletes / provides for numpy -> python2-numpy rename

* Wed Oct 14 2015 Thomas Spura <tomspur@fedoraproject.org> - 1:1.10.1-3
- Remove fortran flags or arm would build with -march=x86-64

* Wed Oct 14 2015 Thomas Spura <tomspur@fedoraproject.org> - 1:1.10.1-2
- Provide python2-* packages
- Run tests with verbose=2

* Tue Oct 13 2015 Jon Ciesla <limburgher@gmail.com> - 1:1.10.1-1
- Update to 1.10.1, BZ 1271022.

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 1:1.10.0-2
- Rebuilt for Python3.5 rebuild

* Tue Oct 06 2015 Jon Ciesla <limburgher@gmail.com> - 1:1.10.0-1
- Update to 1.10.0 final.

* Wed Sep 02 2015 Jon Ciesla <limburgher@gmail.com> - 1:1.10.0-0.b1
- Update to 1.10.0b1, BZ 1252641.

* Thu Aug 13 2015 Orion Poplawski <orion@nwra.com> - 1:1.9.2-3
- Add python2-numpy provides (bug #1249423)
- Spec cleanup

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 1 2015 Orion Poplawski <orion@nwra.com> - 1:1.9.2-1
- Update to 1.9.2

* Tue Jan 6 2015 Orion Poplawski <orion@nwra.com> - 1:1.9.1-2
- Add upstream patch to fix xerbla linkage (bug #1172834)

* Tue Nov 04 2014 Jon Ciesla <limburgher@gmail.com> - 1:1.9.1-1
- Update to 1.9.1, BZ 1160273.

* Sun Sep 7 2014 Orion Poplawski <orion@nwra.com> - 1:1.9.0-1
- Update to 1.9.0

* Wed Aug 27 2014 Orion Poplawski <orion@nwra.com> - 1:1.9.0-0.1.rc1
- Update to 1.9.0rc1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug 10 2014 Orion Poplawski <orion@nwra.com> - 1:1.8.2-1
- Update to 1.8.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 9 2014 Orion Poplawski <orion@nwra.com> - 1:1.8.1-3
- Rebuild for Python 3.4

* Wed May 07 2014 Jaromir Capik <jcapik@redhat.com> - 1:1.8.1-2
- Fixing FTBFS on ppc64le (#1078354)

* Tue Mar 25 2014 Orion Poplawski <orion@nwra.com> - 1:1.8.1-1
- Update to 1.8.1

* Tue Mar 4 2014 Orion Poplawski <orion@nwra.com> - 1:1.8.0-5
- Fix __pycache__ ownership (bug #1072467)

* Mon Feb 10 2014 Thomas Spura <tomspur@fedoraproject.org> - 1:1.8.0-4
- Fix CVE-2014-1858, CVE-2014-1859: #1062009, #1062359

* Mon Nov 25 2013 Orion Poplawski <orion@nwra.com> - 1:1.8.0-3
- Ship doc module (bug #1034357)

* Wed Nov 6 2013 Orion Poplawski <orion@nwra.com> - 1:1.8.0-2
- Move f2py documentation to f2py package (bug #1027394)

* Wed Oct 30 2013 Orion Poplawski <orion@nwra.com> - 1:1.8.0-1
- Update to 1.8.0 final

* Mon Oct 14 2013 Orion Poplawski <orion@nwra.com> - 1:1.8.0-0.7.rc2
- Update to 1.8.0rc2
- Create clean site.cfg
- Use serial atlas

* Mon Sep 23 2013 Orion Poplawski <orion@nwra.com> - 1:1.8.0-0.6.b2
- Add [atlas] to site.cfg for new atlas library names

* Sun Sep 22 2013 Orion Poplawski <orion@nwra.com> - 1:1.8.0-0.5.b2
- Update site.cfg for new atlas library names

* Sat Sep 21 2013 David Tardon <dtardon@redhat.com> - 1:1.8.0-0.4.b2
- rebuild for atlas 3.10

* Tue Sep 10 2013 Jon Ciesla <limburgher@gmail.com> - 1:1.8.0-0.3.b2
- Fix libdir path in site.cfg, BZ 1006242.

* Sun Sep 8 2013 Orion Poplawski <orion@nwra.com> - 1:1.8.0-0.2.b2
- Update to 1.8.0b2

* Wed Sep 4 2013 Orion Poplawski <orion@nwra.com> - 1:1.8.0-0.1.b1
- Update to 1.8.0b1
- Drop f2py patch applied upstream

* Tue Aug 27 2013 Jon Ciesla <limburgher@gmail.com> - 1:1.7.1-5
- URL Fix, BZ 1001337

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Tomas Tomecek <ttomecek@redhat.com> - 1:1.7.1-3
- Fix rpmlint warnings
- Update License
- Apply patch: change shebang of f2py to use binary directly

* Sun Jun 2 2013 Orion Poplawski <orion@nwra.com> - 1:1.7.1-2
- Specfile cleanup (bug #969854)

* Wed Apr 10 2013 Orion Poplawski <orion@nwra.com> - 1:1.7.1-1
- Update to 1.7.1

* Sat Feb 9 2013 Orion Poplawski <orion@nwra.com> - 1:1.7.0-1
- Update to 1.7.0 final

* Sun Dec 30 2012 Orion Poplawski <orion@nwra.com> - 1:1.7.0-0.5.rc1
- Update to 1.7.0rc1

* Thu Sep 20 2012 Orion Poplawski <orion@nwra.com> - 1:1.7.0-0.4.b2
- Update to 1.7.0b2
- Drop patches applied upstream

* Wed Aug 22 2012 Orion Poplawski <orion@nwra.com> - 1:1.7.0-0.3.b1
- Add patch from github pull 371 to fix python 3.3 pickle issue
- Remove cython .c source regeneration - fails now

* Wed Aug 22 2012 Orion Poplawski <orion@nwra.com> - 1:1.7.0-0.2.b1
- add workaround for rhbz#849713 (fixes FTBFS)

* Tue Aug 21 2012 Orion Poplawski <orion@cora.nwra.com> - 1:1.7.0-0.1.b1
- Update to 1.7.0b1
- Rebase python 3.3 patchs to current git master
- Drop patches applied upstream

* Sun Aug  5 2012 David Malcolm <dmalcolm@redhat.com> - 1:1.6.2-5
- rework patches for 3.3 to more directly reflect upstream's commits
- re-enable test suite on python 3
- forcibly regenerate Cython .c source to avoid import issues on Python 3.3

* Sun Aug  5 2012 Thomas Spura <tomspur@fedoraproject.org> - 1:1.6.2-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3
- needs unicode patch

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 1:1.6.2-3
- remove rhel logic from with_python3 conditional

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 20 2012 Orion Poplawski <orion@cora.nwra.com> - 1:1.6.2-1
- Update to 1.6.2 final

* Sat May 12 2012 Orion Poplawski <orion@cora.nwra.com> - 1:1.6.2rc1-0.1
- Update to 1.6.2rc1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 7 2011 Orion Poplawski <orion@cora.nwra.com> - 1:1.6.1-1
- Update to 1.6.1

* Fri Jun 17 2011 Jon Ciesla <limb@jcomserv.net> - 1:1.6.0-2
- Bump and rebuild for BZ 712251.

* Mon May 16 2011 Orion Poplawski <orion@cora.nwra.com> - 1:1.6.0-1
- Update to 1.6.0 final

* Mon Apr 4 2011 Orion Poplawski <orion@cora.nwra.com> - 1:1.6.0-0.2.b2
- Update to 1.6.0b2
- Drop import patch fixed upstream

* Thu Mar 31 2011 Orion Poplawski <orion@cora.nwra.com> - 1:1.6.0-0.1.b1
- Update to 1.6.0b1
- Build python3  module with python3
- Add patch from upstream to fix build time import error

* Wed Mar 30 2011 Orion Poplawski <orion@cora.nwra.com> - 1:1.5.1-1
- Update to 1.5.1 final

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.5.1-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Dan Horák <dan[at]danny.cz> - 1:1.5.1-0.3
- fix the AttributeError during tests
- fix build on s390(x)

* Wed Dec 29 2010 David Malcolm <dmalcolm@redhat.com> - 1:1.5.1-0.2
- rebuild for newer python3

* Wed Oct 27 2010 Thomas Spura <tomspur@fedoraproject.org> - 1:1.5.1-0.1
- update to 1.5.1rc1
- add python3 subpackage
- some spec-cleanups

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1:1.4.1-6
- actually add the patch this time

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1:1.4.1-5
- fix segfault within %%check on 2.7 (patch 2)

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1:1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 18 2010 Dan Horák <dan[at]danny.cz> 1.4.1-3
- ignore the "Ticket #1299 second test" failure on s390(x)

* Thu Jun 24 2010 Jef Spaleta <jspaleta@fedoraprject.org> 1.4.1-2
- source commit fix

* Thu Jun 24 2010 Jef Spaleta <jspaleta@fedoraprject.org> 1.4.1-1
- New upstream release. Include backported doublefree patch

* Mon Apr 26 2010 Jon Ciesla <limb@jcomserv.net> 1.3.0-8
- Moved distutils back to the main package, BZ 572820.

* Thu Apr 08 2010 Jon Ciesla <limb@jcomserv.net> 1.3.0-7
- Reverted to 1.3.0 after upstream pulled 1.4.0, BZ 579065.

* Tue Mar 02 2010 Jon Ciesla <limb@jcomserv.net> 1.4.0-5
- Linking /usr/include/numpy to .h files, BZ 185079.

* Tue Feb 16 2010 Jon Ciesla <limb@jcomserv.net> 1.4.0-4
- Re-enabling atlas BR, dropping lapack Requires.

* Wed Feb 10 2010 Jon Ciesla <limb@jcomserv.net> 1.4.0-3
- Since the previous didn't work, Requiring lapack.

* Tue Feb 09 2010 Jon Ciesla <limb@jcomserv.net> 1.4.0-2
- Temporarily dropping atlas BR to work around 562577.

* Fri Jan 22 2010 Jon Ciesla <limb@jcomserv.net> 1.4.0-1
- 1.4.0.
- Dropped ARM patch, ARM support added upstream.

* Tue Nov 17 2009 Jitesh Shah <jiteshs@marvell.com> - 1.3.0-6.fa1
- Add ARM support

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 11 2009 Jon Ciesla <limb@jcomserv.net> 1.3.0-5
- Fixed atlas BR, BZ 505376.

* Fri Apr 17 2009 Jon Ciesla <limb@jcomserv.net> 1.3.0-4
- EVR bump for pygame chainbuild.

* Fri Apr 17 2009 Jon Ciesla <limb@jcomserv.net> 1.3.0-3
- Moved linalg, fft back to main package.

* Tue Apr 14 2009 Jon Ciesla <limb@jcomserv.net> 1.3.0-2
- Split out f2py into subpackage, thanks Peter Robinson pbrobinson@gmail.com.

* Tue Apr 07 2009 Jon Ciesla <limb@jcomserv.net> 1.3.0-1
- Update to latest upstream.
- Fixed Source0 URL.

* Thu Apr 02 2009 Jon Ciesla <limb@jcomserv.net> 1.3.0-0.rc1
- Update to latest upstream.

* Thu Mar 05 2009 Jon Ciesla <limb@jcomserv.net> 1.2.1-3
- Require python-devel, BZ 488464.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 19 2008 Jon Ciesla <limb@jcomserv.net> 1.2.1-1
- Update to 1.2.1.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.2.0-2
- Rebuild for Python 2.6

* Tue Oct 07 2008 Jon Ciesla <limb@jcomserv.net> 1.2.0-1
- New upstream release, added python-nose BR. BZ 465999.
- Using atlas blas, not blas-devel. BZ 461472.

* Wed Aug 06 2008 Jon Ciesla <limb@jcomserv.net> 1.1.1-1
- New upstream release

* Thu May 29 2008 Jarod Wilson <jwilson@redhat.com> 1.1.0-1
- New upstream release

* Tue May 06 2008 Jarod Wilson <jwilson@redhat.com> 1.0.4-1
- New upstream release

* Mon Feb 11 2008 Jarod Wilson <jwilson@redhat.com> 1.0.3.1-2
- Add python egg to %%files on f9+

* Wed Aug 22 2007 Jarod Wilson <jwilson@redhat.com> 1.0.3.1-1
- New upstream release

* Wed Jun 06 2007 Jarod Wilson <jwilson@redhat.com> 1.0.3-1
- New upstream release

* Mon May 14 2007 Jarod Wilson <jwilson@redhat.com> 1.0.2-2
- Drop BR: atlas-devel, since it just provides binary-compat
  blas and lapack libs. Atlas can still be optionally used
  at runtime. (Note: this is all per the atlas maintainer).

* Mon May 14 2007 Jarod Wilson <jwilson@redhat.com> 1.0.2-1
- New upstream release

* Tue Apr 17 2007 Jarod Wilson <jwilson@redhat.com> 1.0.1-4
- Update gfortran patch to recognize latest gfortran f95 support
- Resolves rhbz#236444

* Fri Feb 23 2007 Jarod Wilson <jwilson@redhat.com> 1.0.1-3
- Fix up cpuinfo bug (#229753). Upstream bug/change:
  http://projects.scipy.org/scipy/scipy/ticket/349

* Thu Jan 04 2007 Jarod Wilson <jwilson@redhat.com> 1.0.1-2
- Per discussion w/Jose Matos, Obsolete/Provide f2py, as the
  stand-alone one is no longer supported/maintained upstream

* Wed Dec 13 2006 Jarod Wilson <jwilson@redhat.com> 1.0.1-1
- New upstream release

* Tue Dec 12 2006 Jarod Wilson <jwilson@redhat.com> 1.0-2
- Rebuild for python 2.5

* Wed Oct 25 2006 Jarod Wilson <jwilson@redhat.com> 1.0-1
- New upstream release

* Wed Sep 06 2006 Jarod Wilson <jwilson@redhat.com> 0.9.8-1
- New upstream release

* Wed Apr 26 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.9.6-1
- Upstream update

* Thu Feb 16 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.9.5-1
- Upstream update

* Mon Feb 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.9.4-2
- Rebuild for Fedora Extras 5

* Thu Feb  2 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 0.9.4-1
- Initial RPM release
- Added gfortran patch from Neal Becker
