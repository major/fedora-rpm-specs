Name:           python-sphinxcontrib-devhelp
Version:        1.0.5
Release:        %autorelease
Summary:        Sphinx extension for Devhelp documents
License:        BSD-2-Clause
URL:            http://sphinx-doc.org/
Source:         %{pypi_source sphinxcontrib_devhelp}
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python%{python3_pkgversion}-devel


%description
sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp document.


%package -n     python%{python3_pkgversion}-sphinxcontrib-devhelp
Summary:        %{summary}

%description -n python%{python3_pkgversion}-sphinxcontrib-devhelp
sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp document.


%generate_buildrequires
%pyproject_buildrequires -x test


%prep
%autosetup -n sphinxcontrib_devhelp-%{version}
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
for lang in `find sphinxcontrib/devhelp/locales -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -printf "%f "`;
do
  test $lang == __pycache__ && continue
  install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mv sphinxcontrib/devhelp/locales/$lang/LC_MESSAGES/*.mo %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
done
rm -rf sphinxcontrib/devhelp/locales
ln -s %{_datadir}/locale sphinxcontrib/devhelp/locales
popd


%find_lang sphinxcontrib.devhelp


%check
%pytest


%files -n python%{python3_pkgversion}-sphinxcontrib-devhelp -f sphinxcontrib.devhelp.lang
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinxcontrib/
%{python3_sitelib}/sphinxcontrib_devhelp-%{version}.dist-info/


%changelog
%autochangelog
