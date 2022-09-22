# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%global py3_shebang_flags %(echo %py3_shebang_flags | sed s/s//)

Name:           python-notebook
%global _docdir_fmt %{name}

# Updating this package? Update the list of bundled things bellow
Version:        6.4.12
Release:        1%{?dist}
Summary:        A web-based notebook environment for interactive computing
License:        BSD
URL:            https://jupyter.org
Source0:        %{pypi_source notebook}

# Patch to use the TeX fonts from the MathJax package rather than STIXWeb
# See BZ: 1581899, 1580129
Patch0:         0001-Use-MathJax-TeX-fonts-rather-than-STIXWeb.patch

# Fix CVE-2022-24785 and CVE-2022-31129 in bundled moment
Patch:          0001-Fix-CVE-2022-24785-and-CVE-2022-31129.patch

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  git-core

# rebuilding js and css
BuildRequires:  /usr/bin/node

# for tests
BuildRequires:  pandoc

# for validating desktop entry
BuildRequires: desktop-file-utils

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

Requires:       fontawesome-fonts
Requires:       fontawesome-fonts-web
Requires:       mathjax >= 2.6
Requires:       js-backbone >= 1.2
Requires:       js-marked >= 0.7
Requires:       js-underscore >= 1.8.3
Requires:       hicolor-icon-theme

# Versions from bower.json
Provides:       bundled(bootstrap) = 3.4
Provides:       bundled(bootstrap-tour) = 0.9.0
Provides:       bundled(codemirror) = 5.56.0
Provides:       bundled(create-react-class) = 15.6.3
Provides:       bundled(es6-promise) = 1.0
Provides:       bundled(google-caja) = 5669
Provides:       bundled(jed) = 1.1.1
Provides:       bundled(jquery) = 3.5.0
Provides:       bundled(jquery-typeahead) = 2.10.6
Provides:       bundled(jquery-ui) = 1.12
Provides:       bundled(moment) = 2.19.3
Provides:       bundled(react) = 16.0.0
Provides:       bundled(requirejs) = 2.2
Provides:       bundled(requirejs-text) = 2.0.15
Provides:       bundled(requirejs-plugins) = 1.0.3
Provides:       bundled(text-encoding) = 0.1
Provides:       bundled(xterm.js) = 3.1.0
Provides:       bundled(xterm.js-css) = 3.1.0
Provides:       bundled(xterm.js-fit) = 3.1.0
# See https://bugzilla.redhat.com/show_bug.cgi?id=1580129
#Provides:       bundled(mathjax) = 2.7.4

%description -n python3-notebook %_description


%prep
%autosetup -n notebook-%{version} -S git

# The nbval package is used for validation of notebooks.
# It's sedded out because it isn't yet packaged in Fedora.
#
# Selenium tests are skipped.
# We don't test coverage.
for pkg in nbval selenium coverage pytest-cov; do
  sed -Ei "s/'$pkg',? ?//" setup.py
done


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install

# Don't use %%pyproject_save_files, because we'll change a lot

# unbundle stuff
pushd %{buildroot}%{python3_sitelib}/notebook/static/components

  rm -r font-awesome/fonts
  ln -vfs %{_datadir}/fonts/fontawesome font-awesome/fonts

  #temporarily kept bundled to workaround #1580129
  rm -r MathJax
  ln -vfs %{_datadir}/javascript/mathjax MathJax

  rm -r backbone
  ln -vfs %{_datadir}/javascript/backbone backbone

  rm -r marked/lib
  ln -vfs %{_datadir}/javascript/marked marked/lib

  rm -r underscore
  ln -vfs %{_datadir}/javascript/underscore underscore

popd

# Remove packaged tests
rm -rv $(find %{buildroot}%{python3_sitelib}/notebook -type d -name tests)

# Remove .po files
rm -v $(find %{buildroot}%{python3_sitelib}/notebook/i18n -type f -name '*.po')


%check
# Workaround: OSError: [Errno 18] Invalid cross-device link: b'/tmp/...' -> b'/builddir/.local/share/Trash/files/...'
mkdir .tmp
export TMPDIR=$(pwd)/.tmp

%pytest --ignore notebook/tests/selenium

desktop-file-validate %{buildroot}%{_datadir}/applications/jupyter-notebook.desktop

# This was previously unbundled, but no more
# See https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/
%pretrans -n python3-notebook -p <lua>
path = "%{python3_sitelib}/notebook/static/components/moment"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end


%files -n python3-notebook
%doc README.md
%license LICENSE
%{_bindir}/jupyter-bundlerextension
%{_bindir}/jupyter-nbextension
%{_bindir}/jupyter-serverextension
%{_bindir}/jupyter-notebook
%{python3_sitelib}/notebook-%{version}.dist-info/

# Exclude i18n:
%dir %{python3_sitelib}/notebook/
%{python3_sitelib}/notebook/[_a-hj-z]*

# Language files (could be scripted, but is short)
%dir %{python3_sitelib}/notebook/i18n/
%{python3_sitelib}/notebook/i18n/*.py
%{python3_sitelib}/notebook/i18n/__pycache__/
%lang(fr) %{python3_sitelib}/notebook/i18n/fr_FR/
%lang(ja) %{python3_sitelib}/notebook/i18n/ja_JP/
%lang(nl) %{python3_sitelib}/notebook/i18n/nl/
%lang(ru) %{python3_sitelib}/notebook/i18n/ru_RU/
%lang(zh) %{python3_sitelib}/notebook/i18n/zh_CN/

# Desktop integration
%{_datadir}/applications/jupyter-notebook.desktop
%{_datadir}/icons/hicolor/scalable/apps/notebook.svg


%changelog
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
