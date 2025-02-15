#%%global git_commit c52f3f41806622c95573de21be042f966f675543
#%%global git_date 201904023

#%%global git_short_commit %%(echo %{git_commit} | cut -c -8)
#%%global git_suffix %%{git_date}git%{git_short_commit}

# By default include binary_firmware, otherwise try to rebuild
# the firmware from sources. If you want to rebuild all firmware
# images you need to install appropriate tools (e.g. Xilinx ISE).
%bcond_without binary_firmware

# Currently broken: https://github.com/EttusResearch/uhd/issues/413
%bcond_with wireshark

# NEON support is by default disabled on ARMs
# building with --with=neon will enable auto detection
%bcond_with neon

# X.Y.Z
%global wireshark_ver_full %((%{__awk} '/^#define VERSION[ \t]+/ { print $NF }' /usr/include/wireshark/config.h 2>/dev/null||echo none)|/usr/bin/tr -d '"')
# X.Y
%global wireshark_ver %(VF="%{wireshark_ver_full}"; echo ${VF%.*})

%ifarch %{arm} aarch64
%if ! %{with neon}
%global have_neon -DHAVE_ARM_NEON_H=0
%endif
%endif

Name:           uhd
URL:            http://github.com/EttusResearch/uhd
Version:        4.7.0.0
%global images_ver %{version}
Release:        5%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  libusb1-devel
BuildRequires:  python3-cheetah
BuildRequires:  ncurses-devel
BuildRequires:  python3-docutils
BuildRequires:  doxygen
BuildRequires:  pkgconfig
BuildRequires:  libpcap-devel
BuildRequires:  python3-numpy
BuildRequires:  vim-common
BuildRequires:  libatomic
%if %{with wireshark}
BuildRequires:  wireshark-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  gnutls-devel
%endif
BuildRequires:  pybind11-devel
BuildRequires:  python3-mako
BuildRequires:  python3-requests
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  tar
%if ! %{with binary_firmware}
BuildRequires:  sdcc
BuildRequires:  sed
%endif
Requires(pre):  glibc-common
Requires:       python3-tkinter
Summary:        Universal Hardware Driver for Ettus Research products
Source0:        %{url}/archive/v%{version}/uhd-%{version}.tar.gz
Source1:        %{name}-limits.conf
Source2:        %{url}/releases/download/v%{images_ver}/uhd-images_%{images_ver}.tar.xz
# dirty workaround for the https://github.com/EttusResearch/uhd/issues/551
# until the better fix is available
Patch0:         uhd-4.2.0.0-imagepath-fix.patch

%description
The UHD is the universal hardware driver for Ettus Research products.
The goal of the UHD is to provide a host driver and API for current and
future Ettus Research products. It can be used standalone without GNU Radio.

%package firmware
Summary:        Firmware files for UHD
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description firmware
Firmware files for the Universal Hardware driver (UHD).

%package devel
Summary:        Development files for UHD
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for the Universal Hardware Driver (UHD).

# arch due to bug in doxygen
%package doc
Summary:        Documentation files for UHD

%description doc
Documentation for the Universal Hardware Driver (UHD).

%package tools
Summary:        Tools for working with / debugging USRP device
Requires:       %{name} = %{version}-%{release}

%description tools
Tools that are useful for working with and/or debugging USRP device.

%if %{with wireshark}
%package wireshark
Summary:        Wireshark dissector plugins
Requires:       %{name} = %{version}-%{release}
Requires:       %{_libdir}/wireshark/plugins/%{wireshark_ver}

%description wireshark
Wireshark dissector plugins.
%endif

%prep
%setup -q
%patch -P0 -p1 -b .imagepath-fix

# firmware
%if %{with binary_firmware}
# extract binary firmware
mkdir -p images/images
tar -xJf %{SOURCE2} -C images/images --strip-components=1
rm -f images/images/{LICENSE.txt,*.tag}
# remove Windows drivers
rm -rf images/winusb_driver
%endif

# fix python shebangs
find . -type f -name "*.py" -exec sed -i '/^#!/ s|.*|#!%{__python3}|' {} \;

# Create a sysusers.d config file
cat >uhd.sysusers.conf <<EOF
g usrp -
EOF

%build
# firmware
%if ! %{with binary_firmware}
# rebuilt from sources
export PATH=$PATH:%{_libexecdir}/sdcc
pushd images
sed -i '/-name "\*\.twr" | xargs grep constraint | grep met/ s/^/#/' Makefile
make %{?_smp_mflags} images
popd
%endif

