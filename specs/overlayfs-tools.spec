%global date 20200817
%global commit 77bf3f7ad3e7b834a15e2166780167646d51cce8
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary: OverlayFS layers manipulation tools
Name: overlayfs-tools
Version: 0
Release: 0.11.%{date}git%{shortcommit}%{?dist}
URL: https://github.com/kmxz/overlayfs-tools/
Source0: %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# https://github.com/kmxz/overlayfs-tools/issues/14
Patch0: %{name}-missing-errno-h.patch
# https://patch-diff.githubusercontent.com/raw/kmxz/overlayfs-tools/pull/13
Patch1: https://patch-diff.githubusercontent.com/raw/kmxz/overlayfs-tools/pull/13.diff
License: WTFPL
BuildRequires: gcc
BuildRequires: help2man
BuildRequires: libattr-devel
BuildRequires: make

%description
OverlayFS is the union filesystem provided by Linux kernel.

This program comes provides three tools:

* vacuum - remove duplicated files in upperdir where copy_up is done but the
  file is not actually modified (see the sentence "the copy_up may turn out to
  be unnecessary" in the Linux documentation). This may reduce the size of
  upperdir without changing lowerdir or overlay.
* diff - show the list of actually changed files (the difference between overlay
  and lowerdir). A file with its type changed (i.e. from symbolic link to
  regular file) will shown as deleted then added, rather than modified.
  Similarly, for a opaque directory in upperdir, the corresponding directory in
  lowerdir (if exists) will be shown as entirely deleted, and a new directory
  with the same name added. File permission/owner changes will be simply shown
  as modified.
* merge - merge down the changes from upperdir to lowerdir. Unlike aubrsync for
  AuFS which bypasses the union filesystem mechanism, overlayfs-utils emulates
  the OverlayFS logic, which will be far more efficient. After this operation,
  upperdir will be empty and lowerdir will be the same as original overlay.
* deref - copy changes from upperdir to uppernew while unfolding redirect
  directories and metacopy regular files, so that new upperdir is compatible
  with legacy overlayfs driver.

For safety reasons, vacuum and merge will not actually modify the filesystem,
but generate a shell script to do the changes instead.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%set_build_flags
%make_build CFLAGS="$CFLAGS" LFLAGS="$LDFLAGS"
help2man --no-info --version-string=%{shortcommit} --output=overlay.1 ./overlay

%install
install -dm755 %{buildroot}%{_bindir}
install -pm755 overlay %{buildroot}%{_bindir}
install -dm755 %{buildroot}%{_mandir}/man1
install -pm644 overlay.1 %{buildroot}%{_mandir}/man1

#%%check
# TODO: testsuite calls sudo

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/overlay
%{_mandir}/man1/overlay.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20200817git77bf3f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20200817git77bf3f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20200817git77bf3f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20200817git77bf3f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20200817git77bf3f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20200817git77bf3f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20200817git77bf3f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20200817git77bf3f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20200817git77bf3f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 10 2021 Dominik Mierzejewski <rpm@greysector.net> 0-0.2.20200817git77bf3f7
- add link to upstream issue for errno fix
- fix %%s appearing in help message instead of program name
- generate manpage with help2man and include it

* Thu Jan 14 2021 Dominik Mierzejewski <rpm@greysector.net> 0-0.1.20200817git77bf3f7
- initial build
