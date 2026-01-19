# The test suite is normally run. It can be disabled with "--without=check".
%bcond_without check

# The low-level bindings are normally regenerated. Regeneration can be disabled
# with "--without=generate".
%bcond_without generate

# Upstream source information.
%global upstream_owner        persan
%global upstream_name         zeromq-Ada
%global upstream_version      4.1.5
%global upstream_commit_date  20251117
%global upstream_commit       c9a0e984b673ee61cbf86819c300d7d54f563fea
%global upstream_shortcommit  %(c=%{upstream_commit}; echo ${c:0:7})

Name:           zeromq-ada
Version:        %{upstream_version}^git%{upstream_commit_date}.%{upstream_shortcommit}
Release:        2%{?dist}
Summary:        Ada binding for ZeroMQ

License:        MIT
# According to the upstream commit history, the license of this library was
# changed to MIT on Apr 8, 2021 (upstream commit 651ca44).

URL:            https://zeromq.org
Source0:        https://github.com/%{upstream_owner}/%{upstream_name}/archive/%{upstream_commit}.tar.gz#/%{name}-%{upstream_shortcommit}.tar.gz

# [Fedora-specific] Remove Python and Makefile languages from the ZMQ
#   GPRbuild-file. Both languages are used only during the development of the
#   bindings/library and are of no relevance to the user of the bindings.
Patch:          %{name}-remove-unnecessary-languages.patch

# [Fedora-specific] Indicate that the examples depend on GNATcoll Core.
Patch:          %{name}-add-gnatcoll-core-dependency-to-zmq-example.patch

# [Fedora-specific] The gnatpp tool, a source code formatter tool which is part
#   of the now obsolete ASIS-toolset, is not available in Fedora.
Patch:          %{name}-skip-gnatpp-during-generate.patch

# [Fedora-specific] Update the GPRbuild project for building the test suite.
#   Note that we want to run the test suite against the Ada bindings installed
#   in the buildroot and must therefore remove any reference to packages that
#   are only defined in the ZMQ project in the source tree.
#
#   - Remove the `helpers' project; the dependency isn't used by any test.
#   - Update the dependency from GNATcoll to GNATcoll Core.
#   - Remove the compiler switches. They're inherited from the ZMQ project in
#     the source tree. When building the testsuite, we'll use the switches of
#     Fedora instead.
#   - Remove the `Ide' package. The package is inherited from the the ZMQ
#     project in the source tree and isn't needed when packaging the library.
#
Patch:          %{name}-adjust-zmq-tests-project.patch

BuildRequires:  gcc-gnat gprbuild
BuildRequires:  fedora-gnat-project-common
BuildRequires:  zeromq-devel
%if %{with generate}
BuildRequires:  make gcc-g++ sed
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command
%endif
%if %{with check}
BuildRequires:  aunit-devel
BuildRequires:  gnatcoll-core-devel
BuildRequires:  xmlada-devel
%endif

Requires:       zeromq

# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
The ZeroMQ lightweight messaging kernel is a library which extends the \
standard socket interfaces with features traditionally provided by specialized \
messaging middleware products. ZeroMQ sockets provide an abstraction of \
asynchronous message queues, multiple messaging patterns, message filtering \
(subscriptions), seamless access to multiple transport protocols and more.

%description %{common_description_en}

This package provides an Ada binding to the ZeroMQ library.

#################
## Subpackages ##
#################

%package devel
Summary:        Development package for the Ada binding for ZeroMQ
License:        MIT AND GPL-2.0-or-later WITH GNAT-exception
# The license is MIT except for:
# - libzmq.gpr.in : GPLv2+ with GNAT runtime exception
# - zmq.gpr.inst  : GPLv2+ with GNAT runtime exception
# - zmq.gpr       : GPLv2+ with GNAT runtime exception
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common
Requires:       zeromq-devel

%description devel %{common_description_en}

This package contains source code and linking information for developing
applications that use the Ada binding for ZeroMQ. It also contains some
code examples.


#############
## Prepare ##
#############

%prep
%autosetup -C -p1

# Work with the GPRbuild-project to be used by users of the Ada bindings.
rm examples/zmq-examples.gpr
cp --preserve=timestamp examples/zmq-examples.gpr.inst \
                        examples/zmq-examples.gpr

# libzmq.gpr is needed by zmq.gpr.
cp libzmq.gpr.in libzmq.gpr

# Regenerate the low-level bindings.
%if %{with generate}
make generate
%endif


###########
## Build ##
###########

%build

# Build the library.
gprbuild %{GPRbuild_flags} -XLIBRARY_TYPE=relocatable -P zmq.gpr


#############
## Install ##
#############

%install

# Install the library.
%{GPRinstall} -XLIBRARY_TYPE=relocatable -P zmq.gpr

# Fix up the symlink.
ln --symbolic --force libzmqAda.so.%{upstream_version} \
   %{buildroot}%{_libdir}/libzmqAda.so

# Copy the examples.
mkdir --parents %{buildroot}%{_pkgdocdir}/examples
cp --preserve=timestamps examples/zmq-examples*.ad* \
                         %{buildroot}%{_pkgdocdir}/examples
cp --preserve=timestamps examples/zmq-examples.gpr \
                         %{buildroot}%{_pkgdocdir}/examples

