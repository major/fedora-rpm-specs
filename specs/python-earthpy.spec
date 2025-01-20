%bcond tests 1

%global _description %{expand:
EarthPy makes it easier to plot and manipulate spatial data in Python.}

Name:           python-earthpy
Version:        0.9.4
Release:        14%{?dist}
Summary:        A package built to support working with spatial data

License:        BSD-3-Clause
URL:            https://github.com/earthlab/earthpy
Source0:        %{url}/archive/v%{version}/earthpy-%{version}.tar.gz

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description %_description

%package -n python3-earthpy
Summary:        %{summary}

BuildRequires:  python3-devel

# See: https://github.com/earthlab/earthpy/blob/v0.9.4/dev-requirements.txt

#For tests
BuildRequires:  python3dist(pytest)

%description -n python3-earthpy %_description

%prep
%autosetup -n earthpy-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files earthpy

%check
%if %{with tests}
# Several tests are failing
# https://github.com/earthlab/earthpy/issues/844
k="${k-}${k+ and }not test_crop_image_with_one_point_raises_error"
k="${k-}${k+ and }not test_crop_image_with_1d_extent_raises_error"
k="${k-}${k+ and }not test_hist_number_of_columns"
k="${k-}${k+ and }not test_warning_mutli_point_clip_function"
# Almost all test_io.py tests require network access.
%pytest --ignore=earthpy/tests/test_io.py -k "${k-}"
%endif

%files -n python3-earthpy -f %{pyproject_files}
%doc README.md paper.md examples/ CHANGELOG.rst
%doc CODE_OF_CONDUCT.rst CONTRIBUTING.rst CONTRIBUTORS.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Python Maint <python-maint@redhat.com> - 0.9.4-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.4-9
- Rebuild for Python 3.12b4

* Tue Jun 27 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.9.4-8
- Update License to SPDX
- Port to pyproject-rpm-macros
- Drop docs build conditional; it is unlikely we will ever fix the doc build
- Use new (rpm 4.17.1+) bcond style

* Sat Feb 04 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.9.4-7
- Skip several tests that are currently failing (close RHBZ#2148632)
- Remove spurious BR on pytest-cov

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.4-5
- Drop support for i686

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Python Maint <python-maint@redhat.com> - 0.9.4-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 7 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.9.4-1
- Update to the latest upstream's release

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.2-3
- Rebuilt for Python 3.10

* Fri May 21 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.9.2-2
- Install additional docs

* Sat May 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.9.2-1
- Initial package
