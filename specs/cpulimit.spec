%global commit f4d2682804931e7aea02a869137344bb5452a3cd
%global build_date 20151118

%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global posttag %{build_date}git%{shortcommit}

Name:		cpulimit
Summary:	CPU Usage Limiter for Linux

# The main program sources are GPLv2+.
# There is one file, "src/memrchr.c", under the MIT license;
# however, that is used only for macOS builds.
License:	GPL-2.0-or-later

Epoch:		1
Version:	0.2^%{posttag}
Release:	1%{?dist}

URL:		https://github.com/opsengine/cpulimit
Source0:	https://github.com/opsengine/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

Patch0:		0000-fix-includes.patch
Patch1:		0001-incompatible-pointer-type.patch

BuildRequires:  gcc
BuildRequires:  make

%description
cpulimit is a simple program which attempts to limit the CPU usage of a process
(expressed in percentage, not in CPU time). This is useful to control batch
jobs, when you don't want them to eat too much CPU. It does not act on the nice
value or other scheduling priority stuff, but on the real CPU usage. Also, it
is able to adapt itself to the overall system load, dynamically and quickly.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%make_build

%install
install -Dp -m 755 src/cpulimit %{buildroot}/%{_bindir}/cpulimit

%files
%{_bindir}/cpulimit
%doc README.md
%license LICENSE

%changelog
* Thu Jan 16 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:0.2^20151118gitf4d2682-1
- Fix build failure

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-24.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.2-23.20151118gitf4d2682
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-22.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-21.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-20.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-19.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-18.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-17.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-16.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-15.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-14.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1:0.2-13.20151118gitf4d2682
- Add a patch to fix build failures
- Respect Fedora's CFLAGS
- Bring the spec up-to-date with current packaging guidelines

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-12.20151118gitf4d2682
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-11.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-10.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-9.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-8.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-7.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-6.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-5.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-4.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-3.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2-2.20151118gitf4d2682
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Christos Triantafyllidis <christos.triantafyllidis@gmail.com> - 1:0.2-1.20151118gitf4d2682
- Updated to version 0.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.1-3.20140722gitcabeb99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.1-2.20140722gitcabeb99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Christos Triantafyllidis <christos.triantafyllidis@gmail.com> - 1:0.1-1.20140722gitcabeb99
- Rebuild based on the github sources

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 07 2011 Christos Triantafyllidis <christos.triantafyllidis@gmail.com> 1.1-1
- initial package creation
