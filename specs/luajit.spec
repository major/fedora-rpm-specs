%global pkgname LuaJIT

%global luajit_version_major 2
%global luajit_version_minor 1
%global luajit_version_patch 1744318430
%global luajit_version %{luajit_version_major}.%{luajit_version_minor}.%{luajit_version_patch}


Name:           luajit
Version:        %{luajit_version}
%global apiver %(v=%{version}; echo ${v%.${v#[0-9].[0-9].}})
Release:        %autorelease
Summary:        Just-In-Time Compiler for Lua
License:        MIT
URL:            http://luajit.org
# LuaJIT is a rolling release, see http://luajit.org/status.html
# To update the tarball you can use the update_tarball.sh script
Source0:        https://github.com/LuaJIT/LuaJIT/archive/refs/heads/v2.1/%{pkgname}-%{version}.tar.gz
Source1:        https://github.com/LuaJIT/LuaJIT-test-cleanup/archive/refs/heads/master/LuaJIT-test-cleanup.tar.gz
Source2:        update_tarball.sh

# Add 'make check'
Patch0: luajit-2.1-make-check.patch
# Patches from https://github.com/cryptomilk/LuaJIT/commits/v2.1-fedora
# git format-patch --stdout -l1 --no-renames origin/v2.1..v2.1-fedora > luajit-2.1-fedora.patch
Patch1: luajit-2.1-fedora.patch
# If the patch doesn't apply, send a mail to:
# Ilya Leoshkevich <iii@de.ibm.com> or Andreas.Krebbel@de.ibm.com
# https://bugzilla.redhat.com/show_bug.cgi?id=2222911
Patch2: https://github.com/luajit/luajit/pull/631.patch#/luajit-2.1-s390x-support.patch

ExcludeArch:    riscv64 ppc64 ppc64le

BuildRequires:  gcc
BuildRequires:  make

%description
LuaJIT implements the full set of language features defined by Lua 5.1.
The virtual machine (VM) is API- and ABI-compatible to the standard
Lua interpreter and can be deployed as a drop-in replacement.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
%autosetup -p1 -n %{pkgname}-%{luajit_version_major}.%{luajit_version_minor} -a1

echo "%{luajit_version_patch}" > .relver

ln -s LuaJIT-test-cleanup-master/bench bench
ln -s LuaJIT-test-cleanup-master/test test

# Enable Lua 5.2 features
sed -i -e '/-DLUAJIT_ENABLE_LUA52COMPAT/s/^#//' src/Makefile

# preserve timestamps (cicku)
sed -i -e '/install -m/s/-m/-p -m/' Makefile


%build
# Q= - enable verbose output
# E= @: - disable @echo messages
# NOTE: we use amalgamated build as per documentation suggestion doc/install.html
make amalg Q= E=@: PREFIX=%{_prefix} TARGET_STRIP=: \
           CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" \
           MULTILIB=%{_lib} \
           %{?_smp_mflags}

%install
# PREREL= - disable -betaX suffix
# INSTALL_TNAME - executable name
%make_install PREFIX=%{_prefix} \
              MULTILIB=%{_lib}

rm -rf _tmp_html ; mkdir _tmp_html
cp -a doc _tmp_html/html

# Remove static .a
find %{buildroot} -type f -name *.a -delete -print

%ldconfig_scriptlets

%check
make check

%files
%license COPYRIGHT
%doc README
%{_bindir}/%{name}
%{_bindir}/%{name}-%{luajit_version}
%{_libdir}/lib%{name}-*.so.*
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}-%{luajit_version_major}.%{luajit_version_minor}/

%files devel
%doc _tmp_html/html/
%{_includedir}/%{name}-%{apiver}/
%{_libdir}/lib%{name}-*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
