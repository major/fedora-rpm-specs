#                        TO WHOM IT MAY CONCERN
#
# Don't add patches, dist-git is the upstream repository for this package.

Summary: Red Hat-family-specific rpm configuration files
Name: redhat-rpm-config
# The version should be 300 + Fedora release number.
# If the branches haven't diverged yet, keep the Fedora release number from
# the older branch. When the branch diverges, bump the Version to the Fedora
# release number.
Version: 342
Release: %autorelease
# config.guess, config.sub are GPL-3.0-or-later WITH Autoconf-exception-generic
License: GPL-1.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-generic AND Boehm-GC
URL: https://src.fedoraproject.org/rpms/redhat-rpm-config

# Core rpm settings
Source0: macros
Source1: rpmrc

# gcc specs files for hardened builds
Source50: redhat-hardened-cc1
Source51: redhat-hardened-ld
Source52: redhat-hardened-ld-errors
# clang config spec files
Source53: redhat-hardened-clang.cfg
Source54: redhat-hardened-clang-ld.cfg

# gcc specs files for annobin builds
Source60: redhat-annobin-cc1
Source61: redhat-annobin-select-gcc-built-plugin
Source62: redhat-annobin-select-annobin-built-plugin
Source63: redhat-annobin-plugin-select.sh

# The macros defined by these files are for things that need to be defined
# at srpm creation time when it is not feasible to require the base packages
# that would otherwise be providing the macros. other language/arch specific
# macros should not be defined here but instead in the base packages that can
# be pulled in at rpm build time, this is specific for srpm creation.
Source100: macros.fedora-misc-srpm
Source102: macros.mono-srpm
Source103: macros.nodejs-srpm
Source104: macros.ldc-srpm
Source105: macros.valgrind-srpm
Source106: macros.java-srpm
Source107: macros.gap-srpm
Source108: macros.dotnet-srpm
Source109: macros.hare-srpm

# Other misc macros
Source150: macros.build-constraints
Source151: macros.dwz
Source152: macros.fedora-misc
Source155: macros.ldconfig
Source156: macros.vpath
Source157: macros.shell-completions
Source158: macros.rpmautospec

# Build policy scripts
# this comes from https://github.com/rpm-software-management/rpm/pull/344
# added a python -> python2 conversion for fedora with warning
# and an echo when the mangling happens
Source201: brp-mangle-shebangs

# Dependency generator scripts (deprecated)
Source300: find-provides
Source304: find-requires

# Misc helper scripts
Source400: dist.sh
Source404: gpgverify

# Snapshots from http://git.savannah.gnu.org/gitweb/?p=config.git
Source500: https://git.savannah.gnu.org/cgit/config.git/plain/config.guess
Source501: https://git.savannah.gnu.org/cgit/config.git/plain/config.sub

# Dependency generators & their rules
Source602: libsymlink.attr

# BRPs
Source700: brp-ldconfig
Source701: brp-strip-lto

# Convenience lua functions
Source800: common.lua

# Documentation
Source900: buildflags.md

BuildArch: noarch
BuildRequires: perl-generators
Requires: coreutils

Requires: efi-srpm-macros
Requires: fonts-srpm-macros
# ↓ Provides macros.forge and forge.lua originally shipped by us
Requires: forge-srpm-macros
Requires: go-srpm-macros
# ↓ Provides kmod.attr originally shipped by us
Requires: kernel-srpm-macros >= 1.0-12
Requires: lua-srpm-macros
Requires: ocaml-srpm-macros
Requires: openblas-srpm-macros
Requires: perl-srpm-macros
# ↓ Has Python BRPs originaly present in redhat-rpm-config
Requires: python-srpm-macros >= 3.11-7
Requires: qt6-srpm-macros
Requires: rust-srpm-macros
Requires: package-notes-srpm-macros
Requires: pyproject-srpm-macros
# ↓ Create compat Provides/Requires when things move around in filesystem
Requires: filesystem-srpm-macros

%if ! 0%{?rhel}
Requires: ansible-srpm-macros
Requires: fpc-srpm-macros
Requires: ghc-srpm-macros
Requires: gnat-srpm-macros
Requires: tree-sitter-srpm-macros
Requires: qt5-srpm-macros
Requires: zig-srpm-macros
Requires: build-reproducibility-srpm-macros
%endif

Requires: rpm >= 4.19.91
Requires: dwz >= 0.4
Requires: zip
Requires: (annobin-plugin-gcc if gcc)
Requires: (gcc-plugin-annobin if gcc)

# for brp-mangle-shebangs
Requires: %{_bindir}/find
Requires: %{_bindir}/file
Requires: %{_bindir}/grep
Requires: %{_bindir}/sed
Requires: %{_bindir}/xargs

# -fstack-clash-protection and -fcf-protection require GCC 8.
Conflicts: gcc < 8.0.1-0.22

# Replaced by macros.rpmautospec shipped by us
Obsoletes: rpmautospec-rpm-macros < 0.6.3-2

Provides: system-rpm-config = %{version}-%{release}

%global rrcdir /usr/lib/rpm/redhat

