%global srcname pyopencl

Name:           python-%{srcname}
Version:        2022.3
Release:        1%{?dist}
Summary:        Python wrapper for OpenCL

# https://bugzilla.redhat.com/show_bug.cgi?id=1219819#c16
# Boost (boost):
# pyopencl/cl/pyopencl-bessel-j.cl
# pyopencl/cl/pyopencl-bessel-y.cl
# pyopencl/cl/pyopencl-eval-tbl.cl
# GPLv2 (cephes):
# pyopencl/cl/pyopencl-airy.cl
# ASL 2.0 (ranluxcl), will be removed in 2018.x:
# pyopencl/cl/pyopencl-ranluxcl.cl
# ASL 2.0:
# pyopencl/scan.py
# BSD (random123):
# pyopencl/cl/pyopencl-random123/array.h
# pyopencl/cl/pyopencl-random123/openclfeatures.h
# pyopencl/cl/pyopencl-random123/philox.cl
# pyopencl/cl/pyopencl-random123/threefry.cl
# BSD:
# pyopencl/bitonic_sort.py
# pyopencl/bitonic_sort_templates.py

License:        MIT and Boost and ASL 2.0 and GPLv2 and BSD
URL:            https://mathema.tician.de/software/pyopencl
Source0:        %{pypi_source}
Patch1:         0001-disable-executing-git-submodule.patch
# Have not asked upstream, but they want to enforce CFLAGS/LDFLAGS
Patch2:         0002-don-t-hack-distutils-with-C-LDFLAGS.patch

# pyopencl/cl/pyopencl-bessel-[j,y].cl and
# pyopencl/cl/pyopencl-eval-tbl.cl contain snippets taken from boost
# and cephes. pyopencl/cl/pyopencl-airy.cl contains code taken from
# cephes.
Provides:       bundled(boost-math)
Provides:       bundled(cephes) = 2.8
# pyopencl/cl/pyopencl-ranluxcl.cl contains a modified version of the
# ranluxcl library
Provides:       bundled(ranluxcl) = 1.3.1
# ./pyopencl/compyte/*
Provides:       bundled(compyte)

BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  opencl-headers
BuildRequires:  ocl-icd-devel
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(gl)

%description
PyOpenCL makes it possible to access GPUs and other massively\
parallel compute devices from Python. Specifically, PyOpenCL\
provides Pythonic access to the OpenCL parallel computation\
API in a manner similar to the sister project `PyCUDA`.

%package -n python3-%{srcname}
Summary:        Python 3 wrapper for OpenCL
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3dist(numpy)
Recommends:     python3dist(Mako)

%description -n python3-%{srcname}
Python 3 version of python-pyopencl.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vrf *.egg-info
rm -vf examples/download-examples-from-wiki.py

# generate html docs
#sphinx-build doc/source html
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}

%build
%{__python3} configure.py --cl-enable-gl --cl-pretend-version=1.2
%py3_build

%install
%py3_install

find %{buildroot}%{python3_sitearch}/%{srcname} -name '*.so' -exec chmod 755 {} \+

%files -n python3-%{srcname}
%license LICENSE
%doc examples
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-*.egg-info/

%changelog
* Tue Nov 22 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.3-1
- Update to v2022.3 (fixes rhbz#2144595)

* Tue Nov 15 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.2.4-1
- Update to v2022.2.4 (fixes rhbz#2134963)

* Mon Oct 03 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.2.3-1
- Update to v2022.2.3 (fixes rhbz#2125950)

* Sun Sep 11 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.2.2-1
- Update to v2022.2.2 (fixes rhbz#2125859)

* Fri Sep 09 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.2.1-1
- Update to v2022.2.1 (fixes rhbz#2125421)

* Thu Sep 08 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.2-1
- Update to v2022.2 (fixes rhbz#2125092)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.1.6-1
- Update to v2022.1.6 (fixes rhbz#2099977)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2022.1.5-2
- Rebuilt for Python 3.11

* Fri May 20 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.1.5-1
- Update to v2022.1.5

* Wed May 18 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.1.4-1
- Update to v2022.1.4

* Fri May 13 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.1.3-1
- Update to v2022.1.3

* Thu Mar 17 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.1-1
- Update to v2022.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2021.2.11-1
- Update to v2021.2.11

* Thu Dec 23 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2021.2.10-1
- Update to v2021.2.10

* Mon Nov 01 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2021.2.9-1
- Update to v2021.2.9

* Fri Oct 15 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2021.2.8-1
- Update to v2021.2.8

* Wed Aug 04 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2021.2.6-1
- Update to v2021.2.6

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2021.2.3-1
- Update to v2021.2.3

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2021.2.2-2
- Rebuilt for Python 3.10

* Mon Apr 12 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2021.2.2-1
- Update to v2021.2.2

* Mon Apr 12 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2021.1.6-1
- Update to v2021.1.6

* Mon Mar 29 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2021.1.4-1
- Update to v2021.1.4

* Thu Feb 18 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2021.1.2-1
- Update to v2021.1.2

* Thu Jan 28 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2021.1.1-1
- Update to v2021.1.1

* Tue Jan 26 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2021.1-1
- Update to v2021.1

* Tue Nov 24 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 2020.3.1-1
- Update to v2020.3.1 (RHBZ#1899285)
- Support nVidia GPUs with proprietary drivers (--cl-pretend-version=1.2) (RHBZ#1900351)

* Mon Sep 28 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 2020.2.2-1
- Update to v2020.2.2

* Thu Aug 27 2020 Iñaki Úcar <iucar@fedoraproject.org> - 2020.2.1-2
- Drop unneeded libraries

* Fri Aug 21 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 2020.2.1-1
- Update to v2020.2.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 2020.2-1
- Update to v2020.2

* Wed Jun 03 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 2020.1-1
- Update to v2020.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2019.1.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 2019.1.2-1
- Update to v2019.1.2

* Fri Nov 08 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 2018.2.5-4
- Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.2.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 09 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2018.2.5-1
- Update to 2018.2.5

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2018.1.1-3
- Drop python2 subpackage

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 2018.1.1-2
- Rebuild with fixed binutils

* Sun Jul 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2018.1.1-1
- Update to 2018.1.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2017.2.2-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2017.2.2-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sun Dec 31 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017.2.2-1
- Update to 2017.2.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Igor Gnatenko <ignatenko@redhat.com> - 2017.2-1
- Update to 2017.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Igor Gnatenko <ignatenko@redhat.com> - 2016.2.1-1
- Upate to 2016.2.1

* Tue Jan 17 2017 Than Ngo <than@redhat.com> - 2016.1-6
- fix the conditionalize tests support
- switching to gnu++11 to fix the build failure on ppc64le

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2016.1-5
- Rebuild for Python 3.6

* Wed Aug 31 2016 Igor Gnatenko <ignatenko@redhat.com> - 2016.1-4
- Update to 2016.1
- Cleanups in packaging

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2015.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2015.2-1
- Update to 2015.2
- Add some description to bundled libs providing
- Provide exact version of bundled cephes
- Force tests passed
- Fixed dependencies list

* Wed Nov 04 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2015.1-4
- Fixed license tag
- Run tests
- Add license

* Sat Oct 24 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2015.1-3
- Fix errors during review

* Sat Oct 24 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2015.1-2
- Trivial fixes in spec

* Fri May 08 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2015.1-1
- Initial package
