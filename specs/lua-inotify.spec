%global luaver 5.4
%global lualibdir %{_libdir}/lua/%{luaver}

Name:           lua-inotify
Epoch:          1
Version:        0.5
Release:        12%{?dist}
Summary:        Inotify bindings for Lua

License:        MIT
URL:            http://hoelz.ro/projects/linotify
Source0:        https://github.com/hoelzro/linotify/archive/%{version}.tar.gz#/linotify-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  lua-devel >= %{luaver}
BuildRequires: make

%description
This is linotify, a binding for Linux's inotify library to Lua.


%prep
%autosetup -p1 -n linotify-%{version}
# do not strip when installing; preserve modtime (not strictly required)
sed -i.nostrip -e 's|install -D -s|install -D -p|' Makefile


%build
# original CFLAGS is computed using Lua's pkgconfig file, but ours
# does not set any.
#
# Overriding with the default %%{optflags}, and keeping the -fPIC
# from the original CFLAGS as the build target is a shared object
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC"


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_PATH=%{lualibdir}


%files
%license COPYRIGHT
%doc README.md Changes
%{lualibdir}/inotify.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 1:0.5-2
- Remove unneeded manual Requires on lua

* Mon Aug 24 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 1:0.5-1
- Upgrade to upstream's actual 0.5 release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.20.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.19.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.18.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.17.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.15.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.14.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.13.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.12.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.11.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.10.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.9.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.20130510git98822877a9d42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Tom Callaway <spot@fedoraproject.org> - 1.0-0.6.20130510git98822877a9d42
- update to latest git, rebuild for lua 5.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.20110529git6d0f7a0973cfb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.20110529git6d0f7a0973cfb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.20110529git6d0f7a0973cfb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep  8 2011 Michel Salim <salimma@fedoraproject.org> - 1.0-0.2.20110529git6d0f7a0973cfb
- add source checkout instructions
- add explanation for overriding CFLAGS

* Tue Aug 16 2011 Michel Salim <salimma@fedoraproject.org> - 1.0-0.1.20110529git6d0f7a0973cfb
- Initial package