pushd host
%cmake %{?have_neon} -DPYTHON_EXECUTABLE="%{__python3}" \
  -DPYBIND11_INCLUDE_DIR="/usr/include/pybind11/" \
  -DUHD_VERSION="%{version}" \
  -DENABLE_TESTS=off ../
%cmake_build
popd

# tools
pushd tools/uhd_dump
make %{?_smp_mflags} CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}"
popd

%if %{with wireshark}
# wireshark dissectors
pushd tools/dissectors
%cmake -DENABLE_RFNOC=ON -DENABLE_OCTOCLOCK=ON -DENABLE_ZPU=ON
%cmake_build
popd
%endif

#%%check
#cd host/%%{_vpath_builddir}
#make test

%install
# fix python shebangs (run again for generated scripts)
find . -type f -name "*.py" -exec sed -i '/^#!/ s|.*|#!%{__python3}|' {} \;

pushd host
%cmake_install

# Fix udev rules and use dynamic ACL management for device
sed -i 's/BUS==/SUBSYSTEM==/;s/SYSFS{/ATTRS{/;s/MODE:="0666"/GROUP:="usrp", MODE:="0660", ENV{ID_SOFTWARE_RADIO}="1"/' %{buildroot}%{_libdir}/uhd/utils/uhd-usrp.rules
mkdir -p %{buildroot}%{_prefix}/lib/udev/rules.d
mv %{buildroot}%{_libdir}/uhd/utils/uhd-usrp.rules %{buildroot}%{_prefix}/lib/udev/rules.d/10-usrp-uhd.rules

# Remove tests, examples binaries
rm -rf %{buildroot}%{_libdir}/uhd/{tests,examples}

