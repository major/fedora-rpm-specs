%global source_version %%(echo "%version" | tr '~' '-')
%global main_version %%(echo "%version" | sed -e 's/~.*//')
%global debug_package %{nil}

# go tool link --help
%global _build_go_ldflags -ldflags '-w -s -X main.Version=%{main_version}'
# go help build
# Fix rpmlint 'position-independent-executable-suggested'
%global build_goflags %{?build_goflags}%{!?build_goflags:%_build_go_ldflags -trimpath -buildmode=pie}

Name: ibus-bamboo
Version: 0.8.4~RC6
Release: %autorelease
Summary: A Vietnamese input method for IBus
# Bamboo files are under GPL-3.0-or-later license.
# emojione.json file is under MIT license.
License: GPL-3.0-or-later and MIT
URL: https://github.com/BambooEngine/ibus-bamboo
Source0: https://github.com/BambooEngine/%{name}/archive/refs/tags/v%{source_version}.tar.gz#/%{name}-%{source_version}.tar.gz
# Bug 2402676
Patch1:  %{name}-2402676-del-attr-none.patch

# Required by desktop-file-install
BuildRequires: desktop-file-utils
# Required by glib-compile-resources
BuildRequires: glib2-devel
BuildRequires: gcc
BuildRequires: go
# Required by ui/keyboard-shortcut-editor
BuildRequires: gtk3-devel
# Required by vendor/github.com/BambooEngine/goibus/ibus/common.go
BuildRequires: ibus-devel
# Required by x11_clipboard.c
BuildRequires: libX11-devel
# xTestFakeKeyEventIM option & Required by x11_keyboard.c
BuildRequires: libXtst-devel
Requires: gtk3
Requires: ibus

%description
A Vietnamese IME for IBus using Bamboo Engine.
The open source Vietnamese keyboard supports most common encodings, popular
Vietnamese typing methods, smart diacritics, spell checking, shortcuts,...

%description -l vi
A Vietnamese IME for IBus using Bamboo Engine.
Bộ gõ tiếng Việt mã nguồn mở hỗ trợ hầu hết các bảng mã thông dụng, các kiểu
gõ tiếng Việt phổ biến, bỏ dấu thông minh, kiểm tra chính tả, gõ tắt,...

%prep
%autosetup -n %{name}-%{source_version}
for data in data/bamboo.xml data/ibus-setup-Bamboo.desktop
do
    sed -i.orig -s "s|/lib/ibus-bamboo/|/libexec/|" $data
done

%build
GOLDFLAGS="${GOLDFLAGS:-%{?build_goflags}}"
%{make_build} GOLDFLAGS="$GOLDFLAGS"

%install
# FIXME: `make install` runs `make build` again.
GOLDFLAGS="${GOLDFLAGS:-%{?build_goflags}}"
%{make_install} GOLDFLAGS="$GOLDFLAGS"

desktop-file-install --delete-original          \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/*

mv ${RPM_BUILD_ROOT}%{_prefix}/lib/%{name} ${RPM_BUILD_ROOT}%{_libexecdir}

# Should be in %%license instead
rm ${RPM_BUILD_ROOT}%{_datadir}/%{name}/data/COPYING.emojione
rm ${RPM_BUILD_ROOT}%{_datadir}/%{name}/data/LICENSE.vietnamese.cm.dict
# Should be in %%{_datadir}/ibus/component instead.
rm ${RPM_BUILD_ROOT}%{_datadir}/%{name}/data/bamboo.xml*
# No need the build file.
rm ${RPM_BUILD_ROOT}%{_datadir}/%{name}/data/ibus-bamboo.spec
# Should be in %%{_datadir}/applications instead.
rm ${RPM_BUILD_ROOT}%{_datadir}/%{name}/data/ibus-setup-Bamboo.desktop*


%check
#`make t` accesses the github.com
CGO_ENABLED=1 go test ./... -mod=vendor
CGO_ENABLED=1 go test ./vendor/github.com/BambooEngine/bamboo-core/... -mod=vendor

%transfiletriggerin -- %{_datadir}/ibus/component
[ -x %{_bindir}/ibus ] && \
  %{_bindir}/ibus write-cache --system &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/ibus/component
[ -x %{_bindir}/ibus ] && \
  %{_bindir}/ibus write-cache --system &>/dev/null || :

%files
%doc README.md
%license LICENSE data/COPYING.emojione data/LICENSE.vietnamese.cm.dict
%{_datadir}/applications/ibus-setup-Bamboo.desktop
%{_datadir}/ibus/component/bamboo.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_libexecdir}/ibus-engine-bamboo

%changelog
%autochangelog
