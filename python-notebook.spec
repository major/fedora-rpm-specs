# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%global py3_shebang_flags %(echo %py3_shebang_flags | sed s/s//)

Name:           python-notebook
%global _docdir_fmt %{name}

Version:        6.5.2
Release:        1%{?dist}
Summary:        A web-based notebook environment for interactive computing
License:        BSD
URL:            https://jupyter.org
Source:         %{pypi_source notebook}

# Patch containing .mo and .json files for translations.
# .mo binary files are regenerated in %%build
# .json files need po2json (JS implementation) which is
# not available in Fedora and therefore we use them from this patch.
Patch0:          https://github.com/jupyter/notebook/pull/6728.patch

BuildArch:      noarch

BuildRequires:  python3-devel
# For translations
BuildRequires:  babel
# For binary patch
BuildRequires:  git-core
# For validating desktop entry
BuildRequires:  desktop-file-utils

%global _description \
The Jupyter Notebook is a web application that allows you to create and \
share documents that contain live code, equations, visualizations, and \
explanatory text. The Notebook has support for multiple programming \
languages, sharing, and interactive widgets.

%description %_description

%package -n     python3-notebook
Summary:        %{summary}
%py_provides    python3-jupyter-notebook
%py_provides    python3-ipython-notebook
%py_provides    notebook
%py_provides    jupyter-notebook

%description -n python3-notebook %_description


%prep
%setup -q -n notebook-%{version}

# Apply binary patch
git --git-dir=. apply --exclude .gitignore --apply %{PATCH0}

# The nbval package is used for validation of notebooks.
# It's sedded out because it isn't yet packaged in Fedora.
#
# Selenium tests are skipped because the version in Fedora is too old.
# We don't test coverage.
for pkg in nbval "selenium==.*" coverage pytest-cov; do
  sed -Ei "s/'$pkg',? ?//" setup.py
done


%generate_buildrequires
%pyproject_buildrequires -x test


%build
# Generate .mo files from .po files and remove .po files
pushd notebook/i18n
for lang in $(ls -d */ | tr -d "/")
do
  for file in nbui notebook
  do
    pybabel compile -D ${file} -f -l ${lang} -i ${lang}/LC_MESSAGES/${file}.po -o ${lang}/LC_MESSAGES/${file}.mo
    rm -v ${lang}/LC_MESSAGES/${file}.po
  done

  # Unfortunately this neither works with po2json from translate-toolkit nor
  # with the po2json package from PyPI and the JS implementation:
  # https://www.npmjs.com/package/po2json
  # is not availabe in Fedora. But the files should be available
  # upstream. Issue: https://github.com/jupyter/notebook/issues/6717
  # po2json -p -F -f jed1.x -d nbjs ${lang}/LC_MESSAGES/nbjs.po ${lang}/LC_MESSAGES/nbjs.json
  rm -v ${lang}/LC_MESSAGES/nbjs.po

done
popd

%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files notebook

# Remove nbjs.json files from pyproject_files
# to add them manually later with %%lang
sed -i "/LC_MESSAGES\/nbjs.json/d" %{pyproject_files}


%check
%pytest --ignore notebook/tests/selenium

desktop-file-validate %{buildroot}%{_datadir}/applications/jupyter-notebook.desktop


%files -n python3-notebook -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/jupyter-bundlerextension
%{_bindir}/jupyter-nbextension
%{_bindir}/jupyter-serverextension
%{_bindir}/jupyter-notebook
# lang .json files not detected by save_files
%lang(fr) %{python3_sitelib}/notebook/i18n/fr_FR/LC_MESSAGES/nbjs.json
%lang(ja) %{python3_sitelib}/notebook/i18n/ja_JP/LC_MESSAGES/nbjs.json
%lang(nl) %{python3_sitelib}/notebook/i18n/nl/LC_MESSAGES/nbjs.json
%lang(ru) %{python3_sitelib}/notebook/i18n/ru_RU/LC_MESSAGES/nbjs.json
%lang(zh) %{python3_sitelib}/notebook/i18n/zh_CN/LC_MESSAGES/nbjs.json
# Desktop integration
%{_datadir}/applications/jupyter-notebook.desktop
%{_datadir}/icons/hicolor/scalable/apps/notebook.svg
# Tests
%exclude %{python3_sitelib}/notebook/auth/tests
%exclude %{python3_sitelib}/notebook/bundler/tests
%exclude %{python3_sitelib}/notebook/nbconvert/tests
%exclude %{python3_sitelib}/notebook/services/api/tests
%exclude %{python3_sitelib}/notebook/services/config/tests
%exclude %{python3_sitelib}/notebook/services/contents/tests
%exclude %{python3_sitelib}/notebook/services/kernels/tests
%exclude %{python3_sitelib}/notebook/services/kernelspecs/tests
%exclude %{python3_sitelib}/notebook/services/nbconvert/tests
%exclude %{python3_sitelib}/notebook/services/sessions/tests
%exclude %{python3_sitelib}/notebook/terminal/tests
%exclude %{python3_sitelib}/notebook/tests
%exclude %{python3_sitelib}/notebook/tree/tests


