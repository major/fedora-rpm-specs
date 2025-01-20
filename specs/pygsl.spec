%global srcname pygsl
%global sum GNU Scientific Library Interface for python

Name:          pygsl
Version:       2.4.0
Release:       3%{?dist}
Summary:       %{sum}

# The package is mostly GPL+ but there are two scripts
# GLPv2+: pygsl/odeiv.py and examples/siman_tsp.py
License:       GPL-2.0-or-later
Url:           https://github.com/pygsl/pygsl

# The should be the canonical but the last release is only available on github
Source:	       %{pypi_source pygsl}
Patch1:	       %{name}_fix_version_2.4.0.patch
Patch2:	       %{name}_fix_manifest_2.4.0.patch
Patch3:	       %{name}_fix_multinomial_default_argument.patch
# Fix an upstream bug that results in allocation failures on big endian arches
Patch4:        %{name}-type-mismatch.patch

# Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires: gcc
BuildRequires: gsl-devel
BuildRequires: flexiblas-devel
BuildRequires: python3-devel

BuildRequires: python3dist(pytest)
# Only need if the generated sources are different from the version used in source
BuildRequires: swig

# Documentation dependencies
BuildRequires: %{py3_dist sphinx}
BuildRequires: %{py3_dist sphinx-rtd-theme}

# Put all the documentation in one place
%global _docdir_fmt %{name}

%description
This project provides a python interface for the GNU scientific library (gsl)


%package -n python3-%{srcname}
Summary:       %{sum}
Obsoletes:     pysgl < 2.4.0-2
Provides:      pygsl = %{version}-%{release}

%description -n python3-%{srcname}
This project provides a python interface for the GNU scientific library (gsl)


%package -n python3-%{srcname}-devel
Summary:       Development files for pygsl
Requires:      python3-%{srcname} = %{version}-%{release}
Obsoletes:     pysgl-devel < 2.4.0-2
Provides:      pygsl-devel = %{version}-%{release}


%description -n python3-%{srcname}-devel
Development files for pygsl


%package doc
Summary:       Reference manual for %{srcname}
License:       GFDL-1.1-no-invariants-or-later AND GPL-2.0-or-later
BuildArch:     noarch

%description doc
Reference manual for %{srcname}.


%prep
%autosetup -p1

fixtimestamp() {
  touch -r $1.orig $1
  rm $1.orig
}

# Fix character encodings
mv ChangeLog ChangeLog.orig
iconv -f ISO-8859-1 -t UTF-8 ChangeLog.orig > ChangeLog
fixtimestamp ChangeLog

# Fix end-of-line encodings
for f in api/pygsl.statistics ref/chebyshev ref/const ref/differentiation \
         ref/errors ref/histogram ref/ieee ref/index ref/old/ref_orig \
	 ref/panda_rst/copyright ref/panda_rst/install ref/rng ref/sf \
	 ref/statistics ref/sum ref-obsolete/copyright ref-obsolete/install \
	 ref-obsolete/ref; do
  sed -i.orig 's/\r//g' doc/$f.rst
  fixtimestamp doc/$f.rst
done

sed -i.orig 's/\r//g' doc/win/pygsl_msys2_prepare.sh
fixtimestamp doc/win/pygsl_msys2_prepare.sh

# Don't invoke python via env
for f in pygsl/{_generic_solver,block,chebyshev,fit,gsl_function,integrate,interpolation,minimize,monte,multifit{,_nlin},multiminimize,multiroots,odeiv,qrng,roots,siman,spline,vector}.py gsl_dist/swig_extension.py typemaps/c.py; do
  sed -i.orig 's,%{_bindir}/env python,%{python3},' $f
  fixtimestamp $f
done

# Use flexiblas instead of gslcblas
# https://fedoraproject.org/wiki/Changes/FlexiBLAS_as_BLAS/LAPACK_manager
sed -i 's/\(gsl_lib_list=\).*/\1["gsl", "flexiblas"]/' gsl_dist/gsl_Location.py

