Name:           fedora-gnat-project-common
Version:        3.22
Release:        2%{?dist}
Summary:        Files shared by Ada libraries
Summary(sv):    Gemensamma filer för adabibliotek

License:        FSFAP
URL:            https://src.fedoraproject.org/rpms/fedora-gnat-project-common
Source1:        directories.gpr.in
Source2:        macros.gnat.in
Source3:        gnat-project.sh
Source4:        gnat-project.csh
Source5:        configure
BuildArch:      noarch

BuildRequires:  sed
Requires:       setup coreutils
# setup owns /etc/profile.d, and coreutils contains uname and realpath.

# Libraries that use directories.gpr don't need redhat-rpm-config, but when RPM
# packages are being built, then build_adaflags uses __build_flags_common,
# which was introduced in redhat-rpm-config 259.
Conflicts:      redhat-rpm-config < 259


%description
The fedora-gnat-project-common package contains files that are used by the GNAT
project files of multiple Ada libraries, and also GNAT-specific RPM macros.

%description -l sv
Paketet fedora-gnat-project-common innehåller filer som används av
GNAT-projektfilerna för flera adabibliotek, samt GNAT-specifika RPM-makron.

%global _GNAT_project_dir /usr/share/gpr
# _GNAT_project_dir is defined here and copied from here to macros.gnat so that
# this package won't build-require itself.


%prep
%setup -c -T
cp --preserve=timestamps %{sources} .


%build
exec_prefix=%{_exec_prefix} bindir=%{_bindir} libexecdir=%{_libexecdir} includedir=%{_includedir} GNAT_project_dir=%{_GNAT_project_dir} ./configure


%install
mkdir --parents %{buildroot}%{_GNAT_project_dir} %{buildroot}%{_sysconfdir}/profile.d %{buildroot}%{rpmmacrodir}
cp -p directories.gpr %{buildroot}%{_GNAT_project_dir}/
cp -p gnat-project.sh gnat-project.csh %{buildroot}%{_sysconfdir}/profile.d/
cp -p macros.gnat %{buildroot}%{rpmmacrodir}/


