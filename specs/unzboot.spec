%global commit 3ccaa1acbd1e092787fa488d046bdcb3762e51ee
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20250530

Name:       unzboot
Version:    0.1~git.%{commitdate}.%{shortcommit}
Release:    2%{?dist}

Summary:    Extracts a kernel vmlinuz image from a EFI application
License:    GPL-2.0-or-later

URL:        https://github.com/eballetbo/unzboot
# Upstream is still under development so they are not tagging releases
# yet. Use the following to do a rebase to a new snapshot:
#
# git archive --format=tar --prefix=${name}-${shortcommit}/ ${shortcommit} | xz > ${name}-${shortcommit}.tar.xz
Source0:       %{name}-%{shortcommit}.tar.xz

BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: meson
BuildRequires: zlib
BuildRequires: libzstd-devel

%description
The unzboot program extracts a kernel vmlinuz image from
a EFI application that carries the actual kernel image in
compressed form.

%prep
%autosetup -n %{name}-%{shortcommit}
%build
%meson
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%license LICENSE
%{_bindir}/unzboot

%changelog
* Wed Sep 24 2025 Enric Balletbo i Serra <eballetbo@redhat.com> - 0.1~git.20250530.3ccaa1a-1
- Check for g_malloc failure in unpack_efi_zboot_image
- EFI zboot payload offset and size validation
- Correct and simplify output file writing logic in main
- Direct gunzip error messages to stderr
- Improve ZSTD decompression error handling and reporting
- Suppress unused parameter warnings in zalloc/zfree
- Initialize z_stream in gunzip to prevent uninitialized use
- Prevent memory leak in gunzip on inflateInit2 failure
- Allow output to stdout to provide greater flexibility
- Refactor output file writing in unzboot
- Add SPDX license identifier and simplify license header
- Add EFI application with zstd compression example
- Append to the name the type of compression

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~git.20250502.0c0c3ad-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon May 5 2025 Enric Balletbo i Serra <eballetbo@redhat.com> -  0.1~git.20250502.0c0c3ad-1
- Add zstd compressed kernel support
- Introduce test case infrastructure and add gunzip tests

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~git.20240903.374ec24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 03 2024 Enric Balletbo i Serra <eballetbo@redhat.com> - 0.1~git.20240903.374ec24-1
- Add support for RISC-V header + some documentation fixes

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~git.20230318.3285b55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~git.20230318.3285b55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~git.20230318.3285b55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 18 2023 Enric Balletbo i Serra <eballetbo@redhat.com> - 0.1~git.20230318.3285b55-1
- initial unzboot spec
