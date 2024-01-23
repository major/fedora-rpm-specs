%global pypi_name EvoPreprocess
%global simple_name evopreprocess


%global _description %{expand:
EvoPreprocess is a Python toolkit for sampling datasets, instance weighting,
and feature selection. It is compatible with scikit-learn and 
imbalanced-learn packages. It is based on the NiaPy library for the 
implementation of nature-inspired algorithms.}

Name:           python-%{pypi_name}
Version:        0.5.0
Release:        5%{?dist}
Summary:        A Python Toolkit for Data Preprocessing
# We conservatively interpret “GPLv3” as GPL-3.0-only, but have requested
# explicit clarification from upstream in:
#
# Please clarify GPL version
# https://github.com/karakatic/EvoPreprocess/issues/16
License:        GPL-3.0-only
URL:            https://github.com/karakatic/%{pypi_name}
Source:         %{pypi_source evopreprocess}
            
BuildArch:      noarch

BuildRequires:  python3-devel

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{simple_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l %{simple_name}

%check
# use smoke tests
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 0.5.0-4
- Assert a license file is automatically handled; don’t package a duplicate
- Update License to SPDX

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.12

* Thu Mar 2 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.5.0-1
- Update to 0.5.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Python Maint <python-maint@redhat.com> - 0.4.6-5
- Rebuilt for Python 3.11

* Sat Apr 16 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.6-4
- Remove rm command in prep

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.6-2
- Enable smoke tests

* Sun Jan 9 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.6-1
- Update to the latest upstream's release
- Add license text

* Sat Jan 8 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.5-1
- Update to the latest upstream's release

* Sat Jan 8 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.3-3
- Switch to new source (use pypi source)

* Sat Oct 30 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.3-1
- Update to the latest upstream's release

* Fri Oct 8 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.2-6
- Reconcile niapy version with patch

* Sun Sep 26 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.2-5
- Remove patch

* Sat Sep 25 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.2-4
- Use python rpm macros

* Fri Sep 3 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.2-3
- Patch dependencies

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.2-1
- Update to the latest upstream's release

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.4-5
- Rebuilt for Python 3.10

* Mon May 10 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.4-4
- Removing some macros
- Install examples

* Sun Feb 14 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.4-3
- Removing dependency generator
- Description fixes
- BuildArch set to noarch
- Fresh rebuilt

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 26 2020 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.4-1
- Initial package
