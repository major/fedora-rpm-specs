# Dependency python3dist(fontPens) for “pens” extra is not yet packaged
%bcond_with pens

Name:           python-defcon
Version:        0.10.2
Release:        6%{?dist}
Summary:        A set of flexible objects for representing UFO data

License:        MIT
URL:            https://github.com/robotools/defcon
Source0:        %{pypi_source defcon %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Defcon is a set of UFO based objects optimized for use in font editing
applications. The objects are built to be lightweight, fast and flexible. The
objects are very bare-bones and they are not meant to be end-all, be-all
objects. Rather, they are meant to provide base functionality so that you can
focus on your application’s behavior, not object observing or maintaining
cached data. Defcon implements UFO3 as described by the UFO font format.}

%description %{_description}

%package -n python3-defcon
Summary:        %{summary}

%description -n python3-defcon %{_description}

%pyproject_extras_subpkg -n python3-defcon lxml%{?with_pens: pens}

%prep
%autosetup -n defcon-%{version}
# Since requirements.txt is used for tox, loosen pinned versions
sed -r -i 's/==/>=/' requirements.txt

%generate_buildrequires
%pyproject_buildrequires -t -x lxml%{?with_pens:,pens}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files defcon

%check
%tox

%files -n python3-defcon -f %{pyproject_files}
# pyproject_files handles License.txt; verify with “rpm -qL -p …”
%doc README.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.10.2-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 26 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.10.2-1
- Modernize spec file macros, and drop obsolete ones
- Run the tests
- Add metapackage for “lxml” extra
- Port to pyproject-rpm-macros (“new Python guidelines”)
- Reduce macro indirection by dropping the srcname macro
- Update to 0.10.2 (close RHBZ#1936574)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.7.2-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7.2-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.2-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 0.7.2-1
- Update version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.9

* Sun Mar 01 2020 Athos Ribeiro <athoscr@fedoraproject.org> - 0.6.0-1
- Update version
- Skip tests due to missing dependency

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.1-5
- Enable python dependency generator

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-4
- Subpackage python2-defcon has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-2
- Rebuilt for Python 3.7

* Tue Apr 10 2018 Athos Ribeiro <athoscr@fedoraproject.org> - 0.5.1-1
- Update version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 7 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.3.5-1
- Update version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 7 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.3.4-1
- Update version

* Wed May 24 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.3.3-1
- Update version

* Mon Apr 3 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.3.2-1
- Update version

* Sun Mar 19 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.2.5-3
- Depends on the lowercase version of ufolib

* Sun Mar 19 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.2.5-2
- Improve %%description
- Remove the sum global

* Sat Mar 18 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0.2.5-1
- Initial package
