Name:           python-pyclip
Version:        0.7.0
Release:        10%{?dist}
Summary:        Cross-platform Clipboard module for Python with binary support

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/spyoungtech/pyclip
Source:         %{url}/archive/v%{version}/pyclip-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description \
Cross-platform Clipboard module for Python with binary support

%description %{_description}

%package -n     python3-pyclip
Summary:        %{summary}

%description -n python3-pyclip %{_description}

%prep
%autosetup -p1 -n pyclip-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyclip

%files -n python3-pyclip -f %{pyproject_files}
%license LICENSE
%doc docs/README.md
%{_bindir}/pyclip

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.0-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.7.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.7.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 03 2022 Alessandro Astone <ales.astone@gmail.com> - 0.7.0-1
- Update to v0.7.0

* Sat Mar 19 2022 Alessandro Astone <ales.astone@gmail.com> - 0.6.0-1
- Update to v0.6.0

* Tue Mar 08 2022 Alessandro Astone <ales.astone@gmail.com> - 0.5.4-2
- Use wl-clipboard

* Mon Mar 07 2022 Alessandro Astone <ales.astone@gmail.com> - 0.5.4-1
- Initial RPM release
