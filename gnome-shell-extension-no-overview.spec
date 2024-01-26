%global extension   no-overview
%global uuid        %{extension}@fthx

Name:           gnome-shell-extension-%{extension}
Version:        16
Release:        3%{?dist}
Summary:        GNOME Shell extension for no overview at start-up
License:        GPL-3.0-only
URL:            https://extensions.gnome.org/extension/4099/no-overview/
Source0:        https://extensions.gnome.org/extension-data/no-overviewfthx.v%{version}.shell-extension.zip
Source1:        https://raw.githubusercontent.com/fthx/no-overview/main/LICENSE#/%{extension}-LICENSE
Source2:        https://raw.githubusercontent.com/fthx/no-overview/main/README.md#/%{extension}-README.md
#Patch0:         %%{name}-HEAD.patch
BuildArch:      noarch
# rhbz#2001561 Delete to require gnome-shell-extension-common
#Requires:       gnome-shell-extension-common
Recommends:     gnome-extensions-app
BuildRequires:  git


%description
GNOME Shell extension for no overview at start-up. For GNOME Shell 40+.

%prep
%autosetup -cn %{name}-%{version} -S git
cp -p %SOURCE1 LICENSE
cp -p %SOURCE2 README.md

%build
# Nothing to build here

%install
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

# install main extension files
cp -rp *.js metadata.json \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

%files
%doc README.md
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}


%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 22 2023 Takao Fujiwara <tfujiwar@redhat.com> - 16-1
- Bump to 16

* Fri Sep 22 2023 Takao Fujiwara <tfujiwar@redhat.com> - 15-1
- Bump to 15

* Thu Aug 17 2023 Takao Fujiwara <tfujiwar@redhat.com> - 13-3
- Add gnome-shell-45

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 04 2023 Takao Fujiwara <tfujiwar@redhat.com> - 13-1
- Bump to 13

* Tue Feb 21 2023 Takao Fujiwara <tfujiwar@redhat.com> - 12-3
- Add gnome-shell-44

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Takao Fujiwara <tfujiwar@redhat.com> - 12-1
- Migrate license tag to SPDX
- Bump to 12

* Sat Aug 13 2022 Takao Fujiwara <tfujiwar@redhat.com> - 11-4
- Add gnome-shell-43

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Takao Fujiwara <tfujiwar@redhat.com> - 11-1
- Bump to 11

* Tue Jan 18 2022 Takao Fujiwara <tfujiwar@redhat.com> - 8-90
- Add gnome-shell-42

* Tue Sep 07 2021 Takao Fujiwara <tfujiwar@redhat.com> - 8-4
- Workaround #2001561 Delete to require gnome-shell-extension-common

* Tue Aug 24 2021 Takao Fujiwara <tfujiwar@redhat.com> - 8-3
- Add gnome-shell-41

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Takao Fujiwara <tfujiwar@redhat.com> - 8-1
- Resolves #1969604 activates after unlock

* Wed Apr 14 2021 Takao Fujiwara <tfujiwar@redhat.com> - 4-1
- Initial integration
