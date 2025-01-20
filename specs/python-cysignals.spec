%global	modname	cysignals

# Python files are installed into nonstandard locations
%global _python_bytecompile_extra 0

# Install documentation in the main package directory
%global _docdir_fmt %{name}

Name:		python-%{modname}
Version:	1.11.4
Release:	7%{?dist}
Summary:	Interrupt and signal handling for Cython
License:	LGPL-3.0-or-later
URL:		https://github.com/sagemath/cysignals
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{modname}-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	pari-devel
# https://bugzilla.redhat.com/show_bug.cgi?id=1445411#c2
Patch0:		%{name}-gdb.patch
# Linux already clears the FPU state
Patch1:		%{name}-emms.patch
# Fix underlinked signals.so
Patch2:		%{name}-underlink.patch
# Do not fail if cysignals_crash_logs cannot be created
Patch3:		%{name}-crash-logs.patch
# Remove workaround for Cython bug that is already fixed in Fedora
Patch4:		%{name}-sigismember.patch

%global _description %{expand:
When writing Cython code, special care must be taken to ensure that the
code can be interrupted with CTRL-C. Since Cython optimizes for speed,
Cython normally does not check for interrupts. For example, code like
the following cannot be interrupted in Cython:

while True:
    pass

The cysignals package provides mechanisms to handle interrupts
(and other signals and errors) in Cython code.

See http://cysignals.readthedocs.org/ for the full documentation.}

%description	%{_description}

%package	-n python3-%{modname}
Summary:	%{summary}
BuildRequires:	python3-devel

%description	-n python3-%{modname} %{_description}

%package	-n python3-%{modname}-devel
Summary:	%{summary} headers files
Requires:	python3-%{modname}%{?_isa} = %{version}-%{release}
Requires:	pari-devel

%description	-n python3-%{modname}-devel %{_description}

%package	doc
Summary:	Documentation for %{name}
BuildRequires:	python3-docs
BuildRequires:	%{py3_dist sphinx}
BuildArch:	noarch

%description	doc
Documentation and examples for %{name}.

%prep
%autosetup -p0 -n %{modname}-%{version}

# Use local objects.inv for intersphinx
sed -i "s|'https://docs\.python\.org/3', None|'https://docs.python.org/3', '%{_docdir}/python3-docs/html/objects.inv'|" docs/source/conf.py

# Build for python 3
sed -i 's/language_level=2/language_level=3/' setup.py

# The doctest timeout is sometimes too short for 32-bit builders
sed -i 's/600/2400/' rundoctests.py

# Upstream does not generate the configure script
autoreconf -fi .

%generate_buildrequires
%pyproject_buildrequires

%build
%configure
%pyproject_wheel

# Build the documentation
export PYTHONPATH=$PWD/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}
make -C docs html
rst2html --no-datestamp README.rst README.html

%install
%pyproject_install
%pyproject_save_files cysignals
rm docs/build/html/.buildinfo

%check
PATH=%{buildroot}%{_bindir}:$PATH
PYTHONPATH=%{buildroot}%{python3_sitearch}
export PATH PYTHONPATH
%{python3} rundoctests.py src/cysignals/*.pyx

%files		-n python3-%{modname} -f %{pyproject_files}
%doc README.html
%{_bindir}/%{modname}-CSI
%{_datadir}/%{modname}/
%exclude %{python3_sitearch}/%{modname}/*.h
%exclude %{python3_sitearch}/%{modname}/*.pxd

%files		-n python3-%{modname}-devel
%{python3_sitearch}/%{modname}/*.h
%{python3_sitearch}/%{modname}/*.pxd

%files		doc
%doc docs/build/html

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Oct  5 2024 Jerry James <loganjerry@gmail.com> - 1.11.4-6
- Rebuild for pari 2.17.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.11.4-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Jerry James <loganjerry@gmail.com> - 1.11.4-1
- Version 1.11.4
- Drop upstreamed fortify patch
- Automatically generate BuildRequires

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.11.2-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.11.2-4
- Rebuild for pari 2.15.0
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.11.2-2
- Rebuilt for Python 3.11

* Thu Mar 17 2022 Jerry James <loganjerry@gmail.com> - 1.11.2-1
- Version 1.11.2
- Drop upstreamed -minsigstksz patch

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 1.10.3-1
- Version 1.10.3
- Add -minsigstksz patch to fix FTBFS (bz 1935643)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.10.2-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov  9 2020 Jerry James <loganjerry@gmail.com> - 1.10.2-10
- Rebuild for pari 2.13.0
- Add pari-devel R to -devel subpackage
- Increase doctest timeout

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Jerry James <loganjerry@gmail.com> - 1.10.2-5
- Do not try to write to an unwritable directory (bz 1751021)
- Fix cross-references in the documentation

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Jerry James <loganjerry@gmail.com> - 1.10.2-1
- New upstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Jerry James <loganjerry@gmail.com> - 1.8.1-1
- New upstream release
- Drop python2 subpackages (bz 1663842)

* Fri Aug 10 2018 Jerry James <loganjerry@gmail.com> - 1.7.2-1
- New upstream release (bz 1601237)
- Drop upstreamed -import patch
- The Cython libraries are used at runtime, so add Requires

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.1-2
- Rebuilt for Python 3.7

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 1.7.1-1
- New upstream version for sagemath 8.2 (bz 1473458)
- Add -fortify, -import, and -underlink patches

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.6.4-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Nov 08 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6.2-1
- Update to version required by sagemath 8.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 27 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.2-3
- Correct mixed tabs and spaces in the spec (#1445411#c5)

* Wed Apr 26 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.2-2
- Remove python preloading (#1445411#c2)
- Add python provides to python3 subpackage (#1445411#c3)
- Add changelog section (#1445411#c3)
- Add URL tag (#1445411#c3)
- Correct license to LGPLv3+ (#1445411#c3)
- Change doc subpackage to noarch
- Correct owner of documentation directory (#1445411#c3)
- Do not call the emms instruction on x86 (#1445411#c3)
- Do not install .buildinfo file in doc subpackage (#1445411#c3)
- Correct problems in python3 tests in %%check due to Popen python
- Install a python 2 or 3 specific cysignals-CSI
- Add requires to the LICENSE file in the doc subpackage (#1445411#c3)

* Wed Apr 26 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.3.2-1
- Initial python-cysignals spec.
