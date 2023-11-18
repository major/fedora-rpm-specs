%global pypi_name sphinxcontrib-qthelp

Name:           python-sphinxcontrib-qthelp
Version:        1.0.6
Release:        2%{?dist}
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
* Thu Nov 16 2023 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-2
- Remove a patch to drop the runtime dependency on Sphinx
- It is no longer needed, python3-sphinx-7.2.6-2+ no longer Requires this

* Thu Aug 24 2023 Karolina Surma <ksumra@redhat.com> - 1.0.6-1
- Update to 1.0.6
Resolves: rhbz#2230149

* Thu Aug 10 2023 Karolina Surma <ksumra@redhat.com> - 1.0.3-16
- Declare the license as an SPDX expression

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 1.0.3-14
- Rebuilt for Python 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.0.3-13
- Bootstrap for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Karolina Surma <ksurma@redhat.com> - 1.0.3-10
- Fix compatibility with Sphinx 5

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.3-9
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.3-8
- Bootstrap for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 1.0.3-5
- Rebuilt for Python 3.10

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 1.0.3-4
- Bootstrap for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.0.3-1
- Update to 1.0.3 (#1808636)

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-8
- Rebuilt for Python 3.9

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-7
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-4
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-3
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-1
- Initial package
