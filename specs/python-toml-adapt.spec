%bcond_without tests

%global original_name toml-adapt
%global pretty_name toml_adapt

%global _description %{expand:
Working with TOML files is becoming inevitable during the package maintenance
process in different ecosystems. Many times package maintainers must either
change the version of dependency or add/remove dependencies when building
their packages, due to the inconsistent base system. For example, solving
this issue can be done either by using the provided patches or using sed
commands. However, this may be slightly time-consuming and irritating. A
very simple yet user-friendly command line interface was developed in
order to make this process easier.}

Name:           python-%{original_name}
Version:        0.3.4
Release:        1%{?dist}
Summary:        A simple command-line interface for manipulating toml files

# SPDX
License:        MIT
URL:            https://github.com/firefly-cpp/%{original_name}
Source0:        %{url}/archive/%{version}/%{original_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{original_name}
Summary:        %{summary}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description -n python3-%{original_name} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{original_name}-%{version}
rm -fv poetry.lock

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pretty_name}

install -D -t '%{buildroot}%{_mandir}/man1' -m 0644 %{original_name}.1

%check
# use smoke tests
%pyproject_check_import

# unit tests
%pytest

%files -n python3-%{original_name} -f %{pyproject_files}
%{_bindir}/%{original_name}
%license LICENSE
%doc README.md AUTHORS.rst CODE_OF_CONDUCT.md CHANGELOG.md CITATION.cff
%{_mandir}/man1/%{original_name}.1*
 
%changelog
* Tue Feb 4 2025 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.4-1
- Update to the latest upstream's release

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.3.3-2
- Rebuilt for Python 3.13

* Sun Mar 24 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.3-1
- Update to the latest upstream's release

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 15 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.0-1
- Update to the latest upstream's release

* Mon Nov 13 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.12-1
- Update to the latest upstream's release

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.2.11-2
- Rebuilt for Python 3.12

* Fri Feb 24 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.11-1
- Update to the latest upstream's release

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 2 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.10-1
- Update to the latest upstream's release

* Sun Oct 9 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.9-1
- Update to the latest upstream's release

* Sun Sep 11 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.8-1
- Update to the latest upstream's release

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.2.7-2
- Rebuilt for Python 3.11

* Thu May 26 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.7-1
- Update to the latest upstream's release

* Mon May 23 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.6-1
- Update to the latest upstream's release

* Mon Feb 28 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.5-1
- Update to the latest upstream's release

* Sat Jan 29 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.4-1
- Update to the latest upstream's release
- Enable unit tests

* Tue Jan 25 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.3-1
- Update to the latest release

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.1-1
- Update to the latest release

* Fri Jan 14 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.0-4
- Improve description

* Thu Jan 13 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.0-3
- Update doc section with new documents

* Thu Jan 13 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.0-2
- Enable smoke tests

* Thu Jan 13 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.0-1
- Update to the latest release

* Wed Oct 27 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.6-1
- Update to the latest release

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.5-1
- Update to the latest release

* Wed Jun 30 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.4-1
- Update to the latest release

* Tue Jun 22 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.3-1
- Update to the latest release

* Wed Jun 09 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.1.2-1
- Update to 0.1.2 (fixes man page installed in %%{python3_sitelib})
- Fix permissions on installed man page

* Tue Jun 8 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.1-1
- Update to the latest release
- Add man page

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 0.1.0-2
- Rebuilt for Python 3.10

* Tue Jun 1 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.1.0-1
- Initial package
