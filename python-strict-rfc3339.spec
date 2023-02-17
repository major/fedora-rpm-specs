%global _description %{expand:
Goals:
- Convert UNIX timestamps to and from RFC3339.
- Either produce RFC3339 strings with a UTC offset (Z) or with the offset that
  the C time module reports is the local timezone offset.
- Simple with minimal dependencies/libraries.
- Avoid timezones as much as possible.
- Be very strict and follow RFC3339.}

Name:           python-strict-rfc3339
Version:        0.7
Release:        9%{?dist}
Summary:        Strict, simple, lightweight RFC3339 functions

License:        GPL-3.0-only
URL:            https://github.com/danielrichman/strict-rfc3339
Source:         %{pypi_source strict-rfc3339}
BuildArch:      noarch

BuildRequires:  python3-devel


%description %{_description}


%package -n     python3-strict-rfc3339
Summary:        %{summary}


%description -n python3-strict-rfc3339 %{_description}


%prep
%autosetup -n strict-rfc3339-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files strict_rfc3339


%check
%pyproject_check_import


%files -n python3-strict-rfc3339 -f %{pyproject_files}
%doc README.md


%changelog
* Wed Feb 15 2023 Carl George <carl@george.computer> - 0.7-9
- Convert to pyproject macros

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.7-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 08 2020 Aurelien Bompard <abompard@fedoraproject.org> - 0.7-1
- Initial package.
