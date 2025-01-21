Name:       smatch
Version:    1.73
Release:    6%{?dist}
Summary:    A static analyzer for C

# License breakdown:
# - Smatch itself is GPL-2.0-or-later
# - Sparse is MIT
# - cwchash is BSD-3-clause
License:    GPL-2.0-or-later AND MIT AND BSD-3-Clause
URL:        https://%{name}.sourceforge.net

# Upstream is https://repo.or.cz/w/smatch.git, but it does not allow an easy
# download of tarballs so we use an official GitHub mirror instead.
Source0:    https://github.com/error27/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:     do-not-build-sparse-binaries.patch
# TODO: Try to upstream these patches.
Patch1:     fix-datadir-path.patch
Patch2:     use-distribution-ldflags.patch
Patch3:     preserve-install-timestamps.patch
# TODO: File an issue upstream about the missing license.
Patch4:     add-BSD-3-license.patch
Patch5:     fix-gcc14-compilation-errors.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: sqlite-devel

Requires: %{name}-data = %{version}-%{release}

Provides: bundled(cwchash)
Provides: bundled(sparse)

%description
Smatch is a static analysis tool for C.

%package data
Summary: Data for Smatch the C static analyzer
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description data
Data for Smatch the static analysis tool for C.

%prep
%autosetup

%build
%if 0%{?rhel}
%set_build_flags
export CFLAGS="-std=gnu99 $CFLAGS"
%endif

%make_build PREFIX='%{_prefix}'

%install
%make_install PREFIX='%{_prefix}'

%check
echo "int main(void) { int a; return a; }" > test.c
./smatch test.c > out
grep "test.c:1 main() error: uninitialized symbol 'a'." out

%files
%doc README Documentation/{arm64-detecting-tagged-addresses,smatch}.txt
%license GPL-2 LICENSE
%{_bindir}/%{name}

%files data
%{_datadir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.73-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.73-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.73-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Lukáš Zaoral <lzaoral@redhat.com> - 1.73-3
- fix compilation with GCC 14 (rhbz#2259190)

* Tue Aug 15 2023 Lukáš Zaoral <lzaoral@redhat.com> - 1.73-2
- drop %%{?isa} for a noarch package

* Tue Aug 15 2023 Lukáš Zaoral <lzaoral@redhat.com> - 1.73-1
- Initial import
