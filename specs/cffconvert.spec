%bcond_without tests

%global pypi_name cffconvert
%global orig_name cff-converter-python

%global _description %{expand:
Implementation of Command-line program to validate and convert
CITATION.cff files in Python.}

Name:           %{pypi_name}
Version:        2.0.0
Release:        15%{?dist}
Summary:        Command line program to validate and convert CITATION.cff files

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/citation-file-format/%{orig_name}
Source0:        %{url}/archive/%{version}/%{orig_name}-%{version}.tar.gz

BuildArch:      noarch

# Allow jsonschema 4.x
# https://github.com/citation-file-format/cff-converter-python/pull/277
Patch:          %{url}/pull/277.patch

BuildRequires:  python3-devel
BuildRequires:  help2man

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description -n %{pypi_name} %_description

%prep
%autosetup -n %{orig_name}-%{version}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/--[^[:blank:]]*\bcov\b[^[:blank:]]*//' setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x gcloud

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l cffconvert

# man page
install -d '%{buildroot}%{_mandir}/man1'
    env PATH="${PATH}:%{buildroot}%{_bindir}" \
        PYTHONPATH='%{buildroot}%{python3_sitelib}' \
        help2man --no-info '%{pypi_name}' \
            --output='%{buildroot}%{_mandir}/man1/%{pypi_name}.1'

%check
%if %{with tests}
PYTHONPATH="${PWD}" %pytest -k "${k-}" test/
%endif

%files -n cffconvert -f %{pyproject_files}
%doc docs/ README.md CHANGELOG.md CITATION.cff CONTRIBUTING.md
%{_bindir}/%{pypi_name}
%{_mandir}/man1/%{pypi_name}.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.0-14
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2.0.0-12
- Rebuilt for Python 3.13

* Wed Apr 03 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.0.0-11
- Fix pytest 8 compatibility and failing tests (close RHBZ#2272969)

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.0.0-8
- Assert a license file is automatically handled; don’t package a duplicate

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 2.0.0-6
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 2.0.0-3
- Allow jsonschema 4.x (fix RHBZ#2101851)

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 2.0.0-2
- Rebuilt for Python 3.11

* Mon May 9 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 2.0.0-1
- Initial package
