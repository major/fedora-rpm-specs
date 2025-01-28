%global commit0 68044cc4dac829729ccd0ee88d0780525b515746
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global snapdate 20250121

%global __python %{__python3}

Name:           icestorm
Version:        0
Release:        0.38.%{snapdate}git%{shortcommit0}%{?dist}
Summary:        Lattice iCE40 FPGA bitstream creation/analysis/programming tools
License:        ISC
URL:            http://bygone.clairexen.net/%{name}
Source0:        https://github.com/YosysHQ/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

# Fedora-specific patch for datadir
Patch1:         %{name}-datadir.patch

BuildRequires:  gcc-c++
BuildRequires:  python%{python3_pkgversion} libftdi-devel
BuildRequires: make

%description
Project IceStorm aims at documenting the bitstream format of Lattice iCE40
FPGAs and providing simple tools for analyzing and creating bitstream files.

%prep
%setup -q -n %{name}-%{commit0}
%patch 1 -p1 -b .datadir

# fix shebang lines in Python scripts
find . -name \*.py -exec sed -i 's|/usr/bin/env python3|/usr/bin/python3|' {} \;
# get rid of .gitignore files in examples
find . -name \.gitignore -delete

%build
%global moreflags -I/usr/include/libftdi1
make %{?_smp_mflags} \
     CFLAGS="%{optflags} %{moreflags}" \
     CXXFLAGS="%{optflags} %{moreflags}" \
     PREFIX="%{_prefix}" \
     CHIPDB_SUBDIR="%{name}" \
     LDFLAGS="$RPM_LD_FLAGS"

%install
%make_install PREFIX="%{_prefix}"
chmod +x %{buildroot}%{_bindir}/icebox.py
mv %{buildroot}%{_datarootdir}/icebox %{buildroot}%{_datarootdir}/%{name}
mv %{buildroot}%{_bindir}/iceboxdb.py %{buildroot}%{_datarootdir}/%{name}
install -pm644 icefuzz/timings_*.txt %{buildroot}%{_datarootdir}/%{name}

# We could do a minimal check section by running make in the example
# directories, but that depends on arachne-pnr, which depends on this
# package, so it would create a circular dependency.

%files
%license README
%doc examples
%{_bindir}/*
%{_datarootdir}/%{name}

%changelog
* Tue Jan 21 2025 Gabriel Somlo <gsomlo@gmail.com> - 0-0.38.20250121git68044cc
- Update to newer snapshot

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.37.20241211git7190770
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 11 2024 Gabriel Somlo <gsomlo@gmail.com> - 0-0.36.20241211git7190770
- Update to newer snapshot

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.35.20240716git738af82
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Gabriel Somlo <gsomlo@gmail.com> - 0-0.34.20240716git738af82
- Update to newer snapshot

* Fri May 24 2024 Gabriel Somlo <gsomlo@gmail.com> - 0-0.33.20240524gitc23e99c
- Update to newer snapshot

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.32.20231218git1a40ae7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.31.20231218git1a40ae7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Gabriel Somlo <gsomlo@gmail.com> - 0-0.30.20231218git1a40ae7
- Update to newer snapshot

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.20230220gitd20a5e9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Gabriel Somlo <gsomlo@gmail.com> - 0-0.28.20230220gitd20a5e9
- Update to newer snapshot

* Wed Feb 15 2023 Gabriel Somlo <gsomlo@gmail.com> - 0-0.27.20230215git8649e3e
- Update to newer snapshot

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.20230104git45f5e5f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Gabriel Somlo <gsomlo@gmail.com> - 0-0.25.20230104git45f5e5f
- Update to newer snapshot

* Thu Oct 06 2022 Gabriel Somlo <gsomlo@gmail.com> - 0-0.24.20221006gita545498
- Update to newer snapshot

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.20220705git2bc5417
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 05 2022 Gabriel Somlo <gsomlo@gmail.com> - 0-0.22.20220705git2bc5417
- Update URL in spec file
- Update to newer snapshot

* Mon May 09 2022 Gabriel Somlo <gsomlo@gmail.com> - 0-0.21.20220509git9f66f9c
- Update to newer snapshot

* Tue Feb 22 2022 Gabriel Somlo <gsomlo@gmail.com> - 0-0.20.20220222git8fa85d5
- Update to newer snapshot

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20210928git83b8ef9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 28 2021 Gabriel Somlo <gsomlo@gmail.com> - 0-0.18.20210928git83b8ef9
- Update to newer snapshot

* Sat Sep 04 2021 Gabriel Somlo <gsomlo@gmail.com> - 0-0.17.20210904gitb93cb16
- Update to newer snapshot

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20200806gitd123087
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20200806gitd123087
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 06 2020 Gabriel Somlo <gsomlo@gmail.com> - 0-0.14.20200806gitd123087
- Update to newer snapshot
- Spec file: update github URL

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20200517gitcd2610e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 17 2020 Gabriel Somlo <gsomlo@gmail.com> - 0-0.12.20200517gitcd2610e
- Update to newer snapshot
- Spec file: remove gcc10 patch (now in upstream)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20190823git9594931
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff Law <law@redhat.com> - 0-0.10.20190823git9594931
- Fix missing #include for gcc-10

* Fri Aug 23 2019 Gabriel Somlo <gsomlo@gmail.com> - 0-0.9.20190823git9594931
- Update to newer snapshot
- Spec file: fix source URL; add 'snapdate' variable

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20190311gitfa1c932
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 19 2019 Lubomir Rintel <lkundrak@v3.sk> - 0-0.7.20190311gitfa1c932
- Update to a newer snapshot
- Package the timing files

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20170914git5c4d4db
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20170914git5c4d4db
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Lubomir Rintel <lkundrak@v3.sk> 0-0.5.20170914git5c4d4db
- Fix the chipdb path for icetime

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20170914git5c4d4db
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 Eric Smith <brouhaha@fedoraproject.org> 0-0.3.20170914git5c4d4db
- Updated per review comments.
- Updated to latest upstream.

* Sat Dec 10 2016 Eric Smith <brouhaha@fedoraproject.org> 0-0.2.20161101git01b9822
- Updated per review comments.
- Updated to latest upstream.

* Mon Sep 12 2016 Eric Smith <brouhaha@fedoraproject.org> 0-0.1.20160904git0b4b038
- Initial version.
