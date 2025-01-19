#%%global snapshot_date 20140530
#%%global snapshot_rev 430863ffea2f6101fbfc0ee35ee098ab2f96b53c
#%%global snapshot_rev_short %(echo %snapshot_rev | cut -c1-6)
#%%global branch trunk

Name:           mingw-w64-tools
Version:        12.0.0
Release:        3%{?dist}
Summary:        Supplementary tools which are part of the mingw-w64 toolchain
# From Debian: Add missing CPU information (ia64, s390, s390x)
Patch0:         widl-missing-cpu-info.patch
# From Debian: Drop unused platform-specific context definitions
Patch1:         widl-no-context.patch
# From Debian: Don't error out on non-Windows CPUs
Patch2:         widl-cpu.patch


# http://sourceforge.net/mailarchive/forum.php?thread_name=5157C0FC.1010309%40users.sourceforge.net&forum_name=mingw-w64-public
# The tools gendef and genidl are GPLv3+, widl is LGPLv2+
License:        GPL-3.0-or-later AND LGPL-2.0-or-later

URL:            http://mingw-w64.sourceforge.net/
%if 0%{?snapshot_date}
# To regenerate a snapshot:
# Use your regular webbrowser to open https://sourceforge.net/p/mingw-w64/mingw-w64/ci/%{snapshot_rev}/tarball
# This triggers the SourceForge instructure to generate a snapshot
# After that you can pull in the archive with:
# spectool -g mingw-w64-tools.spec
Source0:        http://sourceforge.net/code-snapshots/git/m/mi/mingw-w64/mingw-w64.git/mingw-w64-mingw-w64-%{snapshot_rev}.zip
%else
Source0:        http://downloads.sourceforge.net/mingw-w64/mingw-w64-v%{version}.tar.bz2
%endif

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  mingw32-filesystem >= 133
BuildRequires:  mingw64-filesystem >= 133
BuildRequires:  ucrt64-filesystem >= 133


%description
Supplementary tools which are part of the mingw-w64 toolchain
It contains gendef, genidl and mingw-w64-widl


%prep
%if 0%{?snapshot_date}
rm -rf mingw-w64-v%{version}
mkdir mingw-w64-v%{version}
cd mingw-w64-v%{version}
unzip %{S:0}
%autosetup -p1 -D -T -n mingw-w64-v%{version}/mingw-w64-mingw-w64-%{snapshot_rev}
%else
%autosetup -p1 -n mingw-w64-v%{version}
%endif


%build
pushd mingw-w64-tools
    pushd gendef
        %configure
        make %{?_smp_mflags}
    popd

    pushd genidl
        %configure
        make %{?_smp_mflags}
    popd

    pushd widl
        # widl needs to be aware of the location of the IDL files belonging
        # to the toolchain. Therefore it needs to be built for both the win32
        # and win64 targets
        %global _configure ../configure
        mkdir win32
        pushd win32
          %configure --target=%{mingw32_target} --program-prefix=%{mingw32_target}- --with-widl-includedir=%{mingw32_includedir}
          %make_build
        popd
        mkdir win64
        pushd win64
          %configure --target=%{mingw64_target} --program-prefix=%{mingw64_target}- --with-widl-includedir=%{mingw64_includedir}
          %make_build
        popd
        mkdir ucrt64
        pushd ucrt64
          %configure --target=%{ucrt64_target} --program-prefix=%{ucrt64_target}- --with-widl-includedir=%{ucrt64_includedir}
          %make_build
        popd
    popd
popd


%install
pushd mingw-w64-tools
    %make_install -C gendef
    %make_install -C genidl
    %make_install -C widl/win32
    %make_install -C widl/win64
    %make_install -C widl/ucrt64
popd