%generate_buildrequires
%pyproject_buildrequires

%build
# Only need if the generated sources are different from the version used in source
rm -f swig_src/gslwrap_wrap.c
%__python3 setup.py gsl_wrappers
%__python3 setup.py config
%__python3 setup.py build_ext
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}

# Fix permissions
chmod 0755 %{buildroot}%{python3_sitearch}/pygsl/{_generic_solver,block,chebyshev,fit,gsl_dist/swig_extension,gsl_function,integrate,minimize,monte,multifit{,_nlin},multiminimize,multiroots,odeiv,qrng,roots,siman,spline,vector}.py

# Build the documentation once we have an installed tree to reference
%{py3_test_envvars} sphinx-build -b html %{?_smp_mflags} doc html
rst2html --no-datestamp CREDITS.rst CREDITS.html
rst2html --no-datestamp README.rst README.html
rst2html --no-datestamp TODO.rst TODO.html
rm -fr html/.{buildinfo,doctrees}


%check
%pytest tests/

%files -n python3-%{srcname}  -f %{pyproject_files}
%doc ChangeLog README.html CREDITS.html TODO.html

%files -n python3-%{srcname}-devel
%{_includedir}/python%{python3_version}*/%{srcname}

%files doc
%doc examples/ html/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 12 2024 José Matos <jamatos@fedoraproject.org> - 2.4.0-2
- All the changes below come from Jerry James <loganjerry@gmail.com> (from Fri Feb 23 2024)
- Use virtual Provides instead of empty packages
- Link with flexiblas instead of gslcblas
- Move documentation into a doc subpackage
- Various minor spec file cleanups
- Add patch to fix FTBFS on big endian systems

* Sun Aug 11 2024 José Matos <jamatos@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.3.4-2
- Rebuilt for Python 3.13

* Fri Feb 16 2024 José Matos <jamatos@fedoraproject.org> - 2.3.4-1
- Update to 2.3.4
- Remove upstream patches
- Clean the spec file a bit
- Drop ix686 arch

