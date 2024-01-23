Name:           purple-mm-sms
Version:        0.1.7
Release:        8%{?dist}
Summary:        A libpurple plugin for sending and receiving SMS via ModemManager

License:        GPLv3+
URL:            https://source.puri.sm/Librem5/purple-mm-sms
Source0:        https://source.puri.sm/Librem5/purple-mm-sms/-/archive/v%{version}/%{name}-v%{version}.tar.gz

# Until the next release which contains this in the source
Source1:        COPYING

BuildRequires:  gcc
BuildRequires:  pkgconfig(purple)
BuildRequires:  pkgconfig(mm-glib)

# By default, the library file is installed with 0644, which breaks debuginfo.
# https://source.puri.sm/Librem5/purple-mm-sms/-/merge_requests/24
Patch0: install-library-with-correct-permissions.patch

%description
A libpurple plugin for sending and receiving SMS via ModemManager

%prep
%autosetup -p1 -n %{name}-v%{version}

# Temporary until the next release which contains this license
cp %{SOURCE1} .

%build
%set_build_flags
%make_build

%install
%make_install

%files
%{_libdir}/purple-2/mm-sms.so
%{_datadir}/pixmaps/*
%doc README.md
%license COPYING

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jan 29 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 0.1.7-2
- Update for initial push

* Sun Aug 16 2020 Nikhil Jha <hi@nikhiljha.com> - 0.1.7-1
- Update to 0.1.7

* Thu Mar  5 2020 Nikhil Jha <hi@nikhiljha.com> - 0.1.3-1
- Initial packaging
