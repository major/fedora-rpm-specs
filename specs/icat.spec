%global repo_owner atextor
%global repo_name  icat

Name:    icat
Summary: Output images in terminal
License: BSD-2-Clause

%global git_commit 9b5aa622fdfbfbd37a97c9b8d3258100e1d26cd6
%global git_date   20230110
%global git_short  %(c="%{git_commit}"; echo "${c:0:7}")

Version: 0.5
Release: 20.%{git_date}git%{git_short}%{?dist}

URL:     https://github.com/%{repo_owner}/%{repo_name}
Source0: %{URL}/archive/%{git_commit}/%{repo_name}-%{git_commit}.tar.gz

BuildRequires: gcc
BuildRequires: imlib2-devel
BuildRequires: make

# sleuthkit provides a completely unrelated /usr/bin/icat
Conflicts: sleuthkit

%description
Outputs an image on a 256-color or 24-bit color enabled terminal
with UTF-8 locale, such as gnome-terminal, konsole or rxvt-unicode (urxvt).

%prep
%setup -q -n %{repo_name}-%{git_commit}
# Extract license from source code
awk '1;/\*\//{exit}' < icat.c > LICENSE

%build
%make_build

%install
install -m 755 -d %{buildroot}/%{_bindir}
install -m 755 ./icat %{buildroot}/%{_bindir}/icat

install -m 755 -d %{buildroot}/%{_mandir}/man1
install -m 644 ./icat.man %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/icat
%{_mandir}/man1/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-20.20230110git9b5aa62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-19.20230110git9b5aa62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-18.20230110git9b5aa62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17.20230110git9b5aa62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-16.20230110git9b5aa62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Leigh Scott <leigh123linux@gmail.com> - 0.5-15.20230110git9b5aa62
- Rebuild fo new imlib2

* Thu Jun 08 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.5-14.20230110git9b5aa62
- Add an explicit Conflicts tag against sleuthkit

* Tue Apr 18 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.5-13.20230110git9b5aa62
- Update to latest git snapshot (2023-01-10)
- Fix man page having the executable permission bit set
- Convert License tag to SPDX

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Artur Iwicki <fedora@svgames.pl> - 0.5.3
- Add %%set_build_flags to %%build
- Use %%make_build instead of "make %%{?_smp_flags}"
- Add gcc to BuildRequires

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Artur Iwicki <fedora@svgames.pl> - 0.5-1
- Update to new upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5.20171026.git.74b4a1b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Artur Iwicki <fedora@svgames.pl> - 0.4-4.20171016.git.74b4a1b
- Fix manpage being installed with a wrong filename
- Create macros to make marking the release snapshot easier

* Tue Nov 07 2017 Artur Iwicki <fedora@svgames.pl> - 0.4-3.20171016.git.74b4a1b
- Update to latest upstream snapshot
- Specify CFLAGS when calling make, instead of patching the Makefile
- Add manpage to package

* Wed Oct 18 2017 Artur Iwicki <fedora@svgames.pl> - 0.4-2
- Modify Makefile to ensure debuginfo is generated

* Tue Oct 17 2017 Artur Iwicki <fedora@svgames.pl> - 0.4-1
- Initial packaging