%description
Red Hat specific rpm configuration files.

%prep
# Not strictly necessary but allows working on file names instead
# of source numbers in install section
%setup -c -T
cp -p %{sources} .

%install
mkdir -p %{buildroot}%{rrcdir}
install -p -m 644 -t %{buildroot}%{rrcdir} macros rpmrc
install -p -m 444 -t %{buildroot}%{rrcdir} redhat-hardened-*
install -p -m 444 -t %{buildroot}%{rrcdir} redhat-annobin-*
install -p -m 755 -t %{buildroot}%{rrcdir} config.*
install -p -m 755 -t %{buildroot}%{rrcdir} dist.sh
install -p -m 755 -t %{buildroot}%{rrcdir} gpgverify
install -p -m 755 -t %{buildroot}%{rrcdir} brp-*

install -p -m 755 -t %{buildroot}%{rrcdir} find-*
mkdir -p %{buildroot}%{rrcdir}/find-provides.d

install -p -m 755 -t %{buildroot}%{rrcdir} brp-*

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -p -m 644 -t %{buildroot}%{_rpmconfigdir}/macros.d macros.*

mkdir -p %{buildroot}%{_fileattrsdir}
install -p -m 644 -t %{buildroot}%{_fileattrsdir} *.attr

mkdir -p %{buildroot}%{_rpmluadir}/fedora/{rpm,srpm}
install -p -m 644 -t %{buildroot}%{_rpmluadir}/fedora common.lua

# This trigger is used to decide which version of the annobin plugin for gcc
# should be used.  See comments in the script for full details.
#
# Note - whilst "gcc-plugin-annobin" requires "gcc" and hence in theory we
# do not need to trigger on "gcc", the redhat-annobin-plugin-select.sh
# script invokes gcc to determine the version of the gcc plugin, and this
# can be significant.
#
# For example, suppose that version N of gcc is installed and that annobin
# version A (built by gcc version N) is also installed.  Then a new version
# of gcc is released.  If the rpms are updated in this order:
#   gcc-plugin-annobin
#   gcc
# then when the trigger for gcc-plugin-annobin is run, the script will see
# (the not yet updated) gcc is currently version N, which matches the current
# annobin plugin A, so no changes are necessary.  Then gcc is updated and,
# if the trigger below did not include "gcc", the script would not run again
# and so now you would have an out of date version of the annobin plugin.
#
# Alternatively imagine installing gcc and annobin for the first time.
# If the installation order is:
#    gcc
#    annobin-plugin-gcc
#    gcc-plugin-annobin
# then the installation of gcc will not cause the gcc-plugin-annobin to be
# selected, since it does not exist yet.  Then annobin-plugin-gcc is installed
# and since it is the only plugin, it will be selected.  Then
# gcc-plugin-annobin is installed, and if the trigger below was not set to
# run on gcc-plugin-annobin, it would pass unnoticed.
#
# Hence it is necessary to trigger on both gcc and gcc-plugin-annobin.

%triggerin -- annobin-plugin-gcc gcc-plugin-annobin gcc
%{rrcdir}/redhat-annobin-plugin-select.sh
%end

# We also trigger when an annobin plugin is uninstalled.  This allows us to
# switch over to the other version of the plugin.  Note - we do not bother
# triggering on the uninstallation of "gcc", since if that is removed, the
# plugins are rendered useless.

%triggerpostun -- annobin-plugin-gcc gcc-plugin-annobin
%{rrcdir}/redhat-annobin-plugin-select.sh
%end

%files
%dir %{rrcdir}
%{rrcdir}/brp-ldconfig
%{rrcdir}/brp-mangle-shebangs
%{rrcdir}/brp-strip-lto
%{rrcdir}/config.*
%{rrcdir}/dist.sh
%{rrcdir}/find-provides
%{rrcdir}/find-requires
%{rrcdir}/gpgverify
%{rrcdir}/macros
%{rrcdir}/redhat-hardened-*
%{rrcdir}/rpmrc
%{_fileattrsdir}/*.attr
%{_rpmconfigdir}/macros.d/macros.*-srpm
%{_rpmconfigdir}/macros.d/macros.build-constraints
%{_rpmconfigdir}/macros.d/macros.dwz
%{_rpmconfigdir}/macros.d/macros.fedora-misc
%{_rpmconfigdir}/macros.d/macros.ldconfig
%{_rpmconfigdir}/macros.d/macros.rpmautospec
%{_rpmconfigdir}/macros.d/macros.shell-completions
%{_rpmconfigdir}/macros.d/macros.vpath
%dir %{_rpmluadir}/fedora
%dir %{_rpmluadir}/fedora/srpm
%dir %{_rpmluadir}/fedora/rpm
%{_rpmluadir}/fedora/*.lua

%attr(0755,-,-) %{rrcdir}/redhat-annobin-plugin-select.sh
%verify(owner group mode) %{rrcdir}/redhat-annobin-cc1
%{rrcdir}/redhat-annobin-select-gcc-built-plugin
%{rrcdir}/redhat-annobin-select-annobin-built-plugin

%doc buildflags.md

%changelog
%autochangelog
