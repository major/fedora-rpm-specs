Name:		fedora-flathub-remote
Version:	1
Release:	10%{dist}
Summary:	Third party remote pointing to a filtered version of flathub.org

License:	MIT
URL:		https://pagure.io/fedora-flathub-filter
Source0:	LICENSE
Source1:	fedora-flathub.filter
Source2:	fedora-flathub.conf
Source3:	fedora-flathub.flatpakrepo

BuildArch:	noarch

Requires:	fedora-third-party
Requires:	flatpak

%description
This package adds configuration to add a remote pointing to flathub.org when
third-party repositories are enabled on a Fedora Linux system. This remote is
filtered to include only specific Fedora-approved packages. (If the user
installs the Flathub remote manually, the filter is removed, and the flathub
remote is no longer managed as a third-party repository.)


%prep

%build

%install
install -D -m0644 %{SOURCE0} %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

install -D -m0644 %{SOURCE1} %{buildroot}%{_datadir}/flatpak/fedora-flathub.filter
install -D -m0644 %{SOURCE2} -t %{buildroot}%{_prefix}/lib/fedora-third-party/conf.d
install -D -m0644 %{SOURCE3} -t %{buildroot}%{_prefix}/lib/fedora-third-party/conf.d


%files
%license LICENSE
%{_datadir}/flatpak/fedora-flathub.filter
%{_prefix}/lib/fedora-third-party/conf.d/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb  7 2023 Matthias Clasen <mclasen@redhat.com> - 1-5
- Incorporate changes for https://fedoraproject.org/wiki/Changes/UnfilteredFlathub

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 2 2021 Owen Taylor <otaylor@redhat.com> - 1-1
- Initial version