%files
%license COPYING
%{_bindir}/gendef
%{_bindir}/genidl
%{_bindir}/%{mingw32_target}-widl
%{_bindir}/%{mingw64_target}-widl
%{_bindir}/%{ucrt64_target}-widl


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Sandro Mani <manisandro@gmail.com> - 12.0.0-1
- Update to 12.0.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 17 2023 Sandro Mani <manisandro@gmail.com> - 11.0.1-1
- Update to 11.0.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 30 2023 Sandro Mani <manisandro@gmail.com> - 11.0.0-1
- Update to 11.0.0

* Sun Feb 05 2023 Nianqing Yao <imbearchild@outlook.com> - 10.0.0-4
- Fix build on riscv64.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 26 2022 Sandro Mani <manisandro@gmail.com> - 10.0.0-1
- Update to 10.0.0

* Wed Feb 23 2022 Marc-André Lureau <marcandre.lureau@redhat.com> - 9.0.0-4
- Add ucrt64 target.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Sandro Mani <manisandro@gmail.com> - 9.0.0-1
- Update to 9.0.0

* Mon May 17 2021 Sandro Mani <manisandro@gmail.com> - 8.0.2-1
- Update to 8.0.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Sandro Mani <manisandro@gmail.com> - 8.0.0-1
- Update to 8.0.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Sandro Mani <manisandro@gmail.com> - 7.0.0-1
- Update to 7.0.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 Sandro Mani <manisandro@gmail.com> - 6.0.0-1
- Update to 6.0.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Kalev Lember <klember@redhat.com> - 5.0.4-1
- Update to 5.0.4

* Thu Jun 14 2018 Sandro Mani <manisandro@gmail.com> - 5.0.3-1
- Update to 5.0.3

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Kalev Lember <klember@redhat.com> - 5.0.2-1
- Update to 5.0.2
- Use license macro for COPYING

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.999-0.9.trunk.git430863.20140530
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.999-0.8.trunk.git430863.20140530
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.999-0.7.trunk.git430863.20140530
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.999-0.6.trunk.git430863.20140530
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.999-0.5.trunk.git430863.20140530
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.1.999-0.4.trunk.git430863.20140530
- Update to 20140530 snapshot (git rev 430863f)
- Fixes compilation on aarch64

* Wed May 28 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.1.999-0.3.trunk.git502c72.20140524
- Update to 20140524 snapshot (git rev 502c72)
- Upstream has switched from SVN to Git

* Sun Mar 30 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.1.999-0.2.trunk.r6559.20140330
- Update to r6559 (20140330 snapshot)

* Thu Jan  9 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.1.999-0.1.trunk.r6432.20140104
- Bump version to keep working upgrade path

* Sat Jan  4 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.0.999-0.1.trunk.r6432.20140104
- Update to r6432 (20140104 snapshot)

* Sat Jan  4 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Wed Jan  1 2014 Yaakov Selkowitz <yselkowitz@users.sourceforge.net> - 2.0.999-0.10.trunk.r6228.20130907
- Fix widl default includedir (RHBZ #1047727)

* Sat Sep  7 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.999-0.9.trunk.r6228.20130907
- Update to r6228 (20130907 snapshot)
- Updated instructions to regenerate snapshots
  (SourceForge has changed their SVN infrastructure)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.999-0.8.trunk.20130403
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr  3 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.999-0.7.trunk.20130403
- Update to 20130403 snapshot
- Use a different source tarball which doesn't contain unrelevant code (like libiberty)
- Removed Provides: bundled(libiberty)
- Make sure the widl tool is built for both win32 and win64 toolchains
- Upstream has changed the license of the gendef and genidl tools to GPLv3+
  The license of the widl tool is LGPLv2+

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.999-0.6.trunk.20120124
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 15 2012 Jon Ciesla <limburgher@gmail.com> - 2.0.999-0.5.trunk.20120124
- Provides: bundled(libiberty)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.999-0.4.trunk.20120124
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 28 2012 Dan Horák <dan[at]danny.cz> - 2.0.999-0.3.trunk.20120124
- fix build on s390(x)

* Sun Mar 11 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.999-0.2.trunk.20120124
- Eliminated several conditionals

* Mon Jan 30 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.0.999-0.1.trunk.20120124
- Initial package

