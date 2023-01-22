Name:           python-pyclip
Version:        0.7.0
Release:        2%{?dist}
Summary:        Cross-platform Clipboard module for Python with binary support

License:        ASL 2.0
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
