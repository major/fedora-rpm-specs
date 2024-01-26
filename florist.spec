# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     florist
%global upstream_version  22.0.0
%global upstream_gittag   v%{upstream_version}

Name:           florist
Epoch:          2
Version:        %{upstream_version}
Release:        8%{?dist}
Summary:        Open Source implementation of the POSIX Ada Bindings

License:        GPL-2.0-or-later WITH GNAT-exception

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source:         %{url}/archive/%{upstream_gittag}/%{upstream_name}-%{upstream_version}.tar.gz

# C 99 compatibility in the configure script, submitted upstream:
# https://github.com/AdaCore/florist/pull/10
Patch0:         florist-configure-c99.patch
# C 99 compatibility in c-posix.c, backported:
# https://github.com/AdaCore/florist/commit/e6c2f95ff8ae426c3d832f23aa80bcda82dcfa5c
Patch1:         florist-c99.patch

# The following patches have been downloaded from a fork of Florist that
# continued public maintenance of the library while it was not available through
# AdaCore's GitHub page. See the patch files for details.

# [Bugfix] https://github.com/AdaCore/florist/issues/6
Patch:          %{name}-fix-locking-full-size-file-even-when-growing.patch
# [Bugfix] https://github.com/AdaCore/florist/issues/7
Patch:          %{name}-fix-number-of-elements-to-write.patch

BuildRequires:  fedora-gnat-project-common
BuildRequires:  gprbuild gcc-gnat
BuildRequires:  make sed
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
Florist is an implementation of the IEEE Standards 1003.5: 1992, \
IEEE STD 1003.5b: 1996, and parts of IEEE STD 1003.5c: 1998, \
also known as the POSIX Ada Bindings. Using this library, \
you can call operating system services from within Ada programs.

%description %{common_description_en}


#################
## Subpackages ##
#################

%package devel
Summary:    Development files for Florist
Requires:   fedora-gnat-project-common
Requires:   %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel %{common_description_en}

The florist-devel package contains source code and linking information for
developing applications that use Florist.


#############
## Prepare ##
#############

%prep
%autosetup -p1


###########
## Build ##
###########

%build
%configure --enable-shared

%{make_build} GPRBUILD_FLAGS='%{GPRbuild_optflags} -XLIBRARY_TYPE=relocatable' \
     GCCFLAGS='%{build_cflags}' VERSION=%{version} TARGET=


#############
## Install ##
#############

%install
# Use GPRinstall directly to have full control over the installation.
gprinstall %{GPRinstall_flags} --no-manifest --no-build-var \
           -XLIBRARY_TYPE=relocatable \
           florist.gpr

# Fix up some things that GPRinstall does wrong.
ln --symbolic --force lib%{name}.so.1 %{buildroot}%{_libdir}/lib%{name}.so

# Make the generated usage project file architecture-independent.
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/%{name}");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/%{name}";|i' \
    %{buildroot}%{_GNAT_project_dir}/%{name}*.gpr
# The Sed commands are:
# 1: Insert a with clause before the first line to import the directories
#    project.
# 2: Delete a comment that mentions the architecture.
# 3: Replace the value of Source_Dirs with a pathname based on
#    Directories.Includedir.
# 4: Replace the value of Library_Dir with Directories.Libdir.
# 5: Replace the value of Library_ALI_Dir with a pathname based on
#    Directories.Libdir.


###########
## Files ##
###########

%files
%doc README
%license COPYING
%{_libdir}/lib%{name}.so.1


%files devel
%{_GNAT_project_dir}/%{name}.gpr
%{_includedir}/%{name}
%dir %{_libdir}/%{name}
%attr(444,-,-) %{_libdir}/%{name}/*.ali
%{_libdir}/lib%{name}.so


###############
## Changelog ##
###############

%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:22.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:22.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2:22.0.0-6
- Rebuilt with GCC 14 prerelease.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:22.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:22.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Björn Persson <Bjorn@Rombobjörn.se> - 2:22.0.0-3
- Rebuilt with GCC 13.

* Thu Jan 12 2023 Florian Weimer <fweimer@redhat.com> - 2:22.0.0-2
- C99 compatibility fixes

* Fri Sep 23 2022 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:22.0.0-1
- Updated to v22.0.0, using the archive available on GitHub.
- Changed the epoch to mark the new upstream version scheme.
- Changed the epoch to 2 instead of 1 for consistency with the GNATcoll packages.
- Removed patch florist-2017-gcc8; has been fixed upstream (commit: 0bfc497).
- Fixed the symbolic links for the shared libraries.
- Made the generated usage project file architecture-independent.
- Removed license from devel subpackage; inherit from main package.
- Improved spec file readability.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2017-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 03 2022 Björn Persson <Bjorn@Rombobjörn.se> - 2017-12
- Added a workaround to be able to build with GCC 12 prerelease.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2017-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 02 2021 Björn Persson <Bjorn@Rombobjörn.se> - 2017-10
- rebuilt with gcc-11.0.1-0.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2017-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Pavel Zhukov <pzhukov@redhat.com> - 2017-8
- rebuild with new gcc

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2017-4
- Built for x86.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Björn Persson <Bjorn@Rombobjörn.se> - 2017-1
- Upgraded to version 2017.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2011-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2011-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2011-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 02 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2011-19
- Rebuilt with GCC 6 prerelease.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2011-17
- rebuild (gcc / gnat 5)

* Sat Oct 11 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2011-16
- Exclude arm 

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2011-13
- Use GNAT_arches rather than an explicit list

* Wed May  7 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2011-12
- Rebuild with new libgnat

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jan 30 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 2011-10
- Add gcc-gnat to BR

* Sat Jan 26 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 2011-9
- Rebuild with new GCC-.48

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2011-7
- Rebuild for new GCC-4.7

* Wed Aug 10 2011  Pavel Zhukov <landgraf@fedoraproject.org> - 2011-6
- Add ExclusiveArch

* Wed Aug 03 2011  Pavel Zhukov <landgraf@fedoraproject.org> - 2011-5
- Add posix-implemetation_signals
- Add posix-permissions_implementation

* Tue Aug 02 2011  Pavel Zhukov <landgraf@fedoraproject.org> - 2011-4
- Initial build
- Add C sources to *.so
- patch autoconf
