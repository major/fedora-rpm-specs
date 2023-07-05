%bcond_without check
%bcond_with doc

%global pkgname theano
%global pypi_name Theano-PyMC

Name:           python-%{pkgname}
Version:        1.1.2
Release:        7%{?dist}
Summary:        Mathematical expressions involving multidimensional arrays

License:        BSD
URL:            https://docs.pymc.io/PyMC3_and_Theano.html
Source0:        %pypi_source Theano-PyMC
# This file was omitted from the release, but is available from aesara
Source1:        scan_perform.pyx

# Fix the blas interface; see https://github.com/Theano/Theano/issues/6518
# If we fix the Fedora numpy package to specify flexiblas in its __config__.py
# file, we can discard this patch.
Patch0:         %{name}-blas.patch
# Fix a call to a deprecated function in the printing code
Patch1:         %{name}-printing.patch
# Workaround for linecache changes in python 3.10
Patch2:         %{name}-linecache.patch
# It's calling tt.Node instead of pydot.Node
Patch3:         %{name}-pydotnode.patch

BuildArch:      noarch

BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  pkgconfig(flexiblas)

BuildRequires:  python3-devel
BuildRequires:  python3-pygpu-devel
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist wheel}
%if %{with check}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist parameterized}
BuildRequires:  %{py3_dist filelock}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist pydot}
%endif

%global _desc %{expand:
Theano is a Python library that allows you to define, optimize, and
evaluate mathematical expressions involving multi-dimensional arrays
efficiently.  Theano features:
- tight integration with NumPy: Use numpy.ndarray in Theano-compiled
  functions.
- transparent use of a GPU: Perform data-intensive calculations up to
  140x faster than with CPU (float32 only).
- efficient symbolic differentiation: Theano does your derivatives for
  function with one or many inputs.
- speed and stability optimizations: Get the right answer for log(1+x)
  even when x is really tiny.
- dynamic C code generation: Evaluate expressions faster.
- extensive unit-testing and self-verification: Detect and diagnose many
  types of mistake.}

%description %_desc

%package -n python3-%{pkgname} 
Summary:        %{summary}
Requires:       flexiblas-devel
Requires:       gcc-c++
Requires:       gcc-gfortran
Recommends:     python%{python3_version}dist(pygpu)
Suggests:       python%{python3_version}dist(pydot)

%description -n python3-%{pkgname} %_desc

%package doc
Summary:        Theano documentation
%if %{with doc}
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
%endif

%description doc
User documentation for Theano.

%prep
%autosetup -n %{pypi_name}-%{version} -p0
cp -p %{SOURCE1} theano/scan

# We don't need to use /usr/bin/env
for fil in $(grep -FRl /bin/env .); do
  sed -ri.orig 's,( )?(/usr)?/bin/env[[:blank:]]*python.*,%{_bindir}/python3,' $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

%build
# Regenerate from cython sources
cd theano/scan
cython -3 -o c_code/scan_perform.c scan_perform.pyx
cd -

%pyproject_wheel

# Build the documentation
# Latest tarball doesn't include the conf files required to build documentation
%if %{with doc}
export PYTHONPATH=$PWD
%{python3} doc/scripts/docgen.py --nopdf
#rst2html --no-datestamp README.rst README.html
# Remove build artifacts
rm -rf html/.buildinfo html/.doctrees
%endif

%install
%pyproject_install

# Restore executable permission on the scripts
chmod a+x $(find %{buildroot} -name \*.py -o -name \*.sh | xargs grep -l '^#!')

# Do not ship the tests
rm -rf %{buildroot}%{python3_sitelib}/tests

%if %{with check}
%check
%pytest

%endif

%files -n python3-%{pkgname}
%doc DESCRIPTION.txt HISTORY.txt NEWS.txt 
%license doc/LICENSE.txt
%{_bindir}/theano-*
%{python3_sitelib}/Theano*.dist-info/
%{python3_sitelib}/theano/
%{python3_sitelib}/bin/

%files doc
%if %{with doc}
%doc html
%endif

