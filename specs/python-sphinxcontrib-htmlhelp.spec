# RHEL does not include html5lib, without which the tests fail
%bcond tests %{undefined rhel}

Name:           python-sphinxcontrib-htmlhelp
Version:        2.1.0
Release:        %autorelease
Summary:        Sphinx extension for HTML help files
License:        BSD-2-Clause
URL:            http://sphinx-doc.org/
Source:         %{pypi_source sphinxcontrib_htmlhelp}
# Compatibility with Sphinx 9+
Patch:          https://github.com/sphinx-doc/sphinxcontrib-htmlhelp/pull/44.patch
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python%{python3_pkgversion}-devel


%description
sphinxcontrib-htmlhelp is a sphinx extension which renders HTML help files.


%package -n     python%{python3_pkgversion}-sphinxcontrib-htmlhelp
Summary:        %{summary}

%description -n python%{python3_pkgversion}-sphinxcontrib-htmlhelp
sphinxcontrib-htmlhelp is a sphinx extension which renders HTML help files.


%prep
%autosetup -p1 -n sphinxcontrib_htmlhelp-%{version}
find -name '*.mo' -delete


%generate_buildrequires
%pyproject_buildrequires %{?with_tests: -x test, -x standalone}


%build
for po in $(find -name '*.po'); do
  msgfmt --output-file=${po%.po}.mo ${po}
done
%pyproject_wheel


%install
%pyproject_install

# Move language files to /usr/share
pushd %{buildroot}%{python3_sitelib}
for lang in `find sphinxcontrib/htmlhelp/locales -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -printf "%f "`;
do
  test $lang == __pycache__ && continue
  install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mv sphinxcontrib/htmlhelp/locales/$lang/LC_MESSAGES/*.mo %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
done
rm -rf sphinxcontrib/htmlhelp/locales
ln -s %{_datadir}/locale sphinxcontrib/htmlhelp/locales
popd


%find_lang sphinxcontrib.htmlhelp


%check
%py3_check_import sphinxcontrib.htmlhelp
%if %{with tests}
%{__python3} -m pytest
%endif


%files -n python%{python3_pkgversion}-sphinxcontrib-htmlhelp -f sphinxcontrib.htmlhelp.lang
%license LICENCE.rst
%doc README.rst
%{python3_sitelib}/sphinxcontrib/
%{python3_sitelib}/sphinxcontrib_htmlhelp*.dist-info


%changelog
%autochangelog