* Mon Feb  5 2024 José Matos <jamatos@fedoraproject.org> - 2.3.3-4
- Update the spec file to more modern Python guidelines

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep  1 2023 José Matos <jamatos@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3
- Update license tag to SPDX license identifier
- Update url for source
- Add patch to work with Python 3.12

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.3.0-22
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec  3 2022 Florian Weimer <fweimer@redhat.com> - 2.3.0-20
- Avoid implicit function declarations in SWIG-generated code

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.0-19
- Rebuild for gsl-2.7.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3.0-17
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3.0-14
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 José Matos <jamatos@fedoraproject.org> - 2.3.0-11
- Require at build time python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-7
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.3.0-6
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Subpackages python2-pygsl, python2-pygsl-devel have been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 José Matos <jamatos@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0 (#1504422)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.2.0-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr  19 2016 José Matos <jamatos@fedoraproject.org> - 2.2.0-1
- update to 2.2.0

* Sat Mar  5 2016 José Matos <jamatos@fedoraproject.org> - 2.1.1-4
- rebuild for gsl 2.1
- Use swig to regenerate the wrappers.

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.1.1-3
- Rebuild for gsl 2.1

* Sun Feb 14 2016 José Matos <jamatos@fedoraproject.org> - 2.1.1-2
- fix requirements (typos)

* Sat Feb 13 2016 José Matos <jamatos@fedoraproject.org> - 2.1.1-1
- update to 2.1.1
- remove included license
- add python2 and python3 subpackages, preserving the upgrade path

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 José Matos <jamatos@fedoraproject.org> - 0.9.5-8
- Clean spec file (thanks to Jussi #528515)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May  9 2011 José Matos <jamatos@fedoraproject.org> - 0.9.5-5
- Rebuild for a newer gsl (F16+)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon May 10 2010 José Matos <jamatos@fc.up.pt> - 0.9.5-2
- Rebuild for new gsl version (F14+).

* Thu Apr  8 2010 José Matos <jamatos@fc.up.pt> - 0.9.5-1
- Bug fix release. A memory leak was fixed for all modules using
  gsl_functions: integrate, min, roots, deriv.
- Include more original documentation.
- Remove patch applied upstream.

* Thu Nov 19 2009 José Matos <jamatos@fc.up.pt> - 0.9.4-7
- Revert to local patch as upstream one does not work.

* Thu Nov 19 2009 José Matos <jamatos@fc.up.pt> - 0.9.4-6
- Request build with the upstream patch.

* Thu Nov 19 2009 José Matos <jamatos@fc.up.pt> - 0.9.4-5
- Fix typo in -devel Summary. (#504881)

* Tue Sep 15 2009 José Matos <jamatos@fc.up.pt> - 0.9.4-4
- Remove gsm units taken away in gsl-1.13.

* Tue Sep 15 2009 José Matos <jamatos@fc.up.pt> - 0.9.4-3
- Rebuild for new upstream gsl version (F12+).

* Thu Jul 30 2009 José Matos <jamatos[AT]fc.up.pt> - 0.9.4-2
- Add missing BR numpy-f2py

* Thu Jul 30 2009 José Matos <jamatos[AT]fc.up.pt> - 0.9.4-1
- New upstream bugfix release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 José Matos <jamatos@fc.up.pt> - 0.9.3-3
- Rebuild for new gsl (F11+).

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9.3-2
- Rebuild for Python 2.6

* Tue Jun 17 2008 José Matos <jamatos[AT]fc.up.pt> - 0.9.3-1
- New upstream release.

* Fri Feb 22 2008 José Matos <jamatos[AT]fc.up.pt> - 0.9.1-8
- Add egg-info file to package (F9+).

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.1-7
- Autorebuild for GCC 4.3

* Fri Sep 21 2007 José Matos <jamatos[AT]fc.up.pt> - 0.9.1-6
- License clarification.
- Use swig to regenerate the wrappers.
- Rebuild with gsl-1.10.
- Add explicit dependency on gsl version.

* Thu Aug 30 2007 José Matos <jamatos[AT]fc.up.pt> - 0.9.1-5
- Fix typo in Requires for subpackage devel.

* Wed Aug 29 2007 José Matos <jamatos[AT]fc.up.pt> - 0.9.1-4
- Remove docs from documentation as it not carried anymore, add a devel subpackage.

* Wed Aug 29 2007 José Matos <jamatos[AT]fc.up.pt> - 0.9.1-3
- Corrected the reference to numpy.

* Wed Aug 29 2007 José Matos <jamatos[AT]fc.up.pt> - 0.9.1-2
- Rebuild with the correct source.

* Wed Aug 29 2007 José Matos <jamatos[AT]fc.up.pt> - 0.9.1-1
- New upstream version.
- Change from numeric to numpy.

* Wed Aug 29 2007 José Matos <jamatos[AT]fc.up.pt> - 0.3.2-8
- License fix, rebuild for devel (F8).

* Mon Dec 11 2006 José Matos <jamatos[AT]fc.up.pt> - 0.3.2-7
- Rebuild for python 2.5.

* Mon Sep 11 2006 José Matos <jamatos[AT]fc.up.pt> - 0.3.2-6
- Rebuild for FC6.

* Thu Feb 16 2006 José Matos <jamatos[AT]fc.up.pt> - 0.3.2-5
- Rebuild for FC-5.

* Sat Jul  2 2005 José Matos <jamatos[AT]fc.up.pt> - 0.3.2-4
- Add license file from cvs.

* Fri Jul  1 2005 José Matos <jamatos[AT]fc.up.pt> - 0.3.2-3
- Remove duplicated "setup" entry.

* Fri Jul  1 2005 José Matos <jamatos[AT]fc.up.pt> - 0.3.2-2
- Clean spec file.

* Thu Jun 30 2005 José Matos <jamatos[AT]fc.up.pt> - 0.3.2-1
- New version.
