Name:           build-constraints-rpm-macros
Version:        1
Release:        9%{?dist}
Summary:        RPM macros for build constraints

License:        MIT
URL:            https://src.fedoraproject.org/rpms/%{name}
Source0:        macros.build-constraints

# license text
Source200:      LICENSE

BuildArch:      noarch

Requires:       gawk

%description
This package contains macros to constraint resource use during the build
process.


%prep
%autosetup -c -T
cp -a %{sources} .


%build


%install
%if 0%{?el7}
# install -Dt does not precreate target directory
mkdir -p %{buildroot}%{rpmmacrodir}
%endif
install -Dpm 644 -t %{buildroot}%{rpmmacrodir} macros.*


%files
%license LICENSE
%{rpmmacrodir}/macros.build-constraints


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 1-1
- Initial package
