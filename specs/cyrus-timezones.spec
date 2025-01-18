%global git_commit 4f795aeba2d9ee52f82e8666d55f6a469576dfa0
%global git_date 20200903

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Summary:  Timezone information for the Cyrus IMAP Server
Name: cyrus-timezones
Version:  %{git_date}
Release: 12.%{git_suffix}%{dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Group: Applications/Internet
URL: https://github.com/cyrusimap/cyrus-timezones
Source0: https://github.com/cyrusimap/%{name}/archive/%{git_commit}/%{name}-%{version}.tar.gz

BuildRequires: autoconf, automake, libtool
BuildRequires: libical-devel
BuildRequires: glib2-devel
BuildRequires: chrpath
BuildRequires: make

%description
%{summary}

%package devel
Summary: Package config configuration for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconf-pkg-config

%description devel
%{summary}

%prep
%autosetup -p1 -n %{name}-%{git_commit}
autoreconf -i --verbose  --warnings=all

%build
%configure
%make_build

%install
%make_install 
chrpath -d %{buildroot}/%{_bindir}/cyr_vzic

%files
%doc AUTHORS README MAINTAINER_NOTES
%license COPYING
%{_datadir}/%{name}
%{_bindir}/cyr_vzic

%files devel
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20200903-12.20200903git4f795aeb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 20200903-11.20200903git4f795aeb
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200903-10.20200903git4f795aeb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200903-9.20200903git4f795aeb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200903-8.20200903git4f795aeb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20200903-7.20200903git4f795aeb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20200903-6.20200903git4f795aeb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200903-5.20200903git4f795aeb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200903-4.20200903git4f795aeb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200903-3.20200903git4f795aeb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20200903-2.20200903git4f795aeb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild


* Thu Sep 03 2020  Pavel Zhukov <pzhukov@redhat.com> - 20200903-1.20200903git4f795aeb
- Do not use deprecated macroses

* Mon Aug 31 2020 Pavel Zhukov <pzhukov@redhat,com> - 20200901-2.20200901git8c24df1d
- Initial build.
- Fix changelog entry format. 

