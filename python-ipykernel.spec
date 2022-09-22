%global modname ipykernel

# When we bootstrap new Python, we don't yet have all the documentation packages
%bcond_without intersphinx
# And the tests transitively require ipykernel
%bcond_without tests

Name:           python-%{modname}
Version:        6.15.2
Release:        1%{?dist}
Summary:        IPython Kernel for Jupyter
License:        BSD
URL:            https://github.com/ipython/%{modname}
Source0:        https://github.com/ipython/%{modname}/releases/download/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-github-alt
BuildRequires:  python3-myst-parser

%global _description \
This package provides the IPython kernel for Jupyter.

%description %{_description}

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
Requires:       python-jupyter-filesystem

%if %{with intersphinx}
BuildRequires:  python%{python3_pkgversion}-docs
BuildRequires:  python%{python3_pkgversion}-ipython-doc
BuildRequires:  python-jupyter-client-doc
%endif

Recommends:     python%{python3_pkgversion}-matplotlib
Recommends:     python%{python3_pkgversion}-numpy
Recommends:     python%{python3_pkgversion}-pandas
Recommends:     python%{python3_pkgversion}-scipy
Recommends:     python%{python3_pkgversion}-pillow

%description -n python%{python3_pkgversion}-%{modname} %{_description}

%package doc
Summary:        Documentation for %{name}
%if %{with intersphinx}
Requires:       python%{python3_pkgversion}-docs
Requires:       python%{python3_pkgversion}-ipython-doc
Requires:       python-jupyter-client-doc
%endif

%description    doc
This package contains the documentation of %{name}.

%prep
%autosetup -p1 -n %{modname}-%{version}

# Remove the dependency on debugpy.
# See https://github.com/ipython/ipykernel/pull/767
sed -i '/"debugpy/d' pyproject.toml

%if %{with intersphinx}
# Use local objects.inv for intersphinx:
sed -e "s|\(('https://docs.python.org/3/', \)None)|\1'/usr/share/doc/python3-docs/html/objects.inv')|" \
    -e "s|\(('https://ipython.readthedocs.io/en/latest', \)None)|\1'/usr/share/doc/python3-ipython-doc/html/objects.inv')|" \
    -e "s|\(('https://jupyter.readthedocs.io/en/latest', \)None)|\1'/usr/share/doc/python-jupyter-client/html/objects.inv')|" \
    -i docs/conf.py
%endif

%generate_buildrequires
%pyproject_buildrequires -w %{?with_tests:-x test}

%build
%pyproject_wheel

%make_build -C docs html

%install
%pyproject_install
%pyproject_save_files %{modname} %{modname}_launcher
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -fpavr docs/_build/html %{buildroot}%{_docdir}/%{name}
rm %{buildroot}%{_docdir}/%{name}/html/.buildinfo

# Install the kernel so it can be found
# See https://bugzilla.redhat.com/show_bug.cgi?id=1327979#c19
%{python3} -m ipykernel install --prefix %{buildroot}%{_prefix}
ls %{buildroot}%{_datadir}/jupyter/kernels/python3/
cat %{buildroot}%{_datadir}/jupyter/kernels/python3/kernel.json


%if %{with tests}
%check
%pytest
%else
# datapub, pickleutil, serialize need ipyparallel
# pylab needs matplotlib
# trio needs trio
# debugger needs debugpy
# gui needs gobject
%{pyproject_check_import \
    -e %{modname}.datapub -e %{modname}.pickleutil -e %{modname}.serialize \
    -e '%{modname}.pylab*' \
    -e '%{modname}.trio*' \
    -e %{modname}.debugger \
    -e '%{modname}.gui*' \
    -e '*.test*'}
%endif


%files -n python%{python3_pkgversion}-%{modname}
%license COPYING.md
%doc CONTRIBUTING.md MANIFEST.in README.md
%{python3_sitelib}/%{modname}
%pycached %{python3_sitelib}/%{modname}_launcher.py
%{python3_sitelib}/%{modname}*.dist-info/
%{_datadir}/jupyter/kernels/python3

