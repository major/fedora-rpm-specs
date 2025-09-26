%global commit0 c40fb2289952f4f120cc10a5a4c82a6fb88442dc

# The upstream makefile gets version information by invoking git. We can't
# do that. We can still use what the Makefile calls GIT_REV, because that's
# our shortcommit0 variable extracted from commit0 below.  We have to
# hard-code VER and VER_HASH here, as ver0 and verhash0.  When updating this
# package spec for a new git snapshot, clone the git repo, run make in it,
# and inspect the generated version_(has).cc to determine the correct values.
%global ver0 0.1+328+0
%global verhash0 34321

%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           arachne-pnr
Version:        0.1
Release:        0.25.20190729git%{shortcommit0}%{?dist}
Summary:        Place and route for FPGA compilation
License:        MIT
URL:            https://github.com/cseed/arachne-pnr
Source0:        https://github.com/cseed/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

# https://github.com/YosysHQ/arachne-pnr/issues/126
Patch0:         use-std-priority-queue.patch
Patch1:         make-use-of-emplace.patch

# patch the tests, which give equivalent but different results
# (the meaning of the verilog didn't change, but the order and variable numbers did)
Patch2:         test-fixup.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Continue building on s390x, but skip the tests
# those need yosys and it doesn't build on s390x
# TODO: subset tests to run on s390x without yosys
%ifnarch s390x
%bcond check 1
%else
%bcond check 0
%endif

BuildRequires:  gcc-c++
BuildRequires:  icestorm
BuildRequires:  make
%if %{with check}
# shasum,yosys needed to complete simpletests
BuildRequires:  perl(Digest::SHA)
BuildRequires:  yosys
%endif

%description
Arachne-pnr implements the place and route step of the hardware
compilation process for FPGAs. It accepts as input a technology-mapped
netlist in BLIF format, as output by the Yosys synthesis suite for
example. It currently targets the Lattice Semiconductor iCE40 family
of FPGAs. Its output is a textual bitstream representation for
assembly by the IceStorm icepack command. The output of icepack is a
binary bitstream which can be uploaded to a hardware device.

Together, Yosys, arachne-pnr and IceStorm provide an fully open-source
Verilog-to-bistream tool chain for iCE40 1K and 8K FPGA development.

%prep
%autosetup -n %{name}-%{commit0} -p1

# can't use git from Makefile to extract version information
sed -i 's/^VER =.*/VER = %{ver0}/' Makefile
sed -i 's/^GIT_REV =.*/GIT_REV = %{shortcommit0}/' Makefile
sed -i 's/^VER_HASH =.*/VER_HASH = %{verhash0}/' Makefile

%build
make %{?_smp_mflags} \
     CXXFLAGS="%{optflags}" \
     PREFIX="%{_prefix}" \
     ICEBOX="%{_datadir}/icestorm"

%install
make install PREFIX="%{_prefix}" \
             DESTDIR="%{buildroot}" \
             ICEBOX="%{_datadir}/icestorm"

%check
%if %{with check}
make simpletest %{?_smp_mflags} \
     CXXFLAGS="%{optflags} -Isrc/" \
     PREFIX="%{_prefix}" \
     ICEBOX="%{_datadir}/icestorm"
%endif

%files
%license COPYING
%doc README.md
%{_bindir}/*
%{_datadir}/%{name}

%changelog
* Wed Sep 24 2025 Alexander F. Lent <lx@xanderlent.com> - 0.1-0.25.20190729gitc40fb22
- Re-enable builds on s390x while skipping the tests on that arch.

* Fri Aug  1 2025 Alexander F. Lent <lx@xanderlent.com> - 0.1-0.24.20190729gitc40fb22
- Enable the simple test suite to detect future breakage.

* Fri Aug 01 2025 Alexander F. Lent <lx@xanderlent.com> - 0.1-0.23.20190729gitc40fb22
- Fix License, upstream moved to MIT in 2017.

* Fri Aug  1 2025 Marcus A. Romer <aimylios@gmx.de> - 0.1-0.22.20190729gitc40fb22
- Fix RHBZ #1810351

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.21.20190729gitc40fb22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.20.20190729gitc40fb22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1-0.19.20190729gitc40fb22
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.18.20190729gitc40fb22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.17.20190729gitc40fb22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.16.20190729gitc40fb22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.15.20190729gitc40fb22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.14.20190729gitc40fb22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.13.20190729gitc40fb22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.12.20190729gitc40fb22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.11.20190729gitc40fb22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.10.20190729gitc40fb22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.9.20190729gitc40fb22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.8.20190729gitc40fb22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug  7 2019 Vasil Velichkov <vvvelichkov@gmail.com> - 0.1-0.7.20190729gitc40fb22
- Update to upstream git c40fb2289952f4f120cc10a5a4c82a6fb88442dc

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.7.20170628git7e135ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.6.20170628git7e135ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.5.20170628git7e135ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.4.20170628git7e135ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 17 2017 Eric Smith <brouhaha@fedoraproject.org> 0.1-0.3.20170628git7e135ed
- updated to latest upstream.

* Mon Sep 12 2016 Eric Smith <brouhaha@fedoraproject.org> 0.1-0.2.20160813git52e69ed
- Updated directory used for icebox for consistency with icestorm package.

* Mon Sep 12 2016 Eric Smith <brouhaha@fedoraproject.org> 0.1-0.1.20160813git52e69ed
- Initial version.
