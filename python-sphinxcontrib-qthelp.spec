%global pypi_name sphinxcontrib-qthelp

Name:           python-sphinxcontrib-qthelp
Version:        1.0.6
Release:        %autorelease
Summary:        Sphinx extension for QtHelp documents
License:        BSD-2-Clause
URL:            http://sphinx-doc.org/
Source:         %{pypi_source sphinxcontrib_qthelp}
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python%{python3_pkgversion}-devel


%description
sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp document.


%package -n     python%{python3_pkgversion}-sphinxcontrib-qthelp
Summary:        %{summary}

%description -n python%{python3_pkgversion}-sphinxcontrib-qthelp
sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp document.


%generate_buildrequires
%pyproject_buildrequires -x test

%prep
%autosetup -p1 -n sphinxcontrib_qthelp-%{version}
find -name '*.mo' -delete


%build
for po in $(find -name '*.po'); do
  msgfmt --output-file=${po%.po}.mo ${po}
done
%pyproject_wheel


%install
%pyproject_install

# Move language files to /usr/share
pushd %{buildroot}%{python3_sitelib}
for lang in `find sphinxcontrib/qthelp/locales -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -printf "%f "`;
do
  test $lang == __pycache__ && continue
  install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mv sphinxcontrib/qthelp/locales/$lang/LC_MESSAGES/*.mo %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
done
rm -rf sphinxcontrib/qthelp/locales
ln -s %{_datadir}/locale sphinxcontrib/qthelp/locales
popd


%find_lang sphinxcontrib.qthelp


%check
%pytest


%files -n python%{python3_pkgversion}-sphinxcontrib-qthelp -f sphinxcontrib.qthelp.lang
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinxcontrib/
%{python3_sitelib}/sphinxcontrib_qthelp-%{version}.dist-info/


%changelog
%autochangelog