%changelog
* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 1.1.2-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug  6 2022 Jerry James <loganjerry@gmail.com> - 1.1.2-5
- Regenerate cython sources to fix FTBFS (rhbz#2113658)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.1.2-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 1.1.2-1
- New upstream source (1.1.2)
- Drop doc patches and other patches included upstream
- No cython files in tarball
- doc subpackage is empty

* Tue Jun  8 2021 Jerry James <loganjerry@gmail.com> - 1.0.13-4
- Add -linecache patch to fix python 3.10 FTBFS (bz 1959774)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.13-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Jerry James <loganjerry@gmail.com> - 1.0.13-2
- Add -numpy-version patch to fix FTBFS (bz 1914890)

* Thu Dec 24 2020 Jerry James <loganjerry@gmail.com> - 1.0.13-1
- Version 1.0.13

* Mon Nov 23 2020 Jerry James <loganjerry@gmail.com> - 1.0.11-1
- Version 1.0.11
- Switch to the PyMC fork, now the official version
- Drop the -future-warning patch; it yields incorrect answers
- Test with pytest instead of nose

* Fri Aug  7 2020 Jerry James <loganjerry@gmail.com> - 1.0.5-1
- Version 1.0.5
- Drop upstreamed patches: -ceil-floor-trunc, -clip, -format, -gammaq,
  -has-sorted-indices, -is, -iterable, -ordered-dict, -random, -sort, -sphinx3,
  -traceback
- Add patches: -file-leak, -printing
- Build with flexiblas instead of with openblas directly

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-6.1
- Rebuilt for Python 3.9

* Tue Feb  4 2020 Jerry James <loganjerry@gmail.com> - 1.0.4-6
- Add -ordered-dict patch, thanks to Miro Hrončok (bz 1797982)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Jerry James <loganjerry@gmail.com> - 1.0.4-5
- Drop epydoc BR since it has been retired
- Unbundle fonts from the documentation
- Ship an HTML form of the README
- Add -has-sorted-indices patch

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-4.1
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 29 2019 Jerry James <loganjerry@gmail.com> - 1.0.4-4
- Add -iterable, -git, -format, -is, and -doc patches to fix warnings

* Fri Aug 23 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.4-3
- Fix FTBFS with python-theano-sort patch (#1737011)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-2.1
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Jerry James <loganjerry@gmail.com> - 1.0.4-2
- Add -future-warning, -gammaq, -ceil-floor-trunc, -traceback, -clip, and
  -random patches to fix FTBFS (bz 1737011)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 19 2019 Jerry James <loganjerry@gmail.com> - 1.0.4-1
- New upstream release

* Thu Dec 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-2
- Drop duplicated dependencies

* Sat Oct  6 2018 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- New upstream release
- Partially revert the previous commit; the gcc Requires is needed
- Build with openblas instead of atlas
- Send cython output to the correct directory
- Build with pygpu support

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-2
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-1.1
- Rebuilt for Python 3.7

* Wed May 23 2018 Jerry James <loganjerry@gmail.com> - 1.0.2-1
- New upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 22 2017 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- New upstream release
- Add -blas patch to fix compilation errors when using the blas interface
- Reenable the tests
- Pass nose flags to prevent memory exhaustion while running the tests

* Fri Nov 17 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 22 2017 Jerry James <loganjerry@gmail.com> - 0.9.0-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-1.2
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-1.1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Apr 21 2016 Jerry James <loganjerry@gmail.com> - 0.8.2-1
- New upstream release

* Fri Apr 15 2016 Jerry James <loganjerry@gmail.com> - 0.8.1-2
- Remove python2 dependency from the python3 subpackage (bz 1324232)
- Recommend pydot instead of requiring it

* Sat Apr  2 2016 Jerry James <loganjerry@gmail.com> - 0.8.1-1
- New upstream release
- Fix the pydot dependencies

* Wed Mar 23 2016 Jerry James <loganjerry@gmail.com> - 0.8.0-1
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.2.a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 0.7.1-0.1.a1
- Comply with latest python packaging guidelines

* Thu Nov 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.1-0.1.a1
- Update to 0.7.1a1

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2.2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Nov  4 2015 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7.0-2.1
- Fix python3 package requiring python2.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  1 2015 Jerry James <loganjerry@gmail.com> - 0.7.0-1
- New upstream release
- Drop upstreamed -arm patch
- Regenerate cython files to fix build failure

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 0.6.0-5
- Add -arm patch to fix build failure on arm builders due to inverted test

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 0.6.0-4
- Drop workaround for fixed bug (bz 1075826)
- Use license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Jerry James <loganjerry@gmail.com> - 0.6.0-3
- Rebuild for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Mar 13 2014 Jerry James <loganjerry@gmail.com> - 0.6.0-2
- Add python3 subpackage
- Add another icon to the -missing tarball
- Update source icons
- Unbundle python-six
- Add workaround for bz 1075826

* Sat Dec  7 2013 Jerry James <loganjerry@gmail.com> - 0.6.0-1
- New upstream release
- Drop upstreamed -import patch

* Mon Oct 21 2013 Jerry James <loganjerry@gmail.com> - 0.6.0-0.1.rc3
- Add the -import patch to fix an exception
- Add more files to the base package docs

* Tue Aug 27 2013 Jerry James <loganjerry@gmail.com> - 0.6.0-0.rc3
- Initial RPM
