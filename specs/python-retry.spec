Name:           python-retry
Version:        0.9.4
Release:        9%{?dist}
Summary:        Easy to use retry decorator

License:        Apache-2.0
URL:            https://github.com/eSAMTrade/retry
Source:         %{url}/archive/%{version}/retry-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# https://github.com/eSAMTrade/retry/pull/7
# https://github.com/eSAMTrade/retry/pull/8
Patch:          fix_requirements.patch

%global _description %{expand:
Easy to use retry decorator}

%description %_description

%package -n python3-retry
Summary:        %{summary}

%description -n python3-retry %_description


%prep
%autosetup -n retry-%{version}

%generate_buildrequires
export PBR_VERSION="%{version}"
%pyproject_buildrequires -t


%build
export PBR_VERSION="%{version}"
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files retry


%check
%tox


%files -n python3-retry -f %{pyproject_files}
%doc README.* ChangeLog AUTHORS
%license LICENSE


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.4-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.9.4-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Jonathan Wright <jonathan@almalinux.org> - 0.9.4-1
- Change upstream to https://github.com/eSAMTrade/retry
- Update to 0.9.4

* Tue Aug 23 2022 Jonathan Wright <jonathan@almalinux.org> - 0.9.2-2
- Add patch to build properly on EPEL9

* Sun Aug 07 2022 Jonathan Wright <jonathan@almalinux.org> - 0.9.2-1
- Initial package build
- rhbz#2116246