%changelog
* Wed Feb 01 2023 Lumír Balhar <lbalhar@redhat.com> - 6.5.2-1
- Update to 6.5.2 (#2062405)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 03 2022 Karolina Surma <ksurma@redhat.com> - 6.4.12-1
- Update to 6.4.12

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Miro Hrončok <mhroncok@redhat.com> - 6.4.11-3
- Fix CVE-2022-24785 and CVE-2022-31129 in bundled moment
- Fixes: rhbz#2075263

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 6.4.11-2
- Rebuilt for Python 3.11

* Mon May 30 2022 Miro Hrončok <mhroncok@redhat.com> - 6.4.11-1
- Update to 6.4.11

* Tue Mar 22 2022 Miro Hrončok <mhroncok@redhat.com> - 6.4.10-1
- Update to 6.4.10

* Tue Jan 25 2022 Miro Hrončok <mhroncok@redhat.com> - 6.4.8-1
- Update to 6.4.8
- Fixes: rhbz#2045852

* Tue Jan 25 2022 Miro Hrončok <mhroncok@redhat.com> - 6.4.7-1
- Update to 6.4.7
- Fixes: rhbz#2039905

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 29 2021 Karolina Surma <ksurma@redhat.com> - 6.4.6-2
- Remove -s from Python shebang in `jupyter-*` executables
  to let Jupyter see pip installed extensions

* Wed Nov 24 2021 Karolina Surma <ksurma@redhat.com> - 6.4.6-1
- Update to 6.4.6
Resolves: rhbz#2023994

* Tue Oct 26 2021 Lumír Balhar <lbalhar@redhat.com> - 6.4.5-1
- Update to 6.4.5
Resolves: rhbz#2004590

* Wed Aug 11 2021 Tomas Hrnciar <thrnciar@redhat.com> - 6.4.3-1
- Update to 6.4.3
- Fixes: rhbz#1990615
- Fixes: rhbz#1992573

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 24 2021 Lumír Balhar <lbalhar@redhat.com> - 6.4.0-1
- Update to 6.4.0
Resolves: rhbz#1956754

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.3.0-2
- Rebuilt for Python 3.10

* Tue Mar 23 2021 Karolina Surma <ksurma@redhat.com> - 6.3.0-1
- Update to 6.3.0
Resolves: rhbz#1941573
- Add desktop entry
Resolves: rhbz#1275800
- Remove documentation subpackage

* Thu Feb 18 2021 Lumír Balhar <lbalhar@redhat.com> - 6.2.0-1
- Update to 6.2.0
Resolves: rhbz#1915896

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Miro Hrončok <mhroncok@redhat.com> - 6.1.6-1
- Update to 6.1.6
- Fixes: rhbz#1895357

* Thu Sep 10 2020 Tomas Hrnciar <thrnciar@redhat.com> - 6.1.4-1
- Update to 6.1.4
- fixes rhbz#1844874

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 11 2020 Miro Hrončok <mhroncok@redhat.com> - 6.0.3-7
- Remove packaged tests

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 6.0.3-6
- Rebuilt for Python 3.9

* Sat Apr 18 2020 Miro Hrončok <mhroncok@redhat.com> - 6.0.3-5
- Update to 6.0.3 (#1793671)

* Thu Mar 12 2020 Miro Hrončok <mhroncok@redhat.com> - 6.0.2-4
- Workaround RPM problems when replacing a directory with a symbolic link (#1787079)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 26 2019 Miro Hrončok <mhroncok@redhat.com> - 6.0.2-2
- Use bundled JavaScript moment, the Fedora one was retired

* Tue Nov 12 2019 Miro Hrončok <mhroncok@redhat.com> - 6.0.2-1
- Update to 6.0.2 (#1724407)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.7.8-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 5.7.8-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 01 2019 Miro Hrončok <mhroncok@redhat.com> - 5.7.8-1
- Update to 5.7.8, refix CVE-2019-10255

* Sun Mar 31 2019 Miro Hrončok <mhroncok@redhat.com> - 5.7.7-1
- Update to 5.7.7, fix CVE-2019-9644 and CVE-2019-10255

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Miro Hrončok <mhroncok@redhat.com> - 5.7.2-1
- Update to 5.7.2, fix CVE-2018-19351, CVE-2018-19352 (#1651976)

* Wed Nov 07 2018 Miro Hrončok <mhroncok@redhat.com> - 5.6.0-3
- Drop the python2 leaf subpackage again (#1647377)

* Mon Aug 13 2018 Miro Hrončok <mhroncok@redhat.com> - 5.6.0-2
- Require mathjax from python3-notebook (#1615192)

* Mon Jul 23 2018 Miro Hrončok <mhroncok@redhat.com> - 5.6.0-1
- Update to 5.6.0 (#1601163)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.5.0-6
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Miro Hrončok <mhroncok@redhat.com> - 5.5.0-5
- Reintroduce the python2 subpackage for sagemath

* Sun May 27 2018 Miro Hrončok <mhroncok@redhat.com> - 5.5.0-4
- Drop the python2 leaf subpackage

* Sat May 26 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 5.5.0-3
- Unbundle mathjax once more
- Add patch to use the MathJax TeX fonts rather than the STIXWeb ones BZ: 1581899, 1580129

* Wed May 23 2018 Miro Hrončok <mhroncok@redhat.com> - 5.5.0-2
- BR ipykernel >= 4.8 (#1581723)
- Temporarily keep bundled mathjax (#1580129)

* Fri May 11 2018 Miro Hrončok <mhroncok@redhat.com> - 5.5.0-1
- Update to 5.5.0 (#1557990)
- Disable selenium tests and rm them from python2 sitelib

* Wed Mar 21 2018 Miro Hrončok <mhroncok@redhat.com> - 5.4.0-2
- Security fix for CVE-2018-8768 (#1558783)

* Wed Feb 21 2018 Miro Hrončok <mhroncok@redhat.com> - 5.4.0-1
- Update to 5.4.0 (#1535263)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Miro Hrončok <mhroncok@redhat.com> - 5.3.0-1
- Update to 5.3.0
- Enable automatic dependency generator, drop manual Python requires

* Tue Jan 09 2018 Miro Hrončok <mhroncok@redhat.com> - 5.3.0-0.1.rc1
- Update to new 5.3.0rc1 version (#1532430)
- Only BR git-core instead of full git, it is sufficient
- Be more explciit about (Build)Required versions
- Require send2trash, dateutil

* Thu Nov 23 2017 Miro Hrončok <mhroncok@redhat.com> - 5.2.1-1
- Update to new 5.2.1 version (#1504386)

* Fri Sep 15 2017 Miro Hrončok <mhroncok@redhat.com> - 5.1.0-1
- Update to new 5.1.0 final version (#1491890)

* Tue Sep 12 2017 Miro Hrončok <mhroncok@redhat.com> - 5.1.0-0.2.rc3
- Update to new 5.1.0rc3 version (#1490880)
- Remove 2 merged patches

* Wed Aug 23 2017 Miro Hrončok <mhroncok@redhat.com> - 5.1.0-0.1.rc2
- Update to new 5.1.0rc2 version (#1482722)
- Use node to compile JS and CSS

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Miro Hrončok <mhroncok@redhat.com> - 5.0.0-1
- Update to new 5.0.0 version (#1438917)
- Use autosetup with git
- Add the license file to the doc subpackage

* Fri Mar 17 2017 Miro Hrončok <mhroncok@redhat.com> - 4.4.1-3
- Recommend terminado

* Tue Feb 21 2017 Miro Hrončok <mhroncok@redhat.com> - 4.4.1-2
- Make sure the Python 3 executables are really Python 3
- Build the docs
- Run the tests
- Use python2- where possible
- Unbundle some things, declare the rest
- Use the %%_description macro consistently
- Provide pythonX-jupyter-notebook
- Provide/Obsolete pythonX-ipython-notebook

* Thu Feb 09 2017 Thomas Spura <tomspur@fedoraproject.org> - 4.4.1-1
- rename to python-notebook
- only ship python3 executables
- update to 4.4.1

* Mon Apr 18 2016 Thomas Spura <tomspur@fedoraproject.org> - 4.2.0-1
- Initial package.
