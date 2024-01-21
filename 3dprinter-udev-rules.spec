Name:           3dprinter-udev-rules
Version:        0.3
Release:        5%{?dist}
Summary:        Rules for udev to give regular users access to operate 3D printers
License:        MIT-0
URL:            https://github.com/hroncok/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz
BuildArch:      noarch

# For the %%_udevrulesdir macro
BuildRequires:  systemd

# For the directory
Requires:       systemd-udev

%global file_name 66-3dprinter.rules

%description
Normally, when you connect a RepRap like 3D printer to a Linux machine by an
USB cable, you need to be in dialout or similar group to be able to control
it via OctoPrint, Printrun, Cura or any other control software. Not any more.

Install this rule to grant all users read and write access to collected
devices based on the VID and PID.

Disclaimer: Such device might not be a 3D printer, it my be an Arduino, it
might be a modem and it might even be a blender. But normally you would
add your user to dialout and get access to all of those and more anyway.
So I guess be careful when some of the users should not get access to
your blenders.

%prep
%setup -q

%build
# nothing

%install
install -D -p -m 644 %{file_name} %{buildroot}%_udevrulesdir/%{file_name}

%post
%udev_rules_update

%postun
%udev_rules_update

%files
%doc README.md
%license LICENSE
%_udevrulesdir/%{file_name}

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 25 2022 Miro Hrončok <mhroncok@redhat.com> - 0.3-1
- Update to 0.3
- License changed to MIT-0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 12 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-1
- Update to 0.2.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Thu Sep 08 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2-1
- Update to 0.2, with more strict rules rhbz#1370782

* Sat Mar 05 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-2
- Require systemd-udev, that now owns the directory

* Fri Feb 26 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1-1
- Initial package
