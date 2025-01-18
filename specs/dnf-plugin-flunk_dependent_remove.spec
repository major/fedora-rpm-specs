%{!?dnf_lowest_compatible: %global dnf_lowest_compatible 4.2.23}
%global srcname flunk_dependent_remove

%global _description %{expand:
Do not allow "dnf -y remove" to expand the list of packages to remove to
include packages which require one of the explicitly listed packages.
Fail the request instead. This is implemented via a DNF plugin.}

Name:           dnf-plugin-%{srcname}
Version:        1.0
Release:        17%{?dist}
Summary:        DNF plugin to prevent removing packages recursively via automation
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
BuildArch:      noarch
Source0:        %{srcname}.py
Source1:        LICENSE
BuildRequires:  python3-devel
BuildRequires:  python3-dnf >= %{dnf_lowest_compatible}

%description    %{_description}

%package -n     python3-%{name}
Summary:        %{summary}
Requires:       python3-dnf >= %{dnf_lowest_compatible}

%description -n python3-%{name} %{_description}

%prep
cp -p %SOURCE1 .

%install
install -D -m0644 %{SOURCE0} \
  %{buildroot}/%{python3_sitelib}/dnf-plugins/%{srcname}.py

%files -n       python3-%{name}
%license LICENSE
%{python3_sitelib}/dnf-plugins/%{srcname}.py
%{python3_sitelib}/dnf-plugins/__pycache__/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0-16
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.0-14
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.0-10
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.0-7
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Davide Cavalca <dcavalca@fb.com> - 1.0-5
- Fix specfile name to match the actual package

* Thu Aug 26 2021 Davide Cavalca <dcavalca@fb.com> - 1.0-4
- Rename to dnf-plugin-flunk-dependent-remove
- Clarify summary and description

* Thu Aug 26 2021 Davide Cavalca <dcavalca@fb.com> - 1.0-3
- Refactor description and summary
- Add license file

* Thu Feb 25 2021 Davide Cavalca <dcavalca@fb.com> - 1.0-2
- Rename source package to dnf-flunk-dependent-remove
- Add BuildRequires for python-dnf
- Fix license tag

* Fri Jun 12 2020 William Herrin <wherrin@fb.com> - 1.0-1.fb1
- initial version
