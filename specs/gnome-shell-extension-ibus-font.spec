%global uuid          ibus-font-setting@ibus.github.com
%global shortname     ibus-font
%global snapshot_date 20230705

Name:       gnome-shell-extension-%{shortname}
Version:    0.%{snapshot_date}
Release:    6%{?dist}
Summary:    A GNOME Shell extension for ibus-setup custom font settings

License:    GPL-3.0-or-later
URL:        https://extensions.gnome.org/extension/1121/ibus-font-setting/
Source0:    https://pwu.fedorapeople.org/ibus/ibus-font-setting/%{name}-%{snapshot_date}.tar.gz
BuildArch:  noarch

Requires:   gnome-shell
Requires:   ibus

%description
use ibus font setting of ibus setup dialog to enhance the user experience

%prep
%setup -q -c

%build
# None

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
install -Dp -m 0644 {extension.js,metadata.json,prefs.js,stylesheet.css} \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

%files
%license COPYING
%{_datadir}/gnome-shell/extensions/%{uuid}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.20230705-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20230705-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20230705-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20230705-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20230705-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul  6 2023 Peng Wu <pwu@redhat.com> - 0.20230705-1
- Update the package

* Mon Apr 24 2023 Peng Wu <pwu@redhat.com> - 0.20210510-6
- Migrate to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20210510-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20210510-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20210510-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20210510-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 10 2021 Peng Wu <pwu@redhat.com> - 0.20210510-1
- Update the package

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20200831-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Peng Wu <pwu@redhat.com> - 0.20200831-1
- Update the package

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20170217-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20170217-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20170217-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20170217-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20170217-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20170217-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 13 2017 Peng Wu <pwu@redhat.com> - 0.20170217-2
- Import SRPM

* Fri Feb 17 2017 Kermit Wang <kermitwang@163.com> - 0.20170217-1
- Initialize package for Fedora.
