Name:           python-sphinxcontrib-devhelp
Version:        1.0.5
Release:        2%{?dist}
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
* Thu Nov 16 2023 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-2
- Remove a patch to drop the runtime dependency on Sphinx
- It is no longer needed, python3-sphinx-7.2.6-2+ no longer Requires this

* Mon Aug 21 2023 Karolina Surma <ksurma@redhat.com> - 1.0.5-1
- Update to 1.0.5
  Fixes: rhbz#2230147

* Wed Aug 09 2023 Karolina Surma <ksurma@redhat.com> - 1.0.2-15
- Declare the license as an SPDX expression

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 1.0.2-13
- Rebuilt for Python 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.0.2-12
- Bootstrap for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.2-9
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.2-8
- Bootstrap for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 1.0.2-5
- Rebuilt for Python 3.10

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 1.0.2-4
- Bootstrap for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.0.2-1
- Update to 1.0.2 (#1808639)

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-8
- Rebuilt for Python 3.9

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-7
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-4
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-3
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-1
- Initial package
