%global snapshot 42ffc5f

Name:    sunxi-tools
Version: 1.4.2
Release: 22%{?snapshot:.%{snapshot}}%{?dist}
Summary: Tools to help hacking Allwinner (sunxi) based devices
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://linux-sunxi.org/Sunxi-tools

%if 0%{?snapshot:1}
# git archive --format=tar --prefix=%{name}-%{version}/ %{snapshot} | xz > %{name}-%{snapshot}.tar.xz
Source0: %{name}-%{snapshot}.tar.xz
%else
Source0: https://github.com/linux-sunxi/sunxi-tools/archive/v%{version}.tar.gz
%endif

BuildRequires: make
BuildRequires: gcc
BuildRequires: libusbx-devel
BuildRequires: zlib-devel

%description
This package contains various tools to help hacking Allwinner (aka sunxi) based
devices and possibly it's successors.


%prep
%autosetup -p1


%build
make %{?_smp_mflags} CFLAGS='%{optflags} -Iinclude -D_POSIX_C_SOURCE=200112L -std=c99'


%install
install -d %{buildroot}%{_bindir}
install sunxi-fel fel-gpio fex2bin sunxi-nand-part sunxi-fexc sunxi-pio %{buildroot}%{_bindir}
install sunxi-bootinfo %{buildroot}%{_bindir}/sunxi-bootinfo


%files
%license LICENSE.md
%doc README.md
%{_bindir}/*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-22.42ffc5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.2-21.42ffc5f
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-20.42ffc5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-19.42ffc5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-18.42ffc5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-17.42ffc5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-16.42ffc5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-15.42ffc5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-14.42ffc5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-13.42ffc5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-12.42ffc5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-11.42ffc5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.2-10.42ffc5f
- Move to upstream snapshot for newer SoC and SPI support

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 25 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.2-3
- Adjust build flags (fixes RHBZ #1410443)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec  7 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.2-1
- Update to 1.4.2

* Sat Oct 29 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.4.1-1
- Update to 1.4.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 17 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.3-1
- Update to 1.3

* Thu Oct 29 2015 Bastien Nocera <bnocera@redhat.com> 1.2-1.20151029git9bf1de0
- Update to latest git

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5.20140131git271130b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4.20140131git271130b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3.20140131git271130b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 06 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.1-2.20140131git271130b
- Use standard GitHub source URL (Yanko Kaneti, #1062162)
- Rename bootinfo and usb-boot (Yanko Kaneti, #1062162)
- Add a missing BR

* Thu Feb 06 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.1-1.20140131git271130b
- Initial packaging