%files doc
%doc %{_docdir}/%{name}/html


%changelog
* Wed Aug 31 2022 Charalampos Stratakis <cstratak@redhat.com> - 6.15.2-1
- Update to 6.15.2
Resolves: rhbz#2122279

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 6.6.1-4
- Rebuilt for Python 3.11

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 6.6.1-3
- Bootstrap for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Lumír Balhar <lbalhar@redhat.com> - 6.6.1-1
- Update to 6.6.1
Resolves: rhbz#2015753

* Tue Aug 31 2021 Lumír Balhar <lbalhar@redhat.com> - 6.4.1-1
- Update to 6.4.1
Resolves: rhbz#1936895

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.5.0-3
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.5.0-2
- Bootstrap for Python 3.10

* Wed Feb 24 2021 Miro Hrončok <mhroncok@redhat.com> - 5.5.0-1
- Update to 5.5.0
- Fixes: rhbz#1838008

* Wed Feb 24 2021 Miro Hrončok <mhroncok@redhat.com> - 5.4.3-1
- Update to 5.4.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 5.2.1-3
- Rebuilt for Python 3.9

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 5.2.1-2
- Bootstrap for Python 3.9

* Tue Apr 21 2020 Miro Hrončok <mhroncok@redhat.com> - 5.2.1-1
- Update to 5.2.1 (#1815803)

* Fri Feb 21 2020 Jerry James <loganjerry@gmail.com> - 5.1.4-1
- Update to 5.1.4 (bz 1795174)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Miro Hrončok <mhroncok@redhat.com> - 5.1.3-1
- Update to 5.1.3 (#1780932)

* Thu Sep 26 2019 Jerry James <loganjerry@gmail.com> - 5.1.2-1
- Update to 5.1.2 (bz 1742596)
- Drop upstreamed 408 patch
- Drop explicit Provides that are now autogenerated
- Use local objects.inv for intersphinx, add necessary -doc BRs
- Ship this package's objects.inv
- Run all of the tests again

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 5.1.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Miro Hrončok <mhroncok@redhat.com> - 5.1.1-1
- Update to 5.1.1 (#1710745)

* Tue Feb 12 2019 Miro Hrončok <mhroncok@redhat.com> - 4.10.0-1
- Update to 5.1.0, drop Python 2 package

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 13 2018 Miro Hrončok <mhroncok@redhat.com> - 4.8.2-3
- Don't own /usr/share/jupyter/ and /usr/share/jupyter/kernels/,
  require python-jupyter-filesystem instead (#1589420)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.8.2-2
- Rebuilt for Python 3.7

* Wed May 23 2018 Miro Hrončok <mhroncok@redhat.com> - 4.8.2-1
- Update to 4.8.2 (#1438785)
- Use Python 3 Sphinx to build the docs

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Iryna Shcherbina <ishcherb@redhat.com> - 4.6.0-3
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 09 2017 Miro Hrončok <mhroncok@redhat.com> - 4.6.0-1
- Update to 4.6.0
- Recommend some useful packages
- Run the testsuite

* Wed Mar 15 2017 Miro Hrončok <mhroncok@redhat.com> - 4.5.2-6
- Package the kernel json files

* Wed Mar 8 2017 Orion Poplawski <orion@cora.nwra.com> - 4.5.2-5
- Add missing requires (bug #1430480)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.5.2-3
- Preseve timestamp of installed files (#1406958#c7)

* Mon Dec 26 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.5.2-2
- Use proper Source0 format (#1406958#c4)
- Do parallel html make (#1406958#c4)

* Thu Dec 22 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.5.2-1
- Update to latest upstream release.
- Correct removal of unnecessary doc files.

* Wed Nov 16 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.5.1-1
- Initial package.
