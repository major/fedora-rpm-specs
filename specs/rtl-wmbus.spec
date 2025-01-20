%global with_tag       0

Name:                  rtl-wmbus
%global forgeurl       https://github.com/xaelsouth/%{name}
%global the_binary     rtl_wmbus

%if %{with_tag}
%global tag            0.0.0
Version:               %{tag}
%else
%global date           20240118
%global commit         20cafdcecf28121cb4d5546cfe9cbc1822a70a03
Version:               0
%endif

%forgemeta

Release:               22%{?dist}
Summary:               Software defined receiver for wireless M-Bus with RTL-SDR
# Automatically converted from old format: BSD - review is highly recommended.
License:               LicenseRef-Callaway-BSD
Url:                   %{forgeurl}
Source0:               %{forgesource}

BuildRequires:         make
BuildRequires:         /usr/bin/git
BuildRequires:         gcc
BuildRequires:         fixedptc-devel

Requires:              /usr/bin/rtl_sdr


%description
rtl-wmbus is a software defined receiver for Wireless-M-Bus.
It is written in plain C and uses RTL-SDR to interface with RTL2832-based
hardware.

Wireless-M-Bus is the wireless version of M-Bus
("Meter-Bus", http://www.m-bus.com), which is an European standard for
remote reading of smart meters.

The primary purpose of rtl-wmbus is experimenting with digital signal
processing and software radio.

rtl-wmbus can be used on resource constrained devices such as Raspberry Pi Zero
or Raspberry PI B+ overclocked to 1GHz. Any Android based tablet will do
the same too.

rtl-wmbus provides:
  - filtering
  - FSK demodulating
  - clock recovering
  - mode T1 and mode C1 packet decoding


%prep
%forgeautosetup -S git
# Remove bundled fixedptc library and build directory
rm -rf include build

# Split the LICENSE from the README.md
awk '/^  License/ {dump=1; next} \
     /^  -------/ {next} \
     /.*/         {if (dump) {print}}' \
     README.md >LICENSE


%build
%set_build_flags
export LIB="%{__global_ldflags} -lm"
%{make_build} \
    COMMIT_HASH="" \
    TAG=%{version}%{?distprefix} \
    BRANCH="" \
    CHANGES="" \
    TAG_COMMIT_HASH=""


%install
install -p -m 0755 -D build/%{the_binary} %{buildroot}%{_bindir}/%{the_binary}


%files
# The license is in the documentation file
%license LICENSE
%doc README.md
%{_bindir}/%{the_binary}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0-21
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 09 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0-19
- Rebuilt for new rtl-sdr

* Fri Feb 23 2024 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-18
- Update to the latest version

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 14 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-10
- Update to the latest version
- Prepare for supporting tagged version

* Mon Apr 19 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-9
- Remove build directory
- Pass version string to make

* Mon Apr 12 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-8.20210315gitcce47b6
- Update to the latest version
- Drop patch merged upstream

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-4.20191213git6a04c45
- Split the LICENSE from the README.md
- Remove -v from forgemeta

* Tue Mar 03 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-3.20191213git6a04c45
- Use %%set_build_flags

* Mon Mar 02 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-2.20191213git6a04c45
- Add upstream reference to patch.

* Fri Feb 28 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0-1.20191213git6a04c45
- Initial RPM release.
