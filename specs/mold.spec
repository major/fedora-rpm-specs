%bcond check 1

# Prevent `gdb-add-index` from failing with `std::bad_alloc` on i386
%ifarch %{ix86}
%global rustflags_debuginfo 1
%endif

Name:           mold
Version:        3.0.0
Release:        %autorelease
Summary:        A Modern Linker

%global forgeurl https://github.com/rui314/%{name}
%global tag      v%{version}
%forgemeta

SourceLicense:  MIT
License:        %{shrink:
    MIT AND
    (Apache-2.0 OR Apache-2.0 WITH LLVM-exception) AND
    (Apache-2.0 OR MIT) AND
    BSL-1.0 AND
    (MIT OR Apache-2.0) AND
    (MIT-0 OR Apache-2.0) AND
    (Unlicense OR MIT) AND
    Zlib
}
# `LICENSE.dependencies` contains a full license breakdown
URL:            %{forgeurl}
Source:         %{forgesource}

# Upstream commit 4520bf5cbbcdfc64d8a1d71aae098cab58af5909
Patch:          0001-Update-cpp_demangle-to-0.5.1.patch
# Adjust crate dependencies: relax uuid version, use mimalloc from crates.io
Patch:          0002-Adjust-dependencies-for-Fedora-Linux.patch

BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc

# The following packages are only required for executing the tests
%if %{with check}
BuildRequires:  binutils-devel
BuildRequires:  clang
BuildRequires:  gdb
BuildRequires:  gcc-c++
BuildRequires:  glibc-static
%ifarch x86_64
%if 0%{?fedora}
# Koji 64-bit buildroots do not contain packages from 32-bit builds, therefore
# the 'glibc-devel.i686' variant is provided as 'glibc32'.
BuildRequires: (glibc32 or glibc-devel(%__isa_name-32))
%endif
%endif
BuildRequires:  libdwarf-tools
BuildRequires:  libstdc++-static
BuildRequires:  llvm
BuildRequires:  perl-interpreter
%endif

Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description
mold is a faster drop-in replacement for existing Unix linkers.
It is several times faster than the LLVM lld linker.
mold is designed to increase developer productivity by reducing
build time, especially in rapid debug-edit-rebuild cycles.

%prep
%forgeautosetup -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
# Set `MOLD_LIBDIR` in the build, check and install steps so `mold-wrapper.so`
# is installed to (and searched in) the correct directory. This can be dropped
# when packaging the next release.
MOLD_LIBDIR="%{_libdir}" %cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
DESTDIR="%{buildroot}" PREFIX="%{_prefix}" MOLD_LIBDIR="%{_libdir}" \
  ./install-mold.sh
# `LICENSE` is shipped via `%%license`
rm -r "%{buildroot}%{_docdir}/mold"
touch %{buildroot}%{_bindir}/ld

%if %{with check}
%check
MOLD_LIBDIR="%{_libdir}" %cargo_test
# Print skipped tests
(cd target/rpm/mold-test/out/test/results &&
  grep --files-with-matches --line-regexp skip */*.status) || :
%endif

%post
if [ "$1" = 1 ]; then
  update-alternatives --install %{_bindir}/ld ld %{_bindir}/ld.mold 1
fi

%postun
if [ "$1" = 0 ]; then
  update-alternatives --remove ld %{_bindir}/ld.mold
fi

%files
%license LICENSE LICENSE.dependencies
%doc README.md
%ghost %{_bindir}/ld
%{_bindir}/mold
%{_bindir}/ld.mold
%{_libdir}/mold/
%{_libexecdir}/mold/
%{_mandir}/man1/ld.mold.1*
%{_mandir}/man1/mold.1*

%changelog
%autochangelog
