Name: puzzles
Version: 20241230.79be403
Release: 2%{?dist}
Summary: A collection of one-player puzzle games

License: MIT
URL: https://www.chiark.greenend.org.uk/~sgtatham/puzzles/
Source0: https://www.chiark.greenend.org.uk/~sgtatham/puzzles/puzzles-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: ImageMagick
BuildRequires: perl-interpreter

%description
This is a collection of small desktop toys, little games that you can
pop up in a window and play for two or three minutes while you take a
break from whatever else you were doing.

%prep
%autosetup

iconv -f ISO88591 -t UTF8 < LICENCE > LICENSE

%build
# The RPM %%cmake macro doesn't work correctly here:
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/22FW4APH22LP3CMQGULOY4FMAMAVJ5JK/
mkdir redhat-linux-build
pushd redhat-linux-build
cmake .. -DCMAKE_INSTALL_PREFIX=%{_prefix} -DNAME_PREFIX=puzzles-
popd
%cmake_build

%install
%cmake_install
desktop-file-validate %{buildroot}%{_datadir}/applications/puzzles-*.desktop

%files
%doc README HACKING puzzles.txt
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20241230.79be403-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Jan  5 2025 Greg Bailey <gbailey@lxpro.com> - 20241230.79be403-1
- Update version
- Adapt to use new cmake build process

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9023-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9023-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9023-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9023-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9023-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9023-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9023-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9023-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9023-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9023-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9023-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9023-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9023-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9023-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9023-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9023-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9023-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9023-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9023-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 21 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 9023-13
- Use '|' as pattern-delimiter in sed expression (Fix FTFBS).
- Add %%license.
- Modernize spec.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9023-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9023-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9023-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9023-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 9023-8
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9023-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9023-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 29 2012 Bruno Wolff III <bruno@wolff.to> - 9023-5
- Link with math library

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9023-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 9023-3
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9023-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 13 2010 Victor Bogado <victor@bogado.net> 9023
- New upstream release.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8596-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

*Mon Jun 22 2009  Victor Bogado <victor@bogado.net> 8596-1
- updating to a new upstream version

*Thu Dec 11 2008  Victor Bogado <victor@bogado.net> 8365-1
- New updastream version

*Mon Oct 27 2008  Victor Bogado <victor@bogado.net> 8200-3
- Build-Requires should have desktop-file-utils
- Description should start with uppercase
- iconv goes now in prep area
- fixed mistakes in the versions of the change log
- Names on the menu should start with an upper-case

*Mon Oct 20 2008 Victor Bogado <victor@bogado.net> 8200-2
- Fixing problem with desktop files.

*Mon Oct 20 2008 Victor Bogado <victor@bogado.net> 8200-1
- Suggestion made by reviewer Sergio Pascual <sergio.pasra@gmail.com>.
- rename all the binaries.
- rename desktop files to follow the binary name.
- adding LICENCE (renamed to LICENSE) to docs.
- sed "in place", better coding.
- removing sed out of build-requires.
- Updated to last upstream version.

*Mon Sep 01 2008 Victor Bogado <victor@bogado.net> 8149-1
- initial spec
