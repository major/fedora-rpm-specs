# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%global py3_shebang_flags %(echo %py3_shebang_flags | sed s/s//)

Name:           python-notebook
%global _docdir_fmt %{name}

Version:        6.5.3
Release:        %autorelease
Summary:        A web-based notebook environment for interactive computing
License:        BSD
URL:            https://jupyter.org
Source:         %{pypi_source notebook}

BuildArch:      noarch

BuildRequires:  python3-devel
# For translations
BuildRequires:  babel
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
%autosetup -n notebook-%{version}

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
%autochangelog