%files
%{_GNAT_project_dir}
%config(noreplace) %{_sysconfdir}/profile.d/*
%{rpmmacrodir}/*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 29 2024 Björn Persson <Bjorn@Rombobjörn.se> - 3.22-1
- Fixed spurious backslashes in RPM macros.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 24 2024 Björn Persson <Bjorn@Rombobjörn.se> - 3.21-1
- GPRinstall_flags now accepts parameters, making it more flexible.
- The macro GPRinstall has been added.
- build_adaflags now contains a little less C-specific junk.

* Thu Feb 22 2024 Björn Persson <Bjorn@Rombobjörn.se> - 3.20-1
- Added riscv64.

* Wed Feb 21 2024 Björn Persson <Bjorn@Rombobjörn.se> - 3.19-1
- Added -Wtrampolines to help with diagnosing build failures caused by
  restrictions on executable stacks.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 09 2023 Björn Persson <Bjorn@Rombobjörn.se> - 3.18-1
- Removed -m because it has a bug that makes libraries unusable, and several
  Adacore libraries contain filenames that trigger the bug.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 07 2023 Björn Persson <Bjorn@Rombobjörn.se> - 3.17-1
- Added --no-manifest and -m to GPRinstall_flags.
- Deprecated the "opt" part of macro names.
- The license is now FSFAP.

* Thu Sep 22 2022 Björn Persson <Bjorn@Rombobjörn.se> - 3.16-1
- Adapted to backward compatibility breakage in uname.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  2 2020 Pavel Zhukov <pzhukov@redhat.com> - 3.15-1
- Add flags for gprinstall into macros.gnat

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Björn Persson <Bjorn@Rombobjörn.se> - 3.14-1
- A macro definition has been simplified.
- A dependency has been corrected.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 2019 Björn Persson <Bjorn@Rombobjörn.se> - 3.13-1
- Since Gnatmake dropped project support it no longer searches for libgnat.a,
  so the workaround of fedora-gnat-project-common requiring libgnat-static has
  now been dropped.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 18 2018 Björn Persson <Bjorn@Rombobjörn.se> - 3.12-1
- Upgraded to version 3.12.
- One variable name has been corrected in Comfignat_make.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Björn Persson <Bjorn@Rombobjörn.se> - 3.11-1
- Upgraded to version 3.11.

* Sat Feb 17 2018 Björn Persson <Bjorn@Rombobjörn.se> - 3.10-1
- Upgraded to version 3.10.
- A flag has been added to get more useful build logs from GPRbuild.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 12 2015 Björn Persson <bjorn@rombobjörn.se> - 3.9-4
- Restored after experiments with Koji.

* Sun Jul 12 2015 Björn Persson <bjorn@rombobjörn.se> - 3.9-1
- Upgraded to version 3.9.
- The architecture ppc64le has been added.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 01 2015 Björn Persson <bjorn@rombobjörn.se> - 3.8-4
- Tagged the license file as such.

* Sun Feb 08 2015 Björn Persson <bjorn@rombobjörn.se> - 3.8-3
- Removed a temporary explanation file.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 26 2013 Björn Persson <bjorn@rombobjörn.se> - 3.8-1
- Upgraded to version 3.8.

* Wed Nov 13 2013 Björn Persson <bjorn@rombobjörn.se> - 3.7-1
- Upgraded to version 3.7 with support for Comfignat 1.2.

* Wed Aug 14 2013 Björn Persson <bjorn@rombobjörn.se> - 3.6-1
- Upgraded to version 3.6.
- The mapping from architectures to Libdir values has been corrected and
  expanded.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Björn Persson <bjorn@rombobjörn.se> - 3.5-7
- RPM 4.11 or later is required.

* Sat Mar 16 2013 Björn Persson <bjorn@rombobjörn.se> - 3.5-6
- Moved macros.gnat out of /etc because it isn't a configuration file.

* Mon Mar 11 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.5-5
- Remove %%config from %%{_sysconfdir}/rpm/macros.*
  (https://fedorahosted.org/fpc/ticket/259).

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 06 2012 Björn Persson <bjorn@rombobjörn.se> - 3.5-3
- Removed the dependency on gcc-gnat.

* Fri Oct 05 2012 Björn Persson <bjorn@rombobjörn.se> - 3.5-2
- Added ExclusiveArch to distribute the package only for architectures where
  gcc-gnat is available.

* Fri Sep 07 2012 Björn Persson <bjorn@rombobjörn.se> - 3.5-1
- Upgraded to version 3.5.
- Inclusion of runpaths can be controlled with GNAT_add_rpath.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 19 2012 Björn Persson <bjorn@rombobjörn.se> - 3.4-1
- Upgraded to version 3.4.
- Some compiler flags have been added to prevent dangerous suppression of
  important checks and avoid unnecessary build failures.
- GNAT_arches has been moved to macros.gnat-srpm in redhat-rpm-config.
- The location of GNAT project files has been changed to /usr/share/gpr.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Björn Persson <bjorn@rombobjörn.se> - 3.3-1
- Upgraded to version 3.3 with GNAT_arches.

* Wed Aug 03 2011 Björn Persson <bjorn@rombobjörn.se> - 3.2-1
- Upgraded to version 3.2 with partial support for __global_ldflags.

* Sun May 22 2011 Björn Persson <bjorn@rombobjörn.se> - 3.1-1.1
- Removed some obsolete stuff.

* Tue May 03 2011 Björn Persson <bjorn@rombobjörn.se> - 3.1-1
- Upgraded to version 3.1.
- A configuration step has been added, so fewer directory names are hard-coded.
- There are now separate RPM macros with parameters for different tools in the
  GNAT toolchain.

* Sun Apr 03 2011 Björn Persson <bjorn@rombobjörn.se> - 2.2-1
- Updated to version 2.2 which is compatible with GPRbuild (bug 691558).

* Wed Feb 09 2011 Björn Persson <bjorn@rombobjörn.se> - 2.1-1
- Updated to version 2.1 with directories.gpr.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 04 2010 Björn Persson <bjorn@rombobjörn.se> - 1.2-2
- Worked around bug 613407.

* Tue Aug 04 2009 Björn Persson <bjorn@rombobjörn.se> - 1.2-1
- Updated to version 1.2 with a more complete list of processor architectures.

* Thu Jul 23 2009 Björn Persson <bjorn@rombobjörn.se> - 1.1-3
- Added a BuildRoot tag even though it's unnecessary.
- Removed a macro reference from the previous changelog entry.
- Silenced some RPMlint warnings.

* Fri Jul 03 2009 Björn Persson <bjorn@rombobjörn.se> - 1.1-2
- Renamed the package to fedora-gnat-project-common.
- There is now an "upstream" project at Fedora Hosted.
- Added a license file.
- Replaced "/etc" with _sysconfdir.

* Wed Jul 01 2009 Björn Persson <bjorn@rombobjörn.se> - 1-1
- ready to be submitted for review
