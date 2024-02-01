Name:           python-sphinxcontrib-serializinghtml
Version:        1.1.9
Release:        %autorelease
Summary:        Sphinx extension for serialized HTML
License:        BSD-2-Clause
URL:            http://sphinx-doc.org/
Source:         %{pypi_source sphinxcontrib_serializinghtml}
BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  python%{python3_pkgversion}-devel


%description
sphinxcontrib-serializinghtml is a sphinx extension which outputs "serialized"
HTML files (json and pickle).


%package -n     python%{python3_pkgversion}-sphinxcontrib-serializinghtml
Summary:        %{summary}

%description -n python%{python3_pkgversion}-sphinxcontrib-serializinghtml
sphinxcontrib-serializinghtml is a sphinx extension which outputs "serialized"
HTML files (json and pickle).


%generate_buildrequires
%pyproject_buildrequires -x test


%prep
%autosetup -n sphinxcontrib_serializinghtml-%{version}
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
for lang in `find sphinxcontrib/serializinghtml/locales -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -printf "%f "`;
do
  test $lang == __pycache__ && continue
  install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mv sphinxcontrib/serializinghtml/locales/$lang/LC_MESSAGES/*.mo %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
done
rm -rf sphinxcontrib/serializinghtml/locales
ln -s %{_datadir}/locale sphinxcontrib/serializinghtml/locales
popd


%find_lang sphinxcontrib.serializinghtml


%check
%pytest


%files -n python%{python3_pkgversion}-sphinxcontrib-serializinghtml -f sphinxcontrib.serializinghtml.lang
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinxcontrib/
%{python3_sitelib}/sphinxcontrib_serializinghtml-%{version}.dist-info/


%changelog
%autochangelog
