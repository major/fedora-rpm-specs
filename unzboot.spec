%global commit 3285b558529b862391d27afe098368d6f8dda09e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20230318

Name:		unzboot
Version:	0.1~git.%{commitdate}.%{shortcommit}
Release:	3%{?dist}

Summary:	Extracts a kernel vmlinuz image from a EFI application
License:	GPL-2.0-or-later

URL:            https://github.com/eballetbo/unzboot
# Upstream is still under development so they are not tagging releases
# yet. Use the following to do a rebase to a new snapshot:
#
# git archive --format=tar --prefix=${name}-${shortcommit}/ ${shortcommit} | xz > ${name}-${shortcommit}.tar.xz
Source0:       %{name}-%{shortcommit}.tar.xz

BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: meson
BuildRequires: zlib

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
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~git.20230318.3285b55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~git.20230318.3285b55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 18 2023 Enric Balletbo i Serra <eballetbo@redhat.com> - 0.1~git.20230318.3285b55-1
- initial unzboot spec
