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
Source1: bamboo.xml
Source2: us.xml
Source3: others.xml
# Bug 2402676
Patch1:  %{name}-2402676-del-attr-none.patch
# Bug 2430316 to make engine-* sub packages
Patch2:  %{name}-2430316-engine-xml.patch

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
Requires:       gtk3
Requires:       ibus
Requires:       %{name}-engine-vi-us = %{version}-%{release}

%description
A Vietnamese IME for IBus using Bamboo Engine.
The open source Vietnamese keyboard supports most common encodings, popular
Vietnamese typing methods, smart diacritics, spell checking, shortcuts,...

%description -l vi
A Vietnamese IME for IBus using Bamboo Engine.
Bộ gõ tiếng Việt mã nguồn mở hỗ trợ hầu hết các bảng mã thông dụng, các kiểu
gõ tiếng Việt phổ biến, bỏ dấu thông minh, kiểm tra chính tả, gõ tắt,...

%package engine-vi-us
Summary:        Vietnamese input method US layout engines of ibus-bamboo
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description engine-vi-us
This includes Vietnamese input-method engines with the Vietnamese language and
the US keyboard layout of %{name}

%package engine-others
Summary:        Miscellaneous Vietnamese input method engines of ibus-bamboo
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description engine-others
This includes Vietnamese input-method engines with the Vietnamese language and
the default keyboard layout, and the English language and the US keyboard
layout except for %{name}-engine-vi-us

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

diff %SOURCE1 ${RPM_BUILD_ROOT}%{_datadir}/ibus/component/bamboo.xml || :
install -pm 644 -D %SOURCE1 ${RPM_BUILD_ROOT}%{_datadir}/ibus/component/bamboo.xml
install -m 755 -d ${RPM_BUILD_ROOT}%{_datadir}/%{name}/engines
install -pm 644 -D %SOURCE2 ${RPM_BUILD_ROOT}%{_datadir}/%{name}/engines/us.xml
install -pm 644 -D %SOURCE3 ${RPM_BUILD_ROOT}%{_datadir}/%{name}/engines/others.xml


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

%transfiletriggerin engine-vi-us -- %{_datadir}/%{name}/engines
[ -x %{_bindir}/ibus ] && \
  %{_bindir}/ibus write-cache --system &>/dev/null || :

%transfiletriggerpostun engine-vi-us -- %{_datadir}/%{name}/engines
[ -x %{_bindir}/ibus ] && \
  %{_bindir}/ibus write-cache --system &>/dev/null || :

%transfiletriggerin engine-others -- %{_datadir}/%{name}/engines
[ -x %{_bindir}/ibus ] && \
  %{_bindir}/ibus write-cache --system &>/dev/null || :

%transfiletriggerpostun engine-others -- %{_datadir}/%{name}/engines
[ -x %{_bindir}/ibus ] && \
  %{_bindir}/ibus write-cache --system &>/dev/null || :

%files
%doc README.md
%license LICENSE data/COPYING.emojione data/LICENSE.vietnamese.cm.dict
%{_datadir}/applications/ibus-setup-Bamboo.desktop
%{_datadir}/ibus/component/bamboo.xml
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/engines
%{_datadir}/%{name}/data
%{_datadir}/%{name}/icons
%{_libexecdir}/ibus-engine-bamboo

%files engine-vi-us
%{_datadir}/%{name}/engines/us.xml

%files engine-others
%{_datadir}/%{name}/engines/others.xml

%changelog
%autochangelog
