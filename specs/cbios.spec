%define         machines %{_datadir}/openmsx/machines

Name:           cbios
Version:        0.29a
Release:        15%{?dist}
Summary:        A third party BIOS compatible with the MSX BIOS
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://cbios.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.zip
BuildArch:      noarch
BuildRequires:  sjasm
BuildRequires: make

%description
C-BIOS is a BIOS compatible with the MSX BIOS written from scratch by BouKiCHi.
It is available for free, including its source code and can be shipped with MSX
emulators so they are usable out-of-the-box without copyright issues.


# Build c-bios support for different msx emulators as sub packages, cbios has
# support for blueMSX, NLMSX, openMSX, RuMSX but at the moment we only support
# openmsx (others not available for Linux yet).
%package openmsx
Summary:        C-BIOS support for openMSX
Requires:       cbios = %{version}-%{release}
Requires:       openmsx >= 0.9.2

%description openmsx
Adds C-BIOS support for openMSX, a third party MSX compatible BIOS.


%prep
%setup -q
sed -i 's/\r//' doc/*.txt
# Character encoding fixes
iconv -f iso8859-1 doc/cbios.txt -t utf8 > doc/cbios.conv \
    && /bin/mv -f doc/cbios.conv doc/cbios.txt


%build
make %{?_smp_mflags} Z80_ASSEMBLER=sjasm


%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{machines}
install -pm 0644 derived/bin/* %{buildroot}%{_datadir}/%{name}

# Install openmsx configuration and symlinks to cbios
cp -a configs/openMSX/C-BIOS_MSX* %{buildroot}%{machines}
for i in %{buildroot}%{_datadir}/%{name}/*.rom; do
    ln -s --target-directory=%{buildroot}%{machines} \
        ../../%{name}/$(basename $i)
done


%files
%{_datadir}/%{name}
%doc doc/cbios.txt doc/chkram.txt


# We don't own the parent directories here, because they are owned by openmsx,
# also we don't set hardwareconfig.xml as %%config because they are not
# intended to be changed by the end user.
%files openmsx
%{machines}/*
%doc configs/openMSX/README.txt


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.29a-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.29a-14
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.29a-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.29a-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.29a-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.29a-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.29a-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.29a-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.29a-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.29a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.29a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.29a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Hans de Goede <hdegoede@redhat.com> - 0.29a-1
- New upstream release 0.29a

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Hans de Goede <hdegoede@redhat.com> - 0.29-1
- New upstream release 0.29 (rhbz#1547145)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Apr 20 2016 Hans de Goede <hdegoede@redhat.com> - 0.27-1
- New upstream release 0.27 (rhbz#1326651)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul  3 2009 Hans de Goede <hdegoede@redhat.com> 0.23-1
- New upstream release 0.23

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 28 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.21-3
- Really convert some documentation to UTF8 this time.

* Sun Aug 26 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.21-2
- Migration to Fedora
- Converted some documentation to UTF8

* Fri Aug 11 2006 Ian Chapman <packages[AT]amiga-hardware.com> 0.21-1
- Initial Release