# Before making the project files architecture-independent, copy the buildroot
# into a separate directory for later testing. The testsuite fails if applied to
# the buildroot after making the project files architecture-independent because
# of the hardcoded paths in `directories.gpr`.
%if %{with check}
%global checkroot %{_builddir}/%{name}-%{version}/checkroot
mkdir %{checkroot}  # without --parents to not clobber any upstream directory
cp --recursive %{buildroot}/* %{checkroot}/
%endif

# Make the generated usage project file architecture-independent.
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=/package Linker is/,/end Linker/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'%{name}'");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'%{name}'";|i' \
    %{buildroot}%{_GNAT_project_dir}/zmq.gpr
# The Sed commands are:
# 1: Insert a with clause before the first line to import the directories
#    project.
# 2: Delete a comment that mentions the architecture.
# 3: Delete the package Linker, which contains linker parameters that a
#    shared library normally doesn't need, and can contain architecture-
#    specific pathnames.
# 4: Replace the value of Source_Dirs with a pathname based on
#    Directories.Includedir.
# 5: Replace the value of Library_Dir with Directories.Libdir.
# 6: Replace the value of Library_ALI_Dir with a pathname based on
#    Directories.Libdir.


###########
## Check ##
###########

%if %{with check}
%check

# Make the files of this packages visible to the test runner.
export PATH=%{checkroot}%{_bindir}:$PATH
export LD_LIBRARY_PATH=%{checkroot}%{_libdir}:$LD_LIBRARY_PATH
export GPR_PROJECT_PATH=%{checkroot}%{_GNAT_project_dir}:$GPR_PROJECT_PATH

cd tests

# Build the test suite.
gprbuild %{GPRbuild_flags} -P zmq-tests.gpr -cargs -fPIE

# Run the test suite.
bin/test_all

%endif


###########
## Files ##
###########

%files
%license COPYING
%{_libdir}/libzmqAda.so.%{upstream_version}


%files devel
%{_GNAT_project_dir}/zmq.gpr
%{_includedir}/%{name}
%dir %{_libdir}/%{name}
%attr(444,-,-) %{_libdir}/%{name}/*.ali
%{_libdir}/libzmqAda.so
%{_pkgdocdir}/examples


###############
## Changelog ##
###############

%changelog
* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5^git20251117.c9a0e98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 09 2026 Dennis van Raaij <dvraaij@fedoraproject.org> - 4.1.5^git20251117.c9a0e98-1
- Removed debug package creation opt-out.
- Updated to Git revision c9a0e98 (Nov 17, 2025).
- Updated the SPDX license expression.
- The examples can now be found in the package documentation directory.
- All package summaries and descriptions have been updated.
- The README-file has been removed from the package as it doesn't contain any
  useful information for Fedora users.
- The license file can now be found in the package license directory.
- Made the generated project file architecture-independent.

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-16.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-15.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.1.5-14.git
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-13.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-12.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 05 2023 Remi Collet <remi@remirepo.net> - 4.1.5-11.git
- rebuild for new libsodium

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-10.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-9.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-8.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-7.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-6.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Max Reznik <reznikmm@gmail.com> - 4.1.5-5.git
- rebuilt with gcc-11.1.1-1

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-4.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  9 2020 Pavel Zhukov <pzhukov@redhat.com> - 4.1.5-3.git
- Rebuild with new libgnat

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-2.git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Max Reznik <reznikmm@gmail.com> - 4.1.5-1.git
- Update to 4.1.5

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-30.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-29.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-28.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-27.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Pavel Zhukov <landgraf@fedoraproject.org - 2.1.0-26.24032011git
- rebuilt with new gnat
- Use gprbuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-23.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-22.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 2.1.0-21.24032011git
- Rebuilt for libgnat soname bump

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-20.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Thomas Spura <tomspur@fedoraproject.org> - 2.1.0-19.24032011git
- rebuilt for new zeromq 4.1.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-18.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 26 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.0-17.24032011git
- Rebuilt for new libgnat

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-16.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-15.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.0-14.24032011git
- Use GNAT_arches rather than an explicit list

* Sun Apr 20 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-13.24032011git
- Rebuild with new GCC

* Sun Mar 02 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-12.24032011git
- Fix library finalization. https://github.com/persan/zeromq-Ada/issues/10

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-11.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jan 25 2013 Kevin Fenzi <kevin@scrye.com> 2.1.0-10.24032011git
- Rebuild for new libgnat
- Add buildrequires on gcc-gnat. It's no longer pulled in by fedora-gnat-project-common

* Sun Sep 23 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-9.24032011git
- Fix gpr path

* Sun Sep 23 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-8.24032011git
- Fix libraries symlinks
- Add usrmove patch

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-7.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu May 05 2011 Dan Horák <dan[at]danny.cz> - 2.1.0-6.24032011git
- updated the supported arch list

* Fri Apr 29 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-4.24032011git
- Create shared libraries path
- Fix license tag
- Fix spec errors

* Thu Mar 24 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-1.24032011git
- update to new commit

* Wed Feb 2 2011 Pavel Zhukov <pavel@zhukoff.net> - 2.0.10-02022011git
- Initial package