# Move the utils stuff to libexec dir
mkdir -p %{buildroot}%{_libexecdir}/uhd
mv %{buildroot}%{_libdir}/uhd/utils/* %{buildroot}%{_libexecdir}/uhd

popd
# Package base docs to base package
mkdir _tmpdoc
mv %{buildroot}%{_docdir}/%{name}/{LICENSE,README.md} _tmpdoc

install -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/security/limits.d/99-usrp.conf

# firmware
mkdir -p %{buildroot}%{_datadir}/uhd/images
cp -r images/images/* %{buildroot}%{_datadir}/uhd/images

# remove win stuff
rm -rf %{buildroot}%{_datadir}/uhd/images/winusb_driver

# convert hardlinks to symlinks (to not package the file twice)
pushd %{buildroot}%{_bindir}
for f in uhd_images_downloader usrp2_card_burner
do
  unlink $f
  ln -s ../..%{_libexecdir}/uhd/${f}.py $f
done
popd

# tools
install -Dpm 0755 tools/usrp_x3xx_fpga_jtag_programmer.sh %{buildroot}%{_bindir}/usrp_x3xx_fpga_jtag_programmer.sh
install -Dpm 0755 tools/uhd_dump/chdr_log %{buildroot}%{_bindir}/chdr_log

%if %{with wireshark}
# wireshark dissectors
pushd tools/dissectors
%cmake_install
popd
# fix wireshark dissectors location
mkdir -p %{buildroot}%{_libdir}/wireshark/plugins/%{wireshark_ver}
mv %{buildroot}%{_prefix}/epan %{buildroot}%{_libdir}/wireshark/plugins/%{wireshark_ver}
%endif

# add directory for modules
mkdir -p %{buildroot}%{_libdir}/uhd/modules

install -m0644 -D uhd.sysusers.conf %{buildroot}%{_sysusersdir}/uhd.conf

%ldconfig_scriptlets


%files
%exclude %{_docdir}/%{name}/doxygen
%exclude %{_datadir}/uhd/images
%doc _tmpdoc/*
%dir %{_libdir}/uhd
%{_bindir}/usrpctl
%{_bindir}/uhd_*
%{_bindir}/usrp2_*
%{_bindir}/rfnoc_image_builder
%{_bindir}/usrp_hwd.py
%{_prefix}/lib/udev/rules.d/10-usrp-uhd.rules
%config(noreplace) %{_sysconfdir}/security/limits.d/*.conf
%{_libdir}/lib*.so.*
%{_libdir}/uhd/modules
%{_libexecdir}/uhd
%{_mandir}/man1/*.1*
%{_datadir}/uhd
%{python3_sitearch}/uhd
%{python3_sitearch}/usrp_mpm
%{_sysusersdir}/uhd.conf

%files firmware
%dir %{_datadir}/uhd/images
%{_datadir}/uhd/images/*

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/cmake/uhd/*.cmake
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{_docdir}/%{name}/doxygen

%files tools
%doc tools/README.md
%{_bindir}/usrp_x3xx_fpga_jtag_programmer.sh
%{_bindir}/chdr_log

%if %{with wireshark}
%files wireshark
%{_libdir}/wireshark/plugins/%{wireshark_ver}/epan/*
%endif

%changelog
* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.7.0.0-5
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 4.7.0.0-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 4.7.0.0-1
- New version
  Resolves: rhbz#2293732

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 4.6.0.0-4
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 4.6.0.0-2
- Rebuilt for Boost 1.83

* Tue Nov 21 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.6.0.0-1
- New version
  Resolves: rhbz#2247579

* Mon Sep 25 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.5.0.0-1
- New version
  Resolves: rhbz#2237074

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 4.4.0.0-3
- Rebuilt for Python 3.12

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 4.4.0.0-2
- Rebuilt for Boost 1.81

* Wed Feb  1 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 4.4.0.0-1
- New version
  Resolves: rhbz#2164284

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 24 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.3.0.0-1
- New version
  Resolves: rhbz#2124734

* Fri Jul 29 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.0.1-1
- New version
  Resolves: rhbz#2110023

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.0.0-3
- Rebuilt for new python
  Resolves: rhbz#2099182

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 4.2.0.0-2
- Rebuilt for Boost 1.78

* Thu Apr 21 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.2.0.0-1
- New version
  Resolves: rhbz#2073640

* Tue Feb  1 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.0.5-5
- Switched to the upstream patch to fix compilation on the s390x

* Fri Jan 28 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.0.5-4
- Fixed images path

* Fri Jan 28 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.0.5-3
- Defuzzified s390x patch

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.0.5-1
- New version
  Resolves: rhbz#2029036

* Mon Oct  4 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.0.4-1
- New version
  Resolves: rhbz#2006293

* Mon Sep 13 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.0.2-1
- New version
  Resolves: rhbz#1989976

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 4.1.0.1-3
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 14 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.0.1-1
- New version
  Resolves: rhbz#1982075

* Thu Jul  1 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.1.0.0-1
- New version
  Resolves: rhbz#1976430

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.0.0.0-4
- Rebuilt for Python 3.10

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 4.0.0.0-3
- Rebuilt for removed libstdc++ symbol (#1937698)

* Mon Feb  8 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.0.0.0-2
- Fixed requires for wireshark plugin
  Resolves: rhbz#1925577

* Mon Jan 25 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 4.0.0.0-1
- New version
  Resolves: rhbz#1918161

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 3.15.0.0-0.10.rc2
- Rebuilt for Boost 1.75

* Fri Dec  4 2020 Jeff Law <law@redhat.com> - 3.15.0.0-0.9.rc2
- Fix missing #includes for gcc-11

* Wed Aug  5 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 3.15.0.0-0.8.rc2
- Fixed FTBFS
  Resolves: rhbz#1865590
- Made doc arch due to bug in doxygen

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.0.0-0.7.rc2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.0.0-0.6.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Jonathan Wakely <jwakely@redhat.com> - 3.15.0.0-0.5.rc2
- Rebuilt and patched for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.15.0.0-0.4.rc2
- Rebuilt for Python 3.9

* Thu Apr 16 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 3.15.0.0-0.3.rc2
- Provided uhd modules directory

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.0.0-0.2.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov  8 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 3.15.0.0-0.1.rc2
- New version
- Switched to Python 3
  Resolves: rhbz#1738157

* Fri Aug  2 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 3.14.1.0-1
- New version
- Disabled tests
  Resolves: rhbz#1736932

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0.0-3.201904023gitc52f3f41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 3.14.0.0-2.201904023gitc52f3f41
- New git snapshot
- Added python2-numpy build requirement
- Re-enabled tests for upstream to easily reproduce the problem

* Mon Apr 15 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 3.14.0.0-1.20190401gitac96d055
- New version, switched to git snapshot
- Conditionalized wireshark support
- Disabled wireshark support, it's currently broken (upstream ticket #268)
- Disabled tests, it's currently broken (upstream ticket #267)
- Dropped boost169 patch (not needed)

* Mon Apr  1 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 3.12.0.0-5
- Re-introduced usrp group
  Resolves: rhbz#1694665

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Jonathan Wakely <jwakely@redhat.com> - 3.12.0.0-3
- Add upstream patches for Boost 1.69.0 header changes

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 3.12.0.0-3
- Rebuilt for Boost 1.69

* Mon Dec 10 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 3.12.0.0-2
- Rebuilt for new gnuradio
  Resolves: rhbz#1625012
- Fixed python shebangs

* Fri Jul 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 3.12.0.0-1
- New version
  Resolves: rhbz#1606606
- Dropped sdcc-3-fix patch (upstreamed)
- Dropped boost-gcc8-compile-fix patch (not needed)
- Packaged wireshark dissectors

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.10.3.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.10.3.0-2
- Escape macros in %%changelog

* Fri Feb  2 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 3.10.3.0-1
- New version

* Fri Feb  2 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 3.10.1.0-10
- Rebuilt for new boost

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 3.10.1.0-9
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 3.10.1.0-6
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 3.10.1.0-5
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Jonathan Wakely <jwakely@redhat.com> - 3.10.1.0-2
- Rebuilt for Boost 1.63

* Tue Nov 22 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 3.10.1.0-1
- New version
- Dropped base64-decode-fix-off-by-one patch (upstreamed)
- Switched to new version numbering
- Switched image archive to xz

* Wed May 25 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 3.9.4-2
- Fixed off by one in base64_decode by base64-decode-fix-off-by-one patch
  Related: rhbz#1308204

* Tue May 10 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 3.9.4-1
- New version
- Dropped 0001-fix-build patch (upstreamed)

* Mon May  9 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 3.8.2-12
- Rebuilt to fix Boost ABI problem

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 3.8.2-10
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.8.2-9
- Rebuilt for Boost 1.59

* Thu Aug 06 2015 Jonathan Wakely <jwakely@redhat.com> 3.8.2-8
- Bump %%release to match f23 branch

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.8.2-6
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.8.2-4
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 12 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 3.8.2-3
- Enabled build on ppc64 on RHEL

* Wed Mar 11 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 3.8.2-2
- Fixed building without NEON, especially on aarch64
  Resolves: rhbz#1200836

* Fri Mar  6 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 3.8.2-1
- New version
- Dropped uhd-dump-libs and wireshark-1.12-fix patches (both upstreamed)

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 3.7.2-2
- Rebuild for boost 1.57.0

* Mon Sep  1 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 3.7.2-1
- New version
- Added tools subpackage (wireshark plugin disabled due to rhbz#1129419)
- Minor packaging fixes

* Fri Aug 29 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 3.6.2-6
- Migrated udev rule to dynamic ACL management
- Fixed udev rule location
- Group usrp is no more used / created

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug  8 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 3.6.2-4
- Added workaround for build failure on RHEL-7

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 3.6.2-2
- Rebuild for boost 1.55.0

* Tue Feb 11 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 3.6.2-1
- New version
  Resolves: rhbz#1063587

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 3.5.3-2
- Rebuild for boost 1.54.0

* Wed Jun 05 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 3.5.3-1
- New version
- Defuzzified no-neon patch

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.4.3-3
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 3.4.3-2
- Rebuild for Boost-1.53.0

* Wed Aug 22 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 3.4.3-1
- New version

* Fri Aug 10 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 3.4.2-4
- Rebuilt for new boost

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun  6 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 3.4.2-2
- Added firmware subpackage
  Resolves: rhbz#769684

* Wed May 23 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 3.4.2-1
- New version
- Removed usrp1-r45-dbsrx-i2c-fix patch (upstreamed)
- Fixed convert_test failure on ARM by no-neon patch
  Resolves: rhbz#813393

* Tue Mar 27 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 3.4.0-1
- New version
- Fixed lockup on USRP1 r4.5 + DBSRX + another i2c board combo
  (usrp1-r45-dbsrx-i2c-fix patch)
  Resolves: rhbz#804440

* Mon Mar 19 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 3.3.2-1
- New version

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-4
- Rebuilt for c++ ABI breakage

* Fri Feb 10 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 3.3.1-3
- Allowed UHD to boost the thread's scheduling priority
  Resolves: rhbz#781540

* Wed Jan 11 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 3.3.1-2
- Minor tweaks to %%pre scriptlet
- Fixed udev rules
- Added tkinter requires
  Resolves: rhbz#769678

* Fri Dec  2 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 3.3.1-1
- New version

* Thu Dec  1 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 3.3.0-3
- Updated summary to be more descriptive

* Wed Nov 30 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 3.3.0-2
- Fixed according to reviewer comments

* Tue Nov 01 2011 Jaroslav Škarvada <jskarvad@redhat.com> - 3.3.0-1
- Initial version
