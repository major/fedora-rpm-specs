Name:           micronucleus
Version:        2.04
Release:        12%{?dist}
Summary:        Flashing tool for USB devices with Micronucleus bootloader

# The only thing that we package -- the command line tool -- has a MIT
# license block in each file. There's a License.txt (GPLv2 or GPLv3),
# but it's for different code. Oh well.
License:        MIT
URL:            https://github.com/micronucleus/micronucleus
Source0:        https://codeload.github.com/micronucleus/micronucleus/tar.gz/%{version}#/micronucleus-%{version}.tar.gz
Source1:        60-micronucleus.rules

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libusb)
BuildRequires:  systemd-rpm-macros
Requires:       systemd-udev

%description
This package ships a "micronucleus" command line tool. It is used to upload
programs to AVR ATtiny devices that utilize the Micronucleus boot loader.


%prep
%setup -q


%build
# The supplied Makefile doesn't do anything useful. It sets compiler flags
# in a way that disallows overrides and then declares a patterns that
# defeat lazy compilation. Oh well.
cc -o micronucleus -Icommandline/library \
        %{optflags} $(pkg-config --cflags --libs libusb) \
        commandline/library/littleWire_util.c \
        commandline/library/micronucleus_lib.c \
        commandline/micronucleus.c


%install
mkdir -p %{buildroot}%{_bindir}
install -pm0755 micronucleus %{buildroot}%{_bindir}

# Upstream ships some attempt at udev rules, but they essentially consist
# of comments that are not true and chmod 666. Oh well.
mkdir -p %{buildroot}%{_udevrulesdir}
install -pm644 %{SOURCE1} %{buildroot}%{_udevrulesdir}


%files
%{_bindir}/micronucleus
%{_udevrulesdir}/60-micronucleus.rules
%doc commandline/Readme


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Lubomir Rintel <lkundrak@v3.sk> - 2.04-1
- Initial packaging
