%global srcname json-minify
%global srcname_ json_minify
%global Srcname_ JSON_minify

Name:           python-%{srcname}
Version:        0.3.0
Release:        26%{?dist}
Summary:        Python port of the JSON-minify utility

License:        MIT
URL:            https://github.com/getify/JSON.minify/tree/python
Source:         %pypi_source %{Srcname_}
# Fix invalid escape sequences in regex strings.
Patch:          https://github.com/getify/JSON.minify/pull/74.patch

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
JSON-minify minifies blocks of JSON-like content into valid JSON by removing
all whitespace *and* JS-style comments. With JSON-minify, you can maintain
developer-friendly JSON documents, but minify them before parsing or
transmitting them over-the-wire.


%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{srcname}
JSON-minify minifies blocks of JSON-like content into valid JSON by removing
all whitespace *and* JS-style comments. With JSON-minify, you can maintain
developer-friendly JSON documents, but minify them before parsing or
transmitting them over-the-wire.


%prep
%autosetup -n %{Srcname_}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{srcname_}

%check
%{python3} -m unittest discover

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 0.3.0-25
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 30 2024 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-23
- Switch to modern Python packaging macros
- Backport patch to fix invalid escape sequences

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.0-21
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3.0-17
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-15
- Drop support for i686

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.0-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.0-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-1
- Initial package.